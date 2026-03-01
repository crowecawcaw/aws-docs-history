# Writing a Node.js canary script using the Playwright runtime

###### Topics

- [Packaging your Node.js canary files for the Playwright runtime](#Synthetics_canary_Nodejs_Playwright_package "#Synthetics_canary_Nodejs_Playwright_package")
- [Changing an existing Playwright script to use as a CloudWatch Synthetics canary](#CloudWatch_Synthetics_canary_edit_Playwright_script "#CloudWatch_Synthetics_canary_edit_Playwright_script")
- [CloudWatch Synthetics configurations](#Synthetics_canary_configure_Playwright_script "#Synthetics_canary_configure_Playwright_script")

## Packaging your Node.js canary files for the Playwright runtime

Your canary script comprises of a `.js` (CommonJS syntax) or
`.mjs` (ES syntax) file containing your Synthetics handler code, together
with any additional packages and modules your code depends on. Scripts created in ES
(ECMAScript) format should either use .mjs as the extension or include a package.json
file with the "type": "module" field set. Unlike other runtimes like Node.js Puppeteer,
you are not required to save your scripts in a specific folder structure. You can
package your scripts directly. Use your preferred `zip` utility to create a
`.zip` file with your handler file at the root. If your canary
script depends on additional packages or modules that aren't included in the Synthetics
runtime, you can add these dependencies to your `.zip` file. To do
so, you can install your function's required libraries in the
`node_modules` directory by running the `npm install`
command. The following example CLI commands create a `.zip` file
named `my_deployment_package.zip` containing the
`index.js` or `index.mjs` file (Synthetics
handler) and its dependencies. In the example, you install dependencies using the
`npm` package manager.

```
~/my_function
├── index.mjs
├── synthetics.json
├── myhelper-util.mjs
└── node_modules
    ├── mydependency
```

Create a `.zip` file that contains the contents of your project
folder at the root. Use the `r` (recursive) option, as shown in the following
example, to ensure that `zip` compresses the subfolders.

```
zip -r my_deployment_package.zip .
```

Add a Synthetics configuration file to configure the behavior of CloudWatch Synthetics.
You can create a `synthetics.json` file and save it at the same path
as your entry point or handler file.

Optionally, you can also store your entry point file in a folder structure of your
choice. However, be sure that the folder path is specified in your handler name.

**Handler name**

Be sure to set your canary’s script entry point (handler) as
`myCanaryFilename.functionName` to match the file name of your
script’s entry point. You can optionally store the canary in a separate folder such as
`myFolder/my_canary_filename.mjs`. If you store it in a separate
folder, specify that path in your script entry point, such as
`myFolder/my_canary_filename.functionName`.

## Changing an existing Playwright script to use as a CloudWatch Synthetics canary

You can edit an existing script for Node.js and Playwright to be used as a canary.
For more information about Playwright, see the [Playwright library](https://playwright.dev/docs/api/class-playwright "https://playwright.dev/docs/api/class-playwright")
documentation.

You can use the following Playwright script that is saved in file
`exampleCanary.mjs`.

```
import { chromium } from 'playwright';
import { expect } from '@playwright/test';

const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto('https://example.com', {timeout: 30000});
await page.screenshot({path: 'example-home.png'});

const title = await page.title();
expect(title).toEqual("Example Domain");

await browser.close();
```

Convert the script by performing the following steps:

1. Create and export a `handler` function. The handler is the entry
   point function for the script. You can choose any name for the handler function, but the
   function that is used in your script should be the same as in your canary handler.
   If your script name is `exampleCanary.mjs`, and the handler function
   name is `myhandler`, your canary handler is named
   `exampleCanary.myhandler`. In the following example, the handler
   function name is `handler`.

```
exports.handler = async () => {
  // Your script here
  };
```

2. Import the `Synthetics Playwright module` as a dependency.

```
import { synthetics } from '@aws/synthetics-playwright';
```

3. Launch a browser using the Synthetics `Launch` function.

```
const browser = await synthetics.launch();
```

4. Create a new Playwright page by using the Synthetics `newPage`
   function.

```
const page = await synthetics.newPage();
```

Your script is now ready to be run as a Synthetics canary. The following is the the
updated script:

**Updated script in ES6 format**

The script file saved with a `.mjs` extension.

```
import { synthetics } from '@aws/synthetics-playwright';
import { expect } from '@playwright/test';

export const handler = async (event, context) => {
  try {
        // Launch a browser
        const browser = await synthetics.launch();

        // Create a new page
        const page = await synthetics.newPage(browser);

        // Navigate to a website
        await page.goto('https://www.example.com', {timeout: 30000});

        // Take screenshot
        await page.screenshot({ path: '/tmp/example.png' });

        // Verify the page title
        const title = await page.title();
        expect(title).toEqual("Example Domain");
    } finally {
        // Ensure browser is closed
        await synthetics.close();
    }
};
```

**Updated script in CommonJS format**

The script file saved with a `.js` extension.

```
const { synthetics } = require('@aws/synthetics-playwright');
const { expect } = require('@playwright/test');

exports.handler = async (event) => {
  try {
    const browser = await synthetics.launch();
    const page = await synthetics.newPage(browser);
    await page.goto('https://www.example.com', {timeout: 30000});
    await page.screenshot({ path: '/tmp/example.png' });
    const title = await page.title();
    expect(title).toEqual("Example Domain");
  } finally {
    await synthetics.close();
  }
};
```

## CloudWatch Synthetics configurations

You can configure the behavior of the Synthetics Playwright runtime by providing an
optional JSON configuration file named `synthetics.json`. This file
should be packaged in the same location as the handler file. Though a configuration file
is optional, f you don't provide a configuration file, or a configuration key is
missing, CloudWatch assumes defaults.

**Packaging your configuration file**

The following are supported configuration values, and their defaults.

```
{
    "step": {
        "screenshotOnStepStart": false,
        "screenshotOnStepSuccess": false,
        "screenshotOnStepFailure": false,
        "stepSuccessMetric": true,
        "stepDurationMetric": true,
        "continueOnStepFailure": true,
        "stepsReport": true
    },
    "report": {
        "includeRequestHeaders": true,
        "includeResponseHeaders": true,
        "includeUrlPassword": false,
        "includeRequestBody": true,
        "includeResponseBody": true,
        "restrictedHeaders": ['x-amz-security-token', 'Authorization'], // Value of these headers is redacted from logs and reports
        "restrictedUrlParameters": ['Session', 'SigninToken'] // Values of these url parameters are redacted from logs and reports
    },
    "logging": {
        "logRequest": false,
        "logResponse": false,
        "logResponseBody": false,
        "logRequestBody": false,
        "logRequestHeaders": false,
        "logResponseHeaders": false
    },
    "httpMetrics": {
        "metric_2xx": true,
        "metric_4xx": true,
        "metric_5xx": true,
        "failedRequestsMetric": true,
        "aggregatedFailedRequestsMetric": true,
        "aggregated2xxMetric": true,
        "aggregated4xxMetric": true,
        "aggregated5xxMetric": true
    },
    "canaryMetrics": {
        "failedCanaryMetric": true,
        "aggregatedFailedCanaryMetric": true
    },
    "userAgent": "",
    "har": true
}
```

**Step configurations**

- `screenshotOnStepStart` – Determines if Synthetics should
  capture a screenshot before the step starts. The default is `true`.
- `screenshotOnStepSuccess` – Determines if Synthetics should
  capture a screenshot after a step has succeeded. The default is `true`.
- `screenshotOnStepFailure` – Determines if Synthetics should
  capture a screenshot after a step has failed. The default is `true`.
- `continueOnStepFailure` – Determines if a script should
  continue even after a step has failed. The default is `false`.
- `stepSuccessMetric` – Determines if a step’s
  `SuccessPercent` metric is emitted. The `SuccessPercent`
  metric for a step is `100` for the canary run if the step succeeds, and
  `0` if the step fails. The default is `true`.
- `stepDurationMetric` – Determines if a step's
  `Duration` metric is emitted. The `Duration` metric is
  emitted as a duration, in milliseconds, of the step's run. The default is
  `true`.

**Report configurations**

Includes all reports generated by CloudWatch Synthetics, such as a HAR file and a
Synthetics steps report. Sensitive data redaction fields `restrictedHeaders`
and `restrictedUrlParameters` also apply to logs generated by Synthetics.

- `includeRequestHeaders` – Whether to include request headers
  in the report. The default is `false`.
- `includeResponseHeaders` – Whether to include response headers
  in the report. The default is `false`.
- `includeUrlPassword` – Whether to include a password that
  appears in the URL. By default, passwords that appear in URLs are redacted from logs
  and reports, to prevent the disclosure of sensitive data. The default is
  `false`.
- `includeRequestBody` – Whether to include the request body in
  the report. The default is `false`.
- `includeResponseBody` – Whether to include the response body
  in the report. The default is `false`.
- `restrictedHeaders` – A list of header values to ignore, if
  headers are included. This applies to both request and response headers. For
  example, you can hide your credentials by passing `includeRequestHeaders`
  as true and `restrictedHeaders` as `['Authorization']`.
- `restrictedUrlParameters` – A list of URL path or query
  parameters to redact. This applies to URLs that appear in logs, reports, and errors.
  The parameter is case-insensitive. You can pass an asterisk (`*`) as a
  value to redact all URL path and query parameter values. The default is an empty
  array.
- `har` – Determines if an HTTP archive (HAR) should be
  generated. The default is `true`.

The following is an example of a report configurations file.

```
"includeRequestHeaders": true,
"includeResponseHeaders": true,
"includeUrlPassword": false,
"includeRequestBody": true,
"includeResponseBody": true,
"restrictedHeaders": ['x-amz-security-token', 'Authorization'], // Value of these headers is redacted from logs and reports
"restrictedUrlParameters": ['Session', 'SigninToken'] // Values of these URL parameters are redacted from logs and reports
```

**Logging configurations**

Applies to logs generated by CloudWatch Synthetics. Controls the verbosity of request and
response logs.

- `logRequest` – Whether to log every request in canary logs.
  For UI canaries, this logs each request sent by the browser. The default is
  `false`.
- `logResponse` – Whether to log every response in canary logs.
  For UI canaries, this logs every response received by the browser. The default is
  `false`.
- `logRequestBody` – Whether to log request bodies along with
  the requests in canary logs. This configuration applies only if
  `logRequest` is true. The default is `false`.
- `logResponseBody` – Whether to log response bodies along with
  the requests in canary logs. This configuration applies only if
  `logResponse` is true. The default is `false`.
- `logRequestHeaders` – Whether to log request headers along
  with the requests in canary logs. This configuration applies only if
  `logRequest` is true. The default is `false`.
- `logResponseHeaders` – Whether to log response headers along
  with the responses in canary logs. This configuration applies only if
  `logResponse` is true. The default is `false`.

**HTTP metric configurations**

Configurations for metrics related to the count of network requests with different
HTTP status codes, emitted by CloudWatch Synthetics for this canary.

- `metric_2xx` – Whether to emit the `2xx` metric
  (with the `CanaryName` dimension) for this canary. The default is
  `true`.
- `metric_4xx` – Whether to emit the `4xx` metric
  (with the `CanaryName` dimension) for this canary. The default is
  `true`.
- `metric_5xx` – Whether to emit the `5xx` metric
  (with the `CanaryName` dimension) for this canary. The default is
  `true`.
- `failedRequestsMetric` – Whether to emit the
  `failedRequests` metric (with the `CanaryName` dimension)
  for this canary. The default is `true`.
- `aggregatedFailedRequestsMetric` – Whether to emit the
  `failedRequests` metric (without the `CanaryName` dimension)
  for this canary. The default is `true`.
- `aggregated2xxMetric` – Whether to emit the `2xx`
  metric (without the `CanaryName` dimension) for this canary. The default
  is `true`.
- `aggregated4xxMetric` – Whether to emit the `4xx`
  metric (without the `CanaryName` dimension) for this canary. The default
  is `true`.
- `aggregated5xxMetric` – Whether to emit the `5xx`
  metric (without the `CanaryName` dimension) for this canary. The default
  is `true`.

**Canary metric configurations**

Configurations for other metrics emitted by CloudWatch Synthetics.

- `failedCanaryMetric` – Whether to emit the `Failed`
  metric (with the `CanaryName` dimension) for this canary. The default is
  `true`.
- `aggregatedFailedCanaryMetric` – Whether to emit the
  `Failed` metric (without the `CanaryName` dimension) for
  this canary. The default is `true`.

**Other configurations**

- `userAgent` – A string to append to the user agent. The user
  agent is a string that is included in request header, and identifies your browser to
  websites you visit when you use the headless browser. CloudWatch Synthetics automatically
  adds `CloudWatchSynthetics/`canary-arn` to the user
agent`. The specified configuration is appended to the generated user agent.
  The default user agent value to append is an empty string (`""`).

### CloudWatch Synthetics environment variables

Configure the logging level and format by using environment variables.

**Log format**

The CloudWatch Synthetics Playwright runtime creates CloudWatch logs for every canary run.
Logs are written in JSON format for convenient querying. Optionally, you can change
the log format to `TEXT`.

- `Environment variable name` – CW_SYNTHETICS_LOG_FORMAT
- `Supported values` – JSON, TEXT
- `Default` – JSON

**Log levels**

Though enabling `Debug` mode increases verbosity, it can be useful for
troubleshooting.

- `Environment variable name` – CW_SYNTHETICS_LOG_LEVEL
- `Supported values` – TRACE, DEBUG, INFO, WARN, ERROR, FATAL
- `Default` – INFO
