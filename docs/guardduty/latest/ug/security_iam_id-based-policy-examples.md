

# Identity-based policy examples for Amazon GuardDuty
<a name="security_iam_id-based-policy-examples"></a>

By default, users and roles don't have permission to create or modify GuardDuty resources. To grant users permission to perform actions on the resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy documents, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*.

For details about actions and resource types defined by GuardDuty, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon GuardDuty](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonguardduty.html) in the *Service Authorization Reference*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices)
+ [Using the GuardDuty console](#security_iam_id-based-policy-examples-console)
+ [Permissions required to enable GuardDuty](#guardduty_enable-permissions)
+ [Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions)
+ [Custom IAM policy to grant read-only access to GuardDuty](#security_iam_id-based-policy-examples-custom-readonly)
+ [Deny Access to GuardDuty findings](#security_iam_id-based-policy-examples-deny-findings)
+ [Using a custom IAM policy to limit access to GuardDuty resources](#security_iam_id-based-policy-examples-guardduty_restrict_access_to_resources)

## Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete GuardDuty resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

## Using the GuardDuty console
<a name="security_iam_id-based-policy-examples-console"></a>

To access the Amazon GuardDuty console, you must have a minimum set of permissions. These permissions must allow you to list and view details about the GuardDuty resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match the API operation that they're trying to perform.

To ensure that users and roles can still use the GuardDuty console, also attach the GuardDuty `ConsoleAccess` or `ReadOnly` AWS managed policy to the entities. For more information, see [Adding permissions to a user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

## Permissions required to enable GuardDuty
<a name="guardduty_enable-permissions"></a>

To grant permissions that various IAM identities (users, groups, and roles) must have, attach the required [AWS managed policy: AmazonGuardDutyFullAccess\_v2 (recommended)](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonGuardDutyFullAccess-v2) policy to enable GuardDuty.

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

## Custom IAM policy to grant read-only access to GuardDuty
<a name="security_iam_id-based-policy-examples-custom-readonly"></a>

To grant read-only access to GuardDuty you can use the `AmazonGuardDutyReadOnlyAccess` managed policy. 

To create a custom policy that grants an IAM role, user, or group read-only access to GuardDuty, you can use the following statement:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "guardduty:ListMembers",
                "guardduty:GetMembers",
                "guardduty:ListInvitations",
                "guardduty:ListDetectors",
                "guardduty:GetDetector",
                "guardduty:ListFindings",
                "guardduty:GetFindings",
                "guardduty:ListIPSets",
                "guardduty:GetIPSet",
                "guardduty:ListThreatIntelSets",
                "guardduty:GetThreatIntelSet",
                "guardduty:GetMasterAccount",
                "guardduty:GetInvitationsCount",
                "guardduty:GetFindingsStatistics",
                "guardduty:DescribeMalwareScans",
                "guardduty:UpdateMalwareScanSettings",
                "guardduty:GetMalwareScanSettings"
            ],
            "Resource": "*"
        }
    ]
}
```

------

## Deny Access to GuardDuty findings
<a name="security_iam_id-based-policy-examples-deny-findings"></a>

You can use the following policy to deny an IAM role, user, or group access to GuardDuty findings. Users can't view findings or the details about findings, but they can access all other GuardDuty operations:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "guardduty:CreateDetector",
                "guardduty:DeleteDetector",
                "guardduty:UpdateDetector",
                "guardduty:GetDetector",
                "guardduty:ListDetectors",
                "guardduty:CreateIPSet",
                "guardduty:DeleteIPSet",
                "guardduty:UpdateIPSet",
                "guardduty:GetIPSet",
                "guardduty:ListIPSets",
                "guardduty:CreateThreatIntelSet",
                "guardduty:DeleteThreatIntelSet",
                "guardduty:UpdateThreatIntelSet",
                "guardduty:GetThreatIntelSet",                      
                "guardduty:ListThreatIntelSets",
                "guardduty:ArchiveFindings",
                "guardduty:UnarchiveFindings",
                "guardduty:CreateSampleFindings",
                "guardduty:CreateMembers",
                "guardduty:InviteMembers",
                "guardduty:GetMembers",
                "guardduty:DeleteMembers",
                "guardduty:DisassociateMembers",
                "guardduty:StartMonitoringMembers",
                "guardduty:StopMonitoringMembers",
                "guardduty:ListMembers",
                "guardduty:GetMasterAccount",
                "guardduty:DisassociateFromMasterAccount",
                "guardduty:AcceptAdministratorInvitation",
                "guardduty:ListInvitations",
                "guardduty:GetInvitationsCount",
                "guardduty:DeclineInvitations",
                "guardduty:DeleteInvitations"
            ],
            "Resource": "*"
        }, 
         {
            "Effect": "Allow",
            "Action": [
                "iam:CreateServiceLinkedRole"
            ],
            "Resource": "arn:aws:iam::123456789012:role/aws-service-role/guardduty.amazonaws.com/AWSServiceRoleForAmazonGuardDuty",
            "Condition": {
                "StringLike": {
                    "iam:AWSServiceName": "guardduty.amazonaws.com"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:PutRolePolicy",
                "iam:DeleteRolePolicy"
            ],
            "Resource": "arn:aws:iam::123456789012:role/aws-service-role/guardduty.amazonaws.com/AWSServiceRoleForAmazonGuardDuty"
        }
    ]
}
```

------

## Using a custom IAM policy to limit access to GuardDuty resources
<a name="security_iam_id-based-policy-examples-guardduty_restrict_access_to_resources"></a>

To define a user's access to GuardDuty based on the detector ID, you can use all [GuardDuty API actions](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Operations.html) in your custom IAM policies, **except** the following operations:
+ `guardduty:CreateDetector`
+ `guardduty:DeclineInvitations`
+ `guardduty:DeleteInvitations`
+ `guardduty:GetInvitationsCount`
+ `guardduty:ListDetectors`
+ `guardduty:ListInvitations`

Use the following operations in an IAM policy to define a user's access to GuardDuty based on the IPSet ID and ThreatIntelSet ID:
+ `guardduty:DeleteIPSet`
+ `guardduty:DeleteThreatIntelSet`
+ `guardduty:GetIPSet`
+ `guardduty:GetThreatIntelSet`
+ `guardduty:UpdateIPSet`
+ `guardduty:UpdateThreatIntelSet`

The following examples show how to create policies using some of the preceding operations:
+ This policy allows a user to run the `guardduty:UpdateDetector` operation, using the detector ID of 1234567 in the us-east-1 Region: 

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "guardduty:UpdateDetector"
              ],
              "Resource": "arn:aws:guardduty:us-east-1:{{123456789012}}:detector/{{1234567}}"
          }
      ]
  }
  ```

------
+ This policy allows a user to run the `guardduty:UpdateIPSet` operation, using the detector ID of 1234567 and the IPSet ID of 000000 in the us-east-1 Region:
**Note**  
Make sure that the user has the permissions required to access trusted IP lists and threat lists in GuardDuty. For more information, see [Setting up prerequisites for entity lists and IP address lists](guardduty-lists-prerequisites.md).

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "guardduty:UpdateIPSet"
              ],
              "Resource": "arn:aws:guardduty:us-east-1:{{123456789012}}:detector/{{1234567}}/ipset/{{000000}}"
          }
      ]
  }
  ```

------
+ This policy allows a user to run the `guardduty:UpdateIPSet` operation, using any detector ID and the IPSet ID of 000000 in the us-east-1 Region:
**Note**  
Make sure that the user has the permissions required to access trusted IP lists and threat lists in GuardDuty. For more information, see [Setting up prerequisites for entity lists and IP address lists](guardduty-lists-prerequisites.md).

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "guardduty:UpdateIPSet"
              ],
              "Resource": "arn:aws:guardduty:us-east-1:{{123456789012}}:detector/*/ipset/{{000000}}"
          }
      ]
  }
  ```

------
+ This policy allows a user to run the `guardduty:UpdateIPSet` operation, using their detector ID and any IPSet ID in the us-east-1 Region:
**Note**  
Make sure that the user has the permissions required to access trusted IP lists and threat lists in GuardDuty. For more information, see [Setting up prerequisites for entity lists and IP address lists](guardduty-lists-prerequisites.md).

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "guardduty:UpdateIPSet"
              ],
              "Resource": "arn:aws:guardduty:us-east-1:{{123456789012}}:detector/{{1234567}}/ipset/{{*}}"
          }
      ]
  }
  ```

------

The IAM resource ARN for a GuardDuty action matches that action's API resource path. Most actions map to the detector or a sub-resource. For example, `guardduty:GetDetector` uses `detector/detectorId`, and `guardduty:GetFilter` uses `detector/detectorId/filter/filterName`.

Most findings and member actions append the operation name as a suffix on the resource path. The list operations are the exception: `guardduty:ListFindings` and `guardduty:ListMembers` use the base `findings` and `member` paths with no suffix. Include the full path when you scope a policy to these actions:
+ `guardduty:GetFindings` uses `detector/detectorId/findings/get`
+ `guardduty:GetFindingsStatistics` uses `detector/detectorId/findings/statistics`
+ `guardduty:ArchiveFindings` uses `detector/detectorId/findings/archive`
+ `guardduty:GetMembers` uses `detector/detectorId/member/get`
+ `guardduty:ListFindings` uses `detector/detectorId/findings` (no suffix)
+ `guardduty:ListMembers` uses `detector/detectorId/member` (no suffix)

The following policy grants `guardduty:GetFindings` on a specific detector in the us-east-1 Region, using the full resource path:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [{
    "Effect": "Allow",
    "Action": "guardduty:GetFindings",
    "Resource": "arn:aws:guardduty:us-east-1:111122223333:detector/{{a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6}}/findings/get"
  }]
}
```