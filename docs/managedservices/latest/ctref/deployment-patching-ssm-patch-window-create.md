

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# SSM Patch Window \| Create
<a name="deployment-patching-ssm-patch-window-create"></a>

Create an AWS Systems Manager (SSM) patch window for patching to take place on instances with the specified PatchGroup. The patch window is an SSM resource that you can manage with the SSM console.

**Full classification:** Deployment \| Patching \| SSM patch window \| Create

## Change Type Details
<a name="ct-0el2j07llrxs7-DPSc-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-0el2j07llrxs7 | 
| Current version | 1.0 | 
| Expected execution duration | 60 minutes | 
| AWS approval | Required | 
| Customer approval | Not required | 
| Execution mode | Automated | 

## Additional Information
<a name="deployment-patching-ssm-patch-window-create-info"></a>

### Create SSM Patch Window
<a name="ex-patch-window-create-col"></a>

#### Creating an SSM patch window with the Console
<a name="patch-window-create-con"></a>

Screenshot of this change type in the AMS console:

![Create SSM Patch Window page showing description, ID ct-0el2j07lirxs7, and Version 1.0.](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiPatchWindowCT.png)


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

#### Creating an SSM patch window with the CLI
<a name="patch-window-create-cli"></a>

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
aws amscm create-rfc --title {{my-test-patchwindow}} --changetype-id ct-0el2j07llrxs7 --change-type-version 1.0 --execution-parameters '{"Cutoff":{{2}}, "Description":"{{Test}}", "Duration":{{24}}, "MaxConcurrency":"{{10}}", "MaxErrors":"{{12}}", "NotificationEmails":["{{test@supertest.com}}"], "PatchGroup":"{{test-patch-group}}", "Schedule":"{{cron(0 3 ? * 6L *)}}", "ScheduleTimeZone": "{{Africa/Harare}}"}'
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a JSON file; this example names it CreatePatchWindowParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-0el2j07llrxs7" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreatePatchWindowParams.json
   ```

1. Modify and save the CreatePatchWindowParams file.

   ```
   {
   "Cutoff": {{23}},
   "Description": "{{Required param given test}}",
   "Duration": {{24}},
   "EndDate": "{{2008-09-15T15:53:00Z}}",
   "MaxConcurrency": "{{10}}",
   "MaxErrors": "{{12}}",
   "Name": "{{Test1}}",
   "NotificationEmails": ["{{email@example.com}}"],
   "PatchGroup": "{{Prod}}",
   "Schedule": "{{cron(0 3 ? * 6L *)}}",
   "ScheduleTimeZone": "{{Africa/Harare}}",
   "ScheduleOffset": "{{0}}",
   "StartDate": "{{2008-09-15T15:53:00Z}}"
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it CreatePatchWindowRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreatePatchWindowRfc.json
   ```

1. Modify and save the CreatePatchWindowRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{1.0}}",	
   "ChangeTypeId":         "ct-0el2j07llrxs7",
   "Title":                "{{Patch-Window-Create-RFC}}"
   }
   ```

1. Create the RFC, specifying the CreatePatchWindowRfc file and the CreatePatchWindowParams file:

   ```
   aws amscm create-rfc --cli-input-json file://CreatePatchWindowRfc.json --execution-parameters file://CreatePatchWindowParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

1. To view the SSM patch baseline, look in the execution output: Use the stack\_id to view the patch baseline in the Systems Manager console.

#### Tips
<a name="ex-patch-window-create-tip"></a>
+ To learn more about AWS SSM patch windows, see "Maintenance Window" at [ Patching your Windows EC2 instances using AWS Systems Manager Patch Manager](https://aws.amazon.com/blogs/mt/patching-your-windows-ec2-instances-using-aws-systems-manager-patch-manager/).
+ To create an SSM patch baseline, see [SSM Patch Window \| Create](https://docs.aws.amazon.com/managedservices/latest/ctref/deployment-patching-ssm-patch-window-create.html).

  To update a custom Maintenance Window, see [Updating an SSM Patch Window](https://docs.aws.amazon.com/managedservices/latest/ctref/ex-patch-window-update-col.html).

  To delete a custom Maintenance Window, see [Delete stack](https://docs.aws.amazon.com/managedservices/latest/ctref/ex-stack-delete-col.html).

## Execution Input Parameters
<a name="deployment-patching-ssm-patch-window-create-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-0el2j07llrxs7](schemas.md#ct-0el2j07llrxs7-schema-section).

## Example: Required Parameters
<a name="deployment-patching-ssm-patch-window-create-ex-min"></a>

```
Example not available.
```

## Example: All Parameters
<a name="deployment-patching-ssm-patch-window-create-ex-max"></a>

```
{
  "Cutoff": 23,
  "Description": "Required param given test",
  "Duration": 24,
  "EndDate": "2008-09-15T15:53:00Z",
  "MaxConcurrency": "10",
  "MaxErrors": "12",
  "Name": "Test1",
  "NotificationEmails": ["email1@example.com"],
  "PatchGroup": "Prod",
  "Schedule": "cron(0 0 0 ? * 3#2 *)",
  "ScheduleOffset": 1,
  "ScheduleTimeZone": "Africa/Harare",
  "StartDate": "2008-09-15T15:53:00Z"
}
```