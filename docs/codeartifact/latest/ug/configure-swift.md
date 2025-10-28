# Configure the Swift Package Manager with CodeArtifact

To use the Swift Package Manager to publish packages to or consume packages from AWS CodeArtifact,
you'll first need to set up credentials to access your CodeArtifact repository. The recommended method for configuring the
Swift Package Manager CLI with your CodeArtifact credentials and repository endpoint is by using the
`aws codeartifact login` command. You can also configure the Swift Package Manager manually.

## Configure Swift with the login command

Use the `aws codeartifact login` command to configure the Swift Package Manager with CodeArtifact.

###### Note

To use the login command, Swift 5.8 or later is required and Swift 5.9 or later is recommended.

The `aws codeartifact login` command will do the following:

1.  Fetch an authentication token from CodeArtifact and store it in your environment. How the credentials are stored
    depends on the operating system of the environment:

        1. **macOS:** An entry is created in the macOS Keychain application.
        2. **Linux and Windows:** An entry is created in the `~/.netrc` file.

    In all operating systems, if a credentials entry exists, this command replaces that entry with a new token.

2.  Fetch your CodeArtifact repository endpoint URL and add it to your Swift configuration file. The command adds the
    repository endpoint URL to the project level configuration file located at
    `/path/to/project/.swiftpm/configuration/registries.json`.

###### Note

The `aws codeartifact login` command
calls `swift package-registry` commands that must be run from the directory that contains the
`Package.swift` file. Because of this,
`aws codeartifact login` command must be run from within the Swift project.

###### To configure Swift with the login command

1. Navigate to the Swift project directory that contains your project's `Package.swift` file.
2. Run the following `aws codeartifact login` command.

If you are accessing a repository in a domain that you own, you don't need to include
`--domain-owner`. For more information, see [Cross-account domains](domain-overview.md#domain-overview-cross-account "domain-overview.md#domain-overview-cross-account").

```
aws codeartifact login --tool `swift` --domain `my_domain` \
--domain-owner `111122223333` --repository `my_repo` \
[--namespace `my_namespace`]
```

The `--namespace` option configures the application to only consume packages from
your CodeArtifact repository if they're in the designated namespace. [CodeArtifact namespaces](codeartifact-concepts.md#welcome-concepts-package-namespace "codeartifact-concepts.md#welcome-concepts-package-namespace") are synonymous with scopes, and are used to
organize code into logical groups and to
prevent name collisions that can occur when your code base includes multiple libraries.

The default authorization period after calling `login` is 12 hours, and `login` must
be called to periodically refresh the token. For more information about
the authorization token created with the `login` command, see
[Tokens created with the login command](tokens-authentication.md#auth-token-login "tokens-authentication.md#auth-token-login").

## Configure Swift without the login

command

While it is recommended that you [configure Swift with the aws codeartifact login command](#configure-swift-login-command "#configure-swift-login-command"),
you can also configure the Swift Package Manager without the login command by
manually updating the Swift Package Manager configuration.

In the following procedure, you will use the AWS CLI to do the following:

1. Fetch an authentication token from CodeArtifact and store it in your environment. How the credentials are stored
   depends on the operating system of the environment:
   1. **macOS:** An entry is created in the macOS Keychain application.
   2. **Linux and Windows:** An entry is created in the `~/.netrc` file.

2. Fetch your CodeArtifact repository endpoint URL.
3. In the `~/.swiftpm/configuration/registries.json` configuration file, add an entry
   with your repository endpoint URL and authentication type.

###### To configure the Swift without the login command

1. In a command line, use the following command to fetch a CodeArtifact authorization token and store it in an environment variable.
   - Replace `my_domain` with your CodeArtifact domain name.
   - Replace `111122223333` with the AWS account ID of the owner of the domain. If you are accessing a repository in a domain that you own, you don't need to include
     `--domain-owner`. For more information, see [Cross-account domains](domain-overview.md#domain-overview-cross-account "domain-overview.md#domain-overview-cross-account").

macOS and Linux

```
export CODEARTIFACT_AUTH_TOKEN=`aws codeartifact get-authorization-token --domain `my_domain` --domain-owner `111122223333` --query authorizationToken --output text`
```

Windows

    * Windows (using default command shell):



    ```
    for /f %i in ('aws codeartifact get-authorization-token --domain `my_domain` --domain-owner `111122223333` --query authorizationToken --output text') do set CODEARTIFACT_AUTH_TOKEN=%i
    ```
    * Windows PowerShell:



    ```
    $env:CODEARTIFACT_AUTH_TOKEN = aws codeartifact get-authorization-token --domain `my_domain` --domain-owner `111122223333` --query authorizationToken --output text
    ```

2. Get your CodeArtifact repository's endpoint by running the following command. Your repository endpoint is used to point the Swift
   Package Manager to your repository to consume or publish packages.
   - Replace `my_domain` with your CodeArtifact domain name.
   - Replace `111122223333` with the AWS account ID of the owner of the domain. If you are accessing a repository in a domain that you own, you don't need to include
     `--domain-owner`. For more information, see [Cross-account domains](domain-overview.md#domain-overview-cross-account "domain-overview.md#domain-overview-cross-account").
   - Replace `my_repo` with your CodeArtifact repository name.

macOS and Linux

```
export CODEARTIFACT_REPO=`aws codeartifact get-repository-endpoint --domain `my_domain` --domain-owner `111122223333` --repository `my_repo` --format swift --query repositoryEndpoint --output text`
```

Windows

    * Windows (using default command shell):



    ```
    for /f %i in ('aws codeartifact get-repository-endpoint --domain `my_domain` --domain-owner `111122223333` --repository `my_repo` --format swift --query repositoryEndpoint --output text') do set CODEARTIFACT_REPO=%i
    ```
    * Windows PowerShell:



    ```
    $env:CODEARTIFACT_REPO = aws codeartifact get-repository-endpoint --domain `my_domain` --domain-owner `111122223333` --repository `my_repo` --format swift --query repositoryEndpoint --output text
    ```

The following URL is an example repository endpoint.

```
https://`my_domain`-111122223333.d.codeartifact.`us-west-2`.amazonaws.com/swift/`my_repo`/
```

###### Note

To use a dualstack endpoint, use the `codeartifact.`region`.on.aws` endpoint.

###### Important

You must append `login` onto the end of the repository URL endpoint when used to configure the Swift Package Manager. This
is done for you in the commands of this procedure. 3. With these two values stored in environment variables,
pass them to Swift using the `swift package-registry login` command as follows:

macOS and Linux

```
swift package-registry login ${CODEARTIFACT_REPO}login --token ${CODEARTIFACT_AUTH_TOKEN}
```

Windows

    * Windows (using default command shell):



    ```
    swift package-registry login %CODEARTIFACT_REPO%login --token %CODEARTIFACT_AUTH_TOKEN%
    ```
    * Windows PowerShell:



    ```
    swift package-registry login $Env:CODEARTIFACT_REPO+"login" --token $Env:CODEARTIFACT_AUTH_TOKEN
    ```

4. Next, update the package registry used by your application so that any dependency will be pulled from your CodeArtifact repository.
   This command must be run in the project directory where you are trying to resolve the package dependency:

macOS and Linux

```
$ swift package-registry set ${CODEARTIFACT_REPO} [--scope `my_scope`]
```

Windows

    * Windows (using default command shell):



    ```
    $ swift package-registry set %CODEARTIFACT_REPO% [--scope `my_scope`]
    ```
    * Windows PowerShell:



    ```
    $ swift package-registry set $Env:CODEARTIFACT_REPO [--scope `my_scope`]
    ```

The `--scope` option configures the application to only consume packages from
your CodeArtifact repository if they're in the designated scope. Scopes are synonymous with [CodeArtifact namespaces](codeartifact-concepts.md#welcome-concepts-package-namespace "codeartifact-concepts.md#welcome-concepts-package-namespace"), and are used to organize code into logical groups and to
prevent name collisions that can occur when your code base includes multiple libraries. 5. You can confirm the configuration has been set up correctly by viewing the contents of the project level
`.swiftpm/configuration/registries.json` file by running the following command in your project directory:

```
$ cat .swiftpm/configuration/registries.json
{
  "authentication" : {

  },
  "registries" : {
    "[default]" : {
      "url" : "https://my-domain-111122223333.d.codeartifact.us-west-2.amazonaws.com/swift/my-repo/"
    }
  },
  "version" : 1
}
```

Now that you've configured the Swift Package Manager with your CodeArtifact repository, you can use it to publish and consume Swift
packages to and from it. For more information, see [Consuming and publishing Swift packages](swift-publish-consume.md "swift-publish-consume.md").
