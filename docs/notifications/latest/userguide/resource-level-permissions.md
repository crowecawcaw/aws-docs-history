# Resource-level permissions in AWS User Notifications

_Resource-level permissions_ define the AWS resources that you
allow assigned entities (users, groups, and roles) to perform actions on. You specifiy the
Amazon Resource Name (ARN) of one or more resources as part of an IAM policy. You can then
attach this policy to IAM entities. When the action doesn't act on a named resource, or
when you grant permission to perform the action on all resources, the value of the resource
in the policy is a wildcard (**\***).

###### Note

AWS User Notifications doesn't support _resource-based policies_, which are
directly attached to AWS resources. For more information about the differences between
policies and permissions, see [Identity-based
policies and resource-based policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md") in the _IAM User
Guide_.

For more information about defining resource-level permissions, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.

##

Supported resource-level permissions for User Notifications API actions

This table describes the User Notifications API actions that currently support resource-level permissions, as well as the supported resources for each action, including their ARNs and ARN format.

| Resource                                         | API action                                                                                                                        | Resource ARN format                                                                                                                                                                                  | Example                                                                                                                                                                                      |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Managed Notification Configuration               | GetManagedNotificationConfiguration                                                                                               | `arn:aws:notifications::`accountId`:managed-notification-configuration/category/`category-name`/sub-category/`sub-category-name``                                                                    | `arn:aws:notifications::123456789012:managed-notification-configuration/category/AWS-Health/sub-category/Security`                                                                           |
| ListManagedNotificationConfigurations            | `*`                                                                                                                               | `*`                                                                                                                                                                                                  |
| AssociateManagedNotificationAccountContact       | `arn:aws:notifications::`accountId`:managed-notification-configuration/category/`category-name`/sub-category/`sub-category-name`` | `arn:aws:notifications::123456789012:managed-notification-configuration/category/AWS-Health/sub-category/Security`                                                                                   |
| DisassociateManagedNotificationAccountContact    | `arn:aws:notifications::`accountId`:managed-notification-configuration/category/`category-name`/sub-category/`sub-category-name`` | `arn:aws:notifications::123456789012:managed-notification-configuration/category/AWS-Health/sub-category/Security`                                                                                   |
| DisassociateManagedNotificationAdditionalChannel | `arn:aws:notifications::`accountId`:managed-notification-configuration/category/`category-name`/sub-category/`sub-category-name`` | `arn:aws:notifications::123456789012:managed-notification-configuration/category/AWS-Health/sub-category/Security`                                                                                   |
| AssociateManagedNotificationAdditionalChannel    | `arn:aws:notifications::`accountId`:managed-notification-configuration/category/`category-name`/sub-category/`sub-category-name`` | `arn:aws:notifications::123456789012:managed-notification-configuration/category/AWS-Health/sub-category/Security`                                                                                   |
| ListManagedNotificationChannelAssociations       | `arn:aws:notifications::`accountId`:managed-notification-configuration/category/`category-name`/sub-category/`sub-category-name`` | `arn:aws:notifications::123456789012:managed-notification-configuration/category/AWS-Health/sub-category/Security`                                                                                   |
| Notification Configuration                       | CreateNotificationConfiguration                                                                                                   | `arn:aws:notifications:*:`accountId`:configuration/*`                                                                                                                                                | `arn:aws:notifications:*:123456789012:configuration/*`                                                                                                                                       |
| UpdateNotificationConfiguration                  | `arn:aws:notifications::`accountId`:configuration/`configurationId``                                                              | `arn:aws:notifications::123456789012:configuration/a01gkn2k10c7spt0a8x8nj55555`                                                                                                                      |
| DeleteNotificationConfiguration                  | `arn:aws:notifications::`accountId`:configuration/`configurationId``                                                              | `arn:aws:notifications::123456789012:configuration/a01gkn2k10c7spt0a8x8nj55555`                                                                                                                      |
| GetNotificationConfiguration                     | `arn:aws:notifications::`accountId`:configuration/`configurationId``                                                              | `arn:aws:notifications::123456789012:configuration/a01gkn2k10c7spt0a8x8nj55555`                                                                                                                      |
| ListNotificationConfigurations                   | `*`                                                                                                                               | `*`                                                                                                                                                                                                  |
| AssociateChannel                                 | `arn:aws:notifications::`accountId`:configuration/`configurationId``                                                              | `arn:aws:notifications::123456789012:configuration/a01gkn2k10c7spt0a8x8nj55555`                                                                                                                      |
| DisassociateChannel                              | `arn:aws:notifications::`accountId`:configuration/`configurationId``                                                              | `arn:aws:notifications::123456789012:configuration/a01gkn2k10c7spt0a8x8nj55555`                                                                                                                      |
| ListChannels                                     | `*`                                                                                                                               | `*`                                                                                                                                                                                                  |
| Event Rule                                       | CreateEventRule                                                                                                                   | `arn:aws:notifications::`accountId`:configuration/`configurationId`/rule/*`                                                                                                                          | `arn:aws:notifications::123456789012:configuration/a01gkn2k10c7spt0a8x8nj55555/rule/*`                                                                                                       |
| UpdateEventRule                                  | `arn:aws:notifications::`accountId`:configuration/`configurationId`/rule/`eventRuleId``                                           | `arn:aws:notifications::123456789012:configuration/a01gkn2k10c7spt0a8x8nj55555/rule/a01gkn362610da5e7dckrt66666`                                                                                     |
| DeleteEventRule                                  | `arn:aws:notifications::`accountId`:configuration/`configurationId`/rule/`eventRuleId``                                           | `arn:aws:notifications::123456789012:configuration/a01gkn2k10c7spt0a8x8nj55555/rule/a01gkn362610da5e7dckrt66666`                                                                                     |
| GetEventRule                                     | `arn:aws:notifications::`accountId`:configuration/`configurationId`/rule/`eventRuleId``                                           | `arn:aws:notifications::123456789012:configuration/a01gkn2k10c7spt0a8x8nj55555/rule/a01gkn362610da5e7dckrt66666`                                                                                     |
| ListEventRules                                   | `*`                                                                                                                               | `*`                                                                                                                                                                                                  |
| Managed Notification Event                       | GetManagedNotificationEvent                                                                                                       | `arn:aws:notifications::`accountId`:managed-notification-configuration/category/`category-name`/sub-category/`sub-category-name`/event/`notificationEventId``                                        | `arn:aws:notifications::123456789012:managed-notification-configuration/category/AWS-Health/sub-category/Security/event/a01gkn2k10c7spt0a8x8nj55555`                                         |
| ListManagedNotificationEvents                    | `*`                                                                                                                               | `*`                                                                                                                                                                                                  |
| Managed Notification Child Event                 | GetManagedNotificationChildEvent                                                                                                  | `arn:aws:notifications::`accountId`:managed-notification-configuration/category/`category-name`/sub-category/`sub-category-name`/event/`notificationEventId`/child-event/`notificationChildEventId`` | `arn:aws:notifications::123456789012:managed-notification-configuration/category/AWS-Health/sub-category/Security/event/a01gkn2k10c7spt0a8x8nj55555/child-event/b01gaja54v1t6rr10dyshk77777` |
| ListManagedNotificationChildEvents               | `*`                                                                                                                               | `*`                                                                                                                                                                                                  |
| Notification Event                               | GetNotificationEvent                                                                                                              | `arn:aws:notifications::region:`accountId`:configuration/`configurationId`/event/`notificationEventId``                                                                                              | `arn:aws:notifications:us-east-1:123456789012:configuration/a01gkn2k10c7spt0a8x8nj55555/event/b01gaja54v1t6rr10dyshk77777`                                                                   |
| ListNotificationEvents                           | `*`                                                                                                                               | `*`                                                                                                                                                                                                  |
| Notification Hub                                 | RegisterNotificationHub                                                                                                           | `*`                                                                                                                                                                                                  | `*`                                                                                                                                                                                          |
| DeregisterNotificationHub                        | `*`                                                                                                                               | `*`                                                                                                                                                                                                  |
| ListNotificationHubs                             | `*`                                                                                                                               | `*`                                                                                                                                                                                                  |
| Email Contacts                                   | ActivateEmailContact                                                                                                              | `arn:aws:notifications-contacts::`accountId`:emailcontact/`emailContactId``                                                                                                                          | `arn:aws:notifications-contacts::123456789012:emailcontact/02k1g09g`                                                                                                                         |
| CreateEmailContact                               | `arn:aws:notifications-contacts::`accountId`:emailcontact/`emailContactId``                                                       | `arn:aws:notifications-contacts::123456789012:emailcontact/02k1g09g`                                                                                                                                 |
| DeleteEmailContact                               | `arn:aws:notifications-contacts::`accountId`:emailcontact/`emailContactId``                                                       | `arn:aws:notifications-contacts::123456789012:emailcontact/02k1g09g`                                                                                                                                 |
| GetEmailContact                                  | `arn:aws:notifications-contacts::`accountId`:emailcontact/`emailContactId``                                                       | `arn:aws:notifications-contacts::123456789012:emailcontact/02k1g09g`                                                                                                                                 |
| ListEmailContacts                                | `arn:aws:notifications-contacts::`accountId`:emailcontact/`emailContactId``                                                       | `arn:aws:notifications-contacts::123456789012:emailcontact/02k1g09g`                                                                                                                                 |
| ListTagsForResource                              | `arn:aws:notifications-contacts::`accountId`:emailcontact/`emailContactId``                                                       | `arn:aws:notifications-contacts::123456789012:emailcontact/02k1g09g`                                                                                                                                 |
| SendActivationCode                               | `arn:aws:notifications-contacts::`accountId`:emailcontact/`emailContactId``                                                       | `arn:aws:notifications-contacts::123456789012:emailcontact/02k1g09g`                                                                                                                                 |
| TagResource                                      | `arn:aws:notifications-contacts::`accountId`:emailcontact/`emailContactId``                                                       | `arn:aws:notifications-contacts::123456789012:emailcontact/02k1g09g`                                                                                                                                 |
| UntagResource                                    | `arn:aws:notifications-contacts::`accountId`:emailcontact/`emailContactId``                                                       | `arn:aws:notifications-contacts::123456789012:emailcontact/02k1g09g`                                                                                                                                 |

##

Example 1: Full access

This policy allows a user to call all available APIs.

JSON

```
`{
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
}`

```

##

Example 2: ReadOnly access

This policy allows a user to use get and list API actions.

JSON

```
`{
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
}`

```

##

Example 3: Deny a user the ability to update a notification configuration

This policy denies a user the ability to update a notification configuration.

JSON

```
`{
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
}`

```

##

Example 4: Allow users to create notification configurations and associate emails to them

This policy allows users to create notification configurations and associate emails to those configurations.

JSON

```
`{
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
}`

```

##

Example 5: Allow users full create, read, update, and delete (CRUD) access.

This policy allows users full CRUD access.

JSON

```
`{
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
}`

```
