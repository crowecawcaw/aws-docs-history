# Automation assume role

The automation assume role is the role Automation assumes when it runs the
runbook that onboards an Azure virtual machine as a managed node. The role
can call the core Systems Manager APIs needed for hybrid activation. It can also pass a
service role to Systems Manager and assume the Azure federation role to obtain Azure
credentials.

**Role name pattern:**
`SSM-AzureAssumeRole-`connector-name``

The trust policy lets the Systems Manager service principal assume the role, scoped
to your AWS account. Replace `123456789012` with your
AWS account ID.

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

The permissions policy grants the actions Automation needs to execute the
onboarding runbooks. Replace `123456789012` with your
AWS account ID, `us-east-1` with the AWS Region that the Cloud
Connector is created in, `SSM-AzureRole-MyConnector`
with the name of the Azure federation role,
`AmazonEC2RunCommandRoleForManagedInstances` with the name of
the managed instance role attached to the Cloud Connector, and
`connector-id` with the ID of the Cloud Connector.

**Permissions details**

This policy includes the following permissions.

- `ssm` – Allows Automation to create, delete, and
  describe hybrid activations
  (`CreateActivation`, `DeleteActivation`,
  `DescribeActivations`); to register Azure virtual machines
  as managed nodes and read their status
  (`DescribeInstanceInformation`); to tag activations and
  managed instances (`AddTagsToResource`); to read the
  installation runbook (`GetDocument` on
  `AWS-InstallSSMAgentOnAzure`); and to read the Cloud
  Connector configuration (`GetCloudConnector`).
- `iam:PassRole` – Allows Automation to pass the
  managed instance role to Systems Manager when registering an Azure virtual
  machine. The `iam:PassedToService` condition restricts
  the pass to `ssm.amazonaws.com`.
- `iam:ListRoleTags` – Allows Automation to read
  tags on the Azure federation role to confirm it belongs to the same
  Cloud Connector before assuming it.
- `sts:AssumeRole` – Allows Automation to assume the
  Azure federation role to obtain Azure credentials.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "arn:aws:iam::123456789012:role/service-role/SSM-AzureRole-MyConnector"
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
                "arn:aws:ssm:us-east-1:*:document/AWS-InstallSSMAgentOnAzure"
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
