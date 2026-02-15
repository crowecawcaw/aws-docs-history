# Step 1: Prepare your AWS Account

In this example, we step through setting up a sample environment for the installation, which includes a public subnet for RDP and SSH access via the internet. In this scenario, we are using the [AWS Quick Start for Modular and Scalable VPC Architecture](https://aws.amazon.com/quickstart/architecture/vpc/ "https://aws.amazon.com/quickstart/architecture/vpc/") in a Single-AZ deployment to create the VPC, subnets, security groups, and IAM roles. This setup is just an example and you should follow your own network layout and ensure that you comply with your security standards. This could include:

- Using an AWS Quick Start that suits their requirements such as a Multi-AZ deployment of the AWS Quick Start for SAP HANA
- Using a landing zone solution, like [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/")
- Working with your cloud team (for example, a Cloud Center of Excellence or CCoE) to ensure adherence to existing standards
  1.  Check the Region where you want to deploy your AWS resources:
      1. You’ll have picked the Region you want to deploy in during your planning phase.
      2. Display the AWS CLI configuration data:

      ```
       $ aws configure list
      ```

      In the command output, make sure that the default Region that’s listed is the same as the target Region where you want to deploy your AWS resources and install SAP NetWeaver.

  2.  If this is a distributed or HA installation type:
      1. Create a new security group specifically for the EC2 instances running the NetWeaver application servers that allows traffic over the required ports for remote access from the public subnet, for example, RDP.
      2. Edit that security group to allow traffic over ports required for SAP NetWeaver based on your specific use-case. Specify the source as being the security group itself and ensure that this security group is attached to all EC2 instances that will run application servers.
      3. For distributed or HA installations, ensure that the security group attached to each application and central services server allows communication between them over the required ports. You can create a rule that references a security group as its own source, and allow traffic on the required ports for that rule.

  3.  Create a JSON file for the Amazon EBS storage volumes (the volume sizes used are indicative only and should be customized based on your sizing requirements):

  ```
   [
      {
          "DeviceName": "xvdb",
          "Ebs": {
              "VolumeSize": 50,
              "VolumeType": "gp2",
              "DeleteOnTermination": true
          }
      },
      {
          "DeviceName": "xvdc",
          "Ebs": {
              "VolumeSize": 50,
              "VolumeType": "gp2",
              "DeleteOnTermination": true
          }
      }
  ]
  ```

  4.  AWS Windows AMIs provide additional software that prepares an instance when it first boots up. This is either the EC2Config service (Windows AMIs prior to Windows Server 2016) or EC2Launch (Windows Server 2016, or later). After the devices have been mapped to drives, they are initialized and mounted. The root drive is initialized and mounted as `C:\`. By default, when an EBS volume is attached to a Windows instance, it can show up as any drive letter on the instance. You can change the settings to set the drive letters of the volumes per your specifications. For more information, see the [device naming section for storage on Windows](../../../AWSEC2/latest/WindowsGuide/device_naming.md "../../../AWSEC2/latest/WindowsGuide/device_naming.md").
  5.  Install your selected database product. If this is a distributed or high availability deployment, install your selected database product in a separate EC2 instance dedicated to that purpose. Otherwise, install your database in the existing EC2 instance. For more details, see the [AWS Documentation](../../../index.md "../../../index.md") for your database.
  6.  Launch EC2 instances for the SAP installation in your target Region by using the information you gathered in the preparation phase. You will also be creating the storage volumes required for the SAP installation and attaching them to the Amazon EC2 instance for the SAP installation.

  Ensure that you enable detailed monitoring on each instance as this is required for SAP support. (The sample commands provided below enable this.)

  Make sure that you choose one of the [Amazon EC2 Instance Types for SAP](https://aws.amazon.com/sap/instance-types/ "https://aws.amazon.com/sap/instance-types/"). Sample AWS CLI syntax is given below.

  ```
  $ aws ec2 run-instances \
  --image-id <AMI-ID> \
  --monitoring Enabled=true \
  --count <number-of-EC2-instances> \
  --instance-type <instance-type> \
  --key-name=<name-of-key-pair> \
  --security-group-ids <security-group-ID> \
  --subnet-id <subnet-ID> \
  --block-device-mappings https://<bucket>.s3.amazonaws.com/<file>.json
  ```

  ###### Example

  This example enables detailed monitoring (data is available in 1-minute periods for an additional cost) which is a support prerequisite for SAP workloads on Amazon EC2.

  ```
  $ aws ec2 run-instances \
  --image-id ami-012345678901234ab \
  --monitoring Enabled=true \
  --count 1 \
  --instance-type m5.2xlarge \
  --key-name=my_key \
  --security-group-ids sg-01234567890abcdef \
  --subnet-id subnet-0123456789abcdefg \
  --block-device-mappings https://example.s3.amazonaws.com/file.json
  ```
