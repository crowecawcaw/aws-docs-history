# Security Group | Authorize Egress Rule

Authorize multiple egress rules for the specified security group (SG). You must specify the configurations of the egress rule that you are authorizing. Note that adding an egress rule to the specified SG does not modify any existing egress rules.

**Full classification:** Management | Advanced stack components | Security group | Authorize egress rule

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-0lqruajvhwsbk |
| Current version             | 2.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Authorize security group egress rule

Screenshot of this change type in the AMS console:

![Authorize Egress Rule interface with description, ID, and version fields for security group configuration.](images/guiSecGroupEgressAuthorizeCT.png)
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
aws amscm create-rfc --change-type-id "ct-0lqruajvhwsbk" --change-type-version "2.0" --title "`AWSManagedServices-AuthorizeSecurityGroupEgressRulesV2`" --execution-parameters "{\"DocumentName\": \"AWSManagedServices-AuthorizeSecurityGroupEgressRulesV2\",\"Region\": \"`us-east-1`\",\"Parameters\": {\"SecurityGroupId\": [
\"`sg-03b5e3a1ad874bdd7`\"],\"OutboundRules\": [{\"IpProtocol\": \"`tcp`\",\"FromPort\": \"`80`\",\"ToPort\": \"`80`\",\"Destination\": \"`192.168.1.0/24`\"},{\"IpProtocol\": \"`tcp`\",\"FromPort\": \"`99`\",\"ToPort\": \"`99`\",\"Destination\": \"`172.16.0.0/24`\", \"Description\": \"`On-prem IP`\"}]}}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a file; this example names it AuthSGEgressParams.json.

```
aws amscm get-change-type-version --change-type-id "ct-0lqruajvhwsbk" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > AuthSGEgressParams.json
```

2. Modify and save the AuthSGEgressParams file. For example, you can replace the contents with something like this:

```
{
"DocumentName": "AWSManagedServices-AuthorizeSecurityGroupEgressRulesV2",
"Region": "`us-east-1`",
"Parameters": {
{
"SecurityGroupId": [
"sg-03b5e3a1ad874bdd7"
],
"OutboundRules": [
{
"IpProtocol": "`tcp`",
"FromPort": "`80`",
"ToPort": "`80`",
"Destination": "`192.168.1.0/24`"
},
{
"IpProtocol": "`tcp`",
"FromPort": "`99`",
"ToPort": "`99`",
"Destination": "`172.16.0.0/24`",
"Description": "`On-prem IP`"
}
]
}
}
}
```

3. Output the RFC template JSON file to a file named AuthSGEgressRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > AuthSGEgressRfc.json
```

4. Modify and save the AuthSGEgressRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion": "2.0",
"ChangeTypeId": "ct-0lqruajvhwsbk",
"Title": "Authorize Multiple Egress Rules"
}
```

5. Create the RFC, specifying the AuthSGEgressRfc file and the AuthSGEgressParams file:

```
aws amscm create-rfc --cli-input-json file://AuthSGEgressRfc.json  --execution-parameters file://AuthSGEgressParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

###### Note

There are two ways to authorize a new egress rule, one, Security Group: Update change type (ct-3memthlcmvc1b), has ExecutionMode=Manual and provides
a lot of latitude for custom rules; however, being manual, it takes longer to execute as AMS Operations must review it for safety, and possibly
require communications. The other egress rule authorization way, Security Group: Authorize Egress Rule change type (ct-3j2zstluz6dxq), has ExecutionMode=Automated and
provides options for creating standard TCP/UDP or ICMP egress rules. It is more limited in scope; however, being automated, it executes more quickly.

This walkthrough is for the Security Group: Authorize Egress Rule change type.

To learn more about AWS security groups and security group rules, see
[Security Group
Rules Reference](../../../AWSEC2/latest/UserGuide/security-group-rules-reference.md "../../../AWSEC2/latest/UserGuide/security-group-rules-reference.md"); this page
can help you determine the rules you want and, importantly, how to name your security group so choosing it when
creating other resources is intuitive. Also see
[Amazon EC2 Security
Groups for Linux Instances](../../../AWSEC2/latest/UserGuide/using-network-security.md "../../../AWSEC2/latest/UserGuide/using-network-security.md")
and/or [Security Groups
for Your VPC](../../../AmazonVPC/latest/UserGuide/VPC_SecurityGroups.md "../../../AmazonVPC/latest/UserGuide/VPC_SecurityGroups.md").

Once the security group is created, use [Associate security group to resource](management-advanced-security-group-associate.md#ex-sec-group-associate-col "management-advanced-security-group-associate.md#ex-sec-group-associate-col") to associate the security group with your AMS resources. In order to delete a security group, it must have associated
resources.

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-0lqruajvhwsbk](schemas.md#ct-0lqruajvhwsbk-schema-section "schemas.md#ct-0lqruajvhwsbk-schema-section").

## Example: Required Parameters

```
Example not available.
```

## Example: All Parameters

```
Example not available.
```
