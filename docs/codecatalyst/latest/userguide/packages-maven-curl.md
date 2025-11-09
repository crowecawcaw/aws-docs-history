Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Publishing packages with curl

This section shows how to use the HTTP client `curl` to publish Maven
packages to a CodeCatalyst package repository. Publishing packages with `curl` can
be useful if you do not have or want to install the Maven client in your
environments.

###### To publish a Maven package with `curl`

1. You must store a personal access token (PAT) into an environment variable to
   authenticate `curl` with CodeCatalyst. If you already have one, you can use
   that. If not, you can create one and configure the environment variable.
   1. Create a PAT by following the steps in [Grant users repository access with personal access tokens](ipa-tokens-keys.md "ipa-tokens-keys.md"). Copy the PAT to store it in an
      environment variable.
   2. On your local machine's command line, configure an environment
      variable with your PAT.

   ```
   export CodeCatalyst_ARTIFACTS_TOKEN=`your_PAT`
   ```

2. Use the following `curl` command to publish the JAR to a CodeCatalyst
   repository. Replace `username`,
   `space_name`, `proj_name`,
   and `repo_name` with your CodeCatalyst user name, space
   name, project name, and package repository name.

```
curl --request PUT https://packages.`region`.codecatalyst.aws/maven/`space-name`/`proj-name`/`repo-name`/`com`/`mycompany`/`app`/`my-app`/`1.0`/`my-app-1.0.jar` \
     --user "`username`:CodeCatalyst_ARTIFACTS_TOKEN" --header "Content-Type: application/octet-stream" \
     --data-binary @target/`path`/`to`/`my-app-1.0.jar`
```

3. Use the following `curl` command to publish the POM to a CodeCatalyst
   repository. Replace `username`,
   `space_name`, `proj_name`,
   and `repo_name` with your CodeCatalyst user name, space
   name, project name, and package repository name.

```
curl --request PUT https://packages.`region`.codecatalyst.aws/maven/`space-name`/`proj-name`/`repo-name`/`com`/`mycompany`/`app`/`my-app`/`1.0`/`my-app-1.0.pom` \
     --user "`username`:CodeCatalyst_ARTIFACTS_TOKEN" --header "Content-Type: application/octet-stream" \
     --data-binary @target/`my-app-1.0.pom`
```

4.  At this point, the Maven package will be in your CodeCatalyst repository with a
    status of `Unfinished`. To be able to consume the package, it must be
    in the `Published` state. You can move the package from
    `Unfinished` to `Published` by either uploading a
    `maven-metadata.xml` file to your package, or changing the status
    in the CodeCatalyst console.

        1. Option 1: Use the following `curl` command to add a
         `maven-metadata.xml` file to your package. Replace
         `username`,
         `space_name`,
         `proj_name`, and
         `repo_name` with your CodeCatalyst user name,
         space name, project name, and package repository name.



        ```
        curl --request PUT https://packages.`region`.codecatalyst.aws/maven/`space-name`/`proj-name`/`repo-name`/`com`/`mycompany`/`app`/`my-app`/`maven-metadata.xml` \
             --user "`username`:CodeCatalyst_ARTIFACTS_TOKEN" --header "Content-Type: application/octet-stream" \
             --data-binary @target/`maven-metadata.xml`
        ```

        Following is an example of the contents of a
         `maven-metadata.xml` file:



        ```
        <metadata modelVersion="1.1.0">
            <groupId>com.mycompany.app</groupId>
            <artifactId>my-app</artifactId>
            <versioning>
                <latest>1.0</latest>
                <release>1.0</release>
                <versions>
                    <version>1.0</version>
                </versions>
                <lastUpdated>20200731090423</lastUpdated>
            </versioning>
        </metadata>
        ```
        2. Option 2: Update the package status to `Published` in the
         CodeCatalyst console. For information about how to update a package version's
         status, see [Updating a package version's
         status](working-with-packages-update-version-status.md "working-with-packages-update-version-status.md").

    If you only have a package's JAR file, you can publish a consumable package version to
    a CodeCatalyst repository using `mvn`. This can be useful if you do not have access
    to the package's source code or POM. See [Publishing third-party
    packages](packages-maven-mvn.md#publishing-third-party-packages "packages-maven-mvn.md#publishing-third-party-packages") for details.
