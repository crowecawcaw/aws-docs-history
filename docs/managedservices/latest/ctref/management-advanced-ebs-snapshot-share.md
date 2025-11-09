# EBS Snapshot | Share

Share an Elastic Block Store (EBS) snapshot with another AMS account. If the destination account is onboarded in a different AMS Region, use change type ID ct-3lkbpansfv69k in the destination account to copy shared snapshot across regions. Only snapshots encrypted with managed KMS keys can be shared.

**Full classification:** Management | Advanced stack components | EBS snapshot | Share

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-3gg0id58rn82h |
| Current version             | 2.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Share EBS snapshot

![EBS snapshot sharing details with ID, version, and cross-region sharing instructions.](images/guiEbsSnpshtShareCT.png)
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

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-3gg0id58rn82h" --change-type-version "2.0" --title "`Share EBS snapshot`" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-ShareEBSSnapshot\",\"Region\":\"`ap-southeast-2`\",\"Parameters\":{\"AccountId\":[\"`ACCOUNT_ID`\"],\"SnapshotId\":[\"`SNAP_ID`\"]}}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a file; this example names it ShareEbsSnpshtParams.json:

```
aws amscm get-change-type-version --change-type-id "ct-3gg0id58rn82h" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > ShareEbsSnpshtParams.json
```

2. Modify and save the ShareEbsSnpshtParams file. For example, you can replace the contents with something like this:

```
{
  "DocumentName": "AWSManagedServices-ShareEBSSnapshot",
  "Region": "`us-east-1`",
  "Parameters": {
    "AccountId": [
      "`ACCOUNT_ID`"
    ],
    "SnapshotId": [
      "`SNAPSHOT_ID`"
    ]
  }
}
```

3. Output the RFC template JSON file to a file; this example names it ShareEbsSnpshtRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > ShareEbsSnpshtRfc.json
```

4. Modify and save the ShareEbsSnpshtRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`2.0`",
"ChangeTypeId":         "ct-3gg0id58rn82h",
"Title":                "`EBS-Share-RFC`"
}
```

5. Create the RFC, specifying the ShareEbsSnpshtRfc file and the ShareEbsSnpshtParams file:

```
aws amscm create-rfc --cli-input-json file://ShareEbsSnpshtRfc.json  --execution-parameters file://ShareEbsSnpshtParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

###### Note

A typical use for the EBS snapshot share and copy CTs would be:

1. In account A, use the EBS snapshot share CT to share the snapshot with account B.
2. In account B, use the [Copy EBS snapshot](deployment-advanced-ebs-snapshot-copy.md#ex-ebs-snpsht-copy-col "deployment-advanced-ebs-snapshot-copy.md#ex-ebs-snpsht-copy-col")
   CT to copy the snapshot to the AWS Region for account B.

###### Important

This change type version, 2.0, limits snapshot sharing to only snapshots encrypted with managed KMS keys. Additionally,
several parameters were removed, **TargetParameterName**, **Targets**,
**MaxConcurrency**, and **MaxErrors**; and one new parameter was introduced, **SourceSnapshotId**.

To learn more about Amazon EBS snapshots, see [Amazon EBS Snapshots](../../../AWSEC2/latest/UserGuide/EBSSnapshots.md "../../../AWSEC2/latest/UserGuide/EBSSnapshots.md").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-3gg0id58rn82h](schemas.md#ct-3gg0id58rn82h-schema-section "schemas.md#ct-3gg0id58rn82h-schema-section").

## Example: Required Parameters

```
{
  "DocumentName": "AWSManagedServices-ShareEBSSnapshot",
  "Region": "us-east-1",
  "Parameters": {
    "SnapshotId": [
      "snap-1234567890abcdef0"
    ],
    "AccountId": [
      "012345678912"
    ]
  }
}
```

## Example: All Parameters

```
{
  "DocumentName": "AWSManagedServices-ShareEBSSnapshot",
  "Region": "us-east-1",
  "Parameters": {
    "SnapshotId": [
      "snap-1234567890abcdef0"
    ],
    "AccountId": [
      "012345678912"
    ]
  }
}
```
