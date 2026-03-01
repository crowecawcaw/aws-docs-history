# App Runner configuration file reference

###### Note

Configuration files are applicable only to [services that are based on source code](service-source-code.md "service-source-code.md"). You can't use
configuration files with [image-based services](service-source-image.md "service-source-image.md").

This topic is a comprehensive reference guide to the syntax and semantics of an AWS App Runner configuration file. For an overview of App Runner configuration
files, see [Setting App Runner service options using a configuration file](config-file.md "config-file.md").

The App Runner configuration file is a YAML file. Name it `apprunner.yaml`, and place it in the [source directory](service-source-code.md#service-source-code.source-directory "service-source-code.md#service-source-code.source-directory") of your application’s repository.

## Structure overview

The App Runner configuration file is a YAML file. Name it `apprunner.yaml`, and place it in the [source directory](service-source-code.md#service-source-code.source-directory "service-source-code.md#service-source-code.source-directory") of your application’s repository.

The App Runner configuration file contains these main parts:

- _Top section_ – Contains top-level keys
- _Build section_ – Configures the build stage
- _Run section_ – Configures the runtime stage

## Top section

The keys at the top of the file provide general information about the file and your service runtime. The following keys are available:

- `version` – _Required._ The App Runner configuration file version. Ideally, use the latest version.

Syntax

```
**version**: `version`
```

###### Example

```
**version**: 1.0
```

- `runtime` – _Required._ The name of the runtime that your application uses. To learn about available runtimes
  for the different programming platforms that App Runner offers, see [App Runner service based on source code](service-source-code.md "service-source-code.md").

###### Note

The naming convention of a managed runtime is `<language-name><major-version>`.

Syntax

```
**runtime:** `runtime-name`
```

###### Example

```
**runtime:** python3
```

## Build section

The build section configures the build stage of the App Runner service deployment. You can specify build commands and
environment variables. Build commands are
required.

The section starts with the `build:` key, and has the following subkeys:

- `commands` – _Required._ Specifies the commands that App Runner runs during
  various build phases. Includes the following subkeys:

      + `pre-build` – *Optional.* The commands that App Runner runs before the build. For example, install
       **npm** dependencies or test libraries.
      + `build` – *Required.* The commands that App Runner runs to build your application. For example, use
       **pipenv**.
      + `post-build` – *Optional.* The commands that App Runner runs after the build. For example, use Maven to package
       build artifacts into a JAR or WAR file, or run a test.

  Syntax

```
build:
  **commands:**
    **pre-build:**
      - `command`
      - `…`
    **build:**
      - `command`
      - `…`
    **post-build:**
      - `command`
      - `…`
```

###### Example

```
build:
  **commands:**
    **pre-build:**
      - yum install openssl
    **build:**
      - pip install -r requirements.txt
    **post-build:**
      - python manage.py test
```

- `env` – _Optional._ Specifies custom environment variables for the build
  stage. Defined as name-value scalar mappings. You can refer to these variables by name in your build commands.

###### Note

There are two distinct `env` entries in two different locations in this configuration file. One set is in the **Build** section and the other in the **Run** section.

    + The `env` set in the Build section can be referenced by the `pre-build`, `build`, `post-build`, and
     `pre-run` commands during the *build process*.


    ***Important*** - Note that the `pre-run` commands are located in
     the Run section of this file, even though they can only access the environment variables that are defined in the Build section.
    + The `env` set in the Run section can be referenced by the `run` command in the runtime environment.

Syntax

```
build:
  **env:**
    - name: `name1`
      value: `value1`
    - name: `name2`
      value: `value2`
    - `…`
```

###### Example

```
build:
  **env:**
    - name: DJANGO_SETTINGS_MODULE
      value: "django_apprunner.settings"
    - name: MY_VAR_EXAMPLE
      value: "example"
```

## Run section

The run section configures the container running stage of the App Runner application deployment. You can specify runtime version, pre-run commands (revised
format only), start command, network port, and environment variables.

The section starts with the `run:` key, and has the following subkeys:

- `runtime-version` – _Optional._ Specifies a runtime version that you want to lock
  for your App Runner service.

By default, only the major version is locked. App Runner uses the latest minor and patch versions that are available for the runtime on every deployment
or service update. If you specify major and minor versions, both become locked, and App Runner updates only patch versions. If you specify major, minor, and
patch versions, your service is locked on a specific runtime version and App Runner never updates it.

Syntax

```
run:
  **runtime-version:** `major[.minor[.patch]]`
```

###### Note

The runtimes of some platforms have different version components. See specific platform topics for details.

###### Example

```
runtime: python3
run:
  **runtime-version:** 3.7
```

- `pre-run` – _Optional._
  **_[Revised build](service-source-code.md#service-source-code.build-detail "service-source-code.md#service-source-code.build-detail") usage only_**. Specifies the commands that App Runner runs
  after copying your application from the build image to the run image. You can enter commands here to the modify the run image outside the
  `/app` directory. For example, if you need to install additional global dependencies that reside outside of the
  `/app` directory, enter the required commands in this sub-section to do so. For more information about the App Runner build process,
  see [Managed runtime versions and the App Runner build](service-source-code.md#service-source-code.build-detail "service-source-code.md#service-source-code.build-detail").

###### Note

    + ***Important*** – Even though the `pre-run` commands are
     listed in the Run section, they can only reference the environment variables defined in the Build section of this configuration file. They
     cannot reference the environment variables defined in this Run section.
    + The `pre-run` parameter is only supported by the revised App Runner build.
    Do not insert this parameter in your configuration file if your application uses runtime versions that are supported by the
    original App Runner build. For more information, see [Managed runtime versions and the App Runner build](service-source-code.md#service-source-code.build-detail "service-source-code.md#service-source-code.build-detail").

Syntax

```
run:
  **pre-run:**
      - `command`
      - `…`
```

- `command` – _Required._ The command that App Runner uses to run your application after it completes the
  application build.

Syntax

```
run:
  **command:** `command`
```

- `network` – _Optional._ Specifies the port that your application listens to. It includes the following:

      + `port` – *Optional.* If specified, this is the port number that your application listens to. The default
       is `8080`.
      + `env` – *Optional.* If specified, App Runner passes the port number to the container in this environment
       variable, in addition to (not instead of) passing the same port number in the default environment variable, `PORT`. In other words, if
       you specify `env`, App Runner passes the port number in two environment variables.

  Syntax

```
run:
  **network:**
    **port:** `port-number`
    **env:** `env-variable-name`
```

###### Example

```
run:
  **network:**
    **port:** 8000
    **env:** MY_APP_PORT
```

- `env` – _Optional._ Definition of custom environment variables for the run stage. Defined as name-value scalar
  mappings. You can refer to these variables by name in your runtime environment.

###### Note

There are two distinct `env` entries in two different locations in this configuration file. One set is in the **Build** section and the other in the **Run** section.

    + The `env` set in the Build section can be referenced by the `pre-build`, `build`, `post-build`, and
     `pre-run` commands during the *build process*.


    ***Important*** - Note that the `pre-run` commands are located in
     the Run section of this file, even though they can only access the environment variables that are defined in the Build section.
    + The `env` set in the Run section can be referenced by the `run` command in the runtime environment.

Syntax

```
run:
  **env:**
    - name: `name1`
      value: `value1`
    - name: `name2`
      value: `value2`
  **secrets:**
    - name: `name1`
      value-from: `arn:aws:secretsmanager:region:aws_account_id:secret:secret-id`
    - name: `name2`
      value-from: `arn:aws:ssm:region:aws_account_id:parameter/parameter-name`
    - `…`
```

###### Example

```
run:
  **env:**
    - name: MY_VAR_EXAMPLE
      value: "example"
  **secrets:**
    - name: my-secret
      value-from: "arn:aws:secretsmanager:us-east-1:123456789012:secret:testingstackAppRunnerConstr-kJFXde2ULKbT-S7t8xR:username::"
    - name: my-parameter
      value-from: "arn:aws:ssm:us-east-1:123456789012:parameter/parameter-name"
    - name: my-parameter-only-name
      value-from: "parameter-name"
```
