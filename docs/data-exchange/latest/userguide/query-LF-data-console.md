# Setting up and querying AWS Data Exchange for Lake Formation (Test Product)

(Preview)

The following procedure shows how to set up and query a Lake Formation data permission set (Preview)
using the AWS Management Console.

###### To enable querying on the AWS Data Exchange for Lake Formation (Test Product) data set (Preview)

1. Open and sign in to the AWS Data Exchange console.
2. From the left navigation pane under **My subscriptions**, choose
   **Entitled data**.
3. From the list of **Products**, choose **AWS Data Exchange for Lake Formation (Test
   Product) (Preview)**.
4. Choose **Accept** to accept the AWS RAM share.

###### Note

You must accept the AWS RAM share within 12 hours of subscribing to the data product.
If your AWS RAM share invitation expires, select **Request invitation**
and allow several business days for a new share to be sent. You only need to accept the
AWS RAM share once for each provider that you license Lake Formation data sets from. 5. Open the [Lake Formation
console](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"). 6. Sign in as a principal who has the Lake Formation `CREATE_TABLE` or
`CREATE_DATABASE` permission, as well as the `glue:CreateTable` or
`glue:CreateDatabase` AWS Identity and Access Management (IAM) permission. 7. In the navigation pane, choose **Tables**, and then choose
**Create table**. 8. On the **Create table** page, choose **Resource
Link**, and then provide the following information:

    * **Resource link name**  – Enter a name that adheres to the
     same rules as a table name. The name can be the same as the name of the target shared
     table.
    * **Database** – The database in the local Data Catalog must
     contain the resource link.
    * **Shared table** – Select one of the tables shared through
     AWS Data Exchange for Lake Formation (Test product). All of the table names shared through that product
     begin with `adxlf_test`, or enter a local (owned) or shared table name.


    The list contains all of the tables shared with your account. The database and
     owner account ID are listed with each table. If you don’t see a table that you know
     was shared with your account, check the following:




    	+ If you aren’t a data lake administrator, confirm with your administrator that
    	 you were granted Lake Formation permissions on the table.
    	+ If you’re a data lake administrator and your account is not the same AWS
    	 organization as the granting account, confirm that you’ve accepted the AWS Resource Access Manager
    	 (AWS RAM) resource share invitation for the table. For more information, see [Accepting a resource share invitation from AWS RAM](../../../lake-formation/latest/dg/accepting-ram-invite.md "../../../lake-formation/latest/dg/accepting-ram-invite.md").
    * **Shared table's database** – If you selected a shared
     table from the list, this field is populated with the shared table's database in the
     external account. If you didn't select a shared table, enter a local database for a
     resource link to a local table, or the shared table's database in the external
     account.
    * **Shared table owner** – If you selected a shared table from
     the list, this field is populated with the shared table's owner account ID. If you
     didn't select a shared table, enter your AWS account ID for a resource link to a
     local table, or the ID of the AWS account that shared the table.

###### To query the AWS Data Exchange for Lake Formation (Test Product) data set (Preview) with Amazon Athena

(Console)

1. Sign in to the [Amazon Athena console](https://console.aws.amazon.com/athena "https://console.aws.amazon.com/athena") with a
   role that has permissions for Amazon Athena.
2. In the Amazon Athena query editor, choose the resource link that you created
   previously.
3. Choose the additional menu options icon next to `source_data` and choose
   **Preview table**.
4. Choose **Run query**.

###### To allow querying on the AWS Data Exchange for Lake Formation (Test Product) data set (Preview)

(AWS CLI)

1. To retrieve a list of all invitations available to your AWS account, enter the
   following command. The AWS CLI `query` parameter lets you restrict the output to
   only those invitations shared from AWS Data Exchange.

`$ AWS ram get-resource-share-invitations`

`--region us-east-1`

`--query 'resourceShareInvitations[?`

`senderAccountId==147854383891]'` 2. Find the invitations for the AWS Data Exchange for Lake Formation data set. Then, note the
`resourceShareInvitationArn` in the output to use in the following command to
accept the invitation.

`$ AWS ram accept-resource-share-invitation --region us-east-1
 --resource-share-invitation-arn [resourceShareInvitationArn]`

If successful, the response shows that the status has changed from
**PENDING** to **ACCEPTED**. 3. Create a resource link to one of the tables shared through the AWS Data Exchange for Lake Formation data set
with the following command:

`aws glue create-table --database-name [local_database_to_store_resource_link]
 --table-input
 '{"Name":"resource_link_name","TargetTable":{"CatalogId":"[account_owning_original_table]","DatabaseName":"[shared_db_in_provider_account]","Name":"[shared_table_in_provider_account]"}}'.`

###### Note

To create resource links, use the Lake Formation `CREATE_TABLE` or
`CREATE_DATABASE` permission, as well as the `glue:CreateTable`
or `glue:CreateDatabase` IAM permission.
