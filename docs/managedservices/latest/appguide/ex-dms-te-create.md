# 4: AWS DMS target endpoint: Create, create for S3

You can use the AMS console or API/CLI to create an AMS DMS target endpoint for various databases, we provide two examples.

## DMS target endpoint: creating

AMS DMS can use S3 or any Relational Database Service (RDS) with MySQL, MariaDB, Oracle, Postgresql, or Microsoft SQL as a
target endpoint.

Screenshot of this change type in the AMS console:

![Database Migration Service target endpoint creation details for RDS-supported databases.](images/guiDmsCreateTargetEpCT.png)
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
aws --profile saml --region us-east-1 amscm create-rfc --change-type-id "ct-3gf8dolbo8x9p" --change-type-version "1.0" --title "TestDMSTargetEndpoint" --execution-parameters "{\"Description\":\"`TestTE`\",\"VpcId\":\"`VPC-ID`\",\"Name\":\"`TE-NAME`\",\"StackTemplateId\":\"stm-knghtmmgefafdq89u\",\"TimeoutInMinutes\":60,\"Parameters\":{\"EngineName\":\"mysql\",\"Password\":\"`testpw123`\",\"Port\":\"`3306`\",\"ServerName\":\"`mytestdb.d5fga0rf2wpi.ap-southeast-2.rds.amazonaws.com`\",\"Username\":\"`USERNAME`\"}}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters for this change type to a JSON file named CreateDmsTeParams.json.

```
aws amscm get-change-type-version --change-type-id "ct-3gf8dolbo8x9p" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateDmsTeParams.json
```

2. Modify and save the execution parameters JSON file. For example, you can replace the contents with something like this:

```
{
"Description":          "`TestTE`",
"VpcId":                "`VPC_ID`",
"StackTemplateId":      "stm-knghtmmgefafdq89u",
"Name":                 "`TE-NAME`",
"TimeoutInMinutes":     `60`,
"Parameters":   {
    "EngineName":       "`mysql`",
    "ServerName":       "`sql.db.example.com`",
    "Port":             "`3306`",
    "Username":         "`DB-USER`",
    "Password":         "`DB-PW`",}
    }
}
```

3. Output the JSON template to a file in your current folder; this example names it CreateDmsTeRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > CreateDmsTeRfc.json
```

4. Modify and save the CreateDmsTeRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-3gf8dolbo8x9p",
"Title":                "`DB-DMS-Target-Endpoint`"
}
```

5. Create the RFC, specifying the execution parameters file and the CreateDmsTeRfc file:

```
aws amscm create-rfc --cli-input-json file://CreateDmsTeRfc.json --execution-parameters file://CreateDmsTeParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

- This change type is now at version 2.0.
- AMS DMS can use S3 or any Relational Database Service (RDS) with MySQL, MariaDB, Oracle, Postgresql, or Microsoft SQL as a
  target endpoint. For an S3 target endpoint, see [DMS target endpoint for S3: creating](#ex-dms-te-s3-create-col "#ex-dms-te-s3-create-col").
- For more information, see [Targets for Data Migration](../../../dms/latest/userguide/CHAP_Target.md "../../../dms/latest/userguide/CHAP_Target.md").
- You can add up to 50 tags, but to do so you must enable the **Additional configuration** view.

## DMS target endpoint for S3: creating

Screenshot of this change type in the AMS console:

![Change type details for creating a DMS target endpoint for S3, including ID and version.](images/guiDmsCreateTargetEpS3CT.png)
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
aws --profile saml --region us-east-1 amscm create-rfc --change-type-id "ct-05muqzievnxk5" --change-type-version "1.0" --title `"TestDMSTargetEndpointS3"` --execution-parameters "{\"Description\":\"`TestS3TE`\",\"VpcId\":\"`VPC-ID`\",\"Name\":\"`S3TE-NAME`\",\"StackTemplateId\":\"stm-knghtmmgefafdq89u\",\"TimeoutInMinutes\":60,\"Parameters\":{\"EngineName\":\"s3\",\"S3BucketName\":\"`amzn-s3-demo-bucket`\",\"S3ServiceAccessRoleArn\":\"`arn:aws:iam::123456789123:role/my-s3-role`\"}}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters for this change type to a JSON file; this example names it CreateDmsTeS3Params.json:

```
aws amscm get-change-type-version --change-type-id "ct-05muqzievnxk5" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateDmsTeS3Params.json
```

2. Modify and save the execution parameters CreateDmsTeS3Params.json file. For example, you can replace the contents with something like this:

```
{
"Description":          "`TestS3DMS-TE`",
"VpcId":                "`VPC_ID`",
"StackTemplateId":      "stm-knghtmmgefafdq89u",
"Name":                 "`DMS-S3-TE`",
"TimeoutInMinutes":     `60`,
"Parameters":   {
    "EngineName":       "`s3`",
    "S3BucketName":      "`amzn-s3-demo-bucket`",
    "S3ServiceAccessRoleArn":       "`arn:aws:iam::123456789101:role/ams-ops-ct-authors-dms-s3-test-role`"
      }
}
```

3. Output the JSON template to a file in your current folder; this example names it CreateDmsTeS3Rfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > CreateDmsTeS3Rfc.json
```

4. Modify and save the CreateDmsTeS3Rfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-05muqzievnxk5",
"Title":                "`DMS_Target_S3`"
}
```

5. Create the RFC, specifying the execution parameters file and the CreateDmsTeS3Rfc file:

```
aws amscm create-rfc --cli-input-json file://CreateDmsTeS3Rfc.json --execution-parameters file://CreateDmsTeS3Params.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

###### Note

You can add up to 50 tags, but to do so you must enable the **Additional configuration** view.

AMS provides a separate change type for creating a target endpoint for S3. For more information, see
[Using Amazon S3 as a Target for AWS Database Migration Service](../../../dms/latest/userguide/CHAP_Target.md "../../../dms/latest/userguide/CHAP_Target.md") and
[Extra Connection Attributes When Using Amazon S3 as a Target for AWS DMS](../../../dms/latest/userguide/CHAP_Target.md#CHAP_Target.S3.Configuring "../../../dms/latest/userguide/CHAP_Target.md#CHAP_Target.S3.Configuring").
