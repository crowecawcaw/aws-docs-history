# Stack Admin Access | Grant

Request admin access for one or more users for one or more stacks. The maximum access time is 12 hours.

**Full classification:** Management | Access | Stack admin access | Grant

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-1dmlg9g1l91h6 |
| Current version             | 3.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Request administrative access

The following shows this change type in the AMS console.

![Grant Stack Admin access interface showing ID, execution mode, version, and description.](images/guiAccessAdminGrantCT.png)
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

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws --profile saml amscm create-rfc --change-type-id "ct-1dmlg9g1l91h6" --change-type-version "3.0" --title "`Stack-Admin-Access-QC`" --execution-parameters "{\"DomainFQDN\":\"`TEST.com`\",\"StackIds\":[\"`stack-01234567890abcdef`\"],\"TimeRequestedInHours\":1,\"Usernames\":[\"`TEST`\"],\"VpcId\":\"`VPC_ID`\"}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a file; this example names it GrantAdminAccessParams.json:

```
aws amscm get-change-type-version --change-type-id "ct-1dmlg9g1l91h6" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > GrantAdminAccessParams.json
```

Modify and save the GrantAdminAccessParams file. For example, you can replace the contents with something like this:

```
{
"DomainFQDN":           "`mycorpdomain.acme.com`",
"StackIds":             [`STACK_ID`, `STACK_ID`],
"TimeRequestedInHours": `12`,
"Username":             ["`USERNAME`", "`USERNAME`"],
"VpcId":                "`VPC_ID`"
}
```

Note that the `TimeRequestedInHours` option defaults to one hour. You can request up to twelve hours. 2. Output the RFC template to a file in your current folder; this example names it GrantAdminAccessRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > GrantAdminAccessRfc.json
```

3. Modify and save the GrantAdminAccessRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeId":         "ct-1dmlg9g1l91h6",
"ChangeTypeVersion":    "`3.0`",
"Title":                "`Request-Admin-Access-to-EC2-RFC`"
}
```

4. Create the RFC, specifying the GrantAdminAccessRfc file and the GrantAdminAcessParams file:

```
aws amscm create-rfc --cli-input-json file://GrantAdminAccessRfc.json --execution-parameters file://GrantAdminAccessParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

To log in to the instance through a bastion, follow the next procedure,
[Instance access examples](../userguide/access-examples.md "../userguide/access-examples.md").

###### Note

You can submit an update to your access request before it expires. For information, see
[Stack Admin Access | Update](management-access-stack-admin-access-update.md "management-access-stack-admin-access-update.md").

To log in to an instance that is part of an ASG, you request access to the ASG stack,
which gives you access to all associated instances.

For an example about requesting ReadOnly access, see
[ReadOnly access: requesting](ex-access-ro-request-col.md "ex-access-ro-request-col.md").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-1dmlg9g1l91h6](schemas.md#ct-1dmlg9g1l91h6-schema-section "schemas.md#ct-1dmlg9g1l91h6-schema-section").

## Example: Required Parameters

```
{
  "DomainFQDN": "test.domain.com",
  "StackIds": ["stack-12345678901234567"],
  "Usernames": ["AD_User_Name1"],
  "VpcId": "vpc-12345678"
}

```

## Example: All Parameters

```
{
  "DomainFQDN": "test.domain.com",
  "StackIds": ["stack-12345678901234567"],
  "TimeRequestedInHours": 1,
  "Usernames": ["AD_User_Name1"],
  "VpcId": "vpc-12345678"
}

```
