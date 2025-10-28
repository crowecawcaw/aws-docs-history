# Setting up permissions for Amazon Redshift datashares

This topic describes the steps you need to follow to accept a datashare invitation,
create a federated database, and grant permissions. You can use the Lake Formation console or the
AWS Command Line Interface (AWS CLI). The examples in this topic show the producer cluster, the Data Catalog, and the data consumer in the same account.

To learn more about Lake Formation cross-account capabilities, see [Cross-account data sharing in Lake Formation](cross-account-permissions.md "cross-account-permissions.md").

###### To set up permissions for a datashare

1. Review a datashare invitation and accept it.

Console

    1. Sign in to the Lake Formation console as a data lake administrator at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"). Navigate to the **Data sharing** page.
    2. Review the datashares that you're authorized to access. The
     **Status** column indicates your current participation status
     for the datashare. The **Pending** status indicates that you
     have been added to a datashare, but you have not yet accepted it or have
     rejected the invitation.
    3. To respond to a datashare invitation, select the datashare name and choose
     **Review invitation**. In **Accept or reject
     datashare**, review the invitation details. Choose
     **Accept** to accept the invitation or
     **Reject** to decline the invitation. You don't get access to
     the datashare if you reject the invitation.

AWS CLI
The following examples show how to view, accept, and register the invitation.
Replace the AWS account ID with a valid AWS account ID. Replace the
`data-share-arn` with the actual Amazon Resource Name (ARN) that
references the datashare.

    1. View a pending invitation.



    ```
    aws redshift describe-data-shares \
     --data-share-arn 'arn:aws:redshift:us-east-1:111122223333:datashare:abcd1234-1234-ab12-cd34-1a2b3c4d5e6f/federatedds' \
    ```
    2. Accept a datashare.



    ```
     aws redshift associate-data-share-consumer \
     --data-share-arn 'arn:aws:redshift:us-east-1:111122223333:datashare:abcd1234-1234-ab12-cd34-1a2b3c4d5e6f/federatedds' \
     --consumer-arn 'arn:aws:glue:us-east-1:111122223333:catalog
    ```
    3. Register the datashare in the Lake Formation account. Use the [RegisterResource](../APIReference/API_RegisterResource.md "../APIReference/API_RegisterResource.md") API operation to register the datashare in Lake Formation.
     `DataShareArn` is the input parameter for
     `ResourceArn`.


    ###### Note

    This is a mandatory step.



    ```
    aws lakeformation register-resource \
     --resource-arn 'arn:aws:redshift:us-east-1:111122223333:datashare:abcd1234-1234-ab12-cd34-1a2b3c4d5e6f/federatedds'
    ```

2. Create a database.

After you’ve accepted a datashare invitation, you need to create a database that points to the Amazon Redshift database associated with the datashare.
You must be a data lake administrator to create a database.

Console

    1. Select the datashare from the **Invitations** pane and choose **Set database details**.
    2. In **Set database details**, enter a unique name and
     identifier for the datashare. You use this identifier for mapping the datashare
     internally in the metadata hierarchy (dbName.schema.table).
    3. Choose **Next** to grant permissions to other users on the shared database and tables.

AWS CLI
Use the following example code to create a database that points to the Amazon Redshift
database shared with Lake Formation using the AWS CLI.

```
aws glue create-database --cli-input-json \

'{
 "CatalogId": "111122223333",
 "DatabaseInput": {
  "Name": "tahoedb",
  "FederatedDatabase": {
       "Identifier": "arn:aws:redshift:us-east-1:111122223333:datashare:abcd1234-1234-ab12-cd34-1a2b3c4d5e6f/federatedds",
       "ConnectionName": "aws:redshift"
   }
 }
 }'
```

3. Grant permissions.

After you’ve created the database, you can grant permissions to users in your
account or to external AWS accounts and organizations. You'll not be able to grant write
data permissions (insert, delete) and metadata permissions (alter, drop, create) on the
federated database that is mapped to an Amazon Redshift datashare. For more information on granting
permissions, see [Managing Lake Formation permissions](managing-permissions.md "managing-permissions.md").

###### Note

As a data lake administrator, you can only view tables in the federated databases. To perform
any other action, you need to grant yourself more permissions on those tables.

Console

    1. On the **Grant permissions** screen, select the users to
     grant permissions to.
    2. Choose **Grant**.

AWS CLI
Use the following examples to grant database and table permissions using the AWS CLI:

```
aws lakeformation grant-permissions --input-cli-json file://input.json

{
   "Principal": {
           "DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:user/non-admin"
   },
   "Resource": {
          "Database": {
                "CatalogId": "111122223333",
                 "Name": "tahoedb"
           }
    },
    "Permissions": [
             "DESCRIBE"
     ],
    "PermissionsWithGrantOption": [

     ]
 }

```

```
aws lakeformation grant-permissions --input-cli-json file://input.json

{
                   "Principal": {
                          "DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:user/non-admin"
                   },
                  "Resource": {
                         "Table": {
                              "CatalogId": "111122223333",
                              "DatabaseName": "tahoedb",
                              "Name": "public.customer"
                       }
                  },
                 "Permissions": [
                        "SELECT"
                  ],
                 "PermissionsWithGrantOption": [
                         "SELECT"
                   ]
 }

```
