# Set up a

WebSocket API integration request in API Gateway

Setting up an integration request involves the following:

- Choosing a route key to integrate to the backend.
- Specifying the backend endpoint to invoke. WebSocket APIs support the following integration types:

      + `AWS_PROXY`
      + `AWS`
      + `HTTP_PROXY`
      + `HTTP`
      + `MOCK`

  For more information about integration types, see
  [IntegrationType](../../../apigatewayv2/latest/api-reference/apis-apiid-integrations-integrationid.md#apis-apiid-integrations-integrationid-prop-integration-integrationtype "../../../apigatewayv2/latest/api-reference/apis-apiid-integrations-integrationid.md#apis-apiid-integrations-integrationid-prop-integration-integrationtype") in the API
  Gateway V2 REST API.

- Configuring how to transform the route request data, if necessary, into
  integration request data by specifying one or more request templates.

## Set up

a WebSocket API integration request using the API Gateway console

###### To add an integration request to a route in a WebSocket API using the API Gateway

console

1. Sign in to the API Gateway console, choose the API, and choose
   **Routes**.
2. Under **Routes**, choose the route.
3. Choose the
   **Integration request** tab, and then in the **Integration request settings** section, choose **Edit**.
4. For **Integration type**, select one of the
   following:
   - Choose **Lambda function** only if your API will
     be integrated with an AWS Lambda function that you have already
     created in this account or in another account.

   To create a new Lambda function in AWS Lambda, to set a resource
   permission on the Lambda function, or to perform any other Lambda
   service actions, choose **AWS Service**
   instead.
   - Choose **HTTP** if your API will be integrated
     with an existing HTTP endpoint. For more information, see [HTTP integrations for REST APIs in API Gateway](setup-http-integrations.md "setup-http-integrations.md").
   - Choose **Mock** if you want to generate API
     responses from API Gateway directly, without the need for an integration
     backend. For more information, see [Mock integrations for REST APIs in API Gateway](how-to-mock-integration.md "how-to-mock-integration.md").
   - Choose **AWS service** if your API will be
     integrated with an AWS service.
   - Choose **VPC link** if your API will use a
     `VpcLink` as a private integration endpoint. For more
     information, see [Private integrations for REST APIs in API Gateway](set-up-private-integration.md "set-up-private-integration.md").

5. If you chose **Lambda function**, do the following:
   1. For **Use Lambda proxy integration**, choose the
      check box if you intend to use [Lambda proxy
      integration](set-up-lambda-proxy-integrations.md#api-gateway-create-api-as-simple-proxy "set-up-lambda-proxy-integrations.md#api-gateway-create-api-as-simple-proxy") or [cross-account Lambda proxy integration](apigateway-cross-account-lambda-integrations.md "apigateway-cross-account-lambda-integrations.md").
   2. For **Lambda function**, specify the function in
      one of the following ways:
      - If your Lambda function is in the same account, enter
        the function name and then select the function from
        the dropdown list.

      ###### Note

      The function name can optionally include its alias or
      version specification, as in `HelloWorld`,
      `HelloWorld:1`, or
      `HelloWorld:alpha`.
      - If the function is in a different account, enter the ARN
        for the function.

   3. To use the default timeout value of 29 seconds, keep
      **Default timeout** turned on. To
      set a custom timeout, choose **Default timeout** and enter a timeout value
      between `50` and `29000` milliseconds.

6. If you chose **HTTP**, follow the instructions in step 4
   of [Set up an API integration request
   using the API Gateway console](how-to-method-settings-console.md "how-to-method-settings-console.md").
7. If you chose **Mock**, proceed to the **Request
   Templates** step.
8. If you chose **AWS service**, follow the instructions
   in step 6 of [Set up an API integration request
   using the API Gateway console](how-to-method-settings-console.md "how-to-method-settings-console.md").
9. If you chose **VPC link**, do the following:
   1. For **VPC proxy integration**, choose the check
      box if you want your requests to be proxied to your
      `VPCLink`'s endpoint.
   2. For **HTTP method**, choose the HTTP method type
      that most closely matches the method in the HTTP backend.
   3. From the **VPC link** dropdown list, select a VPC link. You can select
      `[Use Stage Variables]` and enter
      `${stageVariables.vpcLinkId}` in the text box below
      the list.

   You can define the `vpcLinkId` stage variable after
   deploying the API to a stage and set its value to the ID of the
   `VpcLink`. 4. For **Endpoint URL**, enter the URL of the HTTP
   backend you want this integration to use. 5. To use the default timeout value of 29 seconds, keep
   **Default timeout** turned on. To
   set a custom timeout, choose **Default timeout** and enter a timeout value
   between `50` and `29000` milliseconds.

10. Choose **Save changes**.
11. Under **Request templates**, do the following:
    1. To enter a **Template selection expression**, under **Request templates**, choose **Edit**.
    2. Enter a **Template selection expression**. Use an expression that API Gateway
       looks for in the message payload. If it is found, it is evaluated,
       and the result is a template key value that is used to select the
       data mapping template to be applied to the data in the message
       payload. You create the data mapping template in the next step. Choose **Edit** to save your changes.
    3. Choose **Create template** to create the data mapping template. For **Template key**, enter a template key value that is used to select the data mapping template to be applied to the data in the message
       payload. Then, enter a mapping template. Choose **Create template**.

    For information about template selection expressions, see [Template
    selection expressions](websocket-api-data-transformations.md#apigateway-websocket-api-template-selection-expressions "websocket-api-data-transformations.md#apigateway-websocket-api-template-selection-expressions").

## Set up

an integration request using the AWS CLI

You can set up an integration request for a route in a WebSocket API by using the
AWS CLI as in the following example, which creates a mock integration:

1. Create a file named `integration-params.json`, with the
   following contents:

```
{"PassthroughBehavior": "WHEN_NO_MATCH", "TimeoutInMillis": 29000, "ConnectionType": "INTERNET", "RequestTemplates": {"application/json": "{\"statusCode\":200}"}, "IntegrationType": "MOCK"}
```

2. Use the following [create-integration](../../../cli/latest/reference/apigatewayv2/create-integration.md "../../../cli/latest/reference/apigatewayv2/create-integration.md") command to create the mock integration.

```
aws apigatewayv2 --region us-east-1 create-integration --api-id aabbccddee --cli-input-json file://integration-params.json
```

The output will look like the following:

```
{
    "PassthroughBehavior": "WHEN_NO_MATCH",
    "TimeoutInMillis": 29000,
    "ConnectionType": "INTERNET",
    "IntegrationResponseSelectionExpression": "${response.statuscode}",
    "RequestTemplates": {
        "application/json": "{\"statusCode\":200}"
    },
    "IntegrationId": "0abcdef",
    "IntegrationType": "MOCK"
}
```

Alternatively, you can set up an integration request for a proxy integration by
using the AWS CLI.

1. Create a Lambda function in the Lambda console and give it a basic Lambda
   execution role.
2. Use the following
   [create-integration](../../../cli/latest/reference/apigatewayv2/create-integration.md "../../../cli/latest/reference/apigatewayv2/create-integration.md") command to create the integration.

```
aws apigatewayv2 create-integration --api-id `aabbccddee` --integration-type AWS_PROXY --integration-method POST --integration-uri arn:aws:apigateway:`us-east-1`:lambda:path/2015-03-31/functions/arn:aws:lambda:`us-east-1`:`123412341234`:function:`simpleproxy-echo-e2e`/invocations
```

The output will look like the following:

```
{
    "PassthroughBehavior": "WHEN_NO_MATCH",
    "IntegrationMethod": "POST",
    "TimeoutInMillis": 29000,
    "ConnectionType": "INTERNET",
    "IntegrationUri": "arn:aws:apigateway:`us-east-1`:lambda:path/2015-03-31/functions/arn:aws:lambda:`us-east-1`:`123412341234`:function:`simpleproxy-echo-e2e`/invocations",
    "IntegrationId": "`abcdefg`",
    "IntegrationType": "AWS_PROXY"
}
```

## Input format of a

Lambda function for proxy integration for WebSocket APIs

In Lambda proxy integration, API Gateway maps the entire client request to the input `event` parameter
of the backend Lambda function. The following example shows the structure of the input event from the
`$connect` route and the input event from the `$disconnect` route that API Gateway sends to a
Lambda proxy integration.

Input from the $connect route

```
{
    headers: {
      Host: 'abcd123.execute-api.us-east-1.amazonaws.com',
      'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
      'Sec-WebSocket-Key': '...',
      'Sec-WebSocket-Version': '13',
      'X-Amzn-Trace-Id': '...',
      'X-Forwarded-For': '192.0.2.1',
      'X-Forwarded-Port': '443',
      'X-Forwarded-Proto': 'https'
    },
    multiValueHeaders: {
      Host: [ 'abcd123.execute-api.us-east-1.amazonaws.com' ],
      'Sec-WebSocket-Extensions': [ 'permessage-deflate; client_max_window_bits' ],
      'Sec-WebSocket-Key': [ '...' ],
      'Sec-WebSocket-Version': [ '13' ],
      'X-Amzn-Trace-Id': [ '...' ],
      'X-Forwarded-For': [ '192.0.2.1' ],
      'X-Forwarded-Port': [ '443' ],
      'X-Forwarded-Proto': [ 'https' ]
    },
    requestContext: {
      routeKey: '$connect',
      eventType: 'CONNECT',
      extendedRequestId: 'ABCD1234=',
      requestTime: '09/Feb/2024:18:11:43 +0000',
      messageDirection: 'IN',
      stage: 'prod',
      connectedAt: 1707502303419,
      requestTimeEpoch: 1707502303420,
      identity: { sourceIp: '192.0.2.1' },
      requestId: 'ABCD1234=',
      domainName: 'abcd1234.execute-api.us-east-1.amazonaws.com',
      connectionId: 'AAAA1234=',
      apiId: 'abcd1234'
    },
    isBase64Encoded: false
  }

```

Input from the $disconnect route

```
{
    headers: {
      Host: 'abcd1234.execute-api.us-east-1.amazonaws.com',
      'x-api-key': '',
      'X-Forwarded-For': '',
      'x-restapi': ''
    },
    multiValueHeaders: {
      Host: [ 'abcd1234.execute-api.us-east-1.amazonaws.com' ],
      'x-api-key': [ '' ],
      'X-Forwarded-For': [ '' ],
      'x-restapi': [ '' ]
    },
    requestContext: {
      routeKey: '$disconnect',
      disconnectStatusCode: 1005,
      eventType: 'DISCONNECT',
      extendedRequestId: 'ABCD1234=',
      requestTime: '09/Feb/2024:18:23:28 +0000',
      messageDirection: 'IN',
      disconnectReason: 'Client-side close frame status not set',
      stage: 'prod',
      connectedAt: 1707503007396,
      requestTimeEpoch: 1707503008941,
      identity: { sourceIp: '192.0.2.1' },
      requestId: 'ABCD1234=',
      domainName: 'abcd1234.execute-api.us-east-1.amazonaws.com',
      connectionId: 'AAAA1234=',
      apiId: 'abcd1234'
    },
    isBase64Encoded: false
  }

```
