# Creating a data grant on AWS Data Exchange containing

APIs

The following topics describe the process of creating a REST API data set and adding it to
a data grant that contains APIs on AWS Data Exchange. You can complete the process by using either the
AWS Data Exchange console or the AWS Command Line Interface.

After you have set up your Amazon API Gateway REST API, you can create a new API data set in AWS Data Exchange.
You can then create a revision, and add API assets.

Creating a data grant with an API asset allows recipient requests to an AWS Data Exchange endpoint to
proxy through to your API Gateway API.

The process has the following steps:

###### Steps

- [Prerequisites](#creating-a-data-grant-api-prereq "#creating-a-data-grant-api-prereq")
- [Step 1: Update the API resource policy](#data-grant-update-API-resource-policy "#data-grant-update-API-resource-policy")
- [Step 2: Create an API data set](#data-grant-create-api-data-set "#data-grant-create-api-data-set")
- [Step 3: Create a revision](#data-grant-create-api-revision "#data-grant-create-api-revision")
- [Step 4: Add API assets to a revision](#data-grant-add-api-asset "#data-grant-add-api-asset")
- [Step 5: Create a new data grant
  containing APIs](#data-grant-publish-api-data-product "#data-grant-publish-api-data-product")

## Prerequisites

Before you can publish a product containing APIs, you must meet the following
prerequisites:

- Before you can use any AWS service, including AWS Data Exchange, you must sign up for AWS and
  create an administrative user. For more information, see [Getting started](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md") in the
  _AWS IAM Identity Center User Guide_.
- Your REST API must be on Amazon API Gateway with an integration that uses an appropriate request
  and response model for accessing your data, such as Amazon DynamoDB or AWS Lambda. For
  more information, see [Developing a REST API in
  API Gateway](../../../apigateway/latest/developerguide/rest-api-develop.md "../../../apigateway/latest/developerguide/rest-api-develop.md") and [Working with REST
  APIs](../../../apigateway/latest/developerguide/apigateway-rest-api.md "../../../apigateway/latest/developerguide/apigateway-rest-api.md") in the _Amazon API Gateway Developer Guide_.

###### Note

Only public API Gateway APIs are supported.

- Your API Gateway REST API must be able to authenticate and authorize calls from the AWS Data Exchange
  service principal. Every request from AWS Data Exchange to your API uses the Signature Version 4 (SigV4)
  protocol signed with AWS Data Exchange credentials. AWS Data Exchange works with custom domains and domain key
  mappings.

###### Note

AWS Data Exchange doesn't support Amazon Cognito, No-Auth, and AWS Lambda authorizers.

- If your API Gateway REST API uses a custom identity system for authentication and
  authorization, configure it to use IAM authentication and import an OpenAPI schema
  describing your API. AWS Data Exchange will invoke your API Gateway REST API with its own service credentials
  and include subscriber information such as account ID.
- Your API Gateway REST API is responsible for integrating with your backend. To do this, do one
  of the following:
  - Attach a long-lived authentication token to every request that comes through your
    API Gateway REST API that the backend can verify.
  - Use API Gateway to invoke a Lambda function that can generate credentials and invoke your
    API.

Your API is invoked per the [API integration request specification](publish-API-product.md#api-request-spec "publish-API-product.md#api-request-spec").

For more information, see the following topics:

###### Topics

- [API data set security](#data-grant-api-data-set-security "#data-grant-api-data-set-security")
- [API integration request specification](#data-grant-api-request-spec "#data-grant-api-request-spec")
- [Header forwarding](#data-grant-header-forwarding "#data-grant-header-forwarding")

### API data set security

AWS Data Exchange encrypts traffic end to end using Transport Layer Security (TLS) 1.2. All metadata
is encrypted at rest. AWS Data Exchange will not store subscriber requests or the responses from
your backend.

### API integration request specification

An API on AWS Data Exchange passes through all headers (except for the headers listed in [Header forwarding](publish-API-product.md#header-forwarding "publish-API-product.md#header-forwarding")), body, http method, path,
and query strings as-is from the customer request and appends the following headers.

```
// These headers help prevent Confused Deputy attacks.  They enable the SourceAccount
// and SourceArn variables in IAM policies.
'x-amz-source-account': ACCOUNT_ID,
'x-amz-source-arn': `arn:aws:dataexchange:${REGION}:${OWNER_ACCOUNT_ID}:data-sets/${DATA_SET_ID}/revisions/${REVISION_ID}/assets/${ASSET_ID}`,

// These headers identify the API Asset in Data Exchange.
'x-amzn-dataexchange-asset-id': ASSET_ID,
'x-amzn-dataexchange-data-set-id': DATA_SET_ID,
'x-amzn-dataexchange-revision-id': REVISION_ID,

// This header identifies the Data Exchange Product.
'x-amzn-dataexchange-product-id': PRODUCT_ID,

// This header identifies the caller of Data Exchange.  It will contain subscriber
// information.
'x-amzn-dataexchange-requester-account-id': REQUESTER_ACCOUNT_ID,

// Providers can attach custom metadata in the form of key/value pairs
// to a particular subscription. We will send these key/value pairs as stringified
// JSON.
'x-amz-dataexchange-subscription-metadata': STRINGIFIED_METADATA,
```

### Header forwarding

AWS Data Exchange removes any headers related to authentication or namespaced to Amazon prior to
forwarding it to a data owner backend. Specifically, AWS Data Exchange removes:

- `Authentication` header
- Any headers that begin with `x-amz`

The `host` header will be overwritten as a consequence of the proxying.

## Step 1: Update the API resource policy

If you have an Amazon API Gateway REST API that meets the [Prerequisites](publish-API-product.md#publish-api-prereq "publish-API-product.md#publish-api-prereq"), you must update your API resource
policy to grant AWS Data Exchange the ability to invoke your API when a subscriber makes a request to get
your API’s schema.

###### To update your API resource policy

1. Add the following policy to your API’s resource policy:

```
{
"Effect": "Allow",
"Principal": {"Service": "dataexchange.amazonaws.com"},
"Action": "execute-api:Invoke",
"Resource": "*",
"Condition": {"StringEquals": {"aws:SourceAccount": "<account-id>"}}
}

```

2. Replace `account-id` with the account that will be creating the API data set.

The account with the API Gateway resource does not need to be in the same account that is
creating the data set.

This policy restricts these permissions to calls made by the AWS Data Exchange service principal and
requires that only your account can authorize AWS Data Exchange to integrate with your API.

###### Note

If you have a resource policy that explicitly denies AWS Data Exchange from doing this invocation,
you must remove or limit this deny.

You’re now ready to [create an API data
set](publish-API-product.md#create-api-data-set "publish-API-product.md#create-api-data-set").

## Step 2: Create an API data set

Data sets in AWS Data Exchange are dynamic and are versioned using revisions, with each revision
containing at least one asset. For more information, see [Data in AWS Data Exchange](data-sets.md "data-sets.md").

You use either the AWS Data Exchange console or the AWS Command Line Interface to create an API data
set:

- [Creating an API data set
  (console)](publish-API-product.md#create-api-ds-console "publish-API-product.md#create-api-ds-console")
- [Creating an API data set (AWS CLI)](publish-API-product.md#create-api-ds-cli "publish-API-product.md#create-api-ds-cli")

### Creating an API data set (console)

###### To create an API data set (console)

1. Open your web browser and sign in to the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. On the left side navigation pane, under **My data**, choose
   **Owned data sets**.
3. In **Owned data sets**, choose **Create data set** to
   open the **Data set creation steps** wizard.
4. In **Select data set type**, choose **Amazon API Gateway
   API**.
5. In **Define data set**, enter a **Name** and
   **Description** for your data set. For more information, see [Data set best practices](data-sets.md#data-set-best-practices "data-sets.md#data-set-best-practices").
6. (Optional) Under **Add tags – optional**, add tags.
7. Choose **Create**.

You are now ready to create a revision.

### Creating an API data set (AWS CLI)

###### To create an API data set (CLI)

1. Use the `create-data-set` command to create an API data set:

```
$ AWS dataexchange create-data-set \
-\\-asset-type API_GATEWAY_API \
-\\-description 'Data Set Description' \
-\\-name 'Data Set Name'

{
"Arn": "arn:aws:dataexchange:us-east-1:123456789012:data-sets/$DATA_SET_ID",
"AssetType": "API_GATEWAY_API",
"CreatedAt": "2021-09-11T00:16:46.349000+00:00",
"Description": "Data Set Description",
"Id": "$DATA_SET_ID",
"Name": "Data Set Name",
"Origin": "OWNED",
"UpdatedAt": "2021-09-11T00:16:46.349000+00:00"
}

```

2. Note the new Asset Type of `API_GATEWAY_API`.

You are now ready to create a revision.

## Step 3: Create a revision

In the following procedure, you create a revision after you’ve created a data set. For
more information, see [Revisions](data-sets.md#revisions "data-sets.md#revisions").

You use either the AWS Data Exchange console or the AWS Command Line Interface to create a revision:

- [Creating a revision
  (console)](publish-API-product.md#create-api-revision-console "publish-API-product.md#create-api-revision-console")
- [Creating a revision (AWS CLI)](publish-API-product.md#create-api-revision-cli "publish-API-product.md#create-api-revision-cli")

### Creating a revision (console)

###### To create a revision (console)

1. On the **Data set overview** section of the data set details
   page:
   1. (Optional) Choose **Edit name** to edit information about your data
      set.
   2. (Optional) Choose **Delete** to delete the data set.

2. On the **Revisions** section, choose **Create
   revision**.
3. Under **Define revision**, provide an optional comment for your
   revision that describes the purpose of the revision.
4. (Optional) Under **Add tags – optional**, add tags associated
   with the resource.
5. Choose **Create revision**.
6. Review, edit, or delete your changes from the previous step.

You are now ready to [add API assets
to the revision](publish-API-product.md#add-api-asset "publish-API-product.md#add-api-asset").

### Creating a revision (AWS CLI)

###### To create a revision (AWS CLI)

1. Use the `create-revision` command to create a revision:

```
$ AWS dataexchange create-revision \
-\\-data-set-id $DATA_SET_ID \
-\\-comment 'First Atlas Revision'
{
"Arn": "arn:aws:dataexchange:us-east-1:123456789012:data-sets/$DATA_SET_ID/revisions/$REVISION_ID",
"Comment": "First Atlas Revision",
"CreatedAt": "2021-09-11T00:18:49.160000+00:00",
"DataSetId": "$DATA_SET_ID",
"Finalized": false,
"Id": "$REVISION_ID",
"UpdatedAt": "2021-09-11T00:18:49.160000+00:00"
}

```

2. [Add the API assets to the revision](publish-API-product.md#add-api-asset "publish-API-product.md#add-api-asset").

###### Note

You will need to know the ID of the API Gateway REST API you want to import as well as the
stage.

## Step 4: Add API assets to a revision

API assets contain the information subscribers need to make calls to your API. For more
information, see [Assets](data-sets.md#assets "data-sets.md#assets").

In the following procedure, you import data assets, and then finalize the revision.

You use either the AWS Data Exchange console or the AWS CLI to add assets to a revision:

- [Adding API assets to a revision
  (console)](publish-API-product.md#add-api-assets "publish-API-product.md#add-api-assets")
- [Adding API assets to a revision
  (AWS CLI)](publish-API-product.md#add-api-assets-cli "publish-API-product.md#add-api-assets-cli")

### Adding API assets to a revision (console)

###### To add assets to the revision (console)

1. Under the **API assets** section of the data set details page, choose
   **Add API stage**.
2. Under **Select API stage**, for **Amazon API Gateway API**,
   enter an API in the input box or choose one of the following from the drop-down list:
   - **API in another AWS account** – this is a cross account API
     that you have been given permission to access.
   - **In this AWS account** – this is an API in your
     AWS account.
   1. If you chose **API in another AWS account**, enter the API ID and
      the API **Stage name** in the input boxes.
   2. If you chose **In this AWS account**, choose the API
      **Stage name** from the drop-down list###### Note

You can create a new API stage by choosing **Create new** and
following the steps in the **Create new API on Amazon API Gateway** modal.
Once the new stage has been created, repeat Step 2. 3. Under **Advanced configuration – optional**, you can choose to
**Connect existing Amazon API Gateway usage plan** to use the throttling
and quota limits as defined in the existing usage plan, and enter the **API
key**. 4. Under **Document API for subscribers**, provide details about the API
that the recipients will see after they accept the data grant.

    1. For **API name**, enter a name that recipients can use to identify
     the API asset.


    ###### Note

    If an **In this AWS account** was selected, the **API
     name** is automatically populated, which you can modify if necessary.

    If a **API in another AWS account** was selected, the
     **API name** is populated with a default name, which you
     should modify to so the recipient can easily understand what it is.
    2. For **OpenAPI 3.0 specification**, either:


    	1. Enter or copy and paste the OpenAPI 3.0 specification file.
    	2. Choose **Import from .JSON file**, and then select the .json file
    	 from your local computer to import.


    	The imported specification appears in the box.
    	3. Choose **Import from Amazon API Gateway**, and then choose a specification
    	 to import.


    	The imported specification appears in the box.
    3. For **Additional documentation - optional**, enter any additional
     information that is useful for the subscriber to know about your API. Markdown is
     supported.###### Note

You can't edit the OpenAPI specification and additional documentation after you add
this asset to a revision.

If you want to update this information, and the revision is not finalized, you can
replace the asset.

If you want to update this information, and the revision is finalized, you can create
a new revision with the updated asset. 5. Choose **Add API stage**.

A job is started to import your asset (in this case, the API) into your data
set.

###### Note

If you do not have an API on Amazon API Gateway, you will be prompted to create one. 6. After the job is finished, the **State** field in the
**Jobs** section is updated to **Completed.** 7. If you have more APIs to add, repeat Step 2. 8. Under **Revision overview**, review your revision and its assets. 9. Choose **Finalize**.

You have successfully finalized a revision for a data set.

You can [edit a revision](publish-API-product.md#edit-api-revision "publish-API-product.md#edit-api-revision") or [delete a revision](publish-API-product.md#delete-api-revision "publish-API-product.md#delete-api-revision") before adding it to a data
grant.

You are now ready to [Create a new data grant
containing APIs](publish-API-product.md#publish-api-data-product "publish-API-product.md#publish-api-data-product").

### Adding API assets to a revision (AWS CLI)

You can add API assets by running an `IMPORT_ASSET_FROM_API_GATEWAY_API`
job.

###### To add API assets to a revision (AWS CLI):

1. Use the `create-job` command to add API assets to the revision:

```
$ AWS dataexchange create-job \
  -\\-type IMPORT_ASSET_FROM_API_GATEWAY_API \
  -\\-details '{"ImportAssetFromApiGatewayApi":{"DataSetId":"$DATA_SET_ID","RevisionId":"$REVISION_ID","ApiId":"$API_ID","Stage":"$API_STAGE","ProtocolType":"REST"}}'
{
    "Arn": "arn:aws:dataexchange:us-east-1:123456789012:jobs/$JOB_ID",
    "CreatedAt": "2021-09-11T00:38:19.875000+00:00",
    "Details": {
        "ImportAssetFromApiGatewayApi": {
            "ApiId": "$API_ID",
            "DataSetId": "$DATA_SET_ID",
            "ProtocolType": "REST",
            "RevisionId": "$REVISION_ID",
            "Stage": "$API_STAGE"
        }
    },
    "Id": "$JOB_ID",
    "State": "WAITING",
    "Type": "IMPORT_ASSET_FROM_API_GATEWAY_API",
    "UpdatedAt": "2021-09-11T00:38:19.875000+00:00"
}

$ AWS dataexchange start-job -\\-job-id $JOB_ID
$ AWS dataexchange get-job -\\-job-id $JOB_ID
{
    "Arn": "arn:aws:dataexchange:us-east-1:0123456789012:jobs/$JOB_ID",
    "CreatedAt": "2021-09-11T00:38:19.875000+00:00",
    "Details": {
        "ImportAssetFromApiGatewayApi": {
            "ApiId": "$API_ID",
            "DataSetId": "$DATA_SET_ID",
            "ProtocolType": "REST",
            "RevisionId": "$REVISION_ID",
            "Stage": "$API_STAGE"
            "ApiEndpoint": "string",
            "ApiKey": "string",
            "ApiName": "string",
            "ApiDescription": "string",
            "ApiSpecificationDownloadUrl": "string",
            "ApiSpecificationDownloadUrlExpiresAt": "string"
        }
    },
    "Id": "$JOB_ID",
    "State": "COMPLETED",
    "Type": "IMPORT_ASSET_FROM_API_GATEWAY_API",
    "UpdatedAt": "2021-09-11T00:38:52.538000+00:00"
}

```

2. Use the `list-revision-assets` command to confirm that the new asset was
   created properly:

```
$ AWS dataexchange list-revision-assets \
  -\\-data-set-id $DATA_SET_ID \
  -\\-revision-id $REVISION_ID
{
    "Assets": [
    {
        "Arn": "arn:aws:dataexchange:us-east-1:123456789012:data-sets/$DATA_SET_ID/revisions/$REVISION_ID/assets/$ASSET_ID",
        "AssetDetails": {
            "ApiGatewayApiAsset": {
                "ApiEndpoint": "https://$API_ID.execute-api.us-east-1.amazonaws.com/$API_STAGE",
                "ApiId": "$API_ID",
                "ProtocolType": "REST",
                "Stage": "$API_STAGE"
            }
        },
        "AssetType": "API_GATEWAY_API",
        "CreatedAt": "2021-09-11T00:38:52.457000+00:00",
        "DataSetId": "$DATA_SET_ID",
        "Id": "$ASSET_ID",
        "Name": "$ASSET_ID/$API_STAGE",
        "RevisionId": "$REVISION_ID",
        "UpdatedAt": "2021-09-11T00:38:52.457000+00:00"
    }
    ]
}

```

You're now ready to create a new data grant containing APIs.

### Edit a revision

###### To edit the revision after you’ve finalized it

1. On the **Revision overview**, choose
   **De-finalize**.

You see a message that the revision is no longer in the finalized state. 2. To edit the revision, from **Revision overview**, choose
**Actions**, **Edit**. 3. Make your changes, and then choose **Update**. 4. Review your changes and then choose **Finalize**.

### Delete a revision

###### To delete the revision after you’ve finalized it

1. On the **Revision overview**, choose
   **Delete**.
2. Type `Delete` in the **Delete revision** dialog
   box, and then choose **Delete**.

###### Warning

This deletes the revision and all of its assets. This action can't be undone.

## Step 5: Create a new data grant

containing APIs

After you've created at least one data set and finalized a revision with assets, you're
ready to publish that data set as a part of a data grant.

###### To create a new data grant

1. In the left navigation pane of the AWS Data Exchange console, under **Exchanged data
   grants**, choose **Sent data grants**.
2. From **Sent data grants**, choose **Create data
   grant** to open the **Define data grant** wizard.
3. In the **Select owned data** set section, select the check box next
   to the data set you want to add.

###### Note

The data set you choose must have a finalized revision. Data sets without
finalized revisions can't be added to data grants.

Unlike with data sets included in data products which are shared on AWS Marketplace, data
sets added to data grants have no revision access rules, meaning a recipient of a data
grant, once the data grant is approved, will have access to all finalized revisions of
a given data set (including historical revisions finalized prior to the data grant
creation). 4. In the **Grant overview** section, enter information the recipient
will see regarding your data grant, including the **Data grant name**,
and **Data grant description**. 5. **Choose Next**. 6. In the **Recipient access information** section, under
**AWS account ID**, enter the AWS account ID of the recipient
account who should receive the data grant. 7. Also, in the **Recipient access information** section, under
**Access end date**, choose whether the data grant should run in
perpetuity, selecting **No end date**, or if it should have an end
date, selecting **Specific end date**, and choosing the desired end
date. 8. Choose **Next**. 9. In the **Review and send** section, review your data grant
information. 10. If you're sure that you want to create the data grant and send it to the chosen
recipient, choose **Create and send data grant**.

You've now completed the manual portion of creating a data grant. The data grant appears on the
**Sent data grants** tab on the **Sent data grants**
page, with a status of **Pending acceptance** until the
recipient account accepts it.
