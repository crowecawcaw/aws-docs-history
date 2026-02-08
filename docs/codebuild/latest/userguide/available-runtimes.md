# Available runtimes

You can specify one or more runtimes in the `runtime-versions` section of your buildspec file. If your runtime
is dependent upon another runtime, you can also specify its dependent runtime in the buildspec file.
If you do not specify any runtimes in the buildspec file, CodeBuild chooses the default runtimes that
are available in the image you use. If you specify one or more runtimes, CodeBuild uses only those runtimes.
If a dependent runtime is not specified, CodeBuild attempts to choose the dependent runtime for you. For more information, see [Specify runtime versions in the buildspec file](build-spec-ref.md#runtime-versions-buildspec-file "build-spec-ref.md#runtime-versions-buildspec-file").

###### Topics

- [Linux image runtimes](#linux-runtimes "#linux-runtimes")
- [macOS image runtimes](#macOS-runtimes "#macOS-runtimes")
- [Windows image runtimes](#windows-runtimes "#windows-runtimes")

## Linux image runtimes

The following table contains the available runtimes and the standard Linux images
that support them.

| Ubuntu and Amazon Linux platform runtimes | Runtime name                                                                                                                                                                                                                                                 | Version                                                                                                                                                                                                     | Images |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| dotnet                                    | 6.0                                                                                                                                                                                                                                                          | Amazon Linux 2 x86_64 Lambda standard:dotnet6<br>Amazon Linux 2 AArch64 Lambda standard:dotnet6<br>Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0   |
| 8.0                                       | Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                                                                                                                                       |
| golang                                    | 1.20                                                                                                                                                                                                                                                         | Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                                                                                      |
| 1.21                                      | Amazon Linux 2 x86_64 Lambda standard:go1.21<br>Amazon Linux 2 AArch64 Lambda standard:go1.21<br>Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                                      |
| 1.22                                      | Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                                                                                                                                       |
| 1.23                                      | Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                                                                                                                                       |
| 1.24                                      | Amazon Linux 2023 x86_64 Lambda standard:go1.24<br>Amazon Linux 2023 AArch64 Lambda standard:go1.24<br>Amazon Linux 2023 x86_64 standard:5.0<br>Ubuntu standard:7.0                                                                                          |
| java                                      | corretto8                                                                                                                                                                                                                                                    | Amazon Linux 2 x86_64 standard:corretto8<br>Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                                          |
| corretto11                                | Amazon Linux 2 x86_64 standard:corretto11<br>Amazon Linux 2 x86_64 Lambda standard:corretto11<br>Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2 AArch64 Lambda standard:corretto11<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0 |
| corretto17                                | Amazon Linux 2 x86_64 Lambda standard:corretto17<br>Amazon Linux 2 AArch64 Lambda standard:corretto17<br>Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                              |
| corretto21                                | Amazon Linux 2 x86_64 Lambda standard:corretto21<br>Amazon Linux 2 AArch64 Lambda standard:corretto21<br>Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                              |
| corretto25                                | Amazon Linux 2023 AArch64 standard:3.0                                                                                                                                                                                                                       |
| nodejs                                    | 18                                                                                                                                                                                                                                                           | Amazon Linux 2 x86_64 Lambda standard:nodejs18<br>Amazon Linux 2 AArch64 Lambda standard:nodejs18<br>Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0 |
| 20                                        | Amazon Linux 2 x86_64 Lambda standard:nodejs20<br>Amazon Linux 2 AArch64 Lambda standard:nodejs20<br>Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                                  |
| 22                                        | Amazon Linux 2023 x86_64 Lambda standard:nodejs22<br>Amazon Linux 2023 AArch64 Lambda standard:nodejs22<br>Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                            |
| 24                                        | Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                                                                                                                                       |
| php                                       | 8.1                                                                                                                                                                                                                                                          | Amazon Linux 2023 AArch64 standard:3.0                                                                                                                                                                      |
| 8.2                                       | Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                                                                                                                                       |
| 8.3                                       | Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                                                                                                                                       |
| 8.4                                       | Amazon Linux 2023 AArch64 standard:3.0                                                                                                                                                                                                                       |
| 8.5                                       | Amazon Linux 2023 AArch64 standard:3.0                                                                                                                                                                                                                       |
| python                                    | 3.9                                                                                                                                                                                                                                                          | Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                                                                                      |
| 3.10                                      | Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                                                                                                                                       |
| 3.11                                      | Amazon Linux 2 x86_64 Lambda standard:python3.11<br>Amazon Linux 2 AArch64 Lambda standard:python3.11<br>Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                              |
| 3.12                                      | Amazon Linux 2 x86_64 Lambda standard:python3.12<br>Amazon Linux 2 AArch64 Lambda standard:python3.12<br>Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                              |
| 3.13                                      | Amazon Linux 2023 x86_64 Lambda standard:python3.13<br>Amazon Linux 2023 AArch64 Lambda standard:python3.13<br>Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                        |
| 3.14                                      | Amazon Linux 2023 AArch64 standard:3.0                                                                                                                                                                                                                       |
| ruby                                      | 3.1                                                                                                                                                                                                                                                          | Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                                                                                      |
| 3.2                                       | Amazon Linux 2 x86_64 Lambda standard:ruby3.2<br>Amazon Linux 2 AArch64 Lambda standard:ruby3.2<br>Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                                    |
| 3.3                                       | Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                                                                                                                                       |
| 3.4                                       | Amazon Linux 2023 x86_64 Lambda standard:ruby3.4<br>Amazon Linux 2023 AArch64 Lambda standard:ruby3.4<br>Amazon Linux 2023 x86_64 standard:5.0<br>Amazon Linux 2023 AArch64 standard:3.0<br>Ubuntu standard:7.0                                              |

## macOS image runtimes

###### Important

The CodeBuild curated images for Mac builds contain macOS and Xcode pre-installed. By using the
Xcode software, you acknowledge, understand, and consent to the
[Xcode and Apple SDKs Agreement](https://www.apple.com/legal/sla/docs/xcode.pdf "https://www.apple.com/legal/sla/docs/xcode.pdf").
If you do not accept the terms and conditions of the agreement, do not use the Xcode software. Instead,
provide your own Amazon Machine Images (AMI). For more information, see [How do I configure a reserved capacity macOS fleet?](fleets.md#fleets.configure-macos "fleets.md#fleets.configure-macos")

The following table contains the available runtimes supported by macOS.

| macOS platform runtimes | Runtime name                           | Version                                    | Images                                     | Additional notes |
| ----------------------- | -------------------------------------- | ------------------------------------------ | ------------------------------------------ | ---------------- |
| bash                    | 3.2.57                                 | macos-arm-base:15<br>macos-arm-base:26     |                                            |
| clang                   | 17.0.0                                 | macos-arm-base:15<br>macos-arm-base:26     |                                            |
| dotnet sdk              | 8.0.416                                | macos-arm-base:15                          |                                            |
| 8.0.417                 | macos-arm-base:26                      |                                            |
| 10.0.101                | macos-arm-base:15                      |                                            |
| 10.0.102                | macos-arm-base:26                      |                                            |
| gcc                     | 11.5.0                                 | macos-arm-base:15<br>macos-arm-base:26     | Available by using the `gcc-11` alias      |
| 12.4.0                  | macos-arm-base:15<br>macos-arm-base:26 | Available by using the `gcc-12` alias      |
| 13.4.0                  | macos-arm-base:15<br>macos-arm-base:26 | Available by using the `gcc-13` alias      |
| 14.3.0                  | macos-arm-base:15<br>macos-arm-base:26 | Available by using the `gcc-14` alias      |
| gnu                     | 11.5.0                                 | macos-arm-base:15<br>macos-arm-base:26     | Available by using the `gfortran-11` alias |
| 12.4.0                  | macos-arm-base:15<br>macos-arm-base:26 | Available by using the `gfortran-12` alias |
| 13.4.0                  | macos-arm-base:15<br>macos-arm-base:26 | Available by using the `gfortran-13` alias |
| 14.3.0                  | macos-arm-base:15<br>macos-arm-base:26 | Available by using the `gfortran-14` alias |
| golang                  | 1.24.11                                | macos-arm-base:15<br>macos-arm-base:26     |                                            |
| 1.25.4                  | macos-arm-base:15<br>macos-arm-base:26 |                                            |
| java                    | Corretto8                              | macos-arm-base:15<br>macos-arm-base:26     |                                            |
| Corretto11              | macos-arm-base:15<br>macos-arm-base:26 |                                            |
| Corretto17              | macos-arm-base:15<br>macos-arm-base:26 |                                            |
| Corretto21              | macos-arm-base:15<br>macos-arm-base:26 |                                            |
| Corretto25              | macos-arm-base:15<br>macos-arm-base:26 |                                            |
| kotlin                  | 2.2.21                                 | macos-arm-base:15                          |                                            |
| 2.3.0                   | macos-arm-base:26                      |                                            |
| mono                    | 6.14.1                                 | macos-arm-base:15<br>macos-arm-base:26     |                                            |
| nodejs                  | 20.19.6                                | macos-arm-base:15<br>macos-arm-base:26     |                                            |
| 22.21.1                 | macos-arm-base:15<br>macos-arm-base:26 |                                            |
| 24.11.1                 | macos-arm-base:15<br>macos-arm-base:26 |                                            |
| perl                    | 5.34.1                                 | macos-arm-base:15<br>macos-arm-base:26     |                                            |
| php                     | 8.2.29                                 | macos-arm-base:15                          |                                            |
| 8.2.30                  | macos-arm-base:26                      |                                            |
| 8.3.28                  | macos-arm-base:15                      |                                            |
| 8.3.30                  | macos-arm-base:26                      |                                            |
| 8.4.15                  | macos-arm-base:15                      |                                            |
| 8.4.17                  | macos-arm-base:26                      |                                            |
| 8.5.0                   | macos-arm-base:15                      |                                            |
| 8.5.2                   | macos-arm-base:26                      |                                            |
| python                  | 3.10.19                                | macos-arm-base:15<br>macos-arm-base:26     |                                            |
| 3.11.14                 | macos-arm-base:15<br>macos-arm-base:26 |                                            |
| 3.12.12                 | macos-arm-base:15<br>macos-arm-base:26 |                                            |
| 3.13.10                 | macos-arm-base:15<br>macos-arm-base:26 |                                            |
| 3.14.1                  | macos-arm-base:15<br>macos-arm-base:26 |                                            |
| ruby                    | 3.2.9                                  | macos-arm-base:15<br>macos-arm-base:26     |                                            |
| 3.3.10                  | macos-arm-base:15<br>macos-arm-base:26 |                                            |
| 3.4.7                   | macos-arm-base:15<br>macos-arm-base:26 |                                            |
| rust                    | 1.91.1                                 | macos-arm-base:15                          |                                            |
| 1.92.0                  | macos-arm-base:26                      |                                            |
| swift                   | 6.2.1                                  | macos-arm-base:15                          |                                            |
| 6.2.3                   | macos-arm-base:26                      |                                            |
| Xcode                   | 26.1.1                                 | macos-arm-base:15                          |                                            |
| 26.2                    | macos-arm-base:26                      |                                            |

## Windows image runtimes

The base image of the Windows Server Core 2019 contains the following runtimes.

| Windows platform runtimes | Runtime name | Windows Server Core 2019 standard:1.0 versions | Windows Server Core 2019 standard:2.0 versions | Windows Server Core 2019 standard:3.0 versions |
| ------------------------- | ------------ | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| dotnet                    | 3.15.0       | 3.16.07.0                                      | 8.0                                            |
| dotnet sdk                | 3.15.0       | 3.16.07.0                                      | 8.0                                            |
| golang                    | 1.14         | 1.18                                           | 1.211.221.23                                   |
| gradle                    | 6.7          | 7.6                                            | 8.12                                           |
| java                      | Corretto11   | Corretto11Corretto17                           | Corretto8Corretto11Corretto17Corretto21        |
| maven                     | 3.6          | 3.8                                            | 3.9                                            |
| nodejs                    | 14.15        | 16.19                                          | 20.1822.13                                     |
| php                       | 7.4          | 8.1                                            | 8.38.4                                         |
| powershell                | 7.1          | 7.2                                            | 7.4                                            |
| python                    | 3.8          | 3.10                                           | 3.103.113.123.13                               |
| ruby                      | 2.7          | 3.1                                            | 3.23.33.4                                      |
