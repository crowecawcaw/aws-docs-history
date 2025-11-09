AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Install AWS Microservice Extractor for .NET

This topic describes how to install AWS Microservice Extractor for .NET. It includes steps to configure
prerequisites to use the runtime profiling agent on your application. You must configure
the runtime profiling prerequisites after you download the Microservice Extractor installer.

###### Installation topics

- [Installation](#microservice-extractor-install-steps "#microservice-extractor-install-steps")
- [Runtime profiling
  prerequisites](#microservice-extractor-install-runtime-profiling "#microservice-extractor-install-runtime-profiling")

## Installation

AWS Microservice Extractor for .NET is available for download as an executable file
(`ServiceExtract.exe`):

[Download
Microservice Extractor](https://aws.amazon.com/microservice-extractor "https://aws.amazon.com/microservice-extractor")

For optional integrity detection, you can download the SHA256 checksum of the
installer.

To use the checksum file, calculate the SHA256 on your downloaded
`.exe` file to compare against the output of the following PowerShell
command:

```
Get-FileHash -Algorithm SHA256 Service-Extract.exe
```

You can verify the authenticity of the signatures of the Microservice Extractor
`.exe` file by running the following command, which verifies that a
valid certificate is contained in the file.

```
Get-AuthenticodeSignature `<file-name>`
```

After you have downloaded the `.exe` file, and performed optional
integrity checks, you can run the installation executable for the Microservice Extractor
assessment tool on your local computer.

When the installation completes, you can find the
`ServiceExtractProfiler.dll` in
`C:\Users\`<username>`\AppData\Local\Programs\AWS
 Microservice Extractor for .NET\resources\AWS
 Tools\serviceextract-profiler\ServiceExtractProfiler.dll`

## Runtime profiling

prerequisites

To use the runtime profiling agent on your application, you must configure the
following prerequisites after you have downloaded the
`ServiceExtract.exe` file.

1. To ensure that IIS manager can access the `.dll` or output
   folder, copy the `.dll` from the default path into the
   `inetpub` folder (for example,
   `C:\inetpub\wwwroot\...`), which is the default folder for
   IIS. In addition, verify that your IIS user has read/write access to the
   output directory.
2. Create a folder for the Microservice Extractor runtime profiler to output to.
3. Register the Microservice Extractor runtime profiler on the server on which the
   application is running using one of the following commands. This step is not
   necessary for .NET Framework version 4 or later.

**Windows 64-bit version:**

```
%systemroot%\System32\regsvr32.exe C:\Users\`<username>`\AppData\Local\Programs\AWS Microservice Extractor for .NET\resources\AWS Tools\serviceextract-profiler\ServiceExtractProfiler.dll
```

**Windows 32-bit version:**

```
%systemroot%\SysWoW64\regsvr32.exe C:\Users\`<username>`\AppData\Local\Programs\AWS Microservice Extractor for .NET\resources\AWS Tools\serviceextract-profiler\ServiceExtractProfiler.dll
```

4. Set relevant environment variables before starting the target binary. You
   must manually update the following system variables.

**.NET Framework**

```
COR_ENABLE_PROFILING enables profiling
COR_ENABLE_PROFILING=1

COR_PROFILER specifies the profiler to use using CLSID or ProgID
COR_PROFILER={DCF75470-C2FC-4198-88EE-D07740A3FB9B}

COR_PROFILER_PATH specifies the path of the serviceextract profiler
COR_PROFILER_PATH=C:\Users\`<username>`\AppData\Local\Programs\AWS Microservice Extractor for .NET\resources\AWS Tools\serviceextract-profiler\ServiceExtractProfiler.dll
```

**.NET Core, NET 7.0, NET 6.0, and .NET
5.0**

```
CORECLR_ENABLE_PROFILING
CORECLR_PROFILER
CORECLR_PROFILER_PATH_64
```

In addition to the previous version-specific updates, you must update the
following variables for **all .NET
versions**:

```
SERVICEEXTRACT_PROFILER_OUTPUT_DIR specifies the output directory used by the profiler
SERVICEEXTRACT_PROFILER_OUTPUT_DIR=C:\ProfilerOutput
SERVICEEXTRACT_PROFILER_TARGET_DLL specifies the output directory used by the profiler
SERVICEEXTRACT_PROFILER_TARGET_DLL=<your-target-app.dll>
```

Here is an example of how to configure IIS with the necessary [environment variables in the applicationHost.config](https://docs.microsoft.com/en-us/iis/configuration/system.applicationhost/applicationpools/applicationpooldefaults/environmentvariables/ "https://docs.microsoft.com/en-us/iis/configuration/system.applicationhost/applicationpools/applicationpooldefaults/environmentvariables/")
file:

```
<applicationPools>
    <add name="DefaultAppPool" />
    <add name="`<YourSiteName>`" autoStart="false" />
    <add name=".NET v4.5 Classic" managedRuntimeVersion="v4.0"
             managedPipelineMode="Classic" />
    <add name=".NET v4.5" managedRuntimeVersion="v4.0" />
    <add name="`<YourSiteName2>`" autoStart="false" />
    <applicationPoolDefaults managedRuntimeVersion="v4.0">
        <processModel identityType="ApplicationPoolIdentity" />
        <environmentVariables>
            <add name="COR_ENABLE_PROFILING" value="1" />
            <add name="COR_PROFILER" value="{DCF75470-C2FC-4198-88EE-D07740A3FB9B}" />
            <add name="COR_PROFILER_PATH" value=" C:\Users\`<username>`\AppData\Local\Programs\AWS Microservice Extractor for .NET\resources\AWS Tools\serviceextract-profiler\ServiceExtractProfiler.dll
            <add name="SERVICEEXTRACT_PROFILER_OUTPUT_DIR" value="C:\ProfilerOutput" />
            <add name="SERVICEEXTRACT_PROFILER_TARGET_DLL" value="`<your-target-app.dll>`" />
        </environmentVariables>
    </applicationPoolDefaults>
</applicationPools>
```

When the manual configuration completes, the runtime profiler automatically
captures metrics when you run your application. Perform typical workloads and test
cases while running your application to capture relevant metrics for an application
assessment. After shutting down the application pool in IIS, a `.csv`
file will be created by the profiler for you to upload to the Microservice Extractor tool for
the assessment. You can find the `.csv` file at the output directory
configured in the previous step for
`SERVICEEXTRACT_PROFILER_OUTPUT_DIR`.
