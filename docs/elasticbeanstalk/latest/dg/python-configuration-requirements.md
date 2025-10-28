# Specifying dependencies using a requirements file on Elastic Beanstalk

This topic describes how to configure you application to install other Python packages that it requires. A typical Python application has dependencies
on other third-party Python packages. With the Elastic Beanstalk Python platform, you have multiple ways to specify Python packages that your application depends
on.

## Use `pip` and `requirements.txt`

The standard tool for installing Python packages is `pip`. It has a feature that allows you to specify all the packages you need (as well
as their versions) in a single requirements file. For more information about the requirements file, see [Requirements File Format](https://pip.pypa.io/en/latest/reference/requirements-file-format/#requirements-file-format "https://pip.pypa.io/en/latest/reference/requirements-file-format/#requirements-file-format") on the pip
documentation website.

Create a file named `requirements.txt` and place it in the top-level directory of your source bundle. The following is an example
`requirements.txt` file for Django.

```
Django==2.2
mysqlclient==2.0.3
```

In your development environment, you can use the `pip freeze` command to generate your requirements file.

```
~/my-app$ `pip freeze > requirements.txt`
```

To ensure that your requirements file only contains packages that are actually used by your application, use a [virtual environment](python-development-environment.md#python-common-setup-venv "python-development-environment.md#python-common-setup-venv") that only has those packages installed. Outside of a virtual environment, the output of
`pip freeze` will include all `pip` packages installed on your development machine, including those that came with your
operating system.

###### Note

On Amazon Linux AMI Python platform versions, Elastic Beanstalk doesn't natively support Pipenv or Pipfiles. If you use Pipenv to manage your application's
dependencies, run the following command to generate a `requirements.txt` file.

```
~/my-app$ `pipenv lock -r > requirements.txt`
```

To learn more, see [Generating a
requirements.txt](https://pipenv.readthedocs.io/en/latest/advanced/#generating-a-requirements-txt "https://pipenv.readthedocs.io/en/latest/advanced/#generating-a-requirements-txt") in the Pipenv documentation.

## Use Pipenv and `Pipfile`

Pipenv is a modern Python packaging tool. It combines package installation with the creation and management of a dependency file and a virtualenv
for your application. For more information, see [Pipenv: Python Dev Workflow for
Humans](https://pipenv.readthedocs.io/en/latest/ "https://pipenv.readthedocs.io/en/latest/").

Pipenv maintains two files:

- `Pipfile` — This file contains various types of dependencies and requirements.
- `Pipfile.lock` — This file contains a version snapshot that enables deterministic builds.

You can create these files on your development environment and include them in the top-level directory of the source bundle that you deploy to
Elastic Beanstalk. For more information about these two files, see [Example Pipfile and
Pipfile.lock](https://pipenv.pypa.io/en/latest/basics/# "https://pipenv.pypa.io/en/latest/basics/#").

The following example uses Pipenv to install Django and the Django REST framework. These commands create the files `Pipfile` and
`Pipfile.lock`.

```
~/my-app$ `pipenv install django`
~/my-app$ `pipenv install djangorestframework`
```

## Precedence

If you include more than one of the requirements files described in this topic, Elastic Beanstalk uses just one of them. The following list shows the
precedence, in descending order.

1. `requirements.txt`
2. `Pipfile.lock`
3. `Pipfile`

###### Note

Starting with the March 7, 2023 Amazon Linux 2 platform release, if you provide more than one of these files, Elastic Beanstalk will issue a console message stating
which one of the dependency files was used during a deployment.

The following steps describe the logic that Elastic Beanstalk follows to install the dependencies when it's deploying an instance.

- If there is a `requirements.txt` file, we use the command `pip install -r requirements.txt`.
- Starting with the March 7, 2023 Amazon Linux 2 platform release, if there is no `requirements.txt` file, but there is a
  `Pipfile.lock`, we use the command `pipenv sync`. Prior to that release, we used `pipenv install
--ignore-pipfile`.
- If there is neither a `requirements.txt` file nor a `Pipfile.lock`, but there is a
  `Pipfile`, we use the command `pipenv install --skip-lock`.
- If none of the three requirements files are found, we don't install any application dependencies.
