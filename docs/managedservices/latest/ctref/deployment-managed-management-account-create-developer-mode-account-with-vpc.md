# Management Account | Create Developer Mode Account (With VPC)

Create a managed AWS landing zone developer mode account and a VPC with up to 10 private subnets and up to 5 optional public subnets per availability zone (AZ) for two or three AZ's. Optionally, also create an AWS Backup plan with up to four different rules. Managed AWS landing zone core accounts must already be onboarded to AWS Managed Services (AMS).

**Full classification:** Deployment | Managed landing zone | Management account | Create developer mode account (with VPC)

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-38xcr0q86k9lh |
| Current version             | 1.0              |
| Expected execution duration | 3600 minutes     |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Create Developer mode account with VPC

Screenshot of this change type in the AMS console:

![AWS console interface showing details for creating a developer mode account with VPC.](images/guiMalzMgmtAcctCreateDevModeAcctCT.png)
How it works:

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
How it works:

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

_INLINE CREATE_:

###### Note

Run this change type from your Management account.

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-38xcr0q86k9lh" --change-type-version "1.0" --title "`Dev Mode account onboarding`" --execution-parameters "{\"AccountName
    \": \"`ACCOUNT_NAME`\",\"AccountEmail\": \"/\",\"DeveloperModeOUName\":
    \"`Development_OU_NAME:CHILD_OU_NAME`\",\"SupportLevel\": \"`LEVEL`\",\"VpcName\":
    \"`VPC_NAME`\",\"NumberOfAZs\": \"`INTEGER`\",\"VpcCIDR\":
    \"`X.X.X.X/X`\", \"PrivateSubnet1AZ1CIDR\": \"`X.X.X.X/X`\",\"PrivateSubnet1AZ2CIDR\":
    \"`X.X.X.X/X`\",\"PrivateSubnet1AZ3CIDR\": \"`X.X.X.X/X`\",\"PublicSubnetAZ1CIDR\":
    \"`X.X.X.X/X`\",\"PublicSubnetAZ2CIDR\": \"`X.X.X.X/X`\",\"PublicSubnetAZ3CIDR\":
    \"`X.X.X.X/X`\", \"RouteType\": \"`ROUTE_TYPE`\", \"TransitGatewayApplicationRouteTableName\":
    \"`TABLE_NAME`\", \"BackupPlanName\":\"`PLAN_NAME`\", \"ResourceTagKey\":
    \"`TAG_KEY`\", \"ResourceTagValue\":\"`TAG_VALUE`\", "\BackupRule1ScheduleExpression\":
    \"`cron(0 2 ? * * *)`\"}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a file; this example names it CreateDevModeAcctWithVpcParams.json:

```
aws amscm get-change-type-version --change-type-id "ct-38xcr0q86k9lh" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateDevModeAcctWithVpcParams.json
```

2. Modify and save the CreateDevModeAcctWithVpcParams file. For example, you can replace the contents with something like this:

```
{
      "AccountName": "`ACCOUNT_NAME`",
      "AccountEmail": "`ACCOUNT_EMAIL`",
      "DeveloperModeOUName": "`DEVELOPER_MODE_OU_NAME:CHILD_OU_NAME`",
      "SupportLevel": "`PLUS_or_PREMIUM`",
      "VpcName": "`VPC_NAME`",
      "NumberOfAZs": "`TWO_or_THREE`",
      "VpcCIDR": "`x.x.x.x/x`",
      "PrivateSubnet1AZ1CIDR": "`x.x.x.x/x`",
      "PrivateSubnet1AZ2CIDR": "`x.x.x.x/x`",
      "PrivateSubnet1AZ3CIDR": "`x.x.x.x/x`",
      "PublicSubnetAZ1CIDR": "`x.x.x.x/x`",
      "PublicSubnetAZ2CIDR": "`x.x.x.x/x`",
      "PublicSubnetAZ3CIDR": "`x.x.x.x/x`",
      "RouteType": "`ROUTABLE_or_ISOLATED`",
      "TransitGatewayApplicationRouteTableName": "`ROUTE_TABLE_NAME`"
}
```

3. Output the RFC template JSON file to a file; this example names it CreateDevModeAcctWithVpcRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > CreateDevModeAcctWithVpcRfc.json
```

4. Modify and save the CreateDevModeAcctWithVpcRfc.json file. For example, you can replace the contents with something like this:

```

{
  "ChangeTypeId": "ct-38xcr0q86k9lh",
  "ChangeTypeVersion": "1.0",
  "Title": "`Create developer mode account with VPC`"
}
```

5. Create the RFC, specifying the CreateDevModeAcctWithVpcRfc file and the CreateDevModeAcctWithVpcParams file:

```
aws amscm create-rfc --cli-input-json file://CreateDevModeAcctWithVpcRfc.json  --execution-parameters file://CreateDevModeAcctWithVpcParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.
To learn more about developer mode, see [Developer mode](../userguide/developer-mode.md "../userguide/developer-mode.md").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-38xcr0q86k9lh](schemas.md#ct-38xcr0q86k9lh-schema-section "schemas.md#ct-38xcr0q86k9lh-schema-section").

## Example: Required Parameters

```
Example not available.
```

## Example: All Parameters

```
Example not available.
```
