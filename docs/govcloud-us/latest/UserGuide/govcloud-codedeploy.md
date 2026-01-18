# AWS CodeDeploy in AWS GovCloud (US)

AWS CodeDeploy is a deployment service that enables developers to automate the deployment of applications to instances and to update the applications as required.

## How AWS CodeDeploy differs for AWS GovCloud (US)

- The new AWS CodeDeploy console is not available in the AWS GovCloud (US) Regions
- Use TLS (HTTPS) when you make calls to the service in AWS GovCloud (US) Regions. In other regions, you can use HTTP or HTTPS.
- Several procedures in the CodeDeploy User Guide require the customer to substitute the name of a region-specific Amazon S3 bucket or bucket ARN. These procedures are for tasks such as restricting bucket access and downloading installation files, samples, and templates. In AWS GovCloud (US) Regions, the formats for accessing these resources do not follow the same patterns as for other Regions.
- ECS capacity providers are not supported.
- Automatically updating outdated instances is not supported.
- CodeDeploy does not have a VPC endpoint powered by PrivateLink.

## Documentation for AWS CodeDeploy

Use the values presented here to complete CodeDeploy procedures in the AWS GovCloud (US).

### CodeDeployAmazon S3 resources bucket

Name of the Amazon S3 bucket containing CodeDeploy files:

```
 aws-codedeploy-us-gov-west-1
```

### CodeDeployAmazon S3 bucket ARN

ARN of the Amazon S3 bucket containing CodeDeploy files:

```
 arn:aws-us-gov:s3:::aws-codedeploy-us-gov-west-1
```

### wget download command

wget command for downloading the CodeDeploy agent on Linux and Ubuntu instances:

```
 wget https://aws-codedeploy-us-gov-west-1.s3-us-gov-west-1.amazonaws.com/latest/install
```

### Sample application locations

Location of sample CodeDeploy applications:

- Amazon Linux, Red Hat Enterprise Linux, and Ubuntu Server instances:

```
 https://s3-us-gov-west-1.amazonaws.com/aws-codedeploy-us-gov-west-1/samples/latest/SampleApp_Linux.zip
```

- Windows Server instances:

```
 https://s3-us-gov-west-1.amazonaws.com/aws-codedeploy-us-gov-west-1/samples/latest/SampleApp_Windows.zip
```

### CloudFormation template location

Location of CloudFormation template for launching Amazon EC2 instance configured for CodeDeploy deployments:

```
 https://s3-us-gov-west-1.amazonaws.com/aws-codedeploy-us-gov-west-1/templates/latest/CodeDeploy_SampleCF_Template.json
```

### Downloading CodeDeploy installer and updater (Windows Server)

Links for downloading CodeDeploy installer and updater for Windows Server instances:

- Installer:

```
 https://aws-codedeploy-us-gov-west-1.s3-us-gov-west-1.amazonaws.com/latest/codedeploy-agent.msi
```

- Updater:

```
 https://aws-codedeploy-us-gov-west-1.s3-us-gov-west-1.amazonaws.com/latest/codedeploy-agent-updater.msi
```

For more information about AWS CodeDeploy, see the [AWS CodeDeploy documentation](https://aws.amazon.com/documentation/codedeploy/ "https://aws.amazon.com/documentation/codedeploy/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- **Application Details:**
  - Name

- **Deployment Groups:**
  - Deployment group name
  - Service Role name
  - EC2 Auto Scaling group names
  - EC2 instance tag key
  - EC2 instance tag group name
  - On-premise Instances tag key
  - On-premise Instances tag group
  - Load Balancer ALB target group
  - Load Balancer NLB target group
  - Deployment trigger name
  - Deployment trigger SNS Topic
  - Deployment CloudWatch alarms

- **Deployment Configuration:**
  - Deployment configuration name
  - Deployment description
