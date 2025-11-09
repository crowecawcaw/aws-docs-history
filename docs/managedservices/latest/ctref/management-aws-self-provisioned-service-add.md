# Self-Provisioned Service | Add

Add a specific, allowed, AWS service to your AMS account. This CT validates prerequisites in the account and deploys a service with the default parameters. Not all Self-service provisioning services are supported, the ServiceName parameter for this CT lists the ones that are. For each service that you add, AMS creates a new role so you use the service without AMS management under the AMS Shared Responsibility model. Compliance is a shared responsibility and your AMS compliance status does not automatically apply to services or applications that you add in this way. Some AWS services do not have compliance certifications. For more information, see the AWS Services in Scope of AWS Assurance Program page. On that page, unless specifically excluded, features of each of the services are considered in scope of the assurance programs, and are reviewed and tested as part of our assessment when you submit this CT.

**Full classification:** Management | AWS service | Self-provisioned service | Add

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-1w8z66n899dct |
| Current version             | 1.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Add Self-Service Provisioning service

The following shows this change type in the AMS console.

![Add Self-Provisioned AWS Service panel with ID, execution mode, and description details.](images/guiAwsSelfServeAddAutoCT.png)
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
quotes when providing execution parameters inline), and then submit the returned RFC ID.
For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-1w8z66n899dct" --change-type-version "1.0" --title "Add new Self-provisioned service" --execution-parameters "{\"DocumentName\": \"AWSManagedServices-HandleCreateSSPSResources-Admin\",\"Region\": \"`us-east-1`\",\"Parameters\": {\"ServiceName\": \"`AWS License Manager`\"}}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters for this change type to a JSON file named
   AddSspsParameters.json.

```
aws amscm get-change-type-version --change-type-id "ct-1w8z66n899dct" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > AddSspsParameters.json
```

2. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

```
{
  "DocumentName": "AWSManagedServices-HandleCreateSSPSResources-Admin",
  "Region": "`us-east-1`",
  "Parameters": {
    "ServiceName": "`AWS License Manager`"
  }
}
```

3. Output the RFC template to a file in your current folder; this example names it
   AddSspsRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > AddSspsRfc.json
```

4. Modify and save the AddSspsRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeId":         "`ct-1w8z66n899dct`",
"ChangeTypeVersion":    "`1.0`",
"Title":                "`Add new Self-provisioned service`"
}
```

5. Create the RFC, specifying the SelfServeServiceRfc file and the SelfServeServiceParams file:

```
aws amscm create-rfc --cli-input-json file://AddSspsRfc.json  --execution-parameters file://AddSspsParameters.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

- The **ServiceName** field in the console lists the self-provisioned
  services supported by this CT. Limited to AMS-approved AWS services. For a list, see
  [Setting Up Self-serve Services](../userguide/self-service-provisioning.md "../userguide/self-service-provisioning.md").
- For self-provisioned services not supported by this CT, or for deployment with custom
  parameters, use the manual version: Management | AWS service |
  [Self-Provisioned Service | Add (managed automation)](management-aws-self-provisioned-service-add-review-required.md "management-aws-self-provisioned-service-add-review-required.md") (ct-3qe6io8t6jtny).

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-1w8z66n899dct](schemas.md#ct-1w8z66n899dct-schema-section "schemas.md#ct-1w8z66n899dct-schema-section").

## Example: Required Parameters

```
{
  "DocumentName" : "AWSManagedServices-HandleCreateSSPSResources-Admin",
  "Region" : "us-east-1",
  "Parameters": {
    "ServiceName": "AWS License Manager"
  }
}
```

## Example: All Parameters

```
{
  "DocumentName" : "AWSManagedServices-HandleCreateSSPSResources-Admin",
  "Region" : "us-east-1",
  "Parameters": {
    "ServiceName": "AWS License Manager",
    "SAMLProviders": "foo-saml-provider,bar-saml-provider",
    "IAMRole": "testing_role"
  }
}
```
