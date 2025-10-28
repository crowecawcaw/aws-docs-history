# App Runner configuration file examples

###### Note

Configuration files are applicable only to [services that are based on source code](service-source-code.md "service-source-code.md"). You can't use
configuration files with [image-based services](service-source-image.md "service-source-image.md").

The following examples demonstrate AWS App Runner configuration files. Some are minimal and contain only required settings. Others are complete, including all
configuration file sections. For an overview of App Runner configuration files, see [Setting App Runner service options using a configuration file](config-file.md "config-file.md").

## Configuration file

examples

With a minimal configuration file, App Runner makes the following assumptions:

- No custom environment variables are necessary during build or run.
- The latest runtime version is used.
- The default port number and port environment variable are used.

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

This example shows the use of all configuration keys in the `apprunner.yaml` original format with a managed runtime.

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

This example shows the use of all configuration keys in the `apprunner.yaml` with a managed runtime.

The `pre-run` parameter is only supported by the revised App Runner build.
Do not insert this parameter in your configuration file if your application uses runtime versions that are supported by the
original App Runner build. For more information, see [Managed runtime versions and the App Runner
build](service-source-code.md#service-source-code.build-detail "service-source-code.md#service-source-code.build-detail").

###### Note

Since this examples is for Python 3.11, we use the `pip3` and `python3` commands. For more information, see
[Callouts for specific runtime versions](service-source-code-python.md#service-source-code-python.callouts "service-source-code-python.md#service-source-code-python.callouts") in the
Python platform topic.

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

For examples of specific managed runtime configuration files, see the specific runtime subtopic under [Code-based service](service-source-code.md "service-source-code.md").
