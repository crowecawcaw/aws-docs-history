

# Resource-level permissions in AWS User Notifications
<a name="resource-level-permissions"></a>

*Resource-level permissions* define the AWS resources that you allow assigned entities (users, groups, and roles) to perform actions on. You specify the Amazon Resource Name (ARN) of one or more resources as part of an IAM policy. You can then attach this policy to IAM entities. When the action doesn't act on a named resource or you grant permission to perform the action on all resources, the value for the resource in the policy is a wildcard (\*). 

**Note**  
AWS User Notifications doesn't support *resource-based policies*, which are directly attached to AWS resources. For more information about the differences between policies and permissions, see [Identity-based policies and resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html) in the *IAM User Guide*. 

 For more information about defining resource-level permissions, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*. 

## Supported resource-level permissions for User Notifications API actions
<a name="rlp-table"></a>

This table describes the User Notifications API actions that currently support resource-level permissions, as well as the supported resources for each action, including their ARNs and ARN format. 



- ** Managed Notification Configuration **
  - **API action:** GetManagedNotificationConfiguration / **Resource ARN format:** `arn:aws:notifications::{{accountId}}:managed-notification-configuration/category/{{category-name}}/sub-category/{{sub-category-name}}` / **Example:** `arn:aws:notifications::123456789012:managed-notification-configuration/category/AWS-Health/sub-category/Security`
  - **API action:** ListManagedNotificationConfigurations / **Resource ARN format:** `*` / **Example:** `*`
  - **API action:** AssociateManagedNotificationAccountContact / **Resource ARN format:** `arn:aws:notifications::{{accountId}}:managed-notification-configuration/category/{{category-name}}/sub-category/{{sub-category-name}}` / **Example:** `arn:aws:notifications::123456789012:managed-notification-configuration/category/AWS-Health/sub-category/Security`
  - **API action:** DisassociateManagedNotificationAccountContact / **Resource ARN format:** `arn:aws:notifications::{{accountId}}:managed-notification-configuration/category/{{category-name}}/sub-category/{{sub-category-name}}` / **Example:** `arn:aws:notifications::123456789012:managed-notification-configuration/category/AWS-Health/sub-category/Security`
  - **API action:** DisassociateManagedNotificationAdditionalChannel / **Resource ARN format:** `arn:aws:notifications::{{accountId}}:managed-notification-configuration/category/{{category-name}}/sub-category/{{sub-category-name}}` / **Example:** `arn:aws:notifications::123456789012:managed-notification-configuration/category/AWS-Health/sub-category/Security`
  - **API action:** AssociateManagedNotificationAdditionalChannel / **Resource ARN format:** `arn:aws:notifications::{{accountId}}:managed-notification-configuration/category/{{category-name}}/sub-category/{{sub-category-name}}` / **Example:** `arn:aws:notifications::123456789012:managed-notification-configuration/category/AWS-Health/sub-category/Security`
  - **API action:** ListManagedNotificationChannelAssociations / **Resource ARN format:** `arn:aws:notifications::{{accountId}}:managed-notification-configuration/category/{{category-name}}/sub-category/{{sub-category-name}}` / **Example:** `arn:aws:notifications::123456789012:managed-notification-configuration/category/AWS-Health/sub-category/Security`

- ** Notification Configuration **
  - **API action:** CreateNotificationConfiguration / **Resource ARN format:** `arn:aws:notifications:*:{{accountId}}:configuration/*` / **Example:** `arn:aws:notifications:*:123456789012:configuration/*`
  - **API action:** UpdateNotificationConfiguration / **Resource ARN format:** `arn:aws:notifications::{{accountId}}:configuration/{{configurationId}}` / **Example:** `arn:aws:notifications::123456789012:configuration/a01gkn2k10c7spt0a8x8nj55555`
  - **API action:** DeleteNotificationConfiguration / **Resource ARN format:** `arn:aws:notifications::{{accountId}}:configuration/{{configurationId}}` / **Example:** `arn:aws:notifications::123456789012:configuration/a01gkn2k10c7spt0a8x8nj55555`
  - **API action:** GetNotificationConfiguration / **Resource ARN format:** `arn:aws:notifications::{{accountId}}:configuration/{{configurationId}}` / **Example:** `arn:aws:notifications::123456789012:configuration/a01gkn2k10c7spt0a8x8nj55555`
  - **API action:** ListNotificationConfigurations / **Resource ARN format:** `*` / **Example:** `*`
  - **API action:** AssociateChannel / **Resource ARN format:** `arn:aws:notifications::{{accountId}}:configuration/{{configurationId}}` / **Example:** `arn:aws:notifications::123456789012:configuration/a01gkn2k10c7spt0a8x8nj55555`
  - **API action:** DisassociateChannel / **Resource ARN format:** `arn:aws:notifications::{{accountId}}:configuration/{{configurationId}}` / **Example:** `arn:aws:notifications::123456789012:configuration/a01gkn2k10c7spt0a8x8nj55555`
  - **API action:** ListChannels / **Resource ARN format:** `*` / **Example:** `*`

- ** Event Rule **
  - **API action:** CreateEventRule / **Resource ARN format:** `arn:aws:notifications::{{accountId}}:configuration/{{configurationId}}/rule/*` / **Example:** `arn:aws:notifications::123456789012:configuration/a01gkn2k10c7spt0a8x8nj55555/rule/*`
  - **API action:** UpdateEventRule / **Resource ARN format:** `arn:aws:notifications::{{accountId}}:configuration/{{configurationId}}/rule/{{eventRuleId}}` / **Example:** `arn:aws:notifications::123456789012:configuration/a01gkn2k10c7spt0a8x8nj55555/rule/a01gkn362610da5e7dckrt66666`
  - **API action:** DeleteEventRule / **Resource ARN format:** `arn:aws:notifications::{{accountId}}:configuration/{{configurationId}}/rule/{{eventRuleId}}` / **Example:** `arn:aws:notifications::123456789012:configuration/a01gkn2k10c7spt0a8x8nj55555/rule/a01gkn362610da5e7dckrt66666`
  - **API action:** GetEventRule / **Resource ARN format:** `arn:aws:notifications::{{accountId}}:configuration/{{configurationId}}/rule/{{eventRuleId}}` / **Example:** `arn:aws:notifications::123456789012:configuration/a01gkn2k10c7spt0a8x8nj55555/rule/a01gkn362610da5e7dckrt66666`
  - **API action:** ListEventRules / **Resource ARN format:** `*` / **Example:** `*`

- ** Managed Notification Event **
  - **API action:** GetManagedNotificationEvent / **Resource ARN format:** `arn:aws:notifications::{{accountId}}:managed-notification-configuration/category/{{category-name}}/sub-category/{{sub-category-name}}/event/{{notificationEventId}}` / **Example:** `arn:aws:notifications::123456789012:managed-notification-configuration/category/AWS-Health/sub-category/Security/event/a01gkn2k10c7spt0a8x8nj55555`
  - **API action:** ListManagedNotificationEvents / **Resource ARN format:** `*` / **Example:** `*`

- ** Managed Notification Child Event **
  - **API action:** GetManagedNotificationChildEvent / **Resource ARN format:** `arn:aws:notifications::{{accountId}}:managed-notification-configuration/category/{{category-name}}/sub-category/{{sub-category-name}}/event/{{notificationEventId}}/child-event/{{notificationChildEventId}}` / **Example:** `arn:aws:notifications::123456789012:managed-notification-configuration/category/AWS-Health/sub-category/Security/event/a01gkn2k10c7spt0a8x8nj55555/child-event/b01gaja54v1t6rr10dyshk77777`
  - **API action:** ListManagedNotificationChildEvents / **Resource ARN format:** `*` / **Example:** `*`

- ** Notification Event **
  - **API action:** GetNotificationEvent / **Resource ARN format:** `arn:aws:notifications::region:{{accountId}}:configuration/{{configurationId}}/event/{{notificationEventId}}` / **Example:** `arn:aws:notifications:us-east-1:123456789012:configuration/a01gkn2k10c7spt0a8x8nj55555/event/b01gaja54v1t6rr10dyshk77777`
  - **API action:** ListNotificationEvents / **Resource ARN format:** `*` / **Example:** `*`

- ** Notification Hub **
  - **API action:** RegisterNotificationHub / **Resource ARN format:** `*` / **Example:** `*`
  - **API action:** DeregisterNotificationHub / **Resource ARN format:** `*` / **Example:** `*`
  - **API action:** ListNotificationHubs / **Resource ARN format:** `*` / **Example:** `*`

- ** Email Contacts **
  - **API action:** ActivateEmailContact / **Resource ARN format:** `arn:aws:notifications-contacts::{{accountId}}:emailcontact/{{emailContactId}}` / **Example:** `arn:aws:notifications-contacts::123456789012:emailcontact/02k1g09g`
  - **API action:** CreateEmailContact / **Resource ARN format:** `arn:aws:notifications-contacts::{{accountId}}:emailcontact/{{emailContactId}}` / **Example:** `arn:aws:notifications-contacts::123456789012:emailcontact/02k1g09g`
  - **API action:** DeleteEmailContact / **Resource ARN format:** `arn:aws:notifications-contacts::{{accountId}}:emailcontact/{{emailContactId}}` / **Example:** `arn:aws:notifications-contacts::123456789012:emailcontact/02k1g09g`
  - **API action:** GetEmailContact / **Resource ARN format:** `arn:aws:notifications-contacts::{{accountId}}:emailcontact/{{emailContactId}}` / **Example:** `arn:aws:notifications-contacts::123456789012:emailcontact/02k1g09g`
  - **API action:** ListEmailContacts / **Resource ARN format:** `arn:aws:notifications-contacts::{{accountId}}:emailcontact/{{emailContactId}}` / **Example:** `arn:aws:notifications-contacts::123456789012:emailcontact/02k1g09g`
  - **API action:** ListTagsForResource / **Resource ARN format:** `arn:aws:notifications-contacts::{{accountId}}:emailcontact/{{emailContactId}}` / **Example:** `arn:aws:notifications-contacts::123456789012:emailcontact/02k1g09g`
  - **API action:** SendActivationCode / **Resource ARN format:** `arn:aws:notifications-contacts::{{accountId}}:emailcontact/{{emailContactId}}` / **Example:** `arn:aws:notifications-contacts::123456789012:emailcontact/02k1g09g`
  - **API action:** TagResource / **Resource ARN format:** `arn:aws:notifications-contacts::{{accountId}}:emailcontact/{{emailContactId}}` / **Example:** `arn:aws:notifications-contacts::123456789012:emailcontact/02k1g09g`
  - **API action:** UntagResource / **Resource ARN format:** `arn:aws:notifications-contacts::{{accountId}}:emailcontact/{{emailContactId}}` / **Example:** `arn:aws:notifications-contacts::123456789012:emailcontact/02k1g09g`



## Example 1: Full access
<a name="admin-access-example"></a>

This policy allows a user to call all available API actions.

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
        "notifications:*",
        "notifications-contacts:*"
      ],
      "Resource": "*"
    }
  ]
}
```

------

## Example 2: ReadOnly access
<a name="readonly-access-example"></a>

This policy allows a user to call all get and list API actions.

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
        "notifications:Get*",
        "notifications:List*",
        "notifications-contacts:Get*",
        "notifications-contacts:List*"
        
      ],
      "Resource": "*"
    }
  ]
}
```

------

## Example 3: Deny a user the ability to update a notification configuration
<a name="deny-user-update-example"></a>

This policy denies a user the ability to update a notification configuration.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Deny",
      "Action": [
        "notifications:UpdateNotificationConfiguration"
      ],
      "Resource": "arn:aws:notifications::123456789012:configuration/a01gkn2k10c7spt0a8x8nj55555"
    }
  ]
}
```

------

## Example 4: Allow users to create notification configurations and associate emails with them
<a name="create-ncs-example"></a>

This policy allows users to create notification configurations and associate emails with those configurations.

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
       "iam:CreateServiceLinkedRole",
       "notifications:RegisterNotificationHub",
       "notifications:CreateNotificationConfiguration",
       "notifications:CreateEventRule",
       "notifications:AssociateChannel",
       "notifications-contacts:CreateEmailContact",
       "notifications-contacts:SendActivationCode",
       "notifications-contacts:ActivateEmailContact"
      ],
      "Resource": "*"
    }
  ]
}
```

------

## Example 5: Allow users full create, read, update, and delete access
<a name="crud-example"></a>

This policy allows users full create, read, update, and delete (CRUD) access.

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
      "iam:CreateServiceLinkedRole",
      "notifications:*",
      "notifications-contacts:*"
      ],
      "Resource": "*"
    }
  ]
}
```

------

## Example 6: Full read-write access with explicit actions
<a name="full-readwrite-example"></a>

This policy grants a user full read-write access to AWS User Notifications by listing all individual actions explicitly. This includes user-configured notifications, managed notifications, organizations, and tagging permissions.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "UserNotificationsReadWrite",
      "Effect": "Allow",
      "Action": [
        "iam:CreateServiceLinkedRole",
        "notifications:RegisterNotificationHub",
        "notifications:DeregisterNotificationHub",
        "notifications:ListNotificationHubs",
        "notifications:CreateNotificationConfiguration",
        "notifications:UpdateNotificationConfiguration",
        "notifications:GetNotificationConfiguration",
        "notifications:DeleteNotificationConfiguration",
        "notifications:ListNotificationConfigurations",
        "notifications:CreateEventRule",
        "notifications:UpdateEventRule",
        "notifications:GetEventRule",
        "notifications:DeleteEventRule",
        "notifications:ListEventRules",
        "notifications:AssociateChannel",
        "notifications:DisassociateChannel",
        "notifications:ListChannels",
        "notifications:GetNotificationEvent",
        "notifications:ListNotificationEvents",
        "notifications:GetManagedNotificationConfiguration",
        "notifications:ListManagedNotificationConfigurations",
        "notifications:ListManagedNotificationChannelAssociations",
        "notifications:AssociateManagedNotificationAccountContact",
        "notifications:DisassociateManagedNotificationAccountContact",
        "notifications:AssociateManagedNotificationAdditionalChannel",
        "notifications:DisassociateManagedNotificationAdditionalChannel",
        "notifications:GetManagedNotificationEvent",
        "notifications:ListManagedNotificationEvents",
        "notifications:GetManagedNotificationChildEvent",
        "notifications:ListManagedNotificationChildEvents",
        "notifications:EnableNotificationsAccessForOrganization",
        "notifications:DisableNotificationsAccessForOrganization",
        "notifications:AssociateOrganizationalUnit",
        "notifications:DisassociateOrganizationalUnit",
        "notifications:ListOrganizationalUnits",
        "notifications:ListMemberAccounts",
        "notifications:GetNotificationsAccessForOrganization",
        "notifications:TagResource",
        "notifications:ListTagsForResource",
        "notifications:UntagResource",
        "notifications-contacts:CreateEmailContact",
        "notifications-contacts:SendActivationCode",
        "notifications-contacts:ActivateEmailContact",
        "notifications-contacts:DeleteEmailContact",
        "notifications-contacts:GetEmailContact",
        "notifications-contacts:ListEmailContacts",
        "notifications-contacts:TagResource",
        "notifications-contacts:UntagResource",
        "notifications-contacts:ListTagsForResource"
      ],
      "Resource": "*"
    }
  ]
}
```

------

## Example 7: Resource-scoped access for managed notifications
<a name="scoped-managed-notifications-example"></a>

This policy demonstrates least-privilege access by scoping managed notification permissions to a specific category (and optionally a specific sub-category) using resource-level ARNs. Replace the category (and optionally the sub-category) in the ARN to match your use case. This example uses AWS Health managed notifications.

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "ScopedManagedNotifications",
      "Effect": "Allow",
      "Action": [
        "notifications:GetManagedNotificationConfiguration",
        "notifications:ListManagedNotificationConfigurations",
        "notifications:ListManagedNotificationChannelAssociations",
        "notifications:AssociateManagedNotificationAccountContact",
        "notifications:DisassociateManagedNotificationAccountContact",
        "notifications:AssociateManagedNotificationAdditionalChannel",
        "notifications:DisassociateManagedNotificationAdditionalChannel",
        "notifications:GetManagedNotificationEvent",
        "notifications:ListManagedNotificationEvents",
        "notifications:GetManagedNotificationChildEvent",
        "notifications:ListManagedNotificationChildEvents"
      ],
      "Resource": "arn:aws:notifications::123456789012:managed-notification-configuration/category/AWS-Health/sub-category/*"
    }
  ]
}
```