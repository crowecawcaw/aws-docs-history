

# Importing AWS Data Exchange assets from AWS Lake Formation (Preview)
<a name="import-LF-asset"></a>

When you import assets from AWS Lake Formation to AWS Data Exchange, the IAM permissions that you use must include the following abilities: 
+ Write to, grant, and revoke Lake Formation permissions
+ Create resource shares for tables, databases, and catalogs
+ Update, delete, associate, and disassociate resource shares for any resource share beginning with **Lake Formation**

For more information about required and recommended IAM permissions, see [Identity and access management in AWS Data Exchange](auth-access.md).

## Importing assets from AWS Lake Formation (Preview) (AWS SDKs)
<a name="import-lf-asset-sdk"></a>

**To import assets from AWS Lake Formation (Preview) (AWS SDKs)**

1. Create a `CreateJob` request of type `Import_Assets_From_Lake_Formation_Tag_Policy`. 

1. Include the following in the request:
   + `AssetSources`
     + `CatalogId`
     + `Database`
       + `Expression`
         + `TagKey`
         + `TagValues`
       + `Permissions`
     + `Table`
       + `Expression`
         + `TagKey`
         + `TagValues`
       + `Permissions`
   + `RoleArn`
   + `DataSetId`
   + `RevisionId`

1. Start the `CreateJob` request with a `StartJob` operation that requires the `JobId`.

1. (Optional) Poll the `GetJob` operation to wait for the job to complete.

1. (Optional) Update the assets' name property after they are created.

## Importing assets from AWS Lake Formation (Preview) (console)
<a name="import-LF-asset-console"></a>

**To import an asset from AWS Lake Formation (Preview) (console)**

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange).

1. In the left side navigation pane, for **Publish data**, choose **Owned data sets**.

1. In **Owned data sets**, choose the data set that has the revision you want to update.

1. On the **Revisions** tab, choose **Create revision** to open the **Create revision** page.

   1. For **Revision settings**, provide an optional comment for your revision that describes the purpose of the revision.

   1. For **Add tags – optional**, add tags associated with the resource.

   1. Choose **Create**.

      Your new revision is created.

1. For the **Lake Formation data permission** section, choose **Add LF-Tag**.

1. Choose the **Key** and **Values** that you want to add and choose **Add LF-Tag**.

   1. (Optional) Choose **Preview Resource(s)** to view the associated data catalog resources that you are granting permission.

1. In **Service access**, select the **Role** to import the AWS Lake Formation resources into AWS Data Exchange.

1. Choose **Create Lake Formation data permission**.

   A job is started to import your assets into your data set. After the job is finished, the **State** field in the **Jobs** section is updated to **Completed**.