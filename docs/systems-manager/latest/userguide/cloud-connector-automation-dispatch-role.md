

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Automation dispatch role
<a name="cloud-connector-automation-dispatch-role"></a>

The automation dispatch role is the role State Manager uses when it starts an Automation execution against a Cloud Connector. State Manager passes the automation assume role to Automation through this role. The dispatch role also assumes the Azure federation role directly so State Manager can resolve which Azure virtual machines match a Cloud Connector's targets when an association runs.

**Role name pattern:** `SSM-AzureDispatchRole-{{connector-name}}`

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

The permissions policy grants the actions State Manager needs to dispatch Automation executions to a Cloud Connector's targets. Replace `123456789012` with your AWS account ID, `us-east-1` with the AWS Region that the Cloud Connector is created in, `SSM-AzureAssumeRole-MyConnector` with the name of the automation assume role, `SSM-AzureRole-MyConnector` with the name of the Azure federation role, and `connector-id` with the ID of the Cloud Connector.

**Permissions details**

This policy includes the following permissions.
+ `iam:PassRole` – Allows State Manager to pass the automation assume role to Automation when starting a runbook execution. The `iam:PassedToService` condition restricts the pass to `ssm.amazonaws.com`, and the `iam:AssociatedResourceARN` condition restricts it to the `AWS-InstallSSMAgentOnAzure` runbook and automation executions in the connector's AWS Region.
+ `iam:ListRoleTags` – Allows State Manager to read tags on roles to confirm they belong to the same Cloud Connector before passing or assuming them.
+ `ssm:GetCloudConnector` – Allows State Manager to read the Cloud Connector configuration during target resolution.
+ `ssm:ListCloudConnectors` – Allows State Manager to enumerate Cloud Connectors when resolving association targets.
+ `ssm:DescribeInstanceInformation` – Allows State Manager to read the status of managed nodes registered through the connector to determine which targets are eligible.
+ `ssm:StartAutomationExecution` – Allows State Manager to start an Automation execution of the `AWS-InstallSSMAgentOnAzure` runbook against the connector's targets.
+ `sts:AssumeRole` – Allows State Manager to assume the Azure federation role so it can authenticate to Azure when resolving the connector's targets.

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::123456789012:role/service-role/SSM-AzureAssumeRole-MyConnector",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "ssm.amazonaws.com"
                },
                "ArnLike": {
                    "iam:AssociatedResourceARN": [
                        "arn:aws:ssm:us-east-1:*:document/AWS-InstallSSMAgentOnAzure",
                        "arn:aws:ssm:us-east-1:*:automation-definition/AWS-InstallSSMAgentOnAzure:1",
                        "arn:aws:ssm:us-east-1:123456789012:automation-execution/*"
                    ]
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": "ssm:GetCloudConnector",
            "Resource": "arn:aws:ssm:us-east-1:123456789012:cloud-connector/connector-id"
        },
        {
            "Effect": "Allow",
            "Action": "ssm:StartAutomationExecution",
            "Resource": [
                "arn:aws:ssm:us-east-1:*:document/AWS-InstallSSMAgentOnAzure",
                "arn:aws:ssm:us-east-1:*:automation-definition/AWS-InstallSSMAgentOnAzure:1",
                "arn:aws:ssm:us-east-1:123456789012:automation-execution/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "arn:aws:iam::123456789012:role/service-role/SSM-AzureRole-MyConnector"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:DescribeInstanceInformation",
                "ssm:ListCloudConnectors",
                "iam:ListRoleTags"
            ],
            "Resource": "*"
        }
    ]
}
```