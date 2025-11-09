# Security Group | Disassociate

Disassociate a security group from up to 50 AWS resources.

**Full classification:** Management | Advanced stack components | Security group | Disassociate

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-13lk0noacn6ua |
| Current version             | 2.0              |
| Expected execution duration | 120 minutes      |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Disassociate security group to resource

Screenshot of this change type in the AMS console:

![Disassociate Security Group change type details, including ID, execution mode, and description.](images/guiSecGroupDisassociateCT.png)
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
aws amscm create-rfc --change-type-id "ct-13lk0noacn6ua" --change-type-version "2.0" --title "`Disassociate security group`" --execution-parameters "{\"DocumentName\": \"AWSManagedServices-DisassociateSecurityGroupV2\", \"Region\": \"`us-east-1`\", \"Parameters\": {\"SecurityGroupId\": \"`sg-xxxxxxxxxxxxxxxxx`\", \"EC2InstanceIds\": [\"`i-xxxxxxxxxxxxxxxxx`\"]}}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a file; this example names it DisassociateSGParams.json.

```
aws amscm get-change-type-version --change-type-id "ct-13lk0noacn6ua" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > DisassociateSGParams.json
```

2. Modify and save the DisassociateSGParams file. For example, you can replace the contents with something like this:

```
{
    "DocumentName": "AWSManagedServices-DisassociateSecurityGroupV2",
    "Region": "`us-east-1`",
    "Parameters": {
        "SecurityGroupId": [
            "`sg-xxxxxxxxxxxxxxxxx`"
        ],
        "EC2InstanceIds": [
            "`i-xxxxxxxxxxxxxxxxx`"
        ]
    }
}
```

3. Output the RFC template JSON file to a file named DisassociateSGRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > DisassociateSGRfc.json
```

4. Modify and save the DisassociateSGRfc.json file. For example, you can replace the contents with something like this:

```
{
  "ChangeTypeVersion": "2.0",
  "ChangeTypeId": "ct-13lk0noacn6ua",
  "Title": "`Disassociate security group`"
}
```

5. Create the RFC, specifying the DisassociateSG Rfc file and the DisassociateSGParams file:

```
aws amscm create-rfc --cli-input-json file://DisassociateSGRfc.json  --execution-parameters file://DisassociateSGParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.
For help deleting a security group from a VPC, see
[Why can't I delete a security group
for my Amazon VPC?](https://aws.amazon.com/premiumsupport/knowledge-center/troubleshoot-delete-vpc-sg/ "https://aws.amazon.com/premiumsupport/knowledge-center/troubleshoot-delete-vpc-sg/").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-13lk0noacn6ua](schemas.md#ct-13lk0noacn6ua-schema-section "schemas.md#ct-13lk0noacn6ua-schema-section").

## Example: Required Parameters

```
Example not available.
```

## Example: All Parameters

```
{
    "DocumentName": "AWSManagedServices-DisassociateSecurityGroupV2",
    "Region": "us-east-1",
    "Parameters": {
      "SecurityGroupId": "sg-1234556eaba0a4799",
      "EC2InstanceIds": ["i-1234567890abababa"],
      "ElasticNetworkInterfaceIds": ["eni-1234567890abababa"],
      "AutoScalingGroupNames": ["myautoscalinggroup"],
      "ElasticLoadBalancerNames": ["myloadbalancer"],
      "ApplicationLoadBalancerNames": ["myloadbalancer"],
      "RDSDBInstanceIdentifiers": ["mydbinstance"],
      "RDSDBClusterIdentifiers": ["mydbcluster"],
      "ElasticacheClusterIdentifiers": ["mycachecluster"],
      "RedshiftClusterIdentifiers": ["myredshiftcluster"],
      "ElasticFileSystemIds": ["myfilesystem"]
    }
}

```
