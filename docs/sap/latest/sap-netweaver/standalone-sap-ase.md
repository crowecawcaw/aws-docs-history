# Standalone deployment

In this example, we set up a sample environment for installation. It includes a public subnet for RDP and SSH access via the internet. We use the [AWS Quick Start for Modular and Scalable Amazon VPC Architecture](https://aws.amazon.com/quickstart/architecture/vpc/ "https://aws.amazon.com/quickstart/architecture/vpc/") in a single Availability Zone deployment to create the Amazon VPC, subnets, security groups, and IAM roles. You can refer to this example set up but should also follow your own network layout and comply with security standards, such as the following:

- Using a Landing Zone solution like [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/").
- Working with a cloud team like Cloud Center of Excellence to use existing standards.

## Step 1: Prepare your AWS account

Check the Region where you want to deploy your AWS resources:

- You pick your region for deployment during the planning phase.
- Display the AWS Command Line Interface configuration data:

```
                $ aws configure list
```

Ensure that the default region listed in the command output is the same as the target region where you want to deploy your AWS resources and install SAP workloads. In this deployment, we provision an Amazon EC2 instance.

###### Note

In this section, the syntax used for the AWS CLI and Linux commands is specific to the scope of this document. Each command supports many additional options. To learn more, use the `aws help` command.

## Step 2: Create a `JSON` file for Amazon EBS storage

Create a `JSON` file containing the storage requirements for SAP ASE database server volumes. The following is an example `JSON` file with two Amazon EBS volumes for swap and installation directories. You can add more volumes as per your storage design.

```
                [
                    {
                        "DeviceName": "/dev/nvme2n1",
                        "Ebs": {
                        "VolumeSize": 32,
                        "VolumeType": "gp3",
                        "DeleteOnTermination": true
                        }
                    },
                    {
                        "DeviceName": "/dev/nvme3n1",
                        "Ebs": {
                        "VolumeSize": 50,
                        "VolumeType": "gp3",
                        "DeleteOnTermination": true
                    }
                  }
                ]
```

###### Note

In the preceding example, the device name `/dev/nvme2n1` is for Nitro based hypervisors. It differs for non-Nitro based hypervisors. For more information, see [Storage configuration](../sap-hana/hana-ops-storage-config.md "../sap-hana/hana-ops-storage-config.md").

## Step 3: Launch the Amazon EC2 instance

Launch the Amazon EC2 instance for the SAP ASE database installation in your target AWS Region, using the information gathered in Step 1. You must create the required storage volumes and attach them to the Amazon EC2 instance for the SAP installation, based on the `JSON` file you created in the Amazon EBS storage (Step 2).

```
$ aws ec2 run-instances \
--image-id <AMI-ID> \
--count <number-of-EC2-instances> \
--instance-type <instance-typ> \
--key-name=<name-of-key-pair> \
--security-group-ids <security-group-ID> \
--subnet-id <subnet-ID> \
--block-device-mappings file://<PATH>\<file>.json \
--region <region-ID>
```

Use this command in a single line format, as shown in the following example.

```
aws ec2 run-instances --image-id ami-xxxxxxxxxxxxxxx --count 1 --instance-type m5.large --key-name=my_key --security-group-ids sg-xxxxxxxx --subnet-id subnet-xxxxxx --block-device-mappings file://<PATH>\<file>.json
```

In this example, _m5.large_ is the value for the `instance-type` parameter. You must select an Amazon EC2 instance type based on your business requirements.

You can also launch Amazon EC2 instances using the AWS Management Console. For more information, see [Launch an instance](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-launch-instance "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-launch-instance").

## Step 4: Prepare the Linux Operating System

Before starting the installation, you need to perform Linux specific prerequisite tasks. For more information, refer to the following SAP Notes (requires SAP portal access).

- [SAP Note 1554717 – SYB: Planning information for SAP on ASE](https://launchpad.support.sap.com/#/notes/0001554717 "https://launchpad.support.sap.com/#/notes/0001554717")
- [SAP Note 1748888 – SYB: Inst.Systems Based on NW 7.3 and Higher: SAP ASE](https://launchpad.support.sap.com/#/notes/1748888 "https://launchpad.support.sap.com/#/notes/1748888")

## Step 5: Prepare each Amazon EC2 instance for SAP ASE installation

Download the SAP installation media as per the SAP installation guide, for the version of SAP NetWeaver you want to install on your Amazon EBS volumes. Locate your installation guide on the [Guide Finder for SAP NetWeaver and ABAP Platform](https://help.sap.com/docs/SAP_NETWEAVER/9e41ead9f54e44c1ae1a1094b0f80712/576f5c1808de4d1abecbd6e503c9ba42.html?language=en-US "https://help.sap.com/docs/SAP_NETWEAVER/9e41ead9f54e44c1ae1a1094b0f80712/576f5c1808de4d1abecbd6e503c9ba42.html?language=en-US"). You can store the SAP installation media using Amazon EFS or an Amazon S3 bucket for later reuse.

If you choose to install the SAP ASE database with high availability deployment across two Availability Zones, repeat the preceding steps for SAP ASE database standby high availability instance in the second Availability Zone.

If you choose to install SAP ASE database with high availability and disaster recovery deployment across two AWS Regions, repeat the preceding steps in the second AWS Region in which you want to run the ASE database standby disaster recovery instance.

## Step 6: Installing SAP ASE on Amazon EC2 instances

You are now ready to install the SAP ASE software on your Amazon EC2 instances. For more information, see the SAP ASE Database Software Installation section of your SAP NetWeaver installation guide. Locate your installation guide on the [Guide Finder for SAP NetWeaver and ABAP Platform](https://help.sap.com/docs/SAP_NETWEAVER/9e41ead9f54e44c1ae1a1094b0f80712/576f5c1808de4d1abecbd6e503c9ba42.html?language=en-US "https://help.sap.com/docs/SAP_NETWEAVER/9e41ead9f54e44c1ae1a1094b0f80712/576f5c1808de4d1abecbd6e503c9ba42.html?language=en-US").

The following is a non-exhaustive list of post-installation tasks for your SAP ASE database.

- Updating to the most recent patch available
- Installation of additional components
- Configure the SAP ASE backup

For more information, see the [Operations](ase-operations.md "ase-operations.md") section.
