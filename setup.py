import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='ecstaskspawner',
    version='0.1.0',
    author='kackyt',
    author_email='t_kaki@nextappli.com',
    description='Spawns JupyterHub single user servers in Docker containers running in AWS ECS Task',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/adacotech/ecstaskspawner',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
