# coding:utf-8
from setuptools import setup, find_packages
import sys, os

version = '0.0.2'

setup(
    name='youdaofanyi',
    version=version,
    description="方便程序员在terminal翻译中英文的小工具",
    long_description="""方便程序员在terminal翻译中英文的小工具""",
    classifiers=[],
    keywords='python youdao dictionary terminal',
    author='maczhis',
    author_email='maczhis@gmail.com',
    url='https://github.com/maczhis',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'termcolor',
        'requests',

    ],
    entry_points={
        'console_scripts': [
            'youdao = youdao.youdao:main'
        ]
    },
)
