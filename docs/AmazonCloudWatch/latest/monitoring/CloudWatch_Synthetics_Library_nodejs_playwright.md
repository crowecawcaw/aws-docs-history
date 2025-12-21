# Runtime versions using

Node.js and Playwright

The following sections contain information about the CloudWatch Synthetics runtime versions for Node.js and Playwright.
Playwright is an open-source automation library for browser testing. For more information about Playwright,
see [https://playwright.dev/](https://playwright.dev "https://playwright.dev")

The naming convention for these runtime versions is
`syn-`language`-`framework`-`majorversion`.`minorversion``.

##

syn-nodejs-playwright-5.0

**Major dependencies**:

- AWS Lambda runtime Node.js 22.x
- Playwright version 1.57.0
- Playwright/test version 1.57.0
- Chromium version 143.0.7499.4
- Firefox version 142.0.1

**Changes in syn-nodejs-playwright-5.0**

- Applied security patches and updated Playwright and browser versions.

For more information, see the following:

- [Playwright change log](https://playwright.dev/docs/release-notes "https://playwright.dev/docs/release-notes")
- [Playwright API reference](https://playwright.dev/docs/api/class-playwright "https://playwright.dev/docs/api/class-playwright")

The following earlier runtime versions for Node.js and Playwright are still supported.

###

syn-nodejs-playwright-4.0

**Major dependencies**:

- AWS Lambda runtime Node.js 22.x
- Playwright version 1.55.0
- Playwright/test version 1.55.0
- Chromium version 140.0.7339.16
- Firefox version 141.0

**Changes in syn-nodejs-playwright-4.0**

- Applied security patches and updated Playwright and browser versions.

For more information, see the following:

- [Playwright change log](https://playwright.dev/docs/release-notes "https://playwright.dev/docs/release-notes")
- [Playwright API reference](https://playwright.dev/docs/api/class-playwright "https://playwright.dev/docs/api/class-playwright")

###

syn-nodejs-playwright-3.0

**Major dependencies**:

- AWS Lambda runtime Node.js 20.x
- Playwright version 1.53.0
- Playwright/test version 1.53.0
- Chromium version 138.0.7204.168

**Changes in syn-nodejs-playwright-3.0**

- Multi-browser support – You can now run your nodejs puppeteer canaries in either Firefox or Chrome
- Support for visual monitoring

For more information, see the following:

- [Playwright change log](https://playwright.dev/docs/release-notes "https://playwright.dev/docs/release-notes")
- [Playwright API reference](https://playwright.dev/docs/api/class-playwright "https://playwright.dev/docs/api/class-playwright")

###

syn-nodejs-playwright-2.0

**Major dependencies**:

- AWS Lambda runtime Node.js 20.x
- Playwright version 1.49.1
- Playwright/test version 1.49.1
- Chromium version 131.0.6778.264

**Changes in syn-nodejs-playwright-2.0**

- The mismatch between total duration and sum of timings for a given request in HAR file is fixed.
- Supports dry runs for the canary which allows for adhoc executions or performing a safe canary update.

For more information, see the following:

- [Playwright change log](https://playwright.dev/docs/release-notes "https://playwright.dev/docs/release-notes")
- [Playwright API reference](https://playwright.dev/docs/api/class-playwright "https://playwright.dev/docs/api/class-playwright")

###

syn-nodejs-playwright-1.0

**Major dependencies**:

- AWS Lambda runtime Node.js 20.x
- Playwright version 1.44.1
- Playwright/test version 1.44.1
- Chromium version 126.0.6478.126

**Features**:

- **PlayWright support** – You can write canary scripts by using the Playwright automation framework.
  You can bring your existing Playwright scripts to run as canaries, and enhance them with AWS monitoring capabilities.
- **CloudWatch Logs integration** – You can query and filter for logs through the CloudWatch Synthetics
  console. Each log message contains unique `canaryRunId`, making it easy to search for logs for a particular canary run.
- **Metrics and canary artifacts** – You can monitor canary run pass rate through CloudWatch metrics,
  and configure alarms to alert you when canaries detect issues.
- **Screenshots and steps association** – You can capture screenshots using native Playwright functionality
  to visualize the stages of a canary script on each run. Screenshots are automatically associated with canary steps, and are uploaded to Amazon S3 buckets.
- **Multiple tabs**– You can create canaries that open multiple browser tabs, and access screenshots
  from each tab. You can create multi-tab and multi-step user workflows in Synthetics.
