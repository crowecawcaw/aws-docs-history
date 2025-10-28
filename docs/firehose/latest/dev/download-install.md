# Download and install the Agent

First, connect to your instance. For more information, see [Connect to Your
Instance](../../../AWSEC2/latest/UserGuide/ec2-connect-to-instance-linux.md "../../../AWSEC2/latest/UserGuide/ec2-connect-to-instance-linux.md") in the _Amazon EC2 User Guide_. If you have trouble
connecting, see [Troubleshooting Connecting to Your Instance](../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md "../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md") in the
_Amazon EC2 User Guide_.

Next, install the agent using one of the following methods.

- **To set up the agent from the Amazon Linux repositories**

This method works only for Amazon Linux instances. Use the following
command:

```

sudo yum install –y aws-kinesis-agent

```

Agent v 2.0.0 or later is installed on computers with operating system Amazon
Linux 2 (AL2). This agent version requires Java 1.8 or later. If required Java
version is not yet present, the agent installation process installs it. For more
information regarding Amazon Linux 2 see [https://aws.amazon.com/amazon-linux-2/](https://aws.amazon.com/amazon-linux-2/ "https://aws.amazon.com/amazon-linux-2/").

- **To set up the agent from the Amazon S3
  repository**

This method works for Red Hat Enterprise Linux, as well as Amazon Linux 2
instances because it installs the agent from the publicly available repository.
Use the following command to download and install the latest version of the
agent version 2.x.x:

```

sudo yum install –y https://s3.amazonaws.com/streaming-data-agent/aws-kinesis-agent-latest.amzn2.noarch.rpm

```

To install a specific version of the agent, specify the version number in the
command. For example, the following command installs agent v 2.0.1.

```

sudo yum install –y https://streaming-data-agent.s3.amazonaws.com/aws-kinesis-agent-2.0.1-1.amzn1.noarch.rpm

```

If you have Java 1.7 and you don’t want to upgrade it, you can download agent
version 1.x.x, which is compatible with Java 1.7. For example, to download agent
v1.1.6, you can use the following command:

```

sudo yum install –y https://s3.amazonaws.com/streaming-data-agent/aws-kinesis-agent-1.1.6-1.amzn1.noarch.rpm

```

You can download the latest agent with the following command

```
sudo yum install -y https://s3.amazonaws.com/streaming-data-agent/aws-kinesis-agent-latest.amzn2.noarch.rpm
```

- **To set up the agent from the GitHub
  repo**
  1.  First, make sure that you have required Java version installed,
      depending on agent version.
  2.  Download the agent from the [awslabs/amazon-kinesis-agent](https://github.com/awslabs/amazon-kinesis-agent "https://github.com/awslabs/amazon-kinesis-agent") GitHub repo.
  3.  Install the agent by navigating to the download directory and running
      the following command:

  ```

  sudo ./setup --install

  ```

- ###### To set up the agent in a Docker container

Kinesis Agent can be run in a container as well via the [amazonlinux](../../../AmazonECR/latest/userguide/amazon_linux_container_image.md "../../../AmazonECR/latest/userguide/amazon_linux_container_image.md") container base. Use the following Dockerfile
and then run `docker build`.

```
`FROM amazonlinux

RUN yum install -y aws-kinesis-agent which findutils
COPY agent.json /etc/aws-kinesis/agent.json

CMD ["start-aws-kinesis-agent"]`
```
