# Using an AWS CloudFormation template to run the Neptune Blue/Green solution

You can use AWS CloudFormation to deploy the Neptune Blue/Green solution. The CloudFormation
template creates an Amazon EC2 instance in the same VPC as your blue source Neptune database,
installs the solution there, and runs it. You can monitor its progress in CloudWatch logs, as
explained in [Monitoring progress](neptune-BG-monitoring.md "neptune-BG-monitoring.md").

You can use these links to review the solution template, or select the
**Launch Stack** button to launch it in the AWS CloudFormation console:

|                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [View](https://aws-neptune-customer-samples-us-east-1.s3.amazonaws.com/neptune-bg/bg.yaml "https://aws-neptune-customer-samples-us-east-1.s3.amazonaws.com/neptune-bg/bg.yaml") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?templateURL=https://aws-neptune-customer-samples-us-east-1.s3.amazonaws.com/neptune-bg/bg.yaml "https://console.aws.amazon.com/cloudformation/designer/home?templateURL=https://aws-neptune-customer-samples-us-east-1.s3.amazonaws.com/neptune-bg/bg.yaml") | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=NeptuneBG&templateURL=https://aws-neptune-customer-samples-us-east-1.s3.amazonaws.com/neptune-bg/bg.yaml "https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=NeptuneBG&templateURL=https://aws-neptune-customer-samples-us-east-1.s3.amazonaws.com/neptune-bg/bg.yaml") |

In the console, choose the AWS region where you want to run the solution from the dropdown
at the upper right of the window.

Set the stack parameters as follows:

- **`DeploymentID`**   –  
  An identifier that is unique to each Neptune Blue/Green deployment.

It is used as the green DB cluster identifier, and as a prefix for naming new
resources created during the deployment.

- **`NeptuneSourceClusterId`**   –  
  The identifier of the blue DB cluster that you want to upgrade.
- **`NeptuneTargetClusterVersion:`**   –  
  The [Neptune engine version](engine-releases.md "engine-releases.md") that you want
  to upgrade the blue DB cluster to.

This must be higher than the current blue DB cluster's engine version.

- **`DeploymentMode`**   –  
  Indicates whether this is a new deployment or an attempt to resume a previous
  deployment. When you are using same `DeploymentID` as a previous deployment,
  set `DeploymentMode` to `resume`.

Valid values are: `new` (the default), and `resume`.

- **`GraphQueryType`**   –  
  The graph data type for your database.

Valid values are: `propertygraph` (the default), and `rdf`.

- **`SubnetId`**   –  
  A subnet ID from the same VPC that your blue DB cluster is located in.
  (see [Connecting to a Neptune DB
  Cluster from an Amazon EC2 instance in the same VPC](get-started-connect-ec2-same-vpc.md "get-started-connect-ec2-same-vpc.md")).

Provide the ID of a public subnet if you want to SSH to the instance through
[EC2
Connect](../../../AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.md "../../../AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.md").

- **`InstanceSecurityGroup`**   –  
  A security group for your Amazon EC2 instance.

The security group must have access to your blue DB cluster, and you must
be able to SSH to the instance. See [Create a security group using the VPC console](get-started-vpc.md#security-vpc-security-group "get-started-vpc.md#security-vpc-security-group").
Wait until the stack is complete. As soon as it's done the solution is started.
You can then monitor deployment process using CloudWatch logs as described in the next section.
