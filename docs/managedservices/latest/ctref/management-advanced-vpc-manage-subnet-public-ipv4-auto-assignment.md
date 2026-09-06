

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# VPC \| Manage Subnet Public IPv4 Auto Assignment
<a name="management-advanced-vpc-manage-subnet-public-ipv4-auto-assignment"></a>

Allow or disallow the automatic assignment of public IPv4 addresses for specified subnets.

**Full classification:** Management \| Advanced stack components \| VPC \| Manage subnet public IPv4 auto assignment

## Change Type Details
<a name="ct-1pqxczuw5uwu6-MAVm-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-1pqxczuw5uwu6 | 
| Current version | 1.0 | 
| Expected execution duration | 60 minutes | 
| AWS approval | Required | 
| Customer approval | Not required | 
| Execution mode | Automated | 

## Additional Information
<a name="management-advanced-vpc-manage-subnet-public-ipv4-auto-assignment-info"></a>

### Manage the VPC Subnet IPv4 Address Auto Assigment
<a name="ex-vpc-subnet-ipv4-assignment-manage-col"></a>

#### Manage VPC Subnet IPv4 Address Auto Assigment with the console
<a name="vpc-subnet-ipv4-assignment-manage-con"></a>

The following shows this change type in the AMS console.

![Manage subnet public IPv4 auto assignment change type details in the AMS console.](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiVpcManageSubnetAddressCT.png)


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

#### Manage VPC Subnet IPv4 Address Auto Assigment with the CLI
<a name="vpc-subnet-ipv4-assignment-manage-cli"></a>

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
aws amscm create-rfc --change-type-id "ct-1pqxczuw5uwu6" --change-type-version "1.0" --title "{{AWSManagedServices-ManageSubnetPublicIpv4AutoAssign}}" --execution-parameters "{\"DocumentName\": \"AWSManagedServices-ManageSubnetPublicIpv4AutoAssign\",\"Region\": \"{{us-east-1}}\",\"Parameters\": {\"SubnetId\": \"{{subnet-0a1b2c3d4e5f67890}}\", \"MapPublicIpOnLaunch\": {{true}}, \"AcknowledgeNetworkImpact\": [\"{{Yes}}\"]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema for this change type; this example names it ManageSubnetAutoAddressParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-1pqxczuw5uwu6" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > ManageSubnetAutoAddressParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
    "DocumentName": "AWSManagedServices-ManageSubnetPublicIpv4AutoAssign",
    "Region": "{{us-east-1}}",
    "Parameters": {
        "SubnetId": "{{subnet-0a1b2c3d4e5f67890}}",
        "MapPublicIpOnLaunch": {{true}},
        "AcknowledgeNetworkImpact": [
            "{{Yes}}"
        ]
    }
   }
   ```

1. Output the RFC template JSON file; this example names it ManageSubnetAutoAddressRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > ManageSubnetAutoAddressRfc.json
   ```

1. Modify and save the ManageSubnetAutoAddressRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion" : "1.0",
     "ChangeTypeId" : "ct-1pqxczuw5uwu6",
     "Title" : "{{ManageSubnetAutoAddress}}"
   }
   ```

1. Create the RFC, specifying the ManageSubnetAutoAddressRfc file and the ManageSubnetAutoAddressParams file:

   ```
   aws amscm create-rfc --cli-input-json file://ManageSubnetAutoAddressRfc.json  --execution-parameters file://ManageSubnetAutoAddressParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

#### Tips
<a name="ex-vpc-endpoint-gateway-create-tip"></a>

For general information on VPCs and subnet addressing, see [IP addressing for your VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html).

## Execution Input Parameters
<a name="management-advanced-vpc-manage-subnet-public-ipv4-auto-assignment-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-1pqxczuw5uwu6](schemas.md#ct-1pqxczuw5uwu6-schema-section).

## Example: Required Parameters
<a name="management-advanced-vpc-manage-subnet-public-ipv4-auto-assignment-ex-min"></a>

```
{
    "DocumentName": "AWSManagedServices-ManageSubnetPublicIpv4AutoAssign",
    "Region": "us-east-1",
    "Parameters": {
      "SubnetId": "subnet-0a1b2c3d4e5f67890",
      "MapPublicIpOnLaunch": false,
      "AcknowledgeNetworkImpact": ["No"]
    }
}
```

## Example: All Parameters
<a name="management-advanced-vpc-manage-subnet-public-ipv4-auto-assignment-ex-max"></a>

```
{
  "DocumentName": "AWSManagedServices-ManageSubnetPublicIpv4AutoAssign",
  "Region": "us-east-1",
  "Parameters": {
    "SubnetId": "subnet-0a1b2c3d4e5f67890",
    "MapPublicIpOnLaunch": true,
    "AcknowledgeNetworkImpact": ["Yes"]
  }
}
```