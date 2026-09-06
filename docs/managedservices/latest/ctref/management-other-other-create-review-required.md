

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Other \| Create (Review Required)
<a name="management-other-other-create-review-required"></a>

Use to request manual creation of a resource.

**Full classification:** Management \| Other \| Other \| Create (review required)

## Change Type Details
<a name="ct-1e1xtak34nx76-MOOc-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-1e1xtak34nx76 | 
| Current version | 1.0 | 
| Expected execution duration | 240 minutes | 
| AWS approval | Required | 
| Customer approval | Not required if submitter | 
| Execution mode | Manual | 

## Additional Information
<a name="management-other-other-create-review-required-info"></a>

### Create Other Other CTs
<a name="ex-other-other-create-col"></a>

#### Creating an Other Other Create RFC with the Console
<a name="other-other-create-con"></a>

Screenshot of this change type in the AMS console:

![Change type Create other interface showing description, ID, version, and execution mode fields.](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiOtherCreate.png)


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

#### Creating an Other Other Create RFC with the CLI
<a name="other-other-create-cli"></a>

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
aws amscm create-rfc --change-type-id "ct-1e1xtak34nx76" --change-type-version "1.0" --title "{{TITLE}}" --execution-parameters "{\"Comment\": \"{{WHAT_TO_CREATE}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file named OtherCreateParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-1e1xtak34nx76" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > OtherCreateParams.json
   ```

1. Modify and save the OtherCreateParams file (example includes optional `Priority` parameter). For example, you can replace the contents with something like this:

   ```
   {
   "Comment":          "{{WHAT-TO-CREATE}}",
   "Priority":         "{{Medium}}"
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it OtherCreateRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > OtherCreateRfc.json
   ```

1. Modify and save the OtherCreateRfc.json file. For example, you can replace the contents with something like this:.

   ```
   {
   "ChangeTypeId":         "ct-1e1xtak34nx76",
   "ChangeTypeVersion":    "{{1.0}}",	
   "Title":                "{{TITLE}}"
   }
   ```

1. Create the RFC, specifying the OtherCreateRfc file and the OtherCreateParams file:

   ```
   aws amscm create-rfc --cli-input-json file://OtherCreateRfc.json  --execution-parameters file://OtherCreateParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

#### Tips
<a name="ex-other-other-create-tip"></a>

**Note**  
To update an existing resource, use [Update Other Other CTs](management-other-other-update-review-required.md#ex-other-other-update-col).

This is a manual change type (an AMS operator must review and run the CT), which means that the RFC can take longer to run and you might have to communicate with AMS through the RFC details page correspondance option. Additionally, if you schedule a manual change type RFC, be sure to allow at least 24 hours, if approval does not happen before the scheduled start time, the RFC is rejected automatically.

Use this CT when you can't find a change type for what you want; however, if you are unsure about specifying parameters in an existing CT, it is better to submit a service request for help. For information on submitting service requests, see [Service Request Examples](https://docs.aws.amazon.com/managedservices/latest/userguide/serv-req-mgmt-examples.html).

To update an existing resource, use [Update Other Other CTs](management-other-other-update-review-required.md#ex-other-other-update-col).

## Execution Input Parameters
<a name="management-other-other-create-review-required-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-1e1xtak34nx76](schemas.md#ct-1e1xtak34nx76-schema-section).

## Example: Required Parameters
<a name="management-other-other-create-review-required-ex-min"></a>

```
{
  "Comment": "This is a test comment"
}
```

## Example: All Parameters
<a name="management-other-other-create-review-required-ex-max"></a>

```
{
  "Comment": "This is a test comment",
  "Priority": "High",
  "RelatedIds": ["foo", "bar", "baz"]
}
```