

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Management Account \| Create StackSets Stack (Managed Automation)
<a name="deployment-managed-management-account-create-stacksets-stack-managed-automation"></a>

Create AWS CloudFormation (CFN) StackSets stacks and deploy the stack instances. Use the CloudFormation StackSets feature to create stacks across multiple accounts.

**Full classification:** Deployment \| Managed landing zone \| Management account \| Create StackSets stack (managed automation)

## Change Type Details
<a name="ct-16pknsfa8lul7-DMMc-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-16pknsfa8lul7 | 
| Current version | 1.0 | 
| Expected execution duration | 240 minutes | 
| AWS approval | Required | 
| Customer approval | Not required if submitter | 
| Execution mode | Manual | 

## Additional Information
<a name="deployment-managed-management-account-create-stacksets-stack-managed-automation-info"></a>

### Create a Stacksets stack
<a name="ex-man-lz-mgmt-acct-stacksets-stack-create-col"></a>

#### Creating a Stacksets stack with the console
<a name="malz-mgmt-acct-stacksets-stack-create-con"></a>

Screenshot of this change type in the AMS console:

![Details of a StackSets stack creation change type, including ID, execution mode, and description.](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiManLzStckstsStckCreateCT.png)


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

#### Creating a Stacksets stack with the CLI
<a name="man-lz-mgmt-acct-stacksets-stack-create-cli"></a>

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
**Note**  
Run this change type from your Management account.

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-16pknsfa8lul7" --change-type-version "1.0" --title "{{Create StackSets Stack}}" --execution-parameters "{\"Name\": \"{{Stackset name}}\", \"Region\": \"{{us-east-1}}\", \"OuId"\: \"{{ou-cccc-00000000}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it UpdateStacksetsStackParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-1v9g9n30woc8h" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateStacksetsStackParams.json
   ```

1. Modify and save the UpdateStacksetsStackParams file. For example, you can replace the contents with something like this:

   ```
   {
      "CloudFormationTemplate": "{{template}}",
      "CloudFormationTemplateS3Endpoint": "{{S3 link of the template}}",
      "Description": "{{Create Stackset}}",
      "Name": "{{test-stackset}}",
      "OuId": ["{{ou-cccc-00000000}}"],
      "Region": "{{us-east-1}}",
      "Parameters": [
        { "Name": "{{test-value}}",
          "Value": "{{test-value}}" }  
      ],
      "Tags": [
        {
          "Key": "{{key1}}",
          "Value": "{{value1}}"
        },
        {
          "Key": "{{key2}}",
          "Value": "{{value2}}"
        }
      ],
      "Priority": "{{High}}"
    }
   ```

1. Output the RFC template JSON file to a file; this example names it UpdateStacksetsStackRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > UpdateStacksetsStackRfc.json
   ```

1. Modify and save the UpdateStacksetsStackRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion": "1.0",
     "ChangeTypeId": "ct-16pknsfa8lul7",
     "Title": "{{Create StackSets Stack}} "
   }
   ```

1. Create the RFC, specifying the UpdateStacksetsStack Rfc file and the UpdateStacksetsStackParams file:

   ```
   aws amscm create-rfc --cli-input-json file://UpdateStacksetsStackRfc.json  --execution-parameters file://UpdateStacksetsStackParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

#### Tips
<a name="ex-man-lz-mgmt-acct-stacksets-stack-create-tip"></a>
+ For CloudFormation details, see [Create a stack set](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.html)
+ For general CloudFormation information on stack sets, see [StackSets concepts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html)
+ To learn more about AMS multi-account landing zone, see [ AWS Managed Services (AMS) Now Offers Managed Landing Zones](https://aws.amazon.com/about-aws/whats-new/2019/10/aws-managed-services-now-offers-managed-landing-zones/).

## Execution Input Parameters
<a name="deployment-managed-management-account-create-stacksets-stack-managed-automation-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-16pknsfa8lul7](schemas.md#ct-16pknsfa8lul7-schema-section).

## Example: Required Parameters
<a name="deployment-managed-management-account-create-stacksets-stack-managed-automation-ex-min"></a>

```
{
  "Description": "AMSTestCT - Create a test stackset",
  "Name": "test-stackset",
  "OuId": ["ou-cccc-00000000"],
  "Region": "us-east-1"
}
```

## Example: All Parameters
<a name="deployment-managed-management-account-create-stacksets-stack-managed-automation-ex-max"></a>

```
{
  "CloudFormationTemplate": "template",
  "CloudFormationTemplateS3Endpoint": "https://s3.amazonaws.com/cf-templates-33kj7hiuwdk9-us-east-1/2017261mYA-stm-dynamic-sqs-no-params-sept-2017.template",
  "Description": "AMSTestCT - Create a test stackset",
  "Name": "test-stackset",
  "OuId": ["ou-cccc-00000000"],
  "Region": "us-east-1",
  "Parameters": [
    { "Name": "test-value",
      "Value": "test-value" }  
  ],
  "Tags": [
    {
      "Key": "key1",
      "Value": "value1"
    },
    {
      "Key": "key2",
      "Value": "value2"
    }
  ],
  "Priority": "High"
}
```