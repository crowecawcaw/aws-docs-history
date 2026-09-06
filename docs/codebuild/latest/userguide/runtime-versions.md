

# Runtime versions
<a name="runtime-versions"></a>

When you specify a runtime in the [`runtime-versions`](build-spec-ref.md#build-spec.phases.install.runtime-versions) section of your buildspec file, you can specify a specific version, a specific major version and the latest minor version, or the latest version. The following table lists the available runtimes and how to specify them. Not all runtime versions are available on all images. Runtime version selection is also not supported for the custom images. For more information, see [Available runtimes](available-runtimes.md). If you'd like to install and use a custom runtime version instead of the pre-installed runtime versions, see [Custom runtime versions](#custom-runtime).


**Ubuntu and Amazon Linux 2 platform runtime versions**  


- **dotnet**
  - **Version:** 6.0 / **Specific version:** `dotnet: 6.0` / **Specific major and latest minor version:** `dotnet: 6.x`
  - **Version:** 8.0 / **Specific version:** `dotnet: 8.0` / **Specific major and latest minor version:** `dotnet: 8.x`
  - **Version:** 10.0 / **Specific version:** `dotnet: 10.0` / **Specific major and latest minor version:** `dotnet: 10.x`
  - **Latest version:** `dotnet: latest`

- **golang**
  - **Version:** 1.20 / **Specific version:** `golang: 1.20`
  - **Version:** 1.21 / **Specific version:** `golang: 1.21`
  - **Version:** 1.22 / **Specific version:** `golang: 1.22`
  - **Version:** 1.23 / **Specific version:** `golang: 1.23`
  - **Version:** 1.24 / **Specific version:** `golang: 1.24`
  - **Version:** 1.25 / **Specific version:** `golang: 1.25`
  - **Version:** 1.26 / **Specific version:** `golang: 1.26`
  - **Specific major and latest minor version:**  `golang: 1.x` 
  - **Latest version:**  `golang: latest` 

- **java**
  - **Version:** corretto8 / **Specific version:** `java: corretto8` / **Specific major and latest minor version:** `java: corretto8.x`
  - **Version:** corretto11 / **Specific version:** `java: corretto11` / **Specific major and latest minor version:** `java: corretto11.x`
  - **Version:** corretto17 / **Specific version:** `java: corretto17` / **Specific major and latest minor version:** `java: corretto17.x`
  - **Version:** corretto21 / **Specific version:** `java: corretto21` / **Specific major and latest minor version:** `java: corretto21.x`
  - **Version:** corretto25 / **Specific version:** `java: corretto25` / **Specific major and latest minor version:** `java: corretto25.x`
  - **Latest version:** `java: latest`

- **nodejs**
  - **Version:** 18 / **Specific version:** `nodejs: 18` / **Specific major and latest minor version:** `nodejs: 18.x`
  - **Version:** 20 / **Specific version:** `nodejs: 20` / **Specific major and latest minor version:** `nodejs: 20.x`
  - **Version:** 22 / **Specific version:** `nodejs: 22` / **Specific major and latest minor version:** `nodejs: 22.x`
  - **Version:** 24 / **Specific version:** `nodejs: 24` / **Specific major and latest minor version:** `nodejs: 24.x`
  - **Latest version:** `nodejs: latest`

- **php**
  - **Version:** 8.1 / **Specific version:** `php: 8.1`
  - **Version:** 8.2 / **Specific version:** `php: 8.2`
  - **Version:** 8.3 / **Specific version:** `php: 8.3`
  - **Version:** 8.4 / **Specific version:** `php: 8.4`
  - **Version:** 8.5 / **Specific version:** `php: 8.5`
  - **Specific major and latest minor version:** `php: 8.x`
  - **Latest version:** `php: latest`

- **python**
  - **Version:** 3.9 / **Specific version:** `python: 3.9`
  - **Version:** 3.10 / **Specific version:** `python: 3.10`
  - **Version:** 3.11 / **Specific version:** `python: 3.11`
  - **Version:** 3.12 / **Specific version:** `python: 3.12`
  - **Version:** 3.13 / **Specific version:** `python: 3.13`
  - **Version:** 3.14 / **Specific version:** `python: 3.14`
  - **Specific major and latest minor version:** `python: 3.x`
  - **Latest version:** `python: latest`

- **ruby**
  - **Version:** 3.1 / **Specific version:** `ruby: 3.1` / **Specific major and latest minor version:** `ruby: 3.x`
  - **Version:** 3.2 / **Specific version:** `ruby: 3.2`
  - **Version:** 3.3 / **Specific version:** `ruby: 3.3`
  - **Version:** 3.4 / **Specific version:** `ruby: 3.4`
  - **Version:** 4.0 / **Specific version:** `ruby: 4.0` / **Specific major and latest minor version:** `ruby: 4.x`
  - **Latest version:** `ruby: latest`

- **rust**
  - **Version:** 1.94
  - **Specific version:** `rust: 1.94`
  - **Specific major and latest minor version:** `rust: 1.x`
  - **Latest version:** `rust: latest`



You can use a build specification to install other components (for example, the AWS CLI, Apache Maven, Apache Ant, Mocha, RSpec, or similar) during the `install` build phase. For more information, see [Buildspec example](build-spec-ref.md#build-spec-ref-example).

## Custom runtime versions
<a name="custom-runtime"></a>

Instead of using the pre-installed runtime versions in CodeBuild-managed images, you can install and use custom versions of your choice. The following table lists the available custom runtimes and how to specify them.

**Note**  
Custom runtime version selection is only supported for Ubuntu and Amazon Linux images.


**Custom runtime versions**  

| Runtime name  | Syntax | Example | 
| --- | --- | --- | 
| dotnet | `{{<major>}}.{{<minor>}}.{{<patch>}}` | `5.0.408` | 
| golang | `{{<major>}}.{{<minor>}}`<br />`{{<major>}}.{{<minor>}}.{{<patch>}}` | `1.19`<br />`1.19.1` | 
| java | `corretto{{<major>}}` | `corretto15` | 
| nodejs | `{{<major>}}`<br />`{{<major>}}.{{<minor>}}`<br />`{{<major>}}.{{<minor>}}.{{<patch>}}` | `14`<br />`14.21`<br />`14.21.3` | 
| php | `{{<major>}}.{{<minor>}}.{{<patch>}}` | `8.0.30` | 
| python | `{{<major>}}`<br />`{{<major>}}.{{<minor>}}`<br />`{{<major>}}.{{<minor>}}.{{<patch>}}` | `3`<br />`3.7`<br />`3.7.16` | 
| ruby | `{{<major>}}.{{<minor>}}.{{<patch>}}` | `3.0.6` | 

### Custom runtime buildspec example
<a name="custom-runtime-buildspec"></a>

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