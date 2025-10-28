# Authenticating with image repositories

This topic describes how to authenticate to online image repositories with Elastic Beanstalk. For private repositories, Elastic Beanstalk must authenticate before it can pull and deploy your images. For Amazon ECR Public, authentication is optional but provides higher rate limits and improved reliability.

## Using images from an Amazon ECR repository

You can store your custom Docker images in AWS with [Amazon Elastic Container Registry](https://aws.amazon.com/ecr "https://aws.amazon.com/ecr") (Amazon ECR).

When you store your Docker images in Amazon ECR, Elastic Beanstalk automatically authenticates to the Amazon ECR registry with your environment's [instance profile](concepts-roles-instance.md "concepts-roles-instance.md"). Therefore you'll need to provide your instances with permission to access the images in your
Amazon ECR repository. To do so add permissions to your environment's instance profile by attaching the [AmazonEC2ContainerRegistryReadOnly](../../../aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryReadOnly.md "../../../aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryReadOnly.md") managed
policy to the instance profile. This provides read-only access to all the Amazon ECR repositories in your account. You also have the option to only access to
single repository by using the following template to create a custom policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowEbAuth",
 "Effect": "Allow",
 "Action": [
 "ecr:GetAuthorizationToken"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "AllowPull",
 "Effect": "Allow",
 "Resource": [
 "arn:aws:ecr:us-east-2:`111122223333`:repository/`repository-name`"
 ],
 "Action": [
 "ecr:GetAuthorizationToken",
 "ecr:BatchCheckLayerAvailability",
 "ecr:GetDownloadUrlForLayer",
 "ecr:GetRepositoryPolicy",
 "ecr:DescribeRepositories",
 "ecr:ListImages",
 "ecr:BatchGetImage"
 ]
 }
 ]
}`

```

Replace the Amazon Resource Name (ARN) in the above policy with the ARN of your repository.

You'll need to specify the image information in your `Dockerrun.aws.json` file. The configuration will be different depending on which
platform you use.

For the [ECS managed Docker platform](create_deploy_docker_v2config.md "create_deploy_docker_v2config.md"), use the `image` key in a container definition
object :

```
"containerDefinitions": [
        {
        "name": "my-image",
        "image": "`account-id`.dkr.ecr.us-east-2.amazonaws.com/`repository-name:latest`",
```

For the [Docker platform](single-container-docker-configuration.md "single-container-docker-configuration.md") refer to the image by URL. The URL goes in the `Image`
definition of your `Dockerrun.aws.json` file:

```
  "Image": {
      "Name": "`account-id`.dkr.ecr.us-east-2.amazonaws.com/`repository-name:latest`",
      "Update": "true"
    },
```

## Using AWS Systems Manager (SSM) Parameter Store or AWS Secrets Manager

Configure Elastic Beanstalk to authenticate with your private repository before deployment to enable access to your container images.

This approach uses the _prebuild_ phase of the Elastic Beanstalk deployment process with two components:

- [ebextensions](ebextensions.md "ebextensions.md") to define environment variables that store repository credentials
- [platform hook scripts](platforms-linux-extend.md "platforms-linux-extend.md") to execute **docker login** before pulling images

The hook scripts securely retrieve credentials from environment variables that are populated from AWS Systems Manager Parameter Store
or AWS Secrets Manager. This feature requires Elastic Beanstalk Docker and ECS managed Docker platforms released on or after [March 26, 2025](../relnotes/release-2025-03-26-windows.md "../relnotes/release-2025-03-26-windows.md").
For more details, see [environment variable configuration](AWSHowTo.secrets.md "AWSHowTo.secrets.md").

###### To configure Elastic Beanstalk to authenticate to your private repository with AWS Systems Manager Parameter Store or AWS Secrets Manager

###### Note

Before proceeding, ensure you have set up your credentials in AWS Systems Manager Parameter Store or AWS Secrets Manager
and configured the necessary IAM permissions. See [Prerequisites
to configure secrets as environment variables](AWSHowTo.secrets.md#AWSHowTo.secrets.configure-env-vars.prerequisites "AWSHowTo.secrets.md#AWSHowTo.secrets.configure-env-vars.prerequisites") for details.

1. Create the following directory structure for your project:

```

├── .ebextensions
│   └── env.config
├── .platform
│   ├── confighooks
│   │   └── prebuild
│   │       └── 01login.sh
│   └── hooks
│       └── prebuild
│           └── 01login.sh
├── Dockerfile
```

2. Use [AWS Systems Manager](../../../systems-manager/latest/userguide/getting-started.md "../../../systems-manager/latest/userguide/getting-started.md") Parameter Store
   or [AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") to save the
   credentials of your private repository. This example shows both AWS Systems Manager Parameter Store and AWS Secrets Manager
   but you can choose to use just one of these services.

```
aws ssm put-parameter --name USER --type SecureString --value "username"
aws secretsmanager create-secret --name PASSWD --secret-string "passwd"
```

3. Create the following `env.config` file and place it in the `.ebextensions` directory as shown in the
   preceding directory structure. This configuration uses the [aws:elasticbeanstalk:application:environmentsecrets](command-options-general.md#command-options-general-elasticbeanstalk-application-environmentsecrets "command-options-general.md#command-options-general-elasticbeanstalk-application-environmentsecrets") namespace to initialize the `USER` and
   `PASSWD` Elastic Beanstalk environment variables to the values that are stored in the Systems Manager Parameter Store.

###### Note

Ensure the variable names `USER` and `PASSWD` match the parameter names used in the
[put-parameter](../../../cli/latest/reference/ssm/put-parameter.md "../../../cli/latest/reference/ssm/put-parameter.md") and
[create-secret](../../../cli/latest/reference/secretsmanager/create-secret.md "../../../cli/latest/reference/secretsmanager/create-secret.md") commands.

```
option_settings:
  aws:elasticbeanstalk:application:environmentsecrets:
    USER: arn:aws:ssm:us-east-1:111122223333:parameter/user
    PASSWD: arn:aws:secretsmanager:us-east-1:111122223333:passwd
```

4. Create the following `01login.sh` script file and place it in the following directories (also shown in the preceding directory
   structure):
   - `.platform/confighooks/prebuild`
   - `.platform/hooks/prebuild`

```
### example 01login.sh
#!/bin/bash
echo $PASSWD | docker login -u $USER --password-stdin
```

The `01login.sh` script uses the environment variables configured in **Step 3**
and securely passes the password to **docker login** via `stdin`.
For more information about Docker authentication, see
[docker login](https://docs.docker.com/engine/reference/commandline/login/ "https://docs.docker.com/engine/reference/commandline/login/") in the Docker documentation.

###### Notes

    * Hook files can be either binary files or script files starting with a **#!** line containing their interpreter path, such as
     **#!/bin/bash**.
    * For more information, see [Platform hooks](platforms-linux-extend.md "platforms-linux-extend.md") in *Extending Elastic Beanstalk Linux
     platforms*.

Once authentication is configured, Elastic Beanstalk can pull and deploy images from your private repository.

## Using the `Dockerrun.aws.json` file

This section describes another approach to authenticate Elastic Beanstalk to a private repository. With this approach, you generate an authentication file with
the Docker command, and then upload the authentication file to an Amazon S3 bucket. You must also include the bucket information in your
`Dockerrun.aws.json` file.

###### To generate and provide an authentication file to Elastic Beanstalk

1. Generate an authentication file with the **docker login** command. For repositories on Docker Hub, run **docker
   login**:

```
$ `docker login`
```

For other registries, include the URL of the registry server:

```
$ `docker login `registry-server-url``
```

###### Note

If your Elastic Beanstalk environment uses the Amazon Linux AMI Docker platform version (precedes Amazon Linux 2), read the relevant information in [Docker configuration on Amazon Linux AMI (preceding Amazon Linux 2)](create_deploy_docker.container.md#docker-alami "create_deploy_docker.container.md#docker-alami").

For more information about the authentication file, see [Store images on Docker Hub](https://docs.docker.com/docker-hub/repos/ "https://docs.docker.com/docker-hub/repos/") and [docker login](https://docs.docker.com/engine/reference/commandline/login/ "https://docs.docker.com/engine/reference/commandline/login/") on the Docker website. 2. Upload a copy of the authentication file that is named `.dockercfg` to a secure Amazon S3 bucket.

    * The Amazon S3 bucket must be hosted in the same AWS Region as the environment that is using it. Elastic Beanstalk cannot download files from an Amazon S3 bucket
     hosted in other Regions.
    * Grant permissions for the `s3:GetObject` operation to the IAM role in the instance profile. For more information, see [Managing Elastic Beanstalk instance profiles](iam-instanceprofile.md "iam-instanceprofile.md").

3. Include the Amazon S3 bucket information in the `Authentication` parameter in your `Dockerrun.aws.json` file.

The following example shows the use of an authentication file named `mydockercfg` in a bucket named `amzn-s3-demo-bucket` to
use a private image in a third-party registry. For the correct version number for `AWSEBDockerrunVersion`, see the note that
follows the example.

```
{
  "AWSEBDockerrunVersion": "`version-no`",
  "Authentication": {
    "Bucket": "`amzn-s3-demo-bucket`",
    "Key": "`mydockercfg`"
  },
  "Image": {
    "Name": "quay.io/johndoe/private-image",
    "Update": "true"
  },
  "Ports": [
    {
      "ContainerPort": "1234"
    }
  ],
  "Volumes": [
    {
      "HostDirectory": "/var/app/mydb",
      "ContainerDirectory": "/etc/mysql"
    }
  ],
  "Logging": "/var/log/nginx"
}
```

###### Dockerrun.aws.json versions

The `AWSEBDockerrunVersion` parameter indicates the version of the `Dockerrun.aws.json` file.

    * The Docker AL2 and AL2023 platforms use the following versions of the file.



    	+ `Dockerrun.aws.json v3` — environments that use Docker Compose.

    	+ `Dockerrun.aws.json v1` — environments that do not use Docker Compose.
    * *ECS running on Amazon Linux 2* and *ECS running on AL2023* uses the
     `Dockerrun.aws.json v2` file. The retired platform *ECS-The Multicontainer Docker Amazon Linux AMI (AL1)* also used this
     same version.

After Elastic Beanstalk can authenticate with the online registry that hosts the private repository, your images can be deployed and pulled.

## Using images from Amazon ECR Public

Amazon ECR Public is a public container registry that hosts Docker images. While Amazon ECR Public repositories are publicly accessible, authenticating provides higher rate limits and better reliability for your deployments.

###### Note

Amazon ECR Public authentication is not supported in China regions (`cn-*`) and AWS GovCloud regions (`us-gov-*`). In these regions, Elastic Beanstalk will use unauthenticated pulls.

To enable Amazon ECR Public authentication, add the following permissions to your environment's [instance profile](concepts-roles-instance.md "concepts-roles-instance.md"). For more information about Amazon ECR Public authentication, see [Registry authentication in Amazon ECR public](../../../AmazonECR/latest/public/public-registries.md "../../../AmazonECR/latest/public/public-registries.md") in the _Amazon Elastic Container Registry Public User Guide_:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecr-public:GetAuthorizationToken",
 "sts:GetServiceBearerToken"
 ],
 "Resource": "*"
 }
 ]
}`

```

Once these permissions are attached to your instance profile, Elastic Beanstalk will automatically authenticate with Amazon ECR Public registries. You can reference Amazon ECR Public images using the standard `public.ecr.aws/`registry-alias`/`repository-name:tag``format in your`Dockerrun.aws.json` file or Dockerfile.
