# Authorization for AWS applications and services using Directory Service

This topic describes authorization for AWS applications and services using AWS Directory Service and AWS Directory Service Data

##

Authorizing an AWS application on an Active Directory

Directory Service grants specific permissions for selected applications to integrate seamlessly with your Active Directory when you authorize an AWS application.
AWS applications are only granted the access that's necessary for their specific use-cases.
The following is a set of internal permissions granted to applications and application administrators after authorization:

###### Note

The `ds:AuthorizationApplication` permission is required to authorize a new AWS application for an Active Directory.
Permissions to this action should only be provided to Administrators that configure integrations with Directory Service.

- Read access to Active Directory user, group, organizational unit, computer, or certification authority data in all Organizational Units (OU) of AWS Managed Microsoft AD, Simple AD, AD Connector directories,
  as well as trusted domains for AWS Managed Microsoft AD if permitted by a trust relationship.
- Write access to users, groups, group membership, computers, or certification authority data in your organizational unit of AWS Managed Microsoft AD. Write access to all OU‘s of Simple AD.
- Authentication and session management of Active Directory users for all directory types.

Certain AWS Managed Microsoft AD applications such as Amazon RDS and Amazon FSx integrate through direct network connection to your Active Directory. In this case, the directory interactions use native Active Directory protocols
such as LDAP and Kerberos. The permissions of these AWS applications are controlled by a directory user account created in the AWS Reserved Organizational Unit (OU) during the application authorization, which includes
DNS management and full access to a custom OU created for the application. In order to use this account, the application requires permissions to `ds:GetAuthorizedApplicationDetails` action through caller credentials or an IAM role.

For more information about Directory Service API permissions, see [Directory Service API permissions: Actions,
resources, and conditions reference](UsingWithDS_IAM_ResourcePermissions.md "UsingWithDS_IAM_ResourcePermissions.md").

For more information about enabling AWS applications and services for AWS Managed Microsoft AD, see [Access to AWS applications and services
from your AWS Managed Microsoft AD](ms_ad_manage_apps_services.md "ms_ad_manage_apps_services.md").
For more information about enabling AWS applications and services for Simple AD, see [Access to AWS applications and services
from your Simple AD](simple_ad_manage_apps_services.md "simple_ad_manage_apps_services.md").
For information about enabling AWS applications and services for AD Connector, see [Access to AWS applications and services from AD Connector](ad_connector_manage_apps_services.md "ad_connector_manage_apps_services.md").

###### Deauthorizing an AWS application on a Active Directory

The `ds:UnauthorizedApplication` permission is required to remove permissions for an AWS application to access an Active Directory.
Follow the procedure the application provides to disable it.

## AWS application authorization with Directory Service Data

For AWS Managed Microsoft AD directories, the Directory Service Data (ds-data) API provides programmatic access to user and group management tasks.
The authorization model of AWS applications is separate from the access controls of Directory Service Data, which means that access policies for Directory Service Data actions don't effect the authorization for AWS applications.
Denying access to a directory in ds-data will not interrupt the AWS Application integration or use-cases of AWS applications.

When writing access policies for AWS Managed Microsoft AD directories that authorize AWS applications, be aware that user and group functionality might be available by calling either an authorized AWS Application or Directory Service Data API.
Amazon WorkDocs, Amazon WorkMail, Amazon WorkSpaces, Amazon Quick Suite, and Amazon Chime all provide user and group management actions in their APIs.
Control access to this AWS application functionality with IAM policies.

###### Examples

The following snippets show the incorrect and correct ways to deny `DeleteUser` functionality when AWS applications, such as WorkDocs and Amazon WorkMail, are authorized on the directory.

**Incorrect**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "VisualEditor0",
 "Effect": "Deny",
 "Action": [
 "ds-data:DeleteUser"
 ],
 "Resource": "*"
 }
 ]
}`

```

**Correct**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "VisualEditor0",
 "Effect": "Deny",
 "Action": [
 "ds-data:DeleteUser",
 "workmail:DeleteUser",
 "workdocs:DeleteUser"
 ],
 "Resource": "*"
 }
 ]
}`

```
