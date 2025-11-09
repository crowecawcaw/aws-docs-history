# Target Group | Detach Instances

Detach instances or private IPv4 addresses from a target group. If the instances or private IP addresses exist but aren't registered with a target group, then the RFC execution ends in a success state without action on the target group.

**Full classification:** Management | Advanced stack components | Target group | Detach instances

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-37bq2l9c8fzxv |
| Current version             | 2.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Detach instances or private IPv4 from a target group

Screenshot of this change type in the AMS console:

![Console interface for detaching instances or private IPv4 addresses from a target group.](images/guiTarGroupDetachInstanceCT.png)
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

Issue the create RFC command with execution parameters provided inline
(escape quotation marks when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

**Detach instances from target group:**

```
aws amscm create-rfc \
--change-type-id "ct-37bq2l9c8fzxv" \
--change-type-version "2.0"
--title "DetachInstancesFromTargetGroup" \
--execution-parameters "{\"DocumentName\":\"AWSManagedServices-DetachInstancesFromTargetGroup\",\"Region\":\"`us-east-1`\",\"Parameters\":{\"InstancesIds\":[\"`i-000000000000`\",\"`i-111111111111`\"],\"InstancesPort\":[\"`80`\"],\"TargetGroupArn\":[\"`arn:aws:elasticloadbalancing:us-east-1:00000000000:targetgroup/test-target-group/0000000000`\"]}}"
```

**Detach IP address from target group:**

```
aws amscm create-rfc \
--change-type-id "ct-37bq2l9c8fzxv" \
--change-type-version "2.0"
--title "DetachInstancesFromTargetGroup" \
--execution-parameters "{\"DocumentName\":\"AWSManagedServices-DetachInstancesFromTargetGroup\",\"Region\":\"`us-east-1`\",\"Parameters\":{\"IPAddresses\":[\"`172.31.0.11`\",\"`172.31.0.12`\"],\"InstancesPort\":[\"`80`\"],\"TargetGroupArn\":[\"`arn:aws:elasticloadbalancing:us-east-1:00000000000:targetgroup/test-target-group/0000000000`\"]}}"
```

TEMPLATE CREATE:

1. Output the execution parameters JSON schema for this change type to a JSON file; this example names it
   TgDetachInstanceParams.json.

```
aws amscm get-change-type-version --change-type-id "ct-37bq2l9c8fzxv" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > TgDetachInstanceParams.json
```

2. Modify and save the TgDetachInstanceParams file. For example, you can replace the contents with something like this:

**Parameter file with instance ids as an example:**

```
{
  "DocumentName": "AWSManagedServices-DetachInstancesFromTargetGroup",
  "Region": "us-east-1",
  "Parameters": {
      "InstancesIds": [
          "i-000000000000",
          "i-111111111111"
      ],
      "InstancesPort": [
          "80"
      ],
      "TargetGroupArn": [
          "arn:aws:elasticloadbalancing:us-east-1:00000000000:targetgroup/test-target-group/0000000000"
      ]
  }
}
```

**Parameter file with IP address as an example:**

```
{
  "DocumentName": "AWSManagedServices-DetachInstancesFromTargetGroup",
  "Region": "us-east-1",
  "Parameters": {
      "IPAddresses": [
          "172.31.0.11",
          "172.31.0.12"
      ],
      "InstancesPort": [
          "80"
      ],
      "TargetGroupArn": [
          "arn:aws:elasticloadbalancing:us-east-1:00000000000:targetgroup/test-target-group/0000000000"
      ]
  }
}
```

3. Output the RFC template to a file in your current folder named TgDetachInstanceRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > TgDetachInstanceRfc.json
```

4. Modify and save the TgDetachInstanceRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`2.0`",
"ChangeTypeId":         "ct-37bq2l9c8fzxv",
"Title":                "`Target-Group-Detach-Instance-RFC`"
}
```

5. Create the RFC, specifying the TgDetachInstanceRfc file and the TgDetachInstanceParams file:

```
aws amscm create-rfc --cli-input-json file://TgDetachInstanceRfc.json --execution-parameters file://TgDetachInstanceParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

For information about target groups, see
[ELB Target Groups](../../../elasticloadbalancing/latest/network/load-balancer-target-groups.md "../../../elasticloadbalancing/latest/network/load-balancer-target-groups.md").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-37bq2l9c8fzxv](schemas.md#ct-37bq2l9c8fzxv-schema-section "schemas.md#ct-37bq2l9c8fzxv-schema-section").

## Example: Required Parameters

```
 {
  "DocumentName": "AWSManagedServices-DetachInstancesFromTargetGroup",
  "Region": "us-east-1",
  "Parameters": {
    "InstancesPort": ["80"],
    "TargetGroupArn": ["arn:aws:elasticloadbalancing:eu-west-1:000000000000:targetgroup/target-group-name/000000000000"]
  }
}

```

## Example: All Parameters

```
 {
  "DocumentName": "AWSManagedServices-DetachInstancesFromTargetGroup",
  "Region": "us-east-1",
  "Parameters": {
    "InstancesIds": ["i-0000000000"],
    "InstancesPort": ["80"],
    "IPAddresses": ["10.0.0.5"],
    "TargetGroupArn": ["arn:aws:elasticloadbalancing:eu-west-1:000000000000:targetgroup/target-group-name/000000000000"]
  }
}

```
