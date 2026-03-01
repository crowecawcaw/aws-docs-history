# Disabling VTL mapping templates with direct Lambda resolvers (VTL)

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please consider using the APPSYNC_JS
runtime and its guides [here](configuring-resolvers-js.md "configuring-resolvers-js.md").

With direct Lambda resolvers, you can circumvent the use of VTL mapping templates when using AWS Lambda data
sources. AWS AppSync can provide a default payload to your Lambda function as well as a default translation from a
Lambda function's response to a GraphQL type. You can choose to provide a request template, a response template, or
neither and AWS AppSync will handle it accordingly.

To learn more about the default request payload and response translation that AWS AppSync provides, see the
[Direct Lambda resolver reference](resolver-mapping-template-reference-lambda.md#direct-lambda-resolvers "resolver-mapping-template-reference-lambda.md#direct-lambda-resolvers"). For more information on setting up
an AWS Lambda data source and setting up an IAM Trust Policy, see [Attaching a
data source](attaching-a-data-source.md "attaching-a-data-source.md").

## Configure direct Lambda resolvers

The following sections will show you how to attach Lambda data sources and add Lambda resolvers to your
fields.

### Add a Lambda data source

Before you can activate direct Lambda resolvers, you must add a Lambda data source.

Console

1. Sign in to the AWS Management Console and open the [AppSync
   console](https://console.aws.amazon.com/appsync/ "https://console.aws.amazon.com/appsync/").
   1. In the **APIs dashboard**, choose your GraphQL API.
   2. In the **Sidebar**, choose **Data
      sources**.

2. Choose **Create data source**.
   1. For **Data source name**, enter a name for your data source, such as
      `myFunction`.
   2. For **Data source type**, choose **AWS Lambda
      function**.
   3. For **Region**, choose the appropriate region.
   4. For **Function ARN**, choose the Lambda function from the dropdown list. You
      can search for the function name or manually enter the ARN of the function you want to use.
   5. Create a new IAM role (recommended) or choose an existing role that has the
      `lambda:invokeFunction` IAM permission. Existing roles need a trust policy, as
      explained in the [Attaching a data source](attaching-a-data-source.md "attaching-a-data-source.md") section.

   The following is an example IAM policy that has the required permissions to perform operations
   on the resource:

   JSONJSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [ "lambda:invokeFunction" ],
    "Resource": [
    "arn:aws:lambda:us-west-2:123456789012:function:myFunction",
    "arn:aws:lambda:us-west-2:123456789012:function:myFunction:*"
    ]
    }
    ]
    }`

   ```

3. Choose the **Create** button.

CLI

1. Create a data source object by running the [`create-data-source`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-data-source.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-data-source.html") command.

You'll need to type in 4 parameters for this particular command:

    1. The `api-id` of your API.
    2. The `name` of your data source. In the console example, this is the **Data
     source name**.
    3. The `type` of data source. In the console example, this is **AWS Lambda function**.
    4. The `lambda-config`, which is the **Function ARN** in the console
     example.

###### Note

There are other parameters such as `Region` that must be configured but will usually
default to your CLI configuration values.

An example command may look like this:

```
aws appsync create-data-source --api-id abcdefghijklmnopqrstuvwxyz --name myFunction --type AWS_LAMBDA --lambda-config lambdaFunctionArn=arn:aws:lambda:us-west-2:102847592837:function:appsync-lambda-example
```

An output will be returned in the CLI. Here's an example:

```
{
    "dataSource": {
        "dataSourceArn": "arn:aws:appsync:us-west-2:102847592837:apis/abcdefghijklmnopqrstuvwxyz/datasources/myFunction",
        "type": "AWS_LAMBDA",
        "name": "myFunction",
        "lambdaConfig": {
            "lambdaFunctionArn": "arn:aws:lambda:us-west-2:102847592837:function:appsync-lambda-example"
        }
    }
}
```

2. To modify a data source's attributes, run the [`update-data-source`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-data-source.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-data-source.html") command.

With the exception of the `api-id` parameter, the parameters used in the
`create-data-source` command will be overwritten by the new values from the
`update-data-source` command.

### Activate direct Lambda resolvers

After creating a Lambda data source and setting up the appropriate IAM role to allow AWS AppSync to invoke
the function, you can link it to a resolver or pipeline function.

Console

1. Sign in to the AWS Management Console and open the [AppSync
   console](https://console.aws.amazon.com/appsync/ "https://console.aws.amazon.com/appsync/").
   1. In the **APIs dashboard**, choose your GraphQL API.
   2. In the **Sidebar**, choose **Schema**.

2. In the **Resolvers** window, choose a field or operation and then select the
   **Attach** button.
3. In the **Create new resolver** page, choose the Lambda function from the dropdown
   list.
4. In order to leverage direct Lambda resolvers, confirm that request and response mapping templates
   are disabled in the **Configure mapping templates** section.
5. Choose the **Save Resolver** button.

CLI

- Create a resolver by running the [`create-resolver`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-resolver.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-resolver.html") command.

You'll need to type in 6 parameters for this particular command:

    1. The `api-id` of your API.
    2. The `type-name` of the type in your schema.
    3. The `field-name` of the field in your schema.
    4. The `data-source-name`, or your Lambda function's name.
    5. The `request-mapping-template`, which is the body of the request. In the console
     example, this was disabled:



    ```
    " "
    ```
    6. The `response-mapping-template`, which is the body of the response. In the console
     example, this was also disabled:



    ```
    " "
    ```

An example command may look like this:

```
aws appsync create-resolver --api-id abcdefghijklmnopqrstuvwxyz --type-name Subscription --field-name onCreateTodo --data-source-name LambdaTest --request-mapping-template " " --response-mapping-template " "
```

An output will be returned in the CLI. Here's an example:

```
{
    "resolver": {
        "resolverArn": "arn:aws:appsync:us-west-2:102847592837:apis/abcdefghijklmnopqrstuvwxyz/types/Subscription/resolvers/onCreateTodo",
        "typeName": "Subscription",
        "kind": "UNIT",
        "fieldName": "onCreateTodo",
        "dataSourceName": "LambdaTest"
    }
}
```

When you disable your mapping templates, there are several additional behaviors that will occur in
AWS AppSync:

- By disabling a mapping template, you are signalling to AWS AppSync that you accept the default data
  translations specified in the [Direct Lambda resolver
  reference](resolver-mapping-template-reference-lambda.md#direct-lambda-resolvers "resolver-mapping-template-reference-lambda.md#direct-lambda-resolvers").
- By disabling the request mapping template, your Lambda data source will receive a payload consisting of
  the entire [Context](resolver-context-reference.md "resolver-context-reference.md") object.
- By disabling the response mapping template, the result of your Lambda invocation will be translated
  depending on the version of the request mapping template or if the request mapping template is also
  disabled.
