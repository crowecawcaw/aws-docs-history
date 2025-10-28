# Define Lambda function handler in Node.js

The Lambda function _handler_ is the method in your function code that processes events. When your function is
invoked, Lambda runs the handler method. Your function runs until the handler returns a response, exits, or times out.

This page describes how to work with Lambda function handlers in Node.js, including options for project
setup, naming conventions, and best practices. This page also includes an example of a Node.js Lambda
function that takes in information about an order, produces a text file receipt, and puts this file
in an Amazon Simple Storage Service (Amazon S3) bucket. For information about how to deploy your function after writing it, see
[Deploy Node.js Lambda functions with .zip file archives](nodejs-package.md "nodejs-package.md") or [Deploy Node.js Lambda functions with container images](nodejs-image.md "nodejs-image.md").

###### Topics

- [Setting up your Node.js handler project](#nodejs-handler-setup "#nodejs-handler-setup")
- [Example Node.js Lambda function code](#nodejs-example-code "#nodejs-example-code")
- [Handler naming conventions](#nodejs-handler-naming "#nodejs-handler-naming")
- [Defining and accessing the input event object](#nodejs-example-input "#nodejs-example-input")
- [Valid handler patterns for Node.js functions](#nodejs-handler-signatures "#nodejs-handler-signatures")
- [Using the SDK for JavaScript v3 in your handler](#nodejs-example-sdk-usage "#nodejs-example-sdk-usage")
- [Accessing environment variables](#nodejs-example-envvars "#nodejs-example-envvars")
- [Using global state](#nodejs-handler-state "#nodejs-handler-state")
- [Code best practices for Node.js Lambda functions](#nodejs-best-practices "#nodejs-best-practices")

## Setting up your Node.js handler project

There are multiple ways to initialize a Node.js Lambda project. For example, you can create a standard Node.js project using `npm`, create an [AWS SAM application](../../../serverless-application-model/latest/developerguide/using-sam-cli-init.md#using-sam-cli-init-new "../../../serverless-application-model/latest/developerguide/using-sam-cli-init.md#using-sam-cli-init-new"), or create an [AWS CDK application](lambda-cdk-tutorial.md#lambda-cdk-step-1 "lambda-cdk-tutorial.md#lambda-cdk-step-1").

To create the project using `npm`:

```
npm init
```

This command initializes your project and generates a `package.json` file that manages your project's metadata and dependencies.

Your function code lives in a `.js` or `.mjs` JavaScript file. In the following example, we name this file `index.mjs` because it uses an ES module handler. Lambda supports both ES module and CommonJS handlers. For more information, see [Designating a function handler as an ES module](lambda-nodejs.md#designate-es-module "lambda-nodejs.md#designate-es-module").

A typical Node.js Lambda function project follows this general structure:

```
/project-root
  ├── index.mjs *— Contains main handler*
  ├── package.json *— Project metadata and dependencies*
  ├── package-lock.json *— Dependency lock file*
  └── node_modules/ *— Installed dependencies*
```

## Example Node.js Lambda function code

The following example Lambda function code takes in information about an order,
produces a text file receipt, and puts this file in an Amazon S3 bucket.

###### Note

This example uses an ES module handler. Lambda supports both ES module and CommonJS handlers. For more information, see [Designating a function handler as an ES module](lambda-nodejs.md#designate-es-module "lambda-nodejs.md#designate-es-module").

###### Example index.mjs Lambda function

```
import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';

// Initialize the S3 client outside the handler for reuse
const s3Client = new S3Client();

/**
 * Lambda handler for processing orders and storing receipts in S3.
 * @param {Object} event - Input event containing order details
 * @param {string} event.order_id - The unique identifier for the order
 * @param {number} event.amount - The order amount
 * @param {string} event.item - The item purchased
 * @returns {Promise<string>} Success message
 */
export const handler = async(event) => {
    try {
        // Access environment variables
        const bucketName = process.env.RECEIPT_BUCKET;
        if (!bucketName) {
            throw new Error('RECEIPT_BUCKET environment variable is not set');
        }

        // Create the receipt content and key destination
        const receiptContent = `OrderID: ${event.order_id}\nAmount: $${event.amount.toFixed(2)}\nItem: ${event.item}`;
        const key = `receipts/${event.order_id}.txt`;

        // Upload the receipt to S3
        await uploadReceiptToS3(bucketName, key, receiptContent);

        console.log(`Successfully processed order ${event.order_id} and stored receipt in S3 bucket ${bucketName}`);
        return 'Success';
    } catch (error) {
        console.error(`Failed to process order: ${error.message}`);
        throw error;
    }
};

/**
 * Helper function to upload receipt to S3
 * @param {string} bucketName - The S3 bucket name
 * @param {string} key - The S3 object key
 * @param {string} receiptContent - The content to upload
 * @returns {Promise<void>}
 */
async function uploadReceiptToS3(bucketName, key, receiptContent) {
    try {
        const command = new PutObjectCommand({
            Bucket: bucketName,
            Key: key,
            Body: receiptContent
        });

        await s3Client.send(command);
    } catch (error) {
        throw new Error(`Failed to upload receipt to S3: ${error.message}`);
    }
}
```

This `index.mjs` file contains the following sections of code:

- `import` block: Use this block to include libraries that your Lambda function requires, such as [AWS SDK clients](../../../sdk-for-javascript/v3/developer-guide/the-request-object.md "../../../sdk-for-javascript/v3/developer-guide/the-request-object.md").
- `const s3Client` declaration: This initializes an [Amazon S3 client](../../../AWSJavaScriptSDK/v3/latest/client/s3.md "../../../AWSJavaScriptSDK/v3/latest/client/s3.md") outside of the handler function. This causes Lambda to run this code during the [initialization phase](lambda-runtime-environment.md#runtimes-lifecycle-ib "lambda-runtime-environment.md#runtimes-lifecycle-ib"), and the client is preserved for [reuse across multiple invocations](lambda-runtime-environment.md#execution-environment-reuse "lambda-runtime-environment.md#execution-environment-reuse").
- JSDoc comment block: Define the input and output types for your handler using [JSDoc annotations](https://jsdoc.app/about-getting-started "https://jsdoc.app/about-getting-started").
- `export const handler`: This is the main handler function that Lambda invokes. When deploying your function, specify `index.handler` for the [Handler](../api/API_CreateFunction.md#lambda-CreateFunction-request-Handler "../api/API_CreateFunction.md#lambda-CreateFunction-request-Handler") property. The value of the `Handler` property is the file name and the name of the exported handler method, separated by a dot.
- `uploadReceiptToS3` function: This is a helper function that's referenced by the main handler function.

For this function to work properly, its [execution role](lambda-intro-execution-role.md "lambda-intro-execution-role.md") must allow the `s3:PutObject` action. Also, ensure that you define the `RECEIPT_BUCKET` environment variable. After a successful invocation, the Amazon S3 bucket should contain a receipt file.

## Handler naming conventions

When you configure a function, the value of the [Handler](../api/API_CreateFunction.md#lambda-CreateFunction-request-Handler "../api/API_CreateFunction.md#lambda-CreateFunction-request-Handler") setting is
the file name and the name of the exported handler method, separated by a dot. The default for functions created in the console and for
examples in this guide is `index.handler`. This indicates the `handler` method that's exported
from the `index.js` or `index.mjs` file.

If you create a function in the console using a different file name or function handler name, you must edit
the default handler name.

###### To change the function handler name (console)

1. Open the [Functions](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") page of the Lambda console and choose your function.
2. Choose the **Code** tab.
3. Scroll down to the **Runtime settings** pane and choose **Edit**.
4. In **Handler**, enter the new name for your function handler.
5. Choose **Save**.

## Defining and accessing the input event object

JSON is the most common and standard input format for Lambda functions. In this example,
the function expects an input similar to the following:

```
{
    "order_id": "12345",
    "amount": 199.99,
    "item": "Wireless Headphones"
}
```

When working with Lambda functions in Node.js, you can define the expected shape of the input event using JSDoc annotations. In this example, we define the input structure in the handler's JSDoc comment:

```
/**
 * Lambda handler for processing orders and storing receipts in S3.
 * @param {Object} event - Input event containing order details
 * @param {string} event.order_id - The unique identifier for the order
 * @param {number} event.amount - The order amount
 * @param {string} event.item - The item purchased
 * @returns {Promise<string>} Success message
 */
```

After you define these types in your JSDoc comment, you can access the fields of the event object directly in your code. For example, `event.order_id` retrieves the value of `order_id` from the original input.

## Valid handler patterns for Node.js functions

We recommend that you use [async/await](../../../sdk-for-javascript/v3/developer-guide/using-async-await.md "../../../sdk-for-javascript/v3/developer-guide/using-async-await.md") to declare the function handler instead of using [callbacks](../../../sdk-for-javascript/v3/developer-guide/using-a-callback-function.md "../../../sdk-for-javascript/v3/developer-guide/using-a-callback-function.md"). Async/await is a concise and readable way to write asynchronous code, without the need for nested callbacks or chaining promises. With async/await, you can write code that reads like synchronous code, while still being asynchronous and non-blocking.

### Using async/await (recommended)

The `async` keyword marks a function as asynchronous, and the `await` keyword pauses the execution of the function until a `Promise` is resolved. The handler accepts the following arguments:

- `event`: Contains the input data passed to your function.
- `context`: Contains information about the invocation, function, and execution environment. For more information, see [Using the Lambda context object to retrieve Node.js function information](nodejs-context.md "nodejs-context.md").

Here are the valid signatures for the async/await pattern:

- ```
  export const handler = async `(event)` => { };
  ```

````
* ```
export const handler = async `(event, context)` => { };
````

###### Note

Use a local integrated development environment (IDE) or text editor to write your TypeScript function code. You can’t create TypeScript code on the Lambda console.

### Using callbacks

Callback handlers must use the event, context, and callback arguments. Example:

```
export const handler = `(event, context, callback)` => { };
```

The callback function expects an `Error` and a response, which must be JSON-serializable. The function continues to execute until the [event loop](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/ "https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/") is empty or the function times out. The response isn't sent to the invoker until all event loop tasks are finished. If the function times out, an error is returned instead. You can configure the runtime to send the response immediately by setting [context.callbackWaitsForEmptyEventLoop](nodejs-context.md "nodejs-context.md") to false.

###### Example – HTTP request with callback

The following example function checks a URL and returns the status code to the invoker.

```
import https from "https";
let url = "https://aws.amazon.com/";

export const handler = (event, context, callback) => {
  https.get(url, (res) => {
    callback(null, res.statusCode);
  }).on("error", (e) => {
    callback(Error(e));
  });
};
```

## Using the SDK for JavaScript v3 in your handler

Often, you’ll use Lambda functions to interact with or make updates to other AWS resources. The simplest way to interface with these resources is to use the AWS SDK for JavaScript. All [supported Lambda Node.js runtimes](lambda-nodejs.md#nodejs-supported-runtimes "lambda-nodejs.md#nodejs-supported-runtimes") include the [SDK for JavaScript version 3](../../../AWSJavaScriptSDK/v3/latest/introduction.md "../../../AWSJavaScriptSDK/v3/latest/introduction.md"). However, we strongly recommend that you include the AWS SDK clients that you need in your deployment package. This maximizes [backward compatibility](runtimes-update.md#runtime-update-compatibility "runtimes-update.md#runtime-update-compatibility") during future Lambda runtime updates. Only rely on the runtime-provided SDK when you can't include additional packages (for example, when using the Lambda console code editor or inline code in an AWS CloudFormation template).

To add SDK dependencies to your function, use the `npm install` command for the specific SDK clients that you need. In the example code, we used the [Amazon S3 client](../../../AWSJavaScriptSDK/v3/latest/client/s3.md "../../../AWSJavaScriptSDK/v3/latest/client/s3.md"). Add this dependency by running the following command in the directory that contains your `package.json` file:

```
npm install @aws-sdk/client-s3
```

In the function code, import the client and commands that you need, as the example function demonstrates:

```
import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';
```

Then, initialize an [Amazon S3 client](../../../AWSJavaScriptSDK/v3/latest/client/s3.md "../../../AWSJavaScriptSDK/v3/latest/client/s3.md"):

```
const s3Client = new S3Client();
```

In this example, we initialized our Amazon S3 client outside of the main handler function to avoid having to initialize it every time we invoke our function. After you initialize your SDK client, you can then use it to make API calls for that AWS service. The example code calls the Amazon S3 [PutObject](../../../AWSJavaScriptSDK/v3/latest/client/s3/command/PutObjectCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/s3/command/PutObjectCommand.md") API action as follows:

```
const command = new PutObjectCommand({
    Bucket: bucketName,
    Key: key,
    Body: receiptContent
});
```

## Accessing environment variables

In your handler code, you can reference any [environment variables](configuration-envvars.md "configuration-envvars.md") by using `process.env`. In this example, we reference the defined `RECEIPT_BUCKET` environment variable using the following lines of code:

```
// Access environment variables
const bucketName = process.env.RECEIPT_BUCKET;
if (!bucketName) {
    throw new Error('RECEIPT_BUCKET environment variable is not set');
}
```

## Using global state

Lambda runs your static code during the [initialization phase](lambda-runtime-environment.md#runtimes-lifecycle-ib "lambda-runtime-environment.md#runtimes-lifecycle-ib") before invoking your function for the first time. Resources created during initialization stay in memory between invocations, so you can avoid having to create them every time you invoke your function.

In the example code, the S3 client initialization code is outside the handler. The runtime initializes the client before the function handles its first event, and the client remains available for reuse across all invocations.

## Code best practices for Node.js Lambda functions

Follow these guidelines when building Lambda functions:

- **Separate the Lambda handler from your core logic.** This allows you to make a more unit-testable function.
- **Control the dependencies in your function's deployment package.** The AWS Lambda execution environment contains a number of libraries. For the Node.js and Python runtimes, these include the AWS SDKs. To enable the latest set of features and security updates, Lambda will periodically update these libraries. These updates may introduce subtle changes to the behavior of your Lambda function. To have full control of the dependencies your function uses, package all of your dependencies with your deployment package.
- **Minimize the complexity of your dependencies.** Prefer simpler frameworks that load quickly on [execution environment](lambda-runtime-environment.md "lambda-runtime-environment.md") startup.
- **Minimize your deployment package size to its runtime necessities.** This will reduce the amount of time that it takes for your deployment package to be downloaded and unpacked ahead of invocation.

**Take advantage of execution environment reuse to improve the performance of your
function.** Initialize SDK clients and database connections outside of the function handler, and
cache static assets locally in the `/tmp` directory. Subsequent invocations processed by
the same instance of your function can reuse these resources. This saves cost by reducing function run time.

To avoid potential data leaks across invocations, don’t use the execution environment to store user data,
events, or other information with security implications. If your function relies on a mutable state that can’t
be stored in memory within the handler, consider creating a separate function or separate versions of a
function for each user.

**Use a keep-alive directive to maintain persistent connections.** Lambda purges idle connections over time.
Attempting to reuse an idle connection when invoking a function will result in a connection error. To maintain your persistent connection, use the
keep-alive directive associated with your runtime.
For an example, see [Reusing Connections with Keep-Alive in Node.js](../../../sdk-for-javascript/v3/developer-guide/node-reusing-connections.md "../../../sdk-for-javascript/v3/developer-guide/node-reusing-connections.md").

**Use [environment variables](configuration-envvars.md "configuration-envvars.md") to pass operational parameters to your function.** For example, if
you are writing to an Amazon S3 bucket, instead of hard-coding the bucket name you are writing to, configure the
bucket name as an environment variable.

**Avoid using recursive invocations** in your Lambda function, where the function
invokes itself or initiates a process that may invoke the function again. This could lead to unintended volume of
function invocations and escalated costs. If you see an unintended volume of invocations, set the function reserved concurrency
to `0` immediately to throttle all invocations to the function, while you update the
code.

**Do not use non-documented, non-public APIs** in your Lambda function code.
For AWS Lambda managed runtimes, Lambda periodically applies security and functional updates to Lambda's internal APIs.
These internal API updates may be backwards-incompatible, leading to unintended consequences such as invocation
failures if your function has a dependency on these non-public APIs. See
[the API reference](../api/welcome.md "../api/welcome.md") for a list of
publicly available APIs.

**Write idempotent code.** Writing idempotent code for your functions ensures that
duplicate events are handled the same way. Your code should properly validate events and gracefully handle
duplicate events. For more information, see
[How do I make
my Lambda function idempotent?](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-function-idempotent/ "https://aws.amazon.com/premiumsupport/knowledge-center/lambda-function-idempotent/").
