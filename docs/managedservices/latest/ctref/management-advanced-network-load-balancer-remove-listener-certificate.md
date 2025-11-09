# Network Load Balancer | Remove Listener Certificate

Remove a certificate from the specified Network Load Balancer (NLB) listener. Use the RemediateStackDrift parameter for the automation to try to remediate drift, if it is introduced.

**Full classification:** Management | Advanced stack components | Network Load Balancer | Remove listener certificate

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-3929xwf222jri |
| Current version             | 1.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Remove NLB listener certificate

The following shows this change type in the AMS console.

![Remove NLB Listener Certificate panel with description, ID, and version details.](images/guiNlbRemoveListenerCertCT.png)
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
aws amscm  create-rfc --change-type-id "ct-3929xwf222jri" --change-type-version "1.0" --title "`Remove listener certificate NLB`" --execution-parameters "{\"DocumentName\": \"AWSManagedServices-RemoveCertificateToElbv2Listener\",\"Region\": \"`us-east-1`\",\"Parameters\":{\"ListenerArn\":[\"`arn:aws:elasticloadbalancing:us-east-1:123456789012:listener/app/testalb/fc656bcb5cacb3ae/a0c0da77f9b1461e`\"],\"CertificateArn\":[\"`arn:aws:acm:us-east-1:123456789012:certificate/ecb242e8-3da5-4da6-813c-17040f086fba`\"],\"IsDefault\":[\"`False`\"],\"RemediateStackDrift\":[\"`True`\"]}}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a
   JSON file. For example, you can replace the contents with something like this:

```
aws amscm get-change-type-version --change-type-id "ct-3929xwf222jri" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > RemoveNlbListenerCertParams.json
```

2. Modify and save the RemoveNlbListenerCertParams file. For example:

```
{
    "DocumentName": "AWSManagedServices-RemoveCertificateToElbv2Listener",
    "Region": "`us-east-1`",
    "Parameters": {
        "ListenerArn": [
            "`arn:aws:elasticloadbalancing:us-east-1:123456789012:listener/app/testalb/fc656bcb5cacb3ae/a0c0da77f9b1461e`"
        ],
        "CertificateArn": [
            "`arn:aws:acm:us-east-1:123456789012:certificate/ecb242e8-3da5-4da6-813c-17040f086fba`"
        ],
        "IsDefault": [
            "`False`"
        ],
        "RemediateStackDrift": [
            "`True`"
        ]
    }
}
```

3. Output the RFC template to a file in your current folder. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --generate-cli-skeleton > RemoveNlbListenerCertRfc.json
```

4. Modify and save the RemoveNlbListenerCertRfc.json file. For example:

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-3929xwf222jri",
"Title":                "`NLB-Remove-Listener-Cert-RFC`"
}
```

5. Create the RFC, specifying the RemoveNlbListenerCertRfc file and the RemoveNlbListenerCertParams file:

```
aws amscm create-rfc --cli-input-json file://RemoveNlbListenerCertRfc.json --execution-parameters file://RemoveNlbListenerCertParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

For information about listeners, see
[ELB Listeners](../../../elasticloadbalancing/latest/network/load-balancer-listeners.md "../../../elasticloadbalancing/latest/network/load-balancer-listeners.md").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-3929xwf222jri](schemas.md#ct-3929xwf222jri-schema-section "schemas.md#ct-3929xwf222jri-schema-section").

## Example: Required Parameters

```
{
    "DocumentName": "AWSManagedServices-RemoveCertificateFromElbv2Listener",
    "Region": "us-east-1",
    "Parameters": {
        "CertificateArn": [
            "arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012"
        ],
        "ListenerArn": [
            "arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/net/my-load-balancer/50dc6c495c0c9188/50dc6c495c0c9188"
        ]
    }
}
```

## Example: All Parameters

```
{
    "DocumentName": "AWSManagedServices-RemoveCertificateFromElbv2Listener",
    "Region": "us-east-1",
    "Parameters": {
        "CertificateArn": [
            "arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012"
        ],
        "ListenerArn": [
            "arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/net/my-load-balancer/50dc6c495c0c9188/50dc6c495c0c9188"
        ],
        "RemediateStackDrift": [
            "False"
        ]
    }
}
```
