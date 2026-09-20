

# Building container images for Beanstalk Cluster environments
<a name="beanstalk-cluster-app-versions"></a>

A Beanstalk Cluster environment runs an application from a container image. As with Beanstalk Standard, an *application version* is deployed to the environment. In a Beanstalk Cluster environment, the application version supplies either an image that Elastic Beanstalk runs as-is or source that Elastic Beanstalk builds into an image. This topic covers the prerequisites, both creation paths, processing status, and the deletion behavior specific to Beanstalk Cluster environments. Deploying, tagging, and version quotas work the same way in both modes, as do the general creation and deletion procedures. See [Managing application versions](applications-versions.md) and [Tagging application versions](applications-versions-tagging.md).

For a Beanstalk Cluster deployment, create the application version with an `ImageConfiguration` that carries exactly one of two members. `Source` identifies a container image that is already built, and `Build` specifies how Elastic Beanstalk builds an image from a source bundle. Elastic Beanstalk rejects a `CreateApplicationVersion` request whose `ImageConfiguration` supplies both members or neither, a request that supplies both `ImageConfiguration.Source` and a `SourceBundle`, and a request that combines `ImageConfiguration` with the `BuildConfiguration` parameter, which configures AWS CodeBuild application versions for Beanstalk Standard. The following sections describe each path.

## Prerequisites
<a name="beanstalk-cluster-app-versions-prerequisites"></a>

The examples in this topic use the AWS CLI. Install and configure it before running the commands; they use the account and AWS Region in your AWS CLI configuration. See [Before you begin](beanstalk-cluster-getting-started.md#beanstalk-cluster-getting-started-prerequisites).

Prepare the following resources and access:
+ For a source build, the `CodeBuildServiceRole` required by `ImageConfiguration.Build`. This is the environment's *image build role*, which the Elastic Beanstalk console creates as `aws-elasticbeanstalk-eks-image-build-role`. For its trusted service and policies, and for the role boundary, see [Roles that you provide](beanstalk-cluster-permissions.md#beanstalk-cluster-permissions-customer-roles) and [Permissions for Beanstalk Cluster](beanstalk-cluster-permissions.md).
+ For an `ImageConfiguration.Source`, a container image that has already been pushed to its registry. The node role used by the environment must be able to pull the image. See [Roles that you provide](beanstalk-cluster-permissions.md#beanstalk-cluster-permissions-customer-roles).
+ For a source build, a `SourceBundle`, an Amazon S3 object containing the application source. Create the archive as described in [Create an Elastic Beanstalk application source bundle](applications-sourcebundle.md), upload it to an Amazon S3 bucket in your account, and pass the bucket and object key as `S3Bucket` and `S3Key`. Set `Process` to `true` to start the build; otherwise the version remains `UNPROCESSED`.

## Container image input
<a name="beanstalk-cluster-app-versions-image"></a>

Supply an `ImageConfiguration` with a `Source` member for a container image that is already built and pushed to a registry. Elastic Beanstalk runs the image without a build step. The `Source` carries a single field, `Uri`, that points at the image. The image can be in Amazon Elastic Container Registry (Amazon ECR), or in any registry that allows an unauthenticated pull. For a private image, use Amazon ECR: the environment's node role authenticates to it. An application version created from a provided image needs no build, so Elastic Beanstalk records it with the status `UNPROCESSED` and it is ready to deploy to a Beanstalk Cluster environment.

Elastic Beanstalk records the URI exactly as you supply it, whether it names a tag or a digest. An image that Elastic Beanstalk builds is recorded by digest.

Use this shape when a separate pipeline builds the image or when an image produced by a previous application version is deployed. To have Elastic Beanstalk build the image, provide a source bundle and a `Build` member as described next.

## Provide source for Elastic Beanstalk to build
<a name="beanstalk-cluster-app-versions-source"></a>

Supply a `SourceBundle` when Elastic Beanstalk must build the container image from application source. The `SourceBundle` identifies the source archive in Amazon Simple Storage Service (Amazon S3) with two fields, `S3Bucket` and `S3Key`. A source bundle also requires an `ImageConfiguration` whose `Build` member specifies how Elastic Beanstalk converts the source into an image. Set `Process` to `true` in the `CreateApplicationVersion` request to start the build; with the AWS CLI, use `--process`. If you omit this setting, the source-based application version remains `UNPROCESSED` and the build does not start. When processing starts, Elastic Beanstalk builds the image and pushes it to Amazon Elastic Container Registry in your account. For the Docker and buildpack build types and their settings, see [Build configuration](#beanstalk-cluster-app-versions-buildconfig).

**Note**  
On macOS, create the source archive with `zip -X -r ../my-app.zip .` from inside the source directory. The Finder's **Compress** command adds `__MACOSX` metadata entries, and a buildpack build can fail on one of those entries with `zip: not a valid zip file`, naming a file that you did not create.

While the build runs, the application version reports the status `BUILDING`. It moves to `PROCESSED` when the image is built and pushed, or to `FAILED` if the build does not succeed.

## Build configuration
<a name="beanstalk-cluster-app-versions-buildconfig"></a>

The `Build` member of `ImageConfiguration` accompanies a source bundle and controls how Elastic Beanstalk builds the image. It carries the following fields alongside the build type described next:
+ `CodeBuildServiceRole`, the IAM role that AWS CodeBuild assumes to run the build in your account. This field is required for a source build.
+ `ComputeType`, the optional size of the build compute: `BUILD_GENERAL1_SMALL`, `BUILD_GENERAL1_MEDIUM`, or `BUILD_GENERAL1_LARGE`. If you omit it, Elastic Beanstalk uses `BUILD_GENERAL1_MEDIUM`.
+ `TimeoutInMinutes`, the optional number of minutes after which Elastic Beanstalk stops a build that has not finished. The value can be from `5` through `480`. If you omit it, Elastic Beanstalk uses `60` minutes.

The `Build` member selects one of two build types through its `Type` field, which is required:
+ `docker`, Elastic Beanstalk builds the image from a Dockerfile in your source. Set `DockerfileLocation` to the path of the Dockerfile; if you omit it, Elastic Beanstalk uses `Dockerfile` at the root of the source.
+ `buildpack`, Elastic Beanstalk builds the image with Cloud Native Buildpacks. Set `Buildpack` to the builder image the build uses, for example `paketobuildpacks/builder-jammy-base`; Elastic Beanstalk passes the value to the build verbatim. The builder is required for a buildpack build. Elastic Beanstalk does not detect one for you, and a buildpack build with no builder set fails.

The `Architecture` field sets the target CPU architecture of the image, either `amd64` or `arm64`. If you omit it, Elastic Beanstalk builds for `amd64`. Build for the same architecture as the environment's `arch` setting, which also defaults to `amd64`. An image built for one architecture does not run on the other. For `arch`, see [Configuration options for Beanstalk Cluster environments](command-options-general-eks.md).

## Inspect and monitor processing status
<a name="beanstalk-cluster-app-versions-processing"></a>

A source-based version reports `BUILDING` while Elastic Beanstalk builds its image. Deploy it only after it reports `PROCESSED`. A status of `FAILED` means that the build did not succeed and the version cannot be deployed. A status of `UNPROCESSED` means that processing did not start, such as when the `CreateApplicationVersion` request omitted `Process`. An application version created from a provided image also reports `UNPROCESSED`, but it is ready to deploy because its image requires no build.

A description of an application version reports its image state as two members, `ImageSource` and `ImageBuildConfiguration`. For a source-based version, `ImageBuildConfiguration` echoes the build settings, and `ImageSource` is absent while the version reports `BUILDING`. When the build succeeds, `ImageSource` returns the digest-pinned URI of the image that the build produced and pushed.

Check the processing status of a source-based version with `DescribeApplicationVersions`. Set `operation_start` to the timestamp recorded immediately before the `CreateApplicationVersion` request; the event queries that follow use it to scope events to the build.

```
$ aws elasticbeanstalk describe-application-versions \
    --application-name my-app \
    --version-labels v1-build \
    --query 'ApplicationVersions[0].Status' \
    --output text
```

Repeat this command until the version reaches a terminal status. `BUILDING` means the build is still running. Deploy the version only after it reports `PROCESSED`; a status of `FAILED` or `UNPROCESSED` means that the version cannot be deployed.

For a source-based version, a `PROCESSED` status and an image-build completion event confirm that Elastic Beanstalk built and recorded the image. Retrieve events for the specific version to distinguish a terminal failure from a build that is still running:

```
$ aws elasticbeanstalk describe-events \
    --application-name my-app \
    --version-label v1-build \
    --start-time "$operation_start" \
    --max-items 20
```

If the version reaches `FAILED`, add `--severity ERROR` to retrieve its failure events. The events distinguish failures such as source download, role assumption, Amazon ECR authentication, and image build or push failures:

```
$ aws elasticbeanstalk describe-events \
    --application-name my-app \
    --version-label v1-build \
    --severity ERROR \
    --start-time "$operation_start" \
    --max-items 20
```

The events identify which stage failed. To see why the build itself failed, use the `BuildArn` that a source-based version reports, which identifies the AWS CodeBuild execution that ran the build. Pass it to the following command to get the build's status and the location of its logs:

```
$ aws codebuild batch-get-builds \
    --ids {{build-arn}} \
    --query 'builds[0].{status:buildStatus,logGroup:logs.groupName,logStream:logs.streamName}'
```

The response also carries a `logs.deepLink` that opens the build's log stream in the Amazon CloudWatch console.

Correct the source location, build configuration, or role configuration identified by the event. Create a new application version with a new label and `Process` set to `true`, then poll it to `PROCESSED`. Do not deploy a version in `FAILED`. Processing success proves only that the image is available to the application version; it does not verify an environment deployment.

## The sample application
<a name="beanstalk-cluster-app-versions-sample"></a>

An application version is optional when creating a Beanstalk Cluster environment. When `CreateEnvironment` is called without a version label (or with a blank one), Elastic Beanstalk deploys a sample application to provide a running environment. Elastic Beanstalk backs the sample with a prebuilt container image, so deployment requires no build step. The sample application cannot be selected or configured as a customer application; Elastic Beanstalk deploys it when no version label is specified. To deploy an application, create an application version as described in this topic and pass its version label to `CreateEnvironment`. For environment creation, see [Getting started with Beanstalk Cluster](beanstalk-cluster-getting-started.md).

## Examples
<a name="beanstalk-cluster-app-versions-example"></a>

The following `CreateApplicationVersion` request provides an existing container image. Elastic Beanstalk runs the image as-is, with no build.

```
aws elasticbeanstalk create-application-version \
  --application-name my-app \
  --version-label v1-image \
  --image-configuration Source={Uri=111122223333.dkr.ecr.us-east-1.amazonaws.com/my-app:v1}
```

The following request instead provides a source bundle in Amazon S3 and a build configuration that builds the image from a Dockerfile for the `arm64` architecture. To run this image, set the environment's `arch` option to `arm64` as well.

```
operation_start=$(date -u +%Y-%m-%dT%H:%M:%SZ)
aws elasticbeanstalk create-application-version \
  --application-name my-app \
  --version-label v1-build \
  --process \
  --source-bundle S3Bucket=my-source-bucket,S3Key=my-app/v1.zip \
  --image-configuration '{
    "Build": {
      "Type": "docker",
      "DockerfileLocation": "Dockerfile",
      "Architecture": "arm64",
      "CodeBuildServiceRole": "arn:aws:iam::111122223333:role/my-build-role",
      "ComputeType": "BUILD_GENERAL1_SMALL",
      "TimeoutInMinutes": 30
    }
  }'
```

The following request builds the image with Cloud Native Buildpacks instead of a Dockerfile. The source needs no Dockerfile, and the builder determines how the image is assembled. The request omits `Architecture`, so Elastic Beanstalk builds for `amd64`.

```
operation_start=$(date -u +%Y-%m-%dT%H:%M:%SZ)
aws elasticbeanstalk create-application-version \
  --application-name my-app \
  --version-label v1-buildpack \
  --process \
  --source-bundle S3Bucket=my-source-bucket,S3Key=my-app/v1.zip \
  --image-configuration '{
    "Build": {
      "Type": "buildpack",
      "Buildpack": "paketobuildpacks/builder-jammy-base",
      "CodeBuildServiceRole": "arn:aws:iam::111122223333:role/my-build-role"
    }
  }'
```

After a source-bundle build reaches `PROCESSED`, deploy any of these versions to a Beanstalk Cluster environment by passing its version label to `CreateEnvironment` or `UpdateEnvironment`, as for a Beanstalk Standard application version. For configuring the environment that runs it, see [Configuring Elastic Beanstalk environments](customize-containers.md).

## Delete and recover application versions
<a name="beanstalk-cluster-app-versions-delete"></a>

Application version lifecycle policies do not delete Beanstalk Cluster application versions. Use `DeleteApplicationVersion` to remove an application version record. Elastic Beanstalk rejects the request while the version is `BUILDING`; wait for a terminal processing status before deleting it.

For a Beanstalk Cluster application version, the `DeleteSourceBundle` option does not delete the source bundle from Amazon S3. Source-object retention is managed separately.

`DeleteApplicationVersion` removes the Elastic Beanstalk application version record. It does not delete an image supplied through `ImageConfiguration.Source`, an image produced by a source build, or the Amazon ECR repository that contains the image. You manage retention of an image that you supplied. When Elastic Beanstalk creates an Amazon ECR repository for source builds, it applies a lifecycle policy to that repository; deleting one application version does not perform immediate image or repository cleanup.

A source-based version in the `FAILED` state cannot be deployed. Correct the source or build configuration and call `CreateApplicationVersion` with a new version label and `Process` set to `true`. To reuse the failed version's label, first delete the version record after it leaves `BUILDING`, then create the corrected version.