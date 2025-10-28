# Resolving package dependencies to prepare for

transformation

After [Confirming your repositories to prepare for transformation](dotnet-confirming-repos.md "dotnet-confirming-repos.md"), if AWS Transform finds missing package dependencies, you must complete this step. You can run a Windows PowerShell script to get the missing package dependencies from the same device as your Visual Studio development environment, or you can retrieve the missing packages manually. Then, upload the missing packages.

AWS Transform lists the missing packages in the _Missing package dependencies_ table. You can search for a missing package by name in the search box. This table includes the following details about the missing packages:

- Name
- Associated repositories
- Framework version status
- Core version status
  To resolve the missing package dependencies, [Upload the missing packages](#upload-missing-packages "#upload-missing-packages").

## Upload the missing packages

1. If you choose, you can download a Windows PowerShell helper script to retrieve the missing package dependencies from within your Visual Studio development environment. Or you can find the missing packages manually.

To use the Windows PowerShell script:

    1. Select **Download Windows PowerShell script**.
    2. Run the script locally with an active connection to the repositories that contain the missing package dependency files.
    3. This script allows you to download the missing package dependencies to your local environment.

2. The script will create a single zip file for you to upload which includes all of the dependencies in one archive. You can also upload individual `.nupkg` or zip files for each dependency.
3. Select **Upload package files.**
4. In the **Upload dependency files** modal, select **Choose files** and browse to the location of the compressed missing package files on your device.
5. Select **Upload**.
6. AWS Transform validates the files you uploaded. During validation, you cannot make any updates. AWS Transform reports the validation status above the _Missing package dependencies_ table.
7. AWS Transform also updates the status columns in the _Missing package dependencies_ table from _Missing_ to _Resolved_. If a package fails validation, its status becomes _Invalid_. For invalid files do the following:
   1. In the _Missing package dependencies_ table, select the invalid package using the check box.
   2. Select **Remove uploaded file**.
   3. This changes its status back to _Missing_.

8. After you have uploaded the missing packages and resolved the package dependencies, select **Proceed to review**.

If you select **Proceed to review** without resolving the missing package dependencies, AWS Transform asks if you would like to start the transformation job without the missing packages.
If you select **Ignore the missing package dependencies**, AWS Transform will use assembly references to transform the code. Proceeding with this action can affect related resources.

## Folder Structure Requirements

For NuGet uploads AWS Transform requires either:

- The `.nuspec` file to be placed at the root level for manually uploaded packages, or
- Use of the provided PowerShell script to generate the correct structure

## Version matching requirements

- Framework status: AWS Transform attempts to match the version of the dependency specified in the
  `.csproj` file (source code) with the version of the uploaded dependency.
  An exact match results in a **Success** status.
- Core status: AWS Transform expects a core version specification in the dependencies
  section of the uploaded `.nuspec` file. If one is found then the core
  status is **Success**.

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
