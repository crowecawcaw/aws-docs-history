# Install the CodeDeploy agent for Ubuntu Server

###### To install the CodeDeploy agent on Ubuntu Server

1. Sign in to the instance.
2. Enter the following commands, one after the other:

```
sudo apt update
```

For version 2.0.x and later:

```
sudo apt install wget
```

For version 1.8.x and earlier:

```
sudo apt install ruby-full wget
```

3. Enter the following command:

```
cd `/home/ubuntu`
```

`/home/ubuntu` represents the default user name for an
Ubuntu Server instance. If your instance was created using a custom AMI, the AMI owner
might have specified a different default user name. 4. Enter the following command. The `latestv2/` prefix serves the version
2.0.x installer, and the `latest/` prefix serves the version 1.8.x
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

For a list of bucket names and region identifiers, see [Resource kit bucket names by Region](resource-kit.md#resource-kit-bucket-names "resource-kit.md#resource-kit-bucket-names"). 5. Enter the following command:

```
chmod +x ./install
```

6. Do one of the following:

   - To install the latest version of the CodeDeploy agent:

   ```
   sudo ./install auto
   ```
   - To install a specific version of the CodeDeploy agent:

     - List the available versions in your Region:

     ```
     aws s3 ls s3://aws-codedeploy-`region-identifier`/releases/ --region `region-identifier` | grep '\.deb$'
     ```
     - Install one of the versions:

     For version 2.0.x and later, packages are architecture-specific:

     ```
     sudo ./install auto -v releases/codedeploy-agent_`version`_`arch`.deb
     ```

     Where `arch` is `amd64` or
     `arm64` depending on your instance architecture.

     For version 1.8.x and earlier, packages use a different naming
     convention:

     ```
     sudo ./install auto -v releases/codedeploy-agent_`version`_all.deb
     ```

     For the latest released version, see [Version history of the CodeDeploy agent](codedeploy-agent.md#codedeploy-agent-version-history "codedeploy-agent.md#codedeploy-agent-version-history").

###### To check that the service is running

1. Enter the following command:

```
systemctl status codedeploy-agent
```

If the CodeDeploy agent is installed and running:

For version 2.0.x and later, you should see: `The AWS CodeDeploy agent is running.`

For version 1.8.x and earlier, you should see: `The AWS CodeDeploy agent is running.` 2. If the agent is not running, start the service and check the status:

```
systemctl start codedeploy-agent
```

```
systemctl status codedeploy-agent
```
