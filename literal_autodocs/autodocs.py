# Copyright (c) 2019-2022 Patricio Cubillos
# literal_autodocs is open-source software under GPL3 license (see LICENSE)

__all__ = [
    'rst_docs',
]

import inspect
import textwrap


def docs(module, rst_file):
    """
    Automated docs how I like it.

    Examples
    --------
    import bibmanager as bm
    with open('api.rst', 'w') as rst_file:
        docs(bm, rst_file)
    """
    print(f'\nModule {module.__name__}')
    for obj_name in module.__all__:
        obj = getattr(module, obj_name)
        if inspect.isfunction(obj):
            print(f'Function {obj.__name__}')
        elif inspect.isclass(obj):
            print(f'Class {obj.__name__}')
        elif inspect.ismodule(obj):
            docs(obj)
        else:
            print(f'Constant: {obj_name} = {repr(obj)}')


def rst_docs(module, rst_file, pre_text=None):
    r"""
    Generate API rst docs based on the package docs.

    Parameters
    ----------
    module: A Python package or module
    rst_file: FILE
        FILE object where to write the rst docs.

    Examples
    --------
    >>> import literal_autodocs as lads
    >>> import bibmanager as bm

    >>> rst_file = 'bibm_api.rst'
    >>> pre_text = 'API\n===\n\n'
    >>> with open('bibm_api.rst', 'w') as rst_file:
    >>>     lads.rst_docs(bm, rst_file, pre_text)
    """
    indent = '    '

    if pre_text is not None:
        rst_file.write(pre_text)

    sub_title_line = '_' * len(module.__name__)
    rst_file.write(f'\n{module.__name__}\n{sub_title_line}\n\n')
    rst_file.write(f'\n.. py:module:: {module.__name__}\n\n')

    submodules = []
    if not hasattr(module, '__all__'):
        return
    for obj_name in module.__all__:
        obj = getattr(module, obj_name)

        if inspect.isroutine(obj):
            docs = textwrap.indent(inspect.getdoc(obj), indent)
            try:
                signature = str(inspect.signature(obj))
            except ValueError:
                signature = '(...)'
            rst_file.write(
                f'.. py:function:: {obj.__name__}'
                f'{signature}\n'
                f'.. code-block:: pycon\n\n{docs}\n\n'
            )

        elif inspect.isclass(obj):
            # The signature call:
            rst_file.write(
                f'.. py:class:: {obj.__name__}'
                f'{str(inspect.signature(obj))}\n\n'
            )
            # One-liner description:
            docs = textwrap.indent(inspect.getdoc(obj), 2*indent)
            rst_file.write(f'{indent}.. code-block:: pycon\n\n{docs}\n\n')
            # On __init__ call:
            docs = textwrap.indent(inspect.getdoc(obj.__init__), 2*indent)
            rst_file.write(f'\n{docs}\n\n')

            # Methods:
            for method_name, method in inspect.getmembers(obj):
                is_method = (
                    not method_name.startswith('_')
                    and inspect.isroutine(method)
                    and inspect.getdoc(method) is not None
                )
                if is_method:
                    sig = inspect.signature(method)
                    parameters = [
                        parameter
                        for pname,parameter in sig.parameters.items()
                        if pname !='self'
                    ]
                    signature = sig.replace(parameters=parameters)
                    docs = textwrap.indent(inspect.getdoc(method), 2*indent)
                    rst_file.write(
                        f'{indent}.. py:method:: {method_name}{signature}\n'
                        f'{indent}.. code-block:: pycon\n\n{docs}\n\n'
                    )

        elif inspect.ismodule(obj):
            submodules.append(obj)
        else:
            rst_file.write(f'.. py:data:: {obj_name}\n')
            rst_file.write(f'.. code-block:: pycon\n\n  {repr(obj)}\n\n')

    # Go on into each sub-module:
    for mod in submodules:
        rst_docs(mod, rst_file)


