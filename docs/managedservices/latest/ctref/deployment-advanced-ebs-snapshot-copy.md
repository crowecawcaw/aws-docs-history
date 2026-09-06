

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# EBS Snapshot \| Copy
<a name="deployment-advanced-ebs-snapshot-copy"></a>

Copy an Elastic Block Store (EBS) snapshot in your AMS account.

**Full classification:** Deployment \| Advanced stack components \| EBS snapshot \| Copy

## Change Type Details
<a name="ct-3lkbpansfv69k-DAEc-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-3lkbpansfv69k | 
| Current version | 2.0 | 
| Expected execution duration | 60 minutes | 
| AWS approval | Required | 
| Customer approval | Not required | 
| Execution mode | Automated | 

## Additional Information
<a name="deployment-advanced-ebs-snapshot-copy-info"></a>

### Copy EBS snapshot
<a name="ex-ebs-snpsht-copy-col"></a>

#### Copying EBS Snapshots with the Console
<a name="ebs-snpsht-copy-con"></a>

![EBS snapshot details showing ID and version 2.0 in the Copy EBS Snapshot interface.](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiEbsSnpshtCopyCT.png)


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

#### Copying EBS Snapshots with the CLI
<a name="ebs-snpsht-copy-cli"></a>

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

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-3lkbpansfv69k" --change-type-version "2.0" --title "{{Copy EBS snapshot}}" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-CopyEBSSnapshot\",\"Region\":\"{{us-east-1}}\",\"Parameters\":{\"SourceSnapshotId\":[\"{{SNAPSHOT_ID}}\"],\"SourceRegion\":[\"{{ap-southeast-2}}\"],\"KmsKeyId\":[\"{{KEY_ID}}\"],\"Description\":[\"{{test-snapshot}}\"]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it CopyEbsSnpshtParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-3lkbpansfv69k" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CopyEbsSnpshtParams.json
   ```

1. Modify and save the CopyEbsSnpshtParams file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-CopyEBSSnapshot",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "SourceSnapshotId": [
         "{{SNAPSHOT_ID}}"
       ],
       "SourceRegion": [
         "{{ap-southeast-2}}"
       ],
       "KmsKeyId": [
         "{{KEY_ID}}"
       ],
       "Description": [
         "{{test-snapshot}}"
       ]
     }
   }
   ```

1. Output the RFC template JSON file to a file; this example names it CopyEbsSnpshtRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CopyEbsSnpshtRfc.json
   ```

1. Modify and save the CopyEbsSnpshtRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion": "2.0",
     "ChangeTypeId": "ct-3lkbpansfv69k",
     "Title": "{{Copy EBS snapshot}}"
   }
   ```

1. Create the RFC, specifying the CopyEbsSnpshtRfc file and the CopyEbsSnpshtParams file:

   ```
   aws amscm create-rfc --cli-input-json file://CopyEbsSnpshtRfc.json  --execution-parameters file://CopyEbsSnpshtParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

#### Tips
<a name="ex-ebs-snpsht-copy-tip"></a>

**Note**  
A typical use for the EBS snapshot share and copy CTs would be:  
In account A, use the [Share EBS snapshot](management-advanced-ebs-snapshot-share.md#ex-ebs-snpsht-share-col) CT to share the snapshot with account B.
In account B, use the EBS snapshot copy CT to copy the snapshot to the AWS Region for account B.

**Important**  
This change type version, 2.0, removes several parameters, **TargetParameterName**, **Targets**, **MaxConcurrency**, and **MaxErrors**; and introduces one new parameter, **SourceSnapshotId**.

To learn more about Amazon EBS snapshots, see [Amazon EBS Snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html).

## Execution Input Parameters
<a name="deployment-advanced-ebs-snapshot-copy-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-3lkbpansfv69k](schemas.md#ct-3lkbpansfv69k-schema-section).

## Example: Required Parameters
<a name="deployment-advanced-ebs-snapshot-copy-ex-min"></a>

```
{
  "DocumentName": "AWSManagedServices-CopyEBSSnapshot",
  "Region": "us-east-1",
  "Parameters": {
    "SourceRegion": [
      "us-east-1"
    ],
    "SourceSnapshotId": [
      "snap-1234567890abcdef0"
    ]
  }
}
```

## Example: All Parameters
<a name="deployment-advanced-ebs-snapshot-copy-ex-max"></a>

```
{
  "DocumentName": "AWSManagedServices-CopyEBSSnapshot",
  "Region": "us-east-1",
  "Parameters": {
    "SourceRegion": [
      "us-east-1"
    ],
    "SourceSnapshotId": [
      "snap-1234567890abcdef0"
    ],
    "KmsKeyId": [
      "01234567-abcd-abcd-abcd-0123456789ab"
    ],
    "Description": [
      "my-snapshot"
    ]
  }
}
```