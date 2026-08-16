# Writing a Node.js canary script using the Puppeteer runtime

###### Topics

- [Creating a CloudWatch Synthetics canary from scratch](#CloudWatch_Synthetics_Canaries_write_from_scratch "#CloudWatch_Synthetics_Canaries_write_from_scratch")
- [Packaging your Node.js canary files](#CloudWatch_Synthetics_Canaries_package "#CloudWatch_Synthetics_Canaries_package")
- [Changing an existing Puppeteer script to use as a Synthetics canary](#CloudWatch_Synthetics_Canaries_modify_puppeteer_script "#CloudWatch_Synthetics_Canaries_modify_puppeteer_script")
- [Related topics](#CloudWatch_Synthetics_Canaries_Nodejs_Pup_related "#CloudWatch_Synthetics_Canaries_Nodejs_Pup_related")

## Creating a CloudWatch Synthetics canary from scratch

Here is an example minimal Synthetics Canary script. This script passes as a
successful run, and returns a string. To see what a failing canary looks like, change `let
 fail = false;` to `let fail = true;`.

You must define an entry point function for the canary script. To see how files are
uploaded to the Amazon S3 location specified as the canary's `ArtifactS3Location`,
create these files in the `/tmp` folder. All canary artifacts should
be stored in `/tmp`, because it's the only writable directory. Be
sure that the screenshot path is set to `/tmp` for any screenshots or
other files created by the script. Synthetics automatically uploads files in `/tmp` to an S3 bucket.

```
/tmp/<name>
```

After the script runs, the pass/fail status and the duration metrics are published
to CloudWatch and the files under`/tmp` are uploaded to an S3 bucket.

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

Next, expand the script to use Synthetics logging and make a call
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

The older packaging structure (for syn-nodejs-puppeteer-10.0 and below) is still
supported in newer versions.

Create a script using one of the following options:

- .js file (CommonJS syntax)
- .mjs file (ES modules syntax)

For ES modules, use one of the following options:

- .js file (CommonJS syntax)
- .mjs file (ES modules syntax)

The package structure is defined below:

- Root-level handler file (index.js/index.mjs)
- Optional configuration file (synthetics.json)
- Additional dependencies in node\_modules (if needed)

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

**To add an optional sub-folder support in
syn-nodejs-puppeteer-3.4+:**

```
nodejs/
└── node_modules/
    └── myFolder/
        └── myCanaryFilename.js
```

###### Note

Handler path in configuration must match your file location.

**Handler name**

Be sure to set your canary's script entry point (handler) as `myCanaryFilename.functionName` to match the file name of your script's entry
point. If you are using a runtime earlier than `syn-nodejs-puppeteer-3.4`,
then `functionName` must be `handler`. If you are using `syn-nodejs-puppeteer-3.4` or later, you can choose any function name as the
handler. If you are using `syn-nodejs-puppeteer-3.4` or later, you can also
optionally store the canary in a separate folder such as `nodejs/node_modules/myFolder/my_canary_filename`. If you store it in a separate
folder, specify that path in your script entry point, such as `myFolder/my_canary_filename.functionName`.

## Changing an existing Puppeteer script to use as a Synthetics canary

This section explains how to take Puppeteer scripts and modify them to run as
Synthetics canary scripts. For more information about Puppeteer, see [Puppeteer API
v1.14.0](https://github.com/puppeteer/puppeteer/blob/v1.14.0/docs/api.md "https://github.com/puppeteer/puppeteer/blob/v1.14.0/docs/api.md").

Start with this example Puppeteer script:

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

- Create and export a `handler` function. The handler is the entry
  point function for the script. If you are using a runtime earlier than `syn-nodejs-puppeteer-3.4`, the handler function must be named `handler`.
  If you are using `syn-nodejs-puppeteer-3.4` or later, the function can
  have any name, but it must be the same name that is used in the script. Also, if you
  are using `syn-nodejs-puppeteer-3.4` or later, you can store your scripts
  under any folder and specify that folder as part of the handler name.

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

The page object returned by the Synthetics.getPage function has the **page.on**
`request`, `response` and `requestfailed` events instrumented for logging. Synthetics also sets up HAR
file generation for requests and responses on the page, and adds the canary ARN to
the user-agent headers of outgoing requests on the page.

The script is now ready to be run as a Synthetics canary. Here is the updated
script:

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

## Related topics

- [Environment variables](CloudWatch_Synthetics_Canaries_CommonFeatures.md#CloudWatch_Synthetics_Environment_Variables "CloudWatch_Synthetics_Canaries_CommonFeatures.md#CloudWatch_Synthetics_Environment_Variables")
- [Encrypting environment variables at rest with a customer managed key](CloudWatch_Synthetics_Canaries_CommonFeatures.md#CloudWatch_Synthetics_function_encryption "CloudWatch_Synthetics_Canaries_CommonFeatures.md#CloudWatch_Synthetics_function_encryption")
- [Encrypting environment variables in transit](CloudWatch_Synthetics_Canaries_CommonFeatures.md#CloudWatch_Synthetics_transit_encryption "CloudWatch_Synthetics_Canaries_CommonFeatures.md#CloudWatch_Synthetics_transit_encryption")
- [Forcing your canary to use a static IP address](CloudWatch_Synthetics_Canaries_CommonFeatures.md#CloudWatch_Synthetics_Canaries_staticIP "CloudWatch_Synthetics_Canaries_CommonFeatures.md#CloudWatch_Synthetics_Canaries_staticIP")
