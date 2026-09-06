

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# EC2 Instance Stack \| Change Hostname (Linux)
<a name="management-advanced-ec2-instance-stack-change-hostname-linux"></a>

Change the hostname of an EC2 Linux instance. If no hostname is provided, then the hostname is randomized.

**Full classification:** Management \| Advanced stack components \| EC2 instance stack \| Change hostname (Linux)

## Change Type Details
<a name="ct-2781aqd6f6svs-MAEc-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-2781aqd6f6svs | 
| Current version | 2.0 | 
| Expected execution duration | 360 minutes | 
| AWS approval | Required | 
| Customer approval | Not required | 
| Execution mode | Automated | 

## Additional Information
<a name="management-advanced-ec2-instance-stack-change-hostname-linux-info"></a>

### Change hostname (Linux)
<a name="ex-ec2-hostname-change-linux-col"></a>

#### Changing the hostname for a Linux EC2 instance with the console
<a name="ec2-hostname-change-linux-con"></a>

The following shows this change type in the AMS console.

![Change Linux Hostname interface showing ID, execution mode, version, and description.](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiEc2HostnameChangeLinuxCT.png)


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

#### Changing the hostname for a Linux EC2 instance with the CLI
<a name="ec2-hostname-change-linux-cli"></a>

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
aws amscm create-rfc --change-type-id "ct-2781aqd6f6svs" --change-type-version "2.0" --title "{{Change Linux hostname}}" --execution-parameters "{\"DocumentName\": \"AWSManagedServices-ChangeHostname\",\"Region\": \"{{us-east-1}}\",\"Parameters\": {\"InstanceId\": [\"{{i-1234567890abcdef0}}\"],\"Hostname\": [\"{{01234567890abcd}}\"],\"Platform\": [\"linux\"]}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file; this example names it ChangeLinuxHostnameParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-2781aqd6f6svs" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > ChangeLinuxHostnameParams.json
   ```

1. Modify and save the ChangeLinuxHostnameParams file, retaining only the parameters that you want to change. For example, you can replace the contents with something like this:

   ```
   {
     "DocumentName": "AWSManagedServices-ChangeHostname",
     "Region": "{{us-east-1}}",
     "Parameters": {
       "InstanceId": [ "{{i-1234567890abcdef0}}" ],
       "Hostname": [ "{{01234567890abcd}}" ],
       "Platform" : ["linux"]
     }
   }}
   ```

1. Output the RFC template to a file in your current folder; this example names it ChangeLinuxHostnameRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > ChangeLinuxHostnameRfc.json
   ```

1. Modify and save the ChangeLinuxHostnameRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
     "ChangeTypeVersion": "2.0",
     "ChangeTypeId": "ct-2781aqd6f6svs",
     "Title": "{{Change Linux Hostname}}"
   }
   ```

1. Create the RFC, specifying the ChangeLinuxHostnameRfc file and the ChangeLinuxHostnameParams file:

   ```
   aws amscm create-rfc --cli-input-json file://ChangeLinuxHostnameRfc.json  --execution-parameters file://ChangeLinuxHostnameParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

#### Tips
<a name="ex-ec2-hostname-change-linux-tip"></a>

**Note**  
This change type is at a new version, 2.0, and is now automated (version 1.0 was execution mode=manual). There are additional parameters, notably **DocumentName** and **Platform**.

To learn more about doing this, see [ Changing the hostname of your Amazon Linux instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-hostname.html).

## Execution Input Parameters
<a name="management-advanced-ec2-instance-stack-change-hostname-linux-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-2781aqd6f6svs](schemas.md#ct-2781aqd6f6svs-schema-section).

## Example: Required Parameters
<a name="management-advanced-ec2-instance-stack-change-hostname-linux-ex-min"></a>

```
{
  "DocumentName" : "AWSManagedServices-ChangeHostname",
  "Region" : "us-east-1",
  "Parameters" : {
    "InstanceId" : [
      "i-1234567890abcdef0"
    ],
    "Platform" : [
      "linux"
    ]
  }
}
```

## Example: All Parameters
<a name="management-advanced-ec2-instance-stack-change-hostname-linux-ex-max"></a>

```
{
  "DocumentName" : "AWSManagedServices-ChangeHostname",
  "Region" : "us-east-1",
  "Parameters" : {
    "InstanceId" : [
      "i-1234567890abcdef0"
    ],
    "Hostname" : [
      "testhostname"
    ],
    "Platform" : [
      "linux"
    ]
  }
}
```