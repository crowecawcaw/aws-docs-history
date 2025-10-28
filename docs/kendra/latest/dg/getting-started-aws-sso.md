# Getting started with an AWS IAM Identity Center identity source

(console)

An AWS IAM Identity Center identity source contains information on your users and groups. This is useful
for setting up user context filtering, where Amazon Kendra filters search results for
different users based on the user or their group's access to documents.

To create an IAM Identity Center identity source, you must activate IAM Identity Center and create an organization in
AWS Organizations. When you activate IAM Identity Center and create an organization for the first time, it
automatically defaults to the Identity Center directory as the identity source. You can
change to Active Directory (Amazon managed or self-managed) or an external identity provider
as your identity source. You must follow the correct guidance for this — see [Changing your
IAM Identity Center identity source](changing-aws-sso-source.md "changing-aws-sso-source.md"). You can have only one identity source per
organization.

In order for your users and groups to be assigned different levels of access to documents,
you need to include your users and groups in your access control list when you ingest
documents into your index. This allows your users and groups to search for documents in
Amazon Kendra in accordance with their level of access. When you issue a query, the
user ID needs to be an exact match of the user name in IAM Identity Center.

You must also grant the required permissions to use IAM Identity Center with Amazon Kendra. For
more information, see [IAM roles for
IAM Identity Center](iam-roles.md#iam-roles-aws-sso "iam-roles.md#iam-roles-aws-sso").

###### To set up an IAM Identity Center identity source

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Enable IAM Identity Center**, and then choose **Create AWS organization**.

Identity Center directory is created by default, and an email is sent to you to
verify the email address associated with the organization. 3. To add a group to your AWS organization, in the navigation pane,
choose **Groups**. 4. On the **Groups page**, choose **Create group**
and enter a group name and description in the dialog box. Choose
**Create**. 5. To add a user to your Organizations, in the navigation pane, choose
**Users**. 6. On the **Users** page, choose **Add user**.
Under **User details**, specify all required fields. For
**Password**, choose **Send an email to the
user**. Choose **Next**. 7. To add a user to a group, choose **Groups** and select a
group. 8. On the **Details** page, under **Group
members**, choose **Add user**. 9. On the **Add users to group** page, select the user you want to
add as a member of the group. You can select multiple users to add to a
group. 10. To sync your list of users and groups with IAM Identity Center, change your identity source to
Active Directory or External identity provider.

Identity Center directory is the default identity source and requires you to
manually add your users and groups using this source if you do not have your own
list managed by a provider. To change your identity source, you must follow the
correct guidance for this—see [Changing your IAM Identity Center identity
source](changing-aws-sso-source.md "changing-aws-sso-source.md").

###### Note

If using Active Directory or an external identity provider as your identity source,
you must map the email addresses of your users to IAM Identity Center user names when you specify the
System for Cross-domain Identity Management (SCIM) protocol. For more information, see
the [IAM Identity Center guide on SCIM for
enabling IAM Identity Center](../../../singlesignon/latest/userguide/scim-profile-saml.md "../../../singlesignon/latest/userguide/scim-profile-saml.md").

Once you have set up your IAM Identity Center identity source, you can activate this in the console when
you create or edit your index. Go to **User access control** in your index
settings and edit your settings to allow fetching user-group information from IAM Identity Center.

You can also activate IAM Identity Center using the [UserGroupResolutionConfiguration](../APIReference/API_UserGroupResolutionConfiguration.md "../APIReference/API_UserGroupResolutionConfiguration.md") object. You provide the
`UserGroupResolutionMode` as `AWS_SSO` and create an IAM role that gives permission to call
`sso:ListDirectoryAssociations`, `sso-directory:SearchUsers`,
`sso-directory:ListGroupsForUser`,
`sso-directory:DescribeGroups`.

###### Warning

Amazon Kendra currently does not support using
`UserGroupResolutionConfiguration` with an AWS
organization member account for your IAM Identity Center identity source. You must create your index
in the management account for the organization in order to use
`UserGroupResolutionConfiguration`.

The following is an overview of how to set up a data source with
`UserGroupResolutionConfiguration` and user access control to filter search
results on user context. This assumes you have already created an index and an IAM role for indexes. You create an index and provide the IAM role
using the [CreateIndex](../APIReference/API_CreateIndex.md "../APIReference/API_CreateIndex.md") API.

###### Setting up a data source with `UserGroupResolutionConfiguration` and user

context filtering

1. Create an [IAM
   role](iam-roles.md#iam-roles-aws-sso "iam-roles.md#iam-roles-aws-sso") that gives permission to access your IAM Identity Center identity source.
2. Configure [`UserGroupResolutionConfiguration`](../APIReference/API_UserGroupResolutionConfiguration.md "../APIReference/API_UserGroupResolutionConfiguration.md") by setting the mode
   to `AWS_SSO` and call [UpdateIndex](../APIReference/API_UpdateIndex.md "../APIReference/API_UpdateIndex.md") to
   update your index to use IAM Identity Center.
3. If you want to use token-based user access control to filter search results on
   user context, set [UserContextPolicy](../APIReference/API_UpdateIndex.md#Kendra-UpdateIndex-request-UserContextPolicy "../APIReference/API_UpdateIndex.md#Kendra-UpdateIndex-request-UserContextPolicy") to `USER_TOKEN` when you call
   `UpdateIndex`. Otherwise, Amazon Kendra crawls the access
   control list for each of your documents for most data source connectors. You can
   also filter search results on user context in the [Query](../APIReference/API_Query.md "../APIReference/API_Query.md") API by providing
   user and group information in `UserContext`. You can also map users to
   their groups using [PutPrincipalMapping](../APIReference/API_PutPrincipalMapping.md "../APIReference/API_PutPrincipalMapping.md") so that you only need to provide the user ID when
   you issue the query.
4. Create an [IAM
   role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") that gives permission to access your data source.
5. [Configure](../APIReference/API_DataSourceConfiguration.md "../APIReference/API_DataSourceConfiguration.md") your data source. You must provide the required connection
   information to connect to your data source.
6. Create a data source using the [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md") API. Provide the `DataSourceConfiguration`
   object, which includes `TemplateConfiguration`, the ID of your index, the
   IAM role for your data source, the data source type, and give
   your data source a name. You can also update your data source.
