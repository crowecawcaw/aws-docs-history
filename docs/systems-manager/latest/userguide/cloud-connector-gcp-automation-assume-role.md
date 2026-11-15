

# Automation assume role
<a name="cloud-connector-gcp-automation-assume-role"></a>

The automation assume role is the role Automation assumes when it runs the runbook that onboards a GCP virtual machine as a managed node. The role can call the core Systems Manager APIs needed for hybrid activation. It can also pass a service role to Systems Manager and assume the GCP federation role to obtain GCP credentials.

**Role name pattern:** `SSM-GCPAssumeRole-{{connector-name}}`

The trust policy lets the Systems Manager service principal assume the role, scoped to your AWS account. Replace `123456789012` with your AWS account ID.

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Principal": {
                "Service": "ssm.amazonaws.com"
            },
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "123456789012"
                }
            }
        }
    ]
}
```

The permissions policy grants the actions Automation needs to execute the onboarding runbooks. Replace `123456789012` with your AWS account ID, `us-east-1` with the AWS Region that the Cloud Connector is created in, `SSM-GCPRole-MyConnector` with the name of the GCP federation role, `SSM-GCPAssumeRole-MyConnector` with the name of the automation assume role, `AmazonEC2RunCommandRoleForManagedInstances` with the name of the managed instance role attached to the Cloud Connector, and `connector-id` with the ID of the Cloud Connector.

**Permissions details**

This policy includes the following permissions:
+ `ssm` – Allows Automation to create, delete, and describe hybrid activations (`CreateActivation`, `DeleteActivation`, `DescribeActivations`); to register GCP virtual machines as managed nodes and read their status (`DescribeInstanceInformation`); to tag activations and managed instances (`AddTagsToResource`); to read the installation runbook and its child runbooks (`GetDocument`); and to read the Cloud Connector configuration (`GetCloudConnector`).
+ `iam:PassRole` – Allows Automation to pass the managed instance role to Systems Manager when registering a GCP virtual machine, and to pass the automation assume role to Automation when it starts a runbook execution. The `iam:PassedToService` condition restricts both passes to `ssm.amazonaws.com`. The `iam:AssociatedResourceARN` condition restricts the automation assume role pass to the `AWS-InstallSSMAgentOnGCP` runbook, its three child runbooks, and automation executions in the connector's AWS Region.
+ `iam:ListRoleTags` – Allows Automation to read tags on the GCP federation role to confirm it belongs to the same Cloud Connector before assuming it.
+ `sts:AssumeRole` – Allows Automation to assume the GCP federation role to obtain GCP credentials.
+ `ssm:StartAutomationExecution` and `ssm:GetAutomationExecution` – Allows Automation to start and monitor executions of the `AWS-InstallSSMAgentOnGCP` runbook and its three child runbooks (`AWS-InstallSSMAgentOnGCP-SetupAndActivation`, `AWS-InstallSSMAgentOnGCP-ApplyOSPolicy`, and `AWS-InstallSSMAgentOnGCP-VerifyVMStatus`) in the connector's AWS Region.

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "arn:aws:iam::123456789012:role/service-role/SSM-GCPRole-MyConnector"
        },
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::123456789012:role/service-role/AmazonEC2RunCommandRoleForManagedInstances",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "ssm.amazonaws.com"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::123456789012:role/service-role/SSM-GCPAssumeRole-MyConnector",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "ssm.amazonaws.com"
                },
                "ArnLike": {
                    "iam:AssociatedResourceARN": [
                        "arn:aws:ssm:us-east-1::document/AWS-InstallSSMAgentOnGCP",
                        "arn:aws:ssm:us-east-1::automation-definition/AWS-InstallSSMAgentOnGCP:$DEFAULT",
                        "arn:aws:ssm:us-east-1::document/AWS-InstallSSMAgentOnGCP-SetupAndActivation",
                        "arn:aws:ssm:us-east-1::automation-definition/AWS-InstallSSMAgentOnGCP-SetupAndActivation:$DEFAULT",
                        "arn:aws:ssm:us-east-1::document/AWS-InstallSSMAgentOnGCP-ApplyOSPolicy",
                        "arn:aws:ssm:us-east-1::automation-definition/AWS-InstallSSMAgentOnGCP-ApplyOSPolicy:$DEFAULT",
                        "arn:aws:ssm:us-east-1::document/AWS-InstallSSMAgentOnGCP-VerifyVMStatus",
                        "arn:aws:ssm:us-east-1::automation-definition/AWS-InstallSSMAgentOnGCP-VerifyVMStatus:$DEFAULT",
                        "arn:aws:ssm:us-east-1:123456789012:automation-execution/*"
                    ]
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:CreateActivation",
                "ssm:DeleteActivation",
                "ssm:DescribeActivations",
                "ssm:DescribeInstanceInformation",
                "iam:ListRoleTags",
                "ssm:AddTagsToResource"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "ssm:GetDocument",
            "Resource": [
                "arn:aws:ssm:us-east-1::document/AWS-InstallSSMAgentOnGCP",
                "arn:aws:ssm:us-east-1::automation-definition/AWS-InstallSSMAgentOnGCP:$DEFAULT",
                "arn:aws:ssm:us-east-1::document/AWS-InstallSSMAgentOnGCP-SetupAndActivation",
                "arn:aws:ssm:us-east-1::automation-definition/AWS-InstallSSMAgentOnGCP-SetupAndActivation:$DEFAULT",
                "arn:aws:ssm:us-east-1::document/AWS-InstallSSMAgentOnGCP-ApplyOSPolicy",
                "arn:aws:ssm:us-east-1::automation-definition/AWS-InstallSSMAgentOnGCP-ApplyOSPolicy:$DEFAULT",
                "arn:aws:ssm:us-east-1::document/AWS-InstallSSMAgentOnGCP-VerifyVMStatus",
                "arn:aws:ssm:us-east-1::automation-definition/AWS-InstallSSMAgentOnGCP-VerifyVMStatus:$DEFAULT"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:StartAutomationExecution",
                "ssm:GetAutomationExecution"
            ],
            "Resource": [
                "arn:aws:ssm:us-east-1::document/AWS-InstallSSMAgentOnGCP",
                "arn:aws:ssm:us-east-1::automation-definition/AWS-InstallSSMAgentOnGCP:$DEFAULT",
                "arn:aws:ssm:us-east-1::document/AWS-InstallSSMAgentOnGCP-SetupAndActivation",
                "arn:aws:ssm:us-east-1::automation-definition/AWS-InstallSSMAgentOnGCP-SetupAndActivation:$DEFAULT",
                "arn:aws:ssm:us-east-1::document/AWS-InstallSSMAgentOnGCP-ApplyOSPolicy",
                "arn:aws:ssm:us-east-1::automation-definition/AWS-InstallSSMAgentOnGCP-ApplyOSPolicy:$DEFAULT",
                "arn:aws:ssm:us-east-1::document/AWS-InstallSSMAgentOnGCP-VerifyVMStatus",
                "arn:aws:ssm:us-east-1::automation-definition/AWS-InstallSSMAgentOnGCP-VerifyVMStatus:$DEFAULT",
                "arn:aws:ssm:us-east-1:123456789012:automation-execution/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "ssm:GetCloudConnector",
            "Resource": "arn:aws:ssm:us-east-1:123456789012:cloud-connector/connector-id"
        }
    ]
}
```