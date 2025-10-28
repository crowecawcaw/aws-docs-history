# Getting started with local mode

The following sections outline the steps needed to get started with local mode in
Amazon SageMaker Studio, including:

- Completing prerequisites
- Setting `EnableDockerAccess`
- Docker installation

## Prerequisites

Complete the following prerequisites to use local mode in Studio
applications:

- To pull images from an Amazon Elastic Container Registry repository, the account hosting the Amazon ECR image
  must provide access permission for the user’s execution role. The domain’s execution
  role must also allow Amazon ECR access.
- Verify that you are using the latest version of the Studio Python SDK by using
  the following command: 

```
pip install -U sagemaker
```

- To use local mode and Docker capabilities, set the following
  parameter of the domain’s `DockerSettings` using the AWS Command Line Interface
  (AWS CLI): 

```
EnableDockerAccess : ENABLED
```

- Using `EnableDockerAccess`, you can also control whether users in the
  domain can use local mode. By default, local mode and Docker capabilities
  aren't allowed in Studio applications. For more information, see [Setting
  EnableDockerAccess](#studio-updated-local-enable "#studio-updated-local-enable").
- Install the Docker CLI in the Studio application by following
  the steps in [Docker
  installation](#studio-updated-local-docker-installation "#studio-updated-local-docker-installation").
- For the [Rootless Docker configuration](#studio-updated-local-rootless "#studio-updated-local-rootless"), ensure your VPC has appropriate
  endpoints and routing configured for your desired Docker registries.

## Setting

`EnableDockerAccess`

The following sections show how to set `EnableDockerAccess` when the domain
has public internet access or is in `VPC-only` mode.

###### Note

Changes to `EnableDockerAccess` only apply to applications created after
the domain is updated. You must create a new application after updating the domain.

**Public internet access**

The following example commands show how to set `EnableDockerAccess` when
creating a new domain or updating an existing domain with public internet access:

```
# create new domain
aws --region `region` \
    sagemaker create-domain --domain-name `domain-name` \
    --vpc-id `vpc-id` \
    --subnet-ids `subnet-ids` \
    --auth-mode IAM \
    --default-user-settings "ExecutionRole=`execution-role`" \
    --domain-settings '{"DockerSettings": {"EnableDockerAccess": "ENABLED"}}' \
    --query DomainArn \
    --output text

# update domain
aws --region `region` \
    sagemaker update-domain --domain-id `domain-id` \
    --domain-settings-for-update '{"DockerSettings": {"EnableDockerAccess": "ENABLED"}}'
```

**`VPC-only` mode**

When using a domain in `VPC-only` mode, Docker image push and
pull requests are routed through the service VPC instead of the VPC configured by the
customer. Because of this functionality, administrators can configure a list of trusted
AWS accounts that users can make Amazon ECR Docker pull and push operations
requests to.

If a Docker image push or pull request is made to an AWS account that
is not in the list of trusted AWS accounts, the request fails. Docker pull
and push operations outside of Amazon Elastic Container Registry (Amazon ECR) aren't supported in `VPC-only`
mode.

The following AWS accounts are trusted by default:

- The account hosting the SageMaker AI domain.
- SageMaker AI accounts that host the following SageMaker images:
  - DLC framework images
  - Sklearn, Spark, XGBoost processing images

To configure a list of additional trusted AWS accounts, specify the
`VpcOnlyTrustedAccounts` value as follows:

```
aws --region `region` \
    sagemaker update-domain --domain-id `domain-id` \
    --domain-settings-for-update '{"DockerSettings": {"EnableDockerAccess": "ENABLED", "VpcOnlyTrustedAccounts": ["`account-list`"]}}'
```

###### Note

When the [Rootless Docker configuration](#studio-updated-local-rootless "#studio-updated-local-rootless") is enabled,
`VpcOnlyTrustedAccounts` is ignored and Docker traffic routes through your
VPC configuration, allowing access to any registry your VPC can reach.

## Rootless Docker configuration

When [`RootlessDocker`](../APIReference/API_DockerSettings.md "../APIReference/API_DockerSettings.md") is enabled, Studio uses a [rootless Docker daemon](https://docs.docker.com/engine/security/rootless/ "https://docs.docker.com/engine/security/rootless/")
that routes traffic through your VPC. This provides enhanced security and allows access to
additional Docker registries. The key differences with `RootlessDocker`
are:

- Container ports are accessible using the Docker gateway IP (`172.17.0.1`)
  instead of localhost.
- Your VPC configuration determines which registries are accessible for Docker
  operations. `VpcOnlyTrustedAccounts` is ignored and Docker traffic routes
  through your VPC configuration.

To use rootless Docker, you will need to set both `EnableDockerAccess` and
`RootlessDocker` to `ENABLED` for your `DockerSettings`.
For example, in the [Setting
EnableDockerAccess](#studio-updated-local-enable "#studio-updated-local-enable") examples above, you can modify your domain
settings to include:

```
'{"DockerSettings": {"EnableDockerAccess": "ENABLED", "RootlessDocker": "ENABLED"}}'
```

## Docker

installation

To use Docker, you must manually install Docker from the
terminal of your Studio application. The steps to install Docker are
different if the domain has access to the internet or not.

### Internet

access

If the domain is created with public internet access or in `VPC-only` mode
with limited internet access, use the following steps to install
Docker.

1. (Optional) If your domain is created in `VPC-only` mode with limited
   internet access, create a public NAT gateway with access to the Docker
   website. For instructions, see [NAT gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md").
2. Navigate to the terminal of the Studio application that you want to
   install Docker in.
3. To return the operating system of the application, run the following command from
   the terminal:

```
cat /etc/os-release
```

4. Install Docker following the instructions for the operating system
   of the application in the [Amazon SageMaker AI Local Mode Examples repository](https://github.com/aws-samples/amazon-sagemaker-local-mode/tree/main/sagemaker_studio_docker_cli_install "https://github.com/aws-samples/amazon-sagemaker-local-mode/tree/main/sagemaker_studio_docker_cli_install").

For example, install Docker on Ubuntu following the
script at [https://github.com/aws-samples/amazon-sagemaker-local-mode/blob/main/sagemaker_studio_docker_cli_install/sagemaker-ubuntu-focal-docker-cli-install.sh](https://github.com/aws-samples/amazon-sagemaker-local-mode/blob/main/sagemaker_studio_docker_cli_install/sagemaker-ubuntu-focal-docker-cli-install.sh "https://github.com/aws-samples/amazon-sagemaker-local-mode/blob/main/sagemaker_studio_docker_cli_install/sagemaker-ubuntu-focal-docker-cli-install.sh")
with the following considerations:

    * If chained commands fail, run commands one at a time.
    * Studio only supports Docker version `20.10.X.`
     and Docker Engine API version `1.41`.
    * The following packages aren't required to use the Docker CLI in
     Studio and their installation can be skipped:




    	+ `containerd.io`
    	+ `docker-ce`
    	+ `docker-buildx-plugin`

###### Note

You do not need to start the Docker service in your applications.
The instance that hosts the Studio application runs Docker
service by default. All Docker API calls are routed through the
Docker service automatically. 5. Use the exposed Docker socket for Docker
interactions within Studio applications. By default, the following socket is
exposed:

```
unix:///docker/proxy.sock
```

The following Studio application environmental variable for the default
`USER` uses this exposed socket:

```
DOCKER_HOST
```

### No internet

access

If the domain is created in `VPC-only` mode with no internet access, use
the following steps to install Docker.

1. Navigate to the terminal of the Studio application that you want to
   install Docker in.
2. Run the following command from the terminal to return the operating system of the
   application:

```
cat /etc/os-release
```

3. Download the required Docker
   `.deb` files to your local machine. For instructions about downloading the
   required files for the operating system of the Studio application, see [Install Docker Engine](https://docs.docker.com/engine/install/ "https://docs.docker.com/engine/install/").

For example, install Docker from a package on Ubuntu following the
steps 1–4 in [Install
from a package](https://docs.docker.com/engine/install/ubuntu/#install-from-a-package "https://docs.docker.com/engine/install/ubuntu/#install-from-a-package") with the following considerations:

    * Install Docker from a package. Using other methods to install
     Docker will fail.
    * Install the latest packages corresponding to Docker
     version `20.10.X`.
    * The following packages aren't required to use the Docker CLI in
     Studio. You don't need to install the following:




    	+ `containerd.io`
    	+ `docker-ce`
    	+ `docker-buildx-plugin`

###### Note

You do not need to start the Docker service in your applications.
The instance that hosts the Studio application runs Docker
service by default. All Docker API calls are routed through the
Docker service automatically. 4. Upload the `.deb` files to the Amazon EFS file system or to the Amazon EBS file
system of the application. 5. Manually install the `docker-ce-cli` and
`docker-compose-plugin`
`.deb` packages from the Studio application terminal. For more
information and instructions, see step 5 in [Install
from a package](https://docs.docker.com/engine/install/ubuntu/#install-from-a-package "https://docs.docker.com/engine/install/ubuntu/#install-from-a-package") on the Docker docs website. 6. Use the exposed Docker socket for Docker
interactions within Studio applications. By default, the following socket is
exposed:

```
unix:///docker/proxy.sock
```

The following Studio application environmental variable for the default
`USER` uses this exposed socket:

```
DOCKER_HOST
```
