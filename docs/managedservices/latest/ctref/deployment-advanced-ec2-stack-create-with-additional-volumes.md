

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# EC2 Stack \| Create (With Additional Volumes)
<a name="deployment-advanced-ec2-stack-create-with-additional-volumes"></a>

Create an Amazon Elastic Compute Cloud (EC2) instance with up to five additional volumes.

**Full classification:** Deployment \| Advanced stack components \| EC2 stack \| Create (with additional volumes)

## Change Type Details
<a name="ct-1aqsjf86w6vxg-DAEc-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-1aqsjf86w6vxg | 
| Current version | 5.0 | 
| Expected execution duration | 360 minutes | 
| AWS approval | Required | 
| Customer approval | Not required | 
| Execution mode | Automated | 

## Additional Information
<a name="deployment-advanced-ec2-stack-create-with-additional-volumes-info"></a>

### Create stack (with additional volumes)
<a name="ex-ec2-create-addl-vol-col"></a>

#### Creating an EC2 instance and additional volumes with the console
<a name="ec2-create-addl-vol-con"></a>

The following shows this change type in the AMS console.

![Create EC2 Stack With Additional Volumes change type details showing ID, execution mode, and version.](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiEc2CreateAddlVolCT.png)


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

#### Creating an EC2 instance and additional volumes with the CLI
<a name="ec2-create-addl-vol-cli"></a>

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

Issue the create RFC command with execution parameters provided inline (escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID (example shows required parameters only). For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-1aqsjf86w6vxg" --change-type-version "4.0" --title "{{EC2-Create-A-V-QC}}" --execution-parameters "{\"Description\":\"{{My EC2 stack with addl vol}}\",\"VpcId\":\"{{VPC_ID}}\",\"Name\":\"{{My Stack}}\",\"StackTemplateId\":\"stm-nn8v8ffhcal611bmo\",\"TimeoutInMinutes\":60,\"Parameters\":{\"InstanceAmiId\":\"{{AMI_ID}}\",\"InstanceSubnetId\":\"{{SUBNET_ID}}\"}}
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file named CreateEC2AVParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-1aqsjf86w6vxg" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateEC2AVParams.json
   ```

1. Modify and save the CreateEC2AVParams file (example shows most parameters). For example, you can replace the contents with something like this:

   ```
   {
   "Description":      "{{EC2-Create-1-Addl-Volumes}}",
   "VpcId":            "{{VPC_ID}}",
   "StackTemplateId":  "stm-nn8v8ffhcal611bmo",
   "Name":             "{{My-EC2-1-Addl-Volume}}",
   "TimeoutInMinutes": 60,
   "Parameters":   {
       "InstanceAmiId":    "{{AMI_ID}}",
       "InstanceSecurityGroupIds": "{{SECURITY_GROUP_ID}}",
       "InstanceCoreCount": {{1}},
       "InstanceThreadsPerCore": {{2}},    
       "InstanceDetailedMonitoring": "{{true}}",
       "InstanceEBSOptimized": "{{false}}",
       "InstanceProfile": "{{customer-mc-ec2-instance-profile}}",
       "InstanceRootVolumeIops": {{100}},
       "InstanceRootVolumeName": "{{/dev/xvda}}",
       "InstanceRootVolumeSize": {{50}},
       "InstanceRootVolumeType": "{{io1}}",
       "RootVolumeKmsKeyId": "{{default}}",
       "InstancePrivateStaticIp": "{{10.27.0.100}}",
       "InstanceSecondaryPrivateIpAddressCount": {{0}},
       "InstanceTerminationProtection": "{{false}}",
       "InstanceType": "{{t3.large}}",
       "CreditSpecification": "{{unlimited}}",
       "InstanceUserData": "{{echo $}}",
       "Volume1Encrypted": "{{true}}",
       "Volume1Iops":      "{{IOPS}}"
       "Volume1KmsKeyId":  "{{KMS_MASTER_KEY_ID}}",
       "Volume1Name":      "{{xvdh}}"
       "Volume1Size":      "{{2 GiB}}",
       "Volume1Snapshot":  "{{SNAPSHOT_ID}}",
       "Volume1Type":      "{{iol}}",
       "InstanceSubnetId": "{{SUBNET_ID}}"
       }
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it CreateEC2AVRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreateEC2AVRfc.json
   ```

1. Modify and save the CreateEC2AVRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{4.0}}",
   "ChangeTypeId":         "ct-1aqsjf86w6vxg",
   "Title":                "{{EC2-Create-1-Addl-Volume-RFC}}"
   }
   ```

1. Create the RFC, specifying the CreateEC2AVRfc file and the CreateEC2AVParams file:

   ```
   aws amscm create-rfc --cli-input-json file://CreateEC2AVRfc.json  --execution-parameters file://CreateEC2AVParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

#### Tips
<a name="ex-ec2-create-addl-vol-tip"></a>

**Important**  
There is a new version of this change type, v 4.0, that uses a different StackTemplateId (stm-nn8v8ffhcal611bmo). This is important if you're submitting the RFC with this change type at the command line. The new version introduces two new parameters (**RootVolumeKmsKeyId** and **CreditSpecification**) and changes the default for one existing parameter (**InstanceType**).

****Instance Types****  
 If you choose to specify the number of cores or threads, you must specify values for both. Use the parameters `InstanceCoreCount` and `InstanceThreadsPerCore`. To find valid combinations of cores/threads, see [ CPU cores and threads per CPU core per instance type ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cpu-options-supported-instances-values.html). 
 AMS does not recommend the **t2.micro/t3.micro** or **t2.nano/t3.nano** instance types. These are too small to support AMS tools such as EPS, SSM, and Cloudwatch in addition to your business workload. For more information, see [Choosing the Right EC2 Instance Type for Your Application](https://aws.amazon.com/blogs/aws/choosing-the-right-ec2-instance-type-for-your-application/). 
 In version 4.0, the default type was raised from **t2.large** to **t3.large**. T3 instances launch with 'unlimited credits' by default. You won't experience CPU throttling even if the instance consumes all CPU credits. You can, instead, choose T2 instances and use the CreditSpecification unlimited option. 
For more information about Amazon EC2, including size recommendations, see [Amazon Elastic Compute Cloud Documentation](https://aws.amazon.com/documentation/ec2/). 
+ To update your EC2 stack with additional volumes after they're created, see [EC2 Instance stack: Updating (With Additional Volumes)](https://docs.aws.amazon.com/managedservices/latest/ctref/management-advanced-ec2-instance-stack-update-with-additional-volumes.html). 
+ Remove stale computer objects before provisioning an instance. If you plan to provision a new instance (Windows or Linux) using a hostname that already exists in Active Directory, for example, when restoring from an AMI or re-using a hostname from a previous stack, you must first run the [Management \| Directory Service \| Computer object \| Remove](https://docs.aws.amazon.com/managedservices/latest/ctref/management-directory-computer-object-remove.html) change type (ct-3d0lrfb8eckuu) to remove the stale computer object. AMS does not provision an instance if a computer object with the same hostname already exists in Active Directory. 

   If you don't remove the stale object, you might experience RFC rejection, duplicate computer objects in the wrong Organizational Unit (OU), broken domain join, DNS record conflicts, and inaccessible instances (RDP failures on Windows, or Kerberos authentication and SSH failures on Linux). This is especially important when the source AMI was captured from a running domain-joined instance without first preparing it. On Windows, this means not running `Invoke-AMSSysprep`, and on Linux, not running the AMS preparation script (`prepare_instance_for_ami_and_shutdown.sh`). 

   Without preparation, the AMI retains the previous instance's machine credentials (computer account SID and password on Windows, or Kerberos keytab on Linux), which causes trust relationship failures and object conflicts when a new instance boots from it. For more information on instance preparation, see the Tips section of [Deployment \| Advanced stack components \| AMI \| Create](https://docs.aws.amazon.com/managedservices/latest/ctref/deployment-advanced-ami-create.html) (ct-3rqqu43krekby). 

## Execution Input Parameters
<a name="deployment-advanced-ec2-stack-create-with-additional-volumes-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-1aqsjf86w6vxg](schemas.md#ct-1aqsjf86w6vxg-schema-section).

## Example: Required Parameters
<a name="deployment-advanced-ec2-stack-create-with-additional-volumes-ex-min"></a>

```
{
  "Description" : "Test description",
  "VpcId" : "vpc-12345678901234567",
  "Name" : "TestStack",
  "StackTemplateId" : "stm-nn8v8ffhcal611bmp",
  "TimeoutInMinutes" : 60,
  "Parameters" : {
    "InstanceAmiId" : "ami-1234567890abcdef0",
    "InstanceSubnetId" : "subnet-1234567890abcdef0",
    "EnforceIMDSV2": "true"
  }
}
```

## Example: All Parameters
<a name="deployment-advanced-ec2-stack-create-with-additional-volumes-ex-max"></a>

```
{
  "Description": "This is a test description",
  "VpcId": "vpc-12345678",
  "Name": "Test Stack",
  "Tags": [
    {
      "Key": "key1",
      "Value": "value1"
    },
    {
      "Key": "key2",
      "Value": "value2"
    }
  ],
  "Parameters": {
    "InstanceAmiId": "ami-12345678",
    "InstanceCoreCount": 0,
    "InstanceThreadsPerCore": 0,
    "InstanceRootVolumeName": "/dev/xvda",
    "InstanceRootVolumeSize": 100,
    "InstanceSubnetId": "subnet-12345678",
    "InstanceDetailedMonitoring": "false",
    "InstanceEBSOptimized": "false",
    "InstanceProfile": "customer-mc-ec2-instance-profile",
    "InstanceRootVolumeIops": 1000,
    "InstanceRootVolumeType": "io1",
    "InstancePrivateStaticIp": "172.16.0.10",
    "InstanceSecondaryPrivateIpAddressCount" : 1,
    "InstanceTerminationProtection" : "true",
    "InstanceType": "t2.small",
    "InstanceUserData": "#!/bin/bash\\npwd\\nls -ltrh\\necho \"Hello, World\"",
    "Volume1Iops": 100,
    "Volume1KmsKeyId": "12345678-1234-1234-1234-1234567890ab",
    "Volume1Name": "/dev/sdf",
    "Volume1Size": 100,
    "Volume1Type": "io1",
    "Volume2Iops": 100,
    "Volume2KmsKeyId": "12345678-1234-1234-1234-1234567890ab",
    "Volume2Name": "/dev/sdg",
    "Volume2Size": 100,
    "Volume2Type": "io1",
    "Volume3Iops": 100,
    "Volume3KmsKeyId": "12345678-1234-1234-1234-1234567890ab",
    "Volume3Name": "/dev/sdh",
    "Volume3Size": 100,
    "Volume3Type": "io1",
    "Volume4Iops": 100,
    "Volume4KmsKeyId": "12345678-1234-1234-1234-1234567890ab",
    "Volume4Name": "/dev/sdi",
    "Volume4Size": 100,
    "Volume4Type": "io1",
    "Volume5Iops": 100,
    "Volume5KmsKeyId": "12345678-1234-1234-1234-1234567890ab",
    "Volume5Name": "/dev/sdj",
    "Volume5Size": 100,
    "Volume5Type": "io1",
    "EnforceIMDSV2": "true"
  },
  "TimeoutInMinutes": 60,
  "StackTemplateId": "stm-nn8v8ffhcal611bmp"
}
```