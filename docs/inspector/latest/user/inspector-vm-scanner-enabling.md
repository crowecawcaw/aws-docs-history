

# Enabling Inspector VM Scanner
<a name="inspector-vm-scanner-enabling"></a>

 When you enable Enhanced EC2 Scanning in the Amazon Inspector console, Amazon Inspector uses Amazon EC2 Systems Manager (SSM) to automatically install the VM Scanner on your managed Amazon EC2 instances. Once installed, the scanner executes periodically (every 3 hours by default) and sends results to the Amazon Inspector Telemetry Service. 

## Requirements
<a name="inspector-vm-scanner-prerequisites"></a>

 To use the automatic installation method, your Amazon EC2 instances must meet the following requirements: 
+ The SSM Agent must be installed and running on the instance. For more information, see [Working with SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html) in the *AWS Systems Manager User Guide*.
+ The instance must have an IAM instance profile that allows SSM to manage the instance. For more information, see [Configure instance permissions for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-permissions.html) in the *AWS Systems Manager User Guide*.
+ The instance must have network connectivity to the SSM service endpoints.

**Note**  
 If your instances do not have SSM Agent installed or cannot meet these requirements, you can use the manual installation method instead. For more information, see [Manual installation and configuration](inspector-vm-scanner-using.md). 

## Enabling Enhanced EC2 Scanning
<a name="inspector-vm-scanner-enable-procedure"></a>

 To enable Enhanced EC2 Scanning and automatically install the VM Scanner: 

1. Open the Amazon Inspector console at [Getting Started with the AWS Management Console](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/getting-started.html).

1. In the navigation pane, choose **Account management**.

1. Under **EC2 scanning**, choose **Edit**.

1. Enable **Enhanced EC2 Scanning**.

 After you enable Enhanced EC2 Scanning, Amazon Inspector creates an SSM association that installs the VM Scanner on all eligible instances in your account. The scanner begins executing vulnerability assessments automatically. 

## Amazon VPC endpoint requirements for Enhanced EC2 Scanning on private Amazon EC2 instances
<a name="inspector-vm-scanner-vpc-endpoints"></a>

 You can run Enhanced EC2 Scanning on Amazon EC2 instances over an Amazon network. However, if you want to run Enhanced EC2 Scanning on private Amazon EC2 instances, you must create Amazon VPC endpoints. The following endpoints are required: 
+ `com.amazonaws.{{region}}.ec2messages`
+ `com.amazonaws.{{region}}.inspector2-telemetry`
+ `com.amazonaws.{{region}}.s3`
+ `com.amazonaws.{{region}}.ssm`
+ `com.amazonaws.{{region}}.ssmmessages`

 Where {{region}} is the Region code for the applicable AWS Region. 

 For more information, see [Improve the security of Amazon EC2 instances by using Amazon VPC endpoints for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-create-vpc.html) in the *AWS Systems Manager User Guide*. 