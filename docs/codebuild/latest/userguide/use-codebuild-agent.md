# Run builds locally with the AWS CodeBuild agent

You can use the AWS CodeBuild agent to run CodeBuild builds on a local machine. There are agents
available for x86_64 and ARM platforms.

You can also subscribe to receive notifications when new versions of the agent are
published.

## Prerequisites

Before you begin, you need to do the following:

- Install Git on your local machine.
- Install and set up [Docker](https://www.docker.com/ "https://www.docker.com/") on your
  local machine.

## Set up the build image

You only need to set up the build image the first time you run the agent, or when the
image has changed.

###### To set up the build image

1. If you want to use a curated Amazon Linux 2 image, you can pull it from the CodeBuild
   public Amazon ECR repository at [https://gallery.ecr.aws/codebuild/amazonlinux-x86_64-standard](https://gallery.ecr.aws/codebuild/amazonlinux-x86_64-standard "https://gallery.ecr.aws/codebuild/amazonlinux-x86_64-standard") with
   the following command:

```
`$` docker pull public.ecr.aws/codebuild/amazonlinux-x86_64-standard:4.0
```

Alternatively, if you want to use another Linux image, perform the following
steps:

    1. Clone the CodeBuild image repo:



    ```
    `$` git clone https://github.com/aws/aws-codebuild-docker-images.git
    ```
    2. Change to the image directory. For this example, use the
     `aws/codebuild/standard:5.0` image:



    ```
    `$` cd aws-codebuild-docker-images/ubuntu/standard/5.0
    ```
    3. Build the image. This will take several minutes.



    ```
    `$` docker build -t aws/codebuild/standard:5.0 .
    ```

2. Download the CodeBuild agent.

To download the x86_64 version of the agent, run the following command:

```
`$` docker pull public.ecr.aws/codebuild/local-builds:latest
```

To download the ARM version of the agent, run the following command:

```
`$` docker pull public.ecr.aws/codebuild/local-builds:aarch64
```

3. The CodeBuild agent is available from [https://gallery.ecr.aws/codebuild/local-builds](https://gallery.ecr.aws/codebuild/local-builds "https://gallery.ecr.aws/codebuild/local-builds").

The Secure Hash Algorithm (SHA) signature for the x86_64 version of the agent
is:

```
sha256:ccb19bdd7af94e4dc761e4c58c267e9455c28ec68d938086b4dc1cf8fe6b0940
```

The SHA signature for the ARM version of the agent is:

```
sha256:7d7b5d35d2ac4e062ae7ba8c662ffed15229a52d09bd0d664a7816c439679192
```

You can use the SHA to identify the version of the agent. To see the agent's
SHA signature, run the following command and look for the SHA under `RepoDigests`:

```
`$` docker inspect public.ecr.aws/codebuild/local-builds:latest
```

## Run the CodeBuild agent

###### To run the CodeBuild agent

1. Change to the directory that contains your build project source.
2. Download the [codebuild_build.sh](https://github.com/aws/aws-codebuild-docker-images/blob/master/local_builds/codebuild_build.sh "https://github.com/aws/aws-codebuild-docker-images/blob/master/local_builds/codebuild_build.sh") script:

```
`$` curl -O  https://raw.githubusercontent.com/aws/aws-codebuild-docker-images/master/local_builds/codebuild_build.sh
`$` chmod +x codebuild_build.sh
```

3. Run the `codebuild_build.sh` script and specify your container
   image and the output directory.

To run an x86_64 build, run the following command:

```
`$` ./codebuild_build.sh -i `<container-image>` -a `<output directory>`
```

To run an ARM build, run the following command:

```
`$` ./codebuild_build.sh -i `<container-image>` -a `<output directory>` -l public.ecr.aws/codebuild/local-builds:aarch64
```

Replace `<container-image>` with the name of the
container image, such as `aws/codebuild/standard:5.0` or
`public.ecr.aws/codebuild/amazonlinux-x86_64-standard:4.0`.

The script launches the build image and runs the build on the project in the
current directory. To specify the location of the build project, add the
`-s `<build project directory>``
option to the script command.

## Receive notifications for new

CodeBuild agent versions

You can subscribe to Amazon SNS notifications so you will be notified when new versions of
the AWS CodeBuild agent are released.

###### To subscribe to CodeBuild agent notifications

1. Open the Amazon SNS console at [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation bar, if it's not already selected, change the AWS Region to
   **US East (N. Virginia)**. You must select this AWS Region
   because the Amazon SNS notifications that you are subscribing to are created in this
   Region.
3. In the navigation pane, choose **Subscriptions**.
4. Choose **Create subscription**.
5. In **Create subscription**, do the following:
   1. For **Topic ARN**, use the following Amazon Resource
      Name (ARN):

   ```
   arn:aws:sns:us-east-1:850632864840:AWS-CodeBuild-Local-Agent-Updates
   ```

   2. For **Protocol**, choose **Email**
      or **SMS**.
   3. For **Endpoint**, choose where (email or SMS) to
      receive the notifications. Enter an email or address or phone number,
      including area code.
   4. Choose **Create subscription**.
   5. Choose **Email** to receive an email asking you to
      confirm your subscription. Follow the directions in the email to
      complete your subscription.

   If you no longer want to receive these notifications, use the
   following procedure to unsubscribe.

###### To unsubscribe from CodeBuild agent notifications

1. Open the Amazon SNS console at [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation pane, choose **Subscriptions**.
3. Select the subscription and from **Actions**, choose
   **Delete subscriptions**. When you are prompted to confirm,
   choose **Delete**.
