# Tag | Create (Managed Automation)

Add tags to existing, supported resources except those in AMS infrastructure stacks (stacks named mc-\*). Tags simplify categorization, identification and targeting AWS resources. For Autoscaling, EC2, Elastic Load Balancing, RDS resources and S3 buckets, use the automated CT ct-3cx7we852p3af.

**Full classification:** Deployment | Advanced stack components | Tag | Create (managed automation)

## Change Type Details

|                             |                           |
| --------------------------- | ------------------------- |
| Change type ID              | ct-0176f0n99vcps          |
| Current version             | 2.0                       |
| Expected execution duration | 240 minutes               |
| AWS approval                | Required                  |
| Customer approval           | Not required if submitter |
| Execution mode              | Manual                    |

## Additional Information

### Create tags (Managed Automation)

Screenshot of this change type in the AMS console:

![](images/guiTagCreateRrCT.png)
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
aws amscm create-rfc --title `create-tag` --change-type-id ct-0176f0n99vcps --change-type-version `2.0` --execution-parameters '{"Resources":[{"ResourceArn":"`i-abcd1234`","AddOrUpdateTags":[{"Key":"Name","Value":"app-instance-1"},{"Key":"Owner","Value":"Dep A"}]},{"ResourceArn":"`arn:aws:ec2:ap-southeast-2:123456789012:instance/i-019714a96c22f5452`","AddOrUpdateTags":[{"Key":"Name","Value":"app-instance-2"},{"Key":"Owner","Value":"Dep A"}]}]}'
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema to a file in your current folder. This example names it TagCreateParams.json.

```
aws amscm create-rfc --generate-cli-skeleton > TagCreateParams.json
```

2. Modify and save the TagCreateParams.json file. For example, you can replace the contents with something like this:

```
{
   "Resources": [
    {
      "ResourceArn": "`i-abcd1234`",
      "AddOrUpdateTags": [
        {
          "Key": "`Name`",
          "Value": "`app-instance-1`"
        },
        {
          "Key": "`Owner`",
          "Value": "`Dep A`"
        }
      ]
    },
    {
      "ResourceArn": "`arn:aws:ec2:ap-southeast-2:123456789012:instance/i-1234567890abcdef1`",
      "AddOrUpdateTags": [
        {
          "Key": "`Name`",
          "Value": "`app-instance-2`"
        },
        {
          "Key": "`Owner`",
          "Value": "`Dep A`"
        }
      ]
    }
  ]
}
```

3. Output the RFC template JSON file to a file; this example names it TagCreateRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > TagCreateRfc.json
```

4. Modify and save the TagCreateRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`2.0`",
"ChangeTypeId":         "ct-0176f0n99vcps",
"Title":                "`TagCreateRfc`"
}
```

5. Create the RFC:

```
aws amscm create-rfc --cli-input-json file://TagCreateRfc.json  --execution-parameters file://TagCreateParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-0176f0n99vcps](schemas.md#ct-0176f0n99vcps-schema-section "schemas.md#ct-0176f0n99vcps-schema-section").

## Example: Required Parameters

```
Example not available.
```

## Example: All Parameters

```
{
  "Resources": [
    {
      "ResourceArn": "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0",
      "AddOrUpdateTags": [
        {
          "Key": "k1",
          "Value": "v1"
        },
        {
          "Key": "k2",
          "Value": "v2"
        },
        {
          "Key": "k3",
          "Value": "v3"
        }
      ]
    },
    {
      "ResourceArn": "i-0fedcba0987654321",
      "AddOrUpdateTags": [
        {
          "Key": "k1",
          "Value": "v1"
        },
        {
          "Key": "k2",
          "Value": "v2"
        },
        {
          "Key": "k3",
          "Value": "v3"
        }
      ]
    }
  ],
  "Priority": "Medium"
}
```
