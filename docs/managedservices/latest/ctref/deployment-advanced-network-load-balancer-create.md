# Network Load Balancer | Create

Use to create a Network Load Balancer.

**Full classification:** Deployment | Advanced stack components | Network Load Balancer | Create

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-2qldv4h9osmau |
| Current version             | 1.0              |
| Expected execution duration | 360 minutes      |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Create NLB load balancer

Screenshot of this change type in the AMS console:

![Network Load Balancer creation details showing change type, description, ID, version, and execution mode.](images/guiNlbCreateCT.png)
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

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit
the returned RFC ID. For example, you can replace the contents with something like this:

```
aws --profile saml --region us-east-1 amscm create-rfc  --change-type-id "ct-2qldv4h9osmau" --change-type-version "1.0" --title "`Test-NLB-QC`" --execution-parameters "{\"Description\":\"`QCNLB`\", \"VpcId\":\"`VPC_ID`\", \"StackTemplateId\":\"stm-l70qr9itukvqssg8d\", \"Name\":\"`QCNLB`\", \"TimeoutInMinutes\":60, \"Parameters\":{\"SubnetIds\":[\"`SUBNET_ID`\",\"`SUBNET_ID`\"]}}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a JSON file; this example names it CreateNlbParams.json:

```
aws amscm get-change-type-version --change-type-id "ct-2qldv4h9osmau" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateNlbParams.json
```

2. Modify and save the CreateNlbParams file. The values given in the example reflect a deployment
   of a public Network Load Balancer, with the health check thresholds relaxed and the
   `Public` parameters set to true (for a public NLB). Note that the
   `Name` you set here is not the actual NLB name, you can find that name in
   the console as the NLB instance name.

```
{
"Description":      "`NLB-Create`",
"VpcId":            "`VPC_ID`",
"StackTemplateId":  "stm-l70qr9itukvqssg8d",
"Name":             "`My-NLB`",

"Parameters":   {
    "SubnetIds":  ["`PUBLIC_AZ1`", "`PUBLIC_AZ2`"],
    "HealthCheckHealthyThreshold":   `2`,
    "HealthCheckInterval":           `30`,
    "HealthCheckTargetPath":         `traffic-port`",
    "DeregistrationDelayTimeout":                 10,
    "Public":                        true
    }
}
```

3. Output the RFC template to a file in your current folder; this example names it CreateNlbRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > CreateNlbRfc.json
```

4. Modify and save the CreateNlbRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-2qldv4h9osmau",
"Title":                "`NLB-Create-RFC`"
}
```

5. Create the RFC, specifying the CreateNlbRfc file and the CreateNlbParams file:

```
aws amscm create-rfc --cli-input-json file://CreateNlbRfc.json --execution-parameters file://CreateNlbParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start. 6. To view the load balancer, look in the execution output: Use the stack_id to view the NLB in
the CloudFormation console or to create a Delete Stack RFC, and use the NLB CName value
to programmatically access the NLB.

###### Note

You can specify up to four Target IDs, Ports, and Availability Zones.

To learn more about AWS Network Load Balancers, see
[Create a Network Load Balancer](../../../elasticloadbalancing/latest/network/create-network-load-balancer.md "../../../elasticloadbalancing/latest/network/create-network-load-balancer.md").

To create a network load balancer listener, see
[Target Group | Create (For NLB)](deployment-advanced-target-group-create-for-nlb.md "deployment-advanced-target-group-create-for-nlb.md").

To create a network load balancer target group, see
[Create NLB target group](deployment-advanced-target-group-create-for-nlb.md#ex-tar-group-nlb-create-col "deployment-advanced-target-group-create-for-nlb.md#ex-tar-group-nlb-create-col").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-2qldv4h9osmau](schemas.md#ct-2qldv4h9osmau-schema-section "schemas.md#ct-2qldv4h9osmau-schema-section").

## Example: Required Parameters

```
Example not available.
```

## Example: All Parameters

```
{
  "Description": "This is a test description",
  "Name": "Test Stack",
  "Parameters": {
    "CrossZoneEnabled": "false",
    "DeregistrationDelayTimeoutSeconds": "300",
    "HealthCheckHealthyThreshold": "3",
    "HealthCheckIntervalSeconds": "30",
    "HealthCheckTargetPath": "/",
    "HealthCheckTargetPort": "80",
    "HealthCheckTargetProtocol": "TCP",
    "InstancePort": "80",
    "LoadBalancerName": "my-load-balancer",
    "LoadBalancerPort": "80",
    "ProxyProtocolV2": "false",
    "Public": "false",
    "SubnetIds": ["subnet-01234567890abcdef", "subnet-01234567891abcdef"],
    "Target1AvailabilityZone": "us-east-1a",
    "Target1ID": "i-01234567890abcdef",
    "Target1Port": "80",
    "Target2AvailabilityZone":  "us-east-1a",
    "Target2ID": "i-11234567890abcdef",
    "Target2Port": "80",
    "Target3AvailabilityZone": "us-east-1a",
    "Target3ID": "i-21234567890abcdef",
    "Target3Port": "80",
    "Target4AvailabilityZone": "us-east-1a",
    "Target4ID": "i-31234567890abcdef",
    "Target4Port": "80",
    "TargetType": "instance"
  },
  "StackTemplateId": "stm-l70qr9itukvqssg8d",
  "TimeoutInMinutes": 60,
  "VpcId": "vpc-01234567890abcdef"
}

```
