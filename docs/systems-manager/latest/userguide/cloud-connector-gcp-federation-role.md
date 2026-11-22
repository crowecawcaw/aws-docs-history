

# GCP federation role

The GCP federation role lets Systems Manager obtain a web identity token from AWS Security Token Service (AWS STS) and exchange it for GCP credentials through OIDC federation. Automation assumes this role during runbook execution to authenticate to your GCP environment. Systems Manager also assumes this role directly to validate the Cloud Connector before any State Manager association exists.

**Role name pattern:** `SSM-GCPRole-{{connector-name}}`

The trust policy includes the following statements:
+ The first statement lets your AWS account assume the role, but only when the calling principal is the automation assume role or the automation dispatch role (matched by the `aws:PrincipalArn` condition) and that principal is tagged with `caller=SSM`. The principal-ARN match requires the assume role and the dispatch role to live under the `/service-role/` IAM path.
+ The second statement lets the Systems Manager service principal assume the role directly. The `aws:SourceAccount` and `aws:SourceArn` conditions provide confused-deputy protection by restricting the trust to your AWS account and to a Cloud Connector ARN.
+ If you chose roles under **Additional trusted roles**, a third statement lets those roles assume the federation role. It names each role by its ARN, and its `aws:PrincipalArn` conditions accept only those roles, and only in your AWS account.

Replace `123456789012` with your AWS account ID.

```json
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
                        "arn:aws:iam::123456789012:role/service-role/SSM-GCPAssumeRole*",
                        "arn:aws:iam::123456789012:role/service-role/SSM-GCPDispatchRole*"
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

If you chose roles under **Additional trusted roles**, the trust policy also includes the following statement, which lists the ARN of each role that you chose (here, `MyAutomationRole`). To change these roles later, edit the trust policy in IAM, and list each role's ARN in both the `Principal` element and the `StringEquals` condition of this statement.

```json
{
    "Effect": "Allow",
    "Action": "sts:AssumeRole",
    "Principal": {
        "AWS": [
            "arn:aws:iam::123456789012:role/MyAutomationRole"
        ]
    },
    "Condition": {
        "ArnLike": {
            "aws:PrincipalArn": "arn:aws:iam::123456789012:role/*"
        },
        "StringEquals": {
            "aws:PrincipalArn": [
                "arn:aws:iam::123456789012:role/MyAutomationRole"
            ]
        }
    }
}
```

The permissions policy lets the role obtain a web identity token whose audience is restricted to `https://sts.googleapis.com`, the audience that Systems Manager requests for GCP workload identity federation.

**Permissions details**

This policy includes the following permissions:
+ `sts:GetWebIdentityToken` – Allows the role to obtain a web identity token from AWS STS that Systems Manager can present to GCP to exchange for GCP credentials.
+ `sts:TagGetWebIdentityToken` – Allows Systems Manager to add tags to the web identity token. Systems Manager adds the tags of the role that assumed the federation role, such as the automation assume role.

```json
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
                "ForAllValues:StringEquals": {
                    "sts:IdentityTokenAudience": [
                        "https://sts.googleapis.com"
                    ]
                },
                "Null": {
                    "sts:IdentityTokenAudience": "false"
                }
            }
        }
    ]
}
```