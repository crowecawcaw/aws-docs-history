# Bastions | Add CIDR Ingress (Managed Automation)

Add RDP or SSH bastion ingress Classless Inter-Domain Routing (CIDR) allow lists.

**Full classification:** Management | Advanced stack components | Bastions | Add CIDR ingress (managed automation)

## Change Type Details

|                             |                           |
| --------------------------- | ------------------------- |
| Change type ID              | ct-36zubwzxp44a4          |
| Current version             | 1.0                       |
| Expected execution duration | 240 minutes               |
| AWS approval                | Required                  |
| Customer approval           | Not required if submitter |
| Execution mode              | Manual                    |

## Additional Information

### Add CIDR ingress (Managed Automation) ct-36zubwzxp44a4

The following shows this change type in the AMS console.

![](images/guiBastionCidrIngressAddCT.png)
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
aws amscm create-rfc --change-type-id "ct-36zubwzxp44a4" --change-type-version "1.0" --title "`Add CIDR ingress`" --execution-parameters "{\"BastionType\": \"`RDP Bastion`\", \"[\"`10.0.0.1/24\",\"10.20.0.4/25\",\"10.0.0.6/25\`"]\": \"`10`\", \"ASGMinCount\": \"`10`\"}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a JSON file;
   this example names it AddBastionCidrIngressParams.json:

```
aws amscm get-change-type-version --change-type-id "ct-36zubwzxp44a4" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > AddBastionCidrIngressParams.json
```

2. Modify and save the AddBastionCidrIngressParams file.

```
{
   "BastionType": "`RDP Bastion`",
   "IngressCIDRAddresses": ["`10.113.44.1/22`", "`10.113.56.1/22`"],
   "Priority": "`Medium`"
 }
```

3. Output the RFC template to a file in your current folder; this example names it AddBastionCidrIngressRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > AddBastionCidrIngressRfc.json
```

4. Modify and save the AddBastionCidrIngressRfc.json file. For example, you can replace the contents with something like this:

```
{
  "ChangeTypeVersion": "1.0",
  "ChangeTypeId": "ct-36zubwzxp44a4",
  "Title": "`Add Bastion CIDR Ingress`"
}
```

5. Create the RFC, specifying the AddBastionCidrIngressRfc file and the AddBastionCidrIngressParams file:

```
aws amscm create-rfc --cli-input-json file://AddBastionCidrIngressRfc.json --execution-parameters file://AddBastionCidrIngressParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

- To learn more, see
  [Authorize inbound traffic for your Linux instances](../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md "../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md").
- This is a manual change type (an AMS operator must review and run the CT), which means that the RFC can take longer
  to run and you might have to communicate with AMS through the RFC details page correspondance option. Additionally, if you schedule a manual change type RFC,
  be sure to allow at least 24 hours, if approval does not happen before the scheduled start time, the RFC is rejected automatically.

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-36zubwzxp44a4](schemas.md#ct-36zubwzxp44a4-schema-section "schemas.md#ct-36zubwzxp44a4-schema-section").

## Example: Required Parameters

```
{
  "BastionType": "RDP Bastion",
  "IngressCIDRAddresses": ["10.113.44.1/22"]
}
```

## Example: All Parameters

```
{
  "BastionType": "RDP Bastion",
  "IngressCIDRAddresses": ["10.113.44.1/22", "10.113.56.1/22"],
  "Priority": "Medium"
}
```
