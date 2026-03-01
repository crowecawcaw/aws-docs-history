# Using the Python platform

###### Important

App Runner will end the support for **Python 3.7** and **Python 3.8**
on December 1, 2025. For recommendations and more information, see [End of support for managed runtime versions](service-source-code.md#service-source-code.managed-platforms.eos "service-source-code.md#service-source-code.managed-platforms.eos").

The AWS App Runner Python platform provides managed runtimes. Each runtime makes it easy to build and run containers with web applications based on a Python
version. When you use a Python runtime, App Runner starts with a managed Python runtime image. This image is based on the [Amazon Linux Docker image](https://hub.docker.com/_/amazonlinux "https://hub.docker.com/_/amazonlinux") and contains the runtime package for a version of Python and some tools and popular
dependency packages. App Runner uses this managed runtime image as a base image, and adds your application code to build a Docker image. It then deploys this
image to run your web service in a container.

You specify a runtime for your App Runner service when you [create a service](manage-create.md "manage-create.md") using the App Runner console or the [CreateService](../api/API_CreateService.md "../api/API_CreateService.md") API operation. You can also specify a runtime as part of your source code. Use the
`runtime` keyword in a [App Runner configuration file](config-file.md "config-file.md") that you include in your code repository.
The naming convention of a managed runtime is `<language-name><major-version>`.

For valid Python runtime names and versions, see [Python runtime release information](service-source-code-python-releases.md "service-source-code-python-releases.md").

App Runner updates the runtime for your service to the latest version on every deployment or service update. If your application requires a specific version of
a managed runtime, you can specify it using the `runtime-version` keyword in the [App Runner configuration file](config-file.md "config-file.md"). You
can lock to any level of version, including a major or minor version. App Runner only makes lower-level updates to the runtime of your service.

Version syntax for Python runtimes:
``major`[.`minor`[.`patch`]]`

For example: `3.8.5`

The following examples demonstrate version locking:

- `3.8` – Lock the major and minor versions. App Runner updates only patch versions.
- `3.8.5` – Lock to a specific patch version. App Runner doesn't update your runtime version.

###### Topics

- [Python runtime configuration](#service-source-code-python.config "#service-source-code-python.config")
- [Callouts for specific runtime versions](#service-source-code-python.callouts "#service-source-code-python.callouts")
- [Python runtime examples](#service-source-code-python.examples "#service-source-code-python.examples")
- [Python runtime release information](service-source-code-python-releases.md "service-source-code-python-releases.md")

## Python runtime configuration

When you choose a managed runtime, you must also configure, as a minimum, build and run commands. You configure them while [creating](manage-create.md "manage-create.md") or [updating](manage-configure.md "manage-configure.md") your App Runner service. You can do this using one of the following methods:

- Using the App Runner console – Specify the commands in the **Configure build** section of the
  creation process or configuration tab.
- Using the App Runner API – Call the [CreateService](../api/API_CreateService.md "../api/API_CreateService.md") or [UpdateService](../api/API_UpdateService.md "../api/API_UpdateService.md") API operation. Specify the commands using the `BuildCommand` and
  `StartCommand` members of the [CodeConfigurationValues](../api/API_CodeConfigurationValues.md "../api/API_CodeConfigurationValues.md") data type.
- Using a [configuration file](config-file.md "config-file.md") – Specify one or more build commands in up to
  three build phases, and a single run command that serves to start your application. There are additional optional configuration settings.

Providing a configuration file is optional. When you create an App Runner service using the console or the API, you specify if App Runner gets your configuration
settings directly when it's created or from a configuration file.

## Callouts for specific runtime versions

###### Note

App Runner now runs an updated build process for applications based on the following runtime versions: Python 3.11, Node.js 22, and Node.js 18. If your application
runs on either one of these runtime versions, see [Managed runtime versions and the App Runner build](service-source-code.md#service-source-code.build-detail "service-source-code.md#service-source-code.build-detail") for more
information about the revised build process. Applications that use all other runtime versions are not affected, and they continue to use the original build
process.

### Python 3.11 (revised App Runner build)

Use the following settings in the _apprunner.yaml_ for the managed Python 3.11 runtime.

- Set the `runtime` key in the Top section to `python311`

###### Example

```
**runtime:** python311
```

- Use the `pip3` instead of `pip` to install dependencies.
- Use the `python3` interpreter instead of `python`.
- Run the `pip3` installer as a `pre-run`command. Python installs dependencies outside of the `/app` directory.
  Since App Runner runs the revised App Runner build for Python 3.11, anything installed outside of the `/app` directory through commands in the Build
  section of the `apprunner.yaml` file will be lost. For more information, see [The revised App Runner build](service-source-code.md#service-source-code.build-detail.v2 "service-source-code.md#service-source-code.build-detail.v2").

###### Example

```
run:
  runtime-version: `3.11`
  pre-run:
    - pip3 install pipenv
    - pipenv install
    - python3 copy-global-files.py
  command: pipenv run gunicorn django_apprunner.wsgi --log-file -
```

For more information, also see the [example of an extended configuration file for
Python 3.11](#service-source-code-python.examples.extended-v2 "#service-source-code-python.examples.extended-v2") later in this topic.

## Python runtime examples

The following examples show App Runner configuration files for building and running a Python service. The last example is the source code for a complete
Python application that you can deploy to a Python runtime service.

###### Note

The runtime version that's used in these examples is `3.7.7` and `3.11`. You can replace it with a
version you want to use. For latest supported Python runtime version, see [Python runtime release information](service-source-code-python-releases.md "service-source-code-python-releases.md").

This example shows a minimal configuration file that you can use with a Python managed runtime. For the assumptions that App Runner makes with a minimal
configuration file, see [Configuration file examples](config-file-examples.md#config-file-examples.managed "config-file-examples.md#config-file-examples.managed").

Python 3.11 uses the `pip3` and `python3` commands. For more information, see the [example of an extended configuration file for Python 3.11](#service-source-code-python.examples.extended-v2 "#service-source-code-python.examples.extended-v2") later in this
topic.

###### Example apprunner.yaml

```
version: 1.0
runtime: python3
build:
  commands:
    build:
      - pip install pipenv
      - pipenv install
run:
  command: python app.py
```

This example shows the use of all configuration keys with a Python managed runtime.

###### Note

The runtime version that's used in these examples is `3.7.7`. You can replace it with a version you want to use. For
latest supported Python runtime version, see [Python runtime release information](service-source-code-python-releases.md "service-source-code-python-releases.md").

Python 3.11 uses the `pip3` and `python3` commands. For more information, see the example of an extended configuration
file for Python 3.11 later in this topic.

###### Example apprunner.yaml

```
version: 1.0
runtime: python3
build:
  commands:
    pre-build:
      - wget -c https://s3.amazonaws.com/amzn-s3-demo-bucket/test-lib.tar.gz -O - | tar -xz
    build:
      - pip install pipenv
      - pipenv install
    post-build:
      - python manage.py test
  env:
    - name: DJANGO_SETTINGS_MODULE
      value: "django_apprunner.settings"
    - name: MY_VAR_EXAMPLE
      value: "example"
run:
  runtime-version: `3.7.7`
  command: pipenv run gunicorn django_apprunner.wsgi --log-file -
  network:
    port: 8000
    env: MY_APP_PORT
  env:
    - name: MY_VAR_EXAMPLE
      value: "example"
  secrets:
    - name: my-secret
      value-from: "arn:aws:secretsmanager:us-east-1:123456789012:secret:testingstackAppRunnerConstr-kJFXde2ULKbT-S7t8xR:username::"
    - name: my-parameter
      value-from: "arn:aws:ssm:us-east-1:123456789012:parameter/parameter-name"
    - name: my-parameter-only-name
      value-from: "parameter-name"
```

This example shows the use of all configuration keys with a Python 3.11 managed runtime in the `apprunner.yaml`. This
example include a `pre-run` section, since this version of Python uses the revised App Runner build.

The `pre-run` parameter is only supported by the revised App Runner build.
Do not insert this parameter in your configuration file if your application uses runtime versions that are supported by the
original App Runner build. For more information, see [Managed runtime versions and the App Runner build](service-source-code.md#service-source-code.build-detail "service-source-code.md#service-source-code.build-detail").

###### Note

The runtime version that's used in these examples is `3.11`. You can replace it with a version you want to use. For
latest supported Python runtime version, see [Python runtime release information](service-source-code-python-releases.md "service-source-code-python-releases.md").

###### Example apprunner.yaml

```
version: 1.0
runtime: python311
build:
  commands:
    pre-build:
      - wget -c https://s3.amazonaws.com/amzn-s3-demo-bucket/test-lib.tar.gz -O - | tar -xz
    build:
      - pip3 install pipenv
      - pipenv install
    post-build:
      - python3 manage.py test
  env:
    - name: DJANGO_SETTINGS_MODULE
      value: "django_apprunner.settings"
    - name: MY_VAR_EXAMPLE
      value: "example"
run:
  runtime-version: `3.11`
  pre-run:
    - pip3 install pipenv
    - pipenv install
    - python3 copy-global-files.py
  command: pipenv run gunicorn django_apprunner.wsgi --log-file -
  network:
    port: 8000
    env: MY_APP_PORT
  env:
    - name: MY_VAR_EXAMPLE
      value: "example"
  secrets:
    - name: my-secret
      value-from: "arn:aws:secretsmanager:us-east-1:123456789012:secret:testingstackAppRunnerConstr-kJFXde2ULKbT-S7t8xR:username::"
    - name: my-parameter
      value-from: "arn:aws:ssm:us-east-1:123456789012:parameter/parameter-name"
    - name: my-parameter-only-name
      value-from: "parameter-name"
```

This example shows the source code for a complete Python application that you can deploy to a Python runtime service.

###### Example requirements.txt

```
pyramid==2.0
```

###### Example server.py

```
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os

def hello_world(request):
    name = os.environ.get('NAME')
    if name == None or len(name) == 0:
        name = "world"
    message = "Hello, " + name + "!\n"
    return Response(message)

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
```

###### Example apprunner.yaml

```
version: 1.0
runtime: python3
build:
  commands:
    build:
      - pip install -r requirements.txt
run:
  command: python server.py
```
