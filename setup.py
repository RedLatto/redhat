
# -*- coding: utf-8 -*-

setup(
    name='Tuxedosam',
    version="2.1",
    packages=find_packages(),
    author="Trey",
    author_email="flawedmx@protonmail.com",
    install_requires=["termcolor","bs4","httpx","trio","tqdm","colorama"],
    description="Tuxedosam allows you to check if the mail is used on different sites like twitter, instagram , snapchat and will retrieve information on sites with the forgotten password function.",
    include_package_data=True,
    url='https://github.com/RedLatto/tuxedosam',
    entry_points = {'console_scripts': ['RedLatto = RedLatto.core:main']},
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
