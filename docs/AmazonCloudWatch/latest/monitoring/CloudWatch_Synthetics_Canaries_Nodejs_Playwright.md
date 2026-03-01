# Library functions available for Node.js canary scripts using Playwright

This section describes the library functions that are available for canary scripts
using the Node.js Playwright runtime.

###### Topics

- [launch](#Synthetics_Library_Nodejs_Playwright_functions "#Synthetics_Library_Nodejs_Playwright_functions")
- [newPage](#Synthetics_Library_Nodejs_Playwright_function_newPage "#Synthetics_Library_Nodejs_Playwright_function_newPage")
- [close](#Synthetics_Library_Nodejs_Playwright_function_close "#Synthetics_Library_Nodejs_Playwright_function_close")
- [getDefaultLaunchOptions](#Synthetics_Library_Nodejs_Playwright_function_getDefaultLaunchOptions "#Synthetics_Library_Nodejs_Playwright_function_getDefaultLaunchOptions")
- [executeStep](#Synthetics_Library_Nodejs_Playwright_function_executeStep "#Synthetics_Library_Nodejs_Playwright_function_executeStep")

## launch

This function launches a Chromium browser using a Playwright launch function, and
returns the browser object. It decompresses browser binaries and launches the chromium
browser by using default options suitable for a headless browser. For more information
about the `launch` function, see [`launch`](https://playwright.dev/docs/api/class-browsertype#browser-type-launch "https://playwright.dev/docs/api/class-browsertype#browser-type-launch") in the Playwright documentation.

**Usage**

```
const browser = await synthetics.launch();
```

**Arguments**

`options`
[options](https://playwright.dev/docs/api/class-browsertype#browser-type-launch "https://playwright.dev/docs/api/class-browsertype#browser-type-launch") (optional) is a configurable set of options for the browser.

**Returns**

Promise `<Browser>` where [Browser](https://playwright.dev/docs/api/class-browser "https://playwright.dev/docs/api/class-browser") is a Playwright
browser instance.

If this function is called again, a previously-opened browser is closed before
initiating a new browser. You can override launch parameters used by CloudWatch Synthetics,
and pass additional parameters when launching the browser. For example, the following
code snippet launches a browser with default arguments and a default executable path,
but with a viewport of 800 x 600 pixels. For more information, see [Playwright
launch options](https://playwright.dev/docs/api/class-browsertype#browser-type-launch "https://playwright.dev/docs/api/class-browsertype#browser-type-launch") in the Playwright documentation.

```
const browser = await synthetics.launch({
  defaultViewport: {
      "deviceScaleFactor": 1,
      "width": 800,
      "height": 600
}});
```

You can also add or override Chromium flags passed on by default to the
browser. For example, you can disable web security by adding a
`--disable-web-security` flag to arguments in the CloudWatch Synthetics launch
parameters:

```
// This function adds the --disable-web-security flag to the launch parameters
const defaultOptions = await synthetics.getDefaultLaunchOptions();
const launchArgs = [...defaultOptions.args, '--disable-web-security'];
const browser = await synthetics.launch({
    args: launchArgs
  });
```

## newPage

The `newPage()` function creates and returns a new Playwright page.
Synthetics automatically sets up a Chrome DevTools Protocol (CDP) connection to enable
network captures for HTTP archive (HAR) generation.

**Usage**

Use `newPage()` in either of the following ways:

**1. Creating a new page in a new browser context:**

```
const page = await synthetics.newPage(browser);
```

**2. Creating a new page in a specified browser
context:**

```
// Create a new browser context
const browserContext = await browser.newContext();

// Create a new page in the specified browser context
const page = await synthetics.newPage(browserContext)
```

**Arguments**

Accepts either Playwright [Browser](https://playwright.dev/docs/api/class-browser "https://playwright.dev/docs/api/class-browser") instance or
Playwright [BrowserContext](https://playwright.dev/docs/api/class-browsercontext "https://playwright.dev/docs/api/class-browsercontext") instance.

**Returns**

Promise <Page> where Page is a Playwright [Page](https://playwright.dev/docs/api/class-page "https://playwright.dev/docs/api/class-page") instance.

## close

Closes the currently-opened browser.

**Usage**

```
await synthetics.close();
```

It is recommended to close the browser in a `finally` block of your
script.

**Arguments**

None

**Returns**

Returns Promise<void> used by the Synthetics launch
function for launching the browser.

## getDefaultLaunchOptions

The `getDefaultLaunchOptions()` function returns the browser launch
options that are used by CloudWatch Synthetics.

**Usage**

```
const defaultOptions = await synthetics.getDefaultLaunchOptions();
```

**Arguments**

None

**Returns**

Returns Playwright [launch
options](https://playwright.dev/docs/api/class-browsertype#browser-type-launch "https://playwright.dev/docs/api/class-browsertype#browser-type-launch") used by the Synthetics `launch` function for launching the
browser.

## executeStep

The `executeStep` function is used to execute a step in a Synthetics
script. In CloudWatch Synthetics, a Synthetics step is a way to break down your canary script
into a series of clearly defined actions, allowing you to monitor different parts of
your application journey separately. For each step, CloudWatch Synthetics does the
following:

- Automatically captures a screenshot before step starts and after a step is complete. You can
  also capture screenshots inside a step. Screenshots are captured by default, but can
  be turned off by using Synthetics configurations `(Todo:
Link)`.
- A report, including a summary, of step execution details like the duration of a step,
  `pass` or `fail` status, source and destination page URLs,
  associated screenshots, etc. is created for each canary run. When you choose a run
  in the CloudWatch Synthetics console, you can view execution details of each step on the
  **Step** tab.
- `SuccessPercent` and `Duration` CloudWatch metrics are emitted for each step,
  enabling users to monitor availability and latency of each step.

**Usage**

```
await synthetics.executeStep("mystepname", async function () {
  await page.goto(url, { waitUntil: 'load', timeout: 30000 });
}
```

###### Note

Steps should run sequentially. Be sure to use `await` on
promises.

**Arguments**

- `stepName` string (required) (boolean)— Name of the Synthetics step.
- `functionToExecute` async function (required)— The function that you want
  Synthetics to run. This function should contain the logic for the step.
- `stepConfig` object (optional)— Step configuration overrides the global
  Synthetics configuration for this step.
  - `continueOnStepFailure` boolean (optional) —
    Whether to continue running the canary script after this step fails.
  - `screenshotOnStepStart` boolean (optional) —
    Whether to take a screenshot at the start of this step.
  - `screenshotOnStepSuccess` boolean (optional) —
    Whether to take a screenshot if this step succeeds.
  - `screenshotOnStepFailure` boolean (optional) —
    Whether to take a screenshot if this step fails.

- `page` — Playwright page object (optional)

A Playwright page object. Synthetics uses this page object to capture
screenshots and URLs. By default, Synthetics uses the Playwright page created when
the `synthetics.newPage()` function is called for capturing page details
like screenshots and URLs.

**Returns**

Returns a Promise that resolves with the value returned by the
`functionToExecute` function. For an example script, see [Sample code for canary scripts](CloudWatch_Synthetics_Canaries_Samples.md "CloudWatch_Synthetics_Canaries_Samples.md") in this guide.
