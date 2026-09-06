

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# S3 Storage \| Manage Lifecycle Configuration
<a name="management-advanced-s3-storage-manage-lifecycle-configuration"></a>

Add a new lifecycle configuration, or replace an existing one for an Amazon S3 bucket.

**Full classification:** Management \| Advanced stack components \| S3 storage \| Manage lifecycle configuration

## Change Type Details
<a name="ct-1ax768xtu8c9q-MASm-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-1ax768xtu8c9q | 
| Current version | 1.0 | 
| Expected execution duration | 360 minutes | 
| AWS approval | Required | 
| Customer approval | Not required | 
| Execution mode | Automated | 

## Additional Information
<a name="management-advanced-s3-storage-manage-lifecycle-configuration-info"></a>

### Manage S3 lifecycle configuration
<a name="ex-s3-add-lifecycle-config-col"></a>

#### Adding a new or replacing an existing lifecycle configuration for an S3 bucket with the Console
<a name="s3-add-lifecycle-config-con"></a>

Screenshot of this change type in the AMS console:

![Manage lifecycle configuration details showing ID, execution mode as Automated, and version 1.0.](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiS3ManageLifecycleCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

**Note**  
When you add a lifecycle configuration from the console, you must provide a JSON string for the `LifecycleConfiguration` parameter similar to the following example:  
`{"Rules":[{"ID": "IDname","Filter": {"Prefix": "bucketprefix/"},"Status": "Enabled","Expiration": {"Days": 30},"NoncurrentVersionExpiration": {"NoncurrentDays": 30}}]}`

#### Adding a new or replacing an existing lifecycle configuration for an S3 bucket with the CLI
<a name="s3-add-lifecycle-config-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc \
--change-type-id "ct-1ax768xtu8c9q" \
--change-type-version "1.0" --title "Manage lifecycle configuration" \
--execution-parameters "{\"DocumentName\":\"AWSManagedServices-PutBucketLifecycleConfiguration\",\"Region\":\"{{us-east-1}}\",\"Parameters\":{\"BucketName\":[\"{{amzn-s3-demo-bucket}}\"],\"LifecycleConfiguration\":[\"{\\\"Rules\\\":[{\\\"Filter\\\":{\\\"Prefix\\\":\\\"documents/\\\"},\\\"Status\\\":\\\"Enabled\\\",\\\"Transitions\\\":[{\\\"Days\\\":{{365}},\\\"StorageClass\\\":\\\"{{GLACIER}}\\\"}],\\\"ID\\\":\\\"{{ExampleRule}}\\\"}]}\"], \"ReplaceExisting\": [\"True\"], \"Verification\": [\"confirm\"], \"MinimumNumberOfDaysBeforeExpiration\": [2]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it ManageS3LifecycleConfigParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-220bdb8blaixf" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > ManageS3LifecycleConfigParams.json
   ```

1. Modify and save the ManageS3LifecycleConfigParams file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-PutBucketLifecycleConfiguration",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "BucketName": ["{{amzn-s3-demo-bucket}}"],
       "LifecycleConfiguration": ["{\"Rules\":[{\"Filter\":{\"Prefix\":\"documents/\"},\"Status\":\"Enabled\",\"Transitions\":[{\"Days\":{{365}},\"StorageClass\":\"{{GLACIER}}\"}],\"ID\":\"{{ExampleRule}}\"}]}"],
       "ReplaceExisting": ["True"],
       "Verification": ["confirm"],
       "MinimumNumberOfDaysBeforeExpiration": [2]
     }
   }
   ```

1. Output the RFC template JSON file to a file named ManageS3LifecycleConfigRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > ManageS3LifecycleConfigRfc.json
   ```

1. Modify and save the ManageS3LifecycleConfigRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeId": "ct-1ax768xtu8c9q",
   "ChangeTypeVersion": "1.0",
   "Title": "{{Testing - ct-1ax768xtu8c9q Manage lifecycle configuration}}"
   }
   ```

1. Create the RFC, specifying the ManageS3LifecycleConfigRfc file and the ManageS3LifecycleConfigParams file:

   ```
   aws amscm create-rfc --cli-input-json file://ManageS3LifecycleConfigRfc.json  --execution-parameters file://ManageS3LifecycleConfigParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

#### Tips
<a name="ex-s3-add-lifecycle-config-tip"></a>

To learn more about Amazon S3, see [Amazon Simple Storage Service Documentation](https://docs.aws.amazon.com/s3/).

## Execution Input Parameters
<a name="management-advanced-s3-storage-manage-lifecycle-configuration-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-1ax768xtu8c9q](schemas.md#ct-1ax768xtu8c9q-schema-section).

## Example: Required Parameters
<a name="management-advanced-s3-storage-manage-lifecycle-configuration-ex-min"></a>

```
{
  "DocumentName" : "AWSManagedServices-PutBucketLifecycleConfiguration",
  "Region" : "us-east-1",
  "Parameters" : {
    "BucketName" : [
      "test-s3-bucket"
    ],
    "LifecycleConfiguration" : [
      "{\"Rules\":[{\"Filter\":{\"Prefix\":\"documents/\"},\"Status\":\"Enabled\",\"Transitions\":[{\"Days\":365,\"StorageClass\":\"GLACIER\"}],\"Expiration\":{\"Days\":3650},\"ID\":\"ExampleRule\"}]}"
    ],
    "Verification" : [
      "confirm"
    ],
    "MinimumNumberOfDaysBeforeExpiration" : [
      10
    ]
  }
}
```

## Example: All Parameters
<a name="management-advanced-s3-storage-manage-lifecycle-configuration-ex-max"></a>

```
{
  "DocumentName" : "AWSManagedServices-PutBucketLifecycleConfiguration",
  "Region" : "us-east-1",
  "Parameters" : {
    "BucketName" : [
      "test-s3-bucket"
    ],
    "LifecycleConfiguration" : [
      "{\"Rules\":[{\"Filter\":{\"Prefix\":\"documents/\"},\"Status\":\"Enabled\",\"Transitions\":[{\"Days\":365,\"StorageClass\":\"GLACIER\"}],\"Expiration\":{\"Days\":3650},\"ID\":\"ExampleRule\"}]}"
    ],
    "ReplaceExisting" : [
      "False"
    ],
    "Verification" : [
      "confirm"
    ],
    "MinimumNumberOfDaysBeforeExpiration" : [
      10
    ]
  }
}
```