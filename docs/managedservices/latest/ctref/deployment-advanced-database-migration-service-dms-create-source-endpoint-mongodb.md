# Database Migration Service (DMS) | Create Source Endpoint (MongoDB)

Use to create a Database Migration Service (DMS) source endpoint for MongoDB.

**Full classification:** Deployment | Advanced stack components | Database Migration Service (DMS) | Create source endpoint (MongoDB)

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-2hxcllf1b4ey0 |
| Current version             | 1.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### DMS source endpoint for MongoDB: Creating

Screenshot of this change type in the AMS console:

![Change type details for creating a DMS source endpoint for MongoDB, including ID and version.](images/guiDmsCreateSourceEpMongoCT.png)
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

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm  --profile saml --region us-east-1 create-rfc --change-type-id "ct-2hxcllf1b4ey0" --change-type-version "1.0" --title '`DMS_Source_MongoDB`' --description "`DESCRIPTION`"  --execution-parameters "{\"Description\":\"`DMS_MongoDB_Source_Endpoint`\",\"VpcId\":\"`VPC_ID`\",\"Name\":\"`DMS-Mongo-SE`\",\"StackTemplateId\":\"stm-pud4ghhkp7395n9bc\",\"TimeoutInMinutes\":60,\"Parameters\":{\"DatabaseName\":\"`mytestdb`\",\"EngineName\":\"mongodb\",\"Port\":`27017`,\"ServerName\":\"`test.example.com`\"}}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters for this change type to a JSON file named CreateDmsSeMongoParams.json.

```
aws amscm get-change-type-version --change-type-id "ct-2hxcllf1b4ey0" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateDmsSeMongoParams.json
```

2. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

```
{
"Description":          "`MongoDB-DMS-SE`",
"VpcId":                "`VPC_ID`",
"StackTemplateId":      "stm-pud4ghhkp7395n9bc",
"Name":                 "`Test Mongo SE`",
"TimeoutInMinutes":     `60`,
"Parameters":   {
    "Description":      "`DESCRIPTION`",
    "DatabaseName":       "`mytestdb`",
    "EngineName":       "`mongodb`",
    "ServerName":       "`test.example.com`",
    "Port":             "`27017`"
    }
}
```

3. Output the JSON template to a file in your current folder; this example names it CreateDmsSeMongoRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > CreateDmsSeMongoRfc.json
```

4. Modify and save the CreateDmsSeMongoRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-2hxcllf1b4ey0",
"Title":                "`DMS_Source_MongoDB`"
}
```

5. Create the RFC, specifying the execution parameters file and the CreateDmsSeMongoRfc file:

```
aws amscm create-rfc --cli-input-json file://CreateDmsSeMongoRfc.json --execution-parameters file://CreateDmsSeMongoParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

###### Note

You can add up to 50 tags, but to do so you must enable the **Additional configuration** view.

AMS DMS can use Mongo or any Relational Database Service (RDS) as a source endpoint. For an S3 source endpoint, see
[DMS source endpoint for S3: creating](deployment-advanced-database-migration-service-dms-create-source-endpoint-s3.md#ex-dms-se-s3-create-col "deployment-advanced-database-migration-service-dms-create-source-endpoint-s3.md#ex-dms-se-s3-create-col").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-2hxcllf1b4ey0](schemas.md#ct-2hxcllf1b4ey0-schema-section "schemas.md#ct-2hxcllf1b4ey0-schema-section").

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
    "CertificateArn": "arn:aws:dms:us-east-1:123456789121:cert:5957UBG4LS4ZJP2PK7YRYET6YE",
    "DatabaseName": "my-database",
    "EndpointIdentifier": "my-endpoint",
    "EngineName": "mongodb",
    "MongoDbAuthMechanism": "default",
    "MongoDbAuthSource": "admin",
    "MongoDbAuthType": "no",
    "MongoDbDocsToInvestigate": "1000",
    "MongoDbExtractDocId": "false",
    "MongoDbMetadataMode": "none",
    "Password": "$tr0n9PA55w0Rd",
    "Port": 27017,
    "ServerName": "my-server",
    "SslMode": "none",
    "Username": "my-user"
  },
  "StackTemplateId": "stm-pud4ghhkp7395n9bc",
  "TimeoutInMinutes": 60,
  "VpcId": "vpc-01234567890abcdef"
}

```
