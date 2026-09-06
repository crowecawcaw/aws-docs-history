

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# DNS \| Update Record Permission
<a name="management-directory-dns-update-record-permission"></a>

Grant permissions to the computer object to update DNS records after failover. For multi-account landing zone (MALZ), use this change type in the shared services account.

**Full classification:** Management \| Directory Service \| DNS \| Update record permission

## Change Type Details
<a name="ct-1eft8s6vdhz0w-MDDu-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-1eft8s6vdhz0w | 
| Current version | 1.0 | 
| Expected execution duration | 60 minutes | 
| AWS approval | Required | 
| Customer approval | Not required | 
| Execution mode | Automated | 

## Additional Information
<a name="management-directory-dns-update-record-permission-info"></a>

### Update DNS record permission
<a name="ex-dirserv-record-permission-update-col"></a>

#### Updating DNS record permissions with the console
<a name="dirserv-record-permission-update-con"></a>

The following shows this change type in the AMS console.

![Update DNS Record Permission interface showing description, ID, and version details.](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiDirservRecordPermUpdateCT.png)


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

#### Updating DNS record permissions with the CLI
<a name="dirserv-record-permission-update-cli"></a>

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

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-1eft8s6vdhz0w" --change-type-version "1.0" --title "{{Update DNS Record}}" --execution-parameters "{\"DocumentName\": \"AWSManagedServices-UpdateDNSRecordsPermission-Admin\",\"Region\": \"{{us-east-1}}\",\"Parameters\": {\"RecordNames\": [\"{{EC2CLUS-SAMPLE}}\",\"{{EC2SAmPL1-AWS}}\"]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it UpdateDNSRecordsPermissionParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-1eft8s6vdhz0w" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateDNSRecordsPermissionParams.json
   ```

   Modify and save the UpdateDNSRecordsPermissionParams file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-UpdateDNSRecordsPermission-Admin",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "RecordNames": ["{{EC2CLUS-SAMPLE}}","{{EC2SAmPL1-AWS}}"]
     }
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it UpdateDNSRecordsPermissionRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > UpdateDNSRecordsPermissionRfc.json
   ```

1. Modify and save the UpdateDNSRecordsPermissionRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion": "1.0",
     "ChangeTypeId": "ct-1eft8s6vdhz0w",
     "Title": "Update DNS record"
   }
   ```

1. Create the RFC, specifying the UpdateDNSRecordsPermissionRfc file and the UpdateDNSRecordsPermissionParams file:

   ```
   aws amscm create-rfc --cli-input-json file://UpdateDNSRecordsPermissionRfc.json --execution-parameters file://UpdateDNSRecordsPermissionParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

#### Tips
<a name="ex-dirserv-record-permission-update-tip"></a>

## Execution Input Parameters
<a name="management-directory-dns-update-record-permission-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-1eft8s6vdhz0w](schemas.md#ct-1eft8s6vdhz0w-schema-section).

## Example: Required Parameters
<a name="management-directory-dns-update-record-permission-ex-min"></a>

```
{
  "DocumentName": "AWSManagedServices-UpdateDNSRecordsPermission-Admin",
  "Region": "us-east-1",
  "Parameters": {
    "RecordNames": ["EC2CLUS-SAMPl1,EC2G90BI1-AWS"]
  }
}
```

## Example: All Parameters
<a name="management-directory-dns-update-record-permission-ex-max"></a>

```
{
  "DocumentName": "AWSManagedServices-UpdateDNSRecordsPermission-Admin",
  "Region": "us-east-1",
  "Parameters": {
    "RecordNames": ["EC2CLUS-SAMPl1,EC2G90BI1-AWS"]
  }
}
```