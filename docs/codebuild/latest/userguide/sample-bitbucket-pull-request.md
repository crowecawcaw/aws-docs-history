# Run the 'Bitbucket pull request and webhook filter'

sample for CodeBuild

AWS CodeBuild supports webhooks when the source repository is Bitbucket. This means that for a
CodeBuild build project that has its source code stored in a Bitbucket repository, webhooks can
be used to rebuild the source code every time a code change is pushed to the repository. For
more information, see [Bitbucket webhook events](bitbucket-webhook.md "bitbucket-webhook.md").

This sample shows you how to create a pull request using a Bitbucket repository. It also
shows you how to use a Bitbucket webhook to trigger CodeBuild to create a build of a
project.

###### Note

When using webhooks, it is possible for a user to trigger an unexpected build. To mitigate
this risk, see [Best practices for using
webhooks](webhooks.md#webhook-best-practices "webhooks.md#webhook-best-practices").

###### Topics

- [Prerequisites](#sample-bitbucket-pull-request-prerequisites "#sample-bitbucket-pull-request-prerequisites")
- [Step 1: Create a build
  project with Bitbucket and enable webhooks](#sample-bitbucket-pull-request-create "#sample-bitbucket-pull-request-create")
- [Step 2: Trigger a build with
  a Bitbucket webhook](#sample-bitbucket-pull-request-trigger "#sample-bitbucket-pull-request-trigger")

## Prerequisites

To run this sample you must connect your AWS CodeBuild project with your Bitbucket
account.

###### Note

CodeBuild has updated its permissions with Bitbucket. If you previously connected
your project to Bitbucket and now receive a Bitbucket connection error, you must
reconnect to grant CodeBuild permission to manage your webhooks.

## Step 1: Create a build

project with Bitbucket and enable webhooks

The following steps describe how to create an AWS CodeBuild project with Bitbucket as
a source repository and enable webhooks.

1. Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home").
2. If a CodeBuild information page is displayed, choose **Create build project**. Otherwise, on the navigation pane, expand **Build**,
   choose **Build projects**, and then choose **Create build project**.
3. Choose **Create build project**.
4. In **Project configuration**:

**Project name**

Enter a name for this build project. Build project names must
be unique across each AWS account. You can also include an
optional description of the build project to help other users
understand what this project is used for. 5. In **Source**:

**Source provider**

Choose **Bitbucket**. Follow the instructions
to connect (or reconnect) with Bitbucket and then choose
**Authorize**.

**Repository**

Choose **Repository in my Bitbucket
account**.

If you have not previously connected to your Bitbucket
account, enter your Bitbucket username and app password, and
select **Save Bitbucket credentials**.

**Bitbucket repository**

Enter the URL for your Bitbucket repository. 6. In **Primary source webhook events**, select the
following.

###### Note

The **Primary source webhook events** section is only
visible if you chose **Repository in my Bitbucket
account** in the previous step.

    1. Select **Rebuild every time a code change is pushed to this repository**
     when you create your project.
    2. From **Event type**, choose one or more events.
    3. To filter when an event triggers a build, under **Start a build under these
     conditions**, add one or more optional filters.
    4. To filter when an event is not triggered, under **Don't start a build under these
     conditions**, add one or more optional filters.
    5. Choose **Add filter group** to add another filter group, if needed.

For more information about Bitbucket webhook event types and filters, see
[Bitbucket webhook events](bitbucket-webhook.md "bitbucket-webhook.md"). 7. In **Environment**:

**Environment image**

Choose one of the following:

To use a Docker image managed by AWS CodeBuild:

Choose **Managed image**, and
then make selections from **Operating
system**,
**Runtime(s)**,
**Image**, and **Image
version**. Make a selection from
**Environment type** if it is
available.

To use another Docker image:

Choose **Custom image**. For
**Environment type**, choose
**ARM**, **Linux**, **Linux GPU**, or **Windows**. If you
choose **Other registry**, for
**External registry URL**, enter
the name and tag of the Docker image in Docker Hub,
using the format ``docker
 repository`/`docker image
 name``. If you choose
**Amazon ECR**, use **Amazon ECR
repository** and **Amazon ECR
image** to choose the Docker image in
your AWS account.

To use a private Docker image:

Choose **Custom image**. For
**Environment type**, choose
**ARM**, **Linux**, **Linux GPU**, or **Windows**. For
**Image registry**, choose
**Other registry**, and then
enter the ARN of the credentials for your private
Docker image. The credentials must be created by
Secrets Manager. For more information, see [What Is AWS Secrets Manager?](../../../secretsmanager/latest/userguide.md "../../../secretsmanager/latest/userguide.md") in the
_AWS Secrets Manager User Guide_.

**Service role**

Choose one of the following:

    * If you do not have a CodeBuild service role, choose
     **New service role**. In
     **Role name**, enter a name for the
     new role.
    * If you have a CodeBuild service role, choose
     **Existing service role**. In
     **Role ARN**, choose the service
     role.

###### Note

When you use the console to create or update a build
project, you can create a CodeBuild service role at the same
time. By default, the role works with that build project
only. If you use the console to associate this service role
with another build project, the role is updated to work with
the other build project. A service role can work with up to
10 build projects. 8. In **Buildspec**, do one of the following:

    * Choose **Use a buildspec file** to use the buildspec.yml file in the source code root
     directory.
    * Choose **Insert build commands** to use the console to insert build commands.

For more information, see the [Buildspec reference](build-spec-ref.md "build-spec-ref.md"). 9. In **Artifacts**:

**Type**

Choose one of the following:

    * If you do not want to create build output artifacts,
     choose **No artifacts**.
    * To store the build output in an S3 bucket, choose
     **Amazon S3**, and then do the
     following:




    	+ If you want to use your project name for the
    	 build output ZIP file or folder, leave
    	 **Name** blank. Otherwise, enter
    	 the name. By default, the artifact name is the
    	 project name. If you want to use a different name,
    	 enter it in the artifacts name box. If you want to
    	 output a ZIP file, include the zip
    	 extension.
    	+ For **Bucket name**, choose
    	 the name of the output bucket.
    	+ If you chose **Insert build
    	 commands** earlier in this procedure, for
    	 **Output files**, enter the
    	 locations of the files from the build that you
    	 want to put into the build output ZIP file or
    	 folder. For multiple locations, separate each
    	 location with a comma (for example,
    	 `appspec.yml, target/my-app.jar`). For
    	 more information, see the description of
    	 `files` in [Buildspec syntax](build-spec-ref.md#build-spec-ref-syntax "build-spec-ref.md#build-spec-ref-syntax").

**Additional configuration**

Expand **Additional configuration** and set
options as appropriate. 10. Choose **Create build project**. On the
**Review** page, choose **Start
build** to run the build.

## Step 2: Trigger a build with

a Bitbucket webhook

For a project that uses Bitbucket webhooks, AWS CodeBuild creates a build when the
Bitbucket repository detects a change in your source code.

1. Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home").
2. On the navigation pane, choose **Build projects**, and
   then choose a project associated with a Bitbucket repository with webhooks.
   For information about creating a Bitbucket webhook project, see [Step 1: Create a build
   project with Bitbucket and enable webhooks](#sample-bitbucket-pull-request-create "#sample-bitbucket-pull-request-create").
3. Make some changes in the code in your project's Bitbucket repository.
4. Create a pull request on your Bitbucket repository. For more information,
   see [Making a pull request](https://www.atlassian.com/git/tutorials/making-a-pull-request "https://www.atlassian.com/git/tutorials/making-a-pull-request").
5. On the Bitbucket webhooks page, choose **View request**
   to see a list of recent events.
6. Choose **View details** to see details about the response
   returned by CodeBuild. It might look something like this:

```
"response":"Webhook received and build started: https://us-east-1.console.aws.amazon.com/codebuild/home..."
"statusCode":200
```

7. Navigate to the Bitbucket pull request page to see the status of the
   build.
