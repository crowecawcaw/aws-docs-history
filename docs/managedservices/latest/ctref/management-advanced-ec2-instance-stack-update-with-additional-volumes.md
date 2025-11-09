# EC2 Instance Stack | Update (With Additional Volumes)

Use to modify the properties of an EC2 instance created using CT id ct-1aqsjf86w6vxg, version 3.0.

**Full classification:** Management | Advanced stack components | EC2 instance stack | Update (with additional volumes)

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-1o1x2itfd6rk8 |
| Current version             | 3.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Update stack (with additional volumes)

Screenshot of this change type in the AMS console:

![Change type details for updating EC2 stack with additional volumes, showing ID and version.](images/guiEc2UpdateAddlVolCT.png)
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
aws amscm create-rfc --title test-ec2-stack-with-additional-volumes-update --change-type-id ct-1o1x2itfd6rk8 --change-type-version 3.0 --execution-parameters '{"VpcId":"`VPC_ID`","StackId":"`STACK_ID`","Parameters":{"InstanceDetailedMonitoring":`false`,"InstanceEBSOptimized":`false`,"InstanceProfile":"`customer-mc-ec2-instance-profile`","InstanceType":"`t2.small`","InstanceUserData":"`#!/bin/bash\\npwd\\nls -ltrh\\necho` \"`Hello, World`\"","InstanceSecondaryPrivateIpAddressCount":`1`,"InstanceTerminationProtection":`true`,"Volume1Iops":`100`,"Volume1KmsKeyId":"`12345678-1234-1234-1234-1234567890ab`","Volume1Name":"`/dev/sdf`","Volume1Size":`100`,"Volume1Type":"`io1`"}}'
```

_TEMPLATE CREATE_:

1. Output the execution parameters for this change type to a JSON file; this example names it UpdateEC2AVParams.json:

```
aws amscm get-change-type-version --change-type-id "ct-1o1x2itfd6rk8" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateEC2AVParams.json
```

2. Modify and save the UpdateEC2AVParams file, retaining only the parameters that you want to change. For example, you can replace the contents with something like this:

```
{
"Description":      "`EC2-Update-1-Addl-Volumes`",
"VpcId":            "`VPC_ID`",
"Name":             "`My-EC2-1-Addl-Volume`",
"TimeoutInMinutes": 60,
"Parameters":   {
    "InstanceAmiId":    "`AMI_ID`",
    "InstanceSubnetId": "`SUBNET_ID`",
    "Volume1Encrypted": "`true`",
    "Volume1Iops":      "`IOPS`"
    "Volume1KmsKeyId":  "`KMS_MASTER_KEY_ID`",
    "Volume1Name":      "`xvdh`"
    "Volume1Size":      "`2 GiB`",
    "Volume1Snapshot":  "`SNAPSHOT_ID`",
    "Volume1Type":      "`iol`"
    }
}
```

3. Output the RFC template to a file in your current folder; this example names it UpdateEC2AVRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > UpdateEC2AVRfc.json
```

4. Modify and save the UpdateEC2AVRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`3.0`",
"ChangeTypeId":         "ct-1o1x2itfd6rk8",
"Title":                "`EC2-Update-1-Addl-Volume-RFC`"
}
```

5. Create the RFC, specifying the UpdateEC2AVRfc file and the UpdateEC2AVParams file:

```
aws amscm create-rfc --cli-input-json file://UpdateEC2AVRfc.json  --execution-parameters file://UpdateEC2AVParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

###### Note

This is a version 3.0 change type and can be used to update EC2 instances created with the corresponding version 3.0 create change type, ct-1aqsjf86w6vxg.

To learn more about Amazon EC2, including size recommendations, see
[Amazon Elastic Compute Cloud Documentation](https://aws.amazon.com/documentation/ec2/ "https://aws.amazon.com/documentation/ec2/").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-1o1x2itfd6rk8](schemas.md#ct-1o1x2itfd6rk8-schema-section "schemas.md#ct-1o1x2itfd6rk8-schema-section").

## Example: Required Parameters

```
{
  "VpcId": "vpc-1234567890abcdef0",
  "StackId": "stack-1234567890abcdef0",
  "Parameters": {
  }
}

```

## Example: All Parameters

```
{
  "VpcId": "vpc-1234567890abcdef0",
  "StackId": "stack-1234567890abcdef0",
  "Parameters": {
    "InstanceDetailedMonitoring": false,
    "InstanceEBSOptimized": false,
    "InstanceProfile": "customer-mc-ec2-instance-profile",
    "InstanceType": "t2.small",
    "InstanceUserData": "#!/bin/bash\\npwd\\nls -ltrh\\necho \"Hello, World\"",
    "InstanceSecondaryPrivateIpAddressCount": 1,
    "InstanceTerminationProtection": true,
    "Volume1Iops": 100,
    "Volume1Name": "/dev/sdf",
    "Volume1Size": 100,
    "Volume1Snapshot": "snap-1234567890abcdef0",
    "Volume1Type": "io1",
    "Volume2Iops": 100,
    "Volume2Name": "/dev/sdg",
    "Volume2Size": 100,
    "Volume2Snapshot": "snap-1234567890abcdef0",
    "Volume2Type": "io1",
    "Volume3Iops": 100,
    "Volume3Name": "/dev/sdh",
    "Volume3Size": 100,
    "Volume3Snapshot": "snap-1234567890abcdef0",
    "Volume3Type": "io1",
    "Volume4Iops": 100,
    "Volume4Name": "/dev/sdi",
    "Volume4Size": 100,
    "Volume4Snapshot": "snap-1234567890abcdef0",
    "Volume4Type": "io1",
    "Volume5Iops": 100,
    "Volume5Name": "/dev/sdj",
    "Volume5Size": 100,
    "Volume5Snapshot": "snap-1234567890abcdef0",
    "Volume5Type": "io1"
  }
}

```
