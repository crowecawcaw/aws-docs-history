

# AWS managed policies for AWS Systems Manager for SAP
<a name="iam-policies"></a>

To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

 AWS services maintain and update AWS managed policies. You can’t change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won’t break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the **ReadOnlyAccess** AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

## AWS managed policy: AWSSystemsManagerForSAPFullAccess
<a name="security-iam-awsmanpol-awssystemsmanagerforsapfullaccess"></a>

Attach the `AWSSystemsManagerForSAPFullAccess` policy to your IAM identities.

The `AWSSystemsManagerForSAPFullAccess` policy grants full access to Systems Manager for SAP service.

 **Permissions details** 

This policy includes the following permissions.
+  `ssm-sap` – Allows principals full access to Systems Manager for SAP.
+  `iam` – Allows a service-linked role to be created, which is a requirement for using Systems Manager for SAP.
+  `ec2` – Allows Systems Manager for SAP to start or stop an Amazon EC2 instance, if that instance is tagged with the key value pair `SSMForSAPManaged=True`.

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AwsSsmForSapPermissions",
            "Effect": "Allow",
            "Action": [
                "ssm-sap:*"
            ],
            "Resource": "arn:*:ssm-sap:*:*:*"
        },
        {
            "Sid": "AwsSsmForSapServiceRoleCreationPermission",
            "Effect": "Allow",
            "Action": [
                "iam:CreateServiceLinkedRole"
            ],
            "Resource": [
                "arn:aws:iam::*:role/aws-service-role/ssm-sap.amazonaws.com/AWSServiceRoleForAWSSSMForSAP"
            ],
            "Condition": {
                "StringEquals": {
                    "iam:AWSServiceName": "ssm-sap.amazonaws.com"
                }
            }
        },
        {
            "Sid": "Ec2StartStopPermission",
            "Effect": "Allow",
            "Action": [
                "ec2:StartInstances",
                "ec2:StopInstances"
            ],
            "Resource": "arn:aws:ec2:*:*:instance/*",
            "Condition": {
                "StringEqualsIgnoreCase": {
                    "ec2:resourceTag/SSMForSAPManaged": "True"
                }
            }
        }
    ]
}
```

## AWS managed policy: AWSSystemsManagerForSAPReadOnlyAccess
<a name="security-iam-awsmanpol-awssystemsmanagerforsapreadonlyaccess"></a>

Attach the `AWSSystemsManagerForSAPReadOnlyAccess` policy to your IAM identities.

The `AWSSystemsManagerForSAPReadOnlyAccess` policy grants read only access to the Systems Manager for SAP service.

 **Permissions details** 

This policy includes the following permissions.
+  `ssm-sap` – Allows principals read only access to Systems Manager for SAP.

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm-sap:get*",
                "ssm-sap:list*"
            ],
            "Resource": "arn:*:ssm-sap:*:*:*"
        }
    ]
}
```

## Systems Manager for SAP updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Systems Manager for SAP since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the Systems Manager for SAP Document history page.


| Change | Description | Date | 
| --- | --- | --- | 
|  [AWSSSMForSAPServiceLinkedRolePolicy](https://docs.aws.amazon.com/ssm-sap/latest/userguide/slr.html#slr-permissions) – Updated policy | The following permissions have been added to the policy for SAP Configuration Checks which validate the IP address used in a Pacemaker HA Setup:+   `ec2:DescribeVpcs`   | August 1, 2025 | 
|  [AWSSSMForSAPServiceLinkedRolePolicy](https://docs.aws.amazon.com/ssm-sap/latest/userguide/slr.html#slr-permissions) – Updated policy | The following permissions have been added to the policy:+   `ce:ListCostAllocationTags`  <br />+   `ce:UpdateCostAllocationTagsStatus`  <br />+   `ce:ListCostAllocationTagBackfillHistory`  <br />+   `ce:StartCostAllocationTagBackfill`   | July 8, 2025 | 
|  [AWSSSMForSAPServiceLinkedRolePolicy](https://docs.aws.amazon.com/ssm-sap/latest/userguide/slr.html#slr-permissions) – Updated policy | Removed `TagKeys` and `ArnLike` condition for `awsApplication` tag. | May 23, 2025 | 
|  [AWSSSMForSAPServiceLinkedRolePolicy](https://docs.aws.amazon.com/ssm-sap/latest/userguide/slr.html#slr-permissions) – Updated policy | The following permissions have been added to `DescribeInstanceActions` within this policy:+   `ec2:DescribeRouteTables`  <br />+   `ec2:DescribeInstanceTypes`  <br />+   `ec2:DescribeVolumes`  <br />+   `ec2:DescribeInstanceAttribute`  <br />+   `ec2:DescribeSnapshots`  <br />These permissions are required to support new functionality that allows users to run discovery on workloads. | July 8, 2025 | 
|  [AWSSSMForSAPServiceLinkedRolePolicy](https://docs.aws.amazon.com/ssm-sap/latest/userguide/slr.html#slr-permissions) – Updated policy | Activate and backfill cost allocation tags created for SAP applications. | December 20, 2024 | 
|  [AWSSSMForSAPServiceLinkedRolePolicy](https://docs.aws.amazon.com/ssm-sap/latest/userguide/slr.html#slr-permissions) – Updated policy | Updated policy for managing application tags on Amazon EBS volumes. | September 05, 2024 | 
|  [AWSSSMForSAPServiceLinkedRolePolicy](https://docs.aws.amazon.com/ssm-sap/latest/userguide/slr.html#slr-permissions) – Updated policy | Added `ec2:CreateTags`, `ec2:DeleteTags`, `resource-groups:Tag`, and `resource-groups:CreateGroup` actions to the policy.<br />These permissions enable you to create and delete tags on EC2 instances and volumes. These permissions also enable you to create, tag, and delete Systems Manager for SAP resource groups. | August 05, 2024 | 
|  [AWSSystemsManagerForSAPFullAccess](https://docs.aws.amazon.com/ssm-sap/latest/userguide/iam-policies.html#security-iam-awsmanpol-AWSSystemsManagerForSAPFullAccess) – Updated policy | Added `ec2:StartInstances` and `ec2:StopInstances` actions to the policy.<br />These permissions enable you to start or stop an SAP application registered with Systems Manager for SAP. | July 10, 2024 | 
|  [AWSSSMForSAPServiceLinkedRolePolicy](https://docs.aws.amazon.com/ssm-sap/latest/userguide/slr.html#slr-permissions) – Updated policy | Added `ec2:StartInstances` and `ec2:StopInstances` actions to the policy.<br />These permissions enable you to start or stop an SAP application registered with Systems Manager for SAP. | April 26, 2024 | 
|  [AWSSSMForSAPServiceLinkedRolePolicy](https://docs.aws.amazon.com/ssm-sap/latest/userguide/slr.html#slr-permissions) – Updated policy | Added AWS Resource Group actions to the policy. | November 21, 2023 | 
|  [AWSSSMForSAPServiceLinkedRolePolicy](https://docs.aws.amazon.com/ssm-sap/latest/userguide/slr.html#slr-permissions) – Updated policy | Added Systems Manager action to the policy. | November 17, 2023 | 
|  [AWSSSMForSAPServiceLinkedRolePolicy](https://docs.aws.amazon.com/ssm-sap/latest/userguide/slr.html#slr-permissions) – Updated policy | Added Amazon EC2 and Systems Manager actions to the policy. | October 27, 2023 | 
|  [AWSSSMForSAPServiceLinkedRolePolicy](https://docs.aws.amazon.com/ssm-sap/latest/userguide/slr.html#slr-permissions) – Updated policy | Added AWS Service Catalog and AWS Resource Group actions to the policy. | July 25, 2023 | 
|  [AWSSSMForSAPServiceLinkedRolePolicy](https://docs.aws.amazon.com/ssm-sap/latest/userguide/slr.html#slr-permissions) – Updated policy | Added the `PutMetricData` Amazon CloudWatch action to the policy. | January 05, 2023 | 
|  [AWSSystemsManagerForSAPFullAccess](https://docs.aws.amazon.com/ssm-sap/latest/userguide/iam-policies.html#security-iam-awsmanpol-AWSSystemsManagerForSAPFullAccess) – Updated policy | Updated the `"arn:aws:iam::*:role/aws-service-role/ssm-sap.amazonaws.com/AWSServiceRoleForAWSSSMForSAP"` resource in policy. | November 18, 2022 | 
|  [AWSSystemsManagerForSAPFullAccess](https://docs.aws.amazon.com/ssm-sap/latest/userguide/iam-policies.html#security-iam-awsmanpol-AWSSystemsManagerForSAPFullAccess) – New policy made available at launch |  **AWSSystemsManagerForSAPFullAccess** grants an IAM user account full access to Systems Manager for SAP service. | November 15, 2022 | 
|  [AWSSystemsManagerForSAPReadOnlyAccess](https://docs.aws.amazon.com/ssm-sap/latest/userguide/iam-policies.html#security-iam-awsmanpol-AWSSystemsManagerForSAPReadOnlyAccess) – New policy made available at launch |  **AWSSystemsManagerForSAPReadOnlyAccess** grants an IAM user account read only access to Systems Manager for SAP service. | November 15, 2022 | 
|  [AWSSSMForSAPServiceLinkedRolePolicy](https://docs.aws.amazon.com/ssm-sap/latest/userguide/slr.html#slr-permissions) – New policy made available at launch | The **AWSSSMForSAPServiceLinkedRolePolicy** service-linked role policy provides access to Systems Manager for SAP. | November 15, 2022 | 
| Systems Manager for SAP started tracking changes | Systems Manager for SAP started tracking changes for its AWS managed policies. | November 15, 2022 | 