

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Computer Object \| Remove
<a name="management-directory-computer-object-remove"></a>

Remove a stale computer object from Microsoft Active Directory (AD) and the corresponding DNS A and PTR records from DNS. Removing the computer object will prevent anyone from raising access against this host using the AMS access control. For multi-account landing zone (MALZ), use this change type in the shared services account.

**Full classification:** Management \| Directory Service \| Computer object \| Remove

## Change Type Details
<a name="ct-3d0lrfb8eckuu-MDCr-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-3d0lrfb8eckuu | 
| Current version | 1.0 | 
| Expected execution duration | 60 minutes | 
| AWS approval | Required | 
| Customer approval | Not required | 
| Execution mode | Automated | 

## Additional Information
<a name="management-directory-computer-object-remove-info"></a>

### Remove a computer object
<a name="ex-dirserv-comp-object-remove-col"></a>

#### Removing a computer object from an AMS-managed AD with the console
<a name="dirserv-comp-object-remove-con"></a>

The following shows this change type in the AMS console.

![Remove Computer Object change type showing ID ct-3d0lfrb8eckuu and version 1.0.](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiDirservCompObjectRemoveCT.png)


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

#### Removing a computer object from an AMS-managed AD with the CLI
<a name="dirserv-comp-object-remove-cli"></a>

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
aws amscm create-rfc --change-type-id "ct-3d0lrfb8eckuu" --change-type-version "1.0" --title "{{Remove Computer Object}}" --execution-parameters "{\"DocumentName\": \"AWSManagedServices-RemoveADComputerObject-Admin\",\"Region\": \"{{us-east-1}}\",\"Parameters\": {\"ADComputerName\": [\"{{ABRACADABRA}}\"]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type to a file; this example names it ComputerObjectRemoveParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-3d0lrfb8eckuu" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > ComputerObjectRemoveParams.json
   ```

   Modify and save the ComputerObjectRemoveParams file. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-RemoveADComputerObject-Admin",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "ADComputerName": [
         "{{ABRACADABRA}}"
       ]
     }
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it ComputerObjectRemoveRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > ComputerObjectRemoveRfc.json
   ```

1. Modify and save the ComputerObjectRemoveRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeId":         "ct-3d0lrfb8eckuu",
   "ChangeTypeVersion":    "{{1.0}}",
   "Title":                "{{Remove computer object}}"
   }
   ```

1. Create the RFC, specifying the ComputerObjectRemoveRfc file and the ComputerObjectRemoveParams file:

   ```
   aws amscm create-rfc --cli-input-json file://ComputerObjectRemoveRfc.json --execution-parameters file://ComputerObjectRemoveParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

#### Tips
<a name="ex-dirserv-comp-object-remove-tip"></a>
+ For information about Directory Service, see the [Directory Service Admin Guide](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html). 
+ Remove stale computer objects before provisioning an instance. If you plan to provision a new instance (Windows or Linux) using a hostname that already exists in Active Directory, for example, when restoring from an AMI or re-using a hostname from a previous stack, you must run this change type first to remove the stale computer object. AMS does not provision an instance if a computer object with the same hostname already exists in Active Directory. 

   If you don't remove the stale object, you might experience RFC rejection, duplicate computer objects in the wrong Organizational Unit (OU), broken domain join, DNS record conflicts, and inaccessible instances (RDP failures on Windows, or Kerberos authentication and SSH failures on Linux). This is especially important when the source AMI was captured from a running domain-joined instance without first preparing it. On Windows, this means not running `Invoke-AMSSysprep`, and on Linux, not running the AMS preparation script (`prepare_instance_for_ami_and_shutdown.sh`). 

   Without preparation, the AMI retains the previous instance's machine credentials (computer account SID and password on Windows, or Kerberos keytab on Linux), which causes trust relationship failures and object conflicts when a new instance boots from it. For more information on instance preparation, see the Tips section of [Deployment \| Advanced stack components \| AMI \| Create](https://docs.aws.amazon.com/managedservices/latest/ctref/deployment-advanced-ami-create.html) (ct-3rqqu43krekby). 

## Execution Input Parameters
<a name="management-directory-computer-object-remove-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-3d0lrfb8eckuu](schemas.md#ct-3d0lrfb8eckuu-schema-section).

## Example: Required Parameters
<a name="management-directory-computer-object-remove-ex-min"></a>

```
{
  "DocumentName" : "AWSManagedServices-RemoveADComputerObject-Admin",
  "Region" : "us-east-1",
  "Parameters" : {
    "Hostname" : [
      "ABRACADABRA"
    ]
  }
}
```

## Example: All Parameters
<a name="management-directory-computer-object-remove-ex-max"></a>

```
{
  "DocumentName" : "AWSManagedServices-RemoveADComputerObject-Admin",
  "Region" : "us-east-1",
  "Parameters" : {
    "Hostname" : [
      "ABRACADABRA"
    ]
  }
}
```