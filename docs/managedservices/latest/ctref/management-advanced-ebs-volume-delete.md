

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# EBS Volume \| Delete
<a name="management-advanced-ebs-volume-delete"></a>

Delete Elastic Block Store (EBS) volumes in an available state. Volumes that are not attached to an instance are in an available state and can be deleted.

**Full classification:** Management \| Advanced stack components \| EBS Volume \| Delete

## Change Type Details
<a name="ct-3e3h8u0sp5z80-MAEd-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-3e3h8u0sp5z80 | 
| Current version | 2.0 | 
| Expected execution duration | 60 minutes | 
| AWS approval | Required | 
| Customer approval | Not required | 
| Execution mode | Automated | 

## Additional Information
<a name="management-advanced-ebs-volume-delete-info"></a>

### Delete EBS volume
<a name="ex-ebs-delete-col"></a>

#### Deleting EBS Volumes with the Console
<a name="ebs-vol-delete-con"></a>

![Delete EBS Volumes page showing description, ID ct-3e3h8u0sp5z80, and version 1.0.](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiEbsVolDeleteCT.png)


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

#### Deleting EBS Volumes with the CLI
<a name="ebs-vol-delete-cli"></a>

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
aws amscm create-rfc --change-type-id "ct-3e3h8u0sp5z80" --change-type-version "2.0" --title "{{Delete Ebs Volumes}}" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-DeleteEBSVolumesV2\",\"Region\":\"{{us-east-1}}\",\"Parameters\":{\"VolumeIds\":[\"{{vol-01234567891234501}}\",\"{{vol-01234567891234502}}\"],\"CreateBackup\":\"{{true}}\", \"DeleteStackVolume\":\"{{true}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it DeleteEbsVolParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-3e3h8u0sp5z80" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > DeleteEbsVolParams.json
   ```

1. Modify and save the DeleteEbsVolParams file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-DeleteEBSVolumes",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "VolumeIds": [
         "{{vol-01234567891234501}}",
         "{{vol-01234567891234502}}"
       ],
       "CreateBackup": [
         {{true}}
       ],
       "DeleteStackVolume": [
         {{true}}
       ]
     }
   }
   ```

1. Output the RFC template JSON file to a file; this example names it DeleteEbsVolRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > DeleteEbsVolRfc.json
   ```

1. Modify and save the DeleteEbsVolRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{2.0}}",
   "ChangeTypeId":         "ct-3e3h8u0sp5z80",
   "Title":                "{{EBS-Volumes-Delete-RFC}}"
   }
   ```

1. Create the RFC, specifying the DeleteEbsVolRfc file and the DeleteEbsVolParams file:

   ```
   aws amscm create-rfc --cli-input-json file://DeleteEbsVolRfc.json  --execution-parameters file://DeleteEbsVolParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

#### Tips
<a name="ex-ebs-delete-tip"></a>

To learn more about Amazon EBS volumes, see [Amazon Elastic Block Store](https://aws.amazon.com/ebs/).

## Execution Input Parameters
<a name="management-advanced-ebs-volume-delete-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-3e3h8u0sp5z80](schemas.md#ct-3e3h8u0sp5z80-schema-section).

## Example: Required Parameters
<a name="management-advanced-ebs-volume-delete-ex-min"></a>

```
{
  "DocumentName": "AWSManagedServices-DeleteEBSVolumesV2",
  "Region": "us-east-1",
  "Parameters": {
    "VolumeIds": [
      "vol-01234567891234501",
      "vol-01234567891234502",
      "vol-01234567891234503",
      "vol-01234567891234504",
      "vol-01234567891234505",
      "vol-01234567891234506",
      "vol-01234567891234507",
      "vol-01234567891234508",
      "vol-01234567891234509",
      "vol-01234567891234510"
    ],
    "CreateBackup": true,
    "DeleteStackVolume": true
  }
}
```

## Example: All Parameters
<a name="management-advanced-ebs-volume-delete-ex-max"></a>

```
{
  "DocumentName": "AWSManagedServices-DeleteEBSVolumesV2",
  "Region": "us-east-1",
  "Parameters": {
    "VolumeIds": [
      "vol-01234567891234501",
      "vol-01234567891234502",
      "vol-01234567891234503",
      "vol-01234567891234504",
      "vol-01234567891234505",
      "vol-01234567891234506",
      "vol-01234567891234507",
      "vol-01234567891234508",
      "vol-01234567891234509",
      "vol-01234567891234510",
      "vol-01234567891234511",
      "vol-01234567891234512",
      "vol-01234567891234513",
      "vol-01234567891234514",
      "vol-01234567891234515",
      "vol-01234567891234516",
      "vol-01234567891234517",
      "vol-01234567891234518",
      "vol-01234567891234519",
      "vol-01234567891234520"
    ],
    "CreateBackup": true,
    "DeleteStackVolume": true
  }
}
```