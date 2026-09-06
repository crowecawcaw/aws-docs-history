

# Available runtimes
<a name="available-runtimes"></a>

You can specify one or more runtimes in the `runtime-versions` section of your buildspec file. If your runtime is dependent upon another runtime, you can also specify its dependent runtime in the buildspec file. If you do not specify any runtimes in the buildspec file, CodeBuild chooses the default runtimes that are available in the image you use. If you specify one or more runtimes, CodeBuild uses only those runtimes. If a dependent runtime is not specified, CodeBuild attempts to choose the dependent runtime for you. 

**Note**  
If a runtime version is not specified, CodeBuild uses the default version. The default version can change when a previously default version reaches end of life (EOL). To avoid unexpected changes to the build environment, we recommend specifying a runtime version in the buildspec file.

 For more information, see [Specify runtime versions in the buildspec file](build-spec-ref.md#runtime-versions-buildspec-file).

[Specify runtime versions in the buildspec file](build-spec-ref.md#runtime-versions-buildspec-file).

.

**Topics**
+ [Linux image runtimes](#linux-runtimes)
+ [macOS image runtimes](#macOS-runtimes)
+ [Windows image runtimes](#windows-runtimes)

## Linux image runtimes
<a name="linux-runtimes"></a>

The following table contains the available runtimes and the standard Linux images that support them. 


**Ubuntu and Amazon Linux platform runtimes**  


- **dotnet**
  - **Version:** 6.0 / **Images:** Amazon Linux 2 x86\_64 Lambda standard:dotnet6<br />Amazon Linux 2 AArch64 Lambda standard:dotnet6<br />Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0
  - **Version:** 8.0 / **Images:** Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0
  - **Version:** 10.0 / **Images:** Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0

- **golang**
  - **Version:** 1.20 / **Images:** Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0
  - **Version:** 1.21 / **Images:** Amazon Linux 2 x86\_64 Lambda standard:go1.21<br />Amazon Linux 2 AArch64 Lambda standard:go1.21<br />Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0
  - **Version:** 1.22 / **Images:** Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0
  - **Version:** 1.23 / **Images:** Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0
  - **Version:** 1.24 / **Images:** Amazon Linux 2023 x86\_64 Lambda standard:go1.24<br />Amazon Linux 2023 AArch64 Lambda standard:go1.24<br />Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0
  - **Version:** 1.25 / **Images:** Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0
  - **Version:** 1.26 / **Images:** Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0

- **java**
  - **Version:** corretto8 / **Images:** Amazon Linux 2 x86\_64 standard:corretto8<br />Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0
  - **Version:** corretto11 / **Images:** Amazon Linux 2 x86\_64 standard:corretto11<br />Amazon Linux 2 x86\_64 Lambda standard:corretto11<br />Amazon Linux 2 AArch64 Lambda standard:corretto11<br />Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0
  - **Version:** corretto17 / **Images:** Amazon Linux 2 x86\_64 Lambda standard:corretto17<br />Amazon Linux 2 AArch64 Lambda standard:corretto17<br />Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0
  - **Version:** corretto21 / **Images:** Amazon Linux 2 x86\_64 Lambda standard:corretto21<br />Amazon Linux 2 AArch64 Lambda standard:corretto21<br />Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0
  - **Version:** corretto25 / **Images:** Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0

- **nodejs**
  - **Version:** 18 / **Images:** Amazon Linux 2 x86\_64 Lambda standard:nodejs18<br />Amazon Linux 2 AArch64 Lambda standard:nodejs18<br />Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0
  - **Version:** 20 / **Images:** Amazon Linux 2 x86\_64 Lambda standard:nodejs20<br />Amazon Linux 2 AArch64 Lambda standard:nodejs20<br />Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0
  - **Version:** 22 / **Images:** Amazon Linux 2023 x86\_64 Lambda standard:nodejs22<br />Amazon Linux 2023 AArch64 Lambda standard:nodejs22<br />Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0
  - **Version:** 24 / **Images:** Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0

- **php**
  - **Version:** 8.1 / **Images:** Amazon Linux 2023 AArch64 standard:3.0
  - **Version:** 8.2 / **Images:** Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0
  - **Version:** 8.3 / **Images:** Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0
  - **Version:** 8.4 / **Images:** Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0
  - **Version:** 8.5 / **Images:** Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0

- **python**
  - **Version:** 3.9 / **Images:** Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0
  - **Version:** 3.10 / **Images:** Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0
  - **Version:** 3.11 / **Images:** Amazon Linux 2 x86\_64 Lambda standard:python3.11<br />Amazon Linux 2 AArch64 Lambda standard:python3.11<br />Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0
  - **Version:** 3.12 / **Images:** Amazon Linux 2 x86\_64 Lambda standard:python3.12<br />Amazon Linux 2 AArch64 Lambda standard:python3.12<br />Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0
  - **Version:** 3.13 / **Images:** Amazon Linux 2023 x86\_64 Lambda standard:python3.13<br />Amazon Linux 2023 AArch64 Lambda standard:python3.13<br />Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0
  - **Version:** 3.14 / **Images:** Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0

- **ruby**
  - **Version:** 3.1 / **Images:** Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0
  - **Version:** 3.2 / **Images:** Amazon Linux 2 x86\_64 Lambda standard:ruby3.2<br />Amazon Linux 2 AArch64 Lambda standard:ruby3.2<br />Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0
  - **Version:** 3.3 / **Images:** Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0
  - **Version:** 3.4 / **Images:** Amazon Linux 2023 x86\_64 Lambda standard:ruby3.4<br />Amazon Linux 2023 AArch64 Lambda standard:ruby3.4<br />Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0
  - **Version:** 4.0 / **Images:** Amazon Linux 2023 x86\_64 standard:5.0<br />Amazon Linux 2023 x86\_64 standard:6.0<br />Amazon Linux 2023 AArch64 standard:3.0<br />Ubuntu 22.04 standard:7.0<br />Ubuntu 24.04 standard:8.0

- **rust**
  - **Version:** 1.94
  - **Images:** Amazon Linux 2023 AArch64 standard:3.0



## macOS image runtimes
<a name="macOS-runtimes"></a>

**Important**  
The CodeBuild curated images for Mac builds contain macOS and Xcode pre-installed. By using the Xcode software, you acknowledge, understand, and consent to the [Xcode and Apple SDKs Agreement](https://www.apple.com/legal/sla/docs/xcode.pdf). If you do not accept the terms and conditions of the agreement, do not use the Xcode software. Instead, provide your own Amazon Machine Images (AMI). For more information, see [How do I configure a reserved capacity macOS fleet?](fleets.md#fleets.configure-macos)

The following table contains the available runtimes supported by macOS.


**macOS platform runtimes**  


- **bash**
  - **Version:** 3.2.57
  - **Images:** macos-arm-base:15<br />macos-arm-base:26
  - **Additional notes:** 

- **clang**
  - **Version:** 17.0.0
  - **Images:** macos-arm-base:15<br />macos-arm-base:26
  - **Additional notes:** 

- **dotnet sdk**
  - **Version:** 8.0.416 / **Images:** macos-arm-base:15 / **Additional notes:** 
  - **Version:** 8.0.417 / **Images:** macos-arm-base:26 / **Additional notes:** 
  - **Version:** 10.0.101 / **Images:** macos-arm-base:15 / **Additional notes:** 
  - **Version:** 10.0.102 / **Images:** macos-arm-base:26 / **Additional notes:** 

- **gcc**
  - **Version:** 11.5.0 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** Available by using the `gcc-11` alias
  - **Version:** 12.4.0 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** Available by using the `gcc-12` alias
  - **Version:** 13.4.0 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** Available by using the `gcc-13` alias
  - **Version:** 14.3.0 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** Available by using the `gcc-14` alias

- **gnu**
  - **Version:** 11.5.0 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** Available by using the `gfortran-11` alias
  - **Version:** 12.4.0 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** Available by using the `gfortran-12` alias
  - **Version:** 13.4.0 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** Available by using the `gfortran-13` alias
  - **Version:** 14.3.0 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** Available by using the `gfortran-14` alias

- **golang**
  - **Version:** 1.24.11 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** 
  - **Version:** 1.25.4 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** 

- **java**
  - **Version:** Corretto8 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** 
  - **Version:** Corretto11 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** 
  - **Version:** Corretto17 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** 
  - **Version:** Corretto21 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** 
  - **Version:** Corretto25 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** 

- **kotlin**
  - **Version:** 2.2.21 / **Images:** macos-arm-base:15 / **Additional notes:** 
  - **Version:** 2.3.0 / **Images:** macos-arm-base:26 / **Additional notes:** 

- **mono**
  - **Version:** 6.14.1
  - **Images:** macos-arm-base:15<br />macos-arm-base:26
  - **Additional notes:** 

- **nodejs**
  - **Version:** 20.19.6 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** 
  - **Version:** 22.21.1 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** 
  - **Version:** 24.11.1 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** 

- **perl**
  - **Version:** 5.34.1
  - **Images:** macos-arm-base:15<br />macos-arm-base:26
  - **Additional notes:** 

- **php**
  - **Version:** 8.2.29 / **Images:** macos-arm-base:15 / **Additional notes:** 
  - **Version:** 8.2.30 / **Images:** macos-arm-base:26 / **Additional notes:** 
  - **Version:** 8.3.28 / **Images:** macos-arm-base:15 / **Additional notes:** 
  - **Version:** 8.3.30 / **Images:** macos-arm-base:26 / **Additional notes:** 
  - **Version:** 8.4.15 / **Images:** macos-arm-base:15 / **Additional notes:** 
  - **Version:** 8.4.17 / **Images:** macos-arm-base:26 / **Additional notes:** 
  - **Version:** 8.5.0 / **Images:** macos-arm-base:15 / **Additional notes:** 
  - **Version:** 8.5.2 / **Images:** macos-arm-base:26 / **Additional notes:** 

- **python**
  - **Version:** 3.10.19 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** 
  - **Version:** 3.11.14 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** 
  - **Version:** 3.12.12 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** 
  - **Version:** 3.13.10 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** 
  - **Version:** 3.14.1 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** 

- **ruby**
  - **Version:** 3.2.9 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** 
  - **Version:** 3.3.10 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** 
  - **Version:** 3.4.7 / **Images:** macos-arm-base:15<br />macos-arm-base:26 / **Additional notes:** 

- **rust**
  - **Version:** 1.91.1 / **Images:** macos-arm-base:15 / **Additional notes:** 
  - **Version:** 1.92.0 / **Images:** macos-arm-base:26 / **Additional notes:** 

- **swift**
  - **Version:** 6.2.1 / **Images:** macos-arm-base:15 / **Additional notes:** 
  - **Version:** 6.2.3 / **Images:** macos-arm-base:26 / **Additional notes:** 

- **Xcode**
  - **Version:** 26.1.1 / **Images:** macos-arm-base:15 / **Additional notes:** 
  - **Version:** 26.2 / **Images:** macos-arm-base:26 / **Additional notes:** 



## Windows image runtimes
<a name="windows-runtimes"></a>

The base image of the Windows Server Core 2019 contains the following runtimes.


**Windows platform runtimes**  

| Runtime name | Windows Server Core 2019 standard:1.0 versions | Windows Server Core 2019 standard:2.0 versions | Windows Server Core 2019 standard:3.0 versions | 
| --- | --- | --- | --- | 
| dotnet | 3.1<br />5.0 | 3.1<br />6.0<br />7.0 | 8.0 | 
| dotnet sdk | 3.1<br />5.0 | 3.1<br />6.0<br />7.0 | 8.0 | 
| golang | 1.14 | 1.18 | 1.21<br />1.22<br />1.23 | 
| gradle | 6.7 | 7.6 | 8.12 | 
| java | Corretto11 | Corretto11<br />Corretto17 | Corretto8<br />Corretto11<br />Corretto17<br />Corretto21 | 
| maven | 3.6 | 3.8 | 3.9 | 
| nodejs | 14.15 | 16.19 | 20.18<br />22.13 | 
| php | 7.4 | 8.1 | 8.3<br />8.4 | 
| powershell | 7.1 | 7.2 | 7.4 | 
| python | 3.8 | 3.10 | 3.10<br />3.11<br />3.12<br />3.13 | 
| ruby | 2.7 | 3.1 | 3.2<br />3.3<br />3.4 | 