

# Install the CodeDeploy agent for macOS
<a name="codedeploy-agent-operations-install-macos"></a>

Sign in to the instance, and run the following commands, one at a time.

Change to your home directory:

```
cd ~
```

Download the CodeDeploy agent installer package:

```
curl -O https://{{bucket-name}}.s3.{{region-identifier}}.amazonaws.com/latestv2/codedeploy-agent.aarch64.pkg
```

{{bucket-name}} is the name of the Amazon S3 bucket that contains the CodeDeploy Resource Kit files for your region, and {{region-identifier}} is the identifier for your region.

For example:

`https://aws-codedeploy-us-east-2.s3.us-east-2.amazonaws.com/latestv2/codedeploy-agent.aarch64.pkg`

For a list of bucket names and region identifiers, see [Resource kit bucket names by Region](resource-kit.md#resource-kit-bucket-names).

To install the latest version of the CodeDeploy agent:
+ 

  ```
  sudo installer -pkg codedeploy-agent.aarch64.pkg -target /
  ```

To install a specific version of the CodeDeploy agent:
+ List the available versions in your Region:

  ```
  aws s3 ls s3://aws-codedeploy-{{region-identifier}}/releases/ --region {{region-identifier}} | grep '\.pkg$'
  ```
+ Download and install one of the versions:

  ```
  aws s3 cp s3://aws-codedeploy-{{region-identifier}}/releases/codedeploy-agent-{{version}}.aarch64.pkg codedeploy-agent.aarch64.pkg --region {{region-identifier}}
  ```

  ```
  sudo installer -pkg codedeploy-agent.aarch64.pkg -target /
  ```

  For the latest released version, see [Version history of the CodeDeploy agent](codedeploy-agent.md#codedeploy-agent-version-history).

To check that the service is running, run the following command:

```
sudo /opt/codedeploy-agent/bin/codedeploy-agent status
```

If the agent is running, you should see a message like `The AWS CodeDeploy agent is running.`

If the agent is not running, start the service and check the status:

```
sudo launchctl kickstart system/com.amazon.aws.codedeploy-agent
```

```
sudo /opt/codedeploy-agent/bin/codedeploy-agent status
```