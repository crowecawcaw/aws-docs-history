

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# CodeDeploy deployment groups
<a name="service-create-codedeploy-dep-group"></a>

Create CodeDeploy application groups.

## Create CodeDeploy deployment group
<a name="ex-cd-dep-group-create-col"></a>

### Creating a CodeDeploy deployment group with the console
<a name="cd-dep-group-create-con"></a>

![Change type details showing ID, version 1.0, and automated execution mode for deployment group.](http://docs.aws.amazon.com/managedservices/latest/appguide/images/guiCDDepGroupCreateCT.png)


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

### Creating a CodeDeploy deployment group with the CLI
<a name="cd-dep-group-create-cli"></a>

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
aws amscm create-rfc --change-type-id "ct-2gd0u847qd9d2" --change-type-version "1.0" --title "{{Stack-Create-CD-Dep-Group}}" --execution-parameters "{\"Description\":\"{{TestCdDepGroupRfc}}\",\"VpcId\":\"{{VPC_ID}}\",\"StackTemplateId\":\"stm-sp9lrk00000000000\",\"Name\":\"{{MyTestCDDepGroup}}\",\"TimeoutInMinutes\":60,\"Parameters\":{\"CodeDeployApplicationName\":\"{{TestCDApp}}\",\"CodeDeployAutoScalingGroups\":[\"{{TestASG}}\"],\"CodeDeployDeploymentConfigName\":\"{{CodeDeployDefault.OneAtATime}}\",\"CodeDeployDeploymentGroupName\":\"{{Test}}\",\"CodeDeployServiceRoleArn\":\"{{arn:aws:iam::000000000:role/aws-codedeploy-role}}\"}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema to a file in your current folder; this example names it CreateCDDepGroupParams.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-2gd0u847qd9d2" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateCDDepGroupParams.json
   ```

1. Modify and save the JSON file. For example, you can replace the contents with something like this:

   ```
   {
   "Description":                      "{{CreateCDDeploymentGroup}}",
   "VpcId":                            "{{VPC_ID}}",
   "StackTemplateId":                  "stm-sp9lrk00000000000",
   "Name":                             "{{WordPressCDAppGroup}}",
   "TimeoutInMinutes":                 60,
   "Parameters":   {
       "CodeDeployApplicationName":        "{{WordPressCDApp}}",
       "CodeDeployAutoScalingGroups":      ["{{ASG_NAME}}"],
       "CodeDeployDeploymentConfigName":   "CodeDeployDefault.HalfAtATime",
       "CodeDeployDeploymentGroupName":    "{{UNIQUE_CDDepGroupNAME}}",
       "CodeDeployServiceRoleArn":         "arn:aws:iam::{{ACCOUNT_ID}}:role/aws-codedeploy-role"
       }
   }
   ```

1. Output the JSON template for CreateRfc to a file in your current folder; this example names it CreateCDDepGroupRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreateCDDepGroupRfc.json
   ```

1. Modify and save the JSON file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{1.0}}",
   "ChangeTypeId":         "ct-2gd0u847qd9d2",
   "Title":                "{{CD-Dep-Group-RFC}}"
   }
   ```

1. Create the RFC, specifying the CreateCDDepGroupRfc file and the execution parameters file:

   ```
   aws amscm create-rfc --cli-input-json file://CreateCDDepGroupRfc.json --execution-parameters file://CreateCDDepGroupParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-cd-dep-group-create-tip"></a>

For more information about AWS CodeDeploy deployment groups, see [Create a Deployment Group with AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-groups-create.html).

## Create CodeDeploy deployment group for EC2
<a name="ex-cd-dep-group-ec2-create-col"></a>

### Creating a CodeDeploy deployment group for EC2 with the console
<a name="cd-dep-group-ec2-create-con"></a>

![Change type details showing CodeDeploy deployment group creation with EC2 instance targeting.](http://docs.aws.amazon.com/managedservices/latest/appguide/images/guiCDDepGroupCreate4Ec2CT.png)


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

### Creating a CodeDeploy deployment group for EC2 with the CLI
<a name="cd-dep-group-ec2-create-cli"></a>

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
aws amscm create-rfc --change-type-id "ct-00tlkda4242x7" --change-type-version "1.0" --title "{{Stack-Create-CD-Ec2-Dep-Group}}" --execution-parameters "{\"Description\":\"{{MyTestCdDepEc2DepGroup}}\",\"VpcId\":\"{{VPC_ID}}\",\"Name\":\"{{TestCDDepEc2Group}}\",\"StackTemplateId\":\"stm-n3hsoirgqeqqdbpk2\",\"TimeoutInMinutes\":60,\"Parameters\":{\"ApplicationName\":\"{{TestCDApp}}\",\"DeploymentConfigName\":\"{{CodeDeployDefault.OneAtATime}}\",\"AutoRollbackEnabled\":\"{{False}}\",\"EC2FilterTag\":\"{{Name=Test}}\",\"EC2FilterTag2\":\"\",\"EC2FilterTag3\":\"\",\"ServiceRoleArn\":\"\"}}"
```

*TEMPLATE CREATE*:

1. Output the execution parameters JSON schema to a file; this example names it CreateCDDepGroupEc2Params.json:

   ```
   aws amscm get-change-type-version --change-type-id "ct-00tlkda4242x7" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateCDDepGroupEc2Params.json
   ```

1. Modify and save the JSON file. For example, you can replace the contents with something like this:

   ```
   {
   "Description":                      "{{CreateCDDepGroupEc2}}",
   "VpcId":                            "{{VPC_ID}}",
   "StackTemplateId":                  "stm-n3hsoirgqeqqdbpk2",
   "Name":                             "{{CDAppGroupEc2}}",
   "TimeoutInMinutes":                 60,
   "Parameters":   {
       "ApplicationName":        "{{CDAppEc2}}",
       "DeploymentConfigName":   "{{CodeDeployDefault.OneAtATime}}",
       "CodeDeployDeploymentGroupName":    "{{UNIQUE_CDDepGroupNAME}}",
       "CodeDeployServiceRoleArn":         "arn:aws:iam::{{ACCOUNT_ID}}:role/aws-codedeploy-role"
       }
   }
   ```

1. Output the JSON template for CreateRfc to a file in your current folder; this example names it CreateCDDepGroupEc2Rfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreateCDDepGroupEc2Rfc.json
   ```

1. Modify and save the JSON file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeVersion":    "{{1.0}}",
   "ChangeTypeId":         "ct-00tlkda4242x7",
   "Title":                "{{CD-Dep-Group-For-Ec2-Stack-RFC}}"
   }
   ```

1. Create the RFC, specifying the CreateCDDepGroupEc2Rfc file and the execution parameters file:

   ```
   aws amscm create-rfc --cli-input-json file://CreateCDDepGroupEc2Rfc.json --execution-parameters file://CreateCDDepGroupEc2Params.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

### Tips
<a name="ex-cd-dep-group-ec2-create-tip"></a>

For more information about AWS CodeDeploy deployment groups, see [Create a Deployment Group with AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-groups-create.html).