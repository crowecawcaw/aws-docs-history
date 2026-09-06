

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# State \| Enable
<a name="management-ams-state-enable"></a>

Enable AMS Resource Scheduler in the account where it was previously disabled. This will re-enable scheduling of resources for automatic start or stop actions where the resources are already tagged with a valid schedule. Make sure to verify currently tagged resources and schedules before enabling the scheduler.

**Full classification:** Management \| AMS Resource Scheduler \| State \| Enable

## Change Type Details
<a name="ct-2wrvu4kca9xky-MASe-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-2wrvu4kca9xky | 
| Current version | 2.0 | 
| Expected execution duration | 360 minutes | 
| AWS approval | Required | 
| Customer approval | Not required | 
| Execution mode | Automated | 

## Additional Information
<a name="management-ams-state-enable-info"></a>

### Enable
<a name="ex-res-sched-enable-col"></a>

#### Enabling AMS Resource Scheduler with the console
<a name="res-sched-state-enable-con"></a>

The following shows this change type in the AMS console.

![AMS Resource Scheduler configuration panel showing ID, execution mode, and version details.](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiResSchedStateEnableCT.png)


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

#### Enabling AMS Resource Scheduler with the CLI
<a name="res-sched-state-enable-cli"></a>

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
aws amscm create-rfc --change-type-id "ct-2wrvu4kca9xky" --change-type-version "2.0" --title "{{Enable AMS Resource Scheduler}}" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-HandleAMSResourceSchedulerStack-Admin\",\"Region\":\"{{us-east-1}}\",\"Parameters\":{\"SchedulingActive\":[\"Yes\"],\"Action\":\"Update\"}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a JSON file; this example names it EnableResSchedulerParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-2wrvu4kca9xky" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > EnableResSchedulerParams.json
   ```

1. Modify and save the EnableResSchedulerParams file.

   ```
   {
     "DocumentName" : "AWSManagedServices-EnableOrDisableAMSResourceScheduler",
     "Region" : "{{us-east-1}}",
     "Parameters" : {
       "SchedulingActive" : ["Yes"],
       "Action" : "Update"
     }
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it EnableResSchedulerRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > EnableResSchedulerRfc.json
   ```

1. Modify and save the EnableResSchedulerRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{2.0}}",
   "ChangeTypeId":         "ct-2wrvu4kca9xky",
   "Title":                "{{Enable AMS Resource Scheduler}}"
   }
   ```

1. Create the RFC, specifying the EnableResSchedulerRfc file and the EnableResSchedulerParams file:

   ```
   aws amscm create-rfc --cli-input-json file://EnableResSchedulerRfc.json --execution-parameters file://EnableResSchedulerParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

#### Tips
<a name="ex-res-sched-enable-tip"></a>

For more information, see [How the AMS Resource Scheduler works](https://docs.aws.amazon.com/managedservices/latest/userguide/resource-scheduler-how-works.html).

AMS Resource Scheduler is based on the AWS Instance Scheduler; to learn more, see [AWS Instance Scheduler](https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/welcome.html).

## Execution Input Parameters
<a name="management-ams-state-enable-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-2wrvu4kca9xky](schemas.md#ct-2wrvu4kca9xky-schema-section).

## Example: Required Parameters
<a name="management-ams-state-enable-ex-min"></a>

```
Example not available.
```

## Example: All Parameters
<a name="management-ams-state-enable-ex-max"></a>

```
{
  "DocumentName" : "AWSManagedServices-HandleAMSResourceSchedulerStack-Admin",
  "Region" : "us-east-1",
  "Parameters" : {
    "SchedulingActive" : ["Yes"],
    "Action" : "Update"
  }
}
```