#

Update the runtime version in the buildspec file

You can modify the runtime used by your project to a new version by updating the
`runtime-versions` section of your buildspec file. The following examples
show how to specify java versions 8 and 11.

- A `runtime-versions` section that specifies version 8 of
  Java:

```
phases:
  install:
    runtime-versions:
      java: corretto8
```

- A `runtime-versions` section that specifies version 11 of
  Java:

```
phases:
  install:
    runtime-versions:
      java: corretto11
```

The following examples show how to specify different versions of Python using the
Ubuntu standard image 5.0 or the Amazon Linux 2 standard image 3.0:

- A `runtime-versions` section that specifies Python version 3.7:

```
phases:
  install:
    runtime-versions:
      python: 3.7
```

- A `runtime-versions` section that specifies Python version 3.8:

```
phases:
  install:
    runtime-versions:
      python: 3.8
```

This sample demonstrates a project that starts with the Java version 8 runtime, and
then is updated to the Java version 10 runtime.

1. Download and install Maven. For information, see [Downloading Apache Maven](https://maven.apache.org/download.cgi "https://maven.apache.org/download.cgi")
   and [Installing Apache
   Maven](https://maven.apache.org/install.html "https://maven.apache.org/install.html") on the Apache Maven website.
2. Switch to an empty directory on your local computer or instance, and then run
   this Maven command.

```
mvn archetype:generate "-DgroupId=com.mycompany.app" "-DartifactId=ROOT" "-DarchetypeArtifactId=maven-archetype-webapp" "-DinteractiveMode=false"
```

If successful, this directory structure and files are created.

```
.
└── ROOT
    ├── pom.xml
    └── src
        └── main
            ├── resources
            └── webapp
                ├── WEB-INF
                │   └── web.xml
                └── index.jsp
```

3. Create a file named `buildspec.yml` with the following
   contents. Store the file in the ``(root directory name)`/my-web-app`
   directory.

```
version: 0.2

phases:
  install:
    runtime-versions:
      java: corretto8
  build:
    commands:
      - java -version
      - mvn package
artifacts:
  files:
    - '**/*'
  base-directory: 'target/my-web-app'

```

In the buildspec file:

    * The `runtime-versions` section specifies that the project
     uses version 8 of the Java runtime.
    * The `- java -version` command displays the version of Java
     used by your project when it builds.

Your file structure should now look like this.

```
`(root directory name)`
└── my-web-app
    ├── src
    │   ├── main
    │   ├── resources
    │   └── webapp
    │       └── WEB-INF
    │           └── web.xml
    │               └── index.jsp
    ├── buildspec.yml
    └── pom.xml
```

4. Upload the contents of the `my-web-app` directory to an
   S3 input bucket or a CodeCommit, GitHub, or Bitbucket repository.

###### Important

Do not upload `(root directory
 name)` or ``(root directory
 name)`/my-web-app`, just the directories and
 files in ``(root directory
name)`/my-web-app`.

If you are using an S3 input bucket, be sure to create a ZIP file that
contains the directory structure and files, and then upload it to the input
bucket. Do not add `(root directory
 name)` or ``(root
 directory name)`/my-web-app` to the ZIP file,
 just the directories and files in ``(root
directory name)`/my-web-app`. 5. Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home"). 6. Create a build project. For more information, see [Create a build project (console)](create-project.md#create-project-console "create-project.md#create-project-console") and [Run a build (console)](run-build-console.md "run-build-console.md"). Leave all settings at their default values, except for these settings.

    * For **Environment**:




    	+ For **Environment image**, choose
    	 **Managed image**.
    	+ For **Operating system**, choose **Amazon Linux 2**.
    	+ For **Runtime(s)**, choose **Standard**.
    	+ For **Image**, choose
    	 **aws/codebuild/amazonlinux-x86\_64-standard:4.0**.

7. Choose **Start build**.
8. On **Build configuration**, accept the defaults, and then
   choose **Start build**.
9. After the build is complete, view the build output on the **Build
   logs** tab. You should see output similar to the following:

```
[Container] Date Time Phase is DOWNLOAD_SOURCE
[Container] Date Time CODEBUILD_SRC_DIR=/codebuild/output/src460614277/src
[Container] Date Time YAML location is /codebuild/output/src460614277/src/buildspec.yml
[Container] Date Time Processing environment variables
[Container] Date Time Selecting 'java' runtime version 'corretto8' based on manual selections...
[Container] Date Time Running command echo "Installing Java version 8 ..."
Installing Java version 8 ...

[Container] Date Time Running command export JAVA_HOME="$JAVA_8_HOME"

[Container] Date Time Running command export JRE_HOME="$JRE_8_HOME"

[Container] Date Time Running command export JDK_HOME="$JDK_8_HOME"

[Container] Date Time Running command for tool_path in "$JAVA_8_HOME"/bin/* "$JRE_8_HOME"/bin/*;
```

10. Update the `runtime-versions` section with Java version 11:

```
install:
    runtime-versions:
      java: corretto11
```

11. After you save the change, run your build again and view the build output.
    You should see that the installed version of Java is 11. You should see output
    similar to the following:

```
[Container] Date Time Phase is DOWNLOAD_SOURCE
[Container] Date Time CODEBUILD_SRC_DIR=/codebuild/output/src460614277/src
[Container] Date Time YAML location is /codebuild/output/src460614277/src/buildspec.yml
[Container] Date Time Processing environment variables
[Container] Date Time Selecting 'java' runtime version 'corretto11' based on manual selections...
Installing Java version 11 ...

[Container] Date Time Running command export JAVA_HOME="$JAVA_11_HOME"

[Container] Date Time Running command export JRE_HOME="$JRE_11_HOME"

[Container] Date Time Running command export JDK_HOME="$JDK_11_HOME"

[Container] Date Time Running command for tool_path in "$JAVA_11_HOME"/bin/* "$JRE_11_HOME"/bin/*;
```
