# Using environment variables in AWS AppSync

You can use environment variables to adjust your AWS AppSync resolvers' and functions' behavior
without updating your code. Environment variables are pairs of strings stored with your API
configuration that are made available to your resolvers and functions to leverage at runtime.
They're particularly useful for situations in which you must reference configuration data that's
only available during the initial setup but needs to be used by your resolvers and functions
during the run. Environment variables expose configuration data in your code, thereby reducing
the need to hard-code those values.

###### Note

To increase database security, we recommend that you use [Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") or [AWS
Systems Manager Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") instead of environment variables to store credentials or sensitive
information. To leverage this feature, see [Invoking AWS services with AWS AppSync HTTP data sources](tutorial-http-resolvers-js.md#invoking-aws-services-js "tutorial-http-resolvers-js.md#invoking-aws-services-js").

Environment variables must follow several behaviors and rules to function properly:

- Both JavaScript resolvers/functions and VTL templates support environment variables.
- Environment variables are not evaluated before function invocation.
- Environment variables **only** support string
  values.
- Any defined value in an environment variable is considered a string literal and not expanded.
- Variable evaluations should ideally be performed in the function code.

## Configuring environment variables (console)

You can configure environment variables for your AWS AppSync GraphQL API by creating the variable and defining
its key-value pair. Your resolvers and functions will use the environment variable's key name to retrieve the
value at runtime. To set environment variables in the AWS AppSync console:

1. Sign in to the AWS Management Console and open the [AppSync
   console](https://console.aws.amazon.com/appsync/ "https://console.aws.amazon.com/appsync/").
2. On the **APIs** page, choose the name of a GraphQL API.
3. On your API's homepage, in the navigation pane, choose
   **Settings**.
4. Under **Environment variables**, choose **Add environment
   variable**.
5. Choose **Add environment variable**.
6. Enter a key and value.
7. If necessary, repeat steps 5 and 6 to add more key values. If you need to remove a key value, choose the
   **Remove** option and the key(s) to remove.
8. Choose **Submit**.

###### Tip

There are a few rules you must follow when creating keys and values:

- Keys must begin with a letter.
- Keys must be at least two characters long.
- Keys can only contain letters, numbers, and the underscore character (\_).
- Values can be up to 512 characters long.
- You can configure up to 50 key-value pairs in a GraphQL API.

## Configuring environment variables (API)

To set an environment variable using APIs, you can use `PutGraphqlApiEnvironmentVariables`. The
corresponding CLI command is `put-graphql-api-environment-variables`.

To retrieve an environment variable using APIs, you can use `GetGraphqlApiEnvironmentVariables`.
The corresponding CLI command is `get-graphql-api-environment-variables`.

The command must contain the API ID and list of environment variables:

```
aws appsync put-graphql-api-environment-variables \
  --api-id "<api-id>" \
  --environment-variables '{"key1":"value1","key2":"value2", …}'
```

The following example sets two environment variables in an API with the ID of
`abcdefghijklmnopqrstuvwxyz` using the `put-graphql-api-environment-variables`
command:

```
aws appsync put-graphql-api-environment-variables \
  --api-id "`abcdefghijklmnopqrstuvwxyz`" \
  --environment-variables '{"`USER_TABLE`":"`users_prod`","`DEBUG`":"`true`"}'
```

Note that when you apply environment variables with the `put-graphql-api-environment-variables`
command, the contents of the environment variables' structure are overwritten; this means existing environment
variables will be lost. To retain existing environment variables when adding new ones, **include all existing key-value pairs** along with the new ones in your request. Using the example
above, if you wanted to add `"EMPTY":""`, you could do the following:

```
aws appsync put-graphql-api-environment-variables \
  --api-id "`abcdefghijklmnopqrstuvwxyz`" \
  --environment-variables '{"`USER_TABLE`":"`users_prod`","`DEBUG`":"`true`", "`EMPTY`":""}'
```

To retrieve the current configuration, use the `get-graphql-api-environment-variables`
command:

```
aws appsync get-graphql-api-environment-variables --api-id "<api-id>"
```

Using the example above, you could use the following command:

```
aws appsync get-graphql-api-environment-variables --api-id "`abcdefghijklmnopqrstuvwxyz`"
```

The result will show the list of environment variables along with their key
values:

```
{
    "environmentVariables": {
        "USER_TABLE": "users_prod",
        "DEBUG": "true",
        "EMPTY": ""
    }
}
```

## Configuring environment variables (CFN)

You can use the template below to create environment
variables:

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  GraphQLApiWithEnvVariables:
    Type: "AWS::AppSync::GraphQLApi"
    Properties:
      Name: "`MyApiWithEnvVars`"
      AuthenticationType: "`AWS_IAM`"
      EnvironmentVariables:
        EnvKey1: "`non-empty`"
        EnvKey2: ""
```

## environment variables and merged APIs

Environment variables defined in Source APIs are also available in your Merged APIs.
Environment variables in Merged APIs are read-only and cannot be updated. Note that your
environment variable keys must be unique across all Source APIs for your merges to succeed;
duplicate keys will always result in a merge failure.

## Retrieving environment variables

To retrieve environment variables in your function code, retrieve the value from the `ctx.env`
object in your resolvers and functions. Below are some examples of this in action.

Publishing to Amazon SNS
In this example, our HTTP resolver sends a message to an Amazon SNS topic. The ARN of the topic is only known
after the stack that defines the GraphQL API and the topic has been deployed.

```
/**
 * Sends a publish request to the SNS topic
 */
export function request(ctx) {
    const TOPIC_ARN = ctx.env.TOPIC_ARN;
    const { input: values } = ctx.args;
    // this custom function sends values to the SNS topic
    return publishToSNSRequest(TOPIC_ARN, values);
}
```

Transactions with DynamoDB
In this example, the names of the DynamoDB table are different if the API is deployed for staging or is
already in production. The resolver code doesn't need to change. The values of the environment variables are
updated based on where the API is deployed.

```
import { util } from '@aws-appsync/utils';
export function request(ctx) {
  const { authorId, postId } = ctx.args;
  return {
    operation: 'TransactWriteItems',
    transactItems: [
      {
        table: ctx.env.POST_TABLE,
        operation: 'PutItem',
        key: util.dynamodb.toMapValues({ postId }),
        // rest of the configuration
      },
      {
        table: ctx.env.AUTHOR_TABLE,
        operation: 'UpdateItem',
        key: util.dynamodb.toMapValues({ authorId }),
        // rest of the configuration
      },
    ],
  };
}
```
