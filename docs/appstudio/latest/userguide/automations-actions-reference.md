

# Automation actions reference
<a name="automations-actions-reference"></a>

The following is the reference documentation for automation actions used in App Studio.

An automation action, commonly referred to as an **action**, is an individual step of logic that make up an automation. Each action performs a specific task, whether it's sending an email, creating a data record, invoking a Lambda function, or calling APIs. Actions are added to automations from the action library, and can be grouped into conditional statements or loops.

For information about creating and configuring automations and their actions, see the topics in [Automations and actions: Define your app's business logic](automations.md).

## Invoke API
<a name="automations-actions-reference-invoke-API"></a>

Invokes an HTTP REST API request. Builders can use this action to send requests from App Studio to other systems or services with APIs. For example, you could use it to connect to third-party systems or homegrown applications to access business critical data, or invoke API endpoints that cannot be called by dedicated App Studio actions.

For more information about REST APIs, see [What is a RESTful API?](https://aws.amazon.com/what-is/restful-api/).

### Properties
<a name="automations-actions-reference-invoke-API-properties"></a>

#### Connector
<a name="automations-actions-reference-invoke-API-properties-connector"></a>

The **Connector** to use for the API requests made by this action. The connector dropdown only contains connectors of the following types: `API Connector` and `OpenAPI Connector`. Depending on how the connector is configured, it can contain important information such as credentials and default headers or query parameters.

For more information about API connectors, including a comparison between using `API Connector` and `OpenAPI Connector`, see [Connect to third-party services](add-connector-third-party.md).

#### API request configuration properties
<a name="automations-actions-reference-invoke-API-properties-request-config"></a>

Choose **Configure API request** from the properties panel to open the request configuration dialog box. If an **API connector** is selected, the dialog box will include connector information.

**Method:** The method for the API call. Possible values are as follows:
+ `DELETE`: Deletes a specified resource.
+ `GET`: Retrieves information or data.
+ `HEAD`: Retrieves only the headers of a response without the body.
+ `POST`: Submits data to be processed.
+ `PUSH`: Submits data to be processed.
+ `PATCH`: Partially updates a specified resource.

**Path:** The relative path to the resource.

**Headers:** Any headers in the form of key-value pairs to be sent with the API request. If a connector is selected, its configured headers will be automatically added and cannot be removed. The configured headers cannot be edited, but you can override them by adding another header with the same name.

**Query parameters:** Any query parameters in the form of key-value pairs to be sent with the API request. If a connector is selected, its configured query parameters will be automatically added and cannot be edited or removed.

**Body:** Information to be sent with the API request in JSON format. There is no body for `GET` requests.

#### Mocked output
<a name="automations-actions-reference-invoke-API-properties-mocked-output"></a>

Actions do not interact with external services or resources in the preview environment. The **Mocked output** field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes. This snippet is stored in the action's `results` map, just like the connector response would be for a published app in the live environment.

With this field, you can test various scenarios and their impact on other actions within the automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with external services through connectors.

## Invoke AWS
<a name="automations-actions-reference-invoke-aws"></a>

Invokes an operation from an AWS service. This is a general action for calling AWS services or operations, and should be used if there is not a dedicated action for the desired AWS service or operation.

### Properties
<a name="automations-actions-reference-invoke-aws-properties"></a>

#### Service
<a name="automations-actions-reference-invoke-aws-properties-service"></a>

The AWS service which contains the operation to be run.

#### Operation
<a name="automations-actions-reference-invoke-aws-properties-operation"></a>

The operation to be run.

#### Connector
<a name="automations-actions-reference-invoke-aws-properties-connector"></a>

The connector to be used for the operations run by this action. The configured connector should be set up with the proper credentials to run the operation, and other configuration information, such as the AWS region that contains any resources referenced in the operation.

#### Configuration
<a name="automations-actions-reference-invoke-aws-properties-configuration"></a>

The JSON input to be when running the specified operation. For more information about configuring inputs for AWS operations, see the [AWS SDK for JavaScript](https://docs.aws.amazon.com/sdk-for-javascript).

## Invoke Lambda
<a name="automations-actions-reference-invoke-lambda"></a>

Invokes an existing Lambda function.

### Properties
<a name="automations-actions-reference-invoke-lambda-properties"></a>

#### Connector
<a name="automations-actions-reference-invoke-lambda-properties-connector"></a>

The connector to be used for the Lambda functions run by this action. The configured connector should be set up with the proper credentials to access the Lambda function, and other configuration information, such as the AWS region that contains the Lambda function. For more information about configuring a connector for Lambda, see [Step 3: Create Lambda connector](connectors-lambda.md#connectors-lambda-create-connector).

#### Function name
<a name="automations-actions-reference-invoke-lambda-properties-function-name"></a>

The name of the Lambda function to be run. Note that this is the function name, and not the function ARN (Amazon Resource Name).

#### Function event
<a name="automations-actions-reference-invoke-lambda-properties-function-event"></a>

Key-value pairs to be passed along to your Lambda function as the event payload.

#### Mocked output
<a name="automations-actions-reference-invoke-lambda-properties-mocked-output"></a>

Actions do not interact with external services or resources in the preview environment. The **Mocked output** field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes. This snippet is stored in the action's `results` map, just like the connector response would be for a published app in the live environment.

With this field, you can test various scenarios and their impact on other actions within the automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with external services through connectors.

## Loop
<a name="automations-actions-reference-loop"></a>

Runs nested actions repeatedly to iterate through a list of items, one item at a time. For example, add the [Create record](#automations-actions-reference-create-record) action to a loop action to create multiple records.

The loop action can be nested within other loops or condition actions. The loop actions are run sequentially, and not in parallel. The results of each action within the loop can only be accessed to subsequent actions within the same loop iteration. They cannot be accessed outside of the loop or in different iterations of the loop.

### Properties
<a name="automations-actions-reference-loop-properties"></a>

#### Source
<a name="automations-actions-reference-loop-properties-source"></a>

The list of items to iterate through, one item at a time. The source can be the result of a previous action or a static list of strings, numbers, or objects that you can provide using a JavaScript expression.

##### Examples
<a name="automations-actions-reference-loop-properties-source-examples"></a>

The following list contains examples of source inputs.
+ Results from a previous action: `{{results.{{actionName}}.data}}`
+ A list of numbers: `{{[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}}`
+ A list of strings: `{{["apple", "banana", "orange", "grape", "kiwi"]}}`
+ A computed value: `{{params.{{actionName}}.split("\n")}}`

#### Current item name
<a name="automations-actions-reference-loop-properties-function-name"></a>

The name of the variable that can be used to reference the current item being iterated. The current item name is configurable so that you can nest two or more loops and access variables from each loop. For example, if you are looping through countries and cities with two loops, you could configure and reference `currentCountry` and `currentCity`.

## Condition
<a name="automations-actions-reference-condition"></a>

Runs actions based on the result of one or more specified logical conditions that are evaluated when the automation is run. The condition action is made up of the following components:
+ A *condition* field, which is used to provide a JavaScript expression that evaluates to `true` or `false`.
+ A *true branch*, which contains actions that are run if the condition evalutes to `true`.
+ A *false branch*, which contains actions that are run if the condition evalutes to `false`.

Add actions to the true and false branches by dragging them into the condition action.

### Properties
<a name="automations-actions-reference-condition-properties"></a>

#### Condition
<a name="automations-actions-reference-condition-properties-condition"></a>

The JavaScript expression to be evaluated when the action is run.

## Create record
<a name="automations-actions-reference-create-record"></a>

Creates one record in an existing App Studio entity.

### Properties
<a name="automations-actions-reference-create-record-properties"></a>

#### Entity
<a name="automations-actions-reference-create-record-properties-entity"></a>

The entity in which a record is to be created. Once an entity is selected, values must be added to the entity's fields for the record to be created. The types of the fields, and if the fields are required or optional are defined in the entity.

## Update record
<a name="automations-actions-reference-update-record"></a>

Updates an existing record in an App Studio entity.

### Properties
<a name="automations-actions-reference-update-record-properties"></a>

#### Entity
<a name="automations-actions-reference-update-record-properties-entity"></a>

The entity that contains the records to be updated.

#### Conditions
<a name="automations-actions-reference-update-record-properties-conditions"></a>

The criteria that defines which records are updated by the action. You can group conditions to create one logical statement. You can combine groups or conditions with `AND` or `OR` statements.

#### Fields
<a name="automations-actions-reference-update-record-properties-fields"></a>

The fields to be updated in the records specified by the conditions.

#### Values
<a name="automations-actions-reference-update-record-properties-values"></a>

The values to be updated in the specified fields.

## Delete record
<a name="automations-actions-reference-delete-record"></a>

Deletes a record from an App Studio entity.

### Properties
<a name="automations-actions-reference-delete-record-properties"></a>

#### Entity
<a name="automations-actions-reference-delete-record-properties-entity"></a>

The entity that contains the records to be deleted.

#### Conditions
<a name="automations-actions-reference-delete-record-properties-conditions"></a>

The criteria that defines which records are deleted by the action. You can group conditions to create one logic statement. You can combine groups or conditions with `AND` or `OR` statements.

## Invoke data action
<a name="automations-actions-reference-invoke-data-action"></a>

Runs a data action with optional parameters.

### Properties
<a name="automations-actions-reference-invoke-data-action-properties"></a>

#### Data action
<a name="automations-actions-reference-invoke-data-action-properties-data-action"></a>

The data action to be run by the action.

#### Parameters
<a name="automations-actions-reference-invoke-data-action-properties-parameters"></a>

Data action parameters to be used by the data action. Data action parameters are used to send values that are used as inputs for data actions. Data action parameters can be added when configuring the automation action, but must be edited in the **Data** tab.

#### Advanced settings
<a name="automations-actions-reference-invoke-data-action-properties-advanced-settings"></a>

The `Invoke data action` action contains the following advanced settings:
+ **Page size:** The maximum number of records to fetch in each query. The default value is 500, and the maximum value is 3000.
+ **Pagination token:** The token used to fetch additional records from a query. For example, if the `Page size` is set to 500, but there are more than 500 records, passing the pagination token to a subsequent query will fetch the next 500. The token will be undefined if no more records or pages exist.

## Amazon S3: Put object
<a name="automations-actions-reference-s3-put-object"></a>

Uses the `Amazon S3 PutObject` operation to add an object identified by a key (file path) to a specified Amazon S3 bucket.

### Properties
<a name="automations-actions-reference-s3-put-object-properties"></a>

#### Connector
<a name="automations-actions-reference-s3-put-object-properties-connector"></a>

The connector to be used for the operations run by this action. The configured connector should be set up with the appropriate credentials to run the operation, and other configuration information, such as the AWS region that contains any resources referenced in the operation.

#### Configuration
<a name="automations-actions-reference-s3-put-object-properties-configuration"></a>

The required options to be used in the `PutObject` command. The options are as follows:

**Note**  
For more information about the `Amazon S3 PutObject` operation, see [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) in the *Amazon Simple Storage Service API Reference*.
+ **Bucket:** The name of the Amazon S3 bucket in which to put an object.
+ **Key:** The unique name of the object to be put into the Amazon S3 bucket.
+ **Body:** The content of the object to be put into the Amazon S3 bucket.

#### Mocked output
<a name="automations-actions-reference-s3-put-object-properties-mocked-output"></a>

Actions do not interact with external services or resources in the preview environment. The **Mocked output** field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes. This snippet is stored in the action's `results` map, just like the connector response would be for a published app in the live environment.

With this field, you can test various scenarios and their impact on other actions within the automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with external services through connectors.

## Amazon S3: Delete object
<a name="automations-actions-reference-s3-delete-object"></a>

Uses the `Amazon S3 DeleteObject` operation to delete an object identified by a key (file path) from a specified Amazon S3 bucket.

### Properties
<a name="automations-actions-reference-s3-delete-object-properties"></a>

#### Connector
<a name="automations-actions-reference-s3-delete-object-properties-connector"></a>

The connector to be used for the operations run by this action. The configured connector should be set up with the proper credentials to run the operation, and other configuration information, such as the AWS region that contains any resources referenced in the operation.

#### Configuration
<a name="automations-actions-reference-s3-delete-object-properties-configuration"></a>

The required options to be used in the `DeleteObject` command. The options are as follows:

**Note**  
For more information about the `Amazon S3 DeleteObject` operation, see [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html) in the *Amazon Simple Storage Service API Reference*.
+ **Bucket:** The name of the Amazon S3 bucket from which to delete an object.
+ **Key:** The unique name of the object to be deleted from the Amazon S3 bucket.

#### Mocked output
<a name="automations-actions-reference-s3-delete-object-properties-mocked-output"></a>

Actions do not interact with external services or resources in the preview environment. The **Mocked output** field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes. This snippet is stored in the action's `results` map, just like the connector response would be for a published app in the live environment.

With this field, you can test various scenarios and their impact on other actions within the automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with external services through connectors.

## Amazon S3: Get object
<a name="automations-actions-reference-s3-get-object"></a>

Uses the `Amazon S3 GetObject` operation to retrieve an object identified by a key (file path) from a specified Amazon S3 bucket.

### Properties
<a name="automations-actions-reference-s3-get-object-properties"></a>

#### Connector
<a name="automations-actions-reference-s3-get-object-properties-connector"></a>

The connector to be used for the operations run by this action. The configured connector should be set up with the proper credentials to run the operation, and other configuration information, such as the AWS region that contains any resources referenced in the operation.

#### Configuration
<a name="automations-actions-reference-s3-get-object-properties-configuration"></a>

The required options to be used in the `GetObject` command. The options are as follows:

**Note**  
For more information about the `Amazon S3 GetObject` operation, see [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) in the *Amazon Simple Storage Service API Reference*.
+ **Bucket:** The name of the Amazon S3 bucket from which to retrieve an object.
+ **Key:** The unique name of the object to be retrieved from the Amazon S3 bucket.

#### Mocked output
<a name="automations-actions-reference-s3-get-object-properties-mocked-output"></a>

Actions do not interact with external services or resources in the preview environment. The **Mocked output** field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes. This snippet is stored in the action's `results` map, just like the connector response would be for a published app in the live environment.

With this field, you can test various scenarios and their impact on other actions within the automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with external services through connectors.

## Amazon S3: List objects
<a name="automations-actions-reference-s3-list-objects"></a>

Uses the `Amazon S3 ListObjects` operation to list objects in a specified Amazon S3 bucket.

### Properties
<a name="automations-actions-reference-s3-list-objects-properties"></a>

#### Connector
<a name="automations-actions-reference-s3-list-objects-properties-connector"></a>

The connector to be used for the operations run by this action. The configured connector should be set up with the proper credentials to run the operation, and other configuration information, such as the AWS region that contains any resources referenced in the operation.

#### Configuration
<a name="automations-actions-reference-s3-list-objects-properties-configuration"></a>

The required options to be used in the `ListObjects` command. The options are as follows:

**Note**  
For more information about the `Amazon S3 ListObjects` operation, see [ListObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html) in the *Amazon Simple Storage Service API Reference*.
+ **Bucket:** The name of the Amazon S3 bucket from which to list objects.

#### Mocked output
<a name="automations-actions-reference-s3-list-objects-properties-mocked-output"></a>

Actions do not interact with external services or resources in the preview environment. The **Mocked output** field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes. This snippet is stored in the action's `results` map, just like the connector response would be for a published app in the live environment.

With this field, you can test various scenarios and their impact on other actions within the automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with external services through connectors.

## Amazon Textract: Analyze document
<a name="automations-actions-reference-textract-analyze-document"></a>

Uses the `Amazon Textract AnalyzeDocument` operation to analyze an input document for relationships between detected items.

### Properties
<a name="automations-actions-reference-textract-analyze-document-properties"></a>

#### Connector
<a name="automations-actions-reference-textract-analyze-document-properties-connector"></a>

The connector to be used for the operations run by this action. The configured connector should be set up with the proper credentials to run the operation, and other configuration information, such as the AWS region that contains any resources referenced in the operation.

#### Configuration
<a name="automations-actions-reference-textract-analyze-document-properties-configuration"></a>

The content of the request to be used in the `AnalyzeDocument` command. The options are as follows:

**Note**  
For more information about the `Amazon Textract AnalyzeDocument` operation, see [AnalyzeDocument](https://docs.aws.amazon.com/textract/latest/dg/API_AnalyzeDocument.html) in the *Amazon Textract Developer Guide*.
+ **Document / S3Object / Bucket:** The name of the Amazon S3 bucket. This parameter can be left empty if a file is passed to the action with the **S3 upload** component.
+ **Document / S3Object / Name:** The file name of the input document. This parameter can be left empty if a file is passed to the action with the **S3 upload** component.
+ **Document / S3Object / Version:** If the Amazon S3 bucket has versioning enabled, you can specify the version of the object. This parameter can be left empty if a file is passed to the action with the **S3 upload** component.
+ **FeatureTypes:** A list of the types of analysis to perform. Valid values are: `TABLES`, `FORMS`, `QUERIES`, `SIGNATURES`, and `LAYOUT`.

#### Mocked output
<a name="automations-actions-reference-textract-analyze-document-properties-mocked-output"></a>

Actions do not interact with external services or resources in the preview environment. The **Mocked output** field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes. This snippet is stored in the action's `results` map, just like the connector response would be for a published app in the live environment.

With this field, you can test various scenarios and their impact on other actions within the automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with external services through connectors.

## Amazon Textract: Analyze expense
<a name="automations-actions-reference-textract-analyze-expense"></a>

Uses the `Amazon Textract AnalyzeExpense` operation to analyze an input document for financially-related relationships between text.

### Properties
<a name="automations-actions-reference-textract-analyze-expense-properties"></a>

#### Connector
<a name="automations-actions-reference-textract-analyze-expense-properties-connector"></a>

The connector to be used for the operations run by this action. The configured connector should be set up with the proper credentials to run the operation, and other configuration information, such as the AWS region that contains any resources referenced in the operation.

#### Configuration
<a name="automations-actions-reference-textract-analyze-expense-properties-configuration"></a>

The content of the request to be used in the `AnalyzeExpense` command. The options are as follows:

**Note**  
For more information about the `Amazon Textract AnalyzeExpense` operation, see [AnalyzeExpense](https://docs.aws.amazon.com/textract/latest/dg/API_AnalyzeExpense.html) in the *Amazon Textract Developer Guide*.
+ **Document / S3Object / Bucket:** The name of the Amazon S3 bucket. This parameter can be left empty if a file is passed to the action with the **S3 upload** component.
+ **Document / S3Object / Name:** The file name of the input document. This parameter can be left empty if a file is passed to the action with the **S3 upload** component.
+ **Document / S3Object / Version:** If the Amazon S3 bucket has versioning enabled, you can specify the version of the object. This parameter can be left empty if a file is passed to the action with the **S3 upload** component.

#### Mocked output
<a name="automations-actions-reference-textract-analyze-expense-properties-mocked-output"></a>

Actions do not interact with external services or resources in the preview environment. The **Mocked output** field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes. This snippet is stored in the action's `results` map, just like the connector response would be for a published app in the live environment.

With this field, you can test various scenarios and their impact on other actions within the automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with external services through connectors.

## Amazon Textract: Analyze ID
<a name="automations-actions-reference-textract-analyze-id"></a>

Uses the `Amazon Textract AnalyzeID` operation to analyze an identity document for relevant information.

### Properties
<a name="automations-actions-reference-textract-analyze-id-properties"></a>

#### Connector
<a name="automations-actions-reference-textract-analyze-id-properties-connector"></a>

The connector to be used for the operations run by this action. The configured connector should be set up with the proper credentials to run the operation, and other configuration information, such as the AWS region that contains any resources referenced in the operation.

#### Configuration
<a name="automations-actions-reference-textract-analyze-id-properties-configuration"></a>

The content of the request to be used in the `AnalyzeID` command. The options are as follows:

**Note**  
For more information about the `Amazon Textract AnalyzeID` operation, see [AnalyzeID](https://docs.aws.amazon.com/textract/latest/dg/API_AnalyzeID.html) in the *Amazon Textract Developer Guide*.
+ **Document / S3Object / Bucket:** The name of the Amazon S3 bucket. This parameter can be left empty if a file is passed to the action with the **S3 upload** component.
+ **Document / S3Object / Name:** The file name of the input document. This parameter can be left empty if a file is passed to the action with the **S3 upload** component.
+ **Document / S3Object / Version:** If the Amazon S3 bucket has versioning enabled, you can specify the version of the object. This parameter can be left empty if a file is passed to the action with the **S3 upload** component.

#### Mocked output
<a name="automations-actions-reference-textract-analyze-id-properties-mocked-output"></a>

Actions do not interact with external services or resources in the preview environment. The **Mocked output** field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes. This snippet is stored in the action's `results` map, just like the connector response would be for a published app in the live environment.

With this field, you can test various scenarios and their impact on other actions within the automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with external services through connectors.

## Amazon Textract: Detect doc text
<a name="automations-actions-reference-textract-detect-document-text"></a>

Uses the `Amazon Textract DetectDocumentText` operation to detect lines of text and the words that make up a line of text in an input document.

### Properties
<a name="automations-actions-reference-textract-detect-document-text-properties"></a>

#### Connector
<a name="automations-actions-reference-textract-detect-document-text-properties-connector"></a>

The connector to be used for the operations run by this action. The configured connector should be set up with the proper credentials to run the operation, and other configuration information, such as the AWS region that contains any resources referenced in the operation.

#### Configuration
<a name="automations-actions-reference-textract-detect-document-text-properties-configuration"></a>

The content of the request to be used in the `DetectDocumentText` command. The options are as follows:

**Note**  
For more information about the `Amazon Textract DetectDocumentText` operation, see [DetectDocumentText](https://docs.aws.amazon.com/textract/latest/dg/API_DetectDocumentText.html) in the *Amazon Textract Developer Guide*.
+ **Document / S3Object / Bucket:** The name of the Amazon S3 bucket. This parameter can be left empty if a file is passed to the action with the **S3 upload** component.
+ **Document / S3Object / Name:** The file name of the input document. This parameter can be left empty if a file is passed to the action with the **S3 upload** component.
+ **Document / S3Object / Version:** If the Amazon S3 bucket has versioning enabled, you can specify the version of the object. This parameter can be left empty if a file is passed to the action with the **S3 upload** component.

#### Mocked output
<a name="automations-actions-reference-textract-detect-document-text-properties-mocked-output"></a>

Actions do not interact with external services or resources in the preview environment. The **Mocked output** field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes. This snippet is stored in the action's `results` map, just like the connector response would be for a published app in the live environment.

With this field, you can test various scenarios and their impact on other actions within the automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with external services through connectors.

## Amazon Bedrock: GenAI Prompt
<a name="automations-actions-reference-bedrock-prompt"></a>

Uses the [Amazon Bedrock InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html) operation to run inference using the prompt and inference parameters provided in the action properties. The action can generate text, images, and embeddings.

### Properties
<a name="automations-actions-reference-bedrock-prompt-properties"></a>

#### Connector
<a name="automations-actions-reference-bedrock-prompt-properties-connector"></a>

The connector to be used for the operations run by this action. To use this action successfully, the connector must be configured with **Amazon Bedrock Runtime** as the service. The configured connector should be set up with the proper credentials to run the operation, and other configuration information, such as the AWS region that contains any resources referenced in the operation.

#### Model
<a name="automations-actions-reference-bedrock-prompt-properties-model"></a>

The foundation model to be used by Amazon Bedrock to process the request. For more information about models in Amazon Bedrock, see [Amazon Bedrock foundation model information](https://docs.aws.amazon.com/bedrock/latest/userguide/foundation-models-reference.html) in the *Amazon Bedrock User Guide*.

#### Input type
<a name="automations-actions-reference-bedrock-prompt-properties-input-type"></a>

The input type of the input send to the Amazon Bedrock model. The possible values are **Text**, **Document**, and **Image**. If an input type is not available for selection, it is likely not supported by the configured model.

#### User prompt
<a name="automations-actions-reference-bedrock-prompt-properties-user-prompt"></a>

The prompt to be sent to the Amazon Bedrock model to be processed to generate a response. You can enter static text, or pass in an input from another part of your application, such as from a component using parameters, a previous action in the automation, or another automation. The following examples show how to pass in a value from a component or previous action:
+ To pass a value from a component using paramters: `{{params.{{paramName}}}}`
+ To pass a value from a previous action: `{{results.{{actionName}}}}`

#### System prompt (Claude models)
<a name="automations-actions-reference-bedrock-prompt-properties-system-prompt"></a>

The system prompt to be used by the Amazon Bedrock model when processing the request. The system prompt is used to provide context, instructions, or guidelines to Claude models.

#### Request settings
<a name="automations-actions-reference-bedrock-prompt-properties-request-settings"></a>

Configure various request settings and model inference parameters. You can configure the following settings:
+ **Temperature**: The temperature to be used by the Amazon Bedrock model when processing the request. The temperature determines the randomness or creativity of the Bedrock model's output. The higher the temperature, the more creative and less analytical the response will be. Possible values are `[0-10]`.
+ **Max Tokens**: Limit the length of the output of the Amazon Bedrock model.
+ **TopP**: In nucleus sampling, the model computes the cumulative distribution over all the options for each subsequent token in decreasing probability order and cuts it off once it reaches a particular probability specified by the **TopP**. You should alter either **temperature** or **TopP**, but not both
+ **Stop Sequences**: Sequences that cause the model to stop processing the request and generating output.

For more information, see [Inference request parameters and response fields for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html) in the *Amazon Bedrock User Guide*.

#### Stop Sequences
<a name="automations-actions-reference-bedrock-prompt-properties-guardrail"></a>

Enter an Amazon Bedrock Guardrail **ID** and **Version**. Guardrails are used to implement safeguards based on your use cases and responsible AI policies. For more information, see [Stop harmful content in models using Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) in the *Amazon Bedrock User Guide*.

#### Mocked output
<a name="automations-actions-reference-bedrock-prompt-properties-mocked-output"></a>

Actions do not interact with external services or resources in the preview environment. The **Mocked output** field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes. This snippet is stored in the action's `results` map, just like the connector response would be for a published app in the live environment.

With this field, you can test various scenarios and their impact on other actions within the automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with external services through connectors.

## Amazon Bedrock: Invoke model
<a name="automations-actions-reference-bedrock-invoke-model"></a>

Uses the [Amazon Bedrock InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html) operation to run inference using the prompt and inference parameters provided in the request body. You use model inference to generate text, images, and embeddings.

### Properties
<a name="automations-actions-reference-bedrock-invoke-model-properties"></a>

#### Connector
<a name="automations-actions-reference-bedrock-invoke-model-properties-connector"></a>

The connector to be used for the operations run by this action. To use this action successfully, the connector must be configured with **Amazon Bedrock Runtime** as the service. The configured connector should be set up with the proper credentials to run the operation, and other configuration information, such as the AWS region that contains any resources referenced in the operation.

#### Configuration
<a name="automations-actions-reference-bedrock-invoke-model-properties-configuration"></a>

The content of the request to be used in the `InvokeModel` command.

**Note**  
For more information about the `Amazon Bedrock InvokeModel` operation, including example commands, see [InvokeModel](https://docs.aws.amazon.com/textract/latest/dg/API_DetectDocumentText.html) in the *Amazon Bedrock API Reference*.

#### Mocked output
<a name="automations-actions-reference-bedrock-invoke-model-properties-mocked-output"></a>

Actions do not interact with external services or resources in the preview environment. The **Mocked output** field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes. This snippet is stored in the action's `results` map, just like the connector response would be for a published app in the live environment.

With this field, you can test various scenarios and their impact on other actions within the automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with external services through connectors.

## JavaScript
<a name="automations-actions-reference-javascript"></a>

Runs a custom JavaScript function to return a specified value.

**Important**  
App Studio does not support using third-party or custom JavaScript libraries.

### Properties
<a name="automations-actions-reference-javascript-properties"></a>

#### Source code
<a name="automations-actions-reference-javascript-properties-source-code"></a>

The JavaScript code snippet to be run by the action.

**Tip**  
You can use AI to help generate JavaScript for you by performing the following steps:  
Choose the expand icon to open the expanded JavaScript editor.
(Optional): Enable the **Modify code** toggle to modify any existing JavaScript. Otherwise, AI will replace any existing JavaScript.
In **Generate JavaScript**, describe what you want to do with JavaScript, for example: **Add two numbers**.
Choose the send icon to generate your JavaScript.

## Invoke automation
<a name="automations-actions-reference-invoke-automation"></a>

Runs a specified automation.

### Properties
<a name="automations-actions-reference-invoke-automation-properties"></a>

#### Invoke Automation
<a name="automations-actions-reference-invoke-automation-properties-invoke-automation"></a>

The automation to be run by the action.

## Send email
<a name="automations-actions-reference-send-email"></a>

Uses the `Amazon SES SendEmail` operation to send an email.

### Properties
<a name="automations-actions-reference-send-email-properties"></a>

#### Connector
<a name="automations-actions-reference-send-email-properties-connector"></a>

The connector to be used for the operations run by this action. The configured connector should be set up with the proper credentials to run the operation, and other configuration information, such as the AWS region that contains any resources referenced in the operation.

#### Configuration
<a name="automations-actions-reference-send-email-properties-configuration"></a>

The content of the request to be used in the `SendEmail` command. The options are as follows:

**Note**  
For more information about the `Amazon SES SendEmail` operation, see [SendEmail](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SendEmail.html) in the *Amazon Simple Email Service API Reference*.

#### Mocked output
<a name="automations-actions-reference-send-email-properties-mocked-output"></a>

Actions do not interact with external services or resources in the preview environment. The **Mocked output** field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes. This snippet is stored in the action's `results` map, just like the connector response would be for a published app in the live environment.

With this field, you can test various scenarios and their impact on other actions within the automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with external services through connectors.