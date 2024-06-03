from setuptools import setup, find_packages

setup(
    name='django-watchlog',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    include_package_data=True,
    license='MIT License',
    description='A simple Django package for logging metrics.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/django-watchlog',
    author='Your Name',
    author_email='your.email@example.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)