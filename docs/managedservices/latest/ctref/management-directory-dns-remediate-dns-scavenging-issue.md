

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# DNS \| Remediate DNS Scavenging Issue
<a name="management-directory-dns-remediate-dns-scavenging-issue"></a>

Remediates DNS scavenging issues for Windows failover clusters by updating permissions on CNO and VCO DNS records. Grants 'Read Permissions' to Everyone on CNO and VCO DNS records, 'Reset Password' permission to Everyone on the CNO computer object, and 'Full Control' permissions to the CNO computer object and specified cluster node computer objects on all CNO and VCO DNS records. This ensures that DNS records associated with the failover cluster are not inadvertently removed during DNS scavenging operations.

**Full classification:** Management \| Directory Service \| DNS \| Remediate DNS scavenging issue

## Change Type Details
<a name="ct-3k67klld7cimj-MDDr-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-3k67klld7cimj | 
| Current version | 1.0 | 
| Expected execution duration | 15 minutes | 
| AWS approval | Required | 
| Customer approval | Not required | 
| Execution mode | Automated | 

## Additional Information
<a name="management-directory-dns-remediate-dns-scavenging-issue-info"></a>

### Remediate DNS scavenging issue
<a name="ex-dirserv-dns-scavenging-remediate-col"></a>

#### Remediating DNS scavenging issue with the console
<a name="dirserv-dns-scavenging-remediate-con"></a>

The following shows this change type in the AMS console.

![Screenshot of the Remediate DNS scavenging issue change type in the AMS console](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiDirservDnsScavengingRemediateCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

#### Remediating DNS scavenging issue with the CLI
<a name="dirserv-dns-scavenging-remediate-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline) and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-3k67klld7cimj" --change-type-version "1.0" --title "Remediate DNS scavenging issue" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-UpdateClusterNodeRecordPermissions-Admin\",\"Parameters\":{\"ClusterCNOName\":[\"{{CLUSTER_CNO_NAME}}\"],\"ClusterNodeComputerNames\":[\"{{NODE_NAME_1}}\",\"{{NODE_NAME_2}}\"],\"ClusterVCONames\":[\"{{VCO_NAME_1}}\",\"{{VCO_NAME_2}}\"]},\"Region\":\"{{us-east-1}}\"}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type; this example names it RemediateDnsScavengingParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-3k67klld7cimj" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > RemediateDnsScavengingParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-UpdateClusterNodeRecordPermissions-Admin",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "ClusterCNOName": ["{{CLUSTER_CNO_NAME}}"],
       "ClusterNodeComputerNames": ["{{NODE_NAME_1}}", "{{NODE_NAME_2}}"],
       "ClusterVCONames": ["{{VCO_NAME_1}}", "{{VCO_NAME_2}}"]
     }
   }
   ```

1. Output the RFC template JSON file; this example names it RemediateDnsScavengingRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > RemediateDnsScavengingRfc.json
   ```

1. Modify and save the RemediateDnsScavengingRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion" : "1.0",
     "ChangeTypeId" : "ct-3k67klld7cimj",
     "Title" : "{{Remediate DNS scavenging issue}}"
   }
   ```

1. Create the RFC, specifying the RemediateDnsScavengingRfc file and the RemediateDnsScavengingParams file:

   ```
   aws amscm create-rfc --cli-input-json file://RemediateDnsScavengingRfc.json  --execution-parameters file://RemediateDnsScavengingParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

## Execution Input Parameters
<a name="management-directory-dns-remediate-dns-scavenging-issue-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-3k67klld7cimj](schemas.md#ct-3k67klld7cimj-schema-section).

## Example: Required Parameters
<a name="management-directory-dns-remediate-dns-scavenging-issue-ex-min"></a>

```
{
  "DocumentName": "AWSManagedServices-UpdateClusterNodeRecordPermissions-Admin",
  "Region": "us-east-1",
  "Parameters": {
    "ClusterCNOName": ["ClusterCNO"],
    "ClusterNodeComputerNames": ["Node1"],
    "ClusterVCONames": ["ClusterVCO1"]
  }
}
```

## Example: All Parameters
<a name="management-directory-dns-remediate-dns-scavenging-issue-ex-max"></a>

```
Example not available.
```