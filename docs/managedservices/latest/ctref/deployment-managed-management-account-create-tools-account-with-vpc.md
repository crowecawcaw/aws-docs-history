

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Management Account \| Create Tools Account (With VPC)
<a name="deployment-managed-management-account-create-tools-account-with-vpc"></a>

Create a managed AWS landing zone tools account and a VPC with a private subnet, an isolated private subnet, and a public subnet. Optionally, also create an AWS Backup plan with up to four different rules. Managed AWS landing zone core accounts must already be onboarded to AWS Managed Services (AMS).

**Full classification:** Deployment \| Managed landing zone \| Management account \| Create tools account (with VPC)

## Change Type Details
<a name="ct-2j7q1hgf26x5c-DMMc-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-2j7q1hgf26x5c | 
| Current version | 2.0 | 
| Expected execution duration | 3600 minutes | 
| AWS approval | Required | 
| Customer approval | Not required | 
| Execution mode | Automated | 

## Additional Information
<a name="deployment-managed-management-account-create-tools-account-with-vpc-info"></a>

### Create Tools account with VPC
<a name="ex-malz-mgmt-acct-create-tools-acct-col"></a>

#### Management account: Creating a Management account Tools account with the console
<a name="ex-malz-mgmt-acct-create-tools-acct-con"></a>

Screenshot of this change type in the AMS console:

![Create Tools Account With VPC change type showing description, ID ct-2j7q1hgf26x5c, and version 2.0.](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiMalzMastAcctCreateToolsAcctVpcCT.png)


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

#### Management account: Creating a Management account Tools account with the CLI
<a name="ex-malz-mgmt-acct-create-tools-acct-cli"></a>

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
aws amscm create-rfc \
--change-type-id "ct-2j7q1hgf26x5c" \
--change-type-version "1.0" --title "New tools account creation" \
--execution-parameters "{\"AccountName\": \"tools\",\"AccountEmail\": \"test@test.com\",\"ApplicationOUName\": \"{{applications:tools}}\",\"TransitGatewayApplicationRouteTableName\": \"{{defaultAppRouteDomain}}\",\"SupportLevel\": \"{{plus}}\",\"VpcName\": \"{{testvpc4}}\",\"VpcCIDR\": \"{{10.106.0.0/24}}\", \"PrivateSubnetIsolatedCIDR\": \"{{10.106.0.128/26}}\", \"PrivateSubnetCIDR\":\"{{10.106.0.192/26}}\",\"PublicSubnetCIDR\":\"{{10.106.0.192/26}}\",\"DirectAlertsEmail\": \"{{test@test.com}}\",\"BackupRule1ScheduleExpression\": \"{{cron(0 2 ? * * )}}\",\"BackupPlanName\": \"{{test}}\",\"ResourceTagKey\": \"{{backup}}\",\"ResourceTagValue\": \"{{true}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it NewToolsAccountParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-2j7q1hgf26x5c" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > NewToolsAccountParams.json
   ```

1. Modify and save the NewToolsAccountParams file. For example, you can replace the contents with something like this:

   ```
   {
   "AccountName":"{{tools}}",
   "AccountEmail":"{{test@test.com}}",
   "ApplicationOUName":"{{applications:tools}}",
   "TransitGatewayApplicationRouteTableName": "{{defaultAppRouteDomain}}",
   "SupportLevel": "{{plus}}",
   "VpcName": "{{testvpc4}}",
   "VpcCIDR": "{{10.106.0.0/24}}",
   "PrivateSubnetIsolatedCIDR": "{{10.106.0.128/26}}",
   "PrivateSubnetCIDR":"{{10.106.0.192/26}}",
   "PublicSubnetCIDR":"{{10.106.0.192/26}}",
   "DirectAlertsEmail": "{{test@test.com}}",
   "BackupRule1ScheduleExpression": "{{cron(0 2 ? * * )}}",
   "BackupPlanName": "{{test}}",
   "ResourceTagKey": "{{backup}}",
   "ResourceTagValue": "{{true}}"
   }
   ```

1. Output the RFC template JSON file to a file; this example names it NewToolsAccountRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > NewToolsAccountRfc.json
   ```

1. Modify and save the NewToolsAccountRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeId": "ct-2j7q1hgf26x5c",
     "ChangeTypeVersion": "2.0",
     "Title": "{{New tools account with VPC creation}}"
   }
   ```

1. Create the RFC, specifying the NewToolsAccount Rfc file and the NewToolsAccountParams file:

   ```
   aws amscm create-rfc --cli-input-json file://NewToolsAccountRfc.json  --execution-parameters file://NewToolsAccountParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

#### Tips
<a name="ex-malz-mgmt-acct-create-tools-acct-tip"></a>

**Note**  
This change type is updated to version 2.0 with changes to input parameters.

To learn more about AMS multi-account landing zone, see [ AWS Managed Services (AMS) Now Offers Managed Landing Zones](https://aws.amazon.com/about-aws/whats-new/2019/10/aws-managed-services-now-offers-managed-landing-zones/).

## Execution Input Parameters
<a name="deployment-managed-management-account-create-tools-account-with-vpc-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-2j7q1hgf26x5c](schemas.md#ct-2j7q1hgf26x5c-schema-section).

## Example: Required Parameters
<a name="deployment-managed-management-account-create-tools-account-with-vpc-ex-min"></a>

```
Example not available.
```

## Example: All Parameters
<a name="deployment-managed-management-account-create-tools-account-with-vpc-ex-max"></a>

```
Example not available.
```