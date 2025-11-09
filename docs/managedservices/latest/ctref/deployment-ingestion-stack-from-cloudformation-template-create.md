# Stack from CloudFormation Template | Create

Create a stack by pointing to a customized CloudFormation (CFN) template in an S3 bucket, or by pasting the contents of that template as input to this change type.

**Full classification:** Deployment | Ingestion | Stack from CloudFormation Template | Create

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-36cn2avfrrj9v |
| Current version             | 2.0              |
| Expected execution duration | 360 minutes      |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Create CloudFormation ingest stack

![Create Stack From CloudFormation Template interface showing description, ID, and version.](images/guiCfnIngestCT.png)
**To create a CloudFormation ingest stack using the console**

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
**To create a CloudFormation ingest stack using the CLI**

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

1. Prepare the CloudFormation template that you will use to create the stack,
   and upload it to your S3 bucket. For important details, see
   [AWS CloudFormation Ingest Guidelines, Best Practices, and Limitations](../appguide/cfn-author-templates.md "../appguide/cfn-author-templates.md").
2. Create and submit the RFC to AMS:
   1. Create and save the execution parameters JSON file, include the CloudFormation template
      parameters that you want. The following example names it
      CreateCfnParams.json.

   Example Web application stack CreateCfnParams.json file:

   ```
   {
     "Name": "`cfn-ingest`",
     "Description": "`CFNIngest Web Application Stack`",
     "VpcId": "`VPC_ID`",
     "CloudFormationTemplateS3Endpoint": "`$S3_URL`",
     "TimeoutInMinutes": 120,
     "Tags": [
      {
       "Key":   "`Enviroment Type`"
       "Value": "`Dev`",
      },
      {
       "Key":   "`Application`"
       "Value": "`PCS`",
      }
     ],
     "Parameters": [
      {
       "Name": "`Parameter-for-S3Bucket-Name`",
       "Value":  "`BUCKET-NAME`"
      },
      {
       "Name": "`Parameter-for-Image-Id`",
       "Value":  "`AMI-ID`"
      }
     ],
   }
   ```

   Example SNS topic CreateCfnParams.json file:

   ```
   {
     "Name": "cfn-ingest",
     "Description": "`CFNIngest Web Application Stack`",
     "CloudFormationTemplateS3Endpoint": "`$S3_URL`",
     "Tags": [
       {"Key": "`Enviroment Type`", "Value": "`Dev`"}
     ],
     "Parameters": [
       {"Name": "`TopicName`", "Value": "`MyTopic1`"}
     ]
   }
   ```

3. Create and save the RFC parameters JSON file with the following content. The following example
   names it CreateCfnRfc.json file:

```
{
   "ChangeTypeId": "ct-36cn2avfrrj9v",
   "ChangeTypeVersion": "2.0",
   "Title": "`cfn-ingest`"
}
```

4. Create the RFC, specifying the CreateCfnRfc file and the CreateCfnParams file:

```
aws amscm create-rfc --cli-input-json file://CreateCfnRfc.json  --execution-parameters file://CreateCfnParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

###### Note

This change type is at version 2.0 and is automated (not manually executed). This allows the
CT execution to go more quickly, and, a new
parameter, **CloudFormationTemplate**, allows you to paste into the RFC a custom CloudFormation template. Additionally,
In this version, we do not attach the default AMS security groups if the you specify your own security groups.
If you do not specify your own security groups in the request, AMS will attach the AMS default security groups.
In CFN Ingest v1.0, we always appended the AMS default security groups whether or not you provided your own
security groups.

AMS has enabled 17 AMS Self-Provisioned services for use in this change type. For information about supported resources,
see [CloudFormation Ingest Stack: Supported Resources](../appguide/cfn-ingest-supp-services.md "../appguide/cfn-ingest-supp-services.md").

###### Note

Version 2.0 accepts an S3 endpoint that is not a presigned URL.

If you use the previous version of this CT, the **CloudFormationTemplateS3Endpoint** parameter value must be a presigned URL.

Example command for generating a presigned S3 bucket URL (Mac/Linux):

```
export S3_PRESIGNED_URL=$(aws s3 presign DASHDASHexpires-in 86400 s3://`BUCKET_NAME`/`CFN_TEMPLATE`.json)
```

Example command for generating a presigned S3 bucket URL (Windows):

```
for /f %i in ('aws s3 presign DASHDASHexpires-in 86400 s3://`BUCKET_NAME`/`CFN_TEMPLATE`.json') do set S3_PRESIGNED_URL=%i
```

See also [Creating Pre-Signed URLs for Amazon S3 Buckets](../../../sdk-for-go/v1/developer-guide/s3-example-presigned-urls.md "../../../sdk-for-go/v1/developer-guide/s3-example-presigned-urls.md").

###### Note

If the S3 bucket exists in an AMS account, you must use your AMS
credentials for this command. For example, you may need to append `--profile saml` after obtaining your AMS AWS Security Token Service (AWS STS) credentials.

Related change types:
[Approve a CloudFormation ingest stack changeset](management-custom-stack-from-cloudformation-template-approve-changeset-and-update.md#ex-cfn-ingest-approve-and-update-col "management-custom-stack-from-cloudformation-template-approve-changeset-and-update.md#ex-cfn-ingest-approve-and-update-col"),
[Update AWS CloudFormation ingest stack](management-custom-stack-from-cloudformation-template-update.md#ex-cfn-ingest-update-col "management-custom-stack-from-cloudformation-template-update.md#ex-cfn-ingest-update-col")

To learn more about AWS CloudFormation, see [AWS Cloud​Formation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/").
To see CloudFormation templates, open the AWS CloudFormation
[Template Reference](../../../AWSCloudFormation/latest/UserGuide/template-reference.md "../../../AWSCloudFormation/latest/UserGuide/template-reference.md").

The template is validated to ensure that it can be created in an AMS account. If
it passes validation, it's updated to include any resources or configurations
required for it to conform with AMS. This includes adding resources such as Amazon CloudWatch
alarms in order to allow AMS Operations to monitor the stack.

The RFC is rejected if any of the following are true:

- RFC JSON Syntax is incorrect or does not follow the given format.
- The provided S3 bucket presigned URL is not valid.
- The template is not valid AWS CloudFormation syntax.
- The template does not have defaults set for all parameter values.
- The template fails AMS validation. For AMS validation steps, see the information later in this topic.
  The RFC fails if the CloudFormation stack fails to create due to a resource creation issue.

To learn more about CFN validation and validator, see
[Template Validation](../appguide/cfn-author-templates.md "../appguide/cfn-author-templates.md") and [CloudFormation ingest stack: CFN validator examples](../appguide/ex-cfn-ingest-validator.md "../appguide/ex-cfn-ingest-validator.md").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-36cn2avfrrj9v](schemas.md#ct-36cn2avfrrj9v-schema-section "schemas.md#ct-36cn2avfrrj9v-schema-section").

## Example: Required Parameters

```
Example not available.
```

## Example: All Parameters

```
Example not available.
```
