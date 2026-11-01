

# Available runtimes
<a name="available-runtimes"></a>

You can specify one or more runtimes in the `runtime-versions` section of your buildspec file. If your runtime is dependent upon another runtime, you can also specify its dependent runtime in the buildspec file. If you do not specify any runtimes in the buildspec file, CodeBuild chooses the default runtimes that are available in the image you use. If you specify one or more runtimes, CodeBuild uses only those runtimes. If a dependent runtime is not specified, CodeBuild attempts to choose the dependent runtime for you. 

**Note**  
If a runtime version is not specified, CodeBuild uses the default version. The default version can change when a previously default version reaches end of life (EOL). To avoid unexpected changes to the build environment, we recommend specifying a runtime version in the buildspec file.

For more information, see [Specify runtime versions in the buildspec file](build-spec-ref.md#runtime-versions-buildspec-file).

**Topics**
+ [Linux image runtimes](#linux-runtimes)
+ [macOS image runtimes](#macOS-runtimes)
+ [Windows image runtimes](#windows-runtimes)

## Linux image runtimes
<a name="linux-runtimes"></a>

The following table contains the cached runtimes in each of the standard Linux images.


**Ubuntu and Amazon Linux platform runtimes**  

| Image | dotnet | golang | java | nodejs | php | python | ruby | rust | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| Amazon Linux 2023 x86\_64 standard:5.0 | 8.0<br />10.0 (default) | 1.26<br />1.27 (default) | corretto8<br />corretto11<br />corretto17 (default)<br />corretto21<br />corretto25 | 22<br />24 (default)<br />26 | 8.2 (default)<br />8.3<br />8.4<br />8.5 | 3.9<br />3.11 (default)<br />3.12<br />3.13<br />3.14<br />3.15 | 3.3<br />3.4<br />4.0 (default) | — | 
| Amazon Linux 2023 x86\_64 standard:6.0 | 8.0<br />10.0 (default) | 1.26<br />1.27 (default) | corretto8<br />corretto11<br />corretto17<br />corretto21<br />corretto25 (default) | 22<br />24 (default)<br />26 | 8.2<br />8.3<br />8.4<br />8.5 (default) | 3.9<br />3.11<br />3.12<br />3.13<br />3.14 (default)<br />3.15 | 3.3<br />3.4<br />4.0 (default) | 1.99 (default) | 
| Amazon Linux 2023 AArch64 standard:3.0 | 8.0<br />10.0 (default) | 1.26<br />1.27 (default) | corretto8<br />corretto11<br />corretto17 (default)<br />corretto21<br />corretto25 | 22<br />24 (default)<br />26 | 8.2<br />8.3<br />8.4<br />8.5 (default) | 3.9<br />3.11 (default)<br />3.12<br />3.13<br />3.14<br />3.15 | 3.3<br />3.4<br />4.0 (default) | 1.99 (default) | 
| Amazon Linux 2023 AArch64 standard:4.0 | 8.0<br />10.0 (default) | 1.26<br />1.27 (default) | corretto8<br />corretto11<br />corretto17<br />corretto21<br />corretto25 (default) | 22<br />24 (default)<br />26 | 8.2<br />8.3<br />8.4<br />8.5 (default) | 3.9<br />3.11<br />3.12<br />3.13<br />3.14 (default)<br />3.15 | 3.3<br />3.4<br />4.0 (default) | 1.99 (default) | 
| Ubuntu 22.04 standard:7.0 | 8.0<br />10.0 (default) | 1.26<br />1.27 (default) | corretto8<br />corretto11<br />corretto17 (default)<br />corretto21<br />corretto25 | 22<br />24 (default)<br />26 | 8.2 (default)<br />8.3<br />8.4<br />8.5 | 3.10<br />3.11 (default)<br />3.12<br />3.13<br />3.14<br />3.15 | 3.3<br />3.4<br />4.0 (default) | — | 
| Ubuntu 24.04 standard:8.0 | 8.0<br />10.0 (default) | 1.26<br />1.27 (default) | corretto8<br />corretto11<br />corretto17<br />corretto21<br />corretto25 (default) | 22<br />24 (default)<br />26 | 8.2<br />8.3<br />8.4 (default)<br />8.5 | 3.11<br />3.12<br />3.13<br />3.14 (default)<br />3.15 | 3.3<br />3.4<br />4.0 (default) | 1.99 (default) | 
| Amazon Linux 2 x86\_64 standard:corretto8 | — | — | corretto8 (default) | — | — | — | — | — | 
| Amazon Linux 2 x86\_64 standard:corretto11 | — | — | corretto11 (default) | — | — | — | — | — | 

The following Amazon Linux 2 and Amazon Linux 2023 Lambda compute images are also available. Each Lambda image provides a single runtime.


**Lambda compute image runtimes**  


- **dotnet**
  - **Version:** 6.0
  - **Images:** Amazon Linux 2 x86\_64 Lambda standard:dotnet6<br />Amazon Linux 2 AArch64 Lambda standard:dotnet6

- **golang**
  - **Version:** 1.21 / **Images:** Amazon Linux 2 x86\_64 Lambda standard:go1.21<br />Amazon Linux 2 AArch64 Lambda standard:go1.21
  - **Version:** 1.24 / **Images:** Amazon Linux 2023 x86\_64 Lambda standard:go1.24<br />Amazon Linux 2023 AArch64 Lambda standard:go1.24

- **java**
  - **Version:** corretto11 / **Images:** Amazon Linux 2 x86\_64 Lambda standard:corretto11<br />Amazon Linux 2 AArch64 Lambda standard:corretto11
  - **Version:** corretto17 / **Images:** Amazon Linux 2 x86\_64 Lambda standard:corretto17<br />Amazon Linux 2 AArch64 Lambda standard:corretto17
  - **Version:** corretto21 / **Images:** Amazon Linux 2 x86\_64 Lambda standard:corretto21<br />Amazon Linux 2 AArch64 Lambda standard:corretto21

- **nodejs**
  - **Version:** 18 / **Images:** Amazon Linux 2 x86\_64 Lambda standard:nodejs18<br />Amazon Linux 2 AArch64 Lambda standard:nodejs18
  - **Version:** 20 / **Images:** Amazon Linux 2 x86\_64 Lambda standard:nodejs20<br />Amazon Linux 2 AArch64 Lambda standard:nodejs20
  - **Version:** 22 / **Images:** Amazon Linux 2023 x86\_64 Lambda standard:nodejs22<br />Amazon Linux 2023 AArch64 Lambda standard:nodejs22

- **python**
  - **Version:** 3.11 / **Images:** Amazon Linux 2 x86\_64 Lambda standard:python3.11<br />Amazon Linux 2 AArch64 Lambda standard:python3.11
  - **Version:** 3.12 / **Images:** Amazon Linux 2 x86\_64 Lambda standard:python3.12<br />Amazon Linux 2 AArch64 Lambda standard:python3.12
  - **Version:** 3.13 / **Images:** Amazon Linux 2023 x86\_64 Lambda standard:python3.13<br />Amazon Linux 2023 AArch64 Lambda standard:python3.13

- **ruby**
  - **Version:** 3.2 / **Images:** Amazon Linux 2 x86\_64 Lambda standard:ruby3.2<br />Amazon Linux 2 AArch64 Lambda standard:ruby3.2
  - **Version:** 3.4 / **Images:** Amazon Linux 2023 x86\_64 Lambda standard:ruby3.4<br />Amazon Linux 2023 AArch64 Lambda standard:ruby3.4



## macOS image runtimes
<a name="macOS-runtimes"></a>

**Important**  
The CodeBuild curated images for Mac builds contain macOS and Xcode pre-installed. By using the Xcode software, you acknowledge, understand, and consent to the [Xcode and Apple SDKs Agreement](https://www.apple.com/legal/sla/docs/xcode.pdf). If you do not accept the terms and conditions of the agreement, do not use the Xcode software. Instead, provide your own Amazon Machine Images (AMI). For more information, see [How do I configure a reserved capacity macOS fleet?](fleets.md#fleets.configure-macos)

The following table contains the available runtimes supported by macOS.


**macOS platform runtimes**  

| Image | bash | clang | dotnet sdk | gcc | gnu | golang | java | kotlin | mono | nodejs | perl | php | python | ruby | rust | swift | Xcode | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| macos-arm-base:15 | 3.2.57 | 17.0.0 | 8.0.416<br />10.0.101 | 11.5.0<br />12.4.0<br />13.4.0<br />14.3.0 | 11.5.0<br />12.4.0<br />13.4.0<br />14.3.0 | 1.24.11<br />1.25.4 | corretto8<br />corretto11<br />corretto17<br />corretto21<br />corretto25 | 2.2.21 | 6.14.1 | 20.19.6<br />22.21.1<br />24.11.1 | 5.34.1 | 8.2.29<br />8.3.28<br />8.4.15<br />8.5.0 | 3.10.19<br />3.11.14<br />3.12.12<br />3.13.10<br />3.14.1 | 3.2.9<br />3.3.10<br />3.4.7 | 1.91.1 | 6.2.1 | 26.1.1 | 
| macos-arm-base:26 | 3.2.57 | 17.0.0 | 8.0.417<br />10.0.102 | 11.5.0<br />12.4.0<br />13.4.0<br />14.3.0 | 11.5.0<br />12.4.0<br />13.4.0<br />14.3.0 | 1.24.11<br />1.25.4 | corretto8<br />corretto11<br />corretto17<br />corretto21<br />corretto25 | 2.3.0 | 6.14.1 | 20.19.6<br />22.21.1<br />24.11.1 | 5.34.1 | 8.2.30<br />8.3.30<br />8.4.17<br />8.5.2 | 3.10.19<br />3.11.14<br />3.12.12<br />3.13.10<br />3.14.1 | 3.2.9<br />3.3.10<br />3.4.7 | 1.92.0 | 6.2.3 | 26.2 | 

Each `gcc` version is available by using the `gcc-{{major-version}}` alias, such as `gcc-14`. Each `gnu` version is available by using the `gfortran-{{major-version}}` alias, such as `gfortran-14`.

## Windows image runtimes
<a name="windows-runtimes"></a>

The base image of the Windows Server Core 2019 contains the following runtimes.


**Windows platform runtimes**  

| Image | dotnet | dotnet sdk | golang | gradle | java | maven | nodejs | php | powershell | python | ruby | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| Windows Server Core 2019 standard:1.0 | 3.1<br />5.0 | 3.1<br />5.0 | 1.14 | 6.7 | corretto11 | 3.6 | 14.15 | 7.4 | 7.1 | 3.8 | 2.7 | 
| Windows Server Core 2019 standard:2.0 | 3.1<br />6.0<br />7.0 | 3.1<br />6.0<br />7.0 | 1.18 | 7.6 | corretto11<br />corretto17 | 3.8 | 16.19 | 8.1 | 7.2 | 3.10 | 3.1 | 
| Windows Server Core 2019 standard:3.0 | 8.0 | 8.0 | 1.21<br />1.22<br />1.23 | 8.12 | corretto8<br />corretto11<br />corretto17<br />corretto21 | 3.9 | 20.18<br />22.13 | 8.3<br />8.4 | 7.4 | 3.10<br />3.11<br />3.12<br />3.13 | 3.2<br />3.3<br />3.4 | 