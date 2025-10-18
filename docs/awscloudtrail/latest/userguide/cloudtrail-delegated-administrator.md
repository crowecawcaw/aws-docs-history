# Organization delegated administrator

When you use CloudTrail with an AWS Organizations organization, you can assign any account within the
 organization to act as a CloudTrail delegated administrator to manage the organization's trails
 and event data stores on behalf of the organization. A delegated administrator is a member
 account in an organization that can perform the same administrative tasks (except as [noted](#cloudtrail-org-tasks "#cloudtrail-org-tasks")) in CloudTrail as the
 management account.

If you choose a delegated administrator, this member account has administrative permissions on all organization trails and event data stores in the organization. Adding a delegated administrator does not alter the management or operation of the organization's trails or event data stores.

The first time you add a delegated administrator in the CloudTrail console, or by using the AWS CLI or CloudTrail API, CloudTrail checks whether the organization’s management account has a service-linked role. If the management account does not have a service-linked role, CloudTrail creates the service-linked role for the management account. For more information about service-linked roles, see [Using service-linked roles for
 CloudTrail](using-service-linked-roles.md "using-service-linked-roles.md").

###### Note

When you add a delegated administrator using the AWS Organizations CLI or API operation, CloudTrail service-linked roles won't be created automatically if they don't exist. 
 The service-linked roles are only created when you make a call from the management account directly to the CloudTrail service. For example, when you add a delegated 
 administrator or create an organization trail or event data store using the CloudTrail console, AWS CLI or CloudTrail API, the AWSServiceRoleForCloudTrail
 service-linked role is created.

When you add a delegated administrator using the AWS CloudTrail; CLI or API operation, CloudTrail will create both the AWSServiceRoleForCloudTrail and 
 the AWSServiceRoleForCloudTrailEventContext service-linked roles. For more information, see [Using service-linked roles for
 CloudTrail](using-service-linked-roles.md "using-service-linked-roles.md")..

Take note of the following factors that define how the delegated administrator operates in CloudTrail.



**The management account remains the owner of any CloudTrail organization resources the delegated administrator creates.**

The organization's management account remains the owner of any CloudTrail organization resources the delegated administrator creates, such as trails and event data stores. This provides continuity for the organization in the event the delegated administrator changes.



**Removing a delegated administrator account does not delete any CloudTrail organization resources they created.**

Organization trails and event data stores created by the delegated administrator are not deleted when you remove the delegated administrator, because 
 the management account always serves as the owner of the CloudTrail organization resources regardless of whether they are created by the 
 delegated administrator or the management account.


**An organization can have a maximum of three CloudTrail delegated administrators.**

You can have a maximum of three CloudTrail delegated administrators per organization. For more information about removing a delegated administrator, see [Remove a CloudTrail delegated administrator](cloudtrail-remove-delegated-administrator.md "cloudtrail-remove-delegated-administrator.md").


The following table shows the capabilities of the management account, delegated administrator accounts, and 
 accounts that are members within the AWS Organizations organization.



| Capabilities  | Management account | Delegated administrator account | Member accounts |
| --- | --- | --- | --- |
| Add or remove delegated administrator accounts. |  Yes |  No |  No |
| Create an organization trail. |  Yes |  Yes1 |  No |
| View a list of organization trails. |  Yes |  Yes |  Yes |
| Update an organization trail. |  Yes |  Yes1, 2 |  No |
| Delete an organization trail. |  Yes |  Yes |  No |
| Create an organization event data store for CloudTrail events or AWS Config configuration items. |  Yes |  Yes |  No |
| Enable Insights on an organization event data store. |  Yes |  No |  No |
| Update an organization event data store. |  Yes |  Yes2 |  No |
| Start and stop event ingestion on an organization event data store. |  Yes |  Yes |  No |
| Enable Lake query federation on an organization event data store3. |  Yes |  Yes |  No |
| Disable Lake query federation on an organization event data store. |  Yes |  Yes |  No |
| Delete an organization event data store. |  Yes |  Yes |  No |
| Copy trail events to an organization event data store. |  Yes |  No |  No |
| Run queries on organization event data stores. |  Yes |  Yes |  No |
| View a managed dashboard for an organization event data store. |  Yes |  No |  No |
| Enable the Highlights dashboard for organization event data stores. |  Yes |  No |  No |
| Create a widget for a custom dashboard that queries an organization event data store. |  Yes |  No |  No | 1The delegated administrator can only configure a CloudWatch Logs log group using the AWS CLI or CloudTrail `CreateTrail` or `UpdateTrail` API operations. Both the CloudWatch Logs log group and log role must exist in the calling account. 2Only the management account can convert an organization trail or event data store to an account-level trail or event data store, or convert an account-level trail or event data store to an organization trail or event data store. These actions are not allowed for the delegated administrator because organization trails and event data stores only exist in the management account. When an organization trail or event data store is converted to an account-level trail or event data store, only the management account has access to the trail or event data store. 3Only a single delegated administrator account or the management account can enable federation on an organization event data store. Other delegated administrator accounts can query and share information using the [Lake Formation data sharing feature](https://docs.aws.amazon.com/lake-formation/latest/dg/data-sharing-overivew.html "https://docs.aws.amazon.com/lake-formation/latest/dg/data-sharing-overivew.html"). Any delegated administrator account as well as the organization's management account can disable federation. ###### Topics <br>• [Required permissions to assign a delegated administrator](cloudtrail-delegated-administrator-permissions.md "cloudtrail-delegated-administrator-permissions.md") <br>• [Add a CloudTrail delegated administrator](cloudtrail-add-delegated-administrator.md "cloudtrail-add-delegated-administrator.md") <br>• [Remove a CloudTrail delegated administrator](cloudtrail-remove-delegated-administrator.md "cloudtrail-remove-delegated-administrator.md")
