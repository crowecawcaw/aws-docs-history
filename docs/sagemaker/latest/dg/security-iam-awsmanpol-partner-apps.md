

# AWS managed policies for Amazon SageMaker Partner AI Apps
<a name="security-iam-awsmanpol-partner-apps"></a>

These AWS managed policies add permissions required to use Amazon SageMaker Partner AI Apps. The policies are available in your AWS account and are used by execution roles created from the SageMaker AI console.

**Topics**
+ [AWS managed policy: AmazonSageMakerPartnerAppsFullAccess](#security-iam-awsmanpol-AmazonSageMakerPartnerAppsFullAccess)
+ [Amazon SageMaker AI updates to Partner AI Apps managed policies](#security-iam-awsmanpol-partner-apps-updates)

## AWS managed policy: AmazonSageMakerPartnerAppsFullAccess
<a name="security-iam-awsmanpol-AmazonSageMakerPartnerAppsFullAccess"></a>

Allows full administrative access to Amazon SageMaker Partner AI Apps.

**Permissions details**

This AWS managed policy includes the following permissions.
+ `sagemaker` – Gives Amazon SageMaker Partner AI App users permission to:
  + Create, update, and delete applications
  + Access and list available applications
  + Launch application web UIs
  + Connect using the application SDK
+ `aws-marketplace` – Gives SageMaker AI permission to:
  + Create a usage-based Marketplace subscription for the Marketplace product listing associated with the partner-app type
  + Retrieve and search agreement details for verifying a valid agreement exists to use Partner App

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AmazonSageMakerPartnerListAppsPermission",
            "Effect": "Allow",
            "Action": "sagemaker:ListPartnerApps",
            "Resource": "*"
        },
        {
            "Sid": "AmazonSageMakerPartnerAppsPermission",
            "Effect": "Allow",
            "Action": [
                "sagemaker:CreatePartnerAppPresignedUrl",
                "sagemaker:DescribePartnerApp",
                "sagemaker:CallPartnerAppApi"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            },
            "Resource": "arn:aws:sagemaker:*:*:partner-app/*"
        }
    ]
}
```

------

## Amazon SageMaker AI updates to Partner AI Apps managed policies
<a name="security-iam-awsmanpol-partner-apps-updates"></a>

View details about updates to AWS managed policies for Partner AI Apps since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the SageMaker AI [Document history page.](doc-history.md)


| Policy | Version | Change | Date | 
| --- | --- | --- | --- | 
| [AmazonSageMakerPartnerAppsFullAccess](#security-iam-awsmanpol-AmazonSageMakerPartnerAppsFullAccess) – Update to an existing policy | 2 | Added SageMaker AI Partner AI App create, update, and delete permissions.<br />Added AWS Marketplace permissions to create, accept, and search agreements to enable Partner App usage. | July 31, 2026 | 
| AmazonSageMakerPartnerAppsFullAccess - New policy | 1 | Initial policy | January 17, 2025 | 