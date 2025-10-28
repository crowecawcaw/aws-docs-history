# EC2 instances: Creating

You can use the AMS console or API/CLI to create an Amazon EC2 and an Amazon EC2 with additional volumes.

## Create stack

The following shows this change type in the AMS console.

![EC2 stack creation details showing ID, execution mode, and version in a classification hierarchy.](images/guiEc2CreateCT.png)
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

Issue the create RFC command with execution parameters provided inline (escape
quotation marks when providing execution parameters inline), and then submit the
returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-14027q0sjyt1h" --change-type-version "4.0" --title "`EC2-Create-RFC`" --execution-parameters "{\"Description\": \"`Create a new EC2 Instance stack`\",\"VpcId\": \"`vpc-0a60eb65b4EXAMPLE`\",\"Name\": \"`My-EC2`\",\"TimeoutInMinutes\": `60`,\"Parameters\": {\"InstanceAmiId\": \"`ami-1234567890EXAMPLE`\",\"InstanceDetailedMonitoring\": `false`,\"InstanceEBSOptimized\": `false`,\"InstanceProfile\": \"`customer-mc-ec2-instance-profile`\",\"InstanceRootVolumeIops\": `3000`,\"InstanceRootVolumeType\": \"`gp3`\",\"InstanceType\": \"`t2.large`\",\"InstanceUserData\": \"\",\"InstanceSubnetId\": \"`subnet-0bb1c79de3EXAMPLE`\",\"EnforceIMDSV2\": \"`false`\"}}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters for this change type to a JSON file; this
   example names it CreateEC2Params.json:

```
aws amscm get-change-type-version --change-type-id "ct-14027q0sjyt1h" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateEC2Params.json
```

2. Modify and save the CreateEC2Params file. For example, you can replace the contents with something like this:

```
{
  "Description": "Create a new EC2 Instance stack",
  "VpcId": "vpc-0a60eb65b4EXAMPLE",
  "Name": "My-EC2",
  "TimeoutInMinutes": 60,
  "Parameters": {
    "InstanceAmiId": "ami-1234567890EXAMPLE",
    "InstanceDetailedMonitoring": false,
    "InstanceEBSOptimized": false,
    "InstanceProfile": "customer-mc-ec2-instance-profile",
    "InstanceRootVolumeIops": 3000,
    "InstanceRootVolumeType": "gp3",
    "InstanceType": "t2.large",
    "InstanceUserData": "",
    "InstanceSubnetId": "subnet-0bb1c79de3EXAMPLE",
    "EnforceIMDSV2": "false"
  }
}
```

3. Output the RFC template to a file in your current folder; this example names
   it CreateEC2Rfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > CreateEC2Rfc.json
```

4. Modify and save the CreateEC2Rfc.json file. For example, you can replace the contents with something like this:.

```
{
"ChangeTypeVersion":    "`4.0`",
"ChangeTypeId":         "ct-14027q0sjyt1h",
"Title":                "`EC2-Create-RFC`"
}
```

5. Create the RFC, specifying the CreateEC2Rfc file and the CreateEC2Params
   file:

```
aws amscm create-rfc --cli-input-json file://CreateEC2Rfc.json  --execution-parameters file://CreateEC2Params.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

###### Security Groups

Starting with version 3.0 of this change type, AMS does not attach the default
AMS security groups if you specify your own security groups. If you do not specify your own
security groups in the request, AMS attaches the AMS default security groups. In previous
versions, AMS attached the default security groups whether or not you provided your own
security groups.

Currently, if you specify custom security groups, you must also specify the
IDs of the default AMS security groups for your account,
`mc-initial-garden-SG-name` and `mc-initial-garden-SG-name`.

###### Instance Types

AMS does not recommend the
**t2.micro/t3.micro** and
**t2.nano/t3.nano** types.
These are smaller instance types, and can degrade the
performance of your application and AMS tools.
EC2 instances need enough
capacity to support AMS tools such as EPS, SSM, and Cloudwatch in addition to
the application workload. For more information, see
[Choosing the Right EC2 Instance Type for Your Application](https://aws.amazon.com/blogs/aws/choosing-the-right-ec2-instance-type-for-your-application/ "https://aws.amazon.com/blogs/aws/choosing-the-right-ec2-instance-type-for-your-application/").

To create an EC2 stack with additional volumes, see
[EC2 Stack | Create (with Additional Volumes)](../ctref/deployment-advanced-ec2-stack-create-with-additional-volumes.md "../ctref/deployment-advanced-ec2-stack-create-with-additional-volumes.md").

You can add up to 50 tags, but to do so you must enable the **Additional configuration** view.

If needed, see [EC2 instance stack create fail](../userguide/rfc-troubleshoot.md#rfc-valid-execute-ec2-create "../userguide/rfc-troubleshoot.md#rfc-valid-execute-ec2-create").

## Create stack (with additional volumes)

The following shows this change type in the AMS console.

![EC2 stack creation details showing ID, execution mode, and version for additional volumes.](images/guiEc2CreateAddlVolCT.png)
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

Issue the create RFC command with execution parameters provided inline (escape quotation
marks when providing execution parameters inline), and then submit the returned RFC ID
(example shows required parameters only). For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-1aqsjf86w6vxg" --change-type-version "4.0" --title "`EC2-Create-A-V-QC`" --execution-parameters "{\"Description\":\"`My EC2 stack with addl vol`\",\"VpcId\":\"`VPC_ID`\",\"Name\":\"`My Stack`\",\"StackTemplateId\":\"stm-nn8v8ffhcal611bmo\",\"TimeoutInMinutes\":60,\"Parameters\":{\"InstanceAmiId\":\"`AMI_ID`\",\"InstanceSubnetId\":\"`SUBNET_ID`\"}}
```

_TEMPLATE CREATE_:

1. Output the execution parameters for this change type to a JSON file named
   CreateEC2AVParams.json.

```
aws amscm get-change-type-version --change-type-id "ct-1aqsjf86w6vxg" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateEC2AVParams.json
```

2. Modify and save the CreateEC2AVParams file (example shows most parameters).
   For example, you can replace the contents with something like this:

```
{
"Description":      "`EC2-Create-1-Addl-Volumes`",
"VpcId":            "`VPC_ID`",
"StackTemplateId":  "stm-nn8v8ffhcal611bmo",
"Name":             "`My-EC2-1-Addl-Volume`",
"TimeoutInMinutes": 60,
"Parameters":   {
    "InstanceAmiId":    "`AMI_ID`",
    "InstanceSecurityGroupIds": "`SECURITY_GROUP_ID`",
    "InstanceCoreCount": `1`,
    "InstanceThreadsPerCore": `2`,
    "InstanceDetailedMonitoring": "`true`",
    "InstanceEBSOptimized": "`false`",
    "InstanceProfile": "`customer-mc-ec2-instance-profile`",
    "InstanceRootVolumeIops": `100`,
    "InstanceRootVolumeName": "`/dev/xvda`",
    "InstanceRootVolumeSize": `50`,
    "InstanceRootVolumeType": "`io1`",
    "RootVolumeKmsKeyId": "`default`",
    "InstancePrivateStaticIp": "`10.27.0.100`",
    "InstanceSecondaryPrivateIpAddressCount": `0`,
    "InstanceTerminationProtection": "`false`",
    "InstanceType": "`t3.large`",
    "CreditSpecification": "`unlimited`",
    "InstanceUserData": "`echo $`",
    "Volume1Encrypted": "`true`",
    "Volume1Iops":      "`IOPS`"
    "Volume1KmsKeyId":  "`KMS_MASTER_KEY_ID`",
    "Volume1Name":      "`xvdh`"
    "Volume1Size":      "`2 GiB`",
    "Volume1Snapshot":  "`SNAPSHOT_ID`",
    "Volume1Type":      "`iol`",
    "InstanceSubnetId": "`SUBNET_ID`"
    }
}
```

3. Output the RFC template to a file in your current folder; this example names it
   CreateEC2AVRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > CreateEC2AVRfc.json
```

4. Modify and save the CreateEC2AVRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`4.0`",
"ChangeTypeId":         "ct-1aqsjf86w6vxg",
"Title":                "`EC2-Create-1-Addl-Volume-RFC`"
}
```

5. Create the RFC, specifying the CreateEC2AVRfc file and the CreateEC2AVParams
   file:

```
aws amscm create-rfc --cli-input-json file://CreateEC2AVRfc.json  --execution-parameters file://CreateEC2AVParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

###### Important

There is a new version of this change type, v 4.0, that uses a different
StackTemplateId (stm-nn8v8ffhcal611bmo). This is important if you're submitting the RFC with
this change type at the command line. The new version introduces two new parameters
(**RootVolumeKmsKeyId** and **CreditSpecification**) and
changes the default for one existing parameter (**InstanceType**).

###### Instance Types

- If you choose to specify the number of cores or threads, you must specify values for both. Use the parameters
  `InstanceCoreCount` and `InstanceThreadsPerCore`. To find valid combinations of cores/threads,
  see [CPU cores and threads per CPU core per instance type](../../../AWSEC2/latest/UserGuide/cpu-options-supported-instances-values.md "../../../AWSEC2/latest/UserGuide/cpu-options-supported-instances-values.md") .
- AMS does not recommend the **t2.micro/t3.micro** or
  **t2.nano/t3.nano** instance types. These are too small to support
  AMS tools such as EPS, SSM, and Cloudwatch in addition to your business workload.
  For more information, see
  [Choosing the Right EC2 Instance Type for Your Application](https://aws.amazon.com/blogs/aws/choosing-the-right-ec2-instance-type-for-your-application/ "https://aws.amazon.com/blogs/aws/choosing-the-right-ec2-instance-type-for-your-application/").
- In version 4.0, the default type was raised from **t2.large** to
  **t3.large**.
  T3 instances launch with 'unlimited credits' by default. You won't experience
  CPU throttling even if the instance consumes all CPU credits.
  You can, instead, choose T2 instances and use the CreditSpecification unlimited option.
- For more information about Amazon EC2, including size recommendations, see [Amazon Elastic Compute Cloud
  Documentation](https://aws.amazon.com/documentation/ec2/ "https://aws.amazon.com/documentation/ec2/").
  To update your EC2 stack with additional volumes after they're created, see
  [EC2 Instance stack: Updating (With Additional
  Volumes)](../ctref/management-advanced-ec2-instance-stack-update-with-additional-volumes.md "../ctref/management-advanced-ec2-instance-stack-update-with-additional-volumes.md")
