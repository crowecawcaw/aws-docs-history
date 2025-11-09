Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# NuGet package name, version, and asset name normalization

CodeCatalyst normalizes package and asset names and package versions before storing them, which means the names or versions in CodeCatalyst may be different than the ones provided when the
package or asset was published.

**Package name normalization:** CodeCatalyst normalizes NuGet package names by converting all letters to lowercase.

**Package version normalization:** CodeCatalyst normalizes NuGet package versions using the same pattern as NuGet.
The following information is from
[Normalized version numbers](https://docs.microsoft.com/en-us/nuget/concepts/package-versioning#normalized-version-numbers "https://docs.microsoft.com/en-us/nuget/concepts/package-versioning#normalized-version-numbers")
from the NuGet documentation.

- Leading zeroes are removed from version numbers:
  - `1.00` is treated as `1.0`
  - `1.01.1` is treated as `1.1.1`
  - `1.00.0.1` is treated as `1.0.0.1`

- A zero in the fourth part of the version number will be omitted:
  - `1.0.0.0` is treated as `1.0.0`
  - `1.0.01.0` is treated as `1.0.1`

- SemVer 2.0.0 build metadata is removed:

      + `1.0.7+r3456` is treated as `1.0.7`

  **Package asset name normalization:** CodeCatalyst constructs the NuGet package asset name from the normalized package name and package version.
