# Installing the AWS Replication Agent on Linux

To install the agent on a Linux source server, you should ensure that your source meets
all the requirements list in the [supported Linux operating systems](Supported-Operating-Systems-Linux.md "Supported-Operating-Systems-Linux.md")
documentation.

Before installing, please ensure that you are aware of the following:

- You need root privileges to run the Agent installer file on a Linux server. Alternatively, you can run the Agent Installer file with sudo permissions.
- The Linux installer creates the **"aws-replication"** group and
  **"aws-replication"** user within that group. The Agent runs
  within the context of the newly created user. Agent installation attempts to add the
  user to **"sudoers"**. Installation fails if the Agent is unable to
  add the newly created **"aws-replication"** user to
  **"sudoers"**.

1. Download the agent installer `aws-replication-installer-init` onto your Linux source server.

The Agent installer download location follows this format:

`https://aws-elastic-disaster-recovery-<REGION>.s3.<REGION>.amazonaws.com/latest/linux/aws-replication-installer-init`

###### Note

Replace `<REGION>` with the AWS Region into which you are replicating.

The following is an example for downloading the installer file from the us-east-1 region:

wget

```
wget -O ./aws-replication-installer-init https://aws-elastic-disaster-recovery-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/aws-replication-installer-init
```

curl

```
curl -o aws-replication-installer-init https://aws-elastic-disaster-recovery-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/aws-replication-installer-init
```

###### Note

If you are using a legacy Linux OS that does not support TLS 1.2, you need to download the installer on a different server
with an OS that supports TLS 1.2 and copy it to the legacy servers you intend to install the agent on.

The command line indicates when the installer has been successfully downloaded.

###### Important

If you need to validate the installer hash, the correct hash is here:

`https://aws-elastic-disaster-recovery-hashes-<REGION>.s3.<REGION>.amazonaws.com/latest/linux/aws-replication-installer-init.sha512`

Replace `<REGION>` with the AWS Region into which you are replicating

For example, when using the **us-east-1** Region

`https://aws-elastic-disaster-recovery-hashes-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/aws-replication-installer-init.sha512`

###### Note

AWS Regions that are not opt-in also support the shorter installer path:

`https://aws-elastic-disaster-recovery-<REGION>.s3.amazonaws.com/latest/linux/aws-replication-installer-init`. Replace
`<REGION>` with the AWS Region into which you are replicating.

###### Note

If you are using a Windows Servers of versions 2016 or older, and are using PowerShell to download the installer,
you need to enable TLS 1.2:
`[System.Net.ServicePointManager]::SecurityProtocol = 'TLS12'` 2. Use this command on your source server in order to run the installation script.

```
chmod +x aws-replication-installer-init; sudo ./aws-replication-installer-init
```

###### Note

To install the agent on a secured network, [learn about the additional required configurations](installing-agent-blocked.md "installing-agent-blocked.md").

If you require additional customization, you can add a variety of parameters to the installer script in order to manipulate the way the Agent is installed on your server.
See the [AWS Replication Agent Installer Parameters](installer-parameters.md "installer-parameters.md") for more information.

The installer confirms that the installation of the AWS Replication Agent has
started.

```
`$` `chmod +x aws-replication-installer-init; sudo ./aws-replication-installer-init``The installation of the AWS Replication Agent has started.`
```

3. The installer prompts you to enter your **AWS Region
   Name**, the **AWS Access Key ID** and
   **AWS Secret Access Key** that you previously
   generated. Enter the complete AWS Region name (for example, eu-central-1), the
   full AWS Access Key ID and the full AWS Secret Access Key.

```
`$` `chmod +x aws-replication-installer-init; sudo ./aws-replication-installer-init``The installation of the AWS Replication Agent has started.
AWS Region name: us-east-1
AWS Access Key ID: AKIAI0SF0DNN71EXAMPLE
AWS Secret Access Key: wJalrXUtnFEMI/K71MDENG/bPxRfiCYEXAMPLEKEY`
```

###### Note

You can also enter these values as part of the installation script command
parameters. If you do not enter these parameters as part of the installation
script, you are prompted to enter them one by one as described above. (for
example: `chmod +x aws-replication-installer-init; sudo
 ./aws-replication-installer-init --region regionname --aws-access-key-id
 AKIAIOSFODNN71EXAMPLE --aws-secret-access-key
 wJalrXUtnFEMI/K71MDENG/bPxRfiCYEXAMPLEKEY`) 4. Once you have entered your credentials, the installer identifies volumes for
replication. The installer displays the identified disks and prompt you to choose
the disks you want to replicate.

```
`$` `chmod +x aws-replication-installer-init; sudo ./aws-replication-installer-init``...
AWS Secret Access Key: wJalrXUtnFEMI/K71MDENG/bPxRfiCYEXAMPLEKEY
Identifying volumes for replication.
Choose the disks you want to replication. Your disks are: /dev/sda,/dev/xvda
To replication some of the disks, type the path of the disks, separated with a comma (for example, /dev/sda,/dev/sdb).
To replication all disks, press Enter:`
```

To replicate some of the disks, type the path of the disks, separated by a comma, as
illustrated in the installer (such as: /dev/sda, /dev/sdb, etc). To replicate all of
the disks, press Enter. The installer identifies the selected disks and prints their
size.

```
`$` `chmod +x aws-replication-installer-init; sudo ./aws-replication-installer-init``...
To replication some of the disks, type the path of the disks, separated with a comma (for example, /dev/sda,/dev/sdb).
To replication all disks, press Enter:
Identified volume for replication: /dev/xvda of size 8 GiB`
```

The installer confirms that all disks were successfully identified.

```
`$` `chmod +x aws-replication-installer-init; sudo ./aws-replication-installer-init``...
Identified volume for replication: /dev/xvda of size 8 GiB
`All volumes for replication were successfully identified.``
```

###### Note

When identifying specific disks for replication, do not use apostrophes, brackets, or
disk paths that do not exist. Type only existing disk paths. Each disk you selected for
replication is displayed with the caption **Disk to replicate
identified**. However, the displayed list of identified disks for replication may
differ from the data you entered. This difference can due to several reasons:

    * The root disk of the source server is always replicated, whether you select it or
     not. Therefore, it always appears on the list of identified disks for replication.
    * AWS Elastic Disaster Recovery replicates whole disks. Therefore, if you choose to replicate a
     partition, its entire disk appears on the list and is later replicated. If
     several partitions on the same disk are selected, then the disk encompassing
     all of them appears only once on the list.
    * Incorrect disks may be chosen by accident. Ensure that the correct disks have been
     chosen.

###### Important

If disks are disconnected from a server, AWS Elastic Disaster Recovery can no longer
replicate them, so they are removed from the list of replicated disks. When they
are reconnected, the AWS Replication Agent cannot know that these were the same
disks that were disconnected and therefore does not add them automatically. To add
the disks after they are reconnected, rerun the AWS Replication Agent installer on
the server.

Note that the returned disks need to be replicated from the beginning. Any disk size
change is automatically identified, but also causes a resync. Perform a test after
installing the Agent to ensure that the correct disks have been added. 5. After all of the disks to be replicated have been successfully identified, the
installer downloads and installs the AWS Replication Agent on the source
server.

```
`$` `chmod +x aws-replication-installer-init; sudo ./aws-replication-installer-init``...
Identified volume for replication: /dev/xvda of size 8 GiB
`All volumes for replication were successfully identified.`
Downloading the AWS Replication Agent onto the source server... `Finished`
Installing the AWS Replication Agent onto the source server... `Finished``
```

6. Once the AWS Replication Agent is installed, the server is added to the AWS Elastic Disaster Recovery
   console and undergoes the initial sync process. The installer provides the source
   server's ID.

```
`$` `chmod +x aws-replication-installer-init; sudo ./aws-replication-installer-init``...
Installing the AWS Replication Agent onto the source server... `Finished`
Syncing the source server with the AWS Elastic Disaster Recovery console... `Finished
The following is the source server ID: s-3146f90b19example
The AWS Replication Agent was successfully installed.`
`$``
```

You can review this process in real time on the **Source
servers** page.
