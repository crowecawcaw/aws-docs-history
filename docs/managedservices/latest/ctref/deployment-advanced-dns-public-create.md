# DNS (Public) | Create

Create a new Route 53 DNS resource record set and a new public hosted zone for a VPC, and configure traffic routing.

**Full classification:** Deployment | Advanced stack components | DNS (public) | Create

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-0vzsr2nyraedl |
| Current version             | 2.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Create public DNS Route 53

Screenshot of this change type in the AMS console:

![Change type details for creating a public DNS record, including description and execution mode.](images/guiDnsPubCreateCT.png)
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
aws amscm create-rfc \
--change-type-id "ct-0vzsr2nyraedl" \
--change-type-version "2.0" --title "`Creating New Public Hosted Zone`" \
--execution-parameters "{\"DocumentName\":\"AWSManagedServices-CreateAddRoute53Resources\",\"Region\":\"`us-east-1`\",\"Parameters\":{\"DomainName\":\"`mydomain.com`\",\"DomainType\":\"public\",\"RecordSet\":[\"[{\\\"Name\\\":\\\"`test1.mydomain.com`\\\",\\\"Type\\\":\\\"`A`\\\",\\\"TTL\\\":`600`,\\\"ResourceRecords\\\":[\\\"`10.1.1.1`\\\",\\\"`10.1.2.2`\\\"]}]}\"]}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters for this change type to a JSON file named CreateDnsPublicParams.json.

```
aws amscm get-change-type-version --change-type-id "ct-0vzsr2nyraedl" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateDnsPublicParams.json
```

2. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

```
{
  "DocumentName": "AWSManagedServices-CreateAddRoute53Resources",
  "Region": "`ap-southeast-2`",
  "Parameters": {
    "DomainName": "`domain.com`",
    "DomainType": "public",
    "RecordSet": [
      "{\"RecordSet\":[{\"Name\":\"`test1.domain.com`\",\"Type\":\"`A`\",\"TTL\":`600`,\"ResourceRecords\":[\"`10.1.1.1`\",\"`10.1.2.2`\"]},{\"Name\":\"`test3.domain.com`\",\"Type\":\"`CNAME`\",\"TTL\":`600`,\"ResourceRecords\":[\"`www.google.com`\"]},{\"Name\":\"`test4.domain.com`\",\"Type\":\"`A`\",\"AliasTarget\":{\"DNSName\":\"`d1i3674zujyzy1.cloudfront.net`\",\"EvaluateTargetHealth\":`true`,\"HostedZoneId\":\"`Z2FDTNDATAQYW2`\"}},{\"Name\":\"`weighted.domain.com`\",\"Weight\":`200`,\"SetIdentifier\":\"`Example-Set-Identifier-1`\",\"Type\":\"`A`\",\"AliasTarget\":{\"DNSName\":\"`d1i3674zujyzy1.cloudfront.net`\",\"EvaluateTargetHealth\":`true`,\"HostedZoneId\":\"`Z2FDTNDATAQYW2`\"}},{\"Name\":\"`geolocationexample.domain.com`\",\"SetIdentifier\":\"`Example-GeoLocation-Identifier-1`\",\"GeoLocation\":{\"CountryCode\":\"`US`\",\"SubdivisionCode\":\"`WA`\"},\"Type\":\"`A`\",\"AliasTarget\":{\"DNSName\":\"`d1i3674zujyzy1.cloudfront.net`\",\"EvaluateTargetHealth\":`true`,\"HostedZoneId\":\"`Z2FDTNDATAQYW2`\"}},{\"Name\":\"`examplelatency.domain.com`\",\"SetIdentifier\":\"`Example-Latency-Identifier-1`\",\"Region\":\"`ap-southeast-2`\",\"Type\":\"`A`\",\"TTL\":`600`,\"ResourceRecords\":[\"`10.1.1.1`\",\"`10.1.2.2`\"]},{\"Name\":\"`examplemultivalue.domain.com`\",\"SetIdentifier\":\"`Example-MultiValue-Identifier-1`\",\"MultiValueAnswer\":`true`,\"Type\":\"`A`\",\"TTL\":`600`,\"ResourceRecords\":[\"`10.1.1.1`\"]}]}"
    ]
  }
}
```

3. Output the JSON template to a file in your current folder; this example names it CreateDnsPublicRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > CreateDnsPublicRfc.json
```

4. Modify and save the CreateDnsPublicRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`2.0`",
"ChangeTypeId":         "ct-0vzsr2nyraedl",
"Title":                "`DNS-Public-Create-RFC`"
}
```

5. Create the RFC, specifying the execution parameters file and the CreateDnsPublicRfc file:

```
aws amscm create-rfc --cli-input-json file://CreateDnsPublicRfc.json --execution-parameters file://CreateDnsPublicParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

###### Note

To create a private Route 53 DNS stack, see [Create private DNS
Route 53](ex-dns-private-create-stack-col.md "ex-dns-private-create-stack-col.md").

###### Note

For **RecordSetType** = A, be sure to specify either
**AliasTargetDnsName**or **RecordSetValue**.

###### Note

You can add up to 50 tags, but to do so you must enable the **Additional configuration** view.

To learn more, see
[Working with Public Hosted Zones](../../../Route53/latest/DeveloperGuide/AboutHZWorkingWith.md "../../../Route53/latest/DeveloperGuide/AboutHZWorkingWith.md").

To update your public DNS stack after it's created, see
[Update public DNS Route 53](ex-dns-public-update-stack-col.md "ex-dns-public-update-stack-col.md").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-0vzsr2nyraedl](schemas.md#ct-0vzsr2nyraedl-schema-section "schemas.md#ct-0vzsr2nyraedl-schema-section").

## Example: Required Parameters

```
Example not available.
```

## Example: All Parameters

```
{
  "DocumentName" : "AWSManagedServices-CreateAddRoute53Resources",
  "Region" : "us-east-1",
  "Parameters": {
    "DomainName": "mydomain.com",
    "DomainType": "public",
    "RecordSet": [
      "{\"RecordSet\":[{\"Name\":\"test1.mydomain.com\",\"Type\":\"A\",\"TTL\":\"600\",\"ResourceRecords\":[\"10.1.1.1\",\"10.1.2.2\"]},{\"Name\":\"test3.mydomain.com\",\"Type\":\"CNAME\",\"TTL\":\"600\",\"ResourceRecords\":[\"amazon.com\"]},{\"Name\":\"test4.mydomain.com\",\"Type\":\"A\",\"AliasTarget\":{\"DNSName\":\"d1i3674zujyzy1.cloudfront.net\",\"EvaluateTargetHealth\":true,\"HostedZoneId\":\"Z2FDTNDATAQYW2\"}},{\"Name\":\"weighted.mydomain.com\",\"Weight\":200,\"SetIdentifier\":\"Example-Set-Identifier-1\",\"Type\":\"A\",\"AliasTarget\":{\"DNSName\":\"d1i3674zujyzy1.cloudfront.net\",\"EvaluateTargetHealth\":true,\"HostedZoneId\":\"Z2FDTNDATAQYW2\"}},{\"Name\":\"geolocationexample.mydomain.com\",\"SetIdentifier\":\"Example-GeoLocation-Identifier-1\",\"GeoLocation\":{\"CountryCode\":\"US\",\"SubdivisionCode\":\"WA\"},\"Type\":\"A\",\"AliasTarget\":{\"DNSName\":\"d1i3674zujyzy1.cloudfront.net\",\"EvaluateTargetHealth\":true,\"HostedZoneId\":\"Z2FDTNDATAQYW2\"}},{\"Name\":\"examplelatency.mydomain.com\",\"SetIdentifier\":\"Example-Latency-Identifier-1\",\"Region\":\"ap-southeast-2\",\"Type\":\"A\",\"TTL\":\"600\",\"ResourceRecords\":[\"10.1.1.1\",\"10.1.2.2\"]},{\"Name\":\"examplemultivalue.mydomain.com\",\"SetIdentifier\":\"Example-MultiValue-Identifier-1\",\"MultiValueAnswer\":true,\"Type\":\"A\",\"TTL\":\"600\",\"ResourceRecords\":[\"10.1.1.1\"]}]}"
    ]
  }
}

```
