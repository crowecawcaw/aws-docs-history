# Using NuGet packages in CodeBuild

The following steps have been tested with the operating systems listed in the
[Docker
images provided by CodeBuild](../../../codebuild/latest/userguide/build-env-ref-available.md "../../../codebuild/latest/userguide/build-env-ref-available.md").

###### Topics

- [Set up permissions with IAM roles](#nuget-packages-in-codebuild-iam "#nuget-packages-in-codebuild-iam")
- [Consume NuGet packages](#consume-nuget-packages-in-codebuild "#consume-nuget-packages-in-codebuild")
- [Build with NuGet packages](#build-nuget-packages-in-codebuild "#build-nuget-packages-in-codebuild")
- [Publish NuGet packages](#publish-nuget-packages-in-codebuild "#publish-nuget-packages-in-codebuild")

## Set up permissions with IAM roles

These steps are required when using NuGet packages from CodeArtifact in CodeBuild.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**. On the
   **Roles** page, edit the role used by your CodeBuild build project.
   This role must have the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [ "codeartifact:GetAuthorizationToken",
 "codeartifact:GetRepositoryEndpoint",
 "codeartifact:ReadFromRepository"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "sts:GetServiceBearerToken",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "sts:AWSServiceName": "codeartifact.amazonaws.com"
 }
 }
 }
 ]
}`

```

###### Important

If you also want to use CodeBuild to publish packages, add the
`codeartifact:PublishPackageVersion` permission.

For information, see [Modifying a
Role](../../../IAM/latest/UserGuide/id_roles_manage_modify.md "../../../IAM/latest/UserGuide/id_roles_manage_modify.md") in the _IAM User Guide_.

## Consume NuGet packages

To consume NuGet packages from CodeBuild, include the following in your project's `buildspec.yaml` file.

1. In the `install` section, install the CodeArtifact Credential Provider
   to configure command line tools such as `msbuild` and `dotnet`
   to build and publish packages to CodeArtifact.
2. In the `pre-build` section, add your CodeArtifact repository to your NuGet
   configuration.

See the following `buildspec.yaml` examples. For more information, see
[Using CodeArtifact with NuGet](using-nuget.md "using-nuget.md").

After the credential provider is installed and your repository source is added, you can run NuGet CLI tool commands
from the `build` section to consume NuGet packages.

### Linux

To consume NuGet packages using `dotnet`:

```
version: 0.2

phases:
  install:
    runtime-versions:
      dotnet: latest
    commands:
      - export PATH="$PATH:/root/.dotnet/tools"
      - dotnet tool install -g AWS.CodeArtifact.NuGet.CredentialProvider
      - dotnet codeartifact-creds install
  pre_build:
    commands:
      -  dotnet nuget add source -n codeartifact $(aws codeartifact get-repository-endpoint --domain `my_domain` --domain-owner `111122223333` --repository `my_repo` --format nuget --query repositoryEndpoint --output text)"v3/index.json"
  build:
    commands:
      - dotnet add package <packageName> --source codeartifact
```

### Windows

To consume NuGet packages using `dotnet`:

```
version: 0.2

phases:
  install:
    commands:
      - dotnet tool install -g AWS.CodeArtifact.NuGet.CredentialProvider
      - dotnet codeartifact-creds install
  pre_build:
    commands:
      - dotnet nuget add source -n codeartifact "$(aws codeartifact get-repository-endpoint --domain `my_domain` --domain-owner `111122223333` --repository `my_repo` --format nuget --query repositoryEndpoint --output text)v3/index.json"
  build:
    commands:
      - dotnet add package <packageName> --source codeartifact
```

## Build with NuGet packages

To build with NuGet packages from CodeBuild, include the following in your project's `buildspec.yaml` file.

1. In the `install` section, install the CodeArtifact Credential Provider
   to configure command line tools such as `msbuild` and `dotnet`
   to build and publish packages to CodeArtifact.
2. In the `pre-build` section, add your CodeArtifact repository to your NuGet
   configuration.

See the following `buildspec.yaml` examples. For more information, see
[Using CodeArtifact with NuGet](using-nuget.md "using-nuget.md").

After the credential provider is installed and your repository source is added, you can run NuGet CLI tool commands
like `dotnet build` from the `build` section.

### Linux

To build NuGet packages using `dotnet`:

```
version: 0.2

phases:
  install:
    runtime-versions:
      dotnet: latest
    commands:
      - export PATH="$PATH:/root/.dotnet/tools"
      - dotnet tool install -g AWS.CodeArtifact.NuGet.CredentialProvider
      - dotnet codeartifact-creds install
  pre_build:
    commands:
      -  dotnet nuget add source -n codeartifact $(aws codeartifact get-repository-endpoint --domain my_domain --domain-owner 111122223333 --repository my_repo --format nuget --query repositoryEndpoint --output text)"v3/index.json"
  build:
    commands:
      - dotnet build
```

To build NuGet packages using `msbuild`:

```
version: 0.2

phases:
  install:
    runtime-versions:
      dotnet: latest
    commands:
      - export PATH="$PATH:/root/.dotnet/tools"
      - dotnet tool install -g AWS.CodeArtifact.NuGet.CredentialProvider
      - dotnet codeartifact-creds install
  pre_build:
    commands:
      - dotnet nuget add source -n codeartifact $(aws codeartifact get-repository-endpoint --domain `my_domain` --domain-owner `111122223333` --repository `my_repo` --format nuget --query repositoryEndpoint --output text)"v3/index.json"
  build:
    commands:
      - msbuild -t:Rebuild -p:Configuration=Release
```

### Windows

To build NuGet packages using `dotnet`:

```
version: 0.2

phases:
  install:
    commands:
      - dotnet tool install -g AWS.CodeArtifact.NuGet.CredentialProvider
      - dotnet codeartifact-creds install
  pre_build:
    commands:
      - dotnet nuget add source -n codeartifact "$(aws codeartifact get-repository-endpoint --domain `my_domain` --domain-owner `111122223333` --repository `my_repo` --format nuget --query repositoryEndpoint --output text)v3/index.json"
  build:
    commands:
      - dotnet build
```

To build NuGet packages using `msbuild`:

```
version: 0.2

phases:
  install:
    commands:
      - dotnet tool install -g AWS.CodeArtifact.NuGet.CredentialProvider
      - dotnet codeartifact-creds install
  pre_build:
    commands:
      - dotnet nuget add source -n codeartifact "$(aws codeartifact get-repository-endpoint --domain `my_domain` --domain-owner `111122223333` --repository `my_repo` --format nuget --query repositoryEndpoint --output text)v3/index.json"
  build:
    commands:
      - msbuild -t:Rebuild -p:Configuration=Release
```

## Publish NuGet packages

To publish NuGet packages from CodeBuild, include the following in your project's `buildspec.yaml` file.

1. In the `install` section, install the CodeArtifact Credential Provider
   to configure command line tools such as `msbuild` and `dotnet`
   to build and publish packages to CodeArtifact.
2. In the `pre-build` section, add your CodeArtifact repository to your NuGet
   configuration.

See the following `buildspec.yaml` examples. For more information, see
[Using CodeArtifact with NuGet](using-nuget.md "using-nuget.md").

After the credential provider is installed and your repository source is added, you can run NuGet CLI tool commands
from the `build` section and publish your NuGet packages.

### Linux

To publish NuGet packages using `dotnet`:

```
version: 0.2

phases:
  install:
    runtime-versions:
      dotnet: latest
    commands:
      - export PATH="$PATH:/root/.dotnet/tools"
      - dotnet tool install -g AWS.CodeArtifact.NuGet.CredentialProvider
      - dotnet codeartifact-creds install
  pre_build:
    commands:
      - dotnet nuget add source -n codeartifact $(aws codeartifact get-repository-endpoint --domain `my_domain` --domain-owner `111122223333` --repository `my_repo` --format nuget --query repositoryEndpoint --output text)"v3/index.json"
  build:
    commands:
      - dotnet pack -o .
      - dotnet nuget push *.nupkg -s codeartifact
```

### Windows

To publish NuGet packages using `dotnet`:

```
version: 0.2

phases:
  install:
    commands:
      - dotnet tool install -g AWS.CodeArtifact.NuGet.CredentialProvider
      - dotnet codeartifact-creds install
  pre_build:
    commands:
      - dotnet nuget add source -n codeartifact "$(aws codeartifact get-repository-endpoint --domain `my_domain` --domain-owner `111122223333` --repository `my_repo` --format nuget --query repositoryEndpoint --output text)v3/index.json"
  build:
    commands:
      - dotnet pack -o .
      - dotnet nuget push *.nupkg -s codeartifact
```
