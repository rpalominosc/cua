from setuptools import setup, Extension

# Define the extension module with custom CFLAGS
module = Extension(
    'cua2024.py',
    sources=['cua2024.py'],
    extra_compile_args=['-I/usr/include/mysql', '-L/usr/lib/x86_64-linux-gnu', '-lmysqlclient']
)

setup(
    name='cua2024',
    version='1.0',
    description='cua2024 custom MySQL CFLAGS',
    ext_modules=[module]
)