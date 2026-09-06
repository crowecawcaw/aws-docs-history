

# `AWSSupport-TroubleshootEKSDNSFailure`
<a name="automation-awssupport-troubleshooteksdnsfailure"></a>

 **Description** 

The `AWSSupport-TroubleshootEKSDNSFailure` runbook helps troubleshoot issues with CoreDNS pods and configuration in Amazon Elastic Kubernetes Service (Amazon EKS) when applications or pods encounter DNS resolution failures. The runbook validates VPC DNS settings, inspects the CoreDNS deployment and ConfigMap, checks Horizontal Pod Autoscaler (HPA) configuration, collects CoreDNS logs, and performs DNS resolution checks on worker nodes. Optionally, a probing Amazon Elastic Compute Cloud instance can be created in the same subnet as the problematic worker node to perform DNS resolution checks without requiring direct access to the node.

**Important**  
The Amazon EKS cluster's authentication mode must be set to `API` or `API_AND_CONFIG_MAP`. This runbook deploys a AWS Lambda (Lambda) function as a proxy to make authenticated Kubernetes API calls and cleans up all created resources at the end of execution.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootEKSDNSFailure) 

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: AWS::IAM::Role::Arn

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ EksClusterName

  Type: String

  Description: (Required) The name of the target Amazon EKS cluster.
+ DnsName

  Type: String

  Default: amazon.com

  Description: (Optional) The stub domain suffix for the domain name that the application or pod is failing to resolve.
+ ProblematicNodeInstanceId

  Type: AWS::EC2::Instance::Id

  Description: (Optional) The instance ID of the worker node where the application experiencing DNS resolution errors is running. When provided, the runbook creates a probing Amazon EC2 instance in the same subnet to perform DNS resolution checks. Use this parameter if the worker node is not in a public subnet or if installing `bind-utils` on the worker node is not permitted.
+ CoreDnsNamespace

  Type: String

  Default: kube-system

  Description: (Optional) The Kubernetes namespace for CoreDNS pods.
+ S3BucketName

  Type: AWS::S3::Bucket::Name

  Description: (Optional) The name of the Amazon Simple Storage Service bucket where CoreDNS troubleshooting logs are uploaded.
+ LambdaRoleArn

  Type: AWS::IAM::Role::Arn

  Description: (Optional) The ARN of the IAM role for the Lambda proxy function. If not provided, the runbook creates a role named `Automation-K8sProxy-Role-<ExecutionId>` with the `AWSLambdaBasicExecutionRole` and `AWSLambdaVPCAccessExecutionRole` managed policies. It is recommended to provide your own role.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `eks:DescribeCluster`
+ `ec2:DescribeVpcs`
+ `ec2:DescribeInstances`
+ `ec2:DescribeSubnets`
+ `ec2:DescribeSecurityGroups`
+ `cloudformation:CreateStack`
+ `cloudformation:DescribeStacks`
+ `cloudformation:DeleteStack`
+ `lambda:InvokeFunction`
+ `s3:GetBucketPublicAccessBlock`
+ `s3:GetBucketAcl`
+ `s3:PutObject`
+ `ssm:DescribeInstanceInformation`
+ `ssm:SendCommand`
+ `ssm:GetCommandInvocation`
+ `ssm:StartAutomationExecution`
+ `ssm:GetAutomationExecution`

 **Document Steps** 

1. `AssertIfTargetClusterExists` - Verifies that the Amazon EKS cluster specified in `EksClusterName` exists and is in the `ACTIVE` state. If the cluster is not found or not active, the runbook skips to `GenerateReport`.

1. `UpdateEksClusterExists` - Sets the internal `eksClusterExists` variable to `true` for use in report generation.

1. `GetVpcDnsSettings` - Retrieves the `enableDnsSupport` and `enableDnsHostnames` settings for the Amazon Virtual Private Cloud associated with the Amazon EKS cluster.

1. `BranchOnVpcDnsSettings` - Checks whether both VPC DNS settings are enabled. If either is disabled, the runbook skips to `GenerateReport`. Otherwise, proceeds to `DeployK8sAuthApisResources`.

1. `DeployK8sAuthApisResources` - Executes `AWSSupport-SetupK8sApiProxyForEKS` to deploy a Lambda function as a proxy for making authenticated Kubernetes API calls to the Amazon EKS cluster.

1. `RetrieveCoreDNSDeployment` - Retrieves information about the CoreDNS deployment, including pod readiness, container status, and the readiness of nodes hosting CoreDNS pods. Also retrieves the CoreDNS cluster IP.

1. `RetrieveAndInspectCoreDNSConfigMap` - Retrieves the CoreDNS ConfigMap from the Amazon EKS cluster and checks for configuration issues, including stub domain settings for the domain specified in `DnsName`.

1. `ValidateHpaConfiguration` - Checks whether a Horizontal Pod Autoscaler (HPA) is configured for the CoreDNS deployment in the specified namespace.

1. `CheckS3BucketPublicStatus` - Validates that the Amazon S3 bucket specified in `S3BucketName` does not allow public or anonymous read or write access.

1. `CollectLogToS3` - Collects CoreDNS pod logs and uploads them to the specified Amazon S3 bucket.

1. `BranchOnProblematicNodeInstanceId` - Checks whether `ProblematicNodeInstanceId` is provided and CoreDNS host nodes exist. If both conditions are met, proceeds to `VerifyThatProblematicNodeInstanceBelongsToCluster`. Otherwise, branches to `BranchOnCoreDnsDeployment`.

1. `VerifyThatProblematicNodeInstanceBelongsToCluster` - Confirms that the instance specified in `ProblematicNodeInstanceId` is a worker node in the Amazon EKS cluster.

1. `UpdateProblematicNodeInstanceStanding` - Sets the internal `problematicNodeInstanceStanding` variable to `true`.

1. `GetProblematicInstanceDetails` - Retrieves the AMI ID, instance type, subnet ID, and security group IDs of the problematic worker node for use when creating the probing Amazon EC2 instance.

1. `CreateProbingInfrastructure` - Creates an instance profile and probing Amazon EC2 instance via an AWS CloudFormation stack in the same subnet as the problematic worker node. The stack is named `AWSSupport-TroubleshootEKSDNSFailure-<ExecutionId>`.

1. `GetProbingInstanceId` - Retrieves the probing Amazon EC2 instance ID from the CloudFormation stack outputs.

1. `WaitForProbingInstanceSSMAgentStateToBeOnline` - Waits for the Amazon EC2 Systems Manager Agent on the probing Amazon EC2 instance to report an `Online` status before proceeding.

1. `RetrieveCoreDNSPodsIPFromProblematicNode` - Retrieves the CoreDNS pod IP addresses as seen from the problematic worker node.

1. `PerformDNSResolutionOnProbing``EC2Instance` - Runs DNS resolution checks on the probing Amazon EC2 instance using the cluster IP and CoreDNS pod IP.

1. `DeleteCloudFormationStack` - Deletes the CloudFormation stack that created the probing Amazon EC2 instance and instance profile.

1. `UpdateCfnStackDeleted` - Sets the internal `cfnStackDeleted` variable to `true`.

1. `BranchOnCoreDnsDeployment` - Checks whether `ProblematicNodeInstanceId` was not provided and CoreDNS host nodes exist. If both conditions are met, proceeds to `PerformDNSResolutionOnCoreDnsWorkerNodes`. Otherwise, proceeds to `CleanupK8sAuthenticationInfrastructure`.

1. `BranchOnCoreDnsNodesExistForRunCommandSteps` - Checks whether CoreDNS host nodes exist before running `aws:runCommand` steps. If no nodes exist (for example, when CoreDNS has zero replicas), skips to `CleanupK8sAuthenticationInfrastructure`.

1. `PerformDNSResolutionOnCoreDnsWorkerNodes` - Runs DNS resolution checks directly on the CoreDNS worker nodes using the cluster IP and CoreDNS pod IP.

1. `VerifyNameserverMatchAndKubeProxyLogsAndIPTableEntries` - Verifies that the nameserver IP matches the cluster IP, checks kube-proxy pod access to the API server, and validates kube-dns iptables entries on the CoreDNS worker nodes.

1. `VerifyPPSThrottlingOnENIs` - Checks the DNS packets-per-second (PPS) limit per Elastic Network Interface (ENI) on the CoreDNS worker nodes to identify potential throttling.

1. `UpdateChecksOnNodes` - Sets the internal `checksOnNodes` variable to `true` to indicate that node-level checks were performed.

1. `CleanupK8sAuthenticationInfrastructure` - Executes `AWSSupport-SetupK8sApiProxyForEKS` with the `Cleanup` operation to remove the Lambda proxy function and associated resources created during the automation.

1. `UpdateK8sInfrastructreDeleted` - Sets the internal `K8sInfrastructreDeleted` variable to `true`.

1. `CleanUpAllResources` - Performs a comprehensive cleanup of any remaining resources, including the CloudFormation stack and Lambda proxy function, in case earlier cleanup steps did not complete successfully.

1. `CollectOutputFromAllRunCommandSteps` - Collects and consolidates the output from all `aws:runCommand` steps that were executed during the automation.

1. `GenerateReport` - Compiles the results from all preceding steps into a comprehensive evaluation report covering VPC DNS settings, CoreDNS deployment health, ConfigMap configuration, HPA configuration, log collection status, and DNS resolution check results.

 **Outputs** 

`GenerateReport.EvalReport` - A comprehensive report of all DNS troubleshooting checks performed, including findings and recommended remediation steps.