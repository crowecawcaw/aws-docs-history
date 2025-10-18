AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Troubleshooting AWS Cloud9

Use the following information to identify and address issues with AWS Cloud9.

If your issue isn't listed or you need additional help, see the [AWS Cloud9 Discussion Forum](https://forums.aws.amazon.com/forum.jspa?forumID=268 "https://forums.aws.amazon.com/forum.jspa?forumID=268"). You
 might be required to sign in when you enter this forum. You can also [contact us](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") directly.

###### Topics

* [Installer](#troubleshooting-installer-group "#troubleshooting-installer-group")
* [AWS Cloud9 Environment](#troubleshooting-environment-group "#troubleshooting-environment-group")
* [Amazon EC2](#troubleshooting-ec2-group "#troubleshooting-ec2-group")
* [Other AWS services](#troubleshooting-other-services-group "#troubleshooting-other-services-group")
* [Application preview](#troubleshooting-preview-group "#troubleshooting-preview-group")
* [Performance](#troubleshooting-performance-group "#troubleshooting-performance-group")
* [Third party applications and
 services](#troubleshooting-third-party-group "#troubleshooting-third-party-group")

## Installer


The following section outlines troubleshooting issues related to the AWS Cloud9
 installer.


### The AWS Cloud9 installer hangs or
 fails



**Issue:** When you [download and run the AWS Cloud9 Installer](installer.md#installer-download-run "installer.md#installer-download-run"), one or more error occurs, and the
 installer script doesn't show `Done`.



**Cause:** The AWS Cloud9 Installer encountered one or more
 errors that it can't recover from and fails as a result.



**Solution:** For more information, see [Troubleshooting the AWS Cloud9 Installer](installer.md#installer-troubleshooting "installer.md#installer-troubleshooting").
 Refer to the common issues, possible causes, and recommended solutions provided.


### AWS Cloud9 installer doesn't finish after
 displaying: "Package Cloud9 IDE 1"


**Issue:** AWS Cloud9 is installed on your existing Amazon EC2
 instance or on your own server as part of the process of creating an SSH development
 environment. The installation stalls after you see this message in the **AWS Cloud9 Installer** dialog box: "Package Cloud9 IDE 1". If you
 choose **Cancel**, you see the following message:
 "Installation Failed." This error occurs when AWS Cloud9 packages can't be installed on the
 customer's SSH host.


**Cause:** An SSH host requires that you installed
 Node.js. We recommend installing the latest Node.js version supported by
 the host's operating system. If you have a version of Node.js on your
 host that AWS Cloud9 doesn't support, an installation error might occur.


**Recommended solution:** Install a version of **Node.js** that AWS Cloud9 supports on your SSH host.


### Failed to install dependencies


**Issue:** AWS Cloud9 needs internet access to download
 dependencies.


**Possible causes:**

 
* If your AWS Cloud9 environment is using
 a proxy to access the internet, AWS Cloud9 needs the proxy details to install dependencies.
 If you didn't provide your proxy details to AWS Cloud9, this error appears.
* Another cause of
 this could be if your environment doesn't allow outbound traffic.

**Recommended solutions:**


* To provide your proxy details to AWS Cloud9, append the following code to your environments `~/.bashrc` file:



```
export http_proxy=[proxy url for http]
export https_proxy=[proxy url for https]
#Certificate Authority used by your proxy
export NODE_EXTRA_CA_CERTS=[path_to_pem_certificate]
```
For example, if your HTTP proxy URL is `https://172.31.26.80:3128` and your HTTP proxy URL is `https://172.31.26.80:3129`, 
 add the following lines to your `~/.bashrc` file and set `NODE_EXTRA_CA_CERTS` to the path of a certificate authority file in PEM format. For more information on this variable, 
 see [https://nodejs.org/api/cli.html#node\_extra\_ca\_certsfile](https://nodejs.org/api/cli.html#node_extra_ca_certsfile "https://nodejs.org/api/cli.html#node_extra_ca_certsfile").



```
export http_proxy=http://172.31.26.80:3128
export https_proxy=https://172.31.26.80:3129
export NODE_EXTRA_CA_CERTS=[path_to_pem_certificate]
```
* If you are using a no-ingress Amazon EC2 instance you must ensure an Amazon VPC endpoint for Amazon S3 is configured. For more information on this, see [Configuring Amazon VPC endpoints for Amazon S3 download dependencies.](ec2-ssm.md#configure-s3-endpoint "ec2-ssm.md#configure-s3-endpoint")

### SSH environment error: "Python version 3 is
 required to install pty.js"



**Issue:** After you open an AWS Cloud9 SSH development environment, the terminal in
 the AWS Cloud9 IDE displays a message that begins with "Python version 3 is required to
 install pty.js."



**Cause:** To work as expected, an SSH environment requires that
 Python version 3 is installed.



**Solution:** Install Python version 3 in the environment. To
 check your version, from your server's terminal, run the command **`python --version`**. To install Python 3 on your server, see one of the following:



* [Step 1: Install Python](sample-python.md#sample-python-install "sample-python.md#sample-python-install") in
 the *Python Sample*.
* [Download Python](https://www.python.org/downloads/ "https://www.python.org/downloads/") on the
 Python website.

## AWS Cloud9 Environment


The following section outlines troubleshooting issues related to the AWS Cloud9
 Environment.


### Environment creation error: "We
 are unable to create EC2 instances ..."



**Issue:** When you try to create an AWS Cloud9 development environment, a
 message appears with the phrase "We are unable to create EC2 instances in your account
 during account verification and activation." 



**Cause:** AWS is currently verifying and activating your
 AWS account. Before activation is complete, which can take up to 24 hours, you can't
 create this or other environments. 



**Solution:** Try creating the environment again later. If you're
 still receiving this message after 24 hours, contact [support](https://support.aws.amazon.com/#/contacts/aws-account-verification "https://support.aws.amazon.com/#/contacts/aws-account-verification"). Besides
 this, it's important to know that, even when an attempt to create an environment fails,
 AWS CloudFormation creates a related stack in your account. These stacks count towards the stack
 creation quota for your account. To avoid exhausting the stack creation quota, you can
 delete these failed stacks. For more information, see [Deleting a Stack on the AWS CloudFormation
 Console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md") in the *AWS CloudFormation User Guide*.


### Environment creation error: "Not
 authorized to perform sts:AssumeRole"



**Issue:** When you try to create a new environment, you see this
 error: "Not authorized to perform sts:AssumeRole," and the environment isn't created.



**Possible causes:** An AWS Cloud9 service-linked role doesn't
 exist in your AWS account.



**Recommended solutions:** Create an AWS Cloud9 service-linked
 role in your AWS account. You can do so by running the following command in the
 AWS Command Line Interface (AWS CLI) or the AWS CloudShell.



```
aws iam create-service-linked-role --aws-service-name cloud9.amazonaws.com # For the AWS CLI.
iam create-service-linked-role --aws-service-name cloud9.amazonaws.com     # For the aws-shell.
```

If you can't do this, check with your AWS account administrator.


After you run this command, try creating the environment again.


### Federated identities can't
 create environments



**Issue:** When you try to use an AWS federated identity
 to create an AWS Cloud9 development environment, an access error message is displayed, and the environment isn't
 created.



**Cause:** : AWS Cloud9 uses service-linked roles. The
 service-linked role is created the first time that an environment is created in an account
 using the `iam:CreateServiceLinkedRole` call. However, federated users can't
 call IAM APIs. For more information, see [GetFederationToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_API_GetFederationToken.html "https://docs.aws.amazon.com/STS/latest/APIReference/API_API_GetFederationToken.html") in the
 *AWS Security Token Service API Reference*.



**Solution:** Ask an AWS account administrator to create
 the service-linked role for AWS Cloud9 either in the IAM console or by running this command
 with the AWS Command Line Interface (AWS CLI):



```
aws iam create-service-linked-role --aws-service-name cloud9.amazonaws.com
```

Or this command with the AWS-shell:



```
iam create-service-linked-role --aws-service-name cloud9.amazonaws.com
```

For more information, see [Using Service-Linked Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html") in the
 *IAM User Guide*.


### Console error: "User is not
 authorized to perform action on resource"



**Issue:** When you try to use the AWS Cloud9 console to create
 or manage an AWS Cloud9 development environment, you see an error that contains a phrase similar to "User
 `arn:aws:iam::123456789012:user/MyUser` is not authorized to perform
 `cloud9:action` on resource
 `arn:aws:cloud9:us-east-2:123456789012:environment:12a34567b8cd9012345ef67abcd890e1`,"
 where:



* `arn:aws:iam::123456789012:user/MyUser` is the Amazon Resource Name
 (ARN) of the requesting user.
* `action` is the name of the operation that the user requested.
* `arn:aws:cloud9:us-east-2:123456789012:environment:12a34567b8cd9012345ef67abcd890e1`
 is the ARN of the environment that the user requested to run the operation.


**Cause:** The user that you signed in to the AWS Cloud9 console
 with doesn't have the correct AWS access permissions to perform the action.



**Solution:** Ensure that the user has the correct AWS
 access permissions, and then try to perform the action again. For more information, see
 the following:



* [Step 2: Add AWS Cloud9 access permissions to the
 group](setup.md#setup-give-user-access "setup.md#setup-give-user-access") in
 *Team Setup*
* [Step 6. Enable groups and users
 within the organization to use AWS Cloud9](setup-enterprise.md#setup-enterprise-groups-users-access "setup-enterprise.md#setup-enterprise-groups-users-access") in *Enterprise
 Setup*
* [About environment member access roles](share-environment.md#share-environment-member-roles "share-environment.md#share-environment-member-roles") in *Working with
 Shared Environments*

### Can't connect to an environment



**Issue:** Users can't connect to an environment, and are
 stuck at the Connecting stage.



**Cause:** If you change the permissions of the
 `~/ .ssh/authorized_keys` file, remove the AWS Cloud9 keys from that
 file, or remove the file entirely, this issue might occur.



**Solution:** Do not delete this file. If you delete it,
 you must recreate your environment and might need to attach the [EBS volume](move-environment.md#move-environment.title "move-environment.md#move-environment.title") of an existing environment to the
 new EC2 environment. This is to retrieve your lost data. If there are missing
 permissions, ensure that the file has `Read-Write` permissions. This is to
 allow the SSH daemon to read it.


### Can't open an environment



**Issue:** When you try to open an environment, the IDE doesn't
 display for more than five minutes.



**Possible causes:**




* The IAM user that's signed in to the AWS Cloud9 console doesn't have the required
 AWS access permissions to open the environment.
* If the environment is associated with an AWS cloud compute instance (for example,
 an Amazon EC2 instance), then the possible might be true:




	+ The VPC that's associated with the instance isn't set to the correct
	 settings for AWS Cloud9.
	+ The instance is transitioning between states or is failing automated
	 status checks when AWS Cloud9 is trying to connect to the instance.
* If the environment is an SSH environment, the associated cloud compute instance or your own
 server isn't set up correctly to allow AWS Cloud9 to access it.


**Recommended solutions:**




* Make sure the IAM user that's signed in to the AWS Cloud9 console has the required
 AWS access permissions to open the environment. Then, try opening the environment again. For
 more information see the following, or check with your AWS account
 administrator:




	+ [Step 2: Add AWS Cloud9 access permissions to the
	 group](setup.md#setup-give-user-access "setup.md#setup-give-user-access") in *Team
	 Setup*
	+ [AWS managed policies for
	 AWS Cloud9](security-iam.md#auth-and-access-control-managed-policies "security-iam.md#auth-and-access-control-managed-policies") in
	 *Authentication and Access Control*
	+ [Customer managed policy examples for teams using
	 AWS Cloud9](setup-teams-policy-examples.md "setup-teams-policy-examples.md") in *Advanced Team
	 Setup*
	+ [Customer managed
	 policy examples](security-iam.md#auth-and-access-control-customer-policies-examples "security-iam.md#auth-and-access-control-customer-policies-examples") in
	 *Authentication and Access Control*
	+ [Changing
	 Permissions for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html") in the
	 *IAM User Guide*
	+ [Troubleshoot IAM
	 Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_policies.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_policies.html") in the *IAM User Guide*
If the signed-in IAM user still can't open the environment, try signing out and
 then signing back in as either the AWS account root user or an administrator
 user in the account. Then, try opening the environment again. If you can't open the
 environment in this way, then there is most likely a problem with the IAM users access
 permissions.
* If the environment is associated with an AWS cloud compute instance (for example,
 an Amazon EC2 instance), do the following:




	+ Make sure that the VPC that's associated with the instance is set to the
	 correct settings for AWS Cloud9, and then try opening the environment again. For more
	 information, see [Amazon VPC requirements for AWS Cloud9](vpc-settings.md#vpc-settings-requirements "vpc-settings.md#vpc-settings-requirements").
	
	
	If the VPC that's associated with the AWS cloud compute instance is set
	 to the correct settings for AWS Cloud9 and you still can't open the environment, the
	 instance's security group might be preventing access to AWS Cloud9. **As a troubleshooting technique only**, check the
	 security group to make sure that at minimum, inbound SSH traffic is allowed
	 over port 22 for all IP addresses (`Anywhere` or
	 `0.0.0.0/0`). For instructions, see [Describing Your Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html#describing-security-group "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html#describing-security-group") and [Updating Security Group Rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html#updating-security-group-rules "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html#updating-security-group-rules") in the
	 *Amazon EC2 User Guide*.
	
	
	For additional VPC troubleshooting steps, watch the related 5-minute
	 video [AWS
	 Knowledge Center Videos: What can I check if I cannot connect to an
	 instance in a VPC?](https://www.youtube.com/watch?v=--BoDeCF5Dw "https://www.youtube.com/watch?v=--BoDeCF5Dw") on YouTube.
	
	
	###### Warning
	
	When you finished troubleshooting, make sure to set the inbound rules
	 to an appropriate address range. For more information, see [Inbound SSH IP address ranges for AWS Cloud9](ip-ranges.md "ip-ranges.md").
	+ Restart the instance, make sure that the instance is running and passed
	 all system checks, and then try opening the environment again. For more
	 information, see [Reboot
	 Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-reboot.html "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-reboot.html") and [Viewing Status Checks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html#viewing_status "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html#viewing_status") in the
	 *Amazon EC2 User Guide*.
* If the environment is an SSH environment, make sure the cloud compute instance associated
 with it or your own server is set up correctly to allow AWS Cloud9 to access it. Then,
 try opening the environment again. For more information, see [SSH environment host requirements](ssh-settings.md "ssh-settings.md").

### Can't open AWS Cloud9 environment: "This
 environment cannot be currently accessed by collaborators. Please wait until the
 removal of managed temporary credentials is complete, or contact the owner of this
 environment."


**Issue:** If a new collaborator is added to an environment by
 someone who isn't the environment owner, AWS managed temporary credentials are disabled. The credentials are
 disabled when you delete the `~/.aws/credentials` file. While the
 `~/.aws/credentials` file is being deleted, new collaborators
 can't access the AWS Cloud9 environment.


**Cause:** Preventing access to the environment while the
 AWS managed temporary credentials is being deleted is a security measure. This allows environment owners to
 confirm that only trusted collaborators can access managed credentials. If they're
 satisfied that the list of collaborators is valid, environment owners can re-enable
 managed credentials so they can be shared. For more information, see [Controlling access to
 AWS managed temporary credentials](security-iam.md#temporary-managed-credentials-control "security-iam.md#temporary-managed-credentials-control").


**Recommended solutions:** Wait for the
 `~/.aws/credentials` file to be fully deleted before trying again
 to open the AWS Cloud9 environment. The maximum waiting time for credentials expiry is 15
 minutes. Alternatively, ask the environment owner to re-enable or disable the managed
 temporary credentials. After the credentials are re-enabled or disabled, collaborators
 can immediately access the environment. By toggling the state of managed credentials to
 ENABLED or DISABLED, the environment owner ensures that the credentials don't remain in
 an intermediate state. An intermediate stat can prevent collaborators from accessing the
 environment.


###### Note

Suppose that the environment owner and collaborator belong to the same
 AWS account. Then, the collaborator can identify the environment owner to contact
 by reviewing the card for an environment in the **Your
 environments** page on the console. The environment owner is also listed
 in the **Environment details** page.


### Environment deletion error: "One or
 more environments failed to delete"


**Issue:** When you attempt to delete one or more
 environments in the AWS Cloud9 console, a message is displayed that reads "one or more
 environments failed to delete," and at least one of the environments isn't deleted.


**Possible cause:** AWS CloudFormation might have a problem
 deleting one or more of the environments. AWS Cloud9 relies on AWS CloudFormation to create and delete
 environments.


**Recommended solution:** Try using AWS CloudFormation to delete each
 of the undeleted environments.


1. Open the AWS CloudFormation console at
 [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the AWS navigation bar, choose the AWS Region for the
 environment.
3. In the list of AWS CloudFormation stacks, select the entry where **Stack
 name** contains the undeleted environment name and
 **Status** is **DELETE\_FAILED**. For example,
 if the environment name is `my-demo-environment`, choose the stack
 that begins with the name **aws-cloud9-my-demo-environment**.
 (Choose the box or option next to the environment name, not the environment name
 itself.)
4. Choose **Actions, Delete Stack**.
5. If prompted, choose **Yes, Delete**.

The process of deleting a stack might take a few minutes.


If the stack disappears from the list, the environment is now deleted.


If the stack still displays **DELETE\_FAILED** after a few minutes,
 the environment still isn't deleted. You can try to manually delete each of the failed stack's
 resources.


###### Note

Manually deleting a failed stack's resources doesn't remove the stack itself from
 your AWS account.


To manually delete these resources, do the following. In the AWS CloudFormation console, choose
 the failed stack, and then select the **Resources** section. Go to the
 console in AWS for each resource in this list, and then use that console to delete the
 resource.


### Changing timeout time for an environment
 in AWS Cloud9 IDE



**Issue:** Users want to update the timeout time for Amazon EC2
 environments.



**Cause:** The default timeout time is 30 minutes. This may
 be too short for some users.



**Recommended solution:**



1. Open the environment that you want to configure.
2. In the **AWS Cloud9 IDE**, on the menu bar, choose
 **AWS Cloud9**
**Preferences**.
3. In the **Preferences** window scroll to the **Amazon EC2
 instance** section.
4. Select the timeout value from the list available and update.

### Error running SAM applications
 locally in AWS Toolkit because the AWS Cloud9 environment doesn't have enough disk
 space


**Issue:** Error occurs when you use the AWS Toolkit to
 run AWS SAM CLI commands for applications defined by SAM templates.


**Possible causes:** When you run and debug serverless
 applications locally with the AWS Toolkit, AWS SAM uses Docker images.
 These images provide a runtime environment and build tools that emulate the Lambda
 environment that you're planning to deploy to.


However, if your environment's lacks enough disk space, the Docker image
 providing these features can't build and your local SAM application fails to run. If
 this occurs, you might receive an error in the **Output** tab similar
 to the following.



```
Error: Could not find amazon/aws-sam-cli-emulation-image-python3.7:rapid-1.18.1 image locally and failed to pull it from docker.
```

This error relates to a SAM application that's built using the Python runtime. You
 might receive a slightly different message, depending on the runtime that you chose for
 your application.


**Recommended solutions:** Free up disk space in your
 environment so the Docker image can build. Remove any unused
 Docker images by running the following command in the IDE's
 terminal.



```
docker image prune -a
```

If you're repeatedly having issues with SAM CLI commands because of disk-space
 restrictions, switch to a development environment uses a different [instance type](create-environment-main.md#create-environment-console "create-environment-main.md#create-environment-console"). 


([back to top](troubleshooting.md "troubleshooting.md"))


### Can't load IDE using earlier versions of
 Microsoft Edge browser


**Issue:**
`HTTP403: FORBIDDEN` error is returned when trying to load AWS Cloud9 IDE using
 the Microsoft Edge web browser.


**Possible causes:** The AWS Cloud9 IDE doesn't support
 certain older versions of Microsoft Edge.


**Recommended solutions:** To update the browser, choose
 the ellipsis (...) button in the Microsoft Edge toolbar. From the menu,
 choose **Settings** and then choose **About Microsoft
 Edge**. If an update is required, it's automatically downloaded
 and installed.


([back to top](troubleshooting.md "troubleshooting.md"))


### Can't create the sub-folder structure **/home/ec2-user/environment/home/ec2-user/environment** in the
 AWS Cloud9 IDE File Explorer.


**Issue:** When you create the sub-folder structure
 **/home/ec2-user/environment/home/ec2-user/environment**
 in the AWS Cloud9 IDE File Explorer, you get an error message stating that it is not possible
 to open this directory. 


**Possible causes:** It's not currently possible to
 create a sub-folder structure **/home/ec2-user/environment** within a folder of the same name using the
 File System of the AWS Cloud9 IDE. You will not be able to access any files within this
 directory from the AWS Cloud9 IDE File Explorer, but you will be able access them using the
 command line. This issue only affects the file path **/home/ec2-user/environment/home/ec2-user/environment**, file paths such as
 **/test/home/ec2-user/environment** and **/home/ec2-user/environment/test** should work. This is a known
 issue and only affects the AWS Cloud9 IDE File Explorer.


**Recommended solutions**: Use a different file name and
 structure.


([back to top](troubleshooting.md "troubleshooting.md"))


### Can't create the sub-folder structure
 **/projects/projects** within the File Explorer of
 the AWS Cloud9 IDE for CodeCatalyst.


**Issue:** When you create the sub-folder structure
 **/projects/projects** in the AWS Cloud9 IDE File Explorer for
 CodeCatalyst, you get an error message stating that it is not possible to open this directory. 


**Possible causes:** It's not currently possible to
 create a sub-folder structure **/projects** within a folder
 of the same name using the File Explorer of the AWS Cloud9 IDE for CodeCatalyst. You will not be
 able to access any files within this directory from the AWS Cloud9 IDE File Explorer, but you
 will be able access them using the command line. This issue only affects the file path
 **/projects/projects**, file paths such as **/test/projects** and **/projects/test** should work. This is a known issue and only affects the
 AWS Cloud9 IDE File Explorer for CodeCatalyst.


**Recommended solutions**: Use a different file name and
 structure.


([back to top](troubleshooting.md "troubleshooting.md"))


### Can't interact with the terminal window in AWS Cloud9
 because of `tmux` session errors


**Issue:** When you attempt to launch a new terminal
 window in AWS Cloud9, the expected command line interface isn't available. There's no command
 prompt and you can't enter text. Error messages such as `tmux: need UTF-8 locale
 (LC_CTYPE)` and `invalid LC_ALL, LC_CTYPE or LANG` are
 returned.


**Possible causes:** An unresponsive terminal might be
 caused by a tmux error. AWS Cloud9 uses the [tmux](https://en.wikipedia.org/wiki/Tmux "https://en.wikipedia.org/wiki/Tmux") utility. This way, information that's displayed in the terminal is
 persisted even when the page reloads or you reconnect to your development
 environment.


In a `tmux` session, what's displayed in the terminal window is handled by
 a client. The client communicates to a server that can manage multiple sessions. The
 server and client communicate through a socket located in the `tmp`
 folder. If the `tmp` folder is missing from your development
 environment or overly restrictive permissions are applied to it, `tmux`
 sessions can't run. If this occurs, the terminal window in the IDE becomes
 unresponsive.


**Recommended solutions**: If `tmux` errors
 are preventing you from interacting with the terminal window, use an alternative way to
 create a `tmp` folder with the right permissions. That way,
 `tmux` sessions can run. One solution is to export `LC_CTYPE`
 in `.bash_profile` or in the `.bashrc` file. Another
 recommended solution is to use AWS Systems Manager to set up a host management configuration. This
 allows access to the relevant instance through the Amazon EC2 console.


**Setting up host management**


1. First, in the AWS Cloud9 console, find the name of your environment's instance. You
 can do so by choosing the relevant panel in the **Your
 environments** page and choosing **View details**.
 In the **Environment details** page, choose **Go to
 Instance**. In the Amazon EC2 console, confirm the name of the instance
 that you need to access.
2. Now go to the AWS Systems Manager console, and in the navigation pane, choose
 **Quick Setup**.
3. In the **Quick Setup** page, choose
 **Create**.
4. For **Configuration types**, go to **Host
 Management** and choose **Create**.
5. For **Customize Host Management configuration options**, in
 the **Targets** section, choose **Manual**.
6. Select the EC2 instance that you want to access and then choose
 **Create**.

**Connecting to the instance and running
 commands**


###### Note

The following steps are for the new EC2 console.


1. In the Amazon EC2 console, in the navigation pane, choose
 **Instances** and select the instance that you want to connect
 to.
2. Choose **Connect**.


If **Connect** isn't activated, you might need to start the
 instance first.
3. In the **Connect to your instance** pane, for
 **Connection method**, choose **Session
 Manager** and then choose **Connect**.
4. In the terminal session window that appears, enter the following commands.
 These commands create the `tmp` folder with the right
 permissions so that the tmux socket is available.



```
sudo mkdir /tmp
sudo chmod 777 /tmp
sudo rmdir /tmp/tmux-*                   
```

([back to top](troubleshooting.md "troubleshooting.md"))


## Amazon EC2


The following section outlines troubleshooting issues related to Amazon EC2.


### Amazon EC2 instances aren't automatically
 updated



**Issue:** Recent system updates are not automatically
 applied to an Amazon EC2 instance that connects to an AWS Cloud9 development environment.



**Cause:** Automatically applying recent system updates
 could cause your code or the Amazon EC2 instance to behave in unexpected ways, without your
 prior knowledge or approval.



**Recommended solutions:**



Apply system updates to the Amazon EC2 instance on a regular basis by following the
 instructions in [Updating Instance
 Software](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-updates.html "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-updates.html") in the *Amazon EC2 User Guide*.


To run commands on the instance, you can use a terminal session in the AWS Cloud9 IDE from
 the environment that is connected to the instance.


Alternatively, you can use an SSH remote access utility such as **ssh** or PuTTY to connect to the instance. To do this, from
 your local computer, use an SSH key pair creation utility such as **ssh-keygen** or PuTTYgen. Use the AWS Cloud9 IDE from the environment
 that's connected to the instance to store the generated public key on the instance. Then
 use the SSH remote access utility along with the generated private key to access the
 instance. For more information, see your utility's documentation.


### AWS CLI or AWS-shell error: "The
 security token included in the request is invalid" in an EC2 environment



**Issue:** When you try to use the AWS Command Line Interface (AWS CLI) or the
 AWS-shell to run a command in the AWS Cloud9 IDE for an EC2 environment, an error displays: "The
 security token included in the request is invalid."



**Cause:** An invalid security token can result if you have
 AWS managed temporary credentials enabled and one of the following occurred: 



* You tried to run a command that's not allowed by AWS managed temporary credentials. For a list of
 allowed commands, see [Actions supported by AWS managed temporary credentials](security-iam.md#auth-and-access-control-temporary-managed-credentials-supported "security-iam.md#auth-and-access-control-temporary-managed-credentials-supported").
* The AWS managed temporary credentials automatically expired after 15 minutes.
* The AWS managed temporary credentials for a shared environment were deactivated because a new member was
 added by someone other than the environment owner.


**Recommended solutions:**




* Run only those commands that are allowed by AWS managed temporary credentials. If you need to run
 a command that's not allowed by AWS managed temporary credentials, configure the AWS CLI or AWS-shell
 in the environment with a set of permanent credentials. This removes this limitation.
 For instructions, see [Create and store permanent access credentials
 in an Environment](credentials.md#credentials-permanent-create "credentials.md#credentials-permanent-create").
* For deactivated or expired credentials, ensure that the environment owner opens the
 environment so that AWS Cloud9 can refresh temporary credentials in the environment. For more
 information, see [Controlling access to
 AWS managed temporary credentials](security-iam.md#temporary-managed-credentials-control "security-iam.md#temporary-managed-credentials-control").

### Can't connect to EC2 environment because VPC's IP addresses are
 used by Docker


**Issue:** For an EC2 environment, if you launch the EC2
 instance into an Amazon VPC that uses the IPv4 Classless Inter-Domain Routing (CIDR) block
 `172.17.0.0/16`, the connection might stall when you attempt to open that
 environment.


**Cause:** Docker uses a link layer device called a
 bridge network that enables containers that are connected to the same bridge network to
 communicate. AWS Cloud9 creates containers that use a default bridge for container
 communication. The default bridge typically uses the `172.17.0.0/16` subnet
 for container networking.


If the VPC subnet for your environment's instance uses the same address range that's
 already used by Docker, an IP address conflict might occur. So, when
 AWS Cloud9 tries to connect to its instance, that connection is routed by the gateway route
 table to the Docker bridge. This prevents AWS Cloud9 from connecting to the
 EC2 instance that backs the development environment.


**Recommended solution:**  To resolve an IP address
 conflict that's caused by Amazon VPC and Docker using the same IPv4 CIDR
 address block, configure a new VPC for the instance backing your EC2 environment. For this new
 VPC, configure a CIDR block that's different from `172.17.0.0/16`. (You can't
 change the IP address range of an existing VPC or subnet.) 


For configuration information, see [VPC and subnet sizing](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html#VPC_Sizing "https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html#VPC_Sizing") in the
 Amazon VPC User Guide. 


### Can't create the sub-folder structure **/home/ec2-user/environment/home/ec2-user/environment** in the
 AWS Cloud9 IDE File Explorer.


**Issue:** When you create the sub-folder structure
 **/home/ec2-user/environment/home/ec2-user/environment**
 in the AWS Cloud9 IDE File Explorer, you get an error message stating that it is not possible
 to open this directory. 


**Possible causes:** It's not currently possible to
 create a sub-folder structure **/home/ec2-user/environment** within a folder of the same name using the
 File System of the AWS Cloud9 IDE. You will not be able to access any files within this
 directory from the AWS Cloud9 IDE File Explorer, but you will be able access them using the
 command line. This issue only affects the file path **/home/ec2-user/environment/home/ec2-user/environment**, file paths such as
 **/test/home/ec2-user/environment** and **/home/ec2-user/environment/test** should work. This is a known
 issue and only affects the AWS Cloud9 IDE File Explorer.


**Recommended solutions**: Use a different file name and
 structure.


### Can't launch AWS Cloud9 from console when an AWS License Manager
 license configuration is associated with Amazon EC2 instances


**Issue:** When you try to launch an AWS Cloud9 EC2
 environment from the console, an error message `unable to access your
 environment` is returned. 


**Possible causes:** AWS License Manager streamlines the
 management of software vendor licenses across the AWS Cloud. When setting up License Manager,
 you create license configurations, which are sets of licensing rules based on the terms
 of your enterprise agreements. These license configurations can be attached to a
 mechanism, such as an Amazon Machine Image (AMI) or AWS CloudFormation. You can use one of these
 mechanisms to launch EC2 instances.


Older versions of **AWSCloud9ServiceRolePolicy** for the
 AWSServiceRoleForAWSCloud9 service-linked role (SLR) currently don't include the
 `license-configuration` resource condition. Because of this, AWS Cloud9 isn't
 allowed to start and stop its instance. So, AWS Cloud9 is denied access to its Amazon EC2
 instance, and an error is returned.


**Recommended solutions**: If you can't access an
 existing AWS Cloud9 environment and use License Manager, replace the old **AWSCloud9ServiceRolePolicy** service-linked role with the [version of the SLR](using-service-linked-roles.md#service-linked-role-permissions "using-service-linked-roles.md#service-linked-role-permissions") that explicitly
 allows EC2 actions when a `license-configuration` applies to the instance.
 You can replace the old role simply by deleting it. The updated role is then created
 automatically.


### Can't run some commands or scripts in an
 EC2 environment



**Issue:** After you open an AWS Cloud9 EC2 development environment, you can't
 install some types of packages, run commands such as `yum` or
 `apt`, or run scripts containing commands that typically work with other
 Linux operating systems.



**Cause:** The Amazon EC2 instances that AWS Cloud9 uses for an
 EC2 environment rely on either Amazon Linux (which is based on Red Hat Enterprise Linux (RHEL)) or
 Ubuntu Server.



**Solution:** If you install or manage packages or run
 commands or scripts in the IDE for an EC2 environment, ensure they are compatible with either
 RHEL (for Amazon Linux) or Ubuntu Server, depending on the instance for that environment.


### Error message reporting "Instance profile
 AWSCloud9SSMInstanceProfile does not exist in account" when creating EC2 environment using
 AWS CloudFormation


**Issue:** When using the [AWS::Cloud9::EnvironmentEC2](../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.md") AWS CloudFormation resource to create an EC2 environment, users
 receive an error message that **`Instance profile AWSCloud9SSMInstanceProfile
 does not exist in account.`**



**Cause:** When creating a no-ingress EC2 environment, you must
 create the service role `AWSCloud9SSMAccessRole` and the instance profile
 `AWSCloud9SSMInstanceProfile`. These IAM resources enable Systems Manager to
 manage the EC2 instance that backs your development environment. 


If you create a no-ingress environment with the console,
 `AWSCloud9SSMAccessRole` and `AWSCloud9SSMInstanceProfile` are
 created automatically. But when using AWS CloudFormation or AWS CLI to create your first no-ingress
 environment, you must create these IAM resources manually. 


**Recommended solution:**  For information about editing
 your AWS CloudFormation template and updating IAM permissions, see [Using AWS CloudFormation to create no-ingress
 EC2 environments](ec2-ssm.md#cfn-role-and-permissions "ec2-ssm.md#cfn-role-and-permissions")


### Error message reporting "not authorized to
 `perform: ssm:StartSession` on resource" when creating EC2 environment using
 AWS CloudFormation


**Issue:** When using the [AWS::Cloud9::EnvironmentEC2](../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.md") AWS CloudFormation resource to create an EC2 environment, users
 receive an `AccessDeniedException` and are informed that they're "not
 authorized to perform: `ssm:StartSession` on resource."


**Cause:** The user lacks the permission to call the
 `StartSession` API that's required as part of the configuration for
 EC2 environments that use Systems Manager for no-ingress instances.


**Recommended solution:**  For information about editing
 your AWS CloudFormation template and updating IAM permissions, see [Using AWS CloudFormation to create no-ingress
 EC2 environments](ec2-ssm.md#cfn-role-and-permissions "ec2-ssm.md#cfn-role-and-permissions").


### Error message reporting no authorization "to
 perform: `iam:GetInstanceProfile` on resource: instance profile
 `AWSCloud9SSMInstanceProfile`" when creating EC2 environment using
 AWS CLI


**Issue:** When using the [AWS CLI](tutorials-basic.md#tutorial-create-environment "tutorials-basic.md#tutorial-create-environment") to create an EC2 environment, users
 receive an `AccessDeniedException` and are informed that their AWS Cloud9
 environment isn't authorized "to perform iam:GetInstanceProfile on resource: instance
 profile `AWSCloud9SSMInstanceProfile`."


**Cause:** AWS Cloud9 lacks the permission to call the
 `StartSession` API that's required as part of the configuration for
 EC2 environments that use Systems Manager for no-ingress instances.


**Recommended solution:**  For information about adding
 the required `AWSCloud9SSMAccessRole` service role and
 `AWSCloud9SSMInstanceProfile` to your AWS Cloud9 environment, see [Managing instance profiles for Systems Manager
 with the AWS CLI](ec2-ssm.md#aws-cli-instance-profiles "ec2-ssm.md#aws-cli-instance-profiles").


### Failure to create environment when default
 encryption is applied to Amazon EBS volumes


**Issue:**
`Failed to create environments. The development environment '[environment-ID]'
 failed to create` error is returned when trying to create an Amazon EC2
 environment.


**Possible causes:** If your AWS Cloud9 IDE uses Amazon EBS
 volumes that by default are encrypted, the AWS Identity and Access Management service-linked role for AWS Cloud9
 requires access to the AWS KMS keys for these EBS volumes. If access isn't provided,
 the AWS Cloud9 IDE might fail to launch, and it might be difficult to debug the
 problem.


**Recommended solutions**: To provide access, add the
 service-linked role for AWS Cloud9, `AWSServiceRoleForAWSCloud9`, to the
 customer managed key that's used by your Amazon EBS volumes.


 For more information about this task, see [Create an AWS Cloud9 that uses Amazon EBS volumes with default encryption](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-an-aws-cloud9-ide-that-uses-amazon-ebs-volumes-with-default-encryption.html "https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-an-aws-cloud9-ide-that-uses-amazon-ebs-volumes-with-default-encryption.html") in
 *AWS Prescriptive Guidance Patterns*. 


### VPC error for EC2-Classic accounts: "Unable to
 access your environment"


**Issue:** EC2-Classic was introduced in the original
 release of Amazon EC2. If you use an AWS account that was set up before December 4, 2013,
 this error might occur if you don't configure an Amazon VPC and subnet when you create an
 AWS Cloud9 EC2 development environment.


If you accept the default VPC settings, the Amazon EC2 instance is launched into the
 EC2-Classic network. The instance is not launched into a subnet of the default VPC. The
 following message is displayed when the environment fails to create: 




**`Environment Error`**


**`Unable to access your environment`**


**`The environment creation failed with the error: The following resource(s)
 failed to create: [Instance]. . Rollback requested by user..`**


You can confirm that the error is caused by the EC2 instance not being in the default
 VPC. Use AWS CloudFormation to view the stack event history for the development environment.


1. Open the AWS CloudFormation console. For more information, see [Logging in to the AWS CloudFormation
 console.](../../../AWSCloudFormation/latest/UserGuide/cfn-console-login.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-login.md")
2. In the AWS CloudFormation console, choose **Stacks**.
3. On the **Stacks** page, choose the name of the
 development environment that failed to create.
4. On the **Stack details** page, choose the
 **Events** tab and check for the following
 entry:


**`Status: CREATE_FAILED`**


**`Status reason: The AssociatePublicIpAddress parameter is only
 supported by VPC launches. [...]`**

**Cause:** An AWS Cloud9 development environment must be associated with an
 Amazon VPC that meets specific VPC requirements. For accounts with EC2-Classic enabled,
 accepting the default network settings when [creating
 an EC2 environment](create-environment.md "create-environment.md") means that the required EC2 instance isn't launched into the VPC.
 Instead, the instance is launched into the EC2-Classic network.


**Recommended solution:** With an EC2-Classic account,
 you must select a VPC and subnet when [creating an
 EC2 environment](create-environment.md "create-environment.md"). On the **Configure settings** page, in
 the **Network settings (advanced)** section, select the VPC
 and subnet that you can launch your EC2 instance into.


## Other AWS services


The following section outlines troubleshooting issues related to other AWS
 services.


### Can't create the sub-folder structure
 **/projects/projects** within the File Explorer of
 the AWS Cloud9 IDE for CodeCatalyst.


**Issue:** When you create the sub-folder structure
 **/projects/projects** in the AWS Cloud9 IDE File Explorer for
 CodeCatalyst, you get an error message stating that it is not possible to open this directory. 


**Possible causes:** It's not currently possible to
 create a sub-folder structure **/projects** within a folder
 of the same name using the File Explorer of the AWS Cloud9 IDE for CodeCatalyst. You will not be
 able to access any files within this directory from the AWS Cloud9 IDE File Explorer, but you
 will be able access them using the command line. This issue only affects the file path
 **/projects/projects**, file paths such as **/test/projects** and **/projects/test** should work. This is a known issue and only affects the
 AWS Cloud9 IDE File Explorer for CodeCatalyst.


**Recommended solutions**: Use a different file name and
 structure.


### Can't display your running application
 outside of the IDE



**Issue:** When you or others try to display your running
 application in a web browser tab outside of the IDE, that web browser tab displays an
 error, or the tab is blank.



**Possible causes:**




* The application isn't running in the IDE.
* The application is running with an IP of `127.0.0.1` or
 `localhost`.
* The application is running in an AWS Cloud9 EC2 development environment. Moreover, one or more
 security groups that are associated with the corresponding Amazon EC2 instance don't
 allow inbound traffic over the protocols, ports, or IP addresses that the
 application requires.
* The application is running in an AWS Cloud9 SSH development environment for an AWS cloud compute
 instance (for example, an Amazon EC2 instance). Moreover, the network ACL for the
 subnet in the virtual private cloud (VPC) that's associated with the corresponding
 instance doesn't allow inbound traffic over the protocols, ports, or IP addresses
 that the application requires.
* The URL is incorrect.
* The URL in the application preview tab is being requested instead of the
 instance's public IP address.
* You're trying to go to an address that contains an IP of `127.0.0.1`
 or `localhost`. These IPs attempts to access resources on your local
 computer instead of resources in the environment.
* The instance's public IP address has changed.
* The web request originates from a virtual private network (VPN) that blocks
 traffic over the protocols, ports, or IP addresses that the application
 requires.
* The application is running in an SSH environment. However, your server or the
 associated network doesn't allow traffic over the protocols, ports, or IP
 addresses that the application requires.


**Recommended solutions:**




* Ensure that the application is running in the IDE.
* Ensure that the application isn't running with an IP of `127.0.0.1`
 or `localhost`. For examples in Node.js and Python, see [Run an application](app-preview.md#app-preview-run-app "app-preview.md#app-preview-run-app").
* Suppose that the application is running on an AWS cloud compute instance (for
 example, an Amazon EC2 instance). Then, ensure all the security groups that are
 associated with the corresponding instance allow inbound traffic over the
 protocols, ports, and IP addresses that the application requires. For
 instructions, see [Step 2: Set up the security group for
 the instance](app-preview-share.md#app-preview-share-security-group "app-preview-share.md#app-preview-share-security-group") in *Share a running
 application over the internet*. See also [Security Groups for Your
 VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html") in the *Amazon VPC User Guide*.
* Suppose that the application is running on an AWS cloud compute instance.
 Moreover, a network ACL exists for the subnet in the VPC that's associated with
 the corresponding instance. Then, ensure that network ACL allows inbound traffic
 over the protocols, ports, and IP addresses that the application requires. For
 instructions, see [Step 3: Set up the subnet for the
 instance](app-preview-share.md#app-preview-share-subnet "app-preview-share.md#app-preview-share-subnet") in *Share a running
 application over the internet*. See also [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html "https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html") in the
 *Amazon VPC User Guide*.
* Ensure that the requesting URL, including the protocol (and port, if it must be
 specified), is correct. For more information, see [Step 4: Share your running application's
 URL](app-preview-share.md#app-preview-share-url "app-preview-share.md#app-preview-share-url") in
 *Share a running application over the internet*.
* We don't recommend requesting a URL with the format
 `https://12a34567b8cd9012345ef67abcd890e1.vfs.cloud9.us-east-2.amazonaws.com/`
 (where `12a34567b8cd9012345ef67abcd890e1` is the ID that AWS Cloud9 assigns
 to the environment, and `us-east-2` is the ID of the AWS Region for the
 environment). This URL works only when the IDE for the environment is open and the
 application is running in the same web browser.
* Suppose that you're trying to go to an address that contains an IP of
 `127.0.0.1` or `localhost`. Try going to the correct
 non-local address for the running application instead. For more information, see
 [Share a running application over the internet](app-preview-share.md "app-preview-share.md").
* Suppose that the application is running on an AWS cloud compute instance.
 Determine whether the instance's public IP address has changed. The instance's
 public IP address might change anytime the instance restarts. To prevent this IP
 address from changing, you can allocate an Elastic IP address and assign it to the
 running instance. For more information, see [Step 4: Share your running application's
 URL](app-preview-share.md#app-preview-share-url "app-preview-share.md#app-preview-share-url") in *Share a running
 application over the internet*.
* If the web request originates from a VPN, ensure that VPN allows traffic over
 the protocols, ports, and IP addresses that the application requires. If you can't
 make changes to your VPN, see your network administrator. Or, make the web request
 from a different network if possible.
* Suppose that the application is running in an SSH environment for your own server.
 Ensure that your server and the associated network allow traffic over the
 protocols, ports, and IP addresses that the application requires. If you can't
 make changes to your server or the associated network, see your server or network
 administrator.
* Try running the application from a terminal in the environment by running the
 `curl` command, followed by the URL. If this command displays an
 error message, there might be some other issue that's not related to AWS Cloud9.

### Error when running AWS Toolkit: "Your environment is
 running out of inodes, please increase 'fs.inotify.max\_user\_watches' limit."


**Issue:** A file watcher utility that AWS Toolkit uses
 is approaching its current limit or quota of files it can watch.


**Cause:** AWS Toolkit uses a file watcher utility that
 monitors changes to files and directories. When the utility is nearly at its current
 quota of files that it can watch, a warning message appears.


**Recommended solution:**  To increase the maximum
 number of files that can be handled by file watcher, do the following: 


1. Start a terminal session by choosing **Window**,
 **New Terminal** on the menu bar.
2. Enter the following command.



```
sudo bash -c 'echo "fs.inotify.max_user_watches=524288" >> /etc/sysctl.conf' && sudo sysctl -p
```

### Lambda local function run error:
 Cannot install SAM Local



**Issue:** After you attempt to run the local version of an
 AWS Lambda function in the AWS Cloud9 IDE, a dialog box is displayed. The dialog box states
 that AWS Cloud9 is having trouble installing SAM Local. AWS Cloud9 needs SAM Local to run local
 versions of AWS Lambda functions in the IDE. Until SAM Local is installed, you can't
 run local versions of Lambda functions in the IDE.


**Cause:** AWS Cloud9 can't find SAM Local at the expected
 path in the environment, which is `~/.c9/bin/sam`. This is because SAM
 Local isn't already installed, or if it's installed, AWS Cloud9 can't find it at that
 location.



**Recommended solutions:** You can wait for AWS Cloud9 to try to
 finish installing SAM Local, or you can install it yourself.


To see how AWS Cloud9 is doing with attempting to install SAM Local, choose
 **Window, Installer** on the menu bar.


To install SAM Local yourself, follow the instructions in [Installing the AWS SAM CLI
 on Linux](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-linux.html "https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-linux.html") in the *AWS Serverless Application Model Developer Guide.*



### AWS Control Tower error when trying to create
 an Amazon EC2 environment using AWS Cloud9: "The environment creation failed with the error:
 The following hook(s) failed:[ControlTower::Guard::Hook]."


**Issue:** A compatibility issue exists with AWS Cloud9 and
 the AWS Control Tower proactive control *CT.EC2.PR.8*. If
 this control is enabled you cannot create an EC2 environment in AWS Cloud9.


**Cause:** AWS Control Tower is expecting the
 *AssociatePublicIpAddress* parameter to be in the
 AWS CloudFormation template. This parameter can't be added at this
 time.


**Recommended solution:**  Disable
 control*CT.EC2.PR.8* from the AWS Control Tower console
 and re-create the environment in AWS Cloud9. 


### Failure to create environment when default
 encryption is applied to Amazon EBS volumes


**Issue:**
`Failed to create environments. The development environment '[environment-ID]'
 failed to create` error is returned when trying to create an Amazon EC2
 environment.


**Possible causes:** If your AWS Cloud9 IDE uses Amazon EBS
 volumes that by default are encrypted, the AWS Identity and Access Management service-linked role for AWS Cloud9
 requires access to the AWS KMS keys for these EBS volumes. If access isn't provided,
 the AWS Cloud9 IDE might fail to launch, and it might be difficult to debug the
 problem.


**Recommended solutions**: To provide access, add the
 service-linked role for AWS Cloud9, `AWSServiceRoleForAWSCloud9`, to the
 customer managed key that's used by your Amazon EBS volumes.


 For more information about this task, see [Create an AWS Cloud9 that uses Amazon EBS volumes with default encryption](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-an-aws-cloud9-ide-that-uses-amazon-ebs-volumes-with-default-encryption.html "https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-an-aws-cloud9-ide-that-uses-amazon-ebs-volumes-with-default-encryption.html") in
 *AWS Prescriptive Guidance Patterns*. 


([back to top](troubleshooting.md "troubleshooting.md"))


### Can't launch AWS Cloud9 from console when an AWS License Manager
 license configuration is associated with Amazon EC2 instances


**Issue:** When you try to launch an AWS Cloud9 EC2
 environment from the console, an error message `unable to access your
 environment` is returned. 


**Possible causes:** AWS License Manager streamlines the
 management of software vendor licenses across the AWS Cloud. When setting up License Manager,
 you create license configurations, which are sets of licensing rules based on the terms
 of your enterprise agreements. These license configurations can be attached to a
 mechanism, such as an Amazon Machine Image (AMI) or AWS CloudFormation. You can use one of these
 mechanisms to launch EC2 instances.


Older versions of **AWSCloud9ServiceRolePolicy** for the
 AWSServiceRoleForAWSCloud9 service-linked role (SLR) currently don't include the
 `license-configuration` resource condition. Because of this, AWS Cloud9 isn't
 allowed to start and stop its instance. So, AWS Cloud9 is denied access to its Amazon EC2
 instance, and an error is returned.


**Recommended solutions**: If you can't access an
 existing AWS Cloud9 environment and use License Manager, replace the old **AWSCloud9ServiceRolePolicy** service-linked role with the [version of the SLR](using-service-linked-roles.md#service-linked-role-permissions "using-service-linked-roles.md#service-linked-role-permissions") that explicitly
 allows EC2 actions when a `license-configuration` applies to the instance.
 You can replace the old role simply by deleting it. The updated role is then created
 automatically.


([back to top](troubleshooting.md "troubleshooting.md"))


## Application preview


The following section outlines troubleshooting issues related to the application
 preview.


### After reloading an environment, you must
 refresh application preview



**Issue:** After you reload an environment that displays an
 application preview tab, the tab doesn't display the application preview.



**Cause:** Sometimes users write code that can run an
 infinite loop. Or their code can uses so much memory that the AWS Cloud9 IDE might pause or
 stop when the application preview is running. To keep this from happening, AWS Cloud9 doesn't
 reload application preview tabs whenever an environment is reloaded.



**Solution:** After you reload an environment that displays an
 application preview tab, to display the application preview, choose the **Click
 to load the page** button on the tab.


### Application preview or file preview notice:
 "Third-party cookies disabled"


**Issue:** When you attempt to preview [an application](app-preview.md "app-preview.md") or [a
 file](file-preview.md "file-preview.md"), a notice is displayed with the following message: "Preview functionality
 is disabled because your browser has third-party cookies disabled."


**Cause:** Third-party cookies aren't required to open
 the AWS Cloud9 IDE. However, you must enable third-party cookies to use the Application
 Preview or File Preview features.


**Solution:** Enable third-party cookies in your web
 browser, reload your IDE, and then try opening the preview again.



* **Apple Safari:**
[Manage cookies and website data in Safari](https://support.apple.com/guide/safari/manage-cookies-and-website-data-sfri11471/mac "https://support.apple.com/guide/safari/manage-cookies-and-website-data-sfri11471/mac") on the Apple Support
 website.
* **Google Chrome:** **Change
 your cookie settings** in [Clear, enable, and manage
 cookies in Chrome](https://support.google.com/chrome/answer/95647 "https://support.google.com/chrome/answer/95647") on the Google Chrome Help website.
* **Internet Explorer:** **Block
 or allow cookies** in [Delete and manage
 cookies](https://support.microsoft.com/en-us/help/17442 "https://support.microsoft.com/en-us/help/17442") on the Microsoft Support website.
* **Microsoft Edge:**
[Blocking third-party cookies](https://support.microsoft.com/en-us/help/4464209/issue-with-blocking-third-party-cookies "https://support.microsoft.com/en-us/help/4464209/issue-with-blocking-third-party-cookies") on the Microsoft Support website.
* **Mozilla Firefox:**
**Accept third party cookies** setting in [Enable and disable cookies that websites use to track your preferences](https://support.mozilla.org/kb/enable-and-disable-cookies-website-preferences "https://support.mozilla.org/kb/enable-and-disable-cookies-website-preferences")
 on the Mozilla Support website.
* **Other web browser:** see that web browser's
 documentation.

If your web browser allows this granularity, you can enable third-party cookies only
 for AWS Cloud9. To do this, specify the following domains, depending on the supported
 AWS Regions where you want to use AWS Cloud9.




| **AWS Region** | **Domains** |
| --- | --- |
| US East (N. Virginia) | `*.vfs.cloud9.us-east-1.amazonaws.com` `vfs.cloud9.us-east-1.amazonaws.com` |
| US East (Ohio) | `*.vfs.cloud9.us-east-2.amazonaws.com` `vfs.cloud9.us-east-2.amazonaws.com` |
| US West (N. California) | `*.vfs.cloud9.us-west-1.amazonaws.com` `vfs.cloud9.us-west-1.amazonaws.com` |
| US West (Oregon) | `*.vfs.cloud9.us-west-2.amazonaws.com` `vfs.cloud9.us-west-2.amazonaws.com` |
| Africa (Cape Town) | `*.vfs.cloud9.af-south-1.amazonaws.com` `vfs.cloud9.af-south-1.amazonaws.com` |
| Asia Pacific (Hong Kong) | `*.vfs.cloud9.ap-east-1.amazonaws.com` `vfs.cloud9.ap-east-1.amazonaws.com` |
| Asia Pacific (Mumbai) | `*.vfs.cloud9.ap-south-1.amazonaws.com` `vfs.cloud9.ap-south-1.amazonaws.com` |
| Asia Pacific (Osaka) | `*.vfs.cloud9.ap-northeast-3.amazonaws.com` `vfs.cloud9.ap-northeast-3.amazonaws.com` |
| Asia Pacific (Seoul) | `*.vfs.cloud9.ap-northeast-2.amazonaws.com` `vfs.cloud9.ap-northeast-2.amazonaws.com` |
| Asia Pacific (Singapore) | `*.vfs.cloud9.ap-southeast-1.amazonaws.com` `vfs.cloud9.ap-southeast-1.amazonaws.com` |
| Asia Pacific (Sydney) | `*.vfs.cloud9.ap-southeast-2.amazonaws.com` `vfs.cloud9.ap-southeast-2.amazonaws.com` |
| Asia Pacific (Tokyo) | `*.vfs.cloud9.ap-northeast-1.amazonaws.com` `vfs.cloud9.ap-northeast-1.amazonaws.com` |
| Canada (Central) | `*.vfs.cloud9.ca-central-1.amazonaws.com` `vfs.cloud9.ca-central-1.amazonaws.com` |
| Europe (Frankfurt) | `*.vfs.cloud9.eu-central-1.amazonaws.com` `vfs.cloud9.eu-central-1.amazonaws.com` |
| Europe (Ireland) | `*.vfs.cloud9.eu-west-1.amazonaws.com` `vfs.cloud9.eu-west-1.amazonaws.com` |
| Europe (London) | `*.vfs.cloud9.eu-west-2.amazonaws.com` `vfs.cloud9.eu-west-2.amazonaws.com` |
| Europe (Milan) | `*.vfs.cloud9.eu-south-1.amazonaws.com` `vfs.cloud9.eu-south-1.amazonaws.com` |
| Europe (Paris) | `*.vfs.cloud9.eu-west-3.amazonaws.com` `vfs.cloud9.eu-west-3.amazonaws.com` |
| Europe (Stockholm) | `*.vfs.cloud9.eu-north-1.amazonaws.com` `vfs.cloud9.eu-north-1.amazonaws.com` |
| Middle East (Bahrain) | `*.vfs.cloud9.me-south-1.amazonaws.com` `vfs.cloud9.me-south-1.amazonaws.com` |
| South America (São Paulo) | `*.vfs.cloud9.sa-east-1.amazonaws.com` `vfs.cloud9.sa-east-1.amazonaws.com` | ### Application preview tab displays an error or is blank **Issue:** On the menu bar in the IDE, when you choose **Preview, Preview Running Application** or **Tools, Preview, Preview Running Application** to try to display your application on a preview tab in the IDE, the tab displays an error, or the tab is blank. **Possible causes:** <br>• Your application isn't running in the IDE. <br>• Your application isn't running using HTTP. <br>• Your application is running over more than one port. <br>• Your application is running over a port other than `8080`, `8081`, or `8082`. <br>• Your application is running with an IP other than `127.0.0.1`, `localhost`, or `0.0.0.0`. <br>• The port (`8080`, `8081`, or `8082`) isn't specified in the URL on the preview tab. <br>• Your network blocks inbound traffic to port `8080`, `8081`, or `8082`. <br>• You're trying to go to an address that contains an IP of `127.0.0.1`, `localhost`, or `0.0.0.0`. By default, the AWS Cloud9 IDE attempts to go to your local computer. It doesn't attempt to go the instance or your own server that's connected to the environment. **Recommended solutions:** <br>• Ensure that the application is running in the IDE. <br>• Ensure that the application is running using HTTP. For examples in Node.js and Python, see [Run an application](app-preview.md#app-preview-run-app "app-preview.md#app-preview-run-app"). <br>• Ensure that the application is running over only one port. For examples in Node.js and Python, see [Run an application](app-preview.md#app-preview-run-app "app-preview.md#app-preview-run-app"). <br>• Ensure that the application is running over port `8080`, `8081`, or `8082`. For examples in Node.js and Python, see [Run an application](app-preview.md#app-preview-run-app "app-preview.md#app-preview-run-app"). <br>• Ensure that the application is running with an IP of `127.0.0.1`, `localhost`, or `0.0.0.0`. For examples in Node.js and Python, see [Run an application](app-preview.md#app-preview-run-app "app-preview.md#app-preview-run-app"). <br>• Add `:8080`, `:8081`, or `:8082` to the URL on the preview tab. <br>• Ensure that your network allows inbound traffic over ports `8080`, `8081`, or `8082`. If you can't make changes to your network, see your network administrator. <br>• If you're trying to go to an address that contains an IP of `127.0.0.1`, `localhost`, or `0.0.0.0`, try going to the following address instead: `https://12a34567b8cd9012345ef67abcd890e1.vfs.cloud9.us-east-2.amazonaws.com/`. In this address, `12a34567b8cd9012345ef67abcd890e1` is the ID that AWS Cloud9 assigns to the environment. `us-east-2` is the ID of the AWS Region for the environment. You can also try to go to this address outside of the IDE. However, this works only when the IDE for the environment is open and the application is running in the same web browser. <br>• After you're sure that all of the preceding conditions are met, try stopping the application and then starting it again. <br>• If you stopped the application and then started it again, try choosing **Preview, Preview Running Application** or **Tools, Preview, Preview Running Application** on the menu bar again. Or try choosing the **Refresh** button (the circular arrow) on the corresponding application preview tab, if the tab is already visible. ### Can't preview web content in the IDE because the connection to the site isn't secure **Issue:** When you try to access web content such as a WordPress site that's hosted in an AWS Cloud9 EC2 environment, the IDE preview window can't display it. **Possible causes:** By default, all web pages that you access in the application preview tab of the AWS Cloud9 IDE automatically use the HTTPS protocol. If a page's URI features the insecure `http` protocol, it's automatically replaced by `https`. And you can't access the insecure content by manually changing `https` back to `http`. **Recommended solutions**: Remove the insecure HTTP scripts or content from the web site that you're trying to preview in the IDE. Follow instructions for your web server or content management system for guidance on implementing HTTPS. ### Previewing a file returns a 499 error **Issue:** When you try to use the AWS Cloud9 IDE to preview a file that contains a `<script>` element that contains the `src` attribute and with the `type` attribute set to `module`, a 499 error occurs and the script doesn't run as expected. **Cause:** File preview fetch requests in the AWS Cloud9 IDE require cookies to be sent by the web browser to authenticate. By default, web browsers send cookies for regular script requests. They don't send cookies for module script requests unless you add the `crossorigin` attribute. **Solution:** Add the `crossorigin` attribute to the `<script>` element. For example, `<script type="module" src="index.js" crossorigin></script>`. Then, save the changed file, and try to preview it again. ## Performance The following section outlines troubleshooting issues related to performance. ### AWS Cloud9 IDE freezing for a significant amount of time **Issue:** During start-up, and when performing a refresh, the AWS Cloud9 IDE terminal freezes for a significant amount of time and becomes unusable. **Cause:** You might have a large amount of files in your environment that are being recursively watched by the file watching module of AWS Cloud9. **Recommended solutions:** You can decrease the file watching depth (the minimum value is 1) and consider adding large folders or folders not related to the source code (build outputs/artifacts, 3rd party packages) to the ignored patterns. To do this navigate to *Preferences > User Settings > File Watching*. Be aware that this will cause CodeLenses in AWS Toolkit to not work correctly. Another possible solution is to consider ignoring large files and folders that aren't related to the source code by decreasing the *Maximum number of files to search*. To do this navigate to *Preferences > Project Settings > Find in Files*. Be aware that this will cause folders that are ignored to not show up in a file search. ### Console warning: "Switching to the minimal code completion engine..." **Issue:** When working in the AWS Cloud9 console (for example, when opening the IDE or refreshing the IDE's web page), you see this message: "One or more sessions or collaborators are active on this environment. Switching to the minimal code completion engine to conserve memory." In correlation with this message, the code-completion behavior might be slow or intermittent. **Cause:** Running the code-completion engine takes memory and CPU cycles from the environment. Additionally, a separate code-completion engine is required for each collaborator and each additional session. To avoid using too many resources, especially on small instance sizes such as t2.nano and t2.micro, AWS Cloud9 switches to the minimal code-completion engine. **Recommended solution:** If you plan to collaborate often and for long periods of time, choose a larger Amazon EC2 instance when creating your EC2 environment. Or, alternatively, connect your SSH environment to an instance with more capacity. ###### Note Choosing a larger Amazon EC2 instance might cause your AWS account to incur additional charges. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/"). ### IDE warning: "This environment is running low on memory" or "This environment has high CPU load" **Issue:** While the IDE is running, you see a message that contains the phrase "this environment is running low on memory" or "this environment has high CPU load." **Cause:** The IDE might not have enough compute resources available to continue running without delays or hangs. **Recommended solutions:** <br>• Stop one or more running processes to free up available memory. To do this, on the menu bar in the IDE for the environment, choose **Tools, Process List**. For each process you want to stop, choose the process, and then choose **Force Kill**. <br>• Create a swap file in the environment. A *swap file* is a file in the environment that the operating system can use as virtual memory. To confirm that the environment is currently using swap memory, run the **`top`** command in a terminal session in the environment. If swap memory is being used, the output displays non-zero `Swap` memory statistics (for example, `Swap: 499996k total, 1280k used, 498716 free, 110672k cached`). To stop showing real-time memory information, press `Ctrl + C`. To create a swap file, run a command such as the following in the environment. ``` sudo fallocate --length 512MB /var/swapfile && sudo chmod 600 /var/swapfile && sudo mkswap /var/swapfile && echo '/var/swapfile swap swap defaults 0 0' | sudo tee -a /etc/fstab > /dev/null ``` The preceding command does the following: 1. Creates a 512 MB file that's named `swapfile` in the `/var` directory. 2. Changes access permissions for the `swapfile` file to read-write for the owner only. 3. Sets up the `swapfile` file as a swap file. 4. Writes information to the `/etc/fstab file`. This makes this swap file available whenever the system reboots. After you run the preceding command, to make this swap file available immediately, run the following command. ``` sudo swapon /var/swapfile ``` <br>• Move or resize the environment to an instance or server with more compute resources. To move or resize Amazon EC2 instances, see [Moving an AWS Cloud9 IDE from Amazon EBS volumes](move-environment.md "move-environment.md"). For other instance or server types, refer to your instance's or server's documentation. ### Unable to upload files in the AWS Cloud9 IDE **Issue:** Users are unable to upload a large file in the AWS Cloud9 IDE. These uploads are failing. **Cause:** AWS Cloud9 throttles the upload speed to the AWS Cloud9 IDE, and as a result the file upload request times out. **Recommended solution:** We recommend uploading the file to Amazon S3, and then use Amazon S3 to download the file to the environment with the CLI in the AWS Cloud9 IDE. For more information on uploading objects to Amazon S3, see [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html") in the *Amazon S3 User Guide*. ### Slow download speed in AWS Cloud9 IDE **Issue:** Users are dealing with slow download speeds when attempting to download files from AWS Cloud9 IDE. **Cause:** When you download files from the IDE to the local file system the speed of transfer will be limited to a speed of 0.1 megabyte/second. **Recommended solution:** To increase the speed of transferring files, use the CLI in your AWS Cloud9 IDE to upload files to Amazon S3 and then use Amazon S3 to download the files from there. ### Can't preview web content in the IDE because the connection to the site isn't secure **Issue:** When you try to access web content such as a WordPress site that's hosted in an AWS Cloud9 EC2 environment, the IDE preview window can't display it. **Possible causes:** By default, all web pages that you access in the application preview tab of the AWS Cloud9 IDE automatically use the HTTPS protocol. If a page's URI features the insecure `http` protocol, it's automatically replaced by `https`. And you can't access the insecure content by manually changing `https` back to `http`. **Recommended solutions**: Remove the insecure HTTP scripts or content from the web site that you're trying to preview in the IDE. Follow instructions for your web server or content management system for guidance on implementing HTTPS. ([back to top](troubleshooting.md "troubleshooting.md")) ## Third party applications and services The following section outlines troubleshooting issues related to third party applications and services. ### Can't interact with the terminal window in AWS Cloud9 because of `tmux` session errors **Issue:** When you attempt to launch a new terminal window in AWS Cloud9, the expected command line interface isn't available. There's no command prompt and you can't enter text. Error messages such as `tmux: need UTF-8 locale (LC_CTYPE)` and `invalid LC_ALL, LC_CTYPE or LANG` are returned. **Possible causes:** An unresponsive terminal might be caused by a tmux error. AWS Cloud9 uses the [tmux](https://en.wikipedia.org/wiki/Tmux "https://en.wikipedia.org/wiki/Tmux") utility. This way, information that's displayed in the terminal is persisted even when the page reloads or you reconnect to your development environment. In a `tmux` session, what's displayed in the terminal window is handled by a client. The client communicates to a server that can manage multiple sessions. The server and client communicate through a socket located in the `tmp` folder. If the `tmp` folder is missing from your development environment or overly restrictive permissions are applied to it, `tmux` sessions can't run. If this occurs, the terminal window in the IDE becomes unresponsive. **Recommended solutions**: If `tmux` errors are preventing you from interacting with the terminal window, use an alternative way to create a `tmp` folder with the right permissions. That way, `tmux` sessions can run. One solution is to export `LC_CTYPE` in `.bash_profile` or in the `.bashrc` file. Another recommended solution is to use AWS Systems Manager to set up a host management configuration. This allows access to the relevant instance through the Amazon EC2 console. **Setting up host management** 1. First, in the AWS Cloud9 console, find the name of your environment's instance. You can do so by choosing the relevant panel in the **Your environments** page and choosing **View details**. In the **Environment details** page, choose **Go to Instance**. In the Amazon EC2 console, confirm the name of the instance that you need to access. 2. Now go to the AWS Systems Manager console, and in the navigation pane, choose **Quick Setup**. 3. In the **Quick Setup** page, choose **Create**. 4. For **Configuration types**, go to **Host Management** and choose **Create**. 5. For **Customize Host Management configuration options**, in the **Targets** section, choose **Manual**. 6. Select the EC2 instance that you want to access and then choose **Create**. **Connecting to the instance and running commands** ###### Note The following steps are for the new EC2 console. 1. In the Amazon EC2 console, in the navigation pane, choose **Instances** and select the instance that you want to connect to. 2. Choose **Connect**. If **Connect** isn't activated, you might need to start the instance first. 3. In the **Connect to your instance** pane, for **Connection method**, choose **Session Manager** and then choose **Connect**. 4. In the terminal session window that appears, enter the following commands. These commands create the `tmp` folder with the right permissions so that the tmux socket is available. ``` sudo mkdir /tmp sudo chmod 777 /tmp sudo rmdir /tmp/tmux-* ``` ### Can't load IDE using earlier versions of Microsoft Edge browser **Issue:** `HTTP403: FORBIDDEN` error is returned when trying to load AWS Cloud9 IDE using the Microsoft Edge web browser. **Possible causes:** The AWS Cloud9 IDE doesn't support certain older versions of Microsoft Edge. **Recommended solutions:** To update the browser, choose the ellipsis (...) button in the Microsoft Edge toolbar. From the menu, choose **Settings** and then choose **About Microsoft Edge**. If an update is required, it's automatically downloaded and installed. ### Error with `gdb` when debugging C++ projects **Issue:** Error reported for `gdb` debugger when trying to debug C++ project in the IDE. **Possible causes:** Suppose that your AWS Cloud9 environment uses certain EC2 instance types (for example, `t3.small` or `m5.large`). Then, a debug error might occur when you try to run and debug a C++ project using the IDE's built-in runner. This error can happen because the version of the `gdb` (the GNU Project Debugger) that's pre-installed for your environment doesn't work on certain processor platforms. You might see the following error code. ``` GDB server terminated with code 1 ``` **Recommended solutions:** The problem with `gdb` not supporting certain processor platforms was fixed from version *3.0* onwards. Uninstall the older version of the debugger and upgrade to a newer version of `gdb`: 1. Remove the existing version of the debugger by running the following command in the AWS Cloud9 terminal. ``` sudo yum -y remove gdb ``` 2. Retrieve the archive for `gdb`, unpack it, and then navigate to the directory that contains the extracted files by running the following commands. ``` wget "http://ftp.gnu.org/gnu/gdb/gdb-8.3.tar.gz" tar xzf gdb-8.3.tar.gz cd gdb-8.3 ``` 3. Build the debugger by running the following command. To do this, copy and paste the following text as a single block and press **Return** to run `make`. ``` ./configure --prefix=/usr \ --with-system-readline \ --with-python=/usr/bin/python3 && make ``` 4. Install the debugger. ``` sudo make -C gdb install ``` 5. Confirm that the updated version of the debugger is installed. ``` gdb `--version` ``` ### Issues with PHP runner in AWS Cloud9 **Issue:** Users are unable to view any output in the PHP CLI runner terminal. **Cause:** CLI runner needs to be set to PHP and the debugger mode needs to be enabled. **Recommended solution:** Set the CLI runner to PHP and ensure the debugger mode is enabled. ### GLIBC errors related to Node.js **Issue:** Users are unable to run Node.js and are getting GLIBC errors. An example of these error messages is outlined below: ``` node: /lib64/libm.so.6: version `GLIBC_2.27' not found (required by node) node: /lib64/libc.so.6: version `GLIBC_2.28' not found (required by node) ``` **Cause:** Potentially it could be Node.js version issues related to the instance being used. **Recommended solution:** Refer to the [Step 1: Install required tools](sample-nodejs.md#sample-nodejs-install "sample-nodejs.md#sample-nodejs-install") section for information on how to install Node.js for AWS Cloud9.
