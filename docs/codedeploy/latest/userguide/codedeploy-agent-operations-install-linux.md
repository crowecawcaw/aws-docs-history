# Install the CodeDeploy agent for Amazon Linux or RHEL

Sign in to the instance, and run the following commands, one at a time. Running the
command `sudo yum update` first is considered best practice when using
`yum` to install packages, but you can skip it if you do not wish to update
all of your packages.

```
sudo yum update
```

For version 2.0.x and later:

```
sudo yum install wget
```

For version 1.8.x and earlier:

```
sudo yum install ruby wget
```

(Optional) To clean the AMI of any previous agent caching information, run the
following script:

```
#!/bin/bash
CODEDEPLOY_BIN="/opt/codedeploy-agent/bin/codedeploy-agent"
$CODEDEPLOY_BIN stop
yum erase codedeploy-agent -y
```

Change to your home directory:

```
cd /home/ec2-user
```

###### Note

In the previous command, `/home/ec2-user` represents the default user
name for an Amazon Linux or RHEL Amazon EC2 instance. If your instance was created using a custom
AMI, the AMI owner might have specified a different default user name.

Download the CodeDeploy agent installer. The `latestv2/` prefix serves the
version 2.0.x installer, and the `latest/` prefix serves the version 1.8.x
installer.

For version 2.0.x and later:

```
wget https://`bucket-name`.s3.`region-identifier`.amazonaws.com/latestv2/install
```

For version 1.8.x and earlier:

```
wget https://`bucket-name`.s3.`region-identifier`.amazonaws.com/latest/install
```

`bucket-name` is the name of the Amazon S3
bucket that contains the CodeDeploy Resource Kit files for your region, and `region-identifier` is the identifier for
your region.

For example, for version 2.0.x and later:

`https://aws-codedeploy-us-east-2.s3.us-east-2.amazonaws.com/latestv2/install`

For version 1.8.x and earlier:

`https://aws-codedeploy-us-east-2.s3.us-east-2.amazonaws.com/latest/install`

For a list of bucket names and region identifiers, see [Resource kit bucket names by Region](resource-kit.md#resource-kit-bucket-names "resource-kit.md#resource-kit-bucket-names").

Set execute permissions on the `install` file:

```
chmod +x ./install
```

To install the latest version of the CodeDeploy agent:

- ```

  ```

sudo ./install auto

```
To install a specific version of the CodeDeploy agent:


* List the available versions in your Region:



```

aws s3 ls s3://aws-codedeploy-`region-identifier`/releases/ --region `region-identifier` | grep '\.rpm$'

```
* Install one of the versions:


For version 2.0.x and later, packages are architecture-specific:



```

sudo ./install auto -v releases/codedeploy-agent-`version`.`arch`.rpm

```

Where `arch` is `x86_64` or
 `aarch64` depending on your instance architecture.


For version 1.8.x and earlier, packages use `noarch`:



```

sudo ./install auto -v releases/codedeploy-agent-`version`.noarch.rpm

```

For the latest released version, see [Version history of the CodeDeploy agent](codedeploy-agent.md#codedeploy-agent-version-history "codedeploy-agent.md#codedeploy-agent-version-history").
To check that the service is running, run the following command:


```

systemctl status codedeploy-agent

```
For version 2.0.x and later, if the agent is running, you should see a message like
 `The AWS CodeDeploy agent is running.`

For version 1.8.x and earlier, if the agent is running, you should see a message like
 `The AWS CodeDeploy agent is running.`

If the agent is not running, start the service and check the status:


```

systemctl start codedeploy-agent

```

```

systemctl status codedeploy-agent

```

```
