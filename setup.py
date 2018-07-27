"""
Flask-ZKPP
-------------

Extension to implement a zero knowledge password proof
to integrate with flask-login
"""
from setuptools import setup


setup(
    name='Flask-ZKPP',
    version='1.0',
    url='http://github.com/theunvarnished/Flask-ZKPP',
    license='WTFPL',
    author='Graham Thompson',
    author_email='grahamwt42@gmail.com',
    description='Extension to implement a zero knowledge password proof that integrates with flask-login',
    long_description=__doc__,
    #py_modules=['flask_zkpp'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    packages=['flask_zkpp'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'Flask-Login',
        'PyCrypto'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
