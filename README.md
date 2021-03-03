# Official AGCloud SDK for Python v4-rc

[![Latest Version](https://img.shields.io/github/release/alfagomma/gomma.svg?style=flat-square)](https://github.com/alfagomma/gomma/releases)
[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)](https://github.com/alfagomma/gomma/blob/master/LICENSE)
[![Quality Score](https://img.shields.io/scrutinizer/g/alfagomma/gomma.svg?style=flat-square)](https://scrutinizer-ci.com/g/alfagomma/gomma)
[![Total Downloads](https://img.shields.io/packagist/dt/alfagomma/gomma.svg?style=flat-square)](https://packagist.org/packages/league/gomma)

Gomma is the Alfagomma Cloud (AGCloud) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Element, H2o. You can find the latest, most up to date, documentation at our doc site, including a list of services that are supported.

## Quick Start

First, install the library and set a default region:

.. code-block:: sh

    $ pip install boto3

Next, set up credentials (in e.g. `~/.agcloud/credentials`):

.. code-block:: ini

    [default]
    agcloud_access_key_id = YOUR_KEY
    agcloud_secret_access_key = YOUR_SECRET

Then, set up a default region (in e.g. `~/.agcloud/config`):

.. code-block:: ini

    [default]
    region=us-east-1

Then, from a Python interpreter:

.. code-block:: python

    >>> import boto3
    >>> s3 = boto3.resource('s3')
    >>> for bucket in s3.buckets.all():
            print(bucket.name)

## TODO

- [ ] Element crimping table
