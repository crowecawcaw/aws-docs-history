

# Using Amazon EventBridge Managed Rules in AMS
<a name="how-event-router-works"></a>

 AMS Accelerate uses Amazon EventBridge Managed Rules. A Managed Rule is a unique type of rule that is directly linked to AMS. These rules match incoming events and send them to targets for processing. Managed Rules are predefined by AMS and include event patterns that are required by the service to manage customer accounts, and unless defined otherwise, only the owning service can utilize these Managed Rules. 

 AMS Accelerate Managed Rules are linked to `events.managedservices.amazonaws.com` service principal. These Managed Rules are managed through the [`AWSServiceRoleForManagedServices_Events` service-linked role](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/using-service-linked-roles.html#slr-evb-rule). To delete these rules a special confirmation by the customer is required. For more information see [Deleting Managed Rules for AMS](#delete-managed-rules). 

 For more information about rules, see [Rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) in the *Amazon EventBridge User Guide*. 

## Amazon EventBridge Managed Rules deployed by AMS
<a name="managed-rules-deployed"></a>


**Amazon EventBridge Managed Rules**  

| Rule Name | Description | Definition | 
| --- | --- | --- | 
| AmsAccessRolesRule | This rule listens for modifications in specific AMS Accelerate roles and policies. | <pre><br />{<br />   "source": ["aws.iam"],<br />   "detail-type": ["AWS API Call via CloudTrail"],<br />   "detail": {<br />     "eventName": [<br />        "DeleteRole",<br />        "DeletePolicy",<br />        "CreatePolicyVersion",<br />        "AttachRolePolicy",<br />        "DetachRolePolicy"<br />     ],<br />     "requestParameters": {<br />        "$or": [<br />            {<br />                "roleName": [<br />                    "ams-access-admin",<br />                    "ams-access-admin-operations",<br />                    "ams-access-operations",<br />                    "ams-access-read-only",<br />                    "ams-access-security-analyst",<br />                    "ams-access-security-analyst-read-only"<br />                ]<br />            },<br />            {<br />                "policyArn": [<br />                    "arn:*:iam::*:policy/ams-access-allow-pass-role",<br />                    "arn:*:iam::*:policy/ams-access-deny-cloudshell-policy",<br />                    "arn:*:iam::*:policy/ams-access-deny-operations-policy",<br />                    "arn:*:iam::*:policy/ams-access-deny-update-iam-policy",<br />                    "arn:*:iam::*:policy/ams-access-ssr-policy",<br />                    "arn:*:iam::*:policy/ams-access-security-analyst-read-only-policy",<br />                    "arn:*:iam::*:policy/ams-access-security-analyst-policy",<br />                    "arn:*:iam::*:policy/ams-access-security-analyst-extended-policy",<br />                    "arn:*:iam::*:policy/ams-access-admin-policy",<br />                    "arn:*:iam::*:policy/ams-access-admin-operations-policy"<br />                ]<br />            },<br />         ]<br />       },<br />   },<br />}<br />                            </pre> | 
| AMSCoreRule | This rule forwards AWS Config and Amazon CloudWatch events to AMS Config remediation and AMS monitoring services respectfully. The AWS Config events create and resolve AWS Systems Manager OpsItems. The Amazon CloudWatch events monitor CloudWatch Alarms. | <pre><br />{<br />    {<br />        "source": ["aws.config", "aws.cloudwatch"],<br />        "detail-type": ["Config Rules Compliance Change", "CloudWatch Alarm State Change"],<br />    }<br />}<br />                    </pre> | 

## Creating Managed Rules for AMS
<a name="create-managed-rules"></a>

You don’t need to manually create Amazon EventBridge Managed Rules. When you onboard to AMS in the AWS Management Console, the AWS CLI, or the AWS API, AMS creates them for you.

## Editing Managed Rules for AMS
<a name="edit-managed-rules"></a>

AMS doesn't allow you to edit the Managed Rules. Name and event pattern for each Managed Rule are predefined by AMS.

## Deleting Managed Rules for AMS
<a name="delete-managed-rules"></a>

You don’t need to manually delete the Managed Rules. When you offboard from AMS in the AWS Management Console, the AWS CLI, or the AWS API, AMS cleans up the resources and deletes all Managed Rules owned by AMS for you.

 In the event AMS fails to remove the Managed Rules during offboarding, you can also use the Amazon EventBridge console, the AWS CLI or the AWS API to manually delete the Managed Rules. To do this, you must first offboard from AMS and conduct a force delete of the Managed Rules. 