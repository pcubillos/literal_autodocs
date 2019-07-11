# Copyright (c) 2019 Patricio Cubillos and contributors.
# literal_autodocs is open-source software under GNU GPL3 license (see LICENSE).

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


def rst_docs(module, rst_file):
    r"""
    Automated rst docs how I like it.

    Examples
    --------
    import literal_autodocs as lads

    import bibmanager as bm
    with open('auto_api.rst', 'w') as rst_file:
        rst_file.write('API\n===\n\n')
        lads.rst_docs(bm, rst_file)

    import MCcubed as mc3
    with open('mc3_api.rst', 'w') as rst_file:
        rst_file.write('API\n===\n\n')
        lads.rst_docs(mc3, rst_file)
    """
    subt = '_' * len(module.__name__)
    rst_file.write(f'\n{module.__name__}\n{subt}\n\n')
    rst_file.write(f'\n.. py:module:: {module.__name__}\n\n')
    submodules = []
    for obj_name in module.__all__:
        obj = getattr(module, obj_name)
        if inspect.isroutine(obj):
            docs = textwrap.indent(inspect.getdoc(obj), '    ')
            try:
                signature = str(inspect.signature(obj))
            except ValueError:
                signature = '(...)'
            rst_file.write(f'.. py:function:: {obj.__name__}'
                f'{signature}\n')
            rst_file.write(f'.. code-block:: pycon\n\n{docs}\n\n')
        elif inspect.isclass(obj):
            rst_file.write(f'.. py:class:: {obj.__name__}'
                f'{str(inspect.signature(obj))}\n\n')
            docs = textwrap.indent(inspect.getdoc(obj), '    ')
            rst_file.write(f'.. code-block:: pycon\n\n{docs}\n\n')
            docs = textwrap.indent(inspect.getdoc(obj.__init__), '    ')
            rst_file.write(f'  .. code-block:: pycon\n\n{docs}\n\n')
            #for mname, method in inspect.getmembers(obj):
            #    if not mname.startswith('_') and inspect.isroutine(method) \
            #       and inspect.getdoc(method) is not None:
            #        print(obj.__name__, mname)
            #        docs = textwrap.indent(inspect.getdoc(method), '    ')
            #        rst_file.write(f'  .. py:function:: {mname}'
            #            f'{str(inspect.signature(method))}\n')
            #        rst_file.write(f'  .. code-block:: pycon\n\n{docs}\n\n')
                    
        elif inspect.ismodule(obj):
            submodules.append(obj)
        else:
            rst_file.write(f'.. py:data:: {obj_name}\n')
            rst_file.write(f'.. code-block:: pycon\n\n  {repr(obj)}\n\n')

    for mod in submodules:
        rst_docs(mod, rst_file)





