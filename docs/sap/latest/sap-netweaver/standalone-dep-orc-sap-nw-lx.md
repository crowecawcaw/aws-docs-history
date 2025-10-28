# Standalone deployment

In this example, we set up a sample environment for installation. It includes a public subnet for RDP and SSH access via the internet. We use AWS Launch Wizard for SAP in a single Availability Zone deployment to create the Amazon VPC, subnets, security groups, and IAM roles. You can refer to this example set up but should also follow your own network layout and comply with security standards, such as the following:

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

Create a JSON file containing the storage requirements for SAP Oracle database server volumes. The following is an example `JSON` file with two Amazon EBS volumes for swap and installation directories. You can add more volumes as per your storage design.

```
[
  {
    "DeviceName": "/dev/sdh",
    "Ebs": {
      "VolumeSize": 32,
      "VolumeType": "gp3",
      "DeleteOnTermination": true
    }
  },
  {
    "DeviceName": "/dev/sdg",
    "Ebs": {
      "VolumeSize": 50,
      "VolumeType": "gp3",
      "DeleteOnTermination": true
    }
  }
]
```

In the preceding example, the device name `/dev/shd` is for non-nitro based hypervisors. On Nitro-based instances, Amazon EBS volumes are presented as NVME block devices. You need to perform additional mapping when configuring these volumes. For more information, see [Operating system and storage configuration](../sap-hana/operating-system-and-storage-configuration.md "../sap-hana/operating-system-and-storage-configuration.md").

## Step 3: Launch the Amazon EC2 instance

Launch the Amazon EC2 instance for the SAP Oracle database installation in your target region, using the information gathered in Step 1. You must create the required storage volumes and attach them to the Amazon EC2 instance for the SAP installation, based on the `JSON` file you created in the Amazon EBS storage (Step 2).

```
$ aws ec2 run-instances \
--image-id <AMI-ID> \
--count <number-of-EC2-instances> \
--instance-type <instance-type> \
--key-name=<name-of-key-pair>
--security-group-ids <security-group-ID> \
--subnet-id <subnet-ID> \
--block-device-mappings file://C:\Users\<file>.json \
--region <region-ID>
```

Use this command in a single line format, as shown in the following example.

```
aws ec2 run-instances --image-id ami-xxxxxxxxxxxxxxx --count 1 --instance-type m5.large --key-name=my_key --security-group-ids sg-xxxxxxxx --subnet-id subnet-xxxxxx  --block-device-mappings file://C:\Users\<file>.json
```

You can also launch Amazon EC2 instances using the AWS Management Console. For more information, see [Launch an instance](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-launch-instance "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-launch-instance").

## Step 4: Prepare the Oracle Linux OS

Before starting the installation, you need to perform Oracle Enterprise Linux specific prerequisite tasks. For more information, refer to SAP Notes [1635808](https://launchpad.support.sap.com/#/notes/1635808 "https://launchpad.support.sap.com/#/notes/1635808"), [2069760](https://launchpad.support.sap.com/#/notes/2069760 "https://launchpad.support.sap.com/#/notes/2069760"), and [2936683](https://launchpad.support.sap.com/#/notes/2936683 "https://launchpad.support.sap.com/#/notes/2936683") (login required).

## Step 5: Prepare each Amazon EC2 instance for SAP Oracle installation

Download the SAP installation media as per the SAP installation guide, for the version of SAP NetWeaver you want to install on your Amazon EBS volumes. Locate your installation guide on the [Guide Finder for SAP NetWeaver](https://help.sap.com/viewer/nwguidefinder "https://help.sap.com/viewer/nwguidefinder").

If you choose to install the SAP Oracle database with high availability deployment across two Availability Zones, repeat the preceding steps for Oracle database standby HA instance in the second Availability Zone.

If you choose to install SAP Oracle database with high availability and disaster recovery deployment across two AWS Regions, repeat the preceding steps in the second AWS Region in which you want to run the Oracle database standby DR instance.

## Step 6: Installing SAP Oracle on Amazon EC2 instances

You are now ready to install the SAP Oracle software on your Amazon EC2 instances. For more information, see the Oracle Database Software Installation section of your SAP NetWeaver installation guide. Locate your installation guide on the [Guide Finder for SAP NetWeaver](https://help.sap.com/viewer/nwguidefinder "https://help.sap.com/viewer/nwguidefinder"). Instructions are available for all supported Oracle database versions.
