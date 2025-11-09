# Directory Service | Accept Sharing

Accept a directory sharing request sent from the directory owner account. This is run in the directory consumer account.

**Full classification:** Management | Advanced stack components | Directory Service | Accept sharing

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-13xvbj5pqg253 |
| Current version             | 1.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Accept directory sharing request

The following shows this change type in the AMS console.

![Accept Directory Sharing Request form with description, ID, and version fields.](images/guiDirservAcceptShareCT.png)
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
aws amscm create-rfc \ --change-type-id "ct-13xvbj5pqg253" \ --change-type-version "1.0" --title "AWS Directory Service accept directory sharing" \ --execution-parameters "{\"DocumentName\":\"AWSManagedServices-AcceptSharedDirectory\",\"Region\":\"`eu-central-1`\",\"Parameters\":{\"SharedDirectoryId\":[\"`d-000000000`\"],\"OwnerAccountId\":[\"`000000000000`\"]}}"

```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a file; this example names it DirectorySharingParams.json:

```
aws amscm get-change-type-version --change-type-id "ct-13xvbj5pqg253" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > DirectorySharingParams.json
```

Modify and save the DirectorySharingParams file. For example, you can replace the contents with something like this:

```
{
{
  "DocumentName": "AWSManagedServices-AcceptSharedDirectory",
  "Region": "`eu-central-1`",
  "Parameters": {
    "SharedDirectoryId": ["`d-000000000`"],
    "OwnerAccountId": ["`000000000000`"]
  }
}
```

2. Output the RFC template to a file in your current folder; this example names it DirectorySharingRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > DirectorySharingRfc.json
```

3. Modify and save the DirectorySharingRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeId":         "ct-13xvbj5pqg253",
"ChangeTypeVersion":    "`1.0`",
"Title":                "`AWS Directory Service accept directory sharing`"
}
```

4. Create the RFC, specifying the DirectorySharingRfc file and the DirectorySharingParams file:

```
aws amscm create-rfc --cli-input-json file://DirectorySharingRfc.json --execution-parameters file://DirectorySharingParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

###### Note

This change type was originally classified as Management | Advanced stack components | Directory service |
Accept sharing, and has now been moved to a more user friendly classification. The change type ID, ct-13xvbj5pqg253,
has not changed.

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-13xvbj5pqg253](schemas.md#ct-13xvbj5pqg253-schema-section "schemas.md#ct-13xvbj5pqg253-schema-section").

## Example: Required Parameters

```
Example not available.
```

## Example: All Parameters

```
{
  "DocumentName": "AWSManagedServices-AcceptSharedDirectory",
  "Region": "us-east-1",
  "Parameters": {
    "SharedDirectoryId": [
      "d-12e456789f"
    ],
    "OwnerAccountId": [
      "123456789012"
    ]
  }
}

```
