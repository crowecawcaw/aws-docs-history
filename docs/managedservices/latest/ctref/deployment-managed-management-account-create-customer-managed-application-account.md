# Management Account | Create Customer-Managed Application Account

Create a customer-managed application account in a multi-account AWS landing zone. Customer-managed accounts give you full control to operate the infrastructure within the centralized architecture managed by AMS. Multi-account AWS landing zone core accounts must already be onboarded to AWS Managed Services (AMS).

**Full classification:** Deployment | Managed landing zone | Management account | Create customer-managed application account

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-3pwbixz27n3tn |
| Current version             | 1.0              |
| Expected execution duration | 3600 minutes     |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Create a Customer Managed application account

Screenshot of this change type in the AMS console:

![Description and details for creating a customer-managed application account in AWS.](images/guiMalzMgmtAcctCreateCustManAppAcctCT.png)
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
aws amscm create-rfc \
--change-type-id "ct-3pwbixz27n3tn" \
--change-type-version "1.0" --title "`New customer-managed account creation`" \
--execution-parameters "{\"AccountName\":\"`test`\", \"AccountEmail\":\"`test@test.com`\", \"CustomerManagedOUName\":\"`customer-managed`\"}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a file; this example names it NewCustomerManagedAccountParams.json:

```
aws amscm get-change-type-version --change-type-id "ct-1zdasmc2ewzrs" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > NewCustomerManagedAccountParams.json
```

2. Modify and save the NewCustomerManagedAccountParams file. For example, you can replace the contents with something like this:

```
{
"AccountName":"`test`",
"AccountEmail":"`test@test.com`",
"CustomerManagedOUName":"`customer-managed`"
}
```

3. Output the RFC template JSON file to a file; this example names it NewCustomerManagedAccountRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > NewCustomerManagedAccountRfc.json
```

4. Modify and save the NewCustomerManagedAccountRfc.json file. For example, you can replace the contents with something like this:

```

{
  "ChangeTypeId": "ct-3pwbixz27n3tn",
  "ChangeTypeVersion": "1.0",
  "Title": "`New customer-managed account creation`"
}
```

5. Create the RFC, specifying the NewCustomerManagedAccount Rfc file and the NewCustomerManagedAccountParams file:

```
aws amscm create-rfc --cli-input-json file://NewCustomerManagedAccountRfc.json  --execution-parameters file://NewCustomerManagedAccountParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.
To learn more about AMS multi-account landing zone, see [AWS Managed Services (AMS) Now Offers Managed Landing Zones](https://aws.amazon.com/about-aws/whats-new/2019/10/aws-managed-services-now-offers-managed-landing-zones/ "https://aws.amazon.com/about-aws/whats-new/2019/10/aws-managed-services-now-offers-managed-landing-zones/").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-3pwbixz27n3tn](schemas.md#ct-3pwbixz27n3tn-schema-section "schemas.md#ct-3pwbixz27n3tn-schema-section").

## Example: Required Parameters

```
Example not available.
```

## Example: All Parameters

```
Example not available.
```
