# Specify a GitHub

repository version with a commit ID

You can specify a source version with only a commit ID, such as
`12345678901234567890123467890123456789`. If you do this, CodeBuild must
download the entire repository to find the version.

###### To specify a GitHub repository version with a commit ID

1. Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home").
2. Create a build project. For information, see [Create a build project (console)](create-project.md#create-project-console "create-project.md#create-project-console")
   and [Run a build (console)](run-build-console.md "run-build-console.md"). Leave
   all settings at their default values, except for these settings:
   - In **Source**:
     - For **Source provider**, choose
       **GitHub**. If you are not connected to
       GitHub, follow the instructions to connect.
     - For **Repository**, choose **Public
       repository**.
     - For **Repository URL**, enter
       `https://github.com/aws/aws-sdk-ruby.git`.

   - In **Environment**:
     - For **Environment image**, choose
       **Managed image**.
     - For **Operating system**, choose
       **Amazon Linux 2**.
     - For **Runtime(s)**, choose
       **Standard**.
     - For **Image**, choose
       **aws/codebuild/amazonlinux-x86_64-standard:4.0**.

3. For **Build specifications**, choose **Insert build
   commands**, and then choose **Switch to editor**.
4. In **Build commands**, replace the placeholder text with the
   following:

```
version: 0.2

phases:
  install:
    runtime-versions:
      ruby: 2.6
  build:
    commands:
       - echo $CODEBUILD_RESOLVED_SOURCE_VERSION
```

The `runtime-versions` section is required when you use the Ubuntu
standard image 2.0. Here, the Ruby version 2.6 runtime is specified, but you can
use any runtime. The `echo` command displays the version of the
source code stored in the `CODEBUILD_RESOLVED_SOURCE_VERSION`
environment variable. 5. On **Build configuration**, accept the defaults, and then
choose **Start build**. 6. For **Source version**, enter
`046e8b67481d53bdc86c3f6affdd5d1afae6d369`. This is the
SHA of a commit in the `https://github.com/aws/aws-sdk-ruby.git`
repository. 7. Choose **Start build**. 8. When the build is complete, you should see the following:

    * On the **Build logs** tab, which version of the
     project source was used. Here is an example.



    ```
    [Container] Date Time Running command echo $CODEBUILD_RESOLVED_SOURCE_VERSION
    046e8b67481d53bdc86c3f6affdd5d1afae6d369

    [Container] Date Time Phase complete: BUILD State: SUCCEEDED
    ```
    * On the **Environment variables** tab, the
     **Resolved source version** matches the commit ID
     used to create the build.
    * On the **Phase details** tab, the duration of the
     `DOWNLOAD_SOURCE` phase.
