# S3 Storage | Update

Modify the properties of an S3 bucket created using change type ID ct-1a68ck03fn98r.

**Full classification:** Management | Advanced stack components | S3 storage | Update

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-1gi93jhvj28eg |
| Current version             | 5.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Update S3 storage

Screenshot of this change type in the AMS console:

![Update S3 Bucket change type details showing ID, execution mode, version, and description.](images/guiS3UpdateCT.png)
How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.
2. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the
   **Choose by category** view.
   - **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the
     **Run RFC** page. Note that you cannot choose an older CT version with quick create.

   To sort CTs, use the **All change types** area in either the **Card** or **Table** view.
   In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable,
   a **Create with older version** option appears next to the **Create RFC** button.
   - **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to
     **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

3. On the **Run RFC** page, open the CT name area to see the CT details box.
   A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the
   **Additional configuration** area to add information about the RFC.

In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure
optional execution parameters, open the **Additional configuration** area. 4. When finished, click **Run**. If there are no errors, the **RFC successfully created**
page displays with the submitted RFC details, and the initial **Run output**. 5. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status.
Optionally, cancel the RFC or create a copy of it with the options at the top of the page.
How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or
   Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc`
   command with the two files as input. Both methods are described here.
2. Submit the RFC: `aws amscm submit-rfc --rfc-id `ID`` command with the returned RFC ID.

Monitor the RFC: `aws amscm get-rfc --rfc-id `ID`` command.
To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value=`CT_ID`
```

###### Note

You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the
change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the
RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the
[AMS Change Management API Reference](../ApiReference-cm/API_CreateRfc.md "../ApiReference-cm/API_CreateRfc.md").

_INLINE CREATE_:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

**Example with only required parameters:**

```
aws amscm create-rfc --title s3-bucket-update --change-type-id ct-1gi93jhvj28eg --change-type-version 5.0 --execution-parameters "{\"DocumentName\":\"AWSManagedServices-UpdateBucket\",\"Region\":\"`us-east-1`\",\"Parameters\":{\"BucketName\":\"`mybucket`\"}}"
```

**Example with all parameters:**

```
aws amscm create-rfc --title s3-bucket-update --change-type-id ct-1gi93jhvj28eg --change-type-version 5.0 --execution-parameters "{\"DocumentName\":\"AWSManagedServices-UpdateBucket\",\"Region\":\"`us-east-1`\",\"Parameters\":{\"BucketName\":\"`mybucket`\",\"ServerSideEncryption\":\"KmsManagedKeys\",\"KMSKeyId\":\"`arn:aws:kms:ap-southeast-2:123456789012:key/9d5948f1-2082-4c07-a183-eb829b8d81c4`\",\"Versioning\":\"`Enabled`\",\"IAMPrincipalsRequiringReadObjectAccess\":[\"`arn:aws:iam::123456789012:user/myuser`\",\"`arn:aws:iam::123456789012:role/myrole`\"],\"IAMPrincipalsRequiringWriteObjectAccess\":[\"`arn:aws:iam::123456789012:user/myuser`\",\"`arn:aws:iam::123456789012:role/myrole`\"],\"ServicesRequiringReadObjectAccess\":[\"`rds.amazonaws.com`\",\"`ec2.amazonaws.com`\",\"`logs.ap-southeast-2.amazonaws.com`\"],\"ServicesRequiringWriteObjectAccess\":[\"`rds.amazonaws.com`\",\"`ec2.amazonaws.com`\",\"`logs.ap-southeast-2.amazonaws.com`\"],\"EnforceSecureTransport\":\"`True`\",\"AccessAllowedIpRanges\":[\"`1.0.0.0/24`\",\"`2.0.0.0/24`\"]}}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a file; this example names it UpdateBucketParams.json.

```
aws amscm get-change-type-version --change-type-id "ct-1gi93jhvj28eg" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateBucketParams.json
```

2. Modify and save the UpdateBucketParams file.

**Example with all parameters (at least one parameter must be specified):**

```
{
  "DocumentName" : "AWSManagedServices-UpdateBucket",
  "Region": "us-east-1",
  "Parameters": {
    "BucketName": "mybucket",
    "ServerSideEncryption": "KmsManagedKeys",
    "KMSKeyId": "arn:aws:kms:ap-southeast-2:123456789012:key/9d5948f1-2082-4c07-a183-eb829b8d81c4",
    "Versioning": "Enabled",
    "IAMPrincipalsRequiringReadObjectAccess": [
      "arn:aws:iam::123456789012:user/myuser",
      "arn:aws:iam::123456789012:role/myrole"
    ],
    "IAMPrincipalsRequiringWriteObjectAccess": [
      "arn:aws:iam::123456789012:user/myuser",
      "arn:aws:iam::123456789012:role/myrole"
    ],
    "ServicesRequiringReadObjectAccess": [
      "rds.amazonaws.com",
      "ec2.amazonaws.com",
      "logs.ap-southeast-2.amazonaws.com"
    ],
    "ServicesRequiringWriteObjectAccess": [
      "rds.amazonaws.com",
      "ec2.amazonaws.com",
      "logs.ap-southeast-2.amazonaws.com"
    ],
    "EnforceSecureTransport": "True",
    "AccessAllowedIpRanges": [
      "1.0.0.0/24",
      "2.0.0.0/24"
    ]
  }
}
```

**Example with required parameters (at least one parameter must be specified):**

```
{
  "DocumentName" : "AWSManagedServices-UpdateBucket",
  "Region": "us-east-1",
  "Parameters": {
    "BucketName": "mybucket",
    "IAMPrincipalsRequiringWriteObjectAccess": [
      "arn:aws:iam::123456789012:role/roleA"
    ]
  }
}
```

For examples of resulting policies, see [S3 Storage Bucket Create Example Resulting Policies](deployment-advanced-s3-storage-create.md#ex-s3-create-policies "deployment-advanced-s3-storage-create.md#ex-s3-create-policies"). 3. Output the RFC template JSON file to a file named UpdateBucketRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > UpdateBucketRfc.json
```

4. Modify and save the UpdateBucketRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`5.0`",
"ChangeTypeId":         "ct-1gi93jhvj28eg",
"Title":                "`S3-Bucket-Update-RFC`"
}
```

5. Create the RFC, specifying the UpdateBucketRfc file and the UpdateBucketParams file:

```
aws amscm create-rfc --cli-input-json file://UpdateBucketRfc.json  --execution-parameters file://UpdateBucketParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start. 6. To view the S3 bucket or load objects to it, look in the execution output: Use the `stack_id` to view the bucket in the CloudFormation Console,
use the **S3BucketName** to view the bucket in the Amazon S3 Console.

###### Note

This walkthrough describes, and provides example commands for, updating an Amazon S3 storage bucket that was created with version 5.0 of the
S3 storage Create change type (ct-1a68ck03fn98r). In that version of that change type, the **AccessControl** parameter was
removed and replaced with specific parameters to allow specified services or IAM roles read or write access.

To learn more about Amazon S3, see [Amazon Simple Storage Service user Guide](https://aws.amazon.com/documentation/s3/ "https://aws.amazon.com/documentation/s3/").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-1gi93jhvj28eg](schemas.md#ct-1gi93jhvj28eg-schema-section "schemas.md#ct-1gi93jhvj28eg-schema-section").

## Example: Required Parameters

```
{
  "DocumentName" : "AWSManagedServices-UpdateBucket",
  "Region": "us-east-1",
  "Parameters": {
    "BucketName": "mybucket"
  }
}

```

## Example: All Parameters

```
{
  "DocumentName" : "AWSManagedServices-UpdateBucket",
  "Region": "us-east-1",
  "Parameters": {
    "BucketName": "mybucket",
    "ServerSideEncryption": "KmsManagedKeys",
    "KMSKeyId": "arn:aws:kms:ap-southeast-2:123456789012:key/9d5948f1-2082-4c07-a183-eb829b8d81c4",
    "Versioning": "Enabled",
    "IAMPrincipalsRequiringReadObjectAccess": [
      "arn:aws:iam::123456789012:user/myuser",
      "arn:aws:iam::123456789012:role/myrole"
    ],
    "IAMPrincipalsRequiringWriteObjectAccess": [
      "arn:aws:iam::123456789012:user/myuser",
      "arn:aws:iam::123456789012:role/myrole"
    ],
    "ServicesRequiringReadObjectAccess": [
      "rds.amazonaws.com",
      "ec2.amazonaws.com",
      "logs.ap-southeast-2.amazonaws.com"
    ],
    "ServicesRequiringWriteObjectAccess": [
      "rds.amazonaws.com",
      "ec2.amazonaws.com",
      "logs.ap-southeast-2.amazonaws.com"
    ],
    "EnforceSecureTransport": "True",
    "AccessAllowedIpRanges": [
      "1.0.0.0/24",
      "2.0.0.0/24"
    ],
    "Tags": [
      "{\"Key\": \"foo\", \"Value\": \"bar\"}",
      "{ \"Key\": \"testkey\",\"Value\": \"testvalue\" }"
    ]
  }
}

```
