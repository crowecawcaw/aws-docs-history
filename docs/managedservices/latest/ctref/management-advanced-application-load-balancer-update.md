# Application Load Balancer | Update

Update the properties of an existing AWS Application Load Balancer (ALB) that was created by version 3.0 CT: ct-111r1yayblnw4.

**Full classification:** Management | Advanced stack components | Application Load Balancer | Update

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-1a1zzgi2nb83d |
| Current version             | 3.0              |
| Expected execution duration | 360 minutes      |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Update application load balancer (ALB)

The following shows this change type in the AMS console.

![Update Application Load Balancer interface showing description, ID, and version details.](images/guiAlbUpdateCT.png)
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
aws amscm create-rfc --title `Test-Update-ALB` --change-type-id ct-1a1zzgi2nb83d --change-type-version 3.0 --execution-parameters '{"Description":"`Updating Test ALB`","VpcId":"`VPC_ID`","StackTemplateId":"stm-sd7uv500000000000","Name":"`Test-Application-LoadBalancer`","TimeoutInMinutes":`360`,"Parameters":{"TargetGroupHealthCheckPath": "`/myAppHealth`"}}'
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a JSON file. For example, you can replace the contents with something like this:

```
aws amscm get-change-type-version --change-type-id "ct-111r1yayblnw4" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > UpdateAlbParams.json
```

2. Modify and save the UpdateAlbParams file. For example:

```
{
"Description":      "`ALB-Update`",
"VpcId":            "`VPC_ID`",
"Name":             "`My-ALB`",
"StackTemplateId":  "stm-sd7uv500000000000",
"TimeoutInMinutes" : `360`,
"Parameters": {
    "LoadBalancerSecurityGroups": [
      "`sg-1234567890abcdef0`"
    ],
    "LoadBalancerSubnetIds": [
      "`subnet-1234567890abcdef0`",
      "`subnet-1234567890abcdef1`"
    ],
    "LoadBalancerDeletionProtection": "`false`",
    "LoadBalancerIdleTimeout": "`60`",
    "Listener1Port": "`443`",
    "Listener1Protocol": "`HTTPS`",
    "Listener1SSLCertificateArn": "`arn:aws:acm:ap-southeast-2:012345678912:certificate/e23c3545-e92d-4542-83b8-63483505b5a5`",
    "Listener1SSLPolicy": "`ELBSecurityPolicy-TLS-1-2-Ext-2018-06`",
    "Listener2Port": "`8080`",
    "Listener2Protocol": "`HTTP`",
    "TargetGroupHealthCheckInterval": "`10`",
    "TargetGroupHealthCheckPath": "`/thing/index.html`",
    "TargetGroupHealthCheckPort": "`8080`",
    "TargetGroupHealthCheckProtocol": "`HTTP`",
    "TargetGroupHealthCheckTimeout": "`10`",
    "TargetGroupHealthyThreshold": "`2`",
    "TargetGroupUnhealthyThreshold": "`10`",
    "TargetGroupValidHTTPCode": "`200`",
    "TargetGroupDeregistrationDelayTimeout": "`300`",
    "TargetGroupSlowStartDuration": "`30`",
    "TargetGroupCookieExpirationPeriod": "`20`"
  }
}
```

3. Output the RFC template to a file in your current folder. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --generate-cli-skeleton > UpdateAlbRfc.json
```

4. Modify and save the UpdateAlbRfc.json file. For example:

```
{
"ChangeTypeVersion":    "`3.0`",
"ChangeTypeId":         "ct-111r1yayblnw4",
"Title":                "`ALB-Update-RFC`"
}
```

5. Create the RFC, specifying the UpdateAlbRfc file and the UpdateAlbParams file:

```
aws amscm create-rfc --cli-input-json file://UpdateAlbRfc.json --execution-parameters file://UpdateAlbParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

###### Note

This change type is version 3.0, and can be used with the version 3.0 of the Create ALB change type (ct-111r1yayblnw4).

To learn more about AWS Application Load Balancers, see
[What Is an Application Load Balancer?](../../../elasticloadbalancing/latest/application/introduction.md "../../../elasticloadbalancing/latest/application/introduction.md")

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-1a1zzgi2nb83d](schemas.md#ct-1a1zzgi2nb83d-schema-section "schemas.md#ct-1a1zzgi2nb83d-schema-section").

## Example: Required Parameters

```
{
  "VpcId": "vpc-1234567890abcdef0",
  "StackId": "stack-1234567890abcdef0",
  "Parameters": {}
}

```

## Example: All Parameters

```
{
  "VpcId": "vpc-12345678",
  "StackId": "stack-1234567890abcdef0",
  "Parameters": {
    "LoadBalancerSecurityGroups": ["sg-12345678"],
    "LoadBalancerSubnetIds": ["subnet-12345678", "subnet-12345688"],
    "LoadBalancerDeletionProtection": "false",
    "LoadBalancerIdleTimeout": "60",
    "Listener1Port": "443",
    "Listener1Protocol": "HTTPS",
    "Listener1SSLCertificateArn": "arn:aws:acm:ap-southeast-2:012345678912:certificate/e23c3545-e92d-4542-83b8-63483505b5a5",
    "Listener1SSLPolicy": "ELBSecurityPolicy-TLS-1-2-Ext-2018-06",
    "Listener2Port": "8080",
    "Listener2Protocol": "HTTP",
    "TargetGroupHealthCheckInterval": "10",
    "TargetGroupHealthCheckPath": "/thing/index.html",
    "TargetGroupHealthCheckPort": "8080",
    "TargetGroupHealthCheckProtocol": "HTTP",
    "TargetGroupHealthCheckTimeout": "10",
    "TargetGroupHealthyThreshold": "2",
    "TargetGroupUnhealthyThreshold": "10",
    "TargetGroupValidHTTPCode": "200",
    "TargetGroupDeregistrationDelayTimeout": "300",
    "TargetGroupSlowStartDuration": "30",
    "TargetGroupCookieExpirationPeriod": "20"
  }
}

```
