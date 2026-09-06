

# Manage access to AWS Support Plans
<a name="security-support-plans"></a>

**Topics**
+ [Permissions for the Support Plans console](#using-the-trusted-advisor-console)
+ [Support Plans actions](#support-plans-actions)
+ [Example IAM policies for Support Plans](#support-plans-policies)
+ [Troubleshooting](#troubleshooting-changing-support-plans)

## Permissions for the Support Plans console
<a name="using-the-trusted-advisor-console"></a>

To access the Support Plans console, a user must have a minimum set of permissions. These permissions must allow the user to list and view details about the Support Plans resources in your AWS account.

You can create an AWS Identity and Access Management (IAM) policy with the `supportplans` namespace. You can use this policy to specify permissions for actions and resources.

When you create a policy, you can specify the namespace of the service to allow or deny an action. The namespace for Support Plans is `supportplans`.

You can use AWS managed policies and attach them to your IAM entities. For more information, see [AWS managed policies for AWS Support Plans](managed-policies-aws-support-plans.md).

## Support Plans actions
<a name="support-plans-actions"></a>

You can perform the following Support Plans actions in the console. You can also specify these Support Plans actions in an IAM policy to allow or deny specific actions. 


| Action | Description | 
| --- | --- | 
| `GetSupportPlan` | Grants permission to view details about the current support plan for this AWS account. | 
| `GetSupportPlanUpdateStatus` | Grants permission to view details about the status for a request to update a support plan. | 
| `StartSupportPlanUpdate` | Grants permission to start the request to update the support plan for this AWS account. | 
| `CreateSupportPlanSchedule` | Grants permission to create support plan schedules for this AWS account. | 
| `ListSupportPlanModifiers ` | Grants permission to view a list of all support plan modifiers for this AWS account. | 

## Example IAM policies for Support Plans
<a name="support-plans-policies"></a>

You can use the following example policies to manage access to Support Plans.

### Full access to Support Plans
<a name="full-access-support-plans"></a>

The following policy allows users full access to Support Plans.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "supportplans:*",
            "Resource": "*"
        }
    ]
}
```

------

### Read-only access to Support Plans
<a name="readonly-access-support-plans"></a>

The following policy allows read-only access to Support Plans.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "supportplans:Get*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "supportplans:List*",
            "Resource": "*"
        }
    ]
}
```

------

### Deny access to Support Plans
<a name="deny-access-support-plans"></a>

The following policy doesn't allow users access to Support Plans.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Deny",
            "Action": "supportplans:*",
            "Resource": "*"
        }
    ]
}
```

------

## Troubleshooting
<a name="troubleshooting-changing-support-plans"></a>

See the following topics to manage access to Support Plans.

### When I try to view or change my support plan, the Support Plans console says that I'm missing the `GetSupportPlan` permission
<a name="missing-iam-permission"></a>

IAM users must have the required permissions to access the Support Plans console. You can update your IAM policy to include the missing permission or use an AWS managed policy, such as AWSSupportPlansFullAccess or AWSSupportPlansReadOnlyAccess. For more information, see [AWS managed policies for AWS Support Plans](managed-policies-aws-support-plans.md).

If you don't have access to update your IAM policies, contact your AWS account administrator. 

#### Related information
<a name="related-information-missing-permissions"></a>

For more information, see the following topics in the *IAM User Guide*:
+ [Testing IAM policies with the IAM policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html)
+ [Troubleshooting access denied error messages](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_access-denied.html)

### I have the correct Support Plans permissions, but I still get the same error
<a name="update-the-service-control-policy"></a>

If your AWS account is a member account that's part of AWS Organizations, the service control policy (SCP) might need to be updated. SCPs are a type of policy that manages permissions in an organization.

Because Support Plans is a *global* service, policies that restrict AWS Regions might prevent member accounts from viewing or changing their support plan. To allow global services for your organization, such as IAM and Support Plans, you must add the service to the exclusion list in any applicable SCP. This means that accounts in the organization can access these services, even if the SCP denies a specified AWS Region.

To add Support Plans as an exception, enter `"supportplans:*"` to the `"NotAction"` list in the SCP.

```
"supportplans:*",
```

Your SCP might appear as the following policy snippet.

**Example : SCP that allows Support Plans access in an organization**  

```
{ "Version": "2012-10-17",		 	 	 
   "Statement": [
     { "Sid":  "GRREGIONDENY",
       "Effect":  "Deny",
       "NotAction": [    
         "aws-portal:*",
         "budgets:*",
         "chime:*"
         "iam:*",
         "supportplans:*",
         ....
```

If you have a member account and can't update the SCP, contact your AWS account administrator. The management account might need to update the SCP so that all member accounts can access Support Plans.

**Notes for AWS Control Tower**  
If your organization uses an SCP with AWS Control Tower, you can update the **Deny access to AWS based on the requested AWS Region** control (commonly referred to as the Region deny control).
If you update the SCP for AWS Control Tower to allow `supportplans`, repairing the drift will remove your update to the SCP. For more information, see [Detect and resolve drift in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/drift.html).

#### Related information
<a name="related-information-scps"></a>

For more information, see the following topics:
+ [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *AWS Organizations User Guide.*
+ [Configure the Region deny control](https://docs.aws.amazon.com/controltower/latest/userguide/region-deny.html) in the *AWS Control Tower User Guide*
+ [Deny access to AWS based on the requested AWS Region](https://docs.aws.amazon.com/controltower/latest/userguide/data-residency-controls.html#primary-region-deny-policy) in the *AWS Control Tower User Guide*