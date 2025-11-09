Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Configuring and using mvn

You use the `mvn` command to run Maven builds. You must configure
`mvn` to use your package repository and provide a personal access token
(PAT) for authentication.

###### Contents

- [Fetching dependencies from CodeCatalyst](packages-maven-mvn.md#mvn-fetch-dependencies "packages-maven-mvn.md#mvn-fetch-dependencies")
- [Fetching packages from external package repositories
  through CodeCatalyst](packages-maven-mvn.md#mvn-install-public "packages-maven-mvn.md#mvn-install-public")
- [Publishing packages to CodeCatalyst](packages-maven-mvn.md#mvn-publish-packages "packages-maven-mvn.md#mvn-publish-packages")
- [Publishing third-party
  packages](packages-maven-mvn.md#publishing-third-party-packages "packages-maven-mvn.md#publishing-third-party-packages")

## Fetching dependencies from CodeCatalyst

To configure `mvn` to fetch dependencies from a CodeCatalyst repository, you
must edit the Maven configuration file, `settings.xml` and
optionally, your project's Project Model Object (POM) file. The POM file contains
information about the project and configuration information for Maven to build the
project such as dependencies, build directory, source directory, test source
directory, plugin, and goals.

###### To use `mvn` to fetch dependencies from your CodeCatalyst package

repository

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. On the overview page for your project, choose
   **Packages**.
3. Choose your package repository from the list of package
   repositories.
4. Choose **Connect to repository**.
5. In the **Connect to repository** dialog box, choose
   **mvn** from the list of package manager
   clients.
6. You will need a personal access token (PAT) to authenticate
   `mvn` with CodeCatalyst. If you already have one, you can use that.
   If not, you can create one here.
   1. Choose **Create token**.
   2. Choose **Copy** to copy your PAT.

   ###### Warning

   You will not be able to see or copy your PAT again after you
   close the dialog box.

7. Add a profile containing your repository to your
   `settings.xml` file. Replace the following
   values.

###### Note

If copying from the console instructions, the following values should
be updated for you and should not be changed.

    * Replace `space_name` with your CodeCatalyst
     space name.
    * Replace `proj_name` with your CodeCatalyst
     project name.
    * Replace `repo_name` with your CodeCatalyst
     package repository name.

```
<profiles>
  <profile>
    <id>`repo_name`</id>
    <activation>
        <activeByDefault>true</activeByDefault>
    </activation>
    <repositories>
        <repository>
          <id>`repo_name`</id>
          <url>https://packages.`region`.codecatalyst.aws/maven/`space_name`/`proj_name`/`repo_name`/</url>
        </repository>
    </repositories>
  </profile>
</profiles>
```

8. Add your server to the list of servers in your
   `settings.xml` file. Replace the following
   values.

###### Note

If copying from the console instructions, the following values should
be updated for you and should not be changed.

    * Replace `repo_name` with your CodeCatalyst
     package repository name.
    * Replace `username` with your CodeCatalyst user
     name.
    * Replace `PAT` with your CodeCatalyst
     PAT.

```
<servers>
  <server>
    <id>`repo_name`</id>
    <username>`username`</username>
    <password>`PAT`</password>
  </server>
</servers>
```

9. (Optional) Set a mirror in your `settings.xml` file
   that captures all connections and routes them to your repository instead of
   a gateway repository.

###### Note

If copying from the console instructions, the following values should
be updated for you and should not be changed.

    * Replace `space_name` with your CodeCatalyst
     space name.
    * Replace `proj_name` with your CodeCatalyst
     project name.
    * Replace `repo_name` with your CodeCatalyst
     package repository name.

```
<mirrors>
  <mirror>
    <id>`repo_name`</id>
    <name>`repo_name`</name>
    <url>https://packages.`region`.codecatalyst.aws/maven/`space_name`/`proj_name`/`repo_name`/</url>
    <mirrorOf>*</mirrorOf>
  </mirror>
</mirrors>
```

###### Important

You can use any value in the `<id>` element, but it must be
the same in both the `<server>` and
`<repository>` elements. This enables the specified
credentials to be included in requests to CodeCatalyst.

After you make these configuration changes, you can build the project.

```
mvn compile
```

## Fetching packages from external package repositories

through CodeCatalyst

You can install Maven packages from public repositories through a CodeCatalyst
repository by configuring it with an upstream connection to the gateway that represents the gateway repository.
Packages installed from the gateway repository are ingested and stored in your CodeCatalyst
repository.

Currently, CodeCatalyst supports the following public Maven package repositories.

- maven-central-gateway
- google-android-gateway
- gradle-plugins-gateway
- commonsware-gateway

###### To install packages from public Maven package repositories

1. If you haven't already, configure `mvn` with your CodeCatalyst
   package repository by following the steps in [Fetching dependencies from CodeCatalyst](#mvn-fetch-dependencies "#mvn-fetch-dependencies").
2. Ensure your repository has added the gateway repository you want to install
   from as an upstream connection. To check which upstream sources are added or
   to add a gateway repository as an upstream source, followthe instructions in
   [Adding an upstream repository](packages-upstream-repositories-add.md "packages-upstream-repositories-add.md").

For more information about requesting packages from upstream repositories, see
[Requesting a package version with upstream repositories](packages-upstream-repositories-request.md "packages-upstream-repositories-request.md").

## Publishing packages to CodeCatalyst

To publish a Maven package with `mvn` to a CodeCatalyst repository, you must
also edit `~/.m2/settings.xml` and the project POM.

###### To use `mvn` to publish packages to your CodeCatalyst package

repository

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. On the overview page for your project, choose
   **Packages**.
3. Choose your package repository from the list of package
   repositories.
4. Choose **Connect to repository**.
5. In the **Connect to repository** dialog box, choose
   **mvn** from the list of package manager
   clients.
6. You will need a personal access token (PAT) to authenticate
   `mvn` with CodeCatalyst. If you already have one, you can use that.
   If not, you can create one here.
   1. Choose **Create token**.
   2. Choose **Copy** to copy your PAT.

   ###### Warning

   You will not be able to see or copy your PAT again after you
   close the dialog box.

7. Configure an environment variable on your local machine with your PAT. You
   will use this environment variable in your `setting.xml`
   file.

```
export CODECATALYST_ARTIFACTS_TOKEN=`your_PAT`
```

8. Add a `<servers>` section to
   `settings.xml` with a reference to the
   `CodeCatalyst_ARTIFACTS_TOKEN` environment variable so that Maven
   passes the token in HTTP requests.

```
<settings>
...
    <servers>
        <server>
            <id>`repo-name`</id>
            <username>`username`</username>
            <password>${env.CodeCatalyst_ARTIFACTS_TOKEN}</password>
        </server>
    </servers>
...
</settings>
```

9. Add a `<distributionManagement>` section to your
   project's `pom.xml`.

```
<project>
...
     <distributionManagement>
         <repository>
             <id>`repo_name`</id>
             <name>`repo_name`</name>
             <url>https://packages.`region`.codecatalyst.aws/maven/`space_name`/`proj_name`/`repo_name`/</url>
         </repository>
     </distributionManagement>
...
</project>
```

After you make these configuration changes, you can build the project and publish
it to the specified repository.

```
mvn deploy
```

You can navigate to your package repository in the CodeCatalyst console to check that
the package was successfully published.

## Publishing third-party

packages

You can publish third-party Maven packages to a CodeCatalyst repository with `mvn
 deploy:deploy-file`. This can be helpful to users that want to publish
packages and only have JAR files and don't have access to package source code or POM
files.

The `mvn deploy:deploy-file` command will generate a POM file based on
the information passed in the command line.

First, create a PAT if you do not have one.

###### To create a personal access token (PAT)

1. In the top menu bar, choose your profile badge, and then choose **My
   settings**.

###### Tip

You can also find your user profile by going to the members page for a project or
space and choosing your name from the members list. 2. In **PAT name**, enter a descriptive name for your PAT. 3. In **Expiration date**, leave the default date or choose the calendar
icon to select a custom date. The expiration date defaults to one year from the current
date. 4. Choose **Create**.

You can also create this token when you choose **Clone repository** for a
source repository. 5. Save the PAT secret in a secure location.

###### Important

The PAT secret only displays once. You cannot retrieve it after you close the window.

###### To publish third-party Maven packages

1. Create a `~/.m2/settings.xml` file with the following
   contents:

```

<settings>
    <servers>
        <server>
            <id>`repo_name`</id>
            <username>`username`</username>
            <password>`PAT`}</password>
        </server>
    </servers>
</settings>

```

2. Run the `mvn deploy:deploy-file` command:

```
mvn deploy:deploy-file -DgroupId=commons-cli          \
-DartifactId=commons-cli       \
-Dversion=1.4                  \
-Dfile=./commons-cli-1.4.jar   \
-Dpackaging=jar                \
-DrepositoryId=`repo-name`      \
-Durl=https://packages.`region`.codecatalyst.aws/maven/`space-name`/`proj-name`/`repo-name`/

```

###### Note

The preceding example publishes `commons-cli 1.4`. Modify
the groupId, artifactID, version, and file arguments to publish a
different JAR.

These instructions are based on examples in the [Guide to deploying 3rd party JARs to remote repository](https://maven.apache.org/guides/mini/guide-3rd-party-jars-remote.html "https://maven.apache.org/guides/mini/guide-3rd-party-jars-remote.html") from the
_Apache Maven documentation_.

For more information, see these topics on the Apache Maven Project website:

- [Setting up Multiple Repositories](https://maven.apache.org/guides/mini/guide-multiple-repositories.html "https://maven.apache.org/guides/mini/guide-multiple-repositories.html")
- [Settings Reference](https://maven.apache.org/settings.html "https://maven.apache.org/settings.html")
- [Distribution Management](https://maven.apache.org/pom.html#Distribution_Management "https://maven.apache.org/pom.html#Distribution_Management")
- [Profiles](https://maven.apache.org/pom.html#Profiles "https://maven.apache.org/pom.html#Profiles")
