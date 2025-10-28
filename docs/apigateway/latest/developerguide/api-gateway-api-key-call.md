# Call a method using an API key

Depending on the API key source type you choose, use one of the following procedures
to use header-sourced API keys or authorizer-returned API keys in method invocation:

###### To use header-sourced API keys:

1. Create an API with desired API methods, and then deploy the API to a stage.
2. Create a new usage plan or choose an existing one. Add the deployed API stage
   to the usage plan. Attach an API key to the usage plan or choose an existing API
   key in the plan. Note the chosen API key value.
3. Set up API methods to require an API key.
4. Redeploy the API to the same stage. If you deploy the API to a new stage,
   make sure to update the usage plan to attach the new API stage.
5. Call the API using the API key. The following example curl command invokes the `GET` method on the
   `getUsers` resource of the `prod` stage of an API using an API key.

```
curl -H "X-API-Key: abcd1234" 'https://b123abcde4.execute-api.us-west-2.amazonaws.com/prod/getUsers'
```

The client can now call the API methods while supplying the `x-api-key`
header with the chosen API key as the header value. A call might look like the following:

###### To use authorizer-sourced API keys:

1. Create an API with desired API methods, and then deploy the API to a stage.
2. Create a new usage plan or choose an existing one. Add the deployed API stage
   to the usage plan. Attach an API key to the usage plan or choose an existing API
   key in the plan. Note the chosen API key value.
3. Create a token-based Lambda authorizer. Include,
   `usageIdentifierKey:`{api-key}`` as a root-level property of the
   authorization response. For instructions on creating a token-based authorizer, see [Example TOKEN authorizer
   Lambda function](apigateway-use-lambda-authorizer.md#api-gateway-lambda-authorizer-token-lambda-function-create "apigateway-use-lambda-authorizer.md#api-gateway-lambda-authorizer-token-lambda-function-create").
4. Set up API methods to require an API key and enable the Lambda authorizer on
   the methods as well.
5. Redeploy the API to the same stage. If you deploy the API to a new stage,
   make sure to update the usage plan to attach the new API stage.
   The client can now call the API key-required methods without explicitly supplying any
   API key. The authorizer-returned API key is used automatically.
