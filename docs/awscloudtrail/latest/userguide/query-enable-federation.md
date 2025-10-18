# Enable Lake query federation

You can enable Lake query federation by using the CloudTrail console, AWS CLI, or 
 [EnableFederation](../APIReference/API_EnableFederation.md "../APIReference/API_EnableFederation.md") 
 API operation. When you enable Lake query federation, CloudTrail creates a managed database named `aws:cloudtrail` (if the database doesn't already exist) and a managed federated table in
 the AWS Glue Data Catalog. The event data store ID is used for the table name. CloudTrail registers the federation role ARN and event data store in
 [AWS Lake Formation](query-federation-lake-formation.md "query-federation-lake-formation.md"), the service responsible for allowing 
 fine-grained access control of the federated resources in the AWS Glue Data Catalog.

This section describes how to enable federation using the CloudTrail console and AWS CLI.


CloudTrail console
The following procedure shows you how to enable Lake query federation on an existing event data store.


1. Sign in to the AWS Management Console and open the CloudTrail console at
 [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the navigation pane, under **Lake**, choose **Event data stores**.
3. Choose the event data store that you want to update. This opens the event data store's details page.
4. In **Lake query federation**, choose **Edit** and then choose **Enable**.
5. Choose whether to create a new IAM role, or use an existing role. When you create a new role, 
 CloudTrail automatically creates a role with the required permissions. If you're using an existing role, be sure the role's policy provides the 
 [required minimum permissions](query-federation.md#query-federation-permissions-role "query-federation.md#query-federation-permissions-role").
6. If you're creating a new IAM role, enter a name for the role.
7. If you're choosing an existing IAM role, choose the role you want to use. The role must exist in your account.
8. Choose **Save changes**. The **Federation status** changes to `Enabled`.


AWS CLI
To enable federation, run the **aws cloudtrail
 enable-federation** command, providing the required
 **--event-data-store** and
 **--role** parameters. For
 **--event-data-store**, provide the event data
 store ARN (or the ID suffix of the ARN). For
 **--role**, provide the ARN for your federation
 role. The role must exist in your account and provide the [required minimum permissions](query-federation.md#query-federation-permissions-role "query-federation.md#query-federation-permissions-role").



```
aws cloudtrail enable-federation
--event-data-store arn:aws:cloudtrail:`region`:`account-id`:eventdatastore/`eds-id`
--role arn:aws:iam::`account-id`:role/`federation-role-name`
```

This example shows how a delegated administrator can enable
 federation on an organization event data store by specifying the ARN
 of the event data store in the management account and the ARN of the
 federation role in the delegated administrator account.



```
aws cloudtrail enable-federation
--event-data-store arn:aws:cloudtrail:`region`:`management-account-id`:eventdatastore/`eds-id`
--role arn:aws:iam::`delegated-administrator-account-id`:role/`federation-role-name`
```
