# Deploy transpiled TypeScript code in Lambda with .zip file archives

Before you can deploy TypeScript code to AWS Lambda, you need to transpile it into JavaScript. This page explains three ways to build and deploy TypeScript code to Lambda with .zip file archives:

- [Using AWS Serverless Application Model (AWS SAM)](#aws-sam-ts "#aws-sam-ts")
- [Using the AWS Cloud Development Kit (AWS CDK)](#aws-cdk-ts "#aws-cdk-ts")
- [Using the AWS Command Line Interface (AWS CLI) and esbuild](#aws-cli-ts "#aws-cli-ts")
  AWS SAM and AWS CDK simplify building and deploying TypeScript functions. The [AWS SAM template specification](../../../serverless-application-model/latest/developerguide/sam-specification.md "../../../serverless-application-model/latest/developerguide/sam-specification.md") provides a simple and clean syntax to describe the Lambda functions, APIs, permissions, configurations, and events that make up your serverless application. The [AWS CDK](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md") lets you build reliable, scalable, cost-effective applications in the cloud with the considerable expressive power of a programming language. The AWS CDK is intended for moderately to highly experienced AWS users. Both the AWS CDK and the AWS SAM use esbuild to transpile TypeScript code into JavaScript.

## Using AWS SAM to deploy TypeScript code to Lambda

Follow the steps below to download, build, and deploy a sample Hello World TypeScript application using the AWS SAM. This application implements a basic API backend. It consists of an Amazon API Gateway endpoint and a Lambda function. When you send a GET request to the API Gateway endpoint, the Lambda function is invoked. The function returns a `hello world` message.

###### Note

AWS SAM uses esbuild to create Node.js Lambda functions from TypeScript code. esbuild support is currently in public preview. During public preview, esbuild support may be subject to backwards incompatible changes.

###### Prerequisites

To complete the steps in this section, you must have the following:

- [AWS CLI version 2](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
- [AWS SAM CLI version 1.75 or later](../../../serverless-application-model/latest/developerguide/serverless-sam-cli-install.md "../../../serverless-application-model/latest/developerguide/serverless-sam-cli-install.md")
- Node.js

###### Deploy a sample AWS SAM application

1. Initialize the application using the Hello World TypeScript template.

```
`sam init --app-template hello-world-typescript --name sam-app --package-type Zip --runtime nodejs24.x`
```

2. (Optional) The sample application includes configurations for commonly used tools, such as [ESLlint](https://eslint.org/ "https://eslint.org/") for code linting and [Jest](https://jestjs.io/ "https://jestjs.io/") for unit testing. To run lint and test commands:

```
cd sam-app/hello-world
npm install
npm run lint
npm run test
```

3. Build the app.

```
cd sam-app
sam build
```

4. Deploy the app.

```
sam deploy --guided
```

5. Follow the on-screen prompts. To accept the default options provided in the interactive experience, respond with `Enter`.
6. The output shows the endpoint for the REST API. Open the endpoint in a browser to test the function. You should see this response:

```
{"message":"hello world"}
```

7. This is a public API endpoint that is accessible over the internet. We recommend that you delete the endpoint after testing.

```
sam delete
```

## Using the AWS CDK to deploy TypeScript code to Lambda

Follow the steps below to build and deploy a sample TypeScript application using the AWS CDK. This application implements a basic API backend. It consists of an API Gateway endpoint and a Lambda function. When you send a GET request to the API Gateway endpoint, the Lambda function is invoked. The function returns a `hello world` message.

###### Prerequisites

To complete the steps in this section, you must have the following:

- [AWS CLI version 2](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
- [AWS CDK version 2](../../../cdk/v2/guide/getting_started.md#getting_started_prerequisites "../../../cdk/v2/guide/getting_started.md#getting_started_prerequisites")
- Node.js
- Either [Docker](https://www.docker.com/get-started/ "https://www.docker.com/get-started/") or [esbuild](https://esbuild.github.io/ "https://esbuild.github.io/")

###### Deploy a sample AWS CDK application

1. Create a project directory for your new application.

```
mkdir hello-world
cd hello-world
```

2. Initialize the app.

```
cdk init app --language typescript
```

3. Add the [@types/aws-lambda](https://www.npmjs.com/package/@types/aws-lambda "https://www.npmjs.com/package/@types/aws-lambda") package as a development dependency. This package contains the type definitions for Lambda.

```
npm install -D @types/aws-lambda
```

4. Open the **lib** directory. You should see a file called **hello-world-stack.ts**. Create two new files in this directory: **hello-world.function.ts** and **hello-world.ts**.
5. Open **hello-world.function.ts** and add the following code to the file. This is the code for the Lambda function.

###### Note

The `import` statement imports the type definitions from [@types/aws-lambda](https://www.npmjs.com/package/@types/aws-lambda "https://www.npmjs.com/package/@types/aws-lambda"). It does not import the `aws-lambda` NPM package, which is an unrelated third-party tool. For more information, see [aws-lambda](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/aws-lambda "https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/aws-lambda") in the DefinitelyTyped GitHub repository.

```
import { Context, APIGatewayProxyResult, APIGatewayEvent } from 'aws-lambda';

export const handler = async (event: APIGatewayEvent, context: Context): Promise<APIGatewayProxyResult> => {
    console.log(`Event: ${JSON.stringify(event, null, 2)}`);
    console.log(`Context: ${JSON.stringify(context, null, 2)}`);
    return {
        statusCode: 200,
        body: JSON.stringify({
            message: 'hello world',
        }),
    };
};
```

6. Open **hello-world.ts** and add the following code to the file. This contains the [NodejsFunction construct](../../../cdk/api/v2/docs/aws-cdk-lib.md "../../../cdk/api/v2/docs/aws-cdk-lib.md"), which creates the Lambda function, and the [LambdaRestApi construct](../../../cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.md "../../../cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.md"), which creates the REST API.

```
import { Construct } from 'constructs';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { LambdaRestApi } from 'aws-cdk-lib/aws-apigateway';

export class HelloWorld extends Construct {
  constructor(scope: Construct, id: string) {
    super(scope, id);
    const helloFunction = new NodejsFunction(this, 'function');
    new LambdaRestApi(this, 'apigw', {
      handler: helloFunction,
    });
  }
}
```

The `NodejsFunction` construct assumes the following by default:

    * Your function handler is called `handler`.
    * The .ts file that contains the function code (**hello-world.function.ts**) is in the same directory as the .ts file that contains the construct (**hello-world.ts**). The construct uses the construct's ID ("hello-world") and the name of the Lambda handler file ("function") to find the function code. For example, if your function code is in a file called **hello-world.my-function.ts**, the **hello-world.ts** file must reference the function code like this:



    ```
    const helloFunction = new NodejsFunction(this, `'my-function'`);
    ```

You can change this behavior and configure other esbuild parameters. For more information, see [Configuring esbuild](../../../cdk/api/v2/docs/aws-cdk-lib.md#configuring-esbuild "../../../cdk/api/v2/docs/aws-cdk-lib.md#configuring-esbuild") in the AWS CDK API reference. 7. Open **hello-world-stack.ts**. This is the code that defines your [AWS CDK stack](../../../cdk/v2/guide/stacks.md "../../../cdk/v2/guide/stacks.md"). Replace the code with the following:

```
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { HelloWorld } from './hello-world';

export class HelloWorldStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    new HelloWorld(this, 'hello-world');
  }
}
```

8. from the `hello-world` directory containing your `cdk.json` file, deploy your
   application.

```
cdk deploy
```

9. The AWS CDK builds and packages the Lambda function using esbuild, and then deploys the function to the Lambda runtime. The output shows the endpoint for the REST API. Open the endpoint in a browser to test the function. You should see this response:

```
{"message":"hello world"}
```

This is a public API endpoint that is accessible over the internet. We recommend that you delete the endpoint after testing.

## Using the AWS CLI and esbuild to deploy TypeScript code to Lambda

The following example demonstrates how to transpile and deploy TypeScript code to Lambda using esbuild and the AWS CLI. esbuild produces one JavaScript file with all dependencies. This is the only file that you need to add to the .zip archive.

###### Prerequisites

To complete the steps in this section, you must have the following:

- [AWS CLI version 2](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
- Node.js
- An [execution role](lambda-intro-execution-role.md "lambda-intro-execution-role.md") for the Lambda function
- For Windows users, a zip file utility such as [7zip](https://www.7-zip.org/download.html "https://www.7-zip.org/download.html").

###### Deploy a sample function

1. On your local machine, create a project directory for your new function.
2. Create a new Node.js project with npm or a package manager of your choice.

```
npm init
```

3. Add the [@types/aws-lambda](https://www.npmjs.com/package/@types/aws-lambda "https://www.npmjs.com/package/@types/aws-lambda") and [esbuild](https://esbuild.github.io/ "https://esbuild.github.io/") packages as development dependencies. The `@types/aws-lambda` package contains the type definitions for Lambda.

```
npm install -D @types/aws-lambda esbuild
```

4. Create a new file called **index.ts**. Add the following code to the new file. This is the code for the Lambda function. The function returns a `hello world` message. The function doesn’t create any API Gateway resources.

###### Note

The `import` statement imports the type definitions from [@types/aws-lambda](https://www.npmjs.com/package/@types/aws-lambda "https://www.npmjs.com/package/@types/aws-lambda"). It does not import the `aws-lambda` NPM package, which is an unrelated third-party tool. For more information, see [aws-lambda](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/aws-lambda "https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/aws-lambda") in the DefinitelyTyped GitHub repository.

```
import { Context, APIGatewayProxyResult, APIGatewayEvent } from 'aws-lambda';

export const handler = async (event: APIGatewayEvent, context: Context): Promise<APIGatewayProxyResult> => {
  console.log(`Event: ${JSON.stringify(event, null, 2)}`);
  console.log(`Context: ${JSON.stringify(context, null, 2)}`);
  return {
      statusCode: 200,
      body: JSON.stringify({
          message: 'hello world',
      }),
   };
};
```

5. Add a build script to the **package.json** file. This configures esbuild to automatically create the .zip deployment package. For more information, see [Build scripts](https://esbuild.github.io/getting-started/#build-scripts "https://esbuild.github.io/getting-started/#build-scripts") in the esbuild documentation.

Linux and MacOS

```
"scripts": {
  "prebuild": "rm -rf dist",
  "build": "esbuild index.ts --bundle --minify --sourcemap --platform=node --target=es2020 --outfile=dist/index.js",
  "postbuild": "cd dist && zip -r index.zip index.js*"
},
```

Windows
In this example, the `"postbuild"` command uses the [7zip](https://www.7-zip.org/download.html "https://www.7-zip.org/download.html") utility to
create your .zip file. Use your own preferred Windows zip utility and modify the command as necessary.

```
"scripts": {
  "prebuild": "del /q dist",
  "build": "esbuild index.ts --bundle --minify --sourcemap --platform=node --target=es2020 --outfile=dist/index.js",
  "postbuild": "cd dist && 7z a -tzip index.zip index.js*"
},
```

6. Build the package.

```
npm run build
```

7. Create a Lambda function using the .zip deployment package. Replace the highlighted text with the Amazon Resource Name (ARN) of your [execution role](lambda-intro-execution-role.md "lambda-intro-execution-role.md").

```
aws lambda create-function --function-name hello-world --runtime "nodejs24.x" --role `arn:aws:iam::123456789012:role/lambda-ex` --zip-file "fileb://dist/index.zip" --handler index.handler
```

8. [Run a test event](testing-functions.md "testing-functions.md") to confirm that the function returns the following response. If you want to invoke this function using API Gateway, [create and configure a REST API](../../../apigateway/latest/developerguide/how-to-create-api.md "../../../apigateway/latest/developerguide/how-to-create-api.md").

```
{
  "statusCode": 200,
  "body": "{\"message\":\"hello world\"}"
}
```
