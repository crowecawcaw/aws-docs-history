# Install the CodeDeploy agent for

Ubuntu Server

###### Note

We recommend installing the CodeDeploy agent with AWS Systems Manager to be able to configure
scheduled updates of the agent. For more information, see [Install the CodeDeploy agent using
AWS Systems Manager](codedeploy-agent-operations-install-ssm.md "codedeploy-agent-operations-install-ssm.md").

###### To install the CodeDeploy agent on Ubuntu Server

1. Sign in to the instance.
2. Enter the following commands, one after the other:

```
sudo apt update
```

```
sudo apt install ruby-full
```

```
sudo apt install wget
```

3. Enter the following command:

```
cd `/home/ubuntu`
```

`/home/ubuntu` represents the default user name for an
Ubuntu Server instance. If your instance was created using a custom AMI, the AMI owner
might have specified a different default user name. 4. Enter the following command:

```
wget https://`bucket-name`.s3.`region-identifier`.amazonaws.com/latest/install
```

`bucket-name` is the name of the Amazon S3
bucket that contains the CodeDeploy Resource Kit files for your region, and `region-identifier` is the identifier for
your region.

For example:

`https://aws-codedeploy-us-east-2.s3.us-east-2.amazonaws.com/latest/install`

For a list of bucket names and region identifiers, see [Resource kit bucket names by Region](resource-kit.md#resource-kit-bucket-names "resource-kit.md#resource-kit-bucket-names"). 5. Enter the following command:

```
chmod +x ./install
```

6. Do one of the following:
   - To install the latest version of the CodeDeploy agent on any supported version of
     Ubuntu Server _except_ 20.04:

   ```
   sudo ./install auto
   ```

   - To install the latest version of the CodeDeploy agent on Ubuntu Server 20.04:

   ###### Note

   Writing the output to a temporary log file is a workaround that should be
   used while we address a known bug with the `install` script on
   Ubuntu Server 20.04.

   ```
   sudo ./install auto > /tmp/logfile
   ```

   - To install a specific version of the CodeDeploy agent on any supported version of
     Ubuntu Server _except_ 20.04:
     - List the available versions in your region:

     ```
     aws s3 ls s3://aws-codedeploy-`region-identifier`/releases/ --region `region-identifier` | grep '\.deb$'
     ```

     - Install one of the versions:

     ```
     sudo ./install auto -v releases/codedeploy-agent-`###`.deb
     ```

     ###### Note

     AWS supports the latest minor version of the CodeDeploy agent. Currently the latest minor version is 1.7.x.

   - To install a specific version of the CodeDeploy agent on Ubuntu Server 20.04:
     - List the available versions in your region:

     ```
     aws s3 ls s3://aws-codedeploy-`region-identifier`/releases/ --region `region-identifier` | grep '\.deb$'
     ```

     - Install one of the versions:

     ```
     sudo ./install auto -v releases/codedeploy-agent-`###`.deb > /tmp/logfile
     ```

     ###### Note

     Writing the output to a temporary log file is a workaround that should
     be used while we address a known bug with the `install` script on
     Ubuntu Server 20.04.

     ###### Note

     AWS supports the latest minor version of the CodeDeploy agent. Currently the latest minor version is 1.7.x.

###### To check that the service is running

1. Enter the following command:

```
systemctl status codedeploy-agent
```

If the CodeDeploy agent is installed and running, you should see a message like
`The AWS CodeDeploy agent is running`. 2. If you see a message like `error: No AWS CodeDeploy agent
 running`, start the service and run the following two commands, one at a
time:

```
systemctl start codedeploy-agent
```

```
systemctl status codedeploy-agent
```
