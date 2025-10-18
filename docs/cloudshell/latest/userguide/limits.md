# Service quotas and restrictions for AWS CloudShell

This page describes the Service quotas and restrictions that apply to the following
 areas:


* [Persistent storage](#persistent-storage-limitations "#persistent-storage-limitations")
* [Monthly usage](#shell-limits-per-month "#shell-limits-per-month")
* [Concurrent shells](#shell-limits-per-region "#shell-limits-per-region")
* [Command size](#character-limits "#character-limits")
* [Shell sessions](#session-lifecycle-limitations "#session-lifecycle-limitations")
* [VPC environments](#vpc-environments-limitations "#vpc-environments-limitations")
* [Network access and data
 transfer](#network-data-limitations "#network-data-limitations")
* [System files and page reloads](#system-files-page-refresh "#system-files-page-refresh")

## Persistent storage


With AWS CloudShell, you have persistent storage of 1 GB for each AWS Region at no cost.
 Persistent storage is located in your home directory ($HOME) and is private to you. Unlike
 ephemeral environment resources that are recycled after each shell session ends, data in
 your home directory persists between sessions.


###### Note

 CloudShell VPC environments do not have persistent storage. The $HOME directory
 is deleted when your VPC environment times out (after 20-30 minutes of inactivity), or
 when you delete your environment. 


If you stop using AWS CloudShell in an AWS Region, data is retained in the persistent
 storage of that Region for **120 days** after the end of your
 last session. After 120 days, unless you take action, your data is automatically deleted
 from the persistent storage of that Region. You can prevent removal by launching AWS CloudShell
 again in that AWS Region. For more information, see [Step 2: Select a Region, launch AWS CloudShell, and choose a shell](getting-started.md#launch-region-shell "getting-started.md#launch-region-shell").


###### Note

**Usage scenario**

Márcia has used AWS CloudShell to store files in her home directories in two AWS Regions:
 US East (N. Virginia) and Europe (Ireland). She then started using AWS CloudShell exclusively
 in Europe (Ireland) and stopped launching shell sessions in US East (N. Virginia).

Before the deadline for deleting data in US East (N. Virginia), Márcia decides to
 prevent her home directory from being recycled by launching AWS CloudShell and selecting the
 US East (N. Virginia) Region again. Because she has continually used Europe (Ireland) for
 shell sessions, her persistent storage in that Region isn't affected.


## Monthly usage


Each AWS Region
 in your AWS account has a monthly usage quota for AWS CloudShell. This quota combines the total
 time spent using CloudShell by all IAM principals in that
 Region.
 If you attempt to access
 CloudShell
 after you reached the monthly quota for that Region, a message displays to explain why the
 shell environment can't be started. 


**To request an increase using the Service Quotas
 console**


You can request an increase for your monthly usage quotas by opening the [Service Quotas console](https://eu-west-1.console.aws.amazon.com/servicequotas/home/services/cloudshell/quotas?region=eu-west-1 "https://eu-west-1.console.aws.amazon.com/servicequotas/home/services/cloudshell/quotas?region=eu-west-1"). For more information, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html "https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html") in the *Service Quotas User
 Guide*.


## Concurrent shells


You can run up to 10 shells at the same time in each AWS Region for your
 account.


**To request an increase using the Service Quotas
 console**


You can request an quota increase for each Region by opening the [Service Quotas console](https://eu-west-1.console.aws.amazon.com/servicequotas/home/services/cloudshell/quotas?region=eu-west-1 "https://eu-west-1.console.aws.amazon.com/servicequotas/home/services/cloudshell/quotas?region=eu-west-1"). For more information, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html "https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html") in the *Service Quotas
 User Guide*.


## Command size


The command size cannot exceed 65412 characters.


###### Note

If you intend to execute the command that exceeds 65412 characters, then create a
 script with the language of your choice, and then execute it from the command line
 interface. For more information about the range of pre-installed software that can be
 accessed from the command line interface, see [Pre-installed software](vm-specs.md#pre-installed-software "vm-specs.md#pre-installed-software").

To see as an example of how to create a script, and then execute it from the command
 line interface, see [Tutorial: Getting started with
 AWS CloudShell](getting-started.md "getting-started.md").


## Shell sessions



* **Inactive sessions**: AWS CloudShell is an interactive
 shell environment—if you don't interact with it using your keyboard or pointer
 for **20–30 minutes**, your shell session ends.
 Running processes don't count as interactions.


If you want to perform terminal-based tasks using an AWS service with more
 flexible timeouts, we recommend launching and [connecting to an Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html").
* **Long-running sessions**: A shell session that runs
 continuously for approximately 12 hours automatically end even if the user is
 regularly interacting with it during that period.

## VPC environments


You
 can only create up to two VPC environments per IAM
 principal.


###### Note

There is no charge to connect to your private VPC and access the resources
 within it. Data transfers within your Private VPC is included in your VPC billing,
 and data transfers between your VPCs through CloudShell are charged at the same
 cost as your current CloudShell.


## Network access and data transfer


The following restrictions apply to both the inbound and outbound traffic of your
 AWS CloudShell environment:



* **Outbound**: You can access the public
 internet.
* **Inbound**: You can’t access inbound ports. No
 public IP address is available.

###### Warning

With access to the public internet, there's a risk that certain users might export
 data from the AWS CloudShell environment. We recommend that IAM administrators manage the
 allow list of trusted AWS CloudShell users through IAM tools. For information about how
 specific users can be explicitly denied access, see [Managing allowable actions in AWS CloudShell using custom
 policies](sec-auth-with-identities.md#restricting-actions "sec-auth-with-identities.md#restricting-actions").


**Data transfer**: Uploading and downloading files to and
 from AWS CloudShell might be slow for large files. Alternatively, you can transfer files to your
 environment from an Amazon S3 bucket using the command line interface of the shell.


## Restrictions on system files and page
 reloads



* **System files**: If you incorrectly modify files
 that are required by the compute environment, you might experience problems when
 accessing or using the AWS CloudShell environment. If this occurs, you might need to [deleting your home directory](getting-started.md#delete-shell-session "getting-started.md#delete-shell-session") to regain
 access.
* **Reloading pages**: To reload the AWS CloudShell
 interface, use the refresh button in your browser instead of the default shortcut key
 sequence for your operating system.
