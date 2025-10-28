# Consuming and publishing Swift packages

## Consuming Swift packages from CodeArtifact

Use the following procedure to consume Swift packages from an AWS CodeArtifact repository.

###### To consume Swift packages from a CodeArtifact repository

1. If you haven't, follow the steps in [Configure the Swift Package Manager with CodeArtifact](configure-swift.md "configure-swift.md") to
   configure the Swift Package Manager to use your CodeArtifact repository with proper credentials.

###### Note

The authorization token generated is valid for 12 hours. You will need to create a new one if 12 hours have passed since a token was created. 2. Edit the `Package.swift` file in your application project folder to update the package dependencies to
be used by your project.

    1. If the `Package.swift` file does not contain a `dependencies` section, add one.
    2. In the `dependencies` section of the `Package.swift` file, add the package you want to use by adding its package identifier.
     The package identifier consists of the scope and package name separated by a period. See the code snippet following a later step for an example.


    ###### Tip

    To find the package identifier, you can use the CodeArtifact console. Find the specific package version you want to use and reference
     the **Install shortcut** instructions on the package version page.
    3. If the `Package.swift` file does not contain a `targets` section, add one.
    4. In the `targets` section, add the targets that will need to use the dependency.


    The following snippet is an example snippet showing configured `dependencies` and `targets` sections
     in a `Package.swift` file:



    ```
    ...
        ],
        dependencies: [
            .package(id: "`my_scope`.`package_name`", from: "`1.0.0`")
        ],
        targets: [
          .target(
             name: "`MyApp`",
             dependencies: ["`package_name`"]
          ),...
        ],
    ...
    ```

3. Now that everything is configured, use the following command to download the package dependencies from CodeArtifact.

```
swift package resolve
```

## Consuming Swift packages from CodeArtifact in Xcode

Use the following procedure to consume Swift packages from a CodeArtifact repository in Xcode.

###### To consume Swift packages from a CodeArtifact repository in Xcode

1. If you haven't, follow the steps in [Configure the Swift Package Manager with CodeArtifact](configure-swift.md "configure-swift.md") to
   configure the Swift Package Manager to use your CodeArtifact repository with proper credentials.

###### Note

The authorization token generated is valid for 12 hours. You will need to create a new one if 12 hours have passed since a token was created. 2. Add the packages as a dependency in your project in Xcode.

    1. Choose **File > Add Packages**.
    2. Search for your package using the search bar. Your search must be in the form `package_scope.package_name`.
    3. Once found, choose the package and choose **Add Package**.
    4. Once the package is verified, choose the package products you want to add as a dependency,
     and choose **Add Package**.

If you run into problems using your CodeArtifact repository with Xcode, see [Swift troubleshooting](swift-troubleshooting.md "swift-troubleshooting.md") for common issues
and possible fixes.

## Publishing Swift packages to CodeArtifact

CodeArtifact recommends Swift 5.9 or later and using the `swift package-registry publish` command to publish Swift packages. If you are using an earlier
version, you must use a Curl command to publish Swift packages to CodeArtifact.

### Publishing CodeArtifact packages with the `swift package-registry publish` command

Use the following procedure with Swift 5.9 or later to publish Swift packages to a CodeArtifact repository with the Swift Package Manager.

1. If you haven't, follow the steps in [Configure the Swift Package Manager with CodeArtifact](configure-swift.md "configure-swift.md") to
   configure the Swift Package Manager to use your CodeArtifact repository with proper credentials.

###### Note

The authorization token generated is valid for 12 hours. You will need to create a new one if 12 hours have passed since it was created. 2. Navigate to the Swift project directory that contains the `Package.swift` file for your package. 3. Run the following `swift package-registry publish` command to publish the package. The command creates a
package source archive and publishes it to your CodeArtifact repository.

```
swift package-registry publish `packageScope`.`packageName` `packageVersion`
```

For example:

```
swift package-registry publish `myScope`.`myPackage` `1.0.0`
```

4. You can confirm that the package was published and exists in the repository by checking in the console or using
   the `aws codeartifact list-packages` command as follows:

```
aws codeartifact list-packages --domain `my_domain` --repository `my_repo`
```

You can list the single version of the package using the `aws codeartifact list-package-versions` command
as follows:

```
aws codeartifact list-package-versions --domain `my_domain` --repository `my_repo` \
--format swift --namespace `my_scope` --package `package_name`
```

### Publishing CodeArtifact packages with Curl

While it is recommended to use the `swift package-registry publish` command that comes with Swift 5.9 or later,
you can also use Curl to publish Swift packages to CodeArtifact.

Use the following procedure to publish Swift packages to an AWS CodeArtifact repository with Curl.

1. If you haven't, create and update the `CODEARTIFACT_AUTH_TOKEN` and
   `CODEARTIFACT_REPO` environment variables by following the steps in
   [Configure the Swift Package Manager with CodeArtifact](configure-swift.md "configure-swift.md").

###### Note

The authorization token is valid for 12 hours. You will need to refresh your
`CODEARTIFACT_AUTH_TOKEN` environment variable with new credentials if 12 hours have passed since it was created. 2. First, if you do not have a Swift package created, you can do so by running the following commands:

```
mkdir `testDir` && cd `testDir`
swift package init
git init .
swift package archive-source
```

3. Use the following Curl command to publish your Swift package to CodeArtifact:

macOS and Linux

```
curl -X PUT  --user "aws:$CODEARTIFACT_AUTH_TOKEN" \
-H "Accept: application/vnd.swift.registry.v1+json" \
-F source-archive="@`test_dir_package_name`.zip" \
"${CODEARTIFACT_REPO}`my_scope`/`package_name`/`packageVersion`"
```

Windows

```
curl -X PUT  --user "aws:%CODEARTIFACT_AUTH_TOKEN%" \
-H "Accept: application/vnd.swift.registry.v1+json" \
-F source-archive="@`test_dir_package_name`.zip" \
"%CODEARTIFACT_REPO%`my_scope`/`package_name`/`packageVersion`"
```

4. You can confirm that the package was published and exists in the repository by checking in the console or using
   the `aws codeartifact list-packages` command as follows:

```
aws codeartifact list-packages --domain `my_domain` --repository `my_repo`
```

You can list the single version of the package using the `aws codeartifact list-package-versions` command
as follows:

```
aws codeartifact list-package-versions --domain `my_domain` --repository `my_repo` \
--format swift --namespace `my_scope` --package `package_name`
```

## Fetching Swift packages from GitHub and republishing to CodeArtifact

Use the following procedure to fetch a Swift package from GitHub and republish it to a CodeArtifact repository.

###### To fetch a Swift package from GitHub and republish it to CodeArtifact

1. If you haven't, follow the steps in [Configure the Swift Package Manager with CodeArtifact](configure-swift.md "configure-swift.md") to
   configure the Swift Package Manager to use your CodeArtifact repository with proper credentials.

###### Note

The authorization token generated is valid for 12 hours. You will need to create a new one if 12 hours have passed since a token was created. 2. Clone the git repository of the Swift package you want to fetch and republish by using the following `git clone` command.
For information about cloning GitHub repositories, see
[Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository "https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository")
in the GitHub Docs.

```
git clone `repoURL`
```

3. Navigate to the repository that you just cloned:

```
cd `repoName`
```

4. Create the package and publish it to CodeArtifact.
   1. **Recommended:** If you are using Swift 5.9 or later, you can use the
      following `swift package-registry publish` command to create the package and publish it to your configured CodeArtifact repository.

   ```
   swift package-registry publish `packageScope`.`packageName` `versionNumber`
   ```

   For example:

   ```
   swift package-registry publish `myScope`.`myPackage` `1.0.0`
   ```

   2. If you're using a Swift version that is older than 5.9, you must use the `swift archive-source`
      command to create the package and then use a Curl command to publish it.
      1. If you haven't configured the `CODEARTIFACT_AUTH_TOKEN` and
         `CODEARTIFACT_REPO` environment variables, or it's been over 12 hours since you have, follow the steps in
         [Configure Swift without the login
         command](configure-swift.md#configure-swift-without-login-command "configure-swift.md#configure-swift-without-login-command").
      2. Create the Swift package by using the `swift package archive-source` command:

      ```
      swift package archive-source
      ```

      If successful, you will see `Created `package_name`.zip` in the command line. 3. Use the following Curl command to publish the Swift package to CodeArtifact:

      macOS and Linux

      ```
      curl -X PUT  --user "aws:$CODEARTIFACT_AUTH_TOKEN" \
      -H "Accept: application/vnd.swift.registry.v1+json" \
      -F source-archive="@`package_name`.zip" \
      "${CODEARTIFACT_REPO}`my_scope`/`package_name`/`packageVersion`"
      ```

      Windows

      ```
      curl -X PUT  --user "aws:%CODEARTIFACT_AUTH_TOKEN%" \
      -H "Accept: application/vnd.swift.registry.v1+json" \
      -F source-archive="@`package_name`.zip" \
      "%CODEARTIFACT_REPO%`my_scope`/`package_name`/`packageVersion`"
      ```

5. You can confirm that the package was published and exists in the repository by checking in the console or using
   the `aws codeartifact list-packages` command as follows:

```
aws codeartifact list-packages --domain `my_domain` --repository `my_repo`
```

You can list the single version of the package using the `aws codeartifact list-package-versions` command
as follows:

```
aws codeartifact list-package-versions --domain `my_domain` --repository `my_repo` \
--format swift --namespace `my_scope` --package `package_name`
```
