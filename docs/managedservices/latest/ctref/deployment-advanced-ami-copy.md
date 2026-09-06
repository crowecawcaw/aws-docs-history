

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# AMI \| Copy
<a name="deployment-advanced-ami-copy"></a>

Copy an Amazon Machine Image (AMI) in your AMS account.

**Full classification:** Deployment \| Advanced stack components \| AMI \| Copy

## Change Type Details
<a name="ct-046aizcwg5idf-DAAc-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-046aizcwg5idf | 
| Current version | 1.0 | 
| Expected execution duration | 60 minutes | 
| AWS approval | Required | 
| Customer approval | Not required | 
| Execution mode | Automated | 

## Additional Information
<a name="deployment-advanced-ami-copy-info"></a>

### Copy an AMI
<a name="ex-ami-copy-col"></a>

#### Copying an AMI with the console
<a name="ami-copy-con"></a>

The following shows this change type in the AMS console.

![Copy AMI change type showing ID ct-046aizcwg5idf with version 1.0 only version.](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiAmiCopyCT.png)


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

#### Copying an AMI with the CLI
<a name="ami-copy-cli"></a>

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
aws amscm create-rfc --change-type-id "ct-046aizcwg5idf" --change-type-version "1.0" --title "Copy AMI" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-CopyAMI\",\"Region\":\"{{us-east-1}}\",\"Parameters\":{\"Name\":[\"{{AmiName}}\"],\"SourceImageId\":[\"{{ami-1234567890abcdef0}}\"],\"SourceRegion\":[\"{{ap-southeast-2}}\"],\"Encrypted\":[\"{{True}}\"],\"KmsKeyId\":[\"{{01234567-abcd-abcd-abcd-0123456789ab}}\"]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it CopyAmiParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-046aizcwg5idf" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CopyAmiParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-CopyAMI",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "Name": [
         "{{AmiName}}"
       ],
       "SourceImageId": [
         "{{ami-1234567890abcdef0}}"
       ],
       "SourceRegion": [
         "{{ap-southeast-2}}"
       ],
       "Encrypted": [
         "{{True}}"
       ],
       "KmsKeyId": [
         "{{01234567-abcd-abcd-abcd-0123456789ab}}"
       ]
     }
   }
   ```

1. Output the RFC template JSON file; this example names it CopyAmiRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CopyAmiRfc.json
   ```

1. Modify and save the CopyAmiRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion": "1.0",
     "ChangeTypeId": "ct-046aizcwg5idf",
     "Title": "{{Copy AMI}}"
   }
   ```

1. Create the RFC, specifying the CopyAmiRfc file and the CopyAmiParams file:

   ```
   aws amscm create-rfc --cli-input-json file://CopyAmiRfc.json  --execution-parameters file://CopyAmiParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

#### Tips
<a name="ex-ami-copy-tip"></a>

To learn more about copying AMIs, see [Copying an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/CopyingAMIs.html).

## Execution Input Parameters
<a name="deployment-advanced-ami-copy-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-046aizcwg5idf](schemas.md#ct-046aizcwg5idf-schema-section).

## Example: Required Parameters
<a name="deployment-advanced-ami-copy-ex-min"></a>

```
{
  "DocumentName": "AWSManagedServices-CopyAMI",
  "Region": "us-east-1",
  "Parameters": {
    "Name": [
      "AmiName"
    ],
    "SourceImageId": [
      "ami-1234567890abcdef0"
    ],
    "SourceRegion": [
      "ap-southeast-2"
    ]
  }
}
```

## Example: All Parameters
<a name="deployment-advanced-ami-copy-ex-max"></a>

```
{
  "DocumentName": "AWSManagedServices-CopyAMI",
  "Region": "us-east-1",
  "Parameters": {
    "Name": [
      "AmiName"
    ],
    "SourceImageId": [
      "ami-1234567890abcdef0"
    ],
    "SourceRegion": [
      "ap-southeast-2"
    ],
    "Encrypted": [
      "True"
    ],
    "KmsKeyId": [
      "arn:aws:kms:us-east-1:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890ab"
    ]
  }
}
```