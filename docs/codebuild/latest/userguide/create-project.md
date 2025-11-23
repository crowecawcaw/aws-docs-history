# Create a build project in AWS CodeBuild

You can use the AWS CodeBuild console, AWS CLI, or AWS SDKs to create a build project.

###### Topics

- [Prerequisites](#create-project-prerequisites "#create-project-prerequisites")
- [Create a build project (console)](#create-project-console "#create-project-console")
- [Create a build project (AWS CLI)](#create-project-cli "#create-project-cli")
- [Create a build project (AWS SDKs)](#create-project-sdks "#create-project-sdks")
- [Create a build project (CloudFormation)](#create-project-cloud-formation "#create-project-cloud-formation")

## Prerequisites

Before creating a build project, answer the questions in [Plan a build](planning.md "planning.md").

## Create a build project (console)

Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home").

If a CodeBuild information page is displayed, choose **Create build project**. Otherwise, on the navigation pane, expand **Build**,
choose **Build projects**, and then choose **Create build project**.

Choose **Create build project**.

Fill in the following sections. Once complete, choose **Create build
project** at the bottom of the page.

###### Sections:

- [Project configuration](#create-project-console-project-config "#create-project-console-project-config")
- [Source](#create-project-console-source "#create-project-console-source")
- [Environment](#create-project-console-environment "#create-project-console-environment")
- [Buildspec](#create-project-console-buildspec "#create-project-console-buildspec")
- [Batch configuration](#create-project-console-batch-config "#create-project-console-batch-config")
- [Artifacts](#create-project-console-artifacts "#create-project-console-artifacts")
- [Logs](#create-project-console-logs "#create-project-console-logs")

### Project configuration

**Project name**

Enter a name for this build project. Build project names must be unique
across each AWS account.

**Description**

Enter an optional description of the build project to help other users
understand what this project is used for.

**Build badge**

(Optional) Select **Enable build badge** to make your
project's build status visible and embeddable. For more information,
see [Build badges sample](sample-build-badges.md "sample-build-badges.md").

###### Note

Build badge does not apply if your source provider is Amazon S3.

**Enable concurrent build limit**

(Optional) If you want to limit the number of concurrent builds for this
project, perform the following steps:

1. Select **Restrict number of concurrent builds this project
   can start**.
2. In **Concurrent build limit**, enter the maximum
   number of concurrent builds that are allowed for this project. This
   limit cannot be greater than the concurrent build limit set for the
   account. If you try to enter a number greater than the account
   limit, an error message is displayed.

New builds are only started if the current number of builds is less than or equal to this limit.
If the current build count meets this limit, new builds are throttled and are not run.

**Additional information**

(Optional) For **Tags**, enter the name and value of any
tags that you want supporting AWS services to use. Use **Add
row** to add a tag. You can add up to 50 tags.

### Source

**Source provider**

Choose the source code provider
type. Use the following lists to make selections appropriate for your source
provider:

###### Note

CodeBuild does not support Bitbucket Server.

Amazon S3

**Bucket**

Choose the name of the input bucket that contains the source code.

**S3 object key or S3 folder**

Enter the name of the ZIP file or the path to the
folder that contains the source code. Enter a forward slash (/) to
download everything in the S3 bucket.

**Source version**

Enter the version ID of the object that represents the build of your
input file. For more information, see[Source version sample with AWS CodeBuild](sample-source-version.md "sample-source-version.md").

CodeCommit

**Repository**

Choose the repository you want to use.

**Reference type**

Choose **Branch**, **Git tag**, or
**Commit ID** to specify the version of your source
code. For more information, see [Source version sample with AWS CodeBuild](sample-source-version.md "sample-source-version.md").

###### Note

We recommend that you choose Git branch names that don't look like commit IDs,
such as `811dd1ba1aba14473856cee38308caed7190c0d` or `5392f7`.
This helps you avoid Git checkout collisions with actual commits.

**Git clone depth**

Choose to create a shallow clone with a history truncated to the
specified number of commits. If you want a full clone, choose
**Full**.

**Git submodules**

Select **Use Git submodules** if you want to include
Git submodules in your repository.

Bitbucket

**Credential**

Choose **Default source credential** or **Custom
source credential** and follow the
instructions to manage the default source credential or customize the source credential.

**Connection type**

Choose **CodeConnections**, **OAuth**, **App password**, or
**Personal access token** to connect to CodeBuild.

**Connection**

Select a Bitbucket connection or a Secrets Manager secret to connect through your specified connection type.

**Repository**

Choose **Repository in my Bitbucket account**
or **Public repository** and enter the repository URL.

**Source version**

Enter a branch, commit ID, tag, or reference and a commit ID. For more
information, see [Source version sample with AWS CodeBuild](sample-source-version.md "sample-source-version.md")

###### Note

We recommend that you choose Git branch names that don't look like commit IDs,
such as `811dd1ba1aba14473856cee38308caed7190c0d` or `5392f7`.
This helps you avoid Git checkout collisions with actual commits.

**Git clone depth**

Choose **Git clone depth** to create a shallow clone
with a history truncated to the specified number of commits. If you want
a full clone, choose **Full**.

**Git submodules**

Select **Use Git submodules** if you want to include
Git submodules in your repository.

**Build status**

Select **Report build statuses to source provider when your
builds start and finish** if you want the status of your
build's start and completion reported to your source provider.

To be able to report the build status to the source provider, the user associated with the source provider must
have write access to the repo. If the user does not have write access, the build status cannot be updated. For more information, see
[Source provider access](access-tokens.md "access-tokens.md").

For **Status context**, enter the value to be used
for the `name` parameter in the Bitbucket commit status. For
more information, see [build](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/commit/%7Bnode%7D/statuses/build "https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/commit/%7Bnode%7D/statuses/build") in the Bitbucket API documentation.

For **Target URL**, enter the value to be used for
the `url` parameter in the Bitbucket commit status. For more
information, see [build](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/commit/%7Bnode%7D/statuses/build "https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/commit/%7Bnode%7D/statuses/build") in the Bitbucket API documentation.

The status of a build triggered by a webhook is always reported to
the source provider. To have the status of a build that is started from the console or an API
call reported to the source provider, you must select this setting.

If your project's builds are triggered by a webhook, you must push a
new commit to the repo for a change to this setting to take
effect.

In **Primary source webhook events**, select **Rebuild
every time a code change is pushed to this repository** if you want
CodeBuild to build the source code every time a code change is pushed to this
repository. For more information about webhooks and filter groups, see [Bitbucket webhook events](bitbucket-webhook.md "bitbucket-webhook.md").

GitHub

**Credential**

Choose **Default source credential** or **Custom
source credential** and follow the
instructions to manage the default source credential or customize the source credential.

**Connection type**

Choose **GitHub App**, **OAuth**, or
**Personal access token** to connect to CodeBuild.

**Connection**

Select a GitHub connection or a Secrets Manager secret to connect through your specified connection type.

**Repository**

Choose **Repository in my GitHub account**, **Public repository**,
or **GitHub scoped webhook** and enter the repository URL.

**Source version**

Enter a branch, commit ID, tag, or reference and a commit ID. For more
information, see [Source version sample with AWS CodeBuild](sample-source-version.md "sample-source-version.md")

###### Note

We recommend that you choose Git branch names that don't look like commit IDs,
such as `811dd1ba1aba14473856cee38308caed7190c0d` or `5392f7`.
This helps you avoid Git checkout collisions with actual commits.

**Git clone depth**

Choose **Git clone depth** to create a shallow clone
with a history truncated to the specified number of commits. If you want
a full clone, choose **Full**.

**Git submodules**

Select **Use Git submodules** if you want to include
Git submodules in your repository.

**Build status**

Select **Report build statuses to source provider when your
builds start and finish** if you want the status of your
build's start and completion reported to your source provider.

To be able to report the build status to the source provider, the user associated with the source provider must
have write access to the repo. If the user does not have write access, the build status cannot be updated. For more information, see
[Source provider access](access-tokens.md "access-tokens.md").

For **Status context**, enter the value to be used
for the `context` parameter in the GitHub commit status. For
more information, see [Create a commit status](https://developer.github.com/v3/repos/statuses/#create-a-commit-status "https://developer.github.com/v3/repos/statuses/#create-a-commit-status") in the GitHub developer
guide.

For **Target URL**, enter the value to be used for
the `target_url` parameter in the GitHub commit status. For
more information, see [Create a commit status](https://developer.github.com/v3/repos/statuses/#create-a-commit-status "https://developer.github.com/v3/repos/statuses/#create-a-commit-status") in the GitHub developer
guide.

The status of a build triggered by a webhook is always reported to
the source provider. To have the status of a build that is started from the console or an API
call reported to the source provider, you must select this setting.

If your project's builds are triggered by a webhook, you must push a
new commit to the repo for a change to this setting to take
effect.

In **Primary source webhook events**, select **Rebuild
every time a code change is pushed to this repository** if you want
CodeBuild to build the source code every time a code change is pushed to this
repository. For more information about webhooks and filter groups, see [GitHub webhook events](github-webhook.md "github-webhook.md").

GitHub Enterprise Server

**Credential**

Choose **Default source credential** or **Custom
source credential** and follow the
instructions to manage the default source credential or customize the source credential.

**Connection type**

Choose **CodeConnections** or **Personal access token** to connect to CodeBuild.

**Connection**

Select a GitHub Enterprise connection or a Secrets Manager secret to connect through your specified connection type.

**Repository**

Choose **Repository in my GitHub Enterprise account** or
**GitHub Enterprise scoped webhook** and enter the repository URL.

**Source version**

Enter a pull request, branch, commit ID, tag, or reference and a
commit ID. For more information, see [Source version sample with AWS CodeBuild](sample-source-version.md "sample-source-version.md").

###### Note

We recommend that you choose Git branch names that don't look like commit IDs,
such as `811dd1ba1aba14473856cee38308caed7190c0d` or `5392f7`.
This helps you avoid Git checkout collisions with actual commits.

**Git clone depth**

Choose **Git clone depth** to create a shallow clone
with a history truncated to the specified number of commits. If you want
a full clone, choose **Full**.

**Git submodules**

Select **Use Git submodules** if you want to include
Git submodules in your repository.

**Build status**

Select **Report build statuses to source provider when your
builds start and finish** if you want the status of your
build's start and completion reported to your source provider.

To be able to report the build status to the source provider, the user associated with the source provider must
have write access to the repo. If the user does not have write access, the build status cannot be updated. For more information, see
[Source provider access](access-tokens.md "access-tokens.md").

For **Status context**, enter the value to be used
for the `context` parameter in the GitHub commit status. For
more information, see [Create a commit status](https://developer.github.com/v3/repos/statuses/#create-a-commit-status "https://developer.github.com/v3/repos/statuses/#create-a-commit-status") in the GitHub developer
guide.

For **Target URL**, enter the value to be used for
the `target_url` parameter in the GitHub commit status. For
more information, see [Create a commit status](https://developer.github.com/v3/repos/statuses/#create-a-commit-status "https://developer.github.com/v3/repos/statuses/#create-a-commit-status") in the GitHub developer
guide.

The status of a build triggered by a webhook is always reported to
the source provider. To have the status of a build that is started from the console or an API
call reported to the source provider, you must select this setting.

If your project's builds are triggered by a webhook, you must push a
new commit to the repo for a change to this setting to take
effect.

**Insecure SSL**

Select **Enable insecure SSL** to ignore SSL warnings
while connecting to your GitHub Enterprise project repository.

In **Primary source webhook events**, select **Rebuild
every time a code change is pushed to this repository** if you want
CodeBuild to build the source code every time a code change is pushed to this
repository. For more information about webhooks and filter groups, see [GitHub webhook events](github-webhook.md "github-webhook.md").

GitLab

**Credential**

Choose **Default source credential** or **Custom
source credential** and follow the
instructions to manage the default source credential or customize the source credential.

**Connection type**

**CodeConnections** is used to connect GitLab to CodeBuild.

**Connection**

Select a GitLab connection to connect through CodeConnections.

**Repository**

Choose the repository you want to use.

**Source version**

Enter a pull request ID, branch, commit ID, tag, or reference and a commit ID. For more
information, see [Source version sample with AWS CodeBuild](sample-source-version.md "sample-source-version.md").

###### Note

We recommend that you choose Git branch names that don't look like commit IDs,
such as `811dd1ba1aba14473856cee38308caed7190c0d` or `5392f7`.
This helps you avoid Git checkout collisions with actual commits.

**Git clone depth**

Choose **Git clone depth** to create a shallow clone
with a history truncated to the specified number of commits. If you want
a full clone, choose **Full**.

**Build status**

Select **Report build statuses to source provider when your
builds start and finish** if you want the status of your
build's start and completion reported to your source provider.

To be able to report the build status to the source provider, the user associated with the source provider must
have write access to the repo. If the user does not have write access, the build status cannot be updated. For more information, see
[Source provider access](access-tokens.md "access-tokens.md").

GitLab Self Managed

**Credential**

Choose **Default source credential** or **Custom
source credential** and follow the
instructions to manage the default source credential or customize the source credential.

**Connection type**

**CodeConnections** is used to connect GitLab Self Managed to CodeBuild.

**Connection**

Select a GitLab Self Managed connection to connect through CodeConnections.

**Repository**

Choose the repository you want to use.

**Source version**

Enter a pull request ID, branch, commit ID, tag, or reference and a commit ID. For more
information, see [Source version sample with AWS CodeBuild](sample-source-version.md "sample-source-version.md").

###### Note

We recommend that you choose Git branch names that don't look like commit IDs,
such as `811dd1ba1aba14473856cee38308caed7190c0d` or `5392f7`.
This helps you avoid Git checkout collisions with actual commits.

**Git clone depth**

Choose **Git clone depth** to create a shallow clone
with a history truncated to the specified number of commits. If you want
a full clone, choose **Full**.

**Build status**

Select **Report build statuses to source provider when your
builds start and finish** if you want the status of your
build's start and completion reported to your source provider.

To be able to report the build status to the source provider, the user associated with the source provider must
have write access to the repo. If the user does not have write access, the build status cannot be updated. For more information, see
[Source provider access](access-tokens.md "access-tokens.md").

### Environment

**Provisioning model**

Do one of the following:

- To use on-demand fleets managed by AWS CodeBuild, choose **On-demand**. With on-demand fleets,
  CodeBuild provides compute for your builds. The machines are destroyed when the build finishes. On-demand fleets
  are fully managed, and includes automatic scaling capabilities to handle spikes in demand.
- To use reserved capacity fleets managed by AWS CodeBuild, choose **Reserved capacity**, and then select a **Fleet name**. With
  reserved capacity fleets, you configure a set of dedicated instances for your build environment. These machines
  remain idle, ready to process builds or tests immediately and reduces build durations. With reserved capacity fleets,
  your machines are always running and will continue to incur costs as long they're provisioned.

For information, see [Run builds on reserved capacity fleets](fleets.md "fleets.md").

**Environment image**

Do one of the following:

- To use a Docker image managed by AWS CodeBuild, choose **Managed image**, and then make selections from
  **Operating system**, **Runtime(s)**, **Image**, and
  **Image version**. Make a selection from **Environment type** if it is available.
- To use another Docker image, choose **Custom image**. For **Environment type**,
  choose **ARM**, **Linux**, **Linux GPU**, or **Windows**. If you
  choose **Other registry**, for **External registry URL**, enter the name and tag of the Docker image in Docker
  Hub, using the format
  ``docker repository`/`docker image name``.
  If you choose **Amazon ECR**, use **Amazon ECR
  repository** and **Amazon ECR image** to choose
  the Docker image in your AWS account.
- To use a private Docker image, choose **Custom image**. For **Environment type**, choose
  **ARM**, **Linux**, **Linux GPU**, or **Windows**. For **Image registry**, choose
  **Other registry**, and then enter the ARN of the credentials for your private Docker image.
  The credentials must be created by Secrets Manager. For more information,
  see [What Is
  AWS Secrets Manager?](../../../secretsmanager/latest/userguide.md "../../../secretsmanager/latest/userguide.md") in the _AWS Secrets Manager User Guide_.

###### Note

CodeBuild overrides the `ENTRYPOINT` for custom Docker images.

**Compute**

Do one of the following:

- To use EC2 compute, choose **EC2**. EC2 compute offers
  optimized flexibility during action runs.
- To use Lambda compute, choose **Lambda**. Lambda compute offers optimized start-up
  speeds for your builds. Lambda supports faster builds due to a lower start-up latency. Lambda also
  automatically scales, so builds aren’t waiting in queue to run. For information, see
  [Run builds on AWS Lambda compute](lambda.md "lambda.md").

**Service role**
Do one of the following:

- If you do not have a CodeBuild service role, choose **New service role**. In **Role
  name**, enter a name for the new role.
- If you have a CodeBuild service role, choose **Existing service role**. In **Role
  ARN**, choose the service role.

###### Note

When you use the console to create a build project, you can create a
CodeBuild service role at the same time. By default, the role works with
that build project only. If you use the console to associate this
service role with another build project, the role is updated to work
with the other build project. A service role can work with up to 10
build projects.

**Additional configuration**

**Auto-retry limit**

Specify the number of additional automatic retries after a failed build. For example, if the
auto-retry limit is set to 2, CodeBuild will call the `RetryBuild` API to automatically retry
your build for up to 2 additional times.

**Timeout**

Specify a value, between 5 minutes and 36 hours, after which
CodeBuild stops the build if it is not complete. If
**hours** and **minutes**
are left blank, the default value of 60 minutes is used.

**Privileged**

(Optional) Select **Enable this flag if you want to build Docker images
or want your builds to get elevated privileges** only if you plan to use
this build project to build Docker images. Otherwise, all
associated builds that attempt to interact with the Docker daemon fail. You
must also start the Docker daemon so that your builds can interact with it.
One way to do this is to initialize the Docker daemon in the
`install` phase of your build spec by running the following
build commands. Do not run these commands if you chose a build environment
image provided by CodeBuild with Docker support.

###### Note

By default, Docker daemon is enabled for non-VPC builds. If you would like to use Docker
containers for VPC builds, see [Runtime
Privilege and Linux Capabilities](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities "https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities") on the Docker Docs website and enable privileged mode. Also, Windows does not support privileged mode.

```
- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://127.0.0.1:2375 --storage-driver=overlay2 &
- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"
```

**VPC**
If you want CodeBuild to work with your VPC:

- For **VPC**, choose the VPC ID that CodeBuild uses.
- For **VPC Subnets**, choose the subnets that include resources that CodeBuild uses.
- For **VPC Security groups**, choose the security groups that CodeBuild uses to allow access to resources in
  the VPCs.

For more information, see [Use AWS CodeBuild with Amazon Virtual Private Cloud](vpc-support.md "vpc-support.md").

**Compute**

Choose one of the available options.

**Registry credential**

Specify a registry credential when the project is configured with
a non-private registry image.

###### Note

This credential will only be utilized if the images are
overridden with those from private registries.

**Environment variables**

Enter the name and value, and then choose the type of each
environment variable for builds to use.

###### Note

CodeBuild sets the environment variable for your AWS Region
automatically. You must set the following environment
variables if you haven't added them to your
buildspec.yml:

- AWS_ACCOUNT_ID
- IMAGE_REPO_NAME
- IMAGE_TAG

Console and AWS CLI users can see environment variables. If you
have no concerns about the visibility of your environment
variable, set the **Name** and
**Value** fields, and then set
**Type** to
**Plaintext**.

We recommend that you store an environment variable with a
sensitive value, such as an AWS access key ID, an AWS secret
access key, or a password as a parameter in Amazon EC2 Systems Manager Parameter
Store or AWS Secrets Manager.

If you use Amazon EC2 Systems Manager Parameter Store, then for
**Type**, choose
**Parameter**. For
**Name**, enter an identifier for CodeBuild to
reference. For **Value**, enter the parameter's
name as stored in Amazon EC2 Systems Manager Parameter Store. Using a parameter
named `/CodeBuild/dockerLoginPassword` as an example,
for **Type**, choose
**Parameter**. For
**Name**, enter
`LOGIN_PASSWORD`. For **Value**,
enter `/CodeBuild/dockerLoginPassword`.

###### Important

If you use Amazon EC2 Systems Manager Parameter Store, we recommend that you store
parameters with parameter names that start with `/CodeBuild/`
(for example, `/CodeBuild/dockerLoginPassword`). You can use the
CodeBuild console to create a parameter in Amazon EC2 Systems Manager. Choose **Create
parameter**, and then follow the instructions in the dialog
box. (In that dialog box, for **KMS key**, you can
specify the ARN of an AWS KMS key in your account. Amazon EC2 Systems Manager uses
this key to encrypt the parameter's value during storage and decrypt it during
retrieval.) If you use the CodeBuild console to create a parameter, the console
starts the parameter name with `/CodeBuild/` as it is being
stored. For more information, see [Systems Manager Parameter Store](../../../systems-manager/latest/userguide/systems-manager-paramstore.md "../../../systems-manager/latest/userguide/systems-manager-paramstore.md") and [Systems Manager Parameter Store Console Walkthrough](../../../systems-manager/latest/userguide/sysman-paramstore-walk.md#sysman-paramstore-console "../../../systems-manager/latest/userguide/sysman-paramstore-walk.md#sysman-paramstore-console") in the
_Amazon EC2 Systems Manager User Guide_.

If your build project refers to parameters stored in Amazon EC2 Systems Manager Parameter
Store, the build project's service role must allow the
`ssm:GetParameters` action. If you chose **New
service role** earlier, CodeBuild includes this action in the
default service role for your build project. However, if you
chose **Existing service role**, you must include this
action to your service role separately.

If your build project refers to parameters stored in Amazon EC2 Systems Manager Parameter
Store with parameter names that do not start with `/CodeBuild/`,
and you chose **New service role**, you must update
that service role to allow access to parameter names that do not start with
`/CodeBuild/`. This is because that service role allows
access only to parameter names that start with
`/CodeBuild/`.

If you choose **New service role**, the service
role includes permission to decrypt all parameters under the
`/CodeBuild/` namespace in the Amazon EC2 Systems Manager Parameter
Store.

Environment variables you set replace existing environment variables. For
example, if the Docker image already contains an environment variable named
`MY_VAR` with a value of `my_value`, and you set
an environment variable named `MY_VAR` with a value of
`other_value`, then `my_value` is replaced by
`other_value`. Similarly, if the Docker image already
contains an environment variable named `PATH` with a value of
`/usr/local/sbin:/usr/local/bin`, and you set an environment
variable named `PATH` with a value of
`$PATH:/usr/share/ant/bin`, then
`/usr/local/sbin:/usr/local/bin` is replaced by the literal
value `$PATH:/usr/share/ant/bin`.

Do not set any environment variable with a name that begins with
`CODEBUILD_`. This prefix is reserved for internal
use.

If an environment variable with the same name is defined in multiple
places, the value is determined as follows:

- The value in the start build operation call takes highest
  precedence.
- The value in the build project definition takes next
  precedence.
- The value in the buildspec declaration takes lowest
  precedence.

If you use Secrets Manager, for **Type**, choose
**Secrets Manager**. For
**Name**, enter an identifier for CodeBuild to
reference. For **Value**, enter a
`reference-key` using the pattern
``secret-id`:`json-key`:`version-stage`:`version-id``.
For information, see [Secrets Manager reference-key in the buildspec file](build-spec-ref.md#secrets-manager-build-spec "build-spec-ref.md#secrets-manager-build-spec").

###### Important

If you use Secrets Manager, we recommend that you store secrets with names
that start with `/CodeBuild/` (for example,
`/CodeBuild/dockerLoginPassword`). For more information, see
[What Is
AWS Secrets Manager?](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") in the _AWS Secrets Manager User Guide_.

If your build project refers to secrets stored in Secrets Manager, the build
project's service role must allow the
`secretsmanager:GetSecretValue` action. If you chose
**New service role** earlier, CodeBuild includes this
action in the default service role for your build project.
However, if you chose **Existing service role**, you
must include this action to your service role separately.

If your build project refers to secrets stored in Secrets Manager with secret names
that do not start with `/CodeBuild/`, and you chose **New
service role**, you must update the service role to allow
access to secret names that do not start with `/CodeBuild/`. This
is because the service role allows access only to secret names that start
with `/CodeBuild/`.

If you choose **New service role**, the service
role includes permission to decrypt all secrets under the
`/CodeBuild/` namespace in the Secrets Manager.

### Buildspec

**Build specifications**

Do one of the following:

- If your source code includes a buildspec file, choose
  **Use a buildspec file**. By default, CodeBuild
  looks for a file named `buildspec.yml` in the
  source code root directory. If your buildspec file uses a different
  name or location, enter its path from the source root in
  **Buildspec name** (for example,
  `buildspec-two.yml` or
  `configuration/buildspec.yml`. If the
  buildspec file is in an S3 bucket, it must be in the same AWS
  Region as your build project. Specify the buildspec file using its
  ARN (for example,
  `arn:aws:s3:::`<my-codebuild-sample2>`/buildspec.yml`).
- If your source code does not include a buildspec file, or if you
  want to run build commands different from the ones specified for the
  `build` phase in the
  `buildspec.yml` file in the source code's
  root directory, choose **Insert build commands**.
  For **Build commands**, enter the commands you want
  to run in the `build` phase. For multiple commands,
  separate each command by `&&` (for example,
  `mvn test && mvn package`). To run commands
  in other phases, or if you have a long list of commands for the
  `build` phase, add a
  `buildspec.yml` file to the source code root
  directory, add the commands to the file, and then choose
  **Use the buildspec.yml in the source code root
  directory**.

For more information, see the [Buildspec reference](build-spec-ref.md "build-spec-ref.md").

### Batch configuration

You can run a group of builds as a single operation. For more information, see [Run builds in batches](batch-build.md "batch-build.md").

**Define batch configuration**

Select to allow batch builds in this project.

**Batch service role**

Provides the service role for batch builds.

Choose one of the following:

- If you do not have a batch service role, choose **New
  service role**. In **Service role**,
  enter a name for the new role.
- If you have a batch service role, choose **Existing
  service role**. In **Service role**,
  choose the service role.

Batch builds introduce a new security role in the batch configuration. This new role
is required as CodeBuild must be able to call the `StartBuild`, `StopBuild`, and
`RetryBuild` actions on your behalf to run builds as part of a batch. Customers should use a new role, and
not the same role they use in their build, for two reasons:

- Giving the build role `StartBuild`, `StopBuild`, and `RetryBuild`
  permissions would allow a single build to start more builds via the buildspec.
- CodeBuild batch builds provide restrictions that restrict the number of builds and compute types that
  can be used for the builds in the batch. If the build role has these permissions, it is possible the builds
  themselves could bypass these restrictions.

**Allowed compute types for batch**

Select the compute types allowed for the batch. Select all that
apply.

**Allowed fleets for batch**

Select the fleets allowed for the batch. Select all that
apply.

**Maximum builds allowed in batch**

Enter the maximum number of builds allowed in the batch. If a batch
exceeds this limit, the batch will fail.

**Batch timeout**

Enter the maximum amount of time for the batch build to complete.

**Combine artifacts**

Select **Combine all artifacts from batch into a single
location** to have all of the artifacts from the batch combined
into a single location.

**Batch report mode**

Select the desired build status report mode for batch builds.

###### Note

This field is only available when the project source is Bitbucket, GitHub, or GitHub
Enterprise, and **Report build statuses to source provider when your builds start
and finish** is selected under **Source**.

**Aggregated builds**

Select to have the statuses for all builds in the batch combined into a single
status report.

**Individual builds**

Select to have the build statuses for all builds in the batch reported
separately.

### Artifacts

**Type**

Do one of the following:

- If you do not want to create any build output artifacts, choose
  **No artifacts**. You might want to do this if
  you're only running build tests or you want to push a Docker image
  to an Amazon ECR repository.
- To store the build output in an S3 bucket, choose
  **Amazon S3**, and then do the following:
  - If you want to use your project name for the build output
    ZIP file or folder, leave **Name** blank.
    Otherwise, enter the name. (If you want to output a ZIP
    file, and you want the ZIP file to have a file extension, be
    sure to include it after the ZIP file name.)
  - Select **Enable semantic versioning** if
    you want a name specified in the buildspec file to override
    any name that is specified in the console. The name in a
    buildspec file is calculated at build time and uses the
    Shell command language. For example, you can append a date
    and time to your artifact name so that it is always unique.
    Unique artifact names prevent artifacts from being
    overwritten. For more information, see [Buildspec syntax](build-spec-ref.md#build-spec-ref-syntax "build-spec-ref.md#build-spec-ref-syntax").
  - For **Bucket name**, choose the name of
    the output bucket.
  - If you chose **Insert build commands**
    earlier in this procedure, then for **Output
    files**, enter the locations of the files from
    the build that you want to put into the build output ZIP
    file or folder. For multiple locations, separate each
    location with a comma (for example, `appspec.yml,
target/my-app.jar`). For more information, see the
    description of `files` in [Buildspec syntax](build-spec-ref.md#build-spec-ref-syntax "build-spec-ref.md#build-spec-ref-syntax").
  - If you do not want your build artifacts encrypted, select
    **Remove artifacts encryption**.

For each secondary set of artifacts you want:

1. For **Artifact identifier**, enter a value that
   is fewer than 128 characters and contains only alphanumeric
   characters and underscores.
2. Choose **Add artifact**.
3. Follow the previous steps to configure your secondary
   artifacts.
4. Choose **Save artifact**.

**Additional configuration**

**Encryption key**

(Optional) Do one of the following:

- To use the AWS managed key
  for Amazon S3 in your account to encrypt the build output
  artifacts, leave **Encryption key**
  blank. This is the default.
- To use a customer managed key to encrypt the build
  output artifacts, in **Encryption
  key**, enter the ARN of the KMS key. Use the format
  `arn:aws:kms:`region-ID`:`account-ID`:key/`key-ID``.

**Cache type**
For **Cache type**, choose one of the following:

- If you do not want to use a cache, choose **No
  cache**.
- If you want to use an Amazon S3 cache, choose **Amazon
  S3**, and then do the following:
  - For **Bucket**, choose the name of the S3
    bucket where the cache is stored.
  - (Optional) For **Cache path prefix**, enter
    an Amazon S3 path prefix. The **Cache path prefix**
    value is similar to a directory name. It makes it possible for
    you to store the cache under the same directory in a bucket.

  ###### Important

  Do not append a trailing slash (/) to the end of the path
  prefix.

- If you want to use a local cache, choose **Local**,
  and then choose one or more local cache modes.

###### Note

Docker layer cache mode is available for
Linux only. If you choose it, your project must run in privileged
mode.

Using a cache saves considerable build time because reusable pieces of the
build environment are stored in the cache and used across builds. For
information about specifying a cache in the buildspec file, see [Buildspec syntax](build-spec-ref.md#build-spec-ref-syntax "build-spec-ref.md#build-spec-ref-syntax"). For
more information about caching, see [Cache builds to improve performance](build-caching.md "build-caching.md").

### Logs

Choose the logs you want to create. You can create Amazon CloudWatch Logs, Amazon S3 logs, or both.

**CloudWatch**

If you want Amazon CloudWatch Logs logs:

**CloudWatch logs**

Select **CloudWatch logs**.

**Group name**

Enter the name of your Amazon CloudWatch Logs log group.

**Stream name**

Enter your Amazon CloudWatch Logs log stream name.

**S3**

If you want Amazon S3 logs:

**S3 logs**

Select **S3 logs**.

**Bucket**

Choose the name of the S3 bucket for your logs.

**Path prefix**

Enter the prefix for your logs.

**Disable S3 log encryption**

Select if you do not want your S3 logs encrypted.

## Create a build project (AWS CLI)

For more information about using the AWS CLI with CodeBuild, see the [Command line reference](cmd-ref.md "cmd-ref.md").

To create a CodeBuild build project using the AWS CLI, you create a JSON-formatted [Project](../APIReference/API_Project.md "../APIReference/API_Project.md") structure, fill in the structure, and call the [`create-project`](../../../cli/latest/reference/codebuild/create-project.md "../../../cli/latest/reference/codebuild/create-project.md") command to create the project.

### Create the JSON file

Create a skeleton JSON file with the [`create-project`](../../../cli/latest/reference/codebuild/create-project.md "../../../cli/latest/reference/codebuild/create-project.md") command, using the
`--generate-cli-skeleton` option:

```
aws codebuild create-project --generate-cli-skeleton > `<json-file>`
```

This creates a JSON file with the path and file name specified by
`<json-file>`.

### Fill in the JSON file

Modify the JSON data as follows and save your results.

```
{
  "name": "`<project-name>`",
  "description": "`<description>`",
  "source": {
    "type": "CODECOMMIT" | "CODEPIPELINE" | "GITHUB" | "GITHUB_ENTERPRISE" | "GITLAB" | "GITLAB_SELF_MANAGED" | "BITBUCKET" | "S3" | "NO_SOURCE",
    "location": "`<source-location>`",
    "gitCloneDepth": "`<git-clone-depth>`",
    "buildspec": "`<buildspec>`",
    "InsecureSsl": "`<insecure-ssl>`",
    "reportBuildStatus": "`<report-build-status>`",
    "buildStatusConfig": {
      "context": "`<context>`",
      "targetUrl": "`<target-url>`"
    },
    "gitSubmodulesConfig": {
      "fetchSubmodules": "`<fetch-submodules>`"
    },
    "auth": {
      "type": "`<auth-type>`",
      "resource": "`<auth-resource>`"
    },
    "sourceIdentifier": "`<source-identifier>`"
  },
  "secondarySources": [
    {
        "type": "CODECOMMIT" | "CODEPIPELINE" | "GITHUB" | "GITHUB_ENTERPRISE" | "GITLAB" | "GITLAB_SELF_MANAGED" | "BITBUCKET" | "S3" | "NO_SOURCE",
        "location": "`<source-location>`",
        "gitCloneDepth": "`<git-clone-depth>`",
        "buildspec": "`<buildspec>`",
        "InsecureSsl": "`<insecure-ssl>`",
        "reportBuildStatus": "`<report-build-status>`",
        "auth": {
          "type": "`<auth-type>`",
          "resource": "`<auth-resource>`"
        },
        "sourceIdentifier": "`<source-identifier>`"
    }
  ],
  "secondarySourceVersions": [
    {
      "sourceIdentifier": "`<secondary-source-identifier>`",
      "sourceVersion": "`<secondary-source-version>`"
    }
  ],
  "sourceVersion": "`<source-version>"`,
  "artifacts": {
    "type": "CODEPIPELINE" | "S3" | "NO_ARTIFACTS",
    "location": "`<artifacts-location>`",
    "path": "`<artifacts-path>`",
    "namespaceType": "`<artifacts-namespacetype>`",
    "name": "`<artifacts-name>`",
    "overrideArtifactName": "`<override-artifact-name>`",
    "packaging": "`<artifacts-packaging>`"
  },
  "secondaryArtifacts": [
    {
      "type": "CODEPIPELINE" | "S3" | "NO_ARTIFACTS",
      "location": "`<secondary-artifact-location>`",
      "path": "`<secondary-artifact-path>`",
      "namespaceType": "`<secondary-artifact-namespaceType>`",
      "name": "`<secondary-artifact-name>`",
      "packaging": "`<secondary-artifact-packaging>`",
      "artifactIdentifier": "`<secondary-artifact-identifier>`"
    }
  ],
  "cache": {
    "type": "`<cache-type>`",
    "location": "`<cache-location>`",
    "mode": [
      "`<cache-mode>`"
    ]
  },
  "environment": {
    "type": "LINUX_CONTAINER" | "LINUX_GPU_CONTAINER" | "ARM_CONTAINER" | "WINDOWS_SERVER_2019_CONTAINER" | "WINDOWS_SERVER_2022_CONTAINER",
    "image": "`<image>`",
    "computeType": "BUILD_GENERAL1_SMALL" | "BUILD_GENERAL1_MEDIUM" | "BUILD_GENERAL1_LARGE" | "BUILD_GENERAL1_2XLARGE",
    "certificate": "`<certificate>`",
    "environmentVariables": [
      {
        "name": "`<environmentVariable-name>`",
        "value": "`<environmentVariable-value>`",
        "type": "`<environmentVariable-type>`"
      }
    ],
    "registryCredential": [
      {
        "credential": "`<credential-arn-or-name>`",
        "credentialProvider": "`<credential-provider>`"
      }
    ],
    "imagePullCredentialsType": "CODEBUILD" | "SERVICE_ROLE",
    "privilegedMode": "`<privileged-mode>`"
  },
  "serviceRole": "`<service-role>`",
  "autoRetryLimit": `<auto-retry-limit>`,
  "timeoutInMinutes": `<timeout>`,
  "queuedTimeoutInMinutes": `<queued-timeout>`,
  "encryptionKey": "`<encryption-key>`",
  "tags": [
    {
      "key": "`<tag-key>`",
      "value": "`<tag-value>`"
    }
  ],
  "vpcConfig": {
    "securityGroupIds": [
         "`<security-group-id>`"
    ],
    "subnets": [
         "`<subnet-id>`"
    ],
    "vpcId": "`<vpc-id>`"
  },
  "badgeEnabled": "`<badge-enabled>`",
  "logsConfig": {
    "cloudWatchLogs": {
      "status": "`<cloudwatch-logs-status>`",
      "groupName": "`<group-name>`",
      "streamName": "`<stream-name>`"
    },
    "s3Logs": {
      "status": "`<s3-logs-status>`",
      "location": "`<s3-logs-location>`",
      "encryptionDisabled": "`<s3-logs-encryption-disabled>`"
    }
  },
  "fileSystemLocations": [
    {
      "type": "EFS",
      "location": "`<EFS-DNS-name-1>`:/`<directory-path>`",
      "mountPoint": "`<mount-point>`",
      "identifier": "`<efs-identifier>`",
      "mountOptions": "`<efs-mount-options>`"
    }
  ],
  "buildBatchConfig": {
    "serviceRole": "`<batch-service-role>`",
    "combineArtifacts": `<combine-artifacts>`,
    "restrictions": {
      "maximumBuildsAllowed": `<max-builds>`,
      "computeTypesAllowed": [
        "`<compute-type>`"
      ],
      "fleetsAllowed": [
        "`<fleet-name>`"
      ]
    },
    "timeoutInMins": `<batch-timeout>`,
    "batchReportMode": "REPORT_AGGREGATED_BATCH" | "REPORT_INDIVIDUAL_BUILDS"
  },
  "concurrentBuildLimit": `<concurrent-build-limit>`
}
```

Replace the following:

#### **name**

Required. The name for this build project. This name must be unique across all of
the build projects in your AWS account.

#### **description**

Optional. The description for this build project.

#### **source**

Required. A [ProjectSource](../APIReference/API_ProjectSource.md "../APIReference/API_ProjectSource.md")
object that contains information about this build project's source code settings.
After you add a `source` object, you can add up to 12 more sources using
the [secondarySources](#cli.secondarysources "#cli.secondarysources"). These
settings include the following:

source/**type**

Required. The type of repository that contains the source code to
build. Valid values include:

- `CODECOMMIT`
- `CODEPIPELINE`
- `GITHUB`
- `GITHUB_ENTERPRISE`
- `GITLAB`
- `GITLAB_SELF_MANAGED`
- `BITBUCKET`
- `S3`
- `NO_SOURCE`

If you use `NO_SOURCE`, the buildspec cannot be a file
because the project does not have a source. Instead, you must use the
`buildspec` attribute to specify a YAML-formatted string
for your buildspec. For more information, see [Create a build project without a source](no-source.md "no-source.md").

source/**location**

Required unless you set `<source-type>` to
`CODEPIPELINE`. The location of the source code for the
specified repository type.

- For CodeCommit, the HTTPS clone URL to the repository that contains
  the source code and the buildspec file (for example,
  `https://git-codecommit.`<region-id>`.amazonaws.com/v1/repos/`<repo-name>``).
- For Amazon S3, the build input bucket name, followed by the path
  and name of the ZIP file that contains the source code and the
  buildspec. For example:
  - For a ZIP file located at the root of the input
    bucket:
    ``<bucket-name>`/`<object-name>`.zip`.
  - For a ZIP file located in a subfolder in the input
    bucket:
    ``<bucket-name>`/`<subfoler-path>`/`<object-name>`.zip`.

- For GitHub, the HTTPS clone URL to the repository that
  contains the source code and the buildspec file. The URL must
  contain github.com. You must connect your AWS account to your
  GitHub account. To do this, use the CodeBuild console to create a
  build project.
  - Choose **Authorize application**.
    (After you have connected to your GitHub account, you do
    not need to finish creating the build project. You can
    close the CodeBuild console.)

- For GitHub Enterprise Server, the HTTP or HTTPS clone URL to
  the repository that contains the source code and the buildspec
  file. You must also connect your AWS account to your GitHub
  Enterprise Server account. To do this, use the CodeBuild console to
  create a build project.
  1.  Create a personal access token in GitHub Enterprise
      Server.
  2.  Copy this token to your clipboard so you can use it
      when you create your CodeBuild project. For more
      information, see [Creating a personal access token for the command
      line](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/ "https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/") on the GitHub Help website.
  3.  When you use the console to create your CodeBuild project,
      in **Source**, for **Source
      provider**, choose **GitHub
      Enterprise**.
  4.  For **Personal Access Token**, paste
      the token that was copied to your clipboard. Choose
      **Save Token**. Your CodeBuild account
      is now connected to your GitHub Enterprise Server
      account.

- For GitLab and GitLab self-managed, the HTTPS clone URL to the
  repository that contains the source code and the buildspec file.
  Note that if you use GitLab, the URL must contain gitlab.com. If
  you use GitLab self-managed, the URL does not need to contain
  gitlab.com. You must connect your AWS account to your GitLab
  or GitLab self-managed account. To do this, use the CodeBuild
  console to create a build project.
  - In the Developer Tools navigation pane, choose
    **Settings**,
    **Connections**, and then
    **Create connection**. On this
    page, create either a GitLab or GitLab self-managed
    connection, and then choose **Connect to
    GitLab**.

- For Bitbucket, the HTTPS clone URL to the repository that
  contains the source code and the buildspec file. The URL must
  contain bitbucket.org. You must also connect your AWS account
  to your Bitbucket account. To do this, use the CodeBuild console to
  create a build project.
  1.  When you use the console to connect (or reconnect)
      with Bitbucket, on the Bitbucket **Confirm
      access to your account** page, choose
      **Grant access**. (After you have
      connected to your Bitbucket account, you do not need to
      finish creating the build project. You can close the
      CodeBuild console.)

- For AWS CodePipeline, do not specify a `location` value
  for `source`. CodePipeline ignores this value because when
  you create a pipeline in CodePipeline, you specify the source code
  location in the Source stage of the pipeline.

source/**gitCloneDepth**

Optional. The depth of history to download. Minimum value is 0. If
this value is 0, greater than 25, or not provided, then the full history
is downloaded with each build project. If your source type is Amazon S3, this
value is not supported.

source/**buildspec**

Optional. The build specification definition or file to use. If this
value is not provided or is set to an empty string, the source code must
contain a `buildspec.yml` file in its root
directory. If this value is set, it can be either an inline buildspec
definition, the path to an alternate buildspec file relative to the root
directory of your primary source, or the path to an S3 bucket. The
bucket must be in the same AWS Region as the build project. Specify
the buildspec file using its ARN (for example,
`arn:aws:s3:::`<my-codebuild-sample2>`/buildspec.yml`).
For more information, see [Buildspec file name and storage
location](build-spec-ref.md#build-spec-ref-name-storage "build-spec-ref.md#build-spec-ref-name-storage").

source/**auth**

Contains information about the authorization settings
for CodeBuild to access the source code to be built.

source/auth/**type**

Required. The authorization type to use. Valid values are:

- `OAUTH`
- `CODECONNECTIONS`
- `SECRETS_MANAGER`

source/auth/**resource**

Optional. The resource value that applies to the specified authorization type.
This can be the Secrets Manager ARN or the CodeConnections ARN.

source/**reportBuildStatus**

Specifies whether to send your source provider the status of a build's
start and completion. If you set this with a source provider other than
GitHub, GitHub Enterprise Server, or Bitbucket, an
`invalidInputException` is thrown.

To be able to report the build status to the source provider, the user associated with the source provider must
have write access to the repo. If the user does not have write access, the build status cannot be updated. For more information, see
[Source provider access](access-tokens.md "access-tokens.md").

source/**buildStatusConfig**

Contains information that defines how the CodeBuild build project reports
the build status to the source provider. This option is only used when
the source type is `GITHUB`, `GITHUB_ENTERPRISE`,
or `BITBUCKET`.

source/buildStatusConfig/**context**

For Bitbucket sources, this parameter is used for the
`name` parameter in the Bitbucket commit
status. For GitHub sources, this parameter is used for the
`context` parameter in the GitHub commit
status.

For example, you can have the `context` contain
the build number and the webhook trigger using the CodeBuild
environment variables:

```
AWS CodeBuild sample-project Build #$CODEBUILD_BUILD_NUMBER - $CODEBUILD_WEBHOOK_TRIGGER
```

This results in the context appearing like this for build
#24 triggered by a webhook pull request event:

```
AWS CodeBuild sample-project Build #24 - pr/8
```

source/buildStatusConfig/**targetUrl**

For Bitbucket sources, this parameter is used for the
`url` parameter in the Bitbucket commit
status. For GitHub sources, this parameter is used for the
`target_url` parameter in the GitHub commit
status.

For example, you can set the `targetUrl` to
`https://aws.amazon.com/codebuild/`<path
 to build>`` and the commit status
will link to this URL.

You can also include CodeBuild environment variables in the
`targetUrl` to add additional information to
the URL. For example, to add the build region to the URL,
set the `targetUrl` to:

```
"targetUrl": "https://aws.amazon.com/codebuild/`<path to build>`?region=$AWS_REGION"
```

If the build region is
`us-east-2`, this will expand
to:

```
https://aws.amazon.com/codebuild/`<path to build>`?region=us-east-2
```

source/**gitSubmodulesConfig**

Optional. Information about the Git submodules configuration. Used
with CodeCommit, GitHub, GitHub Enterprise Server, and Bitbucket only.

source/gitSubmodulesConfig/**fetchSubmodules**

Set `fetchSubmodules` to `true` if
you want to include the Git submodules in your repository.
Git submodules that are included must be configured as
HTTPS.

source/**InsecureSsl**

Optional. Used with GitHub Enterprise Server only. Set this value to
`true` to ignore TLS warnings while connecting to your
GitHub Enterprise Server project repository. The default value is
`false`. `InsecureSsl` should be used for
testing purposes only. It should not be used in a production
environment.

source/**sourceIdentifier**

A user-defined identifier for the project source. Optional for the
primary source. Required for secondary sources.

#### **secondarySources**

Optional. An array of [ProjectSource](../APIReference/API_ProjectSource.md "../APIReference/API_ProjectSource.md")
objects that contain information about the secondary sources for a build project.
You can add up to 12 secondary sources. The `secondarySources` objects
use the same properties used by the [source](#cli.source "#cli.source") object. In a secondary source object, the
`sourceIdentifier` is required.

#### **secondarySourceVersions**

Optional. An array of [ProjectSourceVersion](../APIReference/API_ProjectSourceVersion.md "../APIReference/API_ProjectSourceVersion.md") objects. If `secondarySourceVersions`
is specified at the build level, then they take precedence over this.

#### **sourceVersion**

Optional. The version of the build input to be built for this project. If not
specified, the latest version is used. If specified, it must be one of:

- For CodeCommit, the commit ID, branch, or Git tag to use.
- For GitHub, the commit ID, pull request ID, branch name, or tag name that
  corresponds to the version of the source code you want to build. If a pull
  request ID is specified, it must use the format
  `pr/pull-request-ID` (for example `pr/25`). If a
  branch name is specified, the branch's HEAD commit ID is used. If not
  specified, the default branch's HEAD commit ID is used.
- For GitLab, the commit ID, pull request ID, branch name, tag name, or
  reference and a commit ID. For more information, see [Source version sample with AWS CodeBuild](sample-source-version.md "sample-source-version.md").
- For Bitbucket, the commit ID, branch name, or tag name that corresponds to
  the version of the source code you want to build. If a branch name is
  specified, the branch's HEAD commit ID is used. If not specified, the
  default branch's HEAD commit ID is used.
- For Amazon S3, the version ID of the object that represents the build
  input ZIP file to use.

If `sourceVersion` is specified at the build level, then that version
takes precedence over this `sourceVersion` (at the project level). For
more information, see [Source version sample with AWS CodeBuild](sample-source-version.md "sample-source-version.md").

#### **artifacts**

Required. A [ProjectArtifacts](../APIReference/API_ProjectArtifacts.md "../APIReference/API_ProjectArtifacts.md") object that contains information about this build
project's output artifact settings. After you add an `artifacts` object,
you can add up to 12 more artifacts using the [secondaryArtifacts](#cli.secondaryartifacts "#cli.secondaryartifacts"). These settings include the following:

artifacts/**type**

Required. The type of build output artifact. Valid values are:

- `CODEPIPELINE`
- `NO_ARTIFACTS`
- `S3`

artifacts/**location**

Only used with the `S3` artifact type. Not used for other
artifact types.

The name of the output bucket you created or identified in the
prerequisites.

artifacts/**path**

Only used with the `S3` artifact type. Not used for other
artifact types.

The path in of the output bucket to place ZIP file or folder. If you
do not specify a value for `path`, CodeBuild uses
`namespaceType` (if specified) and `name` to
determine the path and name of the build output ZIP file or folder. For
example, if you specify `MyPath` for `path` and
`MyArtifact.zip` for `name`, the path and name
would be `MyPath/MyArtifact.zip`.

artifacts/**namespaceType**

Only used with the `S3` artifact type. Not used for other
artifact types.

The namespace of the build output ZIP file or folder. Valid values
include `BUILD_ID` and `NONE`. Use
`BUILD_ID` to insert the build ID into the path of the
build output ZIP file or folder. Otherwise, use `NONE`. If
you do not specify a value for `namespaceType`, CodeBuild uses
`path` (if specified) and `name` to determine
the path and name of the build output ZIP file or folder. For example,
if you specify `MyPath` for `path`,
`BUILD_ID` for `namespaceType`, and
`MyArtifact.zip` for `name`, the path and name
would be
`MyPath/`build-ID`/MyArtifact.zip`.

artifacts/**name**

Only used with the `S3` artifact type. Not used for other
artifact types.

The name of the build output ZIP file or folder inside of
`location`. For example, if you specify
`MyPath` for `path` and
`MyArtifact.zip` for `name`, the path and name
would be `MyPath/MyArtifact.zip`.

artifacts/**overrideArtifactName**

Only used with the S3 artifact type. Not used for other artifact
types.

Optional. If set to `true`, the name specified in the
`artifacts` block of the buildspec file overrides
`name`. For more information, see [Build specification reference for CodeBuild](build-spec-ref.md "build-spec-ref.md").

artifacts/**packaging**

Only used with the `S3` artifact type. Not used for other
artifact types.

Optional. Specifies how to package the artifacts. Allowed values
are:

NONE

Create a folder that contains the build artifacts. This is
the default value.

ZIP

Create a ZIP file that contains the build
artifacts.

#### secondaryArtifacts

Optional. An array of [ProjectArtifacts](../APIReference/API_ProjectArtifacts.md "../APIReference/API_ProjectArtifacts.md") objects that contain information about the secondary
artifacts settings for a build project. You can add up to 12 secondary artifacts.
The `secondaryArtifacts` uses many of the same settings used by the [artifacts](#cli.artifacts "#cli.artifacts") object.

#### cache

Required. A [ProjectCache](../APIReference/API_ProjectCache.md "../APIReference/API_ProjectCache.md")
object that contains information about this build project's cache settings. For more
information, see [Cache builds](build-caching.md "build-caching.md").

#### environment

Required. A [ProjectEnvironment](../APIReference/API_ProjectEnvironment.md "../APIReference/API_ProjectEnvironment.md") object that contains information about this
project's build environment settings. These settings include:

environment/**type**

Required. The type of build environment. For more information, see
[type](../APIReference/API_ProjectEnvironment.md#CodeBuild-Type-ProjectEnvironment-type "../APIReference/API_ProjectEnvironment.md#CodeBuild-Type-ProjectEnvironment-type") in the _CodeBuild API
Reference_.

environment/**image**

Required. The Docker image identifier used by this build environment.
Typically, this identifier is expressed as
`image-name`:`tag`.
For example, in the Docker repository that CodeBuild uses to manage its
Docker images, this could be `aws/codebuild/standard:5.0`.
In Docker Hub, `maven:3.3.9-jdk-8`. In Amazon ECR,
``account-id`.dkr.ecr.`region-id`.amazonaws.com/`your-Amazon-ECR-repo-name`:`tag``.
For more information, see [Docker images provided by CodeBuild](build-env-ref-available.md "build-env-ref-available.md").

environment/**computeType**

Required. Specifies the compute resources used by this build
environment. For more information, see [computeType](../APIReference/API_ProjectEnvironment.md#CodeBuild-Type-ProjectEnvironment-computeType "../APIReference/API_ProjectEnvironment.md#CodeBuild-Type-ProjectEnvironment-computeType") in the _CodeBuild API
Reference_.

environment/**certificate**

Optional. The ARN of the Amazon S3 bucket, path prefix, and object key that
contains the PEM-encoded certificate. The object key can be either just
the .pem file or a .zip file containing the PEM-encoded certificate. For
example, if your Amazon S3 bucket name is
`<my-bucket>`,
your path prefix is `<cert>`,
and your object key name is
`<certificate.pem>`,
then acceptable formats for `certificate` are
`<my-bucket/cert/certificate.pem>`
or
`arn:aws:s3:::`<my-bucket/cert/certificate.pem>``.

environment/**environmentVariables**

Optional. An array of [EnvironmentVariable](../APIReference/API_EnvironmentVariable.md "../APIReference/API_EnvironmentVariable.md") objects that contains the environment
variables you want to specify for this build environment. Each
environment variable is expressed as an object that contains a
`name`, `value`, and `type` of
`name`, `value`, and `type`.

Console and AWS CLI users can see all environment variables. If you have
no concerns about the visibility of your environment variable, set
`name` and `value`, and set `type`
to `PLAINTEXT`.

We recommend you store environment variables with sensitive values,
such as an AWS access key ID, an AWS secret access key, or a
password, as a parameter in Amazon EC2 Systems Manager Parameter Store or AWS Secrets Manager. For
`name`, for that stored parameter, set an identifier for
CodeBuild to reference.

If you use Amazon EC2 Systems Manager Parameter Store, for `value`, set the
parameter's name as stored in the Parameter Store. Set `type`
to `PARAMETER_STORE`. Using a parameter named
`/CodeBuild/dockerLoginPassword` as an example, set
`name` to `LOGIN_PASSWORD`. Set
`value` to `/CodeBuild/dockerLoginPassword`.
Set `type` to `PARAMETER_STORE`.

###### Important

If you use Amazon EC2 Systems Manager Parameter Store, we recommend that you store
parameters with parameter names that start with `/CodeBuild/`
(for example, `/CodeBuild/dockerLoginPassword`). You can use the
CodeBuild console to create a parameter in Amazon EC2 Systems Manager. Choose **Create
parameter**, and then follow the instructions in the dialog
box. (In that dialog box, for **KMS key**, you can
specify the ARN of an AWS KMS key in your account. Amazon EC2 Systems Manager uses
this key to encrypt the parameter's value during storage and decrypt it during
retrieval.) If you use the CodeBuild console to create a parameter, the console
starts the parameter name with `/CodeBuild/` as it is being
stored. For more information, see [Systems Manager Parameter Store](../../../systems-manager/latest/userguide/systems-manager-paramstore.md "../../../systems-manager/latest/userguide/systems-manager-paramstore.md") and [Systems Manager Parameter Store Console Walkthrough](../../../systems-manager/latest/userguide/sysman-paramstore-walk.md#sysman-paramstore-console "../../../systems-manager/latest/userguide/sysman-paramstore-walk.md#sysman-paramstore-console") in the
_Amazon EC2 Systems Manager User Guide_.

If your build project refers to parameters stored in Amazon EC2 Systems Manager Parameter
Store, the build project's service role must allow the
`ssm:GetParameters` action. If you chose **New
service role** earlier, CodeBuild includes this action in the
default service role for your build project. However, if you
chose **Existing service role**, you must include this
action to your service role separately.

If your build project refers to parameters stored in Amazon EC2 Systems Manager Parameter
Store with parameter names that do not start with `/CodeBuild/`,
and you chose **New service role**, you must update
that service role to allow access to parameter names that do not start with
`/CodeBuild/`. This is because that service role allows
access only to parameter names that start with
`/CodeBuild/`.

If you choose **New service role**, the service
role includes permission to decrypt all parameters under the
`/CodeBuild/` namespace in the Amazon EC2 Systems Manager Parameter
Store.

Environment variables you set replace existing environment variables. For
example, if the Docker image already contains an environment variable named
`MY_VAR` with a value of `my_value`, and you set
an environment variable named `MY_VAR` with a value of
`other_value`, then `my_value` is replaced by
`other_value`. Similarly, if the Docker image already
contains an environment variable named `PATH` with a value of
`/usr/local/sbin:/usr/local/bin`, and you set an environment
variable named `PATH` with a value of
`$PATH:/usr/share/ant/bin`, then
`/usr/local/sbin:/usr/local/bin` is replaced by the literal
value `$PATH:/usr/share/ant/bin`.

Do not set any environment variable with a name that begins with
`CODEBUILD_`. This prefix is reserved for internal
use.

If an environment variable with the same name is defined in multiple
places, the value is determined as follows:

- The value in the start build operation call takes highest
  precedence.
- The value in the build project definition takes next
  precedence.
- The value in the buildspec declaration takes lowest
  precedence.

If you use Secrets Manager, for `value`, set the parameter's name as
stored in Secrets Manager. Set `type` to
`SECRETS_MANAGER`. Using a secret named
`/CodeBuild/dockerLoginPassword` as an example, set
`name` to `LOGIN_PASSWORD`. Set
`value` to `/CodeBuild/dockerLoginPassword`.
Set `type` to `SECRETS_MANAGER`.

###### Important

If you use Secrets Manager, we recommend that you store secrets with names
that start with `/CodeBuild/` (for example,
`/CodeBuild/dockerLoginPassword`). For more information, see
[What Is
AWS Secrets Manager?](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") in the _AWS Secrets Manager User Guide_.

If your build project refers to secrets stored in Secrets Manager, the build
project's service role must allow the
`secretsmanager:GetSecretValue` action. If you chose
**New service role** earlier, CodeBuild includes this
action in the default service role for your build project.
However, if you chose **Existing service role**, you
must include this action to your service role separately.

If your build project refers to secrets stored in Secrets Manager with secret names
that do not start with `/CodeBuild/`, and you chose **New
service role**, you must update the service role to allow
access to secret names that do not start with `/CodeBuild/`. This
is because the service role allows access only to secret names that start
with `/CodeBuild/`.

If you choose **New service role**, the service
role includes permission to decrypt all secrets under the
`/CodeBuild/` namespace in the Secrets Manager.

environment/**registryCredential**

Optional. A [RegistryCredential](../APIReference/API_RegistryCredential.md "../APIReference/API_RegistryCredential.md") object that specifies the credentials
that provide access to a private Docker registry.

environment/registryCredential/**credential**

Specifies the ARN or name of credentials created using
AWS Managed Services. You can use the name of the credentials only if
they exist in your current Region.

environment/registryCredential/**credentialProvider**

The only valid value is
`SECRETS_MANAGER`.

When this is set:

- `imagePullCredentials` must be set to
  `SERVICE_ROLE`.
- The image cannot be a curated image or an Amazon ECR image.

environment/**imagePullCredentialsType**

Optional. The type of credentials CodeBuild uses to pull images in your
build. There are two valid values:

CODEBUILD

`CODEBUILD` specifies that CodeBuild uses its own
credentials. You must edit your Amazon ECR repository policy to
trust the CodeBuild service principal.

SERVICE_ROLE

Specifies that CodeBuild uses your build project's service
role.

When you use a cross-account or private registry image, you must use
`SERVICE_ROLE` credentials. When you use a CodeBuild curated
image, you must use `CODEBUILD` credentials.

environment/**privilegedMode**

Set to `true` only if you plan to use this build project to
build Docker images. Otherwise, all associated builds that attempt to
interact with the Docker daemon fail. You must also start the Docker
daemon so that your builds can interact with it. One way to do this is
to initialize the Docker daemon in the `install` phase of
your buildspec file by running the following build commands. Do not run
these commands if you specified a build environment image provided by
CodeBuild with Docker support.

###### Note

By default, Docker daemon is enabled for non-VPC builds. If you would like to use Docker
containers for VPC builds, see [Runtime
Privilege and Linux Capabilities](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities "https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities") on the Docker Docs website and enable privileged mode. Also, Windows does not support privileged mode.

```
- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://127.0.0.1:2375 --storage-driver=overlay2 &
- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"
```

#### serviceRole

Required. The ARN of the service role CodeBuild uses to interact with services on
behalf of the user (for example,
`arn:aws:iam::`account-id`:role/`role-name``).

#### autoRetryLimit

Optional. The number of additional automatic retries after a failed build. For example, if the
auto-retry limit is set to 2, CodeBuild will call the `RetryBuild` API to automatically retry
your build for up to 2 additional times.

#### timeoutInMinutes

Optional. The number of minutes, between 5 to 2160 (36 hours), after which CodeBuild
stops the build if it is not complete. If not specified, the default of 60 is used.
To determine if and when CodeBuild stopped a build due to a timeout, run the
`batch-get-builds` command. To determine if the build has
stopped, look in the output for a `buildStatus` value of
`FAILED`. To determine when the build timed out, look in the output
for the `endTime` value associated with a `phaseStatus` value
of `TIMED_OUT`.

#### queuedTimeoutInMinutes

Optional. The number of minutes, between 5 to 480 (8 hours), after which CodeBuild
stops the build if it is is still queued. If not specified, the default of 60 is
used.

#### encryptionKey

Optional. The alias or ARN of the AWS KMS key used by CodeBuild to encrypt the
build output. If you specify an alias, use the format
`arn:aws:kms:`region-ID`:`account-ID`:key/`key-ID``
 or, if an alias exists, use the format
 `alias/`key-alias``. If not specified,
the AWS-managed KMS key for Amazon S3 is used.

#### tags

Optional. An array of [Tag](../APIReference/API_Tag.md "../APIReference/API_Tag.md") objects that
provide the tags you want to associate with this build project. You can specify up
to 50 tags. These tags can be used by any AWS service that supports CodeBuild build
project tags. Each tag is expressed as an object with a `key` and a
`value`.

#### vpcConfig

Optional. A [VpcConfig](../APIReference/API_VpcConfig.md "../APIReference/API_VpcConfig.md") object
that contains information information about the VPC configuration for your project.
For more information, see [Use AWS CodeBuild with Amazon Virtual Private Cloud](vpc-support.md "vpc-support.md").

These properties include:

vpcId

Required. The VPC ID that CodeBuild uses. Run this command to get a list
of all VPC IDs in your Region:

```
aws ec2 describe-vpcs --region `<region-ID>`
```

subnets

Required. An array of subnet IDs that include resources used by CodeBuild.
Run this command to get these IDs:

```
aws ec2 describe-subnets --filters "Name=vpc-id,Values=<vpc-id>" --region `<region-ID>`
```

securityGroupIds

Required. An array of security group IDs used by CodeBuild to allow access
to resources in the VPC. Run this command to get these IDs:

```
aws ec2 describe-security-groups --filters "Name=vpc-id,Values=`<vpc-id>`" --`<region-ID>`
```

#### badgeEnabled

Optional. Specifies whether to include build badges with your CodeBuild project. Set
to `true` to enable build badges, or `false` otherwise. For
more information, see [Build badges sample with CodeBuild](sample-build-badges.md "sample-build-badges.md").

#### logsConfig

A [LogsConfig](../APIReference/API_LogsConfig.md "../APIReference/API_LogsConfig.md")
object that contains information about where this build's logs are located.

logsConfig/**cloudWatchLogs**

A [CloudWatchLogsConfig](../APIReference/API_CloudWatchLogsConfig.md "../APIReference/API_CloudWatchLogsConfig.md") object that contains information about
pushing logs to CloudWatch Logs.

logsConfig/**s3Logs**

An [S3LogsConfig](../APIReference/API_S3LogsConfig.md "../APIReference/API_S3LogsConfig.md") object that contains information about pushing
logs to Amazon S3.

#### fileSystemLocations

Optional. An array of [ProjectFileSystemsLocation](../APIReference/API_ProjectFileSystemLocation.md "../APIReference/API_ProjectFileSystemLocation.md") objects that contains informationabout your
Amazon EFS configuration.

#### buildBatchConfig

Optional. The `buildBatchConfig` object is a [ProjectBuildBatchConfig](../APIReference/API_ProjectBuildBatchConfig.md "../APIReference/API_ProjectBuildBatchConfig.md") structure that contains the batch build
configuration information for the project.

buildBatchConfig/**serviceRole**

The service role ARN for the batch build project.

buildBatchConfig/**combineArtifacts**

A Boolean value that specifies whether to combine the build artifacts
for the batch build into a single artifact location.

buildBatchConfig/restrictions/**maximumBuildsAllowed**

The maximum number of builds allowed.

buildBatchConfig/restrictions/**computeTypesAllowed**

An array of strings that specify the compute types that are allowed
for the batch build. See [Build environment compute types](build-env-ref-compute-types.md "build-env-ref-compute-types.md") for these values.

buildBatchConfig/restrictions/**fleetsAllowed**

An array of strings that specify the fleets that are allowed
for the batch build. See [Run builds on reserved capacity fleets](fleets.md "fleets.md") for more information.

buildBatchConfig/**timeoutInMinutes**

The maximum amount of time, in minutes, that the batch build must be
completed in.

buildBatchConfig/**batchReportMode**

Specifies how build status reports are sent to the source provider for
the batch build. Valid values include:

`REPORT_AGGREGATED_BATCH`

(Default) Aggregate all of the build statuses into a
single status report.

`REPORT_INDIVIDUAL_BUILDS`

Send a separate status report for each individual
build.

#### concurrentBuildLimit

The maximum number of concurrent builds that are allowed for this project.

New builds are only started if the current number of builds is less than or equal to this limit.
If the current build count meets this limit, new builds are throttled and are not run.

### Create the project

To create the project, run the **[`create-project`](../../../cli/latest/reference/codebuild/create-project.md "../../../cli/latest/reference/codebuild/create-project.md")** command again, passing your
JSON file:

```
aws codebuild create-project --cli-input-json file://`<json-file>`
```

If successful, the JSON representation of a [Project](../APIReference/API_Project.md "../APIReference/API_Project.md") object appears
in the console output. See the [CreateProject Response Syntax](../APIReference/API_CreateProject.md#API_CreateProject_ResponseSyntax "../APIReference/API_CreateProject.md#API_CreateProject_ResponseSyntax") for an example of this data.

Except for the build project name, you can change any of the build project's settings
later. For more information, see [Change a build project's settings (AWS CLI)](change-project.md#change-project-cli "change-project.md#change-project-cli").

To start running a build, see [Run a build (AWS CLI)](run-build-cli.md "run-build-cli.md").

If your source code is stored in a GitHub repository, and you want CodeBuild to rebuild the
source code every time a code change is pushed to the repository, see [Start running builds automatically
(AWS CLI)](run-build-cli-auto-start.md "run-build-cli-auto-start.md").

## Create a build project (AWS SDKs)

For information about using AWS CodeBuild with the AWS SDKs, see the [AWS SDKs and tools reference](sdk-ref.md "sdk-ref.md").

## Create a build project (CloudFormation)

For information about using AWS CodeBuild with CloudFormation, see [the CloudFormation template for CodeBuild](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.md") in the _AWS CloudFormation User
Guide_.
