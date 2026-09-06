

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Tag \| Delete (Managed Automation)
<a name="management-advanced-tag-delete-managed-automation"></a>

Delete tags from existing, supported resources except those in AMS infrastructure stacks (stacks named mc-\*). For Autoscaling, EC2, Elastic Load Balancing, RDS resources and S3 buckets, use automated CT ct-2zebb2czoxpjd.

**Full classification:** Management \| Advanced stack components \| Tag \| Delete (managed automation)

## Change Type Details
<a name="ct-1erytvmumckoa-MATd-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-1erytvmumckoa | 
| Current version | 1.0 | 
| Expected execution duration | 240 minutes | 
| AWS approval | Required | 
| Customer approval | Not required if submitter | 
| Execution mode | Manual | 

## Additional Information
<a name="management-advanced-tag-delete-managed-automation-info"></a>

### Delete tags (Managed Automation)
<a name="ex-tag-delete-rr-col"></a>

#### Deleting Tags (Managed Automation) with the Console
<a name="tag-delete-rr-con"></a>

Screenshot of this change type in the AMS console:

![Delete Resource Tags interface showing details for a manual change type in AWS.](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiTagDeleteRrCT.png)


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

#### Deleting Tags (Managed Automation) with the CLI
<a name="tag-delete-rr-cli"></a>

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
aws amscm create-rfc --title {{delete-tags}} --change-type-id ct-1erytvmumckoa --change-type-version 1.0 --execution-parameters '{"Description":"{{test}}","Resources":[{"ResourceArn":"{{i-abcd1234}}","RemoveTags":["Name","{{Owner}}"]},{"ResourceArn":"{{arn:aws:ec2:ap-southeast-2:123456789012:instance/i-019714a96c22f5452}}","RemoveTags":["Name","{{Owner}}"]}]}'
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema to a file in your current folder. This example names it TagDeleteParams.json.

   ```
   aws amscm create-rfc --generate-cli-skeleton > TagDeleteParams.json
   ```

1. Modify and save the TagDeleteParams.json file. For example, you can replace the contents with something like this:

   ```
   {
     "Description": "{{Delete tags}}",
     "Resources": [
       {
         "ResourceArn": "{{i-abcd1234}}",
         "RemoveTags": [
           "{{Unused tag 1}}",
           "{{Unused tag 2}}"
         ]
       },
       {
         "ResourceArn": "{{arn:aws:ec2:ap-southeast-2:123456789012:instance/i-1234567890abcdef1}}",
         "RemoveTags": [
           "{{Unused tag 1}}",
           "{{Unused tag 2}}"
         ]
       }
     ]
   }
   ```

1. Output the RFC template to a file in your current folder. This example names it TagDeleteRfc.json.

   ```
   aws amscm create-rfc --generate-cli-skeleton > TagDeleteRfc.json
   ```

1. Modify and save the TagDeleteRfc.json file.

   The internal quotation marks in the `ExecutionParameters` JSON extension must be escaped with a backslash (\\). Example:

   ```
   {
   "ChangeTypeId":         "ct-1erytvmumckoa",
   "Title":                "{{Delete-Tags-RFC}}"
   }
   ```

1. Create the RFC:

   ```
   aws amscm create-rfc --cli-input-json file://TagDeleteRfc.json  --execution-parameters file://TagDeleteParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

#### Tips
<a name="ex-tag-delete-rr-tip"></a>

This is a manual change type (an AMS operator must review and run the CT), which means that the RFC can take longer to run and you might have to communicate with AMS through the RFC details page correspondance option. Additionally, if you schedule a manual change type RFC, be sure to allow at least 24 hours, if approval does not happen before the scheduled start time, the RFC is rejected automatically.

## Execution Input Parameters
<a name="management-advanced-tag-delete-managed-automation-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-1erytvmumckoa](schemas.md#ct-1erytvmumckoa-schema-section).

## Example: Required Parameters
<a name="management-advanced-tag-delete-managed-automation-ex-min"></a>

```
Example not available.
```

## Example: All Parameters
<a name="management-advanced-tag-delete-managed-automation-ex-max"></a>

```
{
  "Description": "Remove tags from instances",
  "Resources": [
    {
      "ResourceArn": "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0",
      "RemoveTags": ["k1", "k2"]
    },
    {
      "ResourceArn": "i-0fedcba0987654321",
      "RemoveTags": ["k1", "k2"]
    }
  ],
  "Priority": "Medium"
}
```