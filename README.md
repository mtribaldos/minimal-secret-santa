# minimal-secret-santa

[![Build Status](https://travis-ci.org/mtribaldos/minimal-secret-santa.svg)](https://travis-ci.org/mtribaldos/minimal-secret-santa)

Minimal secret santa application in a few lines of Python.

## Installation

```shell
git clone https://github.com/mtribaldos/minimal-secret-santa
cd minimal-secret-santa
sudo python setup.py install
```

Create a YAML configuration file as specified in [this test setup](test/config.yaml).

## Usage

```shell
export MAIL_SMTP_LOGIN=...
export MAIL_SMTP_PASSWD=...

./minimal-secret-santa <config_file>
```



