# Writing a Node.js canary script using the Puppeteer runtime

###### Topics

- [Creating a CloudWatch Synthetics canary from scratch](#CloudWatch_Synthetics_Canaries_write_from_scratch "#CloudWatch_Synthetics_Canaries_write_from_scratch")
- [Packaging your Node.js canary files](#CloudWatch_Synthetics_Canaries_package "#CloudWatch_Synthetics_Canaries_package")
- [Changing an existing Puppeteer script to use as a Synthetics canary](#CloudWatch_Synthetics_Canaries_modify_puppeteer_script "#CloudWatch_Synthetics_Canaries_modify_puppeteer_script")
- [Environment variables](#CloudWatch_Synthetics_Environment_Variables "#CloudWatch_Synthetics_Environment_Variables")
- [Integrating your canary with other AWS services](#CloudWatch_Synthetics_Canaries_AWS_integrate "#CloudWatch_Synthetics_Canaries_AWS_integrate")
- [Forcing your canary to use a static IP address](#CloudWatch_Synthetics_Canaries_staticIP "#CloudWatch_Synthetics_Canaries_staticIP")

## Creating a CloudWatch Synthetics canary from scratch

Here is an example minimal Synthetics Canary script. This script passes
as a successful run, and returns a string.
To see what a failing canary looks like, change `let fail = false;`
to `let fail = true;`.

You must define an entry point function for the canary script. To see how files are
uploaded to the Amazon S3 location specified as the canary's `ArtifactS3Location`,
create these files in the `/tmp` folder. All canary artifacts should
be stored in `/tmp`, because it's the only writable directory. Be
sure that the screenshot path is set to `/tmp` for any screenshots or
other files created by the script. Synthetics automatically uploads files in
`/tmp` to an S3 bucket.

```
/tmp/<name>
```

After the script runs, the pass/fail status and the duration metrics are published
to CloudWatch and the files under`/tmp` are uploaded to an S3
bucket.

```
const basicCustomEntryPoint = async function () {

    // Insert your code here

    // Perform multi-step pass/fail check

    // Log decisions made and results to /tmp

    // Be sure to wait for all your code paths to complete
    // before returning control back to Synthetics.
    // In that way, your canary will not finish and report success
    // before your code has finished executing

    // Throw to fail, return to succeed
    let fail = false;
    if (fail) {
        throw "Failed basicCanary check.";
    }

    return "Successfully completed basicCanary checks.";
};

exports.handler = async () => {
    return await basicCustomEntryPoint();
};
```

Next, we'll expand the script to use Synthetics logging and make a call
using the AWS SDK. For demonstration purposes, this script will create an
Amazon DynamoDB client and make a call to the DynamoDB listTables API. It logs
the response to the request and logs either pass or fail depending on whether
the request was successful.

```
const log = require('@aws/synthetics-logger');
const AWS = require('aws-sdk');
// Require any dependencies that your script needs
// Bundle additional files and dependencies into a .zip file with folder structure
// nodejs/node_modules/`additional files and folders`

const basicCustomEntryPoint = async function () {

    log.info("Starting DynamoDB:listTables canary.");

    let dynamodb = new AWS.DynamoDB();
    var params = {};
    let request = await dynamodb.listTables(params);
    try {
        let response = await request.promise();
        log.info("listTables response: " + JSON.stringify(response));
    } catch (err) {
        log.error("listTables error: " + JSON.stringify(err), err.stack);
        throw err;
    }

    return "Successfully completed DynamoDB:listTables canary.";
};

exports.handler = async () => {
    return await basicCustomEntryPoint();
};
```

## Packaging your Node.js canary files

**For syn-nodejs-puppeteer-11.0 and above**

The older packaging structure (for syn-nodejs-puppeteer-10.0 and below) is still supported in newer versions.

Create a script using one of the following options:

- .js file (CommonJS syntax)
- .mjs file (ES modules syntax)

For ES modules, use one of the following options:

- .js file (CommonJS syntax)
- .mjs file (ES modules syntax)

The package structure is defined below:

- Root-level handler file (index.js/index.mjs)
- Optional configuration file (synthetics.json)
- Additional dependencies in node_modules (if needed)

Packaging structure example:

```
  my_function/
├── index.mjs
├── synthetics.json
├── helper-utils.mjs
└── node_modules/
    └── dependencies
```

To package, follow the steps below:

1. Install dependencies (if any).

```
npm install
```

2. Create a .zip package.

```
zip -r my_deployment_package.zip
```

**For syn-nodejs-puppeteer-11.0 and below**

The following structure is required when using Amazon S3:

```
  nodejs/
└── node_modules/
    └── myCanaryFilename.js
```

**To add an optional sub-folder support in syn-nodejs-puppeteer-3.4+:**

```
nodejs/
└── node_modules/
    └── myFolder/
        └── myCanaryFilename.js
```

###### Note

Handler path in configuration must match your file location.

**Handler name**

Be sure to set your canary’s script entry point (handler) as
`myCanaryFilename.functionName` to match the file name of your script’s entry
point. If you are using a runtime earlier than `syn-nodejs-puppeteer-3.4`, then `functionName`
must be `handler`. If you are using `syn-nodejs-puppeteer-3.4` or later, you can choose any
function name as the handler. If you are using `syn-nodejs-puppeteer-3.4` or later,
you can also optionally store the canary in a separate folder such as
`nodejs/node_modules/myFolder/my_canary_filename`. If you store it in a separate folder,
specify that path in your script entry point, such as `myFolder/my_canary_filename.functionName`.

## Changing an existing Puppeteer script to use as a Synthetics canary

This section explains how to take Puppeteer scripts and modify them to run
as Synthetics canary scripts. For more information about Puppeteer, see
[Puppeteer API v1.14.0](https://github.com/puppeteer/puppeteer/blob/v1.14.0/docs/api.md "https://github.com/puppeteer/puppeteer/blob/v1.14.0/docs/api.md").

We'll start with this example Puppeteer script:

```
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');
  await page.screenshot({path: 'example.png'});

  await browser.close();
})();
```

The conversion steps are as follows:

- Create and export a `handler` function. The
  handler is the entry point function for the script. If you are using a runtime
  earlier than
  `syn-nodejs-puppeteer-3.4`,
  the handler function must be named `handler`. If you are using `syn-nodejs-puppeteer-3.4` or
  later, the function can have any name, but it must be the same name that is
  used in the script. Also, if you are using `syn-nodejs-puppeteer-3.4`
  or later, you can store your scripts under any folder and specify that folder as part of the handler name.

```
const basicPuppeteerExample = async function () {};

exports.handler = async () => {
    return await basicPuppeteerExample();
};
```

- Use the `Synthetics` dependency.

```
var synthetics = require('@aws/synthetics-puppeteer');
```

- Use the `Synthetics.getPage` function to get a Puppeteer `Page`
  object.

```
const page = await synthetics.getPage();
```

The page object returned by the Synthetics.getPage function has the
**page.on**
`request`, `response` and `requestfailed` events
instrumented for logging. Synthetics also sets up HAR file generation for requests
and responses on the page, and adds the canary ARN to the user-agent headers of
outgoing requests on the page.

The script is now ready to be run as a Synthetics canary. Here is the updated script:

```
var synthetics = require('@aws/synthetics-puppeteer');  // Synthetics dependency

const basicPuppeteerExample = async function () {
    const page = await synthetics.getPage(); // Get instrumented page from Synthetics
    await page.goto('https://example.com');
    await page.screenshot({path: '/tmp/example.png'}); // Write screenshot to /tmp folder
};

exports.handler = async () => {  // Exported handler function
    return await basicPuppeteerExample();
};
```

## Environment variables

You can use environment variables when creating canaries. This allows you to write a single
canary script and then use that script with different values to
quickly create multiple canaries that have a similar task.

For example, suppose your
organization has endpoints such as `prod`, `dev`, and `pre-release`
for the different stages of your software development, and you need to create canaries to test
each of these endpoints. You can write a single canary script that
tests your software and then
specify different values for the endpoint environment variable when you create
each of the three canaries. Then, when you create a canary, you specify the script and
the values to use for the environment variables.

The names of environment variables can contain letters, numbers, and the underscore
character. They must start with a letter and be at least two characters. The total size of
your environment variables can't exceed 4 KB. You can't specify any Lambda reserved
environment variables as the names of your environment variables. For more information
about reserved environment variables, see [Runtime
environment variables](../../../lambda/latest/dg/configuration-envvars.md#configuration-envvars-runtime "../../../lambda/latest/dg/configuration-envvars.md#configuration-envvars-runtime").

###### Important

Environment variable keys and values are encrypted at rest using AWS owned AWS KMS keys. However, the environment variables
are not encrypted on the client side. Do not store sensitive information
in them.

The following example script uses two environment variables. This script is for a
canary that checks whether a webpage is available. It uses environment variables to
parameterize both the URL that it checks and the CloudWatch Synthetics log level that it uses.

The following function sets `LogLevel`
to the value of the `LOG_LEVEL` environment variable.

```
 synthetics.setLogLevel(process.env.LOG_LEVEL);
```

This function sets `URL`
to the value of the `URL` environment variable.

```
const URL = process.env.URL;
```

This is the complete script. When you create a canary using this script, you specify
values for the `LOG_LEVEL` and `URL`
environment variables.

```
var synthetics = require('@aws/synthetics-puppeteer');
const log = require('@aws/synthetics-logger');

const pageLoadEnvironmentVariable = async function () {

    // Setting the log level (0-3)
    synthetics.setLogLevel(process.env.LOG_LEVEL);
    // INSERT URL here
    const URL = process.env.URL;

    let page = await synthetics.getPage();
    //You can customize the wait condition here. For instance,
    //using 'networkidle2' may be less restrictive.
    const response = await page.goto(URL, {waitUntil: 'domcontentloaded', timeout: 30000});
    if (!response) {
        throw "Failed to load page!";
    }
    //Wait for page to render.
    //Increase or decrease wait time based on endpoint being monitored.
    await page.waitFor(15000);
    await synthetics.takeScreenshot('loaded', 'loaded');
    let pageTitle = await page.title();
    log.info('Page title: ' + pageTitle);
    log.debug('Environment variable:' + process.env.URL);

    //If the response status code is not a 2xx success code
    if (response.status() < 200 || response.status() > 299) {
        throw "Failed to load page!";
    }
};

exports.handler = async () => {
    return await pageLoadEnvironmentVariable();
};
```

### Passing environment variables to your script

To pass environment variables to your script when you create a canary in the console,
specify the keys and values of the environment variables in the **Environment variables**
section on the console. For more information, see
[Creating a canary](CloudWatch_Synthetics_Canaries_Create.md "CloudWatch_Synthetics_Canaries_Create.md").

To pass environment variables through the API or AWS CLI, use the
`EnvironmentVariables` parameter in the `RunConfig` section. The following
is an example AWS CLI command that creates a canary that uses two environment variables with
keys of `Environment` and `Region`.

```
aws synthetics create-canary --cli-input-json '{
   "Name":"nameofCanary",
   "ExecutionRoleArn":"roleArn",
   "ArtifactS3Location":"s3://amzn-s3-demo-bucket-123456789012-us-west-2",
   "Schedule":{
      "Expression":"rate(0 minute)",
      "DurationInSeconds":604800
   },
   "Code":{
      "S3Bucket": "canarycreation",
      "S3Key": "cwsyn-mycanaryheartbeat-12345678-d1bd-1234-abcd-123456789012-12345678-6a1f-47c3-b291-123456789012.zip",
      "Handler":"pageLoadBlueprint.handler"
   },
   "RunConfig": {
      "TimeoutInSeconds":60,
      "EnvironmentVariables": {
         "Environment":"Production",
         "Region": "us-west-1"
      }
   },
   "SuccessRetentionPeriodInDays":13,
   "FailureRetentionPeriodInDays":13,
   "RuntimeVersion":"syn-nodejs-2.0"
}'

```

## Integrating your canary with other AWS services

All canaries
can use the AWS SDK library. You can use this library when you
write your canary to integrate the canary with other AWS services.

To do so, you need to add the following code to your canary. For these
examples, AWS Secrets Manager is used as the service that the canary is integrating with.

- Import the AWS SDK.

```
const AWS = require('aws-sdk');
```

- Create a client for the AWS service that you are integrating with.

```
const secretsManager = new AWS.SecretsManager();
```

- Use the client to make API calls to that service.

```
var params = {
  SecretId: secretName
};
return await secretsManager.getSecretValue(params).promise();
```

The following canary script code snippet demonstrates an example of integration with
Secrets Manager in more detail.

```
var synthetics = require('@aws/synthetics-puppeteer');
const log = require('@aws/synthetics-logger');

const AWS = require('aws-sdk');
const secretsManager = new AWS.SecretsManager();

const getSecrets = async (secretName) => {
    var params = {
        SecretId: secretName
    };
    return await secretsManager.getSecretValue(params).promise();
}

const secretsExample = async function () {
    let URL = "<URL>";
    let page = await synthetics.getPage();

    log.info(`Navigating to URL: ${URL}`);
    const response = await page.goto(URL, {waitUntil: 'domcontentloaded', timeout: 30000});

    // Fetch secrets
    let secrets = await getSecrets("secretname")

    /**
    * Use secrets to login.
    *
    * Assuming secrets are stored in a JSON format like:
    * {
    *   "username": "<USERNAME>",
    *   "password": "<PASSWORD>"
    * }
    **/
    let secretsObj = JSON.parse(secrets.SecretString);
    await synthetics.executeStep('login', async function () {
        await page.type(">USERNAME-INPUT-SELECTOR<", secretsObj.username);
        await page.type(">PASSWORD-INPUT-SELECTOR<", secretsObj.password);

        await Promise.all([
          page.waitForNavigation({ timeout: 30000 }),
          await page.click(">SUBMIT-BUTTON-SELECTOR<")
        ]);
    });

    // Verify login was successful
    await synthetics.executeStep('verify', async function () {
        await page.waitForXPath(">SELECTOR<", { timeout: 30000 });
    });
};

exports.handler = async () => {
    return await secretsExample();
};
```

## Forcing your canary to use a static IP address

You can set up a canary so that it uses a static IP address.

###### To force a canary to use a static IP address

1. Create a new VPC. For more information, see [Using DNS with Your VPC](../../../vpc/latest/userguide/vpc-dns.md "../../../vpc/latest/userguide/vpc-dns.md").
2. Create a new internet gateway. For more information, see [Adding an internet gateway to your VPC](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#working-with-igw "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#working-with-igw").
3. Create a public subnet inside your new VPC.
4. Add a new route table to the VPC.
5. Add a route in the new route table, that goes from `0.0.0.0/0` to
   the internet gateway.
6. Associate the new route table with the public subnet.
7. Create an elastic IP address. For more information, see
   [Elastic IP addresses](../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md "../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md") .
8. Create a new NAT gateway and assign it to the public subnet and the elastic IP address.
9. Create a private subnet inside the VPC.
10. Add a route to the VPC default route table, that goes from `0.0.0.0/0` to
    the NAT gateway
11. Create your canary.
