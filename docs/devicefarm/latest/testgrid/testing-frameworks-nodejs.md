# Using Device Farm desktop browser testing with Node.js

Device Farm desktop browser testing can be used alongside the AWS SDK for JavaScript in Node.js and W3C WebDriver Specification compatible libraries, such as the official Selenium WebDriver package and Webdriver.IO.

###### Topics

- [Using the Selenium WebDriver Node.js package to interact with Device Farm desktop browser testing](#testing-frameworks-nodejs-selenium "#testing-frameworks-nodejs-selenium")
- [Configuring Webdriver.IO API to interact with Device Farm desktop browser testing](#w12aac10c15c13 "#w12aac10c15c13")

## Using the Selenium WebDriver Node.js package to interact with Device Farm desktop browser testing

You can use Device Farm desktop browser testing with the Selenium Node.js `selenium-webdriver` package. The following
example shows how to use the `selenium-webdriver` npm package to interact with Device Farm desktop browser testing.

###### Note

This example assumes you have the SDK for JavaScript in Node.js configured and installed. For more information, see [AWS SDK for JavaScript in Node.js Getting Started Guide](../../../AWSJavaScriptSDK/guide/node-intro.md "../../../AWSJavaScriptSDK/guide/node-intro.md").

```
var webdriver = require('selenium-webdriver');
var AWS = require("aws-sdk");

var PROJECT_ARN = "arn:aws:devicefarm:us-west-2:`111122223333`:testgrid-project:`123e4567-e89b-12d3-a456-426655440000`";
var devicefarm = new AWS.DeviceFarm({ region: "us-west-2" });

(async () => {
    // Get the endpoint to create a new session
    const testGridUrlResult = await devicefarm.createTestGridUrl({
        projectArn: PROJECT_ARN,
        expiresInSeconds: 600
    }).promise();

    console.log("Created url result:", testGridUrlResult);
    runExample(testGridUrlResult.url);

})().catch((e) => console.error(e));

var runExample = async (urlString) => {
    console.log("Starting WebDriverJS remote driver")
    driver = await new webdriver.Builder()
        .usingServer(urlString)
        .withCapabilities({ browserName: 'chrome' })
        .build();

    console.log("New session created:", driver.getSession());

    await driver.get('https://aws.amazon.com/');
    const title = await driver.getTitle();
    console.log('Title was: ' + title);

    console.log("Deleting session...");
    await driver.quit();
}


```

## Configuring Webdriver.IO API to interact with Device Farm desktop browser testing

Device Farm desktop browser testing is supported in Webdriver.IO with some slight configuration changes. The following two examples show how to use Device Farm desktop browser testing with and without the Mocha test framework.

### Using Webdriver.IO and Device Farm desktop browser testing without Mocha

Using Device Farm desktop browser testing with Webdriver.IO does not require the inherent use of the Mocha test suite. The following example demonstrates how to configure the Webdriver.IO API for use with
Device Farm desktop browser testing and interact with a browser session.

###### Note

This example assumes you have the SDK for JavaScript in Node.js configured and installed. For more information, see [AWS SDK for JavaScript in Node.js Getting Started Guide](../../../AWSJavaScriptSDK/guide/node-intro.md "../../../AWSJavaScriptSDK/guide/node-intro.md").

```
const webdriverio = require('webdriverio');
const AWS = require("aws-sdk");

var PROJECT_ARN = process.env.TEST_GRID_PROJECT
var devicefarm = new AWS.DeviceFarm({ region: "us-west-2" });

(async () => {
    // Get a new signed WebDriver hub URL.
    const testGridUrlResult = await devicefarm.createTestGridUrl({
        projectArn: PROJECT_ARN,
        expiresInSeconds: 600
    }).promise();

    console.log("Created url result:", testGridUrlResult);
    runExample(testGridUrlResult.url);

})().catch((e) => console.error(e));

var runExample = async (urlString) => {
    var url = new URL(urlString)

    console.log("Starting a new remote driver")
    const browser = await webdriverio.remote({
        logLevel: 'trace',
        hostname: url.host,
        path: url.pathname,
        protocol: 'https',
        port: 443,
        connectionRetryTimeout: 180000,
        capabilities: {
            browserName: 'chrome',
        }
    })

    await browser.url('https://aws.amazon.com/')

    const title = await browser.getTitle()
    console.log('Title was: ' + title)

    await browser.deleteSession()
}


```
