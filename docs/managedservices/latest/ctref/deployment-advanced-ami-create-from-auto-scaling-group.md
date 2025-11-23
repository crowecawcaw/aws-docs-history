# AMI | Create from Auto Scaling Group

Create an Amazon Machine Image (AMI) from an EC2 Instance in an Auto Scaling group.

**Full classification:** Deployment | Advanced stack components | AMI | Create from Auto Scaling group

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-3e3prksxmdhw8 |
| Current version             | 1.0              |
| Expected execution duration | 360 minutes      |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Create AMIs from Auto Scaling groups (ASGs)

The following shows this change type in the AMS console.

![Console interface showing "Create AMI From Amazon EC2 Auto Scaling Group" with description and version details.](images/guiAmiCreateFromAsgCT.png)
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
quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws --profile saml --region us-east-1 amscm create-rfc --change-type-id "ct-3e3prksxmdhw8" --change-type-version "2.0" --title "`AMI-Create-IC`" --execution-parameters "{\"AMIName\":\"`MyAmi`\",\"VpcId\":\"`VPC_ID`\",\"EC2InstanceId\":\"`INSTANCE_ID`\"}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a file;
   this example names it CreateAmiFromAsgParams.json:

```
aws amscm create-rfc --change-type-id "ct-3e3prksxmdhw8" --change-type-version "1.0" --title "`Create AMI from an Auto Scaling group`" --execution-parameters "{\"DocumentName\": \"AWSManagedServices-CreateAmiInAutoScalingGroup\",\"Region\": \"`us-east-1`\",\"Parameters\": {\"AutoScalingGroupName\": [\"`stack-ab0123cdef-ASG-1ABC2345`\"],\"Sysprep\": [\"`False`\"],\"StopInstance\": [\"`False`\"]}}"
```

2. Modify and save the execution parameters CreateAmiFromAsgParams.json file. For example, you can replace the contents with something like this:

```
{
  "DocumentName": "AWSManagedServices-CreateAmiInAutoScalingGroup",
  "Region": "`us-east-1`",
  "Parameters": {
    "AutoScalingGroupName": [
      "`stack-ab0123cdef-ASG-1ABC2345`"
    ],
    "Sysprep": [
      "`False`"
    ],
    "StopInstance": [
      "`False`"
    ]
  }
}
```

3. Output the RFC template JSON file to a file in your current folder; this example
   names it CreateAmiFromAsgRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > CreateAmiFromAsgRfc.json
```

4. Modify and save the CreateAmiFromAsgRfc.json file. For example, you can replace the contents with something like this:

```
{
  "ChangeTypeVersion": "1.0",
  "ChangeTypeId": "ct-3e3prksxmdhw8",
  "Title": "`Create AMI from an Auto Scaling group`"
}
```

5. Create the RFC, specifying the CreateAmiFromAsgRfc file and the CreateAmiFromAsgParams file:

```
aws amscm create-rfc --cli-input-json file://CreateAmiFromAsgRfc.json  --execution-parameters file://CreateAmiFromAsgParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

###### Note

After you have created a custom AMI, you can submit a service request to
AMS to have your existing EC2 Auto Scaling group use the new AMI. For information
about creating a service request, see [Service Request Examples](../userguide/serv-req-mgmt-examples.md "../userguide/serv-req-mgmt-examples.md").

For information about failed AMI Create RFCs, see
[RFC failure troubleshooting](../userguide/rfc-failures.md "../userguide/rfc-failures.md").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-3e3prksxmdhw8](schemas.md#ct-3e3prksxmdhw8-schema-section "schemas.md#ct-3e3prksxmdhw8-schema-section").

## Example: Required Parameters

```
{
  "DocumentName" : "AWSManagedServices-CreateAmiInAutoScalingGroup",
  "Region" : "us-east-1",
  "Parameters" : {
    "AutoScalingGroupName" : [
      "TestASG"
    ],
    "Sysprep" : [
      "False"
    ],
    "StopInstance" : [
      "False"
    ]
  }
}

```

## Example: All Parameters

```
{
  "DocumentName" : "AWSManagedServices-CreateAmiInAutoScalingGroup",
  "Region" : "us-east-1",
  "Parameters" : {
    "AutoScalingGroupName" : [
      "TestASG"
    ],
    "Sysprep" : [
      "False"
    ],
    "StopInstance" : [
      "False"
    ]
  }
}

```
