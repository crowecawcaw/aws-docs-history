# Application Account | Confirm Offboarding

Confirm offboarding of the specified application account. Run this from the application account that you want off-boarded. Once this CT is executed successfully, login into the Management account of your MALZ environment and run the Offboard application account CT (ct-0vdiy51oyrhhm). After you successfully submit both CTs, AMS can't undo the offboarding, repurpose the account, or help you to remediate issues in the account.

**Full classification:** Management | Managed landing zone | Application account | Confirm offboarding

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-2wlfo2jxj2rkj |
| Current version             | 1.0              |
| Expected execution duration | 3600 minutes     |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Confirm offboarding

###### Important

After confirming your intent to offboard the application account, you have 48 hours to run the
[Management account: Offboard Application account](management-managed-management-account-offboard-application-account.md#ex-man-lz-man-acct-offb-app-acct-col "management-managed-management-account-offboard-application-account.md#ex-man-lz-man-acct-offb-app-acct-col") change type (ct-0vdiy51oyrhhm). After 48 hours, the
offboarding request fails and the process of confirming and then offboarding must be restarted.

Screenshot of this change type in the AMS console:

![Account offboarding confirmation details showing ID, execution mode, and classification.](images/guiManLzAppAcctConfirmOffBCT.png)
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

Run this change type from your Application account.

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then
submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-2wlfo2jxj2rkj" --change-type-version "1.0" --title "`Confirm Offboarding`" --execution-parameters "{\"AccountID\": \"`000000000000`\",\"AccountEmail\": \"`email@amazon.com`\"}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a file; this example names it ConfirmAppAcctOffBParams.json:

```
aws amscm get-change-type-version --change-type-id "ct-2wlfo2jxj2rkj" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > ConfirmAppAcctOffBParams.json
```

2. Modify and save the ConfirmAppAcctOffBParams file. For example, you can replace the contents with something like this:

```
{
  "AccountID": "`000000000000`",
  "AccountEmail": "`email@amazon.com`",
}
```

3. Output the RFC template JSON file to a file; this example names it ConfirmAppAcctOffBRfc.json:

```

    aws amscm create-rfc --generate-cli-skeleton > ConfirmAppAcctOffBRfc.json

```

4. Modify and save the ConfirmAppAcctOffBRfc.json file. For example, you can replace the contents with something like this:

```
{
  "ChangeTypeVersion": "1.0",
  "ChangeTypeId": "ct-2wlfo2jxj2rkj",
  "Title": "Confirm Offboarding"
}
```

5. Create the RFC, specifying the ConfirmAppAcctOffBRfc file and the ConfirmAppAcctOffBParams file:

```

    aws amscm create-rfc --cli-input-json file://ConfirmAppAcctOffBRfc.json  --execution-parameters file://ConfirmAppAcctOffBParams.json

```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

- The second step to offboarding the AMS multi-account landing zone Application account is to submit the
  [Management account: Offboard Application account](management-managed-management-account-offboard-application-account.md#ex-man-lz-man-acct-offb-app-acct-col "management-managed-management-account-offboard-application-account.md#ex-man-lz-man-acct-offb-app-acct-col") change type (ct-0vdiy51oyrhhm) from the application account
  _within 48 hours_ of successfully running this change type confirming the intent to offboard.
- For application accounts (other than Customer Managed), run this from the Application account that you want offboarded. After successful confirmation, run the
  [Offboard application account](management-managed-management-account-offboard-application-account.md "management-managed-management-account-offboard-application-account.md")
  CT (ct-0vdiy51oyrhhm) from the associated management account. Offboarding is intended for account closure and cannot be undone.
- Do not use this CT for Customer Managed application accounts. Go directly to
  [Offboard application account](management-managed-management-account-offboard-application-account.md "management-managed-management-account-offboard-application-account.md")
  CT (ct-0vdiy51oyrhhm).

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-2wlfo2jxj2rkj](schemas.md#ct-2wlfo2jxj2rkj-schema-section "schemas.md#ct-2wlfo2jxj2rkj-schema-section").

## Example: Required Parameters

```
{
  "RequestType": "OffboardingConfirmation",
  "Parameters": {
    "AccountId": "000000000000",
    "AccountEmail": "example@email.com"
  }
}

```

## Example: All Parameters

```
{
  "RequestType": "OffboardingConfirmation",
  "Parameters": {
    "AccountId": "000000000000",
    "AccountEmail": "example@email.com"
  }
}

```
