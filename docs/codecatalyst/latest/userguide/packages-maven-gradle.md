Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Configuring and using Gradle Groovy

To use Gradle Groovy with CodeCatalyst, you must connect Gradle Groovy to your package repository and
provide a personal access token (PAT) for authentication. You can view instructions for
connecting Gradle Groovy to your package repository in the CodeCatalyst console.

###### Contents

- [Fetching dependencies from
  CodeCatalyst](packages-maven-gradle.md#gradle-fetch-dependencies "packages-maven-gradle.md#gradle-fetch-dependencies")
- [Fetching plugins from CodeCatalyst](packages-maven-gradle.md#gradle-fetch-plugins "packages-maven-gradle.md#gradle-fetch-plugins")
- [Fetching packages from external package
  repositories through CodeCatalyst](packages-maven-gradle.md#gradle-install-public "packages-maven-gradle.md#gradle-install-public")
- [Publishing packages to CodeCatalyst](packages-maven-gradle.md#gradle-publish-packages "packages-maven-gradle.md#gradle-publish-packages")
- [Running a Gradle build in IntelliJ IDEA](packages-maven-gradle.md#gradle-intellij "packages-maven-gradle.md#gradle-intellij")
  - [Method 1: Put the PAT in
    gradle.properties](packages-maven-gradle.md#gradle-intellij-gradle-properties "packages-maven-gradle.md#gradle-intellij-gradle-properties")
  - [Method 2: Put the PAT in a separate
    file](packages-maven-gradle.md#gradle-intellij-file "packages-maven-gradle.md#gradle-intellij-file")

## Fetching dependencies from

CodeCatalyst

The following instructions explain how to configure Gradle Groovy to fetch dependencies
your CodeCatalyst package repository.

###### To use Gradle Groovy to fetch dependencies from your CodeCatalyst package

repository

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your project.
3. In the navigation pane, choose **Packages**.
4. Choose your package repository from the list of package
   repositories.
5. Choose **Connect to repository**.
6. In the **Connect to repository** dialog box, choose
   **Gradle Groovy** from the list of package manager
   clients.
7. You will need a personal access token (PAT) to authenticate Gradle Groovy with
   CodeCatalyst. If you already have one, you can use that. If not, you can create
   one here.
   1. Choose **Create token**.
   2. Choose **Copy** to copy your PAT.

   ###### Warning

   You will not be able to see or copy your PAT again after you
   close the dialog box.

8. Update your gradle properties file with your access credentials. Replace
   `username` with your CodeCatalyst username and
   replace `PAT` with your CodeCatalyst personal access
   token. You can use any value for `spaceUsername` and
   `spacePassword` as long as you use the same
   values in the following steps.

```
`spaceUsername`=`username`
`spacePassword`=`PAT`
```

9. To fetch dependencies from CodeCatalyst in a Gradle build, copy the
   `maven` code snippet and add it to the
   `repositories` section in your project's
   `build.gradle` file. Replace the following values. You can use
   any value for `spaceName` as long as you use the same
   values in the following steps.

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
maven {
  name = '`spaceName`'
  url = uri('https://packages.`region`.codecatalyst.aws/maven/`space_name`/`proj_name`/`repo_name`/')
  credentials(PasswordCredentials)
}
```

10. (Optional) To use the CodeCatalyst package repository as the only source for
    your project dependencies, remove any other sections in repositories from
    the `build.gradle` file. If you have more than one repository,
    Gradle searches each repository for dependencies in the order they are
    listed.

## Fetching plugins from CodeCatalyst

By default Gradle will resolve plugins from the public [Gradle Plugin Portal](https://plugins.gradle.org/ "https://plugins.gradle.org/"). The following
steps configure your Gradle project to resolve plugins from your CodeCatalyst package
repository.

###### To use Gradle to fetch plugins from your CodeCatalyst package repository

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your project.
3. In the navigation pane, choose **Packages**.
4. Choose your package repository from the list of package
   repositories.
5. Choose **Connect to repository**.
6. In the **Connect to repository** dialog box, choose
   **Gradle** from the list of package manager
   clients.
7. You will need a personal access token (PAT) to authenticate Gradle with
   CodeCatalyst. If you already have one, you can use that. If not, you can create
   one here.
   1. Choose **Create token**.
   2. Choose **Copy** to copy your PAT.

   ###### Warning

   You will not be able to see or copy your PAT again after you
   close the dialog box.

8. Update your gradle properties file with your access credentials. Replace
   `username` with your CodeCatalyst username and
   replace `PAT` with your CodeCatalyst personal access
   token. You can use any value for `spaceUsername` and
   `spacePassword` as long as you use the same
   values in the following steps.

```
`spaceUsername`=`username`
`spacePassword`=`PAT`
```

9. Add a `pluginManagement` block to your
   `settings.gradle` file. The `pluginManagement`
   block must appear before any other statements in
   `settings.gradle`. Replace the following values.

###### Note

If copying from the console instructions, the following values should
be updated for you and should not be changed.

    * Replace `spaceName` with the name
     value used in the previous step.
    * Replace `space_name` with your CodeCatalyst
     space name.
    * Replace `proj_name` with your CodeCatalyst
     project name.
    * Replace `repo_name` with your CodeCatalyst
     package repository name.

```
pluginManagement {
    repositories {
        maven {
            name = '`spaceName`'
            url = uri('https://packages.`region`.codecatalyst.aws/maven/`space_name`/`proj_name`/`repo_name`/')
            credentials(PasswordCredentials)
        }
    }
}
```

This will ensure that Gradle resolves plugins from the specified
repository. The repository must have an upstream connection configured to
the Gradle Plugin Portal (`gradle-plugins-store`) so that
commonly required Gradle plugins are available to the build. For more
information, see the [Gradle documentation](https://docs.gradle.org/current/userguide/plugins.html#sec:custom_plugin_repositories "https://docs.gradle.org/current/userguide/plugins.html#sec:custom_plugin_repositories").

## Fetching packages from external package

repositories through CodeCatalyst

You can install Maven packages from public repositories through a CodeCatalyst
repository by configuring it with an upstream connection to the gateway that represents the gateway repository.
Packages installed from the gateway repository are ingested and stored in your CodeCatalyst
repository.

CodeCatalyst supports the following public Maven package repositories.

- maven-central-gateway
- google-android-gateway
- gradle-plugins-gateway
- commonsware-gateway

###### To install packages from public Maven package repositories

1. If you haven't already, configure Gradle with your CodeCatalyst package
   repository by following the steps in [Fetching dependencies from
   CodeCatalyst](#gradle-fetch-dependencies "#gradle-fetch-dependencies") or [Fetching plugins from CodeCatalyst](#gradle-fetch-plugins "#gradle-fetch-plugins").
2. Ensure that your repository has added the gateway repository you want to
   install from as an upstream connection. You can do this by following the
   instructions in [Adding an upstream repository](packages-upstream-repositories-add.md "packages-upstream-repositories-add.md") and choosing the
   public package repository you want to add as an upstream.

For more information about requesting packages from upstream repositories, see
[Requesting a package version with upstream repositories](packages-upstream-repositories-request.md "packages-upstream-repositories-request.md").

## Publishing packages to CodeCatalyst

This section describes how to publish a Java library built with Gradle Groovy to a CodeCatalyst
repository.

###### To use Gradle Groovy to publish packages to a CodeCatalyst package repository

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. On the overview page for your project, choose
   **Packages**.
3. Choose your package repository from the list of package
   repositories.
4. Choose **Connect to repository**.
5. In the **Connect to repository** dialog box, choose
   **Gradle Groovy** from the list of package manager
   clients.
6. You will need a personal access token (PAT) to authenticate Gradle with
   CodeCatalyst. If you already have one, you can use that. If not, you can create
   one here.
   1. Choose **Create token**.
   2. Choose **Copy** to copy your PAT.

   ###### Warning

   You will not be able to see or copy your PAT again after you
   close the dialog box.

7. Update your gradle properties file with your access credentials. Replace
   `username` with your CodeCatalyst username and
   replace `PAT` with your CodeCatalyst personal access
   token. You can use any value for `spaceUsername` and
   `spacePassword` as long as you use the same
   values in the following steps.

```
`spaceUsername`=`username`
`spacePassword`=`PAT`
```

8. Add the `maven-publish` plugin to the `plugins`
   section of the project's `build.gradle` file.

```
plugins {
    id 'java-library'
    id 'maven-publish'
}
```

9. Next, add a `publishing` section to the project
   `build.gradle` file. Replace the following
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
publishing {
    publications {
        mavenJava(MavenPublication) {
            groupId = '`group-id`'
            artifactId = '`artifact-id`'
            version = '`version`'
            from components.java
        }
    }
    repositories {
        maven {
            name = '`spaceName`'
            url = uri('https://packages.`region`.codecatalyst.aws/maven/`space_name`/`proj_name`/`repo_name`/')
            credentials(PasswordCredentials)
        }
    }
}
```

The `maven-publish` plugin generates a POM file based on the
`groupId`, `artifactId`, and `version`
specified in the `publishing` section. 10. After these changes to `build.gradle` are complete, run
the following command to build the project and upload it to the
repository.

```
./gradlew publish
```

11. Navigate to your package repository in the CodeCatalyst console to check that
    the package was successfully published. You should see the package in the
    **Packages** list of your package repository.

For more information, see these topics on the Gradle website:

- [Building
  Java Libraries](https://guides.gradle.org/building-java-libraries/ "https://guides.gradle.org/building-java-libraries/")
- [Publishing a project as a module](https://docs.gradle.org/current/userguide/publishing_setup.html "https://docs.gradle.org/current/userguide/publishing_setup.html")

## Running a Gradle build in IntelliJ IDEA

You can run a Gradle build in IntelliJ IDEA that pulls dependencies from CodeCatalyst.
To authenticate Gradle with CodeCatalyst, you must use a personal access token (PAT). You
can store your CodeCatalyst PAT in `gradle.properties` or a separate file of
your choice.

### Method 1: Put the PAT in

`gradle.properties`

Use this method if you are not using the `gradle.properties` file
and can overwrite its contents with your PAT. If you are using
`gradle.properties`, you can modify this method to add the PAT
instead of overwriting the file's contents.

###### Note

The example shows the `gradle.properties` file located in
`GRADLE_USER_HOME`.

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

Next, update your `build.gradle` file with the following
snippet:

```
repositories {
    maven {
        name = '`spaceName`'
        url = uri('https://packages.`region`.codecatalyst.aws/maven/`space_name`/`proj_name`/`repo_name`/')
        credentials(PasswordCredentials)
    }
}
```

### Method 2: Put the PAT in a separate

file

Use this method if you do not want to modify your
`gradle.properties` file.

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

###### To put your PAT in a separate file

1. Update your `build.gradle` file with the following snippet.
   Replace `space_name`,
   `proj_name`, and
   `repo_name` with your CodeCatalyst user name,
   space name, project name, and package repository name.

```
def props = new Properties()
file("`fileName`").withInputStream { props.load(it) }

repositories {
        maven {
            name = '`spaceName`'
            url = uri('https://packages.`region`.codecatalyst.aws/maven/`space_name`/`proj_name`/`repo_name`/')
            credentials(PasswordCredentials)
        }
    }
}
```

2. Write your PAT into the file that was specified in your
   `build.gradle` file:

```
echo "codecatalystArtifactsToken=`PAT`" > `fileName`
```
