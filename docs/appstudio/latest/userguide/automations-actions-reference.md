# Automation actions reference

The following is the reference documentation for automation actions used in App Studio.

An automation action, commonly referred to as an **action**,
is an individual step of logic that make up an automation. Each action performs a specific task, whether it's sending an email, creating a data record, invoking a Lambda function,
or calling APIs. Actions are added to automations from the action library, and can be grouped into conditional statements or loops.

For information about creating and configuring automations and their actions, see the topics in
[Automations and actions: Define your app's business logic](automations.md "automations.md").

## Invoke API

Invokes an HTTP REST API request. Builders can use this action to send requests from App Studio to other systems or services with APIs. For example, you
could use it to connect to third-party systems or homegrown applications to access business critical data, or invoke API endpoints that cannot be called by dedicated
App Studio actions.

For more information about REST APIs, see [What is a RESTful API?](https://aws.amazon.com/what-is/restful-api/ "https://aws.amazon.com/what-is/restful-api/").

### Properties

#### Connector

The **Connector** to use for the API requests made by this action. The connector dropdown only contains
connectors of the following types: `API Connector` and `OpenAPI Connector`. Depending
on how the connector is configured, it can contain
important information such as credentials and default headers or query parameters.

For more information about
API connectors, including a comparison between using `API Connector` and `OpenAPI Connector`,
see [Connect to third-party services](add-connector-third-party.md "add-connector-third-party.md").

#### API request configuration properties

Choose **Configure API request** from the properties panel to open the request configuration dialog box. If
an **API connector** is selected, the dialog box will include connector information.

**Method:** The method for the API call. Possible values are as follows:

- `DELETE`: Deletes a specified resource.
- `GET`: Retrieves information or data.
- `HEAD`: Retrieves only the headers of a response without the body.
- `POST`: Submits data to be processed.
- `PUSH`: Submits data to be processed.
- `PATCH`: Partially updates a specified resource.

**Path:** The relative path to the resource.

**Headers:** Any headers in the form of key-value pairs to be sent with the API request.
If a connector is selected, its configured headers will
be automatically added and cannot be removed. The configured headers cannot be edited, but you can override them by adding another header
with the same name.

**Query parameters:** Any query parameters in the form of key-value pairs to be sent with the API request.
If a connector is selected, its configured query parameters will
be automatically added and cannot be edited or removed.

**Body:** Information to be sent with the API request in JSON format. There is no body for `GET` requests.

#### Mocked output

Actions do not interact with external services or resources in the preview environment. The **Mocked output**
field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes.
This snippet is stored in the action's `results` map, just like the connector response would be for a published app
in the live environment.

With this field, you can test various scenarios and their impact on other actions within the
automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with
external services through connectors.

## Invoke AWS

Invokes an operation from an AWS service. This is a general action for calling AWS services or operations, and
should be used if there is not a dedicated action for the desired AWS service or operation.

### Properties

#### Service

The AWS service which contains the operation to be run.

#### Operation

The operation to be run.

#### Connector

The connector to be used for the operations run by this action. The configured connector should be set up with the
proper credentials to run the operation, and other configuration information, such as the AWS region that contains any
resources referenced in the operation.

#### Configuration

The JSON input to be when running the specified operation. For more information about configuring inputs for AWS operations,
see the [AWS SDK for JavaScript](../../../sdk-for-javascript.md "../../../sdk-for-javascript.md").

## Invoke Lambda

Invokes an existing Lambda function.

### Properties

#### Connector

The connector to be used for the Lambda functions run by this action. The configured connector should be set up with the
proper credentials to access the Lambda function, and other configuration information, such as the AWS region that contains the
Lambda function. For more information about configuring a connector for Lambda, see [Step 3: Create Lambda connector](connectors-lambda.md#connectors-lambda-create-connector "connectors-lambda.md#connectors-lambda-create-connector").

#### Function name

The name of the Lambda function to be run. Note that this is the function name, and not the function ARN (Amazon Resource Name).

#### Function event

Key-value pairs to be passed along to your Lambda function as the event payload.

#### Mocked output

Actions do not interact with external services or resources in the preview environment. The **Mocked output**
field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes.
This snippet is stored in the action's `results` map, just like the connector response would be for a published app
in the live environment.

With this field, you can test various scenarios and their impact on other actions within the
automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with
external services through connectors.

## Loop

Runs nested actions repeatedly to iterate through a list of items, one item at a time. For example, add the
[Create record](#automations-actions-reference-create-record "#automations-actions-reference-create-record") action to a loop action
to create multiple records.

The loop action can be nested within other loops or condition actions. The loop actions are run sequentially, and not in parallel. The
results of each action within the loop can only be accessed to subsequent actions within the same loop iteration. They cannot be accessed outside of
the loop or in different iterations of the loop.

### Properties

#### Source

The list of items to iterate through, one item at a time. The source can be the result of a previous action or a static list of strings, numbers, or objects that
you can provide using a JavaScript expression.

##### Examples

The following list contains examples of source inputs.

- Results from a previous action: `{{results.`actionName`.data}}`
- A list of numbers: `{{[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}}`
- A list of strings: `{{["apple", "banana", "orange", "grape", "kiwi"]}}`
- A computed value: `{{params.`actionName`.split("\n")}}`

#### Current item name

The name of the variable that can be used to reference the current item being iterated. The current item name is configurable so that you can nest two or more loops
and access variables from each loop. For example, if you are looping through countries and cities with two loops, you could configure and reference `currentCountry`
and `currentCity`.

## Condition

Runs actions based on the result of one or more specified logical conditions that are evaluated when the automation is run. The condition action
is made up of the following components:

- A _condition_ field, which is used to provide a JavaScript expression that evaluates to `true` or `false`.
- A _true branch_, which contains actions that are run if the condition evalutes to `true`.
- A _false branch_, which contains actions that are run if the condition evalutes to `false`.

Add actions to the true and false branches by dragging them into the condition action.

### Properties

#### Condition

The JavaScript expression to be evaluated when the action is run.

## Create record

Creates one record in an existing App Studio entity.

### Properties

#### Entity

The entity in which a record is to be created. Once an entity is selected, values must be added to the
entity's fields for the record to be created. The types of the fields, and if the fields are required or optional are defined
in the entity.

## Update record

Updates an existing record in an App Studio entity.

### Properties

#### Entity

The entity that contains the records to be updated.

#### Conditions

The criteria that defines which records are updated by the action. You can group conditions to create one logical statement.
You can combine groups or conditions with `AND` or `OR` statements.

#### Fields

The fields to be updated in the records specified by the conditions.

#### Values

The values to be updated in the specified fields.

## Delete record

Deletes a record from an App Studio entity.

### Properties

#### Entity

The entity that contains the records to be deleted.

#### Conditions

The criteria that defines which records are deleted by the action. You can group conditions to create one logic statement.
You can combine groups or conditions with `AND` or `OR` statements.

## Invoke data action

Runs a data action with optional parameters.

### Properties

#### Data action

The data action to be run by the action.

#### Parameters

Data action parameters to be used by the data action. Data action parameters are used to send values that are used as inputs
for data actions. Data action parameters can be added when configuring the automation action, but must be edited in the **Data** tab.

#### Advanced settings

The `Invoke data action` action contains the following advanced settings:

- **Page size:** The maximum number of records to fetch in each query. The default value is 500, and the maximum value is 3000.
- **Pagination token:** The token used to fetch additional records from a query. For example, if the `Page size` is
  set to 500, but there are more than 500 records, passing the pagination token to a subsequent query will fetch the next 500. The token will be undefined if
  no more records or pages exist.

## Amazon S3: Put object

Uses the `Amazon S3 PutObject` operation to add an object identified by a key (file path) to a specified Amazon S3 bucket.

### Properties

#### Connector

The connector to be used for the operations run by this action. The configured connector should be set up with the
appropriate credentials to run the operation, and other configuration information, such as the AWS region that contains any
resources referenced in the operation.

#### Configuration

The required options to be used in the `PutObject` command. The options are as follows:

###### Note

For more information about the `Amazon S3 PutObject` operation, see
[PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md") in the _Amazon Simple Storage Service API Reference_.

- **Bucket:** The name of the Amazon S3 bucket in which to put an object.
- **Key:** The unique name of the object to be put into the Amazon S3 bucket.
- **Body:** The content of the object to be put into the Amazon S3 bucket.

#### Mocked output

Actions do not interact with external services or resources in the preview environment. The **Mocked output**
field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes.
This snippet is stored in the action's `results` map, just like the connector response would be for a published app
in the live environment.

With this field, you can test various scenarios and their impact on other actions within the
automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with
external services through connectors.

## Amazon S3: Delete object

Uses the `Amazon S3 DeleteObject` operation to delete an object identified by a key (file path) from a specified Amazon S3 bucket.

### Properties

#### Connector

The connector to be used for the operations run by this action. The configured connector should be set up with the
proper credentials to run the operation, and other configuration information, such as the AWS region that contains any
resources referenced in the operation.

#### Configuration

The required options to be used in the `DeleteObject` command. The options are as follows:

###### Note

For more information about the `Amazon S3 DeleteObject` operation, see
[DeleteObject](../../../AmazonS3/latest/API/API_DeleteObject.md "../../../AmazonS3/latest/API/API_DeleteObject.md") in the _Amazon Simple Storage Service API Reference_.

- **Bucket:** The name of the Amazon S3 bucket from which to delete an object.
- **Key:** The unique name of the object to be deleted from the Amazon S3 bucket.

#### Mocked output

Actions do not interact with external services or resources in the preview environment. The **Mocked output**
field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes.
This snippet is stored in the action's `results` map, just like the connector response would be for a published app
in the live environment.

With this field, you can test various scenarios and their impact on other actions within the
automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with
external services through connectors.

## Amazon S3: Get object

Uses the `Amazon S3 GetObject` operation to retrieve an object identified by a key (file path) from a specified Amazon S3 bucket.

### Properties

#### Connector

The connector to be used for the operations run by this action. The configured connector should be set up with the
proper credentials to run the operation, and other configuration information, such as the AWS region that contains any
resources referenced in the operation.

#### Configuration

The required options to be used in the `GetObject` command. The options are as follows:

###### Note

For more information about the `Amazon S3 GetObject` operation, see
[GetObject](../../../AmazonS3/latest/API/API_GetObject.md "../../../AmazonS3/latest/API/API_GetObject.md") in the _Amazon Simple Storage Service API Reference_.

- **Bucket:** The name of the Amazon S3 bucket from which to retrieve an object.
- **Key:** The unique name of the object to be retrieved from the Amazon S3 bucket.

#### Mocked output

Actions do not interact with external services or resources in the preview environment. The **Mocked output**
field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes.
This snippet is stored in the action's `results` map, just like the connector response would be for a published app
in the live environment.

With this field, you can test various scenarios and their impact on other actions within the
automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with
external services through connectors.

## Amazon S3: List objects

Uses the `Amazon S3 ListObjects` operation to list objects in a specified Amazon S3 bucket.

### Properties

#### Connector

The connector to be used for the operations run by this action. The configured connector should be set up with the
proper credentials to run the operation, and other configuration information, such as the AWS region that contains any
resources referenced in the operation.

#### Configuration

The required options to be used in the `ListObjects` command. The options are as follows:

###### Note

For more information about the `Amazon S3 ListObjects` operation, see
[ListObjects](../../../AmazonS3/latest/API/API_ListObjects.md "../../../AmazonS3/latest/API/API_ListObjects.md") in the _Amazon Simple Storage Service API Reference_.

- **Bucket:** The name of the Amazon S3 bucket from which to list objects.

#### Mocked output

Actions do not interact with external services or resources in the preview environment. The **Mocked output**
field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes.
This snippet is stored in the action's `results` map, just like the connector response would be for a published app
in the live environment.

With this field, you can test various scenarios and their impact on other actions within the
automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with
external services through connectors.

## Amazon Textract: Analyze document

Uses the `Amazon Textract AnalyzeDocument` operation to analyze an input document for relationships between detected items.

### Properties

#### Connector

The connector to be used for the operations run by this action. The configured connector should be set up with the
proper credentials to run the operation, and other configuration information, such as the AWS region that contains any
resources referenced in the operation.

#### Configuration

The content of the request to be used in the `AnalyzeDocument` command. The options are as follows:

###### Note

For more information about the `Amazon Textract AnalyzeDocument` operation, see
[AnalyzeDocument](../../../textract/latest/dg/API_AnalyzeDocument.md "../../../textract/latest/dg/API_AnalyzeDocument.md") in the _Amazon Textract Developer Guide_.

- **Document / S3Object / Bucket:** The name of the Amazon S3 bucket. This parameter can be left empty if a file is passed to the
  action with the **S3 upload** component.
- **Document / S3Object / Name:** The file name of the input document. This parameter can be left empty if a file is passed to the
  action with the **S3 upload** component.
- **Document / S3Object / Version:** If the Amazon S3 bucket has versioning enabled, you can specify the version of the object.
  This parameter can be left empty if a file is passed to the action with the **S3 upload** component.
- **FeatureTypes:** A list of the types of analysis to perform. Valid values are:
  `TABLES`, `FORMS`, `QUERIES`, `SIGNATURES`, and `LAYOUT`.

#### Mocked output

Actions do not interact with external services or resources in the preview environment. The **Mocked output**
field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes.
This snippet is stored in the action's `results` map, just like the connector response would be for a published app
in the live environment.

With this field, you can test various scenarios and their impact on other actions within the
automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with
external services through connectors.

## Amazon Textract: Analyze expense

Uses the `Amazon Textract AnalyzeExpense` operation to analyze an input document for financially-related relationships between text.

### Properties

#### Connector

The connector to be used for the operations run by this action. The configured connector should be set up with the
proper credentials to run the operation, and other configuration information, such as the AWS region that contains any
resources referenced in the operation.

#### Configuration

The content of the request to be used in the `AnalyzeExpense` command. The options are as follows:

###### Note

For more information about the `Amazon Textract AnalyzeExpense` operation, see
[AnalyzeExpense](../../../textract/latest/dg/API_AnalyzeExpense.md "../../../textract/latest/dg/API_AnalyzeExpense.md") in the _Amazon Textract Developer Guide_.

- **Document / S3Object / Bucket:** The name of the Amazon S3 bucket. This parameter can be left empty if a file is passed to the
  action with the **S3 upload** component.
- **Document / S3Object / Name:** The file name of the input document. This parameter can be left empty if a file is passed to the
  action with the **S3 upload** component.
- **Document / S3Object / Version:** If the Amazon S3 bucket has versioning enabled, you can specify the version of the object.
  This parameter can be left empty if a file is passed to the action with the **S3 upload** component.

#### Mocked output

Actions do not interact with external services or resources in the preview environment. The **Mocked output**
field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes.
This snippet is stored in the action's `results` map, just like the connector response would be for a published app
in the live environment.

With this field, you can test various scenarios and their impact on other actions within the
automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with
external services through connectors.

## Amazon Textract: Analyze ID

Uses the `Amazon Textract AnalyzeID` operation to analyze an identity document for relevant information.

### Properties

#### Connector

The connector to be used for the operations run by this action. The configured connector should be set up with the
proper credentials to run the operation, and other configuration information, such as the AWS region that contains any
resources referenced in the operation.

#### Configuration

The content of the request to be used in the `AnalyzeID` command. The options are as follows:

###### Note

For more information about the `Amazon Textract AnalyzeID` operation, see
[AnalyzeID](../../../textract/latest/dg/API_AnalyzeID.md "../../../textract/latest/dg/API_AnalyzeID.md") in the _Amazon Textract Developer Guide_.

- **Document / S3Object / Bucket:** The name of the Amazon S3 bucket. This parameter can be left empty if a file is passed to the
  action with the **S3 upload** component.
- **Document / S3Object / Name:** The file name of the input document. This parameter can be left empty if a file is passed to the
  action with the **S3 upload** component.
- **Document / S3Object / Version:** If the Amazon S3 bucket has versioning enabled, you can specify the version of the object.
  This parameter can be left empty if a file is passed to the action with the **S3 upload** component.

#### Mocked output

Actions do not interact with external services or resources in the preview environment. The **Mocked output**
field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes.
This snippet is stored in the action's `results` map, just like the connector response would be for a published app
in the live environment.

With this field, you can test various scenarios and their impact on other actions within the
automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with
external services through connectors.

## Amazon Textract: Detect doc text

Uses the `Amazon Textract DetectDocumentText` operation to detect lines of text and the words that make up a line of text in an input document.

### Properties

#### Connector

The connector to be used for the operations run by this action. The configured connector should be set up with the
proper credentials to run the operation, and other configuration information, such as the AWS region that contains any
resources referenced in the operation.

#### Configuration

The content of the request to be used in the `DetectDocumentText` command. The options are as follows:

###### Note

For more information about the `Amazon Textract DetectDocumentText` operation, see
[DetectDocumentText](../../../textract/latest/dg/API_DetectDocumentText.md "../../../textract/latest/dg/API_DetectDocumentText.md") in the _Amazon Textract Developer Guide_.

- **Document / S3Object / Bucket:** The name of the Amazon S3 bucket. This parameter can be left empty if a file is passed to the
  action with the **S3 upload** component.
- **Document / S3Object / Name:** The file name of the input document. This parameter can be left empty if a file is passed to the
  action with the **S3 upload** component.
- **Document / S3Object / Version:** If the Amazon S3 bucket has versioning enabled, you can specify the version of the object.
  This parameter can be left empty if a file is passed to the action with the **S3 upload** component.

#### Mocked output

Actions do not interact with external services or resources in the preview environment. The **Mocked output**
field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes.
This snippet is stored in the action's `results` map, just like the connector response would be for a published app
in the live environment.

With this field, you can test various scenarios and their impact on other actions within the
automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with
external services through connectors.

## Amazon Bedrock: GenAI Prompt

Uses the [Amazon Bedrock InvokeModel](../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md "../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md") operation to run
inference using the prompt and inference parameters provided in the action properties. The action can generate text, images, and embeddings.

### Properties

#### Connector

The connector to be used for the operations run by this action. To use this action successfully, the connector must be configured with
**Amazon Bedrock Runtime** as the service. The configured connector should be set up with the
proper credentials to run the operation, and other configuration information, such as the AWS region that contains any
resources referenced in the operation.

#### Model

The foundation model to be used by Amazon Bedrock to process the request. For more information about models in Amazon Bedrock, see
[Amazon Bedrock foundation model information](../../../bedrock/latest/userguide/foundation-models-reference.md "../../../bedrock/latest/userguide/foundation-models-reference.md") in the _Amazon Bedrock User Guide_.

#### Input type

The input type of the input send to the Amazon Bedrock model. The possible values are **Text**, **Document**, and **Image**.
If an input type is not available for selection, it is likely not supported by the configured model.

#### User prompt

The prompt to be sent to the Amazon Bedrock model to be processed to generate a response. You can enter static text, or pass in an input from another part of your application, such
as from a component using parameters, a previous action in the automation, or another automation. The following examples show how to pass in a value from a component
or previous action:

- To pass a value from a component using paramters: `{{params.`paramName`}}`
- To pass a value from a previous action: `{{results.`actionName`}}`

#### System prompt (Claude models)

The system prompt to be used by the Amazon Bedrock model when processing the request. The system prompt is used to provide context, instructions, or guidelines to Claude models.

#### Request settings

Configure various request settings and model inference parameters. You can configure the following settings:

- **Temperature**: The temperature to be used by the Amazon Bedrock model when processing the request. The temperature determines the randomness or creativity of the Bedrock model's output.
  The higher the temperature, the more creative and less analytical the response will be. Possible values are `[0-10]`.
- **Max Tokens**: Limit the length of the output of the Amazon Bedrock model.
- **TopP**: In nucleus sampling, the model computes the cumulative distribution over all the options for each subsequent token in decreasing probability order and cuts it off once it reaches a particular probability specified by the **TopP**.
  You should alter either **temperature** or **TopP**, but not both
- **Stop Sequences**: Sequences that cause the model to stop processing the request and generating output.

For more information, see
[Inference request parameters and response fields for foundation models](../../../bedrock/latest/userguide/model-parameters.md "../../../bedrock/latest/userguide/model-parameters.md") in
the _Amazon Bedrock User Guide_.

#### Stop Sequences

Enter an Amazon Bedrock Guardrail **ID** and **Version**. Guardrails are used to implement safeguards based on your use
cases and responsible AI policies. For more information, see
[Stop harmful content in models using Amazon Bedrock Guardrails](../../../bedrock/latest/userguide/guardrails.md "../../../bedrock/latest/userguide/guardrails.md") in
the _Amazon Bedrock User Guide_.

#### Mocked output

Actions do not interact with external services or resources in the preview environment. The **Mocked output**
field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes.
This snippet is stored in the action's `results` map, just like the connector response would be for a published app
in the live environment.

With this field, you can test various scenarios and their impact on other actions within the
automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with
external services through connectors.

## Amazon Bedrock: Invoke model

Uses the [Amazon Bedrock InvokeModel](../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md "../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md") operation to run
inference using the prompt and inference parameters provided in the request body. You use model inference to generate text, images, and embeddings.

### Properties

#### Connector

The connector to be used for the operations run by this action. To use this action successfully, the connector must be configured with
**Amazon Bedrock Runtime** as the service. The configured connector should be set up with the
proper credentials to run the operation, and other configuration information, such as the AWS region that contains any
resources referenced in the operation.

#### Configuration

The content of the request to be used in the `InvokeModel` command.

###### Note

For more information about the `Amazon Bedrock InvokeModel` operation, including example commands, see
[InvokeModel](../../../textract/latest/dg/API_DetectDocumentText.md "../../../textract/latest/dg/API_DetectDocumentText.md") in the _Amazon Bedrock API Reference_.

#### Mocked output

Actions do not interact with external services or resources in the preview environment. The **Mocked output**
field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes.
This snippet is stored in the action's `results` map, just like the connector response would be for a published app
in the live environment.

With this field, you can test various scenarios and their impact on other actions within the
automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with
external services through connectors.

## JavaScript

Runs a custom JavaScript function to return a specified value.

###### Important

App Studio does not support using third-party or custom JavaScript libraries.

### Properties

#### Source code

The JavaScript code snippet to be run by the action.

###### Tip

You can use AI to help generate JavaScript for you by performing the following steps:

1. Choose the expand icon to open the expanded JavaScript editor.
2. (Optional): Enable the **Modify code** toggle to modify any existing JavaScript. Otherwise, AI will replace any existing JavaScript.
3. In **Generate JavaScript**, describe what you want to do with JavaScript, for example: `Add two numbers`.
4. Choose the send icon to generate your JavaScript.

## Invoke automation

Runs a specified automation.

### Properties

#### Invoke Automation

The automation to be run by the action.

## Send email

Uses the `Amazon SES SendEmail` operation to send an email.

### Properties

#### Connector

The connector to be used for the operations run by this action. The configured connector should be set up with the
proper credentials to run the operation, and other configuration information, such as the AWS region that contains any
resources referenced in the operation.

#### Configuration

The content of the request to be used in the `SendEmail` command. The options are as follows:

###### Note

For more information about the `Amazon SES SendEmail` operation, see
[SendEmail](../../../ses/latest/APIReference-V2/API_SendEmail.md "../../../ses/latest/APIReference-V2/API_SendEmail.md")
in the _Amazon Simple Email Service API Reference_.

#### Mocked output

Actions do not interact with external services or resources in the preview environment. The **Mocked output**
field is used to provide a JSON expression that simulates the behavior of a connector in the preview environment for testing purposes.
This snippet is stored in the action's `results` map, just like the connector response would be for a published app
in the live environment.

With this field, you can test various scenarios and their impact on other actions within the
automation such as simulating different result values, error scenarios, edge cases, or unhappy paths without communicating with
external services through connectors.
