# Install the agent

The AWS Ground Station Agent can be installed in the following ways:

1. CloudFormation template (recommended).
2. Manual install on Amazon EC2.

## Use a CloudFormation template

The EC2 data delivery CloudFormation template creates the required AWS resources to deliver data to your EC2 instance. This CloudFormation template uses the AWS Ground Station managed AMI that has the AWS Ground Station Agent pre-installed.
The created EC2 instance’s boot script then populates the agent configuration file and applies the necessary performance tuning ([Tune your EC2 instance for performance](ec2-instance-performance-tuning.md "ec2-instance-performance-tuning.md")).

### Step 1: Create AWS resources

Create your AWS resources stack using template
[Public broadcast satellite utilizing AWS Ground Station Agent (wideband)](../ug/examples.md "../ug/examples.md") .

### Step 2: Check agent status

By default the agent is configured and active (started).
In order to check the agent status you can connect to the EC2 instance (SSH or SSM Session Manager) and see [AWS Ground Station Agent status](managing-agent.md#gs-agent-status "managing-agent.md#gs-agent-status").

## Install manually on EC2

While Ground Station recommends using CloudFormation templates to provision your AWS Resources there may be use cases where the standard template may not suffice.
For such cases we recommend that you customize the template to suit your needs.
If that still does not meet your requirements, you can manually create your AWS resources and install the agent.

### Step 1: Create AWS resources

See
[Example mission profile configurations](../ug/examples.md "../ug/examples.md") for instructions to set up the AWS resources required for a contact
manually.

The **AwsGroundStationAgentEndpoint** resource defines an endpoint for receiving a DigIF dataflow via AWS Ground Station Agent and is a critical to taking a successful contact.
While the API documentation is located in the [API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md"), this section will briefly discuss concepts relevant to the AWS Ground Station Agent.

The endpoint’s `ingressAddress` is where the AWS Ground Station Agent will receive AWS KMS encrypted UDP traffic from the Antenna.
The `socketAddress` `name` is the public IP of the EC2 instance (from the attached EIP).
The `portRange` should be at least 300 contiguous ports in a range that has been reserved from any other usage. See [Reserve ingress ports - impacts network](ec2-instance-performance-tuning.md#reserve-ingress-ports "ec2-instance-performance-tuning.md#reserve-ingress-ports") for instructions.
These ports must be configured to allow UDP ingress traffic on the security group for the VPC where the receiver instance is running.

The endpoint’s `egressAddress` is where the Agent will hand off the DigIF dataflow to you.
You should have an application (e.g. SDR) receiving the data over a UDP socket at this location.

### Step 2: Create EC2 instance

The following AMIs are supported:

1. AWS Ground Station AMI - `groundstation-al2-gs-agent-ami-*` where \* is the date the AMI was built - comes with agent installed (recommended).
2. `amzn2-ami-kernel-5.10-hvm-x86_64-gp2`.

### Step 3: Download and install agent

###### Note

Steps in this section must be completed if you did **not** choose the AWS Ground Station Agent AMI in the previous step.

#### Download agent

The AWS Ground Station Agent is available from region specific S3 buckets and can be downloaded onto support EC2 instances using the AWS command line (CLI) from `s3://groundstation-wb-digif-software-${AWS::Region}/aws-groundstation-agent/latest/amazon_linux_2_x86_64/aws-groundstation-agent.rpm` where ${AWS::Region} refers to one of the supported [AWS Ground Station Console and Data Delivery Regions](../ug/aws-ground-station-antenna-locations.md "../ug/aws-ground-station-antenna-locations.md").

Example: Download the latest rpm version from AWS region us-east-2 locally to the /tmp folder.

```

aws s3 --region us-east-2 cp s3://groundstation-wb-digif-software-us-east-2/aws-groundstation-agent/latest/amazon_linux_2_x86_64/aws-groundstation-agent.rpm /tmp

```

If you need to download a specific version of the AWS Ground Station Agent, you can download it from the version specific folder in the S3 bucket.

Example: Download version 1.0.2716.0 of the rpm from AWS region us-east-2 locally to the /tmp folder.

```

aws s3 --region us-east-2 cp s3://groundstation-wb-digif-software-us-east-2/aws-groundstation-agent/1.0.2716.0/amazon_linux_2_x86_64/aws-groundstation-agent.rpm /tmp

```

###### Note

If you want to confirm the RPM you downloaded was vended by AWS Ground Station, follow the instructions for [RPM installation validation](rpm-install-validation.md "rpm-install-validation.md").

#### Install agent

```

sudo yum install ${MY_RPM_FILE_PATH}

Example: Assumes agent is in the "/tmp" directory
sudo yum install /tmp/aws-groundstation-agent.rpm

```

### Step 4: Configure the agent

After installing the agent you must update the agent configuration file. See [Configure the agent](configuring-agent.md "configuring-agent.md").

### Step 5: Apply Performance Tuning

**AWS Ground Station Agent AMI**: If you chose the AWS Ground Station Agent AMI in the previous step then apply the following performance tunings.

- [Tune hardware interrupts and receive queues - impacts CPU and network](ec2-instance-performance-tuning.md#tune-hardware-interrupts "ec2-instance-performance-tuning.md#tune-hardware-interrupts")
- [Reserve ingress ports - impacts network](ec2-instance-performance-tuning.md#reserve-ingress-ports "ec2-instance-performance-tuning.md#reserve-ingress-ports")
- [Reboot](ec2-instance-performance-tuning.md#reboot "ec2-instance-performance-tuning.md#reboot")

**Other AMIs**: If you chose any other AMI in the previous step then apply all tunings listed under [Tune your EC2 instance for performance](ec2-instance-performance-tuning.md "ec2-instance-performance-tuning.md") and Reboot the instance.

### Step 6: Manage the agent

In order to start, stop and check agent status see [Manage the agent](managing-agent.md "managing-agent.md").
