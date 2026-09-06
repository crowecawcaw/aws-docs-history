

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# ACM Certificate With Additional SANs \| Create
<a name="deployment-advanced-acm-certificate-with-additional-sans-create"></a>

ACM Certificate with additional SANs

**Full classification:** Deployment \| Advanced stack components \| ACM Certificate with additional SANs \| Create

## Change Type Details
<a name="ct-3l14e139i5p50-DAAc-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-3l14e139i5p50 | 
| Current version | 1.0 | 
| Expected execution duration | 60 minutes | 
| AWS approval | Required | 
| Customer approval | Not required | 
| Execution mode | Automated | 

## Additional Information
<a name="deployment-advanced-acm-certificate-with-additional-sans-create-info"></a>

### Create ACM certificate with additional SANs
<a name="ex-acm-create-col"></a>

#### Creating an ACM with the console
<a name="acm-create-con"></a>

The following shows this change type in the AMS console.

![Change type details for ACM Certificate with additional SANs, including ID and version.](http://docs.aws.amazon.com/managedservices/latest/ctref/images/guiAcmCreateCT.png)


How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.

1. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the **Choose by category** view.
   + **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the **Run RFC** page. Note that you cannot choose an older CT version with quick create.

     To sort CTs, use the **All change types** area in either the **Card** or **Table** view. In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable, a **Create with older version** option appears next to the **Create RFC** button.
   + **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

1. On the **Run RFC** page, open the CT name area to see the CT details box. A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the **Additional configuration** area to add information about the RFC.

   In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure optional execution parameters, open the **Additional configuration** area.

1. When finished, click **Run**. If there are no errors, the **RFC successfully created** page displays with the submitted RFC details, and the initial **Run output**. 

1. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status. Optionally, cancel the RFC or create a copy of it with the options at the top of the page.

#### Creating an ACM with the CLI
<a name="acm-create-cli"></a>

How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc` command with the two files as input. Both methods are described here.

1. Submit the RFC: `aws amscm submit-rfc --rfc-id {{ID}}` command with the returned RFC ID.

   Monitor the RFC: `aws amscm get-rfc --rfc-id {{ID}}` command.

To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value={{CT_ID}}
```
**Note**  
You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the [AMS Change Management API Reference](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_CreateRfc.html).

*INLINE CREATE*:

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

All parameters:

```
aws amscm create-rfc --title {{test-acm-certificate}} --change-type-id ct-3l14e139i5p50 --change-type-version 1.0 --execution-parameters '{ "Description": "{{Create an ACM certificate}}", "VpcId": "{{VPC_ID}}", "Name": "{{Create an ACM certificate}}", "StackTemplateId": "stm-ftu71ma6q29bvulv0", "Parameters": { "DomainName": "{{*.example.com}}", "ValidationDomain": "{{example.com}}", "SubjectAlternativeName1": "{{*.example-domain.com}}", "SubjectAlternativeNameValidationDomain1": "{{example-domain.com}}", "SubjectAlternativeName2": "{{*.example.net}}", "SubjectAlternativeNameValidationDomain2": "{{example.net}}", "SubjectAlternativeName3": "{{*.example-domain.net}}", "SubjectAlternativeNameValidationDomain3": "{{example-domain.net}}", "SubjectAlternativeName4": "{{*.example.org}}", "SubjectAlternativeNameValidationDomain4": "{{example.org}}", "SubjectAlternativeName5": "{{*.example-domain.org}}", "SubjectAlternativeNameValidationDomain5": "{{example-domain.org}}" }, "TimeoutInMinutes": 60 }'
```

Only required parameters:

```
aws amscm create-rfc --title {{test-acm-certificate}} --change-type-id ct-3l14e139i5p50 --change-type-version 1.0 --execution-parameters '{ "Description": "{{Create an ACM certificate}}", "VpcId": "{{VPC_ID}}", "Name": "{{Create an ACM certificate}}", "StackTemplateId": "stm-ftu71ma6q29bvulv0", "Parameters": { "DomainName": "{{*.example.com}}" }, "TimeoutInMinutes": 60 }'
```

*TEMPLATE CREATE*:

1. Output the execution parameters for this change type to a JSON file named CreateAcmParams.json.

   ```
   aws amscm get-change-type-version --change-type-id "ct-3l14e139i5p50" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateAcmParams.json
   ```

1. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

   ```
   {
   "VpcId":            "{{VPC_ID}}",
   "StackTemplateId":  "stm-ftu71ma6q29bvulv0",
   "DomainName":    "{{DOMAIN_NAME}}"
   }
   ```

1. Output the RFC template to a file in your current folder; this example names it CreateAcmRfc.json:

   ```
   aws amscm create-rfc --generate-cli-skeleton > CreateAcmRfc.json
   ```

1. Modify and save the CreateAcmRfc.json file. For example, you can replace the contents with something like this:

   ```
   {
   "ChangeTypeId":         "ct-3l14e139i5p50",
   "ChangeTypeVersion":    "{{1.0}}",
   "Title":                "{{ACM-Create-RFC}}"
   }
   ```

1. Create the RFC, specifying the CreateAcmRfc file and the CreateAcmParams file:

   ```
   aws amscm create-rfc --cli-input-json file://CreateAcmRfc.json  --execution-parameters file://CreateAcmParams.json
   ```

   You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

#### Tips
<a name="ex-acm-create-tip"></a>

**Note**  
The timeout setting isn't only about execution, but also your validation of the ACM certificate through email validation. Without your validation, the RFC fails.

To learn more about ACM certificates, see [ What Is AWS Certificate Manager?](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) and [ACM Certificate Characteristics](https://docs.aws.amazon.com/acm/latest/userguide/acm-certificate.html).

## Execution Input Parameters
<a name="deployment-advanced-acm-certificate-with-additional-sans-create-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-3l14e139i5p50](schemas.md#ct-3l14e139i5p50-schema-section).

## Example: Required Parameters
<a name="deployment-advanced-acm-certificate-with-additional-sans-create-ex-min"></a>

```
Example not available.
```

## Example: All Parameters
<a name="deployment-advanced-acm-certificate-with-additional-sans-create-ex-max"></a>

```
{
  "Description": "This is a test description",
  "Name": "Test Stack",
  "Parameters": {
    "DomainName": "example.com",
    "ValidationDomain": "example.com",
    "SubjectAlternativeName1": "domain-1.example.com",
    "SubjectAlternativeNameValidationDomain1": "domain-1.example.com",
    "SubjectAlternativeName2": "domain-2.example.com",
    "SubjectAlternativeNameValidationDomain2": "domain-2.example.com",
    "SubjectAlternativeName3": "domain-3.example.com",
    "SubjectAlternativeNameValidationDomain3": "domain-3.example.com",
    "SubjectAlternativeName4": "domain-4.example.com",
    "SubjectAlternativeNameValidationDomain4": "domain-4.example.com",
    "SubjectAlternativeName5": "domain-5.example.com",
    "SubjectAlternativeNameValidationDomain5": "domain-5.example.com"
  },
  "StackTemplateId": "stm-ftu71ma6q29bvulv0",
  "TimeoutInMinutes": 60,
  "VpcId": "vpc-01234567890abcdef"
}
```