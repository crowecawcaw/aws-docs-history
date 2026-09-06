

# Identity-based policy examples for AWS HealthImaging
<a name="security_iam_id-based-policy-examples"></a>

By default, users and roles don't have permission to create or modify HealthImaging resources. To grant users permission to perform actions on the resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy documents, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*.

For details about actions and resource types defined by Awesome, including the format of the ARNs for each of the resource types, see [Actions, Resources, and Condition Keys for AWS Awesome ](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awskeymanagementservice.html) in the *Service Authorization Reference*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices)
+ [Using the HealthImaging console](#security_iam_id-based-policy-examples-console)
+ [Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions)
+ [Granting permissions based on Study Instance UID and Series Instance UID](#security_iam_id-based-policy-examples-study-series-uid)

## Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete HealthImaging resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

## Using the HealthImaging console
<a name="security_iam_id-based-policy-examples-console"></a>

To access the AWS HealthImaging console, you must have a minimum set of permissions. These permissions must allow you to list and view details about the HealthImaging resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match the API operation that they're trying to perform.

To ensure that users and roles can still use the HealthImaging console, also attach the HealthImaging `{{ConsoleAccess}}` or `{{ReadOnly}}` AWS managed policy to the entities. For more information, see [Adding permissions to a user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

## Allow users to view their own permissions
<a name="security_iam_id-based-policy-examples-view-own-permissions"></a>

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## Granting permissions based on Study Instance UID and Series Instance UID
<a name="security_iam_id-based-policy-examples-study-series-uid"></a>

HealthImaging DICOMWeb APIs support granting access to image sets based on the Study Instance UID and Series Instance UID. You can define IAM policies that limit access by adding condition statements with the `StudyInstanceUID` and `SeriesInstanceUID` condition context keys.

HealthImaging DICOMWeb APIs that use `StudyInstanceUID` as a required parameter support IAM policies that limit access based on the `StudyInstanceUID` key. Similarly, HealthImaging DICOMWeb APIs that use `SeriesInstanceUID` as a required parameter support policies with the `SeriesInstanceUID` key.

**HealthImaging APIs that support IAM policies using `StudyInstanceUID` and `SeriesInstanceUID` context keys**


| Name | Support for `StudyInstanceUID` condition | Support for `SeriesInstanceUID` condition | 
| --- | --- | --- | 
| GetDICOMInstance | Yes | Yes | 
| GetDICOMInstanceFrames | Yes | Yes | 
| GetDICOMInstanceMetadata | Yes | Yes | 
| GetDICOMSeriesMetadata | Yes | Yes | 
| GetDICOMBulkdata | Yes | Yes | 
| SearchDICOMSeries | Yes | No | 
| SearchDICOMInstances | Yes | Yes | 
| StoreDICOMStudy | Yes | No | 

**Note**  
A HealthImaging API that does not support this context key will function as if no context key was specified when invoked with a policy that contains a `StudyInstanceUID` or `SeriesInstanceUID` context key.

### Example 1: Granting access based on a StudyInstanceUID
<a name="security_iam_id-based-policy-examples-study-uid"></a>

To grant access only to specific DICOM studies, attach a policy to the role that specifies a condition on the `StudyInstanceUID`.

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Action": [
                "medical-imaging:SearchDICOMSeries"
            ],
            "Resource": [
                "arn:aws:medical-imaging:us-west-2:{{account-id}}:datastore/{{your-datastore-id}}"
            ],
            "Condition": {
                "StringEquals": {
                    "medical-imaging:StudyInstanceUID": "{{your study instance UID}}"
                }
            }
        }
    ]
}
```

When this role is assumed via `sts assume-role`, the caller will only be authorized to access image sets that match the condition specified in the role policy, otherwise the calls will be rejected throwing an `AccessDenied` error. In this case, the caller will be granted access to all image sets having the specified `StudyInstanceUID`.

You can use all IAM string condition operators in your policies, including wildcard matching and multiple matches.

An example policy for wildcard matching:

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Action": [
                "medical-imaging:SearchDICOMSeries"
            ],
            "Resource": [
                "arn:aws:medical-imaging:us-west-2:{{account-id}}:datastore/{{your-datastore-id}}"
            ],
            "Condition": {
                "StringLike": {
                    "medical-imaging:StudyInstanceUID": "123.456.789*"
                }
            }
        }
    ]
}
```

An example policy for multiple matches:

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Action": [
                "medical-imaging:SearchDICOMSeries"
            ],
            "Resource": [
                "arn:aws:medical-imaging:us-west-2:{{account-id}}:datastore/{{your-datastore-id}}"
            ],
            "Condition": {
                "StringEquals": {
                    "medical-imaging:StudyInstanceUID": [
                        "123.456.789",
                        "1.2.3.4.5.6"
                    ]
                }
            }
        }
    ]
}
```

### Example 2: Granting access based on a SeriesInstanceUID
<a name="security_iam_id-based-policy-examples-series-uid"></a>

To grant access only to specific image sets corresponding to a DICOM Series, attach a policy to the role that specifies a condition on the `SeriesInstanceUID`.

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Action": [
                "medical-imaging:SearchDICOMInstances"
            ],
            "Resource": [
                "arn:aws:medical-imaging:us-west-2:{{account-id}}:datastore/{{your-datastore-id}}"
            ],
            "Condition": {
                "StringEquals": {
                    "medical-imaging:SeriesInstanceUID": [
                        "123.456.789",
                        "1.2.3.4.5.6"
                    ]
                }
            }
        }
    ]
}
```

### Example 3: Granting access based on StudyInstanceUIDs and SeriesInstanceUIDs
<a name="security_iam_id-based-policy-examples-study-and-series-uid"></a>

To grant access only to image sets of a particular DICOM Study and Series, attach a policy to the role that specifies conditions on both the `StudyInstanceUID` and `SeriesInstanceUID`.

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Action": [
                "medical-imaging:SearchDICOMInstances"
            ],
            "Resource": [
                "arn:aws:medical-imaging:us-west-2:{{account-id}}:datastore/{{your-datastore-id}}"
            ],
            "Condition": {
                "StringEquals": {
                    "medical-imaging:StudyInstanceUID": ["123.456.789"],
                    "medical-imaging:SeriesInstanceUID": ["1.2.3.4.5.6"]
                }
            }
        }
    ]
}
```