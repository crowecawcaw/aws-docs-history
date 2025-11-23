# Creating and managing Lambda function URLs

A function URL is a dedicated HTTP(S) endpoint for your Lambda function. You can create and configure a function URL through the Lambda console or the Lambda API.

###### Tip

Lambda offers two ways to invoke your function through an HTTP endpoint: function URLs and Amazon API Gateway. If you're not sure which is the best method for your
use case, see [Select a method to invoke your Lambda function using an HTTP request](furls-http-invoke-decision.md "furls-http-invoke-decision.md").

When you create a function URL, Lambda automatically generates a unique URL endpoint for you. Once you create a function URL, its URL endpoint never changes. Function
URL endpoints have the following format:

```
https://`<url-id>`.lambda-url.<region>.on.aws
```

###### Note

Function URLs are not supported in the following AWS Regions: Asia Pacific (Hyderabad) (`ap-south-2`), Asia Pacific (Melbourne) (`ap-southeast-4`), Asia Pacific (Malaysia) (`ap-southeast-5`), Asia Pacific (New Zealand) (`ap-southeast-6`), Asia Pacific (Thailand) (`ap-southeast-7`), Asia Pacific (Taipei) (`ap-east-2`), Canada West (Calgary) (`ca-west-1`), Europe (Spain) (`eu-south-2`), Europe (Zurich) (`eu-central-2`), Israel (Tel Aviv) (`il-central-1`), and Middle East (UAE) (`me-central-1`).

Function URLs are dual stack-enabled, supporting IPv4 and IPv6. After you configure a function URL for your
function, you can invoke your function through its HTTP(S) endpoint via a web browser, curl, Postman, or any HTTP
client.

###### Note

You can access your function URL through the public Internet only. While Lambda functions do support
AWS PrivateLink, function URLs do not.

Lambda function URLs use [resource-based policies](access-control-resource-based.md "access-control-resource-based.md") for
security and access control. Function URLs also support cross-origin resource sharing (CORS) configuration
options.

You can apply function URLs to any function alias, or to the `$LATEST` unpublished function version.
You can't add a function URL to any other function version.

The following section show how to create and manage a function URL using the Lambda console, AWS CLI, and CloudFormation template

###### Topics

- [Creating a function URL (console)](#create-url-console "#create-url-console")
- [Creating a function URL (AWS CLI)](#create-url-cli "#create-url-cli")
- [Adding a function URL to a CloudFormation template](#urls-cfn "#urls-cfn")
- [Cross-origin resource sharing (CORS)](#urls-cors "#urls-cors")
- [Throttling function URLs](#urls-throttling "#urls-throttling")
- [Deactivating function URLs](#urls-deactivating "#urls-deactivating")
- [Deleting function URLs](#w2aac31c75c53 "#w2aac31c75c53")
- [Control access to Lambda function URLs](urls-auth.md "urls-auth.md")
- [Invoking Lambda function URLs](urls-invocation.md "urls-invocation.md")
- [Monitoring Lambda function URLs](urls-monitoring.md "urls-monitoring.md")
- [Select a method to invoke your Lambda function using an HTTP request](furls-http-invoke-decision.md "furls-http-invoke-decision.md")
- [Tutorial: Creating a webhook endpoint using a Lambda function URL](urls-webhook-tutorial.md "urls-webhook-tutorial.md")

## Creating a function URL (console)

Follow these steps to create a function URL using the console.

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Choose the name of the function that you want to create the function URL for.
3. Choose the **Configuration** tab, and then choose **Function
   URL**.
4. Choose **Create function URL**.
5. For **Auth type**, choose **AWS_IAM** or
   **NONE**. For more information about function URL authentication, see [Access control](urls-auth.md "urls-auth.md").
6. (Optional) Select **Configure cross-origin resource sharing (CORS)**, and then configure
   the CORS settings for your function URL. For more information about CORS, see [Cross-origin resource sharing (CORS)](#urls-cors "#urls-cors").
7. Choose **Save**.
   This creates a function URL for the `$LATEST` unpublished version of your function. The function URL
   appears in the **Function overview** section of the console.

8. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
9. Choose the name of the function with the alias that you want to create the function URL for.
10. Choose the **Aliases** tab, and then choose the name of the alias that you want to create
    the function URL for.
11. Choose the **Configuration** tab, and then choose **Function
    URL**.
12. Choose **Create function URL**.
13. For **Auth type**, choose **AWS_IAM** or **NONE**.
    For more information about function URL authentication, see [Access control](urls-auth.md "urls-auth.md").
14. (Optional) Select **Configure cross-origin resource sharing (CORS)**, and then configure
    the CORS settings for your function URL. For more information about CORS, see [Cross-origin resource sharing (CORS)](#urls-cors "#urls-cors").
15. Choose **Save**.
    This creates a function URL for your function alias. The function URL appears in the console's **Function
    overview** section for your alias.

###### To create a new function with a function URL (console)

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Choose **Create function**.
3. Under **Basic information**, do the following:
   1. For **Function name**, enter a name for your function, such as
      `my-function`.
   2. For **Runtime**, choose the language runtime that you prefer, such as
      **Node.js 22**.
   3. For **Architecture**, choose either **x86_64** or
      **arm64**.
   4. Expand **Permissions**, then choose whether to create a new execution role or use
      an existing one.

4. Expand **Advanced settings**, and then select **Function URL**.
5. For **Auth type**, choose **AWS_IAM** or **NONE**.
   For more information about function URL authentication, see [Access control](urls-auth.md "urls-auth.md").
6. (Optional) Select **Configure cross-origin resource sharing (CORS)**. By selecting this
   option during function creation, your function URL allows requests from all origins by default. You can edit
   the CORS settings for your function URL after creating the function. For more information about CORS, see
   [Cross-origin resource sharing (CORS)](#urls-cors "#urls-cors").
7. Choose **Create function**.
   This creates a new function with a function URL for the `$LATEST`
   unpublished version of the function. The function URL appears in the **Function
   overview** section of the console.

## Creating a function URL (AWS CLI)

To create a function URL for an existing Lambda function using the AWS Command Line Interface (AWS CLI), run the following
command:

```
aws lambda create-function-url-config \
    --function-name `my-function` \
    --qualifier `prod` \ // optional
    --auth-type `AWS_IAM`
    --cors-config `{AllowOrigins="https://example.com"}` // optional
```

This adds a function URL to the `prod` qualifier for the function
`my-function`. For more information about these configuration parameters, see
[CreateFunctionUrlConfig](../api/API_CreateFunctionUrlConfig.md "../api/API_CreateFunctionUrlConfig.md") in the API reference.

###### Note

To create a function URL via the AWS CLI, the function must already exist.

## Adding a function URL to a CloudFormation template

To add an `AWS::Lambda::Url` resource to your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::Lambda::Url",
  "Properties" : {
      "AuthType" : String,
      "Cors" : Cors,
      "Qualifier" : String,
      "TargetFunctionArn" : String
    }
}
```

### YAML

```
Type: AWS::Lambda::Url
Properties:
  AuthType: String
  Cors:
    Cors
  Qualifier: String
  TargetFunctionArn: String
```

### Parameters

- (Required) `AuthType` – Defines the type of authentication for your function URL. Possible
  values are either `AWS_IAM` or `NONE`. To restrict access to authenticated users
  only, set to `AWS_IAM`. To bypass IAM authentication and allow any user to make requests to
  your function, set to `NONE`.
- (Optional) `Cors` – Defines the [CORS settings](#urls-cors "#urls-cors") for
  your function URL. To add `Cors` to your `AWS::Lambda::Url` resource in CloudFormation,
  use the following syntax.

###### Example AWS::Lambda::Url.Cors (JSON)

```
{
  "AllowCredentials" : Boolean,
  "AllowHeaders" : [ String, ... ],
  "AllowMethods" : [ String, ... ],
  "AllowOrigins" : [ String, ... ],
  "ExposeHeaders" : [ String, ... ],
  "MaxAge" : Integer
}
```

###### Example AWS::Lambda::Url.Cors (YAML)

```
  AllowCredentials: Boolean
  AllowHeaders:
    - String
  AllowMethods:
    - String
  AllowOrigins:
    - String
  ExposeHeaders:
    - String
  MaxAge: Integer
```

- (Optional) `Qualifier` – The alias name.
- (Required) `TargetFunctionArn` – The name or Amazon Resource Name (ARN) of the Lambda function.
  Valid name formats include the following:
  - **Function name** – `my-function`
  - **Function ARN** –
    `arn:aws:lambda:us-west-2:123456789012:function:my-function`
  - **Partial ARN** – `123456789012:function:my-function`

## Cross-origin resource sharing (CORS)

To define how different origins can access your function URL, use [cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS "https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS"). We
recommend configuring CORS if you intend to call your function URL from a different domain. Lambda supports the
following CORS headers for function URLs.

| CORS header                                                                                                                                                                                                                 | CORS configuration property | Example values                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | -------------------------------------------------------------------------------- |
| [Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin")                | `AllowOrigins`              | `*` (allow all origins)<br>`https://www.example.com`<br>`http://localhost:60905` |
| [Access-Control-Allow-Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Methods "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Methods")             | `AllowMethods`              | `GET`, `POST`, `DELETE`, `*`                                                     |
| [Access-Control-Allow-Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Headers "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Headers")             | `AllowHeaders`              | `Date`, `Keep-Alive`, `X-Custom-Header`                                          |
| [Access-Control-Expose-Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Expose-Headers "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Expose-Headers")          | `ExposeHeaders`             | `Date`, `Keep-Alive`, `X-Custom-Header`                                          |
| [Access-Control-Allow-Credentials](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials") | `AllowCredentials`          | `TRUE`                                                                           |
| [Access-Control-Max-Age](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Max-Age "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Max-Age")                               | `MaxAge`                    | `5` (default), `300`                                                             |

When you configure CORS for a function URL using the Lambda console or the AWS CLI, Lambda automatically adds the
CORS headers to all responses through the function URL. Alternatively, you can manually add CORS headers to your
function response. If there are conflicting headers, the expected behavior depends on the
type of request:

- For preflight requests such as OPTIONS requests, the configured CORS headers on the function URL take
  precedence. Lambda returns only these CORS headers in the response.
- For non-preflight requests such as GET or POST requests, Lambda returns both the configured CORS headers
  on the function URL, as well as the CORS headers returned by the function. This can result in duplicate CORS
  headers in the response. You may see an error similar to the following: `The 'Access-Control-Allow-Origin'
header contains multiple values '*, *', but only one is allowed`.

In general, we recommend configuring all CORS settings on the function URL, rather than sending CORS
headers manually in the function response.

## Throttling function URLs

Throttling limits the rate at which your function processes requests. This is useful in many situations, such
as preventing your function from overloading downstream resources, or handling a sudden surge in requests.

You can throttle the rate of requests that your Lambda function processes through a function URL by configuring
reserved concurrency. Reserved concurrency limits the number of maximum concurrent invocations
for your function. Your function's maximum request rate per second (RPS) is equivalent to 10 times the configured
reserved concurrency. For example, if you configure your function with a reserved concurrency of 100, then the
maximum RPS is 1,000.

Whenever your function concurrency exceeds the reserved concurrency, your function URL returns an HTTP
`429` status code. If your function receives a request that exceeds the 10x RPS maximum based on your
configured reserved concurrency, you also receive an HTTP `429` error. For more information about
reserved concurrency, see [Configuring reserved concurrency for a function](configuration-concurrency.md "configuration-concurrency.md").

## Deactivating function URLs

In an emergency, you might want to reject all traffic to your function URL. To deactivate your function URL,
set the reserved concurrency to zero. This throttles all requests to your function URL, resulting in HTTP
`429` status responses. To reactivate your function URL, delete the reserved concurrency
configuration, or set the configuration to an amount greater than zero.

## Deleting function URLs

When you delete a function URL, you can’t recover it. Creating a new function URL will result in a different URL address.

###### Note

If you delete a function URL with auth type `NONE`, Lambda doesn't automatically delete the
associated resource-based policy. If you want to delete this policy, you must manually do so.

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Choose the name of the function.
3. Choose the **Configuration** tab, and then choose **Function
   URL**.
4. Choose **Delete**.
5. Enter the word _delete_ into the field to confirm the deletion.
6. Choose **Delete**.

###### Note

When you delete a function that has a function URL, Lambda asynchronously deletes the function URL. If you immediately create a new function with the same name in the same account, it is possible that the original function URL will be mapped to the new function instead of deleted.
