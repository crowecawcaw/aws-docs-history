# Tutorial: Create a REST API with a Lambda proxy

integration

[Lambda proxy integration](set-up-lambda-proxy-integrations.md "set-up-lambda-proxy-integrations.md") is a
lightweight, flexible API Gateway API integration type that allows you to integrate an API method
– or an entire API – with a Lambda function. The Lambda function can be written
in [any language that Lambda supports](../../../lambda/latest/dg/lambda-runtimes.md "../../../lambda/latest/dg/lambda-runtimes.md").
Because it's a proxy integration, you can change the Lambda function implementation at any
time without needing to redeploy your API.

In this tutorial, you do the following:

- Create a "Hello, World!" Lambda function to be the backend for the API.
- Create and test a "Hello, World!" API with Lambda proxy integration.

###### Topics

- [Create a "Hello,
  World!" Lambda function](#api-gateway-proxy-integration-create-lambda-backend "#api-gateway-proxy-integration-create-lambda-backend")
- [Create a
  "Hello, World!" API](#api-gateway-create-api-as-simple-proxy-for-lambda-build "#api-gateway-create-api-as-simple-proxy-for-lambda-build")
- [Deploy and test
  the API](#api-gateway-create-api-as-simple-proxy-for-lambda-test "#api-gateway-create-api-as-simple-proxy-for-lambda-test")

## Create a "Hello,

World!" Lambda function

###### To create a "Hello, World!" Lambda function in the Lambda console

1. Sign in to the Lambda console at [https://console.aws.amazon.com/lambda](https://console.aws.amazon.com/lambda "https://console.aws.amazon.com/lambda").
2. On the AWS navigation bar, choose an [AWS Region](../../../general/latest/gr/apigateway.md "../../../general/latest/gr/apigateway.md").

###### Note

Note the region where you create the Lambda function. You'll need it when
you create the API. 3. Choose **Functions** in the navigation pane. 4. Choose **Create function**. 5. Choose **Author from scratch**. 6. Under **Basic information**, do the following:

    1. In **Function name**, enter
     `GetStartedLambdaProxyIntegration`.
    2. For **Runtime**, choose either the latest supported **Node.js** or
     **Python** runtime.
    3. For **Architecture**, keep the default setting.
    4. Under **Permissions**, expand **Change default execution role**. For **Execution
     role** dropdown list, choose **Create new role from
     AWS policy templates**.
    5. In **Role name**, enter
     `GetStartedLambdaBasicExecutionRole`.
    6. Leave the **Policy templates** field blank.
    7. Choose **Create function**.

7. Under **Function code**, in the inline code editor,
   copy/paste the following code:

Node.js

```
export const handler = async(event, context) => {
    console.log('Received event:', JSON.stringify(event, null, 2));
    var res ={
        "statusCode": 200,
        "headers": {
            "Content-Type": "*/*"
        }
    };
    var greeter = 'World';
    if (event.greeter && event.greeter!=="") {
        greeter =  event.greeter;
    } else if (event.body && event.body !== "") {
        var body = JSON.parse(event.body);
        if (body.greeter && body.greeter !== "") {
            greeter = body.greeter;
        }
    } else if (event.queryStringParameters && event.queryStringParameters.greeter && event.queryStringParameters.greeter !== "") {
        greeter = event.queryStringParameters.greeter;
    } else if (event.multiValueHeaders && event.multiValueHeaders.greeter && event.multiValueHeaders.greeter != "") {
        greeter = event.multiValueHeaders.greeter.join(" and ");
    } else if (event.headers && event.headers.greeter && event.headers.greeter != "") {
        greeter = event.headers.greeter;
    }
    res.body = "Hello, " + greeter + "!";
    return res
};
```

Python

```
import json


def lambda_handler(event, context):
    print(event)

    greeter = 'World'

    try:
        if (event['queryStringParameters']) and (event['queryStringParameters']['greeter']) and (
                event['queryStringParameters']['greeter'] is not None):
            greeter = event['queryStringParameters']['greeter']
    except KeyError:
        print('No greeter')

    try:
        if (event['multiValueHeaders']) and (event['multiValueHeaders']['greeter']) and (
                event['multiValueHeaders']['greeter'] is not None):
            greeter = " and ".join(event['multiValueHeaders']['greeter'])
    except KeyError:
        print('No greeter')

    try:
        if (event['headers']) and (event['headers']['greeter']) and (
                event['headers']['greeter'] is not None):
            greeter = event['headers']['greeter']
    except KeyError:
        print('No greeter')

    if (event['body']) and (event['body'] is not None):
        body = json.loads(event['body'])
        try:
            if (body['greeter']) and (body['greeter'] is not None):
                greeter = body['greeter']
        except KeyError:
            print('No greeter')

    res = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "*/*"
        },
        "body": "Hello, " + greeter + "!"
    }

    return res
```

8. Choose **Deploy**.

## Create a

"Hello, World!" API

Now create an API for your "Hello, World!" Lambda function by using the API Gateway
console.

###### To create a "Hello, World!" API

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway "https://console.aws.amazon.com/apigateway").
2. If this is your first time using API Gateway, you see a page that introduces you to
   the features of the service. Under **REST API**, choose **Build**. When the
   **Create Example API** popup appears, choose
   **OK**.

If this is not your first time using API Gateway, choose **Create
API**. Under **REST API**, choose **Build**. 3. For **API name**, enter `LambdaProxyAPI`. 4. (Optional) For **Description**, enter a description. 5. Keep **API endpoint type** set to **Regional**. 6. For **IP address type**, select **IPv4**. 7. Choose **Create API**.

After you create an API, you create a resource. Typically, API resources are organized in a resource tree
according to the application logic. For this example, you create a **/helloworld** resource.

###### To create a resource

1. Choose **Create resource**.
2. Keep **Proxy resource** turned off.
3. Keep **Resource path** as `/`.
4. For **Resource name**, enter `helloworld`.
5. Keep **CORS (Cross Origin Resource Sharing)** turned off.
6. Choose **Create resource**.

In a proxy integration, the entire request is sent to the backend Lambda
function as-is, via a catch-all `ANY` method that represents any HTTP
method. The actual HTTP method is specified by the client at run time. The
`ANY` method allows you to use a single API method setup for all
of the supported HTTP methods: `DELETE`, `GET`,
`HEAD`, `OPTIONS`, `PATCH`,
`POST`, and `PUT`.

###### To create an `ANY` method

1. Select the **/helloworld** resource, and then choose **Create method**.
2. For **Method type**, select **ANY**.
3. For **Integration type**, select **Lambda function**.
4. Turn on **Lambda proxy integration**.
5. For **Lambda function**, select the AWS Region where you created your Lambda
   function, and then enter the function name.
6. To use the default timeout value of 29 seconds, keep
   **Default timeout** turned on. To
   set a custom timeout, choose **Default timeout** and enter a timeout value
   between `50` and `29000` milliseconds.
7. Choose **Create method**.

## Deploy and test

the API

###### To deploy your API

1. Choose **Deploy API**.
2. For **Stage**, select **New stage**.
3. For **Stage name**, enter `test`.
4. (Optional) For **Description**, enter a description.
5. Choose **Deploy**.
6. Under **Stage details**, choose the copy icon to copy your API's invoke URL.

### Use

browser and cURL to test an API with Lambda proxy integration

You can use a browser or [cURL](https://curl.se/ "https://curl.se/") to test
your API.

To test `GET` requests using only query string parameters, you can enter the URL for the API's
`helloworld` resource into a browser address bar.

To create the URL for the API's `helloworld` resource, append the resource `helloworld` and the query string parameter `?greeter=John` to your invoke URL. Your URL should look like the following.

```
https://`r275xc9bmd`.execute-api.`us-east-1`.amazonaws.com/test/helloworld?greeter=John
```

For other methods, you must use more advanced REST API testing utilities, such as
[POSTMAN](https://www.postman.com/ "https://www.postman.com/") or [cURL](https://curl.se/ "https://curl.se/"). This tutorial uses cURL. The cURL
command examples below assume that cURL is installed on your computer.

###### To test your deployed API using cURL:

1. Open a terminal window.
2. Copy the following cURL command and paste it into the terminal window, and replace the invoke URL with the one you copied in the previous step and add `/helloworld` to the end of the URL.

###### Note

If you're running the command on Windows, use this syntax
instead:

```
curl -v -X POST "https://`r275xc9bmd`.execute-api.`us-east-1`.amazonaws.com/test/helloworld" -H "content-type: application/json" -d "{ \"greeter\": \"John\" }"
```

    1. To call the API with the query string parameter of
     `?greeter=John`:



    ```
    curl -X GET 'https://`r275xc9bmd`.execute-api.`us-east-1`.amazonaws.com/test/helloworld?greeter=John'
    ```
    2. To call the API with a header parameter of
     `greeter:John`:



    ```
    curl -X GET https://`r275xc9bmd`.execute-api.`us-east-1`.amazonaws.com/test/helloworld \
      -H 'content-type: application/json' \
      -H 'greeter: John'
    ```
    3. To call the API with a body of `{"greeter":"John"}`:



    ```
    curl -X POST https://`r275xc9bmd`.execute-api.`us-east-1`.amazonaws.com/test/helloworld \
      -H 'content-type: application/json' \
      -d '{ "greeter": "John" }'
    ```In all the cases, the output is a 200 response with the following response

body:

```
Hello, John!
```
