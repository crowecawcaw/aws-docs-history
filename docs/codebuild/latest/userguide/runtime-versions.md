# Runtime versions

When you specify a runtime in the [runtime-versions](build-spec-ref.md#build-spec.phases.install.runtime-versions "build-spec-ref.md#build-spec.phases.install.runtime-versions") section of your buildspec file, you can
specify a specific version, a specific major version and the latest minor version, or
the latest version. The following table lists the available runtimes and how to specify
them. Not all runtime versions are available on all images. Runtime version selection is
also not supported for the custom images. For more information, see
[Available runtimes](available-runtimes.md "available-runtimes.md"). If you'd
like to install and use a custom runtime version instead of the pre-installed
runtime versions, see [Custom runtime versions](#custom-runtime "#custom-runtime").

| Ubuntu and Amazon Linux 2 platform runtime versions | Runtime name       | Version              | Specific version    | Specific major and latest minor version | Latest version |
| --------------------------------------------------- | ------------------ | -------------------- | ------------------- | --------------------------------------- | -------------- |
| dotnet                                              | 6.0                | `dotnet: 6.0`        | `dotnet: 6.x`       | `dotnet: latest`                        |
| 8.0                                                 | `dotnet: 8.0`      | `dotnet: 8.x`        |
| 10.0                                                | `dotnet: 10.0`     | `dotnet: 10.x`       |
| golang                                              | 1.20               | `golang: 1.20`       | `golang: 1.x`       | `golang: latest`                        |
| 1.21                                                | `golang: 1.21`     |
| 1.22                                                | `golang: 1.22`     |
| 1.23                                                | `golang: 1.23`     |
| 1.24                                                | `golang: 1.24`     |
| 1.25                                                | `golang: 1.25`     |
| 1.26                                                | `golang: 1.26`     |
| java                                                | corretto8          | `java: corretto8`    | `java: corretto8.x` | `java: latest`                          |
| corretto11                                          | `java: corretto11` | `java: corretto11.x` |
| corretto17                                          | `java: corretto17` | `java: corretto17.x` |
| corretto21                                          | `java: corretto21` | `java: corretto21.x` |
| corretto25                                          | `java: corretto25` | `java: corretto25.x` |
| nodejs                                              | 18                 | `nodejs: 18`         | `nodejs: 18.x`      | `nodejs: latest`                        |
| 20                                                  | `nodejs: 20`       | `nodejs: 20.x`       |
| 22                                                  | `nodejs: 22`       | `nodejs: 22.x`       |
| 24                                                  | `nodejs: 24`       | `nodejs: 24.x`       |
| php                                                 | 8.1                | `php: 8.1`           | `php: 8.x`          | `php: latest`                           |
| 8.2                                                 | `php: 8.2`         |
| 8.3                                                 | `php: 8.3`         |
| 8.4                                                 | `php: 8.4`         |
| 8.5                                                 | `php: 8.5`         |
| python                                              | 3.9                | `python: 3.9`        | `python: 3.x`       | `python: latest`                        |
| 3.10                                                | `python: 3.10`     |
| 3.11                                                | `python: 3.11`     |
| 3.12                                                | `python: 3.12`     |
| 3.13                                                | `python: 3.13`     |
| 3.14                                                | `python: 3.14`     |
| ruby                                                | 3.1                | `ruby: 3.1`          | `ruby: 3.x`         | `ruby: latest`                          |
| 3.2                                                 | `ruby: 3.2`        |
| 3.3                                                 | `ruby: 3.3`        |
| 3.4                                                 | `ruby: 3.4`        |
| 4.0                                                 | `ruby: 4.0`        | `ruby: 4.x`          |
| rust                                                | 1.94               | `rust: 1.94`         | `rust: 1.x`         | `rust: latest`                          |

You can use a build specification to install other components (for example, the AWS CLI,
Apache Maven, Apache Ant, Mocha, RSpec, or similar) during the `install`
build phase. For more information, see [Buildspec example](build-spec-ref.md#build-spec-ref-example "build-spec-ref.md#build-spec-ref-example").

## Custom runtime versions

Instead of using the pre-installed runtime versions in CodeBuild-managed images, you can install and use custom
versions of your choice. The following table lists the available custom runtimes and how to specify them.

###### Note

Custom runtime version selection is only supported for Ubuntu and Amazon Linux images.

| Custom runtime versions | Runtime name                                                          | Syntax                       | Example |
| ----------------------- | --------------------------------------------------------------------- | ---------------------------- | ------- |
| dotnet                  | ``<major>`.`<minor>`.`<patch>``                                       | `5.0.408`                    |
| golang                  | ``<major>`.`<minor>``<br>``<major>`.`<minor>`.`<patch>``              | `1.19`<br>`1.19.1`           |
| java                    | `corretto`<major>``                                                   | `corretto15`                 |
| nodejs                  | `<major>`<br>``<major>`.`<minor>``<br>``<major>`.`<minor>`.`<patch>`` | `14`<br>`14.21`<br>`14.21.3` |
| php                     | ``<major>`.`<minor>`.`<patch>``                                       | `8.0.30`                     |
| python                  | `<major>`<br>``<major>`.`<minor>``<br>``<major>`.`<minor>`.`<patch>`` | `3`<br>`3.7`<br>`3.7.16`     |
| ruby                    | ``<major>`.`<minor>`.`<patch>``                                       | `3.0.6`                      |

### Custom runtime buildspec example

Here is an example of a buildspec that specifies custom runtime versions.

```
version: 0.2
phases:
  install:
    runtime-versions:
      java: corretto15
      php: 8.0.30
      ruby: 3.0.6
      golang: 1.19
      python: 3.7
      nodejs: 14
      dotnet: 5.0.408
```
