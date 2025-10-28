#

Specify two runtimes

You can specify more than one runtime in the same CodeBuild build project. This sample
project uses two source files: one that uses the Go runtime and one that uses the
Node.js runtime.

1. Create a directory named `my-source`.
2. Inside the `my-source` directory, create a directory named
   `golang-app`.
3. Create a file named `hello.go` with the following contents.
   Store the file in the `golang-app` directory.

```
package main
import "fmt"

func main() {
  fmt.Println("hello world from golang")
  fmt.Println("1+1 =", 1+1)
  fmt.Println("7.0/3.0 =", 7.0/3.0)
  fmt.Println(true && false)
  fmt.Println(true || false)
  fmt.Println(!true)
  fmt.Println("good bye from golang")
}
```

4. Inside the `my-source` directory, create a directory named
   `nodejs-app`. It should be at the same level as the
   `golang-app` directory.
5. Create a file named `index.js` with the following contents.
   Store the file in the `nodejs-app` directory.

```
console.log("hello world from nodejs");
console.log("1+1 =" + (1+1));
console.log("7.0/3.0 =" + 7.0/3.0);
console.log(true && false);
console.log(true || false);
console.log(!true);
console.log("good bye from nodejs");
```

6. Create a file named `package.json` with the following
   contents. Store the file in the `nodejs-app` directory.

```
{
  "name": "mycompany-app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"run some tests here\""
  },
  "author": "",
  "license": "ISC"
}
```

7. Create a file named `buildspec.yml` with the following
   contents. Store the file in the `my-source` directory, at the
   same level as the `nodejs-app` and
   `golang-app` directories. The
   `runtime-versions` section specifies the Node.js version 12 and
   Go version 1.13 runtimes.

```
version: 0.2

phases:
  install:
    runtime-versions:
      golang: 1.13
      nodejs: 12
  build:
    commands:
      - echo Building the Go code...
      - cd $CODEBUILD_SRC_DIR/golang-app
      - go build hello.go
      - echo Building the Node code...
      - cd $CODEBUILD_SRC_DIR/nodejs-app
      - npm run test
artifacts:
  secondary-artifacts:
    golang_artifacts:
      base-directory: golang-app
      files:
        - hello
    nodejs_artifacts:
      base-directory: nodejs-app
      files:
        - index.js
        - package.json
```

8. Your file structure should now look like this.

```
my-source
├── golang-app
│   └── hello.go
├── nodejs.app
│   ├── index.js
│   └── package.json
└── buildspec.yml
```

9. Upload the contents of the `my-source` directory to an
   S3 input bucket or a CodeCommit, GitHub, or Bitbucket repository.

###### Important

If you are using an S3 input bucket, be sure to create a ZIP file that contains the directory structure and files,
and then upload it to the input bucket. Do not add `my-source` to the ZIP file, just the directories and files in
`my-source`. 10. Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home"). 11. Create a build project. For more information, see [Create a build project (console)](create-project.md#create-project-console "create-project.md#create-project-console") and [Run a build (console)](run-build-console.md "run-build-console.md"). Leave all settings at their default values, except for these settings.

    * For **Environment**:




    	+ For **Environment image**, choose
    	 **Managed image**.
    	+ For **Operating system**, choose
    	 **Amazon Linux 2**.
    	+ For **Runtime(s)**, choose
    	 **Standard**.
    	+ For **Image**, choose
    	 **aws/codebuild/amazonlinux-x86\_64-standard:4.0**.

12. Choose **Create build project**.
13. Choose **Start build**.
14. On **Build configuration**, accept the defaults, and then
    choose **Start build**.
15. After the build is complete, view the build output on the **Build
    logs** tab. You should see output similar to the following. It
    shows output from the Go and Node.js runtimes. It also shows output from the Go
    and Node.js applications.

```
[Container] Date Time Processing environment variables
[Container] Date Time Selecting 'golang' runtime version '1.13' based on manual selections...
[Container] Date Time Selecting 'nodejs' runtime version '12' based on manual selections...
[Container] Date Time Running command echo "Installing Go version 1.13 ..."
Installing Go version 1.13 ...

[Container] Date Time Running command echo "Installing Node.js version 12 ..."
Installing Node.js version 12 ...

[Container] Date Time Running command n $NODE_12_VERSION
   installed : v12.20.1 (with npm 6.14.10)

[Container] Date Time Moving to directory /codebuild/output/src819694850/src
[Container] Date Time Registering with agent
[Container] Date Time Phases found in YAML: 2
[Container] Date Time  INSTALL: 0 commands
[Container] Date Time  BUILD: 1 commands
[Container] Date Time Phase complete: DOWNLOAD_SOURCE State: SUCCEEDED
[Container] Date Time Phase context status code:  Message:
[Container] Date Time Entering phase INSTALL
[Container] Date Time Phase complete: INSTALL State: SUCCEEDED
[Container] Date Time Phase context status code:  Message:
[Container] Date Time Entering phase PRE_BUILD
[Container] Date Time Phase complete: PRE_BUILD State: SUCCEEDED
[Container] Date Time Phase context status code:  Message:
[Container] Date Time Entering phase BUILD
[Container] Date Time Running command echo Building the Go code...
Building the Go code...

[Container] Date Time Running command cd $CODEBUILD_SRC_DIR/golang-app

[Container] Date Time Running command go build hello.go

[Container] Date Time Running command echo Building the Node code...
Building the Node code...

[Container] Date Time Running command cd $CODEBUILD_SRC_DIR/nodejs-app

[Container] Date Time Running command npm run test

> mycompany-app@1.0.0 test /codebuild/output/src924084119/src/nodejs-app
> echo "run some tests here"

run some tests here
```
