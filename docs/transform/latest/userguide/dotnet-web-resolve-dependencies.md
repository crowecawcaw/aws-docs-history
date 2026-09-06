

# Resolving package dependencies to prepare for transformation
<a name="dotnet-web-resolve-dependencies"></a>

In the *Prepare for transformation* phase, you will:
+ Select repositories for transformation.
+ Resolve any missing dependencies.
+ Review and optionally customize the generated modernization plan.

If AWS Transform finds missing package dependencies, you must complete this step. You can run a Windows PowerShell script to get the missing package dependencies from the same device as your Visual Studio development environment, or you can retrieve the missing packages manually. Then, upload the missing packages.

The Missing Package Dependencies can be updated in two ways:
+ **Resolve using Artifact Connector: ** Resolve by configuring an Artifact Repository (ADO NuGet Connector) through a dedicated Connect Artifact Repository HITL workflow, which is displayed when an Artifact Connector is not configured and packages are missing.
+ **Update missing package:** AWS Transform lists the missing packages in the Missing package dependencies table. You can search for a missing package by name in the search box. This table includes the following details about the missing packages:
  + Name
  + Associated repositories
  + Framework version status
  + Core version status

To resolve the missing package dependencies, [Upload the missing packages](#upload-missing-packages).

## Upload the missing packages
<a name="upload-missing-packages"></a>

1. If you choose, you can download a Windows PowerShell helper script to retrieve the missing package dependencies from within your Visual Studio development environment. Or you can find the missing packages manually.

   To use the Windows PowerShell script:

   1. Select **Download Windows PowerShell script**.

   1. Run the script locally with an active connection to the repositories that contain the missing package dependency files.

   1. This script allows you to download the missing package dependencies to your local environment.

1. The script will create a single zip file for you to upload which includes all of the dependencies in one archive. You can also upload individual `.nupkg` or zip files for each dependency.

1. Select **Upload package files.**

1. In the **Upload dependency files** modal, select **Choose files** and browse to the location of the compressed missing package files on your device.

1. Select **Upload**.

1. AWS Transform validates the files you uploaded. During validation, you cannot make any updates. AWS Transform reports the validation status above the *Missing package dependencies* table.

1. AWS Transform also updates the status columns in the *Missing package dependencies* table from *Missing* to *Resolved*. If a package fails validation, its status becomes *Invalid*. For invalid files do the following:

   1. In the *Missing package dependencies* table, select the invalid package using the check box.

   1. Select **Remove uploaded file**.

   1. This changes its status back to *Missing*.

1. After you have uploaded the missing packages and resolved the package dependencies, select **Proceed to review**.

   If you select **Proceed to review** without resolving the missing package dependencies, AWS Transform asks if you would like to start the transformation job without the missing packages. If you select **Ignore the missing package dependencies**, AWS Transform will use assembly references to transform the code. Proceeding with this action can affect related resources.

## Folder Structure Requirements
<a name="folder-structure-requirements"></a>

For NuGet uploads AWS Transform requires either:
+ The `.nuspec` file to be placed at the root level for manually uploaded packages, or
+ Use of the provided PowerShell script to generate the correct structure

## Version matching requirements
<a name="version-matching-requirements"></a>
+ Framework status: AWS Transform attempts to match the version of the dependency specified in the `.csproj` file (source code) with the version of the uploaded dependency. An exact match results in a **Success** status.
+ Core status: AWS Transform expects a core version specification in the dependencies section of the uploaded `.nuspec` file. If one is found then the core status is **Success**.

  **Example format:**

  ```
  <dependencies>
      <group targetFramework="net8.0" />
  </dependencies>
  ```

  Common versions include:
  + .NET 5.0 (net5.0)
  + .NET 6.0 (net6.0)
  + .NET 7.0 (net7.0)
  + .NET 8.0 (net8.0)