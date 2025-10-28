# Technical prerequisites

## Technical prerequisites

Implementing Elastic Disaster Recovery is a critical step in ensuring business continuity and resilience against unexpected disruptions. To achieve a successful deployment, it is essential to meet specific technical requirements that encompass various aspects of the system.
These requirements range from network settings and communication protocols to supported operating systems, Regions, and installation prerequisites.

The following sections provide a detailed overview of the technical requirements necessary for the implementation of Elastic Disaster Recovery. They include guidelines for staging area subnets, network requirements, Amazon S3 bucket access, operational subnets, supported
AWS Regions, general installation requirements, and specific considerations for Windows and Linux systems.

1.  **Administrative rights** - Elastic Disaster Recovery can only be initialized by the Admin user of your AWS Account.
    1. If you are using Single Sign On (SSO), refer to
       [Authenticating with identities in AWS Elastic Disaster Recovery](../../../drs/latest/userguide/security_iam_authentication.md "../../../drs/latest/userguide/security_iam_authentication.md")for more information

2.  **Multi-Account Requirements**
    [Reference](../../../drs/latest/userguide/multi-account.md "../../../drs/latest/userguide/multi-account.md")

        * **Staging Account Planning and Limitations**: Due to AWS account wide API limitations, Elastic Disaster Recovery is limited to protecting 300 source servers per AWS account. In order to replicate more than 300 servers, you would be required to create multiple staging area AWS accounts. It would still be possible to recover all of your servers into
        a single recovery environment. Elastic Disaster Recovery can recover up to 3,000 servers into a single target AWS account.

3.  **Network Requirements**
    **[https://docs.aws.amazon.com/drs/latest/userguide/Network-Requirements.html](../../../drs/latest/userguide/Network-Requirements.md "../../../drs/latest/userguide/Network-Requirements.md")Reference**

        * **Preparation**: Create a dedicated staging subnet for data replication from source servers to AWS.




        	+ This subnet should have a Classless Inter Domain Routing (CIDR) range that meets the following criteria:




        		- Not overlap with the source server CIDR ranges.
        		- Have enough IP addresses for 1 replication server per 15 source volumes, or dedicated replication servers for highly transactional sources.
        		- Support 1 conversion server per source server to be launched.
        * **Staging subnet access requirements**: The staging area subnet requires outbound internet access to the Amazon EC2, Amazon S3, and Elastic Disaster Recovery endpoints within the Target Region. You can create private link endpoints, or use public internet access to communicate with these AWS services.
        * **Communication over TCP Port 443**: All communication is encrypted with TLS. All control plane traffic is handled over TCP port 443 and should be permitted for the following:




        	+ Between the source servers and Elastic Disaster Recovery Service
        	+ Between the staging area subnet and AWS Elastic Disaster Recovery
        	+ The Elastic Disaster Recovery AWS Region-specific Console address: *example: [drs.eu-west-1.amazonaws.com](http://drs.eu-west-1.amazonaws.com/ "http://drs.eu-west-1.amazonaws.com/")*
        	+ Amazon S3 service URLs (required for downloading AWS Elastic Disaster Recovery software)
        	+ The AWS Replication Agent installer should have access to the S3 bucket URL of the AWS Region you are using with Elastic Disaster Recovery.
        	+ The staging area subnet should have access to the Regional S3 endpoint.
        	+ The staging area subnet requires outbound access to the
        	[Amazon EC2 endpoint of its AWS Region](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
        * **Communication over TCP Port 1500**: All data replication traffic is transmitted between the Source servers and the staging area subnet using TCP Port 1500; this communication is also encrypted.
        * **Bandwidth Requirements**: The average network bandwidth must exceed the peak write rate of the source servers to ensure successful replication in the AWS Elastic Disaster Recovery service. Adequate network capacity is critical to maintain continuous data protection and meet your recovery point objectives.

4.  **Amazon S3 Buckets**
    [**Reference**](../../../drs/latest/userguide/Network-Requirements.md "../../../drs/latest/userguide/Network-Requirements.md")

        * **Access Requirements**: Agent installation and replication server components require Amazon S3 bucket access.
        * **VPC Endpoint Policy**: Ensure that the relevant VPC endpoint policy includes access to all required Amazon S3 buckets. Refer to the example policy for
        [replicating to us-east-1](../../../drs/latest/userguide/Network-Requirements.md "../../../drs/latest/userguide/Network-Requirements.md") and
        [Amazon
        S3 documentation](../../../AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.md "../../../AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.md") for policy requirements.

5.  **Operational Subnets**
    **[https://docs.aws.amazon.com/drs/latest/userguide/Network-Settings-Preparations.html](../../../drs/latest/userguide/Network-Settings-Preparations.md "../../../drs/latest/userguide/Network-Settings-Preparations.md")
    **Reference\*\*\*\*

        * **Drill and Recovery Subnets**: Create Recovery subnets (and optionally Drill subnets), before attempting to launch Recovery Instances. Instances are launched in a subnet specified in the Amazon EC2 launch template associated with each source server.

6.  **Supported Elastic Disaster Recovery AWS Regions**
    [**Reference**](../../../drs/latest/userguide/supported-regions.md "../../../drs/latest/userguide/supported-regions.md")

        * Refer to AWS Elastic Disaster Recovery
        [supported Regions reference](../../../drs/latest/userguide/supported-regions.md "../../../drs/latest/userguide/supported-regions.md") for an up to date list of all supported Regions.

7.  **Supported Operating Systems**
    **[https://docs.aws.amazon.com/drs/latest/userguide/Supported-Operating-Systems.html](../../../drs/latest/userguide/Supported-Operating-Systems.md "../../../drs/latest/userguide/Supported-Operating-Systems.md")
    **Reference\*\*\*\*

        * Elastic Disaster Recovery supports many versions of Windows and Linux operating systems, some of which are not natively supported by Amazon EC2. Refer to
        [Supported Operating Systems](../../../drs/latest/userguide/Supported-Operating-Systems.md "../../../drs/latest/userguide/Supported-Operating-Systems.md") for up-to-date versions of supported operating systems.

8.  **Windows Installation Requirements**
    **[https://docs.aws.amazon.com/drs/latest/userguide/installation-requiremets.html#windows-requirements](../../../drs/latest/userguide/installation-requiremets.md#windows-requirements "../../../drs/latest/userguide/installation-requiremets.md#windows-requirements")
    **Reference\*\*\*\*

        * **Supported Operating Systems**: Ensure that your source server
        [operating system](../../../drs/latest/userguide/Supported-Operating-Systems.md "../../../drs/latest/userguide/Supported-Operating-Systems.md") is supported.
        * **Free Disk Space**: At least 4 GB of free disk space on the root directory (C:by default).
        * **Free RAM**: At least 300 MB of free RAM.
        * **MAC Address Stability**: Ensure that the MAC addresses of the source servers do not change upon a reboot or any other common changes in your network environment. The AWS Replication Agent may use the MAC address in its process to link the source server to its replication infrastructure.

9.  **Linux Installation Requirements**
    **[https://docs.aws.amazon.com/drs/latest/userguide/installation-requiremets.html#linux-requirements](../../../drs/latest/userguide/installation-requiremets.md#linux-requirements "../../../drs/latest/userguide/installation-requiremets.md#linux-requirements")
    **Reference\*\*\*\*

        * **Supported Operating Systems**: Ensure that your source server operating system is supported (referenced above)
        * **MAC Address Stability**: Ensure that the MAC addresses of the source servers do not change upon a reboot or any other common changes in your network environment. The AWS Replication Agent may use the MAC address in its process to link the source server to its replication infrastructure.




        	1. **Python**: Python 2 (2.4 or above) or Python 3 (3.0 or above) must be installed on the server.
        	2. **Free Disk Space**: At least 4 GB on the root directory (/), 500 MB on the /tmp directory.
        	3. **GRUB Bootloader**: The active bootloader software must be GRUB 1 or 2.
        	4. **/tmp Directory**: Mounted as read+write and with the exec option.
        	5. **Sudoers List**: The Linux account that is installing AWS Elastic Disaster Recovery needs to be in the sudoers list.
        	6. **dhclient Package**: Ensure that the dhclient package is installed.
        	7. **Kernel Headers**: Verify that kernel-devel/linux-headers are installed and match the running kernel version.
        	8. **Symbolic Link Considerations**: Ensure that the content of the kernel-devel/linux-headers is not a symbolic link.




        		1. Sometimes, the content of the kernel-devel/linux-headers, which match the version of the kernel, is actually a symbolic link. In this case, you will need to remove the link before installing the required package.




        			1. To verify that the folder that contains the
        			kernel-devel/linux-headers is not a symbolic link, run the following command:




        				1. On RHEL/CENTOS/Oracle: `ls -l /usr/src/kernels``
        				2. On Debian/Ubuntu/SUSE: `ls -l /usr/src``
        		2. If you found that the content of the kernel-devel/linux-headers, which matches the version of the kernel, is a symbolic link, you need to delete the link.




        			1. Run the following command: `rm /usr/src/``





        				1. For example: `rm /usr/src/linux-headers-4.4.1``
        	9. **Kernel Headers Installation**: For the agent to operate properly, you need to install a kernel headers package with the exact same version number of the running kernel.




        		1. To install the correct kernel-devel/linux-headers, run the following commands:




        			1. On RHEL/CENTOS/Oracle/SUSE: `sudo yum install
        			kernel-devel-`+uname -r+`
        			2. On Debian/Ubuntu: `s__udo apt-get install
        			linux-headers-`+uname -r+`
        		2. If no matching package was found on the repositories configured on your server, you can download it manually from the Internet and then install it. To download the matching kernel-devel/linux-headers package, navigate to the following sites:




        			1. RHEL, CENTOS, Oracle, and SUSE [package directory](http://rpm.pbone.net/ "http://rpm.pbone.net/")
        			2. Debian [package directory](https://packages.debian.org/ "https://packages.debian.org/")
        			3. Ubuntu [package directory](https://packages.ubuntu.com/ "https://packages.ubuntu.com/")

10. **AWS Specific Considerations**
    1. Number of disks per server
       1. Elastic Disaster Recovery uses Amazon Elastic Block Store and Amazon Elastic Compute Cloud for the replication infrastructure. Because of this, Elastic Disaster Recovery is limited to the amount of disks that can be added to the replication servers.
          1. For
             [Nitro replication instances](../../../ec2/latest/instancetypes/ec2-nitro-instances.md "../../../ec2/latest/instancetypes/ec2-nitro-instances.md") (such as t3.small), we are limited to source servers with less than 26 volumes
          2. For
             [Xen replication instances](../../../ec2/latest/instancetypes/instance-types.md#previous-gen-instances "../../../ec2/latest/instancetypes/instance-types.md#previous-gen-instances") (such as t2.small), the limitation is 40 volumes per source server

    2. Maximum source disk size
       1. Elastic Disaster Recovery uses Amazon Elastic Block Store and Amazon Elastic Compute Cloud for the replication infrastructure. Because of this, Elastic Disaster Recovery is limited to the 16TB for each disk on the source machines being protected.
