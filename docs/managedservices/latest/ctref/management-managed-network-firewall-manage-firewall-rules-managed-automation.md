End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](../userguide/SunsetPlan.md "../userguide/SunsetPlan.md").

# Network Firewall | Manage Firewall Rules (Managed Automation)

Manages AWS Network Firewall egress rules by converting simple parameters (source IP, destination, port, protocol) into security policies, generating Suricata rules, and updating Network Firewall rule groups.

**Full classification:** Management | Managed firewall | Network firewall | Manage firewall rules (managed automation)

## Change Type Details

|                             |                           |
| --------------------------- | ------------------------- |
| Change type ID              | ct-2lo1hs6ks7chl          |
| Current version             | 1.0                       |
| Expected execution duration | 60 minutes                |
| AWS approval                | Required                  |
| Customer approval           | Not required if submitter |
| Execution mode              | Manual                    |

## Additional Information

### Manage network firewall rules (managed automation)

Screenshot of this change type in the AMS console:

![Manage Network Firewall Rules change type showing ID, execution mode, version, and classification.](images/guiManageNetworkFirewallRulesCT.png)
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
aws amscm create-rfc --change-type-id "ct-2lo1hs6ks7chl" --change-type-version "`1.0`" --title "`Manage Network Firewall Rules`" --execution-parameters "{\"SourceIP\": \"`192.168.1.0/24`\", \"Destination\": \"`example.com`\", \"Protocol\": \"`TCP`\", \"Port\": `443`, \"Action\": \"`Allow`\", \"RuleName\": \"`allow-https-traffic`\", \"Operation\": \"`Create`\"}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a file; this example names
   it ManageFirewallRulesParams.json.

```
aws amscm get-change-type-version --change-type-id "ct-2lo1hs6ks7chl" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > ManageFirewallRulesParams.json
```

2. Modify and save the ManageFirewallRulesParams file. For example, you can replace the contents with something like this:

```
{
"SourceIP": "`192.168.1.0/24`",
"Destination": "`example.com`",
"Protocol": "`TCP`",
"Port": `443`,
"Action": "`Allow`",
"RuleName": "`allow-https-traffic`",
"Operation": "`Create`",
"DryRun": `false`
}
```

3. Output the RFC template JSON file to a file named ManageFirewallRulesRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > ManageFirewallRulesRfc.json
```

4. Modify and save the ManageFirewallRulesRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-2lo1hs6ks7chl",
"Title":                "`Manage-Network-Firewall-Rules-RFC`"
}
```

5. Create the RFC, specifying the ManageFirewallRulesRfc file and the ManageFirewallRulesParams
   file:

```
aws amscm create-rfc --cli-input-json file://ManageFirewallRulesRfc.json  --execution-parameters file://ManageFirewallRulesParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

- Use the `DryRun` parameter set to `true` to validate your request without making changes.
- The `Operation` parameter supports Create, Read, Update, and Delete actions on Network Firewall rules.

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-2lo1hs6ks7chl](schemas.md#ct-2lo1hs6ks7chl-schema-section "schemas.md#ct-2lo1hs6ks7chl-schema-section").

## Example: Required Parameters

```
{
  "SourceIP": "10.0.0.0/24",
  "Destination": "203.0.113.0/24",
  "Protocol": "TCP",
  "Port": 443,
  "Action": "Allow",
  "RuleName": "test-rule",
  "Operation": "Create"
}

```

## Example: All Parameters

```
{
  "SourceIP": "192.168.1.0/24",
  "Destination": "example.com",
  "Protocol": "TCP",
  "Port": 443,
  "Action": "Allow",
  "RuleName": "allow-https-traffic",
  "Operation": "Create",
  "DryRun": false
}

```
