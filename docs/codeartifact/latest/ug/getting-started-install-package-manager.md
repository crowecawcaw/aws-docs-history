

# Install your package manager or build tool
<a name="getting-started-install-package-manager"></a>

To publish or consume packages from CodeArtifact, you must use a package manager. There are different package managers for each package type. The following list contains some package managers that you can use with CodeArtifact. If you haven't already, install the package managers for the package type you want to use.
+ For npm, use the [npm CLI](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) or [pnpm](https://pnpm.io/installation).
+ For Maven, use either [Apache Maven (`mvn`)](https://maven.apache.org/install.html) or [Gradle](https://gradle.org/install/).
+ For Python, use [pip](https://pip.pypa.io/en/stable/installation/) to install packages and [twine](https://twine.readthedocs.io/en/stable/#installation) to publish packages.
+ For NuGet, use the [Toolkit for Visual Studio](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/setup.html) in Visual Studio or the [nuget](https://learn.microsoft.com/en-us/nuget/reference/nuget-exe-cli-reference) or [dotnet](https://learn.microsoft.com/en-us/dotnet/core/install/) CLIs.
+ For [generic](using-generic.md) packages, use the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) or SDK to publish and download package contents.

## Next steps
<a name="getting-started-install-package-manager-next-steps"></a>

Your next steps will depend on which package type or types you are using with CodeArtifact, and the state of your CodeArtifact resources.

If you are getting started with CodeArtifact for the first time for yourself, your team, or organization, see the following documentation for general getting started information and help creating the resources you will need.
+ [Getting started using the console](getting-started-console.md)
+ [Getting started using the AWS CLI](getting-started-cli.md)

If your resources have already been created and you are ready to configure your package manager to push packages to or install packages from a CodeArtifact repository, see the documentation that corresponds to your package type or package manager.
+ [Using CodeArtifact with npm](using-npm.md)
+ [Using CodeArtifact with Python](using-python.md)
+ [Using CodeArtifact with Maven](using-maven.md)
+ [Using CodeArtifact with NuGet](using-nuget.md)
+ [Using CodeArtifact with generic packages](using-generic.md)