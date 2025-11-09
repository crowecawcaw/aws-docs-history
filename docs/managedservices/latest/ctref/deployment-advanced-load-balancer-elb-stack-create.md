# Load Balancer (ELB) Stack | Create

Use to create an Amazon ELB Classic Load Balancer. Use alternate change types to create an Application Load Balancer (ct-111r1yayblnw4) or Network Load Balancer (ct-2qldv4h9osmau).

**Full classification:** Deployment | Advanced stack components | Load balancer (ELB) stack | Create

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-12amsdz909cfh |
| Current version             | 3.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Create ELB load balancer

Screenshot of this change type in the AMS console:

![Change type details for creating an Amazon ELB Classic Load Balancer stack.](images/guiElbCreateCT.png)
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
aws amscm create-rfc --change-type-id ct-12amsdz909cfh --change-type-version 3.0 --title "`my-elb`" --execution-parameters '{"Description":"`My ELB`","VpcId":"`VPC_ID`","StackTemplateId":"stm-sdhopv30000000000","Name":"`myElb`","TimeoutInMinutes":60,"Parameters":{"ELBSubnetIds":["`SUBNET_ID`","`SUBNET_ID`"],"ELBLoadBalancerPort":"`80`","ELBLoadBalancerProtocol":"`HTTP`","ELBInstancePort":"`80`"}}'
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a JSON file; this example names it CreateElbParams.json:

```
aws amscm get-change-type-version --change-type-id "ct-12amsdz909cfh" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateElbParams.json
```

2. Modify and save the CreateElbParams file. The values given in the example reflect a deployment of a Public ELB, with the health check thresholds relaxed and the ELBScheme set to `true` (for a public ELB).
   Note that the `Name` you set here is not the actual ELB name, you can find that name in the console as the ELB instance name. Not all optional parameters are shown in the example.

```
{
"Description":      "`ELB-Create`",
"VpcId":            "`VPC_ID`",
"StackTemplateId":  "stm-sdhopv00000000000",
"Name":             "`My-ELB`",

"Parameters":   {
    "ELBSubnetIds":  ["`PUBLIC_AZ1`", "`PUBLIC_AZ2`"],
    "ELBHealthCheckHealthyThreshold":   `2`,
    "ELBHealthCheckInterval":           `30`,
    "ELBHealthCheckTarget":             "`HTTP:80/status`",
    "ELBHealthCheckTimeout":            10,
    "ELBHealthCheckUnhealthyThreshold": 3,
    "ELBScheme":                        true
    }
}
```

3. Output the RFC template to a file in your current folder; this example names it CreateElbRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > CreateElbRfc.json
```

4. Modify and save the CreateElbRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`3.0`",
"ChangeTypeId":         "ct-12amsdz909cfh",
"Title":                "`ELB-Create-RFC`"
}
```

5. Create the RFC, specifying the CreateElbRfc file and the CreateElbParams file:

```
aws amscm create-rfc --cli-input-json file://CreateElbRfc.json --execution-parameters file://CreateElbParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start. 6. To view the load balancer, look in the execution output: Use the `stack_id` to view the ELB in the Cloud Formation console or to create a Delete Stack RFC,
use the ELBCName value to programmatically access the ELB.

You might need to submit a Management | Other | Other | Update change type to open ports and associate security groups, see
[Other | Other requests](ex-other-other.md "ex-other-other.md").
To learn more about AWS Classic Load Balancers, see
[What Is a Classic Load Balancer?](../../../elasticloadbalancing/latest/classic/introduction.md "../../../elasticloadbalancing/latest/classic/introduction.md")

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-12amsdz909cfh](schemas.md#ct-12amsdz909cfh-schema-section "schemas.md#ct-12amsdz909cfh-schema-section").

## Example: Required Parameters

```
{
  "Description": "This is a test description",
  "VpcId": "vpc-1234567890abcdef0",
  "StackTemplateId": "stm-sdhopv30000000000",
  "Name": "Test Stack",
  "TimeoutInMinutes": 60,
  "Parameters": {
    "ELBSubnetIds": ["subnet-1234567890abcdef0", "subnet-1234567890abcdef1"],
    "ELBInstancePort": "80",
    "ELBInstanceProtocol": "HTTP",
    "ELBLoadBalancerPort": "80",
    "ELBLoadBalancerProtocol": "HTTP"
  }
}

```

## Example: All Parameters

```
{
  "Description": "This is a test description",
  "VpcId": "vpc-12345678",
  "StackTemplateId": "stm-sdhopv30000000000",
  "Name": "Test Stack",
  "Tags": [
    {
      "Key": "foo",
      "Value": "bar"
    },
    {
      "Key": "testkey",
      "Value": "testvalue"
    }
  ],
  "TimeoutInMinutes": 60,
  "Parameters": {
    "ELBSubnetIds": ["subnet-a0b1c2d3", "subnet-a0b2c9d8"],
    "ELBHealthCheckHealthyThreshold": 2,
    "ELBHealthCheckInterval": 10,
    "ELBHealthCheckTarget": "HTTP:80/index.html",
    "ELBHealthCheckTimeout": 10,
    "ELBHealthCheckUnhealthyThreshold": 3,
    "ELBIdleTimeout": 30,
    "ELBInstancePort": "80",
    "ELBInstanceProtocol": "HTTPS",
    "ELBCookieExpirationPeriod": "60",
    "ELBCookieStickinessPolicyName": "MyPolicy",
    "ELBLoadBalancerName": "MyLoadBalancer",
    "ELBLoadBalancerPort": "443",
    "ELBLoadBalancerProtocol": "HTTP",
    "ELBSSLCertificateId": "arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012",
    "ELBScheme": false,
    "ELBCrossZone": true,
    "ELBBackendInstances": ["i-12345678", "i-01234567"],
    "ELBInstancePort2": "80",
    "ELBInstanceProtocol2": "HTTPS",
    "ELBCookieExpirationPeriod2": "60",
    "ELBCookieStickinessPolicyName2": "MyPolicy2",
    "ELBLoadBalancerPort2": "445",
    "ELBLoadBalancerProtocol2": "HTTP",
    "ELBSSLCertificateId2": "arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012"
  }
}

```
