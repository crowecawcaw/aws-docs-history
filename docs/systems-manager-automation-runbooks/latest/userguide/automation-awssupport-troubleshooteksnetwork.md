

# `AWSSupport-TroubleshootEKSNetwork`
<a name="automation-awssupport-troubleshooteksnetwork"></a>

## Description
<a name="automation-awssupport-troubleshooteksnetwork-description"></a>

The `AWSSupport-TroubleshootEKSNetwork` runbook helps you troubleshoot network connectivity issues in containers running in Amazon Elastic Kubernetes Service (Amazon EKS) clusters. The runbook collects compute and networking statistics from the traffic source and the destination, depending on the destination type.

## How it works
<a name="automation-awssupport-troubleshooteksnetwork-how-it-works"></a>

Use this runbook to troubleshoot connectivity to the following destination types:
+ **POD**: Another Kubernetes pod.
+ **SERVICE**: A Kubernetes service.
+ **IP**: An IPv4/IPv6 address, internal or external to the cluster or Amazon VPC.
+ **DNS**: A domain name, internal or external to the cluster or Amazon VPC.

**Important**  
In addition to the following IAM permissions, the AutomationAssumeRole must have access to the Amazon EKS clusters using the [supported Amazon EKS API access methods](https://docs.aws.amazon.com/eks/latest/userguide/grant-k8s-access.html). For clusters using access entries, the `AmazonEKSViewPolicy` access policy is the minimum required policy.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootEKSNetwork) 

## Required IAM permissions
<a name="automation-awssupport-troubleshooteksnetwork-permissions"></a>

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ec2:DescribeInstances`
+ `ec2:DescribeNetworkInterfaces`
+ `ec2:DescribeRegions`
+ `ec2:DescribeRouteTables`
+ `ec2:DescribeSecurityGroups`
+ `ec2:DescribeSubnets`
+ `ec2:DescribeVpcPeeringConnections`
+ `ec2:DescribeVpcs`
+ `eks:DescribeCluster`
+ `eks:DescribeFargateProfile`
+ `s3:GetBucketLocation`
+ `s3:GetObject`
+ `ssm:DescribeAutomationExecutions`
+ `ssm:DescribeAutomationStepExecutions`
+ `ssm:DescribeDocument`
+ `ssm:GetAutomationExecution`
+ `ssm:GetDocument`
+ `ssm:StartAutomationExecution`
+ `sts:GetCallerIdentity`

The following example policy shows the least-privilege permissions required for the `AutomationAssumeRole`. Replace `REGION`, `ACCOUNTID`, `SOURCE_CLUSTER_NAME`, `DESTINATION_CLUSTER_NAME`, and `S3_BUCKET_NAME` with your own values:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EKSClusterAccess",
            "Effect": "Allow",
            "Action": "eks:DescribeCluster",
            "Resource": [
                "arn:aws:eks:{{REGION}}:{{ACCOUNTID}}:cluster/{{SOURCE_CLUSTER_NAME}}",
                "arn:aws:eks:{{REGION}}:{{ACCOUNTID}}:cluster/{{DESTINATION_CLUSTER_NAME}}"
            ]
        },
        {
            "Sid": "EKSFargateProfileAccess",
            "Effect": "Allow",
            "Action": "eks:DescribeFargateProfile",
            "Resource": [
                "arn:aws:eks:{{REGION}}:{{ACCOUNTID}}:fargateprofile/{{SOURCE_CLUSTER_NAME}}/*",
                "arn:aws:eks:{{REGION}}:{{ACCOUNTID}}:fargateprofile/{{DESTINATION_CLUSTER_NAME}}/*"
            ]
        },
        {
            "Sid": "EC2DescribePermissions",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:DescribeRegions",
                "ec2:DescribeRouteTables",
                "ec2:DescribeVpcs",
                "ec2:DescribeVpcPeeringConnections",
                "ec2:DescribeSubnets"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestedRegion": "{{REGION}}"
                }
            }
        },
        {
            "Sid": "SSMAutomationExecution",
            "Effect": "Allow",
            "Action": [
                "ssm:StartAutomationExecution",
                "ssm:GetAutomationExecution",
                "ssm:DescribeAutomationExecutions",
                "ssm:DescribeAutomationStepExecutions"
            ],
            "Resource": "arn:aws:ssm:{{REGION}}:{{ACCOUNTID}}:automation-execution/*"
        },
        {
            "Sid": "SSMDocumentAccess",
            "Effect": "Allow",
            "Action": [
                "ssm:DescribeDocument",
                "ssm:GetDocument"
            ],
            "Resource": [
                "arn:aws:ssm:{{REGION}}:{{ACCOUNTID}}:document/AWSSupport-TroubleshootEKSNetwork",
                "arn:aws:ssm:{{REGION}}:{{ACCOUNTID}}:document/AWSSupport-SetupK8sApiProxyForEKS",
                "arn:aws:ssm:{{REGION}}:{{ACCOUNTID}}:document/AWSSupport-CollectEKSLinuxNodeStatistics",
                "arn:aws:ssm:{{REGION}}:*:document/AWS-RunShellScript"
            ]
        },
        {
            "Sid": "S3TroubleshootingAssets",
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::{{S3_BUCKET_NAME}}/AWSSupport-CollectEKSLinuxNodeStatistics/*"
        },
        {
            "Sid": "S3BucketLocation",
            "Effect": "Allow",
            "Action": "s3:GetBucketLocation",
            "Resource": "arn:aws:s3:::{{S3_BUCKET_NAME}}"
        },
        {
            "Sid": "STSCallerIdentity",
            "Effect": "Allow",
            "Action": "sts:GetCallerIdentity",
            "Resource": "*"
        }
    ]
}
```

This runbook also runs two child runbooks under the same `AutomationAssumeRole`, so that role must also have their permissions:
+ [`AWSSupport-SetupK8sApiProxyForEKS`](automation-awssupport-setupk8sapiproxyforeks.md). This runbook doesn't pass a `LambdaRoleArn` to it, so the child runbook always creates the Lambda execution role, and the role must also have the additional permissions for that case.
+ [`AWSSupport-CollectEKSLinuxNodeStatistics`](automation-awssupport-collectekslinuxnodestatistics.md).

## Instructions
<a name="automation-awssupport-troubleshooteksnetwork-instructions"></a>

1. Open [`AWSSupport-TroubleshootEKSNetwork`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootEKSNetwork/description) in Systems Manager under Documents.

1. Choose **Execute automation**.

1. For the input parameters, enter the following:
   + **AutomationAssumeRole (Optional):**

     The ARN of the IAM role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses your permissions to run this runbook.
   + **S3BucketName (Required):**

     Amazon S3 bucket name for uploading troubleshooting assets.
   + **SourceClusterName (Required):**

     Name of the source Amazon EKS cluster to troubleshoot.
   + **SourcePodName (Required):**

     Name of the source Kubernetes pod initiating the network connection.
   + **SourcePodNamespace (Required):**

     Namespace where the source Kubernetes pod resides.
   + **DestinationType (Required):**

     Type of network connection destination. Valid values: `POD`, `SERVICE`, `IP`, or `DNS`.
   + **ConnectionProtocol (Required):**

     Protocol for network connection. Valid values: `tcp`, `udp`, or `sctp`.
   + **DestinationPort (Required):**

     The port of the network connection's destination.
   + **DestinationClusterName (Optional):**

     The destination Amazon EKS cluster name (required for POD and SERVICE destination types).
   + **DestinationPodName (Optional):**

     The name of the destination Kubernetes pod (required for POD destination type).
   + **DestinationPodNamespace (Optional):**

     Namespace where the destination Kubernetes pod resides (required for POD destination type).
   + **DestinationServiceName (Optional):**

     The name of the destination Kubernetes service (required for SERVICE destination type).
   + **DestinationServiceNamespace (Optional):**

     Namespace where the destination Kubernetes service resides (required for SERVICE destination type).
   + **DestinationIpAddress (Optional):**

     Destination IPv4 or IPv6 address (required for IP destination type).
   + **DestinationDnsName (Optional):**

     Destination DNS name (required for DNS destination type).

1. Choose **Execute**.

1. The automation starts. Monitor the execution status on the **Executions** tab.

1. The document performs the following steps automatically:
   + **`ValidateTroubleshootingParameters`**:

     Verifies the input parameters required for troubleshooting, such as whether the cluster exists.
   + **`SetupAuthProxyForSourceEKSCluster`**:

     Runs the `AWSSupport-SetupK8sApiProxyForEKS` document to set up a Lambda function to make Amazon EKS API calls on the source Amazon EKS cluster.
   + **`BranchOnDestinationProxySetupRequired`**:

     Determines whether to run `SetupK8sApiProxyForEKS` for a destination cluster based on the destination type.
   + **`SetupAuthProxyForDestinationEKSCluster`**:

     If required, runs the `AWSSupport-SetupK8sApiProxyForEKS` document to set up a Lambda function for the destination Amazon EKS cluster.
   + **`CollectSourcePodData`**:

     Collects and validates the source pod's information.
   + **`BranchOnSourcePodComputeEngine`**:

     Branches on whether the source Kubernetes pod runs on Amazon EC2 to collect Linux statistics for the node.
   + **`CollectSourceLinuxNodeStatistics`**:

     If the source pod runs on Amazon EC2, runs the `AWSSupport-CollectEKSLinuxNodeStatistics` document to fetch Linux statistics from the source Kubernetes pod's node.
   + **`CollectDestinationData`**:

     Collects and validates the destination information.
   + **`BranchOnDestinationResults`**:

     Branches on whether the destination Kubernetes pod runs on Amazon EC2 to collect Linux statistics for the node.
   + **`CollectDestinationLinuxNodeStatistics`**:

     If the destination pod runs on Amazon EC2, runs the `AWSSupport-CollectEKSLinuxNodeStatistics` document to fetch Linux statistics from the destination Amazon EKS node.
   + **`CleanupAuthProxyForSourceEKSCluster`**:

     Runs the `AWSSupport-SetupK8sApiProxyForEKS` document using the Cleanup operation to clean up resources created for the source cluster.
   + **`CleanupAuthProxyForDestinationEKSCluster`**:

     If applicable, runs the `AWSSupport-SetupK8sApiProxyForEKS` document using the Cleanup operation to clean up resources created for the destination cluster.
   + **`GenerateReport`**:

     Generates a report for the troubleshooting flow.

1. After the automation completes, review the Outputs section for the execution results.

## References
<a name="automation-awssupport-troubleshooteksnetwork-references"></a>

Systems Manager Automation
+ For more information, see [Run an automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing.html).
+ For more information, see [Set up Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup.html).
+ For more information, see [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/).