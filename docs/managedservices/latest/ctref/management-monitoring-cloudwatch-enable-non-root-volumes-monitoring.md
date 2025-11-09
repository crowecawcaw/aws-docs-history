# CloudWatch | Enable Non-Root Volumes Monitoring

Enable monitoring on non-root volumes of an EC2 instance.

**Full classification:** Management | Monitoring and notification | CloudWatch | Enable Non-Root Volumes Monitoring

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-0erkoad6uyvvg |
| Current version             | 1.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Enable CloudWatch non-root volumes monitoring

The following shows this change type in the AMS console.

![Change type for enabling non-root volumes monitoring on EC2 instances with ID and version.](images/guiCwEnableNonRootVolMonCT.png)
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
aws amscm create-rfc --change-type-id "ct-0erkoad6uyvvg" --change-type-version "1.0" --title "`Enable Non-Root Volumes Monitoring`" --execution-parameters "{\"DocumentName\":\"AWSManagedServices-DeployNonRootVolumeMonitoring\",\"Region\":\"`us-east-1`\",\"Parameters\":{\"InstanceId\":[\"`i-1234567890abcdef0`\"]}}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a file in your current folder; this example names it CwNonRootVolumeMonitoringParams.json:

```
aws amscm get-change-type-version --change-type-id "ct-0erkoad6uyvvg" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CwNonRootVolumeMonitoringParams.json
```

2. Modify and save the CwNonRootVolumeMonitoringParams.json file. For example, you can replace the contents with something like this:

```
{
    "DocumentName": "AWSManagedServices-DeployNonRootVolumeMonitoring",
    "Region": "`us-east-1`",
    "Parameters": {
        "InstanceId": [
            "`i-1234567890abcdef0`"
        ]
    }
}
```

3. Output the JSON template for CreateRfc to a file in your current folder; this example names it CwNonRootVolumeMonitoringRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > CwNonRootVolumeMonitoringRfc.json
```

4. Modify and save the CwNonRootVolumeMonitoringRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-0erkoad6uyvvg",
"Title":                "`CW-NON-ROOT-VOL-MONITORING-RFC`"
}
```

5. Create the RFC, specifying the CwNonRootVolumeMonitoringRfc file and the execution parameters file:

```
aws amscm create-rfc --cli-input-json file://CwNonRootVolumeMonitoringRfc.json --execution-parameters file://CwNonRootVolumeMonitoringParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.
To learn more about CloudWatch, see
[Enable or disable detailed monitoring for your instances](../../../AWSEC2/latest/UserGuide/using-cloudwatch-new.md "../../../AWSEC2/latest/UserGuide/using-cloudwatch-new.md").

The EC2 instance alart `Non-root volume usage` is **DISABLED** by default. If you require alert generation based on this alarm, then you must enable it using this RFC.

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-0erkoad6uyvvg](schemas.md#ct-0erkoad6uyvvg-schema-section "schemas.md#ct-0erkoad6uyvvg-schema-section").

## Example: Required Parameters

```
{
  "DocumentName": "AWSManagedServices-DeployNonRootVolumeMonitoring",
  "Region": "us-east-1",
  "Parameters": {
    "InstanceId": [
      "i-1234567890abcdef0"
    ]
  }
}
```

## Example: All Parameters

```
{
  "DocumentName": "AWSManagedServices-DeployNonRootVolumeMonitoring",
  "Region": "us-east-1",
  "Parameters": {
    "InstanceId": [
      "i-1234567890abcdef0"
    ]
  }
}
```
