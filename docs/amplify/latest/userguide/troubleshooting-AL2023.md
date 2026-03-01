# Troubleshooting Amazon Linux 2023 build image issues

The following information can help you troubleshoot issues with the Amazon Linux 2023
(AL2023) build image.

###### Topics

- [I want to run Amplify functions with the Python runtime](#python-runtime "#python-runtime")
- [I want to run commands that require superuser or root privileges](#root-privileges "#root-privileges")

## I want to run Amplify functions with the Python runtime

Amplify Hosting now uses the Amazon Linux 2023 build image by default when you deploy
a new application. AL2023 comes pre-installed with Python versions 3.8, 3.9, 3.10,
and 3.11.

For backwards compatibility with the Amazon Linux 2 image, the AL2023 build image has
symlinks for older versions of Python pre-installed.

By default, Python version 3.10 is used globally. To build your functions using a
specific Python version, run the following commands in your application's build
specification file.

```
version: 1
backend:
  phases:
    build:
      commands:
        # use a python version globally
        - pyenv global 3.11
        # verify python version
        - python --version
        # install pipenv
        - pip install --user pipenv
        # add to path
        - export PATH=$PATH:/root/.local/bin
        # verify pipenv version
        - pipenv --version
        - amplifyPush --simple
```

## I want to run commands that require superuser or root privileges

If you are using the Amazon Linux 2023 build image and get an error when running system
commands that require superuser or root privileges, you must run these commands
using the Linux `sudo` command. For example, if you get an error running
`yum install -y gcc`, use `sudo yum install -y
 gcc`.

The Amazon Linux 2 build image used the root user, but Amplify's AL2023 image runs your
code with a custom `amplify` user. Amplify grants this user privileges
to run commands using the Linux `sudo` command. It is a best practice to
use `sudo` for commands that require superuser privileges.
