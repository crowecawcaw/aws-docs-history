# Troubleshooting AWS CloudShell

While using AWS CloudShell, you might encounter issues, such as when you launch CloudShell or
perform key tasks using the shell command line interface. The information that's covered in
this chapter covers how to troubleshoot some of the common issues that you might
encounter.

For answers to a variety of questions about CloudShell, see the [AWS CloudShell FAQs](https://aws.amazon.com/cloudshell/faqs/ "https://aws.amazon.com/cloudshell/faqs/"). You can also search
for answers and post questions in the [AWS CloudShell Discussion
Forum](https://repost.aws/tags/TA5ZaPf1NkT4uNitnWVitlyQ/aws-cloud-shell "https://repost.aws/tags/TA5ZaPf1NkT4uNitnWVitlyQ/aws-cloud-shell"). When you enter this forum, you might be required to sign in to AWS. You
can also [contact us](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") directly.

## Troubleshooting errors

When you come across any of the following indexed errors, you can use the following
solutions to resolve these errors.

###### Topics

- [Denied
  access](#unable-to-launch-cloudshell "#unable-to-launch-cloudshell")
- [Insufficient
  permissions](#no-access-cloudshell "#no-access-cloudshell")
- [Unable to access AWS CloudShell command line](#locked-out-cloudshell "#locked-out-cloudshell")
- [Unable to ping external IP addresses](#ping-cloudshell "#ping-cloudshell")
- [There were some issues preparing your
  terminal](#old-browser-issue-cloudshell "#old-browser-issue-cloudshell")
- [Arrow keys not working correctly in PowerShell](#pwsh-arrow-keys "#pwsh-arrow-keys")
- [Unsupported Web Sockets cause a failure to
  start CloudShell sessions](#web-sockets-cloudshell "#web-sockets-cloudshell")
- [Unable to import the
  AWSPowerShell.NetCore module](#import-PowerShell-module "#import-PowerShell-module")
- [Docker is not running when using AWS CloudShell](#docker-not-running "#docker-not-running")
- [Docker has ran out of disk space](#docker-space-full "#docker-space-full")
- [docker push is timing out and keeps retrying](#docker-push-timeout "#docker-push-timeout")
- [Unable to access resources within VPC from
  my AWS CloudShell VPC environment](#unable-access-VPC-resources "#unable-access-VPC-resources")
- [The ENI used by AWS CloudShell for my VPC environment
  is not cleaned up](#unable-cleanup-VPC-ENI "#unable-cleanup-VPC-ENI")
- [User with
  CreateEnvironment permission for only VPC environments also has
  access to public AWS CloudShell environments](#user-has-access-to-publicCloudShellenv "#user-has-access-to-publicCloudShellenv")

### Denied

access

**Issue:** When you
try
to launch
CloudShell
from the
AWS Management Console, you
get the message "**`Unable to start the environment. To retry, refresh the
 browser or restart by selecting Actions, Restart AWS CloudShell`**
".
You're
denied access even after you have required permissions from your IAM administrator and
you have refreshed your browser or restarted CloudShell.

**Solution:** Contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

([back to top](troubleshooting.md "troubleshooting.md"))

### Insufficient

permissions

**Issue:** When you
try
to launch
CloudShell
from the
AWS Management Console, you
get the message **`"Unable to start the environment. You don't have required
 permissions. Ask your IAM administrator to grant access to AWS CloudShell"`**.
You're
denied access and notified that you don't have required permissions.

**Cause:** The IAM identity that you're using to
access AWS CloudShell lacks the necessary IAM permissions.

**Solution:** Request your IAM administrator to
provide you with the necessary permissions. They can do this either through adding an
attached AWS managed policy (AWSCloudShellFullAccess) or an embedded inline policy. For
more information, see [Managing AWS CloudShell access and usage with IAM
policies](sec-auth-with-identities.md#sec-auth-with-identities.title "sec-auth-with-identities.md#sec-auth-with-identities.title").

([back to top](troubleshooting.md "troubleshooting.md"))

### Unable to access AWS CloudShell command line

**Issue:** After modifying a file that the compute
environment uses, you can't access the command line in AWS CloudShell.

**Solution:** If you lose access after incorrectly
modifying `.bashrc` or any other file, you can return AWS CloudShell to its
default settings by [deleting your home
directory](getting-started.md#delete-shell-session "getting-started.md#delete-shell-session").

([back to top](troubleshooting.md "troubleshooting.md"))

### Unable to ping external IP addresses

**Issue:** When you run a ping command from the command
line (for example, `ping amazon.com`), you receive the following
message.

```
ping: socket: Operation not permitted
```

**Cause**: The ping utility uses Internet Control
Message Protocol (ICMP) to send echo requests packets to a target host. It waits for an
echo to reply from the target. Because the ICMP protocol isn't enabled in AWS CloudShell, the
ping utility doesn't operate in the shell's compute environment.

**Solution**: Due to the fact that ICMP is not supported in AWS CloudShell, you can run the following command
to install Netcat. Netcat is a is a computer networking utility for reading from, and writing to, network connections using TCP or UDP.

```
sudo yum install nc
nc -zv www.amazon.com 443
```

([back to top](troubleshooting.md "troubleshooting.md"))

### There were some issues preparing your

terminal

**Issue:** When trying to access AWS CloudShell using the
Microsoft Edge browser, you can't start a shell session, and the browser displays an
error message.

**Cause**: AWS CloudShell isn't compatible with earlier
versions of Microsoft Edge. You can access AWS CloudShell using the latest four major versions
of supported browsers.

**Solution:** Install an updated version of Edge browser
from the [Microsoft
site](https://www.microsoft.com/en-us/edge "https://www.microsoft.com/en-us/edge").

([back to top](troubleshooting.md "troubleshooting.md"))

### Arrow keys not working correctly in PowerShell

**Issue:** In normal operation, you can use arrow keys
to navigate the command line interface and scan backwards and forwards through your
command history. But, when you press arrow keys in certain versions of PowerShell on
AWS CloudShell, letters might be incorrectly outputted.

**Cause**: The situation where arrow keys incorrectly
output letters is a known issue with PowerShell 7.2.x versions running on Linux.

**Solution:** To strip out escape sequences that modify
the behavior of arrow keys, edit the PowerShell profile file and set the
`$PSStyle` variable to `PlainText`.

1. In the AWS CloudShell command line, enter the following command to open the profile
   file.

```
vim ~/.config/powershell/Microsoft.PowerShell_profile.ps1
```

###### Note

If you're already in PowerShell, you can also open the profile file in the
editor with the following command.

```
vim $PROFILE
```

2. In the editor, go to the end of the file's existing text, press **i** to enter **Insert** mode,
   and then add the following statement.

```
$PSStyle.OutputRendering = 'PlainText'
```

3. After you make the edit, press **Esc** to enter the command
   mode. Next, enter the following command to save the file and exit the
   editor.

```
:wq
```

###### Note

Your changes take effect the next time you start PowerShell.

([back to top](troubleshooting.md "troubleshooting.md"))

### Unsupported Web Sockets cause a failure to

start CloudShell sessions

**Issue:** When
you
try to start AWS CloudShell, you repeatedly receive the following message:
`Failed to open sessions : Timed out while opening the session`.

**Cause**: CloudShell depends on the
_WebSocket protocol_, which allows for two-way interactive
communication between your web browser and AWS CloudShell. If you're using a browser in a
private network, secure access to the internet is probably facilitated by proxy servers
and firewalls. WebSocket communication can usually traverse proxy servers without a
problem. But, in some cases, proxy servers prevent WebSockets from working correctly. If
this issue occurs, CloudShell can't start a shell session and the attempt to connect
eventually times out.

**Solution:** A connection timeout might be caused by an
issue other than unsupported WebSockets. If this is the case, first refresh the browser
window where the CloudShell command line interface is located.

If you're still getting timeout errors after the refresh, see the documentation for
your proxy server. And, make sure that your proxy server is configured to allow Web
Sockets. Alternatively, contact your network's system administrator.

###### Note

Say that you want to define granular permissions by allowlisting specific URLs.
You can add part of the URL that the AWS Systems Manager session uses to open a WebSocket
connection for sending input and receiving outputs. Your AWS CloudShell commands are sent
to that Systems Manager session.

The format for this StreamUrl that's used by Systems Manager is `wss://ssmmessages.**region**.amazonaws.com/v1/data-channel/**session-id**?stream=(input|output)`.

The **region** represents the Region identifier for
an AWS Region that's supported by AWS Systems Manager. For example,
`us-east-2` is the Region identifier for the US East (Ohio) Region.

Because the **session-id** is created _after_ a particular Systems Manager session is successfully started,
you can only specify `wss://ssmmessages.region.amazonaws.com` when
you update your URL allowlist. For more information, see the [StartSession](../../../systems-manager/latest/APIReference/API_StartSession.md "../../../systems-manager/latest/APIReference/API_StartSession.md") operation in the
_AWS Systems Manager API Reference_.

([back to top](troubleshooting.md "troubleshooting.md"))

### Unable to import the

`AWSPowerShell.NetCore` module

**Issue:** When you import the AWSPowerShell.NetCore
module in PowerShell by `Import-Module -Name AWSPowerShell.NetCore`, you
receive the following error message:

**`Import-Module: The specified module 'AWSPowerShell.NetCore' was not loaded
 because no valid module file was found in any module directory.`**

**Cause:** The `AWSPowerShell.NetCore` module
is replaced by the per-service AWS.Tools modules in AWS CloudShell.

**Solution:** Any explicit import statements might no
longer be required or need to be changed to the related per-service AWS.Tools
module.

- For most cases, as long as no .Net types are used, you don’t need any
  explicit import statement. The following are examples of import
  statements.
  - `Get-S3Bucket`
  - `(Get-EC2Instance).Instances`

- If .Net types are used, import the service-level module
  (`AWS.Tools.<Service>`). The following is example
  syntax.

```
Import-Module -Name AWS.Tools.EC2
$InstanceTag = [Amazon.EC2.Model.Tag]::new("Environment","Dev")
```

```
Import-Module -Name AWS.Tools.S3
$LifecycleRule = [Amazon.S3.Model.LifecycleRule]::new()
```

For more information, see the [version 4 announcement](https://aws.amazon.com/blogs/developer/aws-tools-for-powershell-is-now-generally-available-with-version-4-0/ "https://aws.amazon.com/blogs/developer/aws-tools-for-powershell-is-now-generally-available-with-version-4-0/") for the AWS Tools for PowerShell.

([back to top](troubleshooting.md "troubleshooting.md"))

### Docker is not running when using AWS CloudShell

**Issue:** Docker is not running properly when using
AWS CloudShell. You receive the following error message: `docker: Cannot connect to the
 Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?`.

**Solution:** Try restarting your environment. This
error message can occur when you run Docker in AWS CloudShell in a
GovCloud
Region.
Make sure that you are running Docker in the supported AWS Regions. For a list of
Regions in which Docker is available, see [Supported AWS Regions for
AWS CloudShell](supported-aws-regions.md "supported-aws-regions.md").

### Docker has ran out of disk space

**Issue:** You are receiving the following error
message: `ERROR: failed to solve: failed to register layer: write [...]: no space
 left on device`.

**Cause:** The Dockerfile is exceeding the available
disk space in AWS CloudShell. This can be caused due to large individual images or too many
pre-existing Docker images.

**Solution:** Run `df -h` to find the disk
usage. Run `sudo du -sh /folder/folder1` to asses the size of certain folders
that you feel may be large and consider deleting other files to free up space. One
option would be to consider removing unused Docker images by running `docker
 rmi`. You should be aware that Docker has limited space in the environment, for
more information on Docker, see the [Docker Documentation
guide](https://docs.docker.com/guides/docker-overview/ "https://docs.docker.com/guides/docker-overview/").

### `docker push` is timing out and keeps retrying

**Issue:** When you run `docker push` it is timing out and continues to retry with no success.

**Cause:** This can be caused as a result of missing permissions, pushing to the wrong repository or a lack of authentication.

**Solution:** To try and resolve this issue
make
sure you are pushing to the correct repository. Run `docker
 login` to properly authenticate.
Make
sure that you have all the required permissions for pushing to an
Amazon ECR repository.

### Unable to access resources within VPC from

my AWS CloudShell VPC environment

**Issue:** Unable to access resources within the VPC
while using my AWS CloudShell VPC environment.

**Cause:** Your AWS CloudShell VPC environment inherits the
network settings of your VPC.

**Solution:** To resolve this issue
make
sure that your VPC is set up correctly to access your resources. For
more information, see VPC documentation [Connect your VPC to other
networks](../../../vpc/latest/userguide/extend-intro.md "../../../vpc/latest/userguide/extend-intro.md") and the and the Network Access Analyzer documentation [Network Access Analyzer](../../../vpc/latest/network-access-analyzer/what-is-network-access-analyzer.md "../../../vpc/latest/network-access-analyzer/what-is-network-access-analyzer.md"). You can find the IPv4 address that the AWS CloudShell VPC
environment is using, by running the command **`ip -a`** inside your
environment in the command line prompt, or on the VPC Console page.

### The ENI used by AWS CloudShell for my VPC environment

is not cleaned up

**Issue:** Unable to clean up the ENI used by AWS CloudShell
for my VPC environment.

**Cause:**
`ec2:DeleteNetworkInterface` permission is not enabled for your role.

**Solution:** To resolve this issue,
make
sure that `ec2:DeleteNetworkInterface` permission is
enabled for your role as shown in the following sample script:

```
{
  "Effect": "Allow",
  "Action": [
    "ec2:DeleteNetworkInterface"
  ],
  "Condition": {
    "StringEquals": {
      "aws:ResourceTag/ManagedByCloudShell": ""
    }
  },
  "Resource": "arn:aws:ec2:*:*:network-interface/*"
}
```

### User with

`CreateEnvironment` permission for only VPC environments also has
access to public AWS CloudShell environments

**Issue:** User restricted with
`CreateEnvironment` permission for only VPC environments is also able to
access public AWS CloudShell environments.

**Cause:** When you limit `CreateEnvironment`
permissions for creation of VPC environments only and if you have already created a
public environment, you will keep your access to the existing public CloudShell
environment until this environment is deleted using the web user interface. But if you
have never used CloudShell before, you will not have access to public environments.

**Solution:** To restrict access to public AWS CloudShell
environments, the IAM administrator must first update the IAM policy with the
restriction, and then the user must manually delete the existing public environment
using the AWS CloudShell web user interface. (**Actions** → **Delete
CloudShell environment**).
