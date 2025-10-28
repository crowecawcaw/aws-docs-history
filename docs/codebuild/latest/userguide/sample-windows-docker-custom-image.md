# Windows Docker builds sample for CodeBuild

The following sample builds and runs a Windows Docker image by using CodeBuild.

###### Topics

- [Run Windows Docker builds
  sample](#sample-windows-docker-build-running "#sample-windows-docker-build-running")

## Run Windows Docker builds

sample

Use the following procedure to run the Windows Docker builds.

###### To run Windows Docker builds sample

1. Create the files as described in the [Directory structure](#sample-windows-docker-custom-image-dir "#sample-windows-docker-custom-image-dir") and [Files](#sample-windows-docker-custom-image-files "#sample-windows-docker-custom-image-files") sections of this topic,
   and then upload them to an S3 input bucket or an AWS CodeCommit, GitHub, or Bitbucket
   repository.

###### Important

Do not upload `(root directory
 name)`, just the files inside of
`(root directory
 name)`.

If you are using an S3 input bucket, be sure to create a ZIP file that
contains the files, and then upload it to the input bucket. Do not add
`(root directory
 name)` to the ZIP file, just the files inside of
`(root directory
 name)`. 2. Create a `WINDOWS_EC2` fleet.

If you use the AWS CLI to create the fleet, the JSON-formatted input to the `create-fleet`
command might look similar to this. (Replace the placeholders with your own values.)

```
{
  "name": "`fleet-name`",
  "baseCapacity": 1,
  "environmentType": "WINDOWS_EC2",
  "computeType": "BUILD_GENERAL1_MEDIUM"
}
```

3. Create a build project, run the build, and view related build
   information.

If you use the AWS CLI to create the build project, the JSON-formatted input to
the `create-project` command might look similar to this.
(Replace the placeholders with your own values.)

```
{
  "name": "`project-name`",
  "source": {
    "type": "S3",
    "location": "`bucket-name`/DockerImageSample.zip"
  },
  "artifacts": {
    "type": "NO_ARTIFACTS"
  },
  "environment": {
    "type": "WINDOWS_EC2",
    "image": "Windows",
    "computeType": "BUILD_GENERAL1_MEDIUM",
    "fleet": {
       "fleetArn": "`fleet-arn`"
    }
  },
  "serviceRole": "arn:aws:iam::`account-ID`:role/`role-name`"
}
```

4. To see the build results, look in the build's log for the string `Hello,
World!`. For more information, see [View build details](view-build-details.md "view-build-details.md").

### Directory structure

This sample assumes this directory structure.

```
`(root directory name)`
├── buildspec.yml
└── Dockerfile
```

### Files

The base image of the operating system used in this sample is `mcr.microsoft.com/windows/servercore:ltsc2022`. The sample uses these files.

`buildspec.yml` (in `(root directory
 name)`)

```
version: 0.2

phases:
  pre_build:
    commands:
      - docker build -t helloworld .
  build:
    commands:
      - docker images
      - docker run helloworld powershell -Command "Write-Host 'Hello World!'"
```

`Dockerfile` (in `(root directory
 name)`)

```
FROM mcr.microsoft.com/windows/servercore:ltsc2022

RUN powershell -Command "Write-Host 'Hello World'"
```
