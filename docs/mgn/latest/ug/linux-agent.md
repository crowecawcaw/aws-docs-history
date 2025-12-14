NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Installing the AWS Replication Agent on Linux servers

Complete these steps to install the AWS Replication Agent on Linux source
servers.

1. Ensure that the necessary service roles have been created by clicking on the
   Reinitialize service permissions button on the AWS Application Migration Service console's replication settings page.
   You must have the permissions necessary to create IAM roles in order for this operation to
   succeed.
2. Download the agent installer with the wget command your Linux source server. This wget
   command downloads the Agent installer file - aws-replication-installer-init onto your
   server.

The Agent installer follows this format:
`https://aws-application-migration-service-<region>.s3.<region>.amazonaws.com/latest/linux/aws-replication-installer-init`
. Replace `<region>` with the AWS Region into which you are replicating.

This is an example of the full wget command for us-east-1:

`wget -O ./aws-replication-installer-init
 https://aws-application-migration-service-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/aws-replication-installer-init`

The command line indicates when the installer has been successfully downloaded.

###### Important

    * You need root privileges to run the Agent installer file on a Linux server.
     Alternatively, you can run the Agent Installer file with sudo permissions.
    * If you need to validate the installer hash, the correct hash can be found here:
     `https://aws-application-migration-service-hashes-<region>.s3.<region>.amazonaws.com/latest/linux/aws-replication-installer-init.sha512`
     (replace <region> with the AWS Region into which you are replicating. For example,
     us-east-1:


    https://aws-application-migration-service-hashes-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/aws-replication-installer-init.sha512
    * Replicating Amazon EC2 instances that were launched with marketplace product codes, is not
     supported.

###### Note

    * The Linux installer creates the "`aws-replication`" group and
     "`aws-replication`" user within that group. The Agent runs within the
     context of the newly created user. Agent installation attempts to add the user to
     "`sudoers`". Installation fails if the Agent is unable to add the newly
     created "`aws-replication`" user to "`sudoers`".
    * AWS Regions that are not opt-in also support the shorter installer path:
     `https://aws-application-migration-service-<region>.s3.amazonaws.com/latest/linux/aws-replication-installer-init`
     . Replace `<region>` with the AWS Region into which you are
     replicating.
    * You can generate a custom installation command through the **Add
     servers** prompt. [Learn more about the Add
     servers prompt](add-server-server-page.md#server-actions-main "add-server-server-page.md#server-actions-main").

This table contains the installer download link by supported
AWS Region:

| Region name               | Region identity | Download Link                                                                                                                                                                                                                                                                                                                |
| ------------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US East (Ohio)            | us-east-2       | **IPv4 -\*<br>• https://aws-application-migration-service-us-east-2.s3.us-east-2.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-us-east-2.s3.dualstack.us-east-2.amazonaws.com/latest/linux/aws-replication-installer-init                     |
| US East (N. Virginia)     | us-east-1       | **IPv4 -\*<br>• https://aws-application-migration-service-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-us-east-1.s3.dualstack.us-east-1.amazonaws.com/latest/linux/aws-replication-installer-init                     |
| US West (N. California)   | us-west-1       | **IPv4 -\*<br>• https://aws-application-migration-service-us-west-1.s3.us-west-1.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-us-west-1.s3.dualstack.us-west-1.amazonaws.com/latest/linux/aws-replication-installer-init                     |
| US West (Oregon)          | us-west-2       | **IPv4 -\*<br>• https://aws-application-migration-service-us-west-2.s3.us-west-2.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-us-west-2.s3.dualstack.us-west-2.amazonaws.com/latest/linux/aws-replication-installer-init                     |
| Africa (Cape Town)        | af-south-1      | **IPv4 -\*<br>• https://aws-application-migration-service-af-south-1.s3.af-south-1.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-af-south-1.s3.dualstack.af-south-1.amazonaws.com/latest/linux/aws-replication-installer-init                 |
| Asia Pacific (Thailand)   | ap-southeast-7  | **IPv4 -\*<br>• https://aws-application-migration-service-ap-southeast-7.s3.ap-southeast-7.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-ap-southeast-7.s3.dualstack.ap-southeast-7.amazonaws.com/latest/linux/aws-replication-installer-init |
| Asia Pacific (Hong Kong)  | ap-east-1       | **IPv4 -\*<br>• https://aws-application-migration-service-ap-east-1.s3.ap-east-1.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-ap-east-1.s3.dualstack.ap-east-1.amazonaws.com/latest/linux/aws-replication-installer-init                     |
| Asia Pacific (Jakarta)    | ap-southeast-3  | **IPv4 -\*<br>• https://aws-application-migration-service-ap-southeast-3.s3.ap-southeast-3.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-ap-southeast-3.s3.dualstack.ap-southeast-3.amazonaws.com/latest/linux/aws-replication-installer-init |
| Asia Pacific (Malaysia)   | ap-southeast-5  | **IPv4 -\*<br>• https://aws-application-migration-service-ap-southeast-5.s3.ap-southeast-5.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-ap-southeast-5.s3.dualstack.ap-southeast-5.amazonaws.com/latest/linux/aws-replication-installer-init |
| Asia Pacific (Mumbai)     | ap-south-1      | **IPv4 -\*<br>• https://aws-application-migration-service-ap-south-1.s3.ap-south-1.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-ap-south-1.s3.dualstack.ap-south-1.amazonaws.com/latest/linux/aws-replication-installer-init                 |
| Asia Pacific (Osaka)      | ap-northeast-3  | **IPv4 -\*<br>• https://aws-application-migration-service-ap-northeast-3.s3.ap-northeast-3.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-ap-northeast-3.s3.dualstack.ap-northeast-3.amazonaws.com/latest/linux/aws-replication-installer-init |
| Asia Pacific (Seoul)      | ap-northeast-2  | **IPv4 -\*<br>• https://aws-application-migration-service-ap-northeast-2.s3.ap-northeast-2.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-ap-northeast-2.s3.dualstack.ap-northeast-2.amazonaws.com/latest/linux/aws-replication-installer-init |
| Asia Pacific (Singapore)  | ap-southeast-1  | **IPv4 -\*<br>• https://aws-application-migration-service-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-ap-southeast-1.s3.dualstack.ap-southeast-1.amazonaws.com/latest/linux/aws-replication-installer-init |
| Asia Pacific (Sydney)     | ap-southeast-2  | **IPv4 -\*<br>• https://aws-application-migration-service-ap-southeast-2.s3.ap-southeast-2.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-ap-southeast-2.s3.dualstack.ap-southeast-2.amazonaws.com/latest/linux/aws-replication-installer-init |
| Asia Pacific (Tokyo)      | ap-northeast-1  | **IPv4 -\*<br>• https://aws-application-migration-service-ap-northeast-1.s3.ap-northeast-1.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-ap-northeast-1.s3.dualstack.ap-northeast-1.amazonaws.com/latest/linux/aws-replication-installer-init |
| Canada (Central)          | ca-central-1    | **IPv4 -\*<br>• https://aws-application-migration-service-ca-central-1.s3.ca-central-1.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-ca-central-1.s3.dualstack.ca-central-1.amazonaws.com/latest/linux/aws-replication-installer-init         |
| Europe (Frankfurt)        | eu-central-1    | **IPv4 -\*<br>• https://aws-application-migration-service-eu-central-1.s3.eu-central-1.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-eu-central-1.s3.dualstack.eu-central-1.amazonaws.com/latest/linux/aws-replication-installer-init         |
| Europe (Ireland)          | eu-west-1       | **IPv4 -\*<br>• https://aws-application-migration-service-eu-west-1.s3.eu-west-1.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-eu-west-1.s3.dualstack.eu-west-1.amazonaws.com/latest/linux/aws-replication-installer-init                     |
| Europe (London)           | eu-west-2       | **IPv4 -\*<br>• https://aws-application-migration-service-eu-west-2.s3.eu-west-2.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-eu-west-2.s3.dualstack.eu-west-2.amazonaws.com/latest/linux/aws-replication-installer-init                     |
| Europe (Milan)            | eu-south-1      | **IPv4 -\*<br>• https://aws-application-migration-service-eu-south-1.s3.eu-south-1.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-eu-south-1.s3.dualstack.eu-south-1.amazonaws.com/latest/linux/aws-replication-installer-init                 |
| Europe (Paris)            | eu-west-3       | **IPv4 -\*<br>• https://aws-application-migration-service-eu-west-3.s3.eu-west-3.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-eu-west-3.s3.dualstack.eu-west-3.amazonaws.com/latest/linux/aws-replication-installer-init                     |
| Europe (Stockholm)        | eu-north-1      | **IPv4 -\*<br>• https://aws-application-migration-service-eu-north-1.s3.eu-north-1.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-eu-north-1.s3.dualstack.eu-north-1.amazonaws.com/latest/linux/aws-replication-installer-init                 |
| Middle East (Bahrain)     | me-south-1      | **IPv4 -\*<br>• https://aws-application-migration-service-me-south-1.s3.me-south-1.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-me-south-1.s3.dualstack.me-south-1.amazonaws.com/latest/linux/aws-replication-installer-init                 |
| South America (São Paulo) | sa-east-1       | **IPv4 -\*<br>• https://aws-application-migration-service-sa-east-1.s3.sa-east-1.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-sa-east-1.s3.dualstack.sa-east-1.amazonaws.com/latest/linux/aws-replication-installer-init                     |
| Middle East (UAE)         | me-central-1    | **IPv4 -\*<br>• https://aws-application-migration-service-me-central-1.s3.me-central-1.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-me-central-1.s3.dualstack.me-central-1.amazonaws.com/latest/linux/aws-replication-installer-init         |
| Asia Pacific (Melbourne)  | ap-southeast-4  | **IPv4 -\*<br>• https://aws-application-migration-service-ap-southeast-4.s3.ap-southeast-4.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-ap-southeast-4.s3.dualstack.ap-southeast-4.amazonaws.com/latest/linux/aws-replication-installer-init |
| Asia Pacific (Hyderabad)  | ap-south-2      | **IPv4 -\*<br>• https://aws-application-migration-service-ap-south-2.s3.ap-south-2.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-ap-south-2.s3.dualstack.ap-south-2.amazonaws.com/latest/linux/aws-replication-installer-init                 |
| Europe (Zurich)           | eu-central-2    | **IPv4 -\*<br>• https://aws-application-migration-service-eu-central-2.s3.eu-central-2.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-eu-central-2.s3.dualstack.eu-central-2.amazonaws.com/latest/linux/aws-replication-installer-init         |
| Europe (Spain)            | eu-south-2      | **IPv4 -\*<br>• https://aws-application-migration-service-eu-south-2.s3.eu-south-2.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-eu-south-2.s3.dualstack.eu-south-2.amazonaws.com/latest/linux/aws-replication-installer-init                 |
| Israel (Tel Aviv)         | il-central-1    | **IPv4 -\*<br>• https://aws-application-migration-service-il-central-1.s3.il-central-1.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-il-central-1.s3.dualstack.il-central-1.amazonaws.com/latest/linux/aws-replication-installer-init         |
| AWS GovCloud (US-East)    | us-gov-east-1   | **IPv4 -\*<br>• https://aws-application-migration-service-us-gov-east-1.s3.us-gov-east-1.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-us-gov-east-1.s3.dualstack.us-gov-east-1.amazonaws.com/latest/linux/aws-replication-installer-init     |
| AWS GovCloud (US-West)    | us-gov-west-1   | **IPv4 -\*<br>• https://aws-application-migration-service-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/latest/linux/aws-replication-installer-init<br>**Dual-stack -\*<br>• https://aws-application-migration-service-us-gov-west-1.s3.dualstack.us-gov-west-1.amazonaws.com/latest/linux/aws-replication-installer-init     |

3. [Generate the temporary credentials](credentials.md "credentials.md") that are required
   to install the AWS Replication Agent.

###### Important

When using [temporary credentials](credentials.md "credentials.md") (created using an
IAM role instead of a user), you need to enter these parameters to the
command prompt:

    * AWS access key
    * AWS secret access key
    * AWS session tokenThe request to enter an AWS session token only appears if the system identifies

that you are using temporary credentials. AWS access key for temporary credentials begins
with the letters ASIA. 4. Once the agent installer has successfully downloaded, copy and input the installer
command into the command line on your source server in order to run the installation script.

`sudo chmod +x aws-replication-installer-init; sudo
 ./aws-replication-installer-init`

You can choose to add the Region and required credential as parameters in the
installation scripts:

    * **--region** – The AWS Region in which the installer
     registers the source server.
    * **--aws-access-key-id** – The AWS IAM Access Key used
     for authenticating the installing user. If this parameter is not provided, the installer
     prompts for it.
    * **--aws-secret-access-key** – The AWS IAM Secret
     Access Key tied to the AWS IAM Access Key used for authenticating the installing user.
     If this parameter is not provided, the installer prompts for it.
    * **--aws-session-token** – The session token is generated
     when using [temporary credentials](credentials.md "credentials.md") that are generated
     using AWS STS. If you use temporary credentials and do not provide this parameter, the
     installer prompts for it.

If you require additional customization, you can add a variety of parameters to the
installation script in order to manipulate the way the agent is installed on your server. Add
the parameters to the end of the installation script.

Available parameters include:

    * --no-prompt


    This parameter runs a silent installation.
    * --devices


    This parameter specifies which specific disks to replicate. The devices should be
     mentioned with comma separated, example
     `--devices="/dev/sda,/dev/sdb,/dev/sdc,/dev/sdd"`
    * --force-volumes


    This parameter must be used with the --no-prompt parameter. This parameter cancels
     the automatic detection of physical disks to replicate. You need to specify the exact
     disks to replicate using the --devices parameter (including the root disk, failure to
     specify the root disk causes replication to fail). This parameter should only be used
     as a troubleshooting tool if the --devices parameter fails to identify the disks correctly.
    * --tags


    Use this parameter to add resource tags to the source server. Use a space to separate
     each tag (for example: --tags KEY=VALUE [KEY=VALUE ...])


    ###### Note

    This flag may only be used when adding new source servers to Application Migration Service. You cannot use
     the --tags flag to modify tags of source servers that have already been added to Application Migration Service.
    * --s3-endpoint


    Use this parameter to specify a VPC endpoint you created for Amazon S3 if you do not wish
     to open your firewall ports to access the default Amazon S3 endpoint. [Learn more about installing the Agent on a blocked
     network.](installing-agent-blocked.md "installing-agent-blocked.md")
    * --user-provided-id


    This parameter allows you to provide a name to the source server that you are about to
     add, or identify a source server that needs to be updated. This identification is
     used by Application Migration Service to consistently recognize the server replication, and avoid
     duplication when [importing inventory](import-main.md "import-main.md") from a CSV file. Once provided for a server this parameter cannot be modified.
    * --endpoint


    Use this parameter:




    	+ To specify the private link endpoint you created for AWS Application Migration Service if
    	 you do not wish to open your firewall ports to access the default Application Migration Service endpoint. [Learn more about installing the Agent on a blocked
    	 network.](installing-agent-blocked.md "installing-agent-blocked.md")
    	+ When using dual-stack, to specify a Application Migration Service dual-stack endpoint. You must also specify the `--dualstack` flag.
    * --no-replication


    By default after agent installation, the replication begins automatically. This
     attribute allows you to install the agent without immediately starting the replication. The
     90-day free replication period excludes hours where the replication was stopped.


    To start the replication post installation of replication agent using
     `--no-replication` attribute you can start replication by using the "Start
     Replication" option from Replication menu for the source server in the AWS MGN Dashboard or
     by using AWS CLI [start-replication](../APIReference/API_StartReplication.md "../APIReference/API_StartReplication.md")
    * --dualstack


    This parameter enables the agent to run in a dual-stack Application Migration Service configuration. When using this flag, you must also use the `--endpoint` flag to specify a Application Migration Service dual-stack endpoint.

The installer confirms that the installation of the AWS Replication Agent has
started.

![Terminal output showing successful start of AWS Replication Agent installation.](images/sourceservers-linuxagent1.png) 5. The installer prompts you to enter your **AWS Region
Name**, the **AWS Access Key ID**, the **AWS Secret Access Key**, and the **AWS Session
Token** that you previously generated. Enter the complete AWS Region name (for
example, eu-central-1) and the full credentials.

![Terminal window showing AWS Replication Agent installation with region and credential inputs.](images/sourceservers-linuxagent2.png)

###### Note

    * You can also enter these values as part of the installation script command
     parameters. If you do not enter these parameters as part of the installation script, you
     are prompted to enter them one by one as described above. (for example: `sudo
     chmod +x aws-replication-installer-init; sudo ./aws-replication-installer-init --region
     regionname --aws-access-key-id AKIAIOSFODNN7EXAMPLE --aws-secret-access-key
     wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`).
    * The AWS Access Key ID and AWS Secret Access Key values are hidden when
     entered into the installer.

6. Once you have entered your credentials, the installer identifies volumes for
   replication. The installer displays the identified disks and prompt you to choose the
   disks you want to replicate.

![Terminal window showing AWS Replication Agent installation and volume identification process.](images/sourceservers-linuxagent3.png)

To replicate some of the disks, type the path of the disks, separated by a comma, as
illustrated in the installer (such as: /dev/sda, /dev/sdb, and more). To replicate all of the
disks, click **Enter**. The installer identifies the selected
disks and print their size.

![Terminal output showing AWS Replication Agent installation and volume identification process.](images/sourceservers-linuxagent4.png)

The installer confirms that all disks were successfully identified.

![Terminal output showing AWS Replication Agent installation and volume identification process.](images/sourceservers-linuxagent5.png)

###### Note

When identifying specific disks for replication, do not use apostrophes, brackets, or
disk paths that do not exist. Type only existing disk paths. Each disk you selected for
replication is displayed with the caption **Disk to replicate
identified**. However, the displayed list of identified disks for replication may
differ from the data you entered. This difference can due to several reasons:

    * The root disk of the source server is always replicated, whether you select it or
     not. Therefore, it always appears on the list of identified disks for replication.
    * AWS Application Migration Service replicates whole disks. Therefore, if you choose to replicate a partition,
     its entire disk appears on the list and is later replicated. If several
     partitions on the same disk are selected then that disk appears only once on the
     list.
    * Incorrect disks may be chosen by accident. Ensure that the correct disks have been
     chosen.

###### Important

If disks are disconnected from a server, AWS Application Migration Service can no longer replicate them, so
they are removed from the list of replicated disks. When they are reconnected, the AWS
Replication Agent cannot know that these were the same disks that were disconnected and
therefore does not add them automatically. To add the disks after they are reconnected,
rerun the AWS Replication Agent installer on the server.

Note that the returned disks need be replicated from the beginning. Any disk size
changes are automatically identified, but this also causes a resync. Perform a test
after installing the Agent to ensure that the correct disks have been added. 7. After all of the disks that are to be replicated have been successfully identified, the
installer downloads and installs the AWS Replication Agent on the source server.

![Terminal output showing AWS Replication Agent installation and volume identification process.](images/sourceservers-linuxagent6.png) 8. Once the AWS Replication Agent is installed, the server is added to the AWS Application Migration Service
console and undergoes the initial sync process. The installer provides you with the
source server's ID.

![Terminal output showing AWS Replication Agent installation and volume identification process.](images/sourceservers-linuxagent7.png)

You can review this process in real time on the **Source
servers** page. [Learn more about the initial sync
process](migration-dashboard.md#initiation "migration-dashboard.md#initiation").
