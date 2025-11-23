# Auto Scaling Group | Update

Update an Auto Scaling Group and associated launch configuration created with CT ct-2tylseo8rxfsc, version 2.0.

**Full classification:** Management | Advanced stack components | Auto scaling group | Update

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-3fi2cx8b83iua |
| Current version             | 2.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Update Auto Scaling groups

The following shows this change type in the AMS console.

![Change type details for updating an Amazon EC2 Auto Scaling Group, showing description, ID, and execution mode.](images/guiAsgUpdateCT.png)
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
aws amscm  --profile saml --region us-east-1 create-rfc --change-type-id "ct-3fi2cx8b83iua" --change-type-version "2.0" --title "`Test-Update ASG`" --description "`Test Update`"  --execution-parameters "{\"VpcId\":\"`VPC_ID`\",\"StackId\":\"`STACK_ID`\",\"Parameters\":{\"ASGAmiId\":\"`AMI_ID`\",\"ASGInstanceType\":\"`m3.medium`\"}}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a file in your current folder; this example names it UpdateAsgParams.json:

```
aws amscm get-change-type-version --change-type-id "ct-3fi2cx8b83iua" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateAsgParams.json
```

###### Note

Scripts are newline-delimited (separate with literal: "\n"), also, scripts entered as UserData are executed as the "root" user and do not need to use the "sudo" command.

The RFC waits up to six hours for all of the UserData script commands to execute before returning a final status of success or failure. 2. Modify and save the file. For example, you can replace the contents with something like this:

```
{
  "VpcId": "`VPC_ID`",
  "StackId": "`STACK_ID`",
  "Parameters": {
    "ASGAmiId": "`AMI_ID`",
    "ASGInstanceType": "`m3.medium`"
  }
}
```

3. Output the JSON template for UpdateRfc to a file in your current folder; example names it UpdateAsgRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > UpdateAsgRfc.json
```

4. Modify and save the JSON file as follows. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`2.0`",
"ChangeTypeId":         "ct-3fi2cx8b83iua",
"Title":                "`ASG-Update-Stack-RFC`"
}
```

5. Create the RFC, specifying the UpdateAsgRfc file and the execution parameters file:

```
aws amscm create-rfc --cli-input-json file://UpdateAsgRfc.json --execution-parameters file://UpdateAsgParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

###### Note

This is a version 2.0 change type and can be used to update Auto Scaling groups
A(SG) created with the corresponding version 2.0 create change type, ct-2tylseo8rxfsc.

To learn more, see [Amazon Auto Scaling](https://aws.amazon.com/autoscaling/ "https://aws.amazon.com/autoscaling/").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-3fi2cx8b83iua](schemas.md#ct-3fi2cx8b83iua-schema-section "schemas.md#ct-3fi2cx8b83iua-schema-section").

## Example: Required Parameters

```
Example not available.
```

## Example: All Parameters

```
{
  "VpcId": "vpc-12345678",
  "StackId": "stack-12345678901234567",
  "Parameters": {
    "ASGAmiId": "ami-a0b1c2d3",
    "ASGCooldown": 300,
    "ASGDesiredCapacity": 1,
    "ASGEBSOptimized": "false",
    "ASGIAMInstanceProfile": "customer-mc-ec2-instance-profile",
    "ASGInstanceDetailedMonitoring": "false",
    "ASGInstanceRootVolumeIops": 0,
    "ASGInstanceRootVolumeSize": 8,
    "ASGInstanceRootVolumeType": "standard",
    "ASGInstanceType": "m3.medium",
    "ASGLoadBalancerNames": ["elb1"],
    "ASGMaxInstances": 1,
    "ASGMinInstances": 1,
    "ASGHealthCheckGracePeriod": 600,
    "ASGHealthCheckType":"EC2",
    "ASGScaleDownMetricName": "CPUUtilization",
    "ASGScaleDownPolicyCooldown": 300,
    "ASGScaleDownPolicyEvaluationPeriods": 4,
    "ASGScaleDownPolicyPeriod": 60,
    "ASGScaleDownPolicyScalingAdjustment": -1,
    "ASGScaleDownPolicyStatistic": "Average",
    "ASGScaleDownPolicyThreshold": 35,
    "ASGScaleUpMetricName": "CPUUtilization",
    "ASGScaleUpPolicyCooldown": 60,
    "ASGScaleUpPolicyEvaluationPeriods": 2,
    "ASGScaleUpPolicyPeriod": 60,
    "ASGScaleUpPolicyScalingAdjustment": 2,
    "ASGScaleUpPolicyStatistic": "Average",
    "ASGScaleUpPolicyThreshold": 75,
    "ASGSubnetIds": ["subnet-a0b1c2d3", "subnet-e4f5g6h7"],
    "ASGUserData": "#!/bin/bash\npwd\nls -ltrh\necho \"Hello, World\""
  }
}

```
