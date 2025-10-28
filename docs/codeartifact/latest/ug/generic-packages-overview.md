# Generic packages overview

Using the `generic` package format, you can upload any type of file to create
a package in a CodeArtifact repository. Generic packages aren't associated with any specific
programming language, file type, or package management ecosystem. This can be useful for
storing and versioning arbitrary build artifacts, such as application installers, machine
learning models, configuration files, and others.

A generic package consists of a package name, namespace, version, and one or more assets (or files).
Generic packages can exist alongside packages of other formats in a single CodeArtifact repository.

You can use the AWS CLI or SDK to work with generic packages. For a full list of AWS CLI commands that work with generic packages, see
[Supported commands for generic packages](generic-packages-supported-commands.md "generic-packages-supported-commands.md").

## Generic package constraints

- They are never fetched from upstream repositories. They can only be obtained
  from the repository to which they were published.
- They cannot declare dependencies to be returned from [ListPackageVersionDependencies](../APIReference/API_ListPackageVersionDependencies.md "../APIReference/API_ListPackageVersionDependencies.md") or displayed in the AWS Management Console .
- They can store README and LICENSE files, but they're not interpreted by CodeArtifact. Information in
  these files is not returned from [GetPackageVersionReadme](../APIReference/API_GetPackageVersionReadme.md "../APIReference/API_GetPackageVersionReadme.md") or [DescribePackageVersion](../APIReference/API_DescribePackageVersion.md "../APIReference/API_DescribePackageVersion.md"), and doesn't appear in the AWS Management Console.
- Like all packages in CodeArtifact, there are limits to asset size and the number of assets per
  package. For more information about limits and quotas in CodeArtifact, see [Quotas in AWS CodeArtifact](service-limits.md "service-limits.md").
- The asset names that they contain must follow these rules:
  - Asset names can use Unicode letters and numbers. Specifically, these Unicode character
    categories are allowed: Lowercase Letter (`Ll`), Modifier Letter (`Lm`),
    Other Letter (`Lo`), Titlecase Letter (`Lt`),
    Uppercase Letter (`Lu`), Letter Number (`Nl`), and Decimal Number (`Nd`).
  - The following special characters are allowed: `~!@^&()-_+[]{};,.`
  - Assets cannot be named `.` or `..`
  - Spaces are the only allowed whitespace character. Asset names cannot start or end with a space character, or include consecutive spaces.
