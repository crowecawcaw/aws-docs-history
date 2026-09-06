

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Azure federation role
<a name="cloud-connector-azure-federation-role"></a>

The Azure federation role lets Systems Manager obtain a web identity token from AWS Security Token Service (AWS STS) and exchange it for Azure credentials through OIDC federation. Automation assumes this role during runbook execution to authenticate to your Azure tenant. The Systems Manager service also assumes this role directly to validate the Cloud Connector before any State Manager association exists.

**Role name pattern:** `SSM-AzureRole-{{connector-name}}`

The trust policy includes two statements:
+ The first statement lets the customer's AWS account assume the role, but only when the calling principal is the automation assume role or the automation dispatch role (matched by the `aws:PrincipalArn` condition) and that principal is tagged with `caller=SSM`. The principal-ARN match requires the assume role and the dispatch role to live under the `/service-role/` IAM path.
+ The second statement lets the Systems Manager service principal assume the role directly. The `aws:SourceAccount` and `aws:SourceArn` conditions provide confused-deputy protection by restricting the trust to your AWS account and to a Cloud Connector ARN.

Replace `123456789012` with your AWS account ID.

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Principal": {
                "AWS": "arn:aws:iam::123456789012:root"
            },
            "Condition": {
                "StringEquals": {
                    "aws:PrincipalTag/caller": "SSM"
                },
                "ArnLike": {
                    "aws:PrincipalArn": [
                        "arn:aws:iam::123456789012:role/service-role/SSM-AzureAssumeRole*",
                        "arn:aws:iam::123456789012:role/service-role/SSM-AzureDispatchRole*"
                    ]
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Principal": {
                "Service": "ssm.amazonaws.com"
            },
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "123456789012"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:ssm:*:123456789012:cloud-connector/*"
                }
            }
        }
    ]
}
```

The permissions policy lets the role obtain a web identity token whose audience is restricted to `api://AzureADTokenExchange`, which is the audience that Microsoft Entra ID requires for OIDC federation.

**Permissions details**

This policy includes the following permissions.
+ `sts:GetWebIdentityToken` – Allows the role to obtain a web identity token from AWS STS that Systems Manager can present to Microsoft Entra ID to exchange for Azure credentials.
+ `sts:TagGetWebIdentityToken` – Allows Systems Manager to add identity tags (such as the connector ID) to the issued web identity token. This lets you scope Microsoft Entra ID federation rules to a specific Cloud Connector.

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:GetWebIdentityToken",
                "sts:TagGetWebIdentityToken"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "sts:IdentityTokenAudience": [
                        "api://AzureADTokenExchange"
                    ]
                }
            }
        }
    ]
}
```