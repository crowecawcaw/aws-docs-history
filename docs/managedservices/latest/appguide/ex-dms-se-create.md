# 3: AWS DMS source endpoint: Create, create for Mongo DB, create for S3

You can use the AMS console or API/CLI to create an AMS DMS source endpoint for various databases, we provide three examples.

## DMS source endpoint: creating

Screenshot of this change type in the AMS console:

![Change type details for creating a DMS source endpoint, including ID and version.](images/guiDmsCreateSourceEpCT.png)
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
aws --profile saml --region us-east-1 amscm create-rfc --title "`MariaDB-DMS-Source-Endpoint`" --aws-account-id `ACCOUNT-ID` --change-type-id ct-0attesnjqy2cx --change-type-version 1.0 --execution-parameters "{\"Description\":\"`DESCRIPTION.`\",\"VpcId\":\"`VPC-ID`\",\"Name\":\"`MariaDB-DMS-SE`\",\"Parameters\":{\"EngineName\":\"`mariadb`\",\"ServerName\":\"`mariadb.db.example.com`\",\"Port\":`3306`,\"Username\":\"`DB-USER`\",\"Password\":\"`DB-PW`\"},\"TimeoutInMinutes\":60,\"StackTemplateId\":\"stm-pud4ghhkp7395n9bc\"}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters for this change type to a JSON file named CreateDmsSeParams.json.

```
aws amscm get-change-type-version --change-type-id "ct-0attesnjqy2cx" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateDmsSeParams.json
```

2. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

```
{
"Description":          "`MariaDB-DMS-SE`",
"VpcId":                "`VPC_ID`",
"Name":                 "`Test SE`",
"StackTemplateId":      "stm-pud4ghhkp7395n9bc",
"TimeoutInMinutes":     `60`,
"Parameters":   {
    "Description":      "`DESCRIPTION`",
    "EngineName":       "`mariadb`",
    "ServerName":       "`mariadb.db.example.com`",
    "Port":             "`3306`",
    "Username":         "`DB-USER`",
    "Password":         "`DB-PW`",}
    }
}
```

3. Output the JSON template to a file in your current folder; this example names it CreateDmsSeRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > CreateDmsSeRfc.json
```

4. Modify and save the CreateDmsSeRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-0attesnjqy2cx",
"Title":                "`MariaDB-DMS-Source-Endpoint`"
}
```

5. Create the RFC, specifying the execution parameters file and the CreateDmsSeRfc file:

```
aws amscm create-rfc --cli-input-json file://CreateDmsSeRfc.json --execution-parameters file://CreateDmsSeParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.
Before you create the DMS endpoint, make sure that your password doesn't contain unsupported characters. For more information, see [Creating source and target endpoints](../../../dms/latest/userguide/CHAP_Endpoints.md "../../../dms/latest/userguide/CHAP_Endpoints.md") in the _AWS Database Migration Service User Guide_.

To learn more, see [Sources for Data Migration](../../../dms/latest/userguide/CHAP_Source.md "../../../dms/latest/userguide/CHAP_Source.md").

For an S3 source endpoint, see [DMS source endpoint for S3: creating](#ex-dms-se-s3-create-col "#ex-dms-se-s3-create-col").

For a Mongo DB source endpoint, see [DMS source endpoint for MongoDB: Creating](#ex-dms-se-mongo-create-col "#ex-dms-se-mongo-create-col").

## DMS source endpoint for MongoDB: Creating

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
[DMS source endpoint for S3: creating](#ex-dms-se-s3-create-col "#ex-dms-se-s3-create-col").

## DMS source endpoint for S3: creating

Screenshot of this change type in the AMS console:

![Change type details for creating a DMS source endpoint for S3, including ID and version.](images/guiDmsCreateSourceEpS3CT.png)
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
aws --profile saml --region us-east-1 amscm create-rfc --title "`S3DMSSourceEndpoint`" --aws-account-id `ACCOUNT-ID` --change-type-id ct-2oxl37nphsrjz --change-type-version 1.0 --execution-parameters "{\"Description\":\"`TestS3DMS-SE`\",\"VpcId\":\"`VPC-ID`\",\"Name\":\"`S3-DMS-SE`\",\"Parameters\":{\"EngineName\":\"s3\",\"S3BucketName\":\"`amzn-s3-demo-bucket`\",\"S3ExternalTableDefinition\":\"{\\\"TableCount\\\":\\\"1\\\",\\\"Tables\\\":[{\\\"TableName\\\":\\\"employee\\\",\\\"TablePath\\\":\\\"hr/employee/\\\",\\\"TableOwner\\\":\\\"hr\\\",\\\"TableColumns\\\":[{\\\"ColumnName\\\":\\\"Id\\\",\\\"ColumnType\\\":\\\"INT8\\\",\\\"ColumnNullable\\\":\\\"false\\\",\\\"ColumnIsPk\\\":\\\"true\\\"},{\\\"ColumnName\\\":\\\"LastName\\\",\\\"ColumnType\\\":\\\"STRING\\\",\\\"ColumnLength\\\":\\\"20\\\"},{\\\"ColumnName\\\":\\\"FirstName\\\",\\\"ColumnType\\\":\\\"STRING\\\",\\\"ColumnLength\\\":\\\"30\\\"},{\\\"ColumnName\\\":\\\"HireDate\\\",\\\"ColumnType\\\":\\\"DATETIME\\\"},{\\\"ColumnName\\\":\\\"OfficeLocation\\\",\\\"ColumnType\\\":\\\"STRING\\\",\\\"ColumnLength\\\":\\\"20\\\"}],\\\"TableColumnsTotal\\\":\\\"5\\\"}]}\",\"S3ServiceAccessRoleArn\":\"`arn:aws:iam::123456789101:role/ams-ops-ct-authors-dms-s3-test-role`\"},\"TimeoutInMinutes\":60,\"StackTemplateId\":\"stm-pud4ghhkp7395n9bc\"}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters for this change type to a JSON file named CreateDmsSeS3Params.json.

```
aws amscm get-change-type-version --change-type-id "ct-2oxl37nphsrjz" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateDmsSeS3Params.json
```

2. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

```
{
"Description":          "`TestS3DMS-SE`",
"VpcId":                "`VPC_ID`",
"Name":                 "`S3-DMS-SE`",
"StackTemplateId":      "stm-pud4ghhkp7395n9bc",
"TimeoutInMinutes":     `60`,
"Parameters":   {
    "EngineName":               "`s3`",
    "S3BucketName":              "`amzn-s3-demo-bucket`",
    "S3ExternalTableDefinition":  "`BUCKET-NAME`",
    {"TableCount":                "`1`",
      "Tables":[{"TableName":"`employee`","TablePath":"`hr/employee/`","TableOwner":"`hr`","TableColumns":[{"ColumnName":"`Id`","ColumnType":"`INT8`","ColumnNullable":"`false`","ColumnIsPk":"`true`"},{"ColumnName":"`LastName`","ColumnType":"`STRING`","ColumnLength":"`20`"},{"ColumnName":"`FirstName`","ColumnType":"`STRING`","ColumnLength":"`30`"},{"ColumnName":"`HireDate`","ColumnType":"`DATETIME`"},{"ColumnName":"`OfficeLocation`","ColumnType":"`STRING`","ColumnLength":"`20`"}],"TableColumnsTotal":"`5`"}]}"
    "S3ServiceAccessRoleArn":      "`arn:aws:iam::123456789101:role/ams-ops-ct-authors-dms-s3-test-role`",
      }
}
```

3. Output the JSON template to a file in your current folder; this example names it CreateDmsSeS3Rfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > CreateDmsSeS3Rfc.json
```

4. Modify and save the CreateDmsSeS3Rfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-2oxl37nphsrjz",
"Title":                "`DMS_Source_S3`"
}
```

5. Create the RFC, specifying the execution parameters file and the CreateDmsSeS3Rfc file:

```
aws amscm create-rfc --cli-input-json file://CreateDmsSeS3Rfc.json --execution-parameters file://CreateDmsSeS3Params.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

###### Note

You can add up to 50 tags, but to do so you must enable the **Additional configuration** view.

AMS DMS can use S3 or any Relational Database Service (RDS) source endpoint. For a Mongo DB source endpoint, see
[DMS source endpoint for MongoDB: Creating](#ex-dms-se-mongo-create-col "#ex-dms-se-mongo-create-col").
