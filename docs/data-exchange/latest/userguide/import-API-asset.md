

# Importing AWS Data Exchange assets from an Amazon API Gateway API
<a name="import-API-asset"></a>

AWS Data Exchange subscribers can use their IAM credentials and AWS SDKs to call APIs from data providers. AWS Data Exchange manages access to APIs by handling authentication and subscription entitlements.

## Importing API assets from an Amazon API Gateway API (AWS SDKs)
<a name="import-api-asset-prog"></a>

**Note**  
Currently, the `SendApiAsset` operation is not supported for the following SDKs:  
SDK for .NET
AWS SDK for C\+\+
AWS SDK for Java 2.x

**To import assets from an Amazon API Gateway API (AWS SDKs)**

1. Create a `CreateJob` request of type `IMPORT_ASSET_FROM_API_GATEWAY_API`.

1. Include the following in the request:
   + `ApiID`
   + `DataSetID`
   + `ProtocolType`
   + `RevisionID`
   + `Stage`

1. Start the `CreateJob` request with a `StartJob` operation that requires the `JobId` returned in step 1.

1. (Optional) Poll the `GetJob` operation to wait for the job to complete.

1. (Optional) Update the assets' name property after they are created.

## Importing API assets from an Amazon API Gateway API (console)
<a name="import-api-asset-console"></a>

**To import an asset from an Amazon API Gateway API (console)**

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange).

1. In the left side navigation pane, for **Publish data**, choose **Owned data sets**.

1. In **Owned data sets**, choose the data set that has the asset you want to update.

1. On the **Revisions** tab, choose **Create revision** to open the **Create revision** page.

   1. For **Revision settings**, provide an optional comment for your revision that describes the purpose of the revision.

   1. For **Add tags – optional**, add tags associated with the resource.

   1. Choose **Create**.

      Your new revision is created.

1. For the **API assets** section, choose **Add API stage**.

1. On the **Add API stage** page, select the **Amazon API Gateway API** and the **Stage name** from your AWS account or another account.

1. For **Document API for subscribers**:

   1. Update the **API name** to a clear and concise name that subscribers can understand.

   1. Document the OpenAPI 3.0 specification by entering the specification in the field, importing the specification by choosing **Import from .JSON file**, or importing the specification by choosing **Import from Amazon API Gateway**.

1. Choose **Add API stage**.

   A job is started to import your API assets into your data set. After the job is finished, the **State** field in the **Jobs** section is updated to **Completed**.