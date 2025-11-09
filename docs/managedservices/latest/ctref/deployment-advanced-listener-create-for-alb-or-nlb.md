# Listener | Create (For ALB or NLB)

Create a listener for an Application Load Balancer (ALB) or Network Load Balancer (NLB). A listener is a process that checks for connection requests, the rules that you define for a listener determine how the load balancer routes requests to its registered targets.

**Full classification:** Deployment | Advanced stack components | Listener | Create (for ALB or NLB)

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-14yjom3kvpinu |
| Current version             | 2.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Create listener

Screenshot of this change type in the AMS console:

![Form to create a listener for Application Load Balancer or Network Load Balancer with execution details.](images/guiListenerAlbNlbCreateCT.png)
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
aws --profile saml --region us-east-1 amscm create-rfc --change-type-id "ct-14yjom3kvpinu" --change-type-version "2.0" --title "`TITLE`" --execution-parameters "{\"Description\":\"`DESCRIPTION`\", \"VpcId\":\"`VPC_ID`\", \"StackTemplateId\": \"stm-u5n0r6aacdvdwthhm\", \"Name\":\"`NAME`\", \"TimeoutInMinutes\":60, \"Parameters\": {\"LoadBalancerArn\":\"`LB-ARN`",\"DefaultActionTargetGroupArn\":\"`TARGET-GROUP-ARN`",\"Port\":\"`80`\",\"Protocol\":\"`HTTP`\"}}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a JSON file; this example names it CreateListenerParams.json:

```
aws amscm get-change-type-version --change-type-id "ct-14yjom3kvpinu" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateListenerParams.json
```

2. Modify and save the CreateListenerParams file. For example, you can replace the contents with something like this:

```
{
"Description":      "`Listener-Create`",
"VpcId":            "`VPC_ID`",
"StackTemplateId":  "stm-u5n0r6aacdvdwthhm",
"Name":             "`My-Listener`",

"Parameters":   {
    "LoadBalancerArn":               `ARN`,
    "DefaultActionTargetGroupArn":   `ARN`,
    "Port":                          `PORT`,
    "Protocol":                     `Protocol`"
    }
}
```

3. Output the RFC template to a file in your current folder; this example names it CreateListenerRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > CreateListenerRfc.json
```

4. Modify and save the CreateListenerRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`2.0`",
"ChangeTypeId":         "ct-14yjom3kvpinu",
"Title":                "`Listener-Create-RFC`"
}
```

5. Create the RFC, specifying the CreateListenerRfc file and the CreateListenerParams file:

```
aws amscm create-rfc --cli-input-json file://CreateListenerRfc.json --execution-parameters file://CreateListenerParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

Next Steps: Submit a Management | Other | Other | Update change type to open ports and associate security groups, see
[Other | Other requests](ex-other-other.md "ex-other-other.md").

###### Note

You can specify up to four Target IDs, Ports, and Availability Zones.

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-14yjom3kvpinu](schemas.md#ct-14yjom3kvpinu-schema-section "schemas.md#ct-14yjom3kvpinu-schema-section").

## Example: Required Parameters

```
{
  "Description": "This is a test description",
  "Name": "Test Stack",
  "Parameters": {
    "DefaultActionTargetGroupArn": "arn:aws:elasticloadbalancing:eu-west-1:123456789012:targetgroup/target-group-name/123456789012",
    "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-app-load-balancer/abcdefghij",
    "Port": "80",
    "Protocol": "HTTP"
  },
  "StackTemplateId": "stm-u5n0r6aacdvdwthhm",
  "TimeoutInMinutes": 60,
  "VpcId": "vpc-01234567890abcdef"
}

```

## Example: All Parameters

```
{
  "Description": "This is a test description",
  "Name": "Test Stack",
  "Parameters": {
    "CertificateArn": "arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012",
    "DefaultActionTargetGroupArn": "arn:aws:elasticloadbalancing:eu-west-1:123456789012:targetgroup/target-group-name/123456789012",
    "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-app-load-balancer/abcdefghij",
    "Port": "443",
    "Protocol": "HTTP",
    "ALBSslPolicy": "ELBSecurityPolicy-2016-08",
    "AlpnPolicy": "HTTP2Only"
  },
  "StackTemplateId": "stm-u5n0r6aacdvdwthhm",
  "TimeoutInMinutes": 60,
  "VpcId": "vpc-01234567890abcdef"
}

```
