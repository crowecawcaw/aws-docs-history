# Runtime versions using Node.js and Playwright

The following sections contain information about the CloudWatch Synthetics runtime versions
for Node.js and Playwright. Playwright is an open-source automation library for browser
testing. For more information about Playwright, see [https://playwright.dev/](https://playwright.dev "https://playwright.dev")

The naming convention for these runtime versions is `syn-`language`
 -`framework`-`majorversion`.`minorversion``.

## syn-nodejs-playwright-8.0

###### Important

Starting Synthetics `syn-nodejs-playwright-5.1` and later, Synthetics
runtime uses the new namespace. Please migrate the canary script to use the new
namespace. Legacy namespace will be deprecated in a future release.

- @amzn/synthetics-playwright → @aws/synthetics-playwright

**Major dependencies**:

- AWS Lambda runtime Node.js 22.x
- Playwright version 1.61.1
- Playwright/test version 1.61.1
- Chromium version 150.0.7871.24
- Firefox version 151.0

**Changes in syn-nodejs-playwright-8.0**

- Upgrade `Chromium` to 150.0.7871.24 to address the following CVEs:

  - CVE-2026-11645

- Upgrade `ImageMagick` to 7.1.2-27 to address the following CVEs:

  - CVE-2026-28494
  - CVE-2026-28691
  - CVE-2026-28693
  - CVE-2026-30883
  - CVE-2026-30929
  - CVE-2026-30931
  - CVE-2026-32636
  - CVE-2026-33900
  - CVE-2026-33901
  - CVE-2026-33905
  - CVE-2026-33908

For more information, see the following:

- [Playwright release notes](https://playwright.dev/docs/release-notes "https://playwright.dev/docs/release-notes") on the Playwright website
- [Playwright API
  reference](https://playwright.dev/docs/api/class-playwright "https://playwright.dev/docs/api/class-playwright") on the Playwright website

The following earlier runtime versions for Node.js and Playwright are still
supported.

### syn-nodejs-playwright-7.1

**Major dependencies**:

- AWS Lambda runtime Node.js 22.x
- Playwright version 1.59.1
- Playwright/test version 1.59.1
- Chromium version 147.0.7727.15
- Firefox version 148.0.2

**Changes in syn-nodejs-playwright-7.1**

- Fix bug where HTTP headers with array values were not being captured properly.
- Upgrade `ws` to 8.20.1 to address the following CVEs:

  - CVE-2026-45736

- Upgrade `fast-xml-parser` to 5.7.2 to address the following CVEs:

  - CVE-2026-41650

### syn-nodejs-playwright-7.0

**Major dependencies**:

- AWS Lambda runtime Node.js 22.x
- Playwright version 1.59.1
- Playwright/test version 1.59.1
- Chromium version 147.0.7727.15
- Firefox version 148.0.2

**Changes in syn-nodejs-playwright-7.0**

- [Multilocation canaries](CloudWatch_Synthetics_Canaries_MultiLocation.md "CloudWatch_Synthetics_Canaries_MultiLocation.md") – Run the
  same canary across multiple AWS Regions from a single point of
  management.
- Upgrade `ImageMagick` to 7.1.2-15 to address the following CVEs:

  - CVE-2023-34152
  - CVE-2025-53014
  - CVE-2025-53101
  - CVE-2025-57807
  - CVE-2026-22770
  - CVE-2026-23876
  - CVE-2026-25897
  - CVE-2026-25898
  - CVE-2026-25968
  - CVE-2026-25971
  - CVE-2026-25983
  - CVE-2026-25986
  - CVE-2026-25987
  - CVE-2026-26284

### syn-nodejs-playwright-6.1

**Major dependencies**:

- AWS Lambda runtime Node.js 22.x
- Playwright version 1.59.1
- Playwright/test version 1.59.1
- Chromium version 147.0.7727.15
- Firefox version 148.0.2

**Changes in syn-nodejs-playwright-6.1**

- Updated Playwright and browser versions.
- Upgrade `fast-xml-parser` to 5.5.7 to address the following CVEs:

  - CVE-2026-27942
  - CVE-2026-33036

- Upgrade `Chromium` to 147.0.7727.15 to address the following CVEs:

  - CVE-2026-3909
  - CVE-2026-3910
  - CVE-2026-5281

### syn-nodejs-playwright-6.0

**Major dependencies**:

- AWS Lambda runtime Node.js 22.x
- Playwright version 1.58.2
- Playwright/test version 1.58.2
- Chromium version 145.0.7632.77
- Firefox version 146.0.1

**Changes in syn-nodejs-playwright-6.0**

- Applied security patches and updated Playwright and browser versions.

### syn-nodejs-playwright-5.1

**Major dependencies**:

- AWS Lambda runtime Node.js 22.x
- Playwright version 1.57.0
- Playwright/test version 1.57.0
- Chromium version 143.0.7499.169
- Firefox version 142.0.1

**Changes in syn-nodejs-playwright-5.1**

- Synthetics runtime namespace migration.
- Type definition is available in [npm Registry](https://www.npmjs.com/package/@aws/synthetics-playwright "https://www.npmjs.com/package/@aws/synthetics-playwright").
  Please ensure the type definition package version matches your canary's runtime
  version.

### syn-nodejs-playwright-5.0

**Major dependencies**:

- AWS Lambda runtime Node.js 22.x
- Playwright version 1.57.0
- Playwright/test version 1.57.0
- Chromium version 143.0.7499.4
- Firefox version 142.0.1

**Changes in syn-nodejs-playwright-5.0**

- Applied security patches and updated Playwright and browser versions.

### syn-nodejs-playwright-4.0

**Major dependencies**:

- AWS Lambda runtime Node.js 22.x
- Playwright version 1.55.0
- Playwright/test version 1.55.0
- Chromium version 140.0.7339.16
- Firefox version 141.0

**Changes in syn-nodejs-playwright-4.0**

- Applied security patches and updated Playwright and browser versions.

### syn-nodejs-playwright-3.0

**Major dependencies**:

- AWS Lambda runtime Node.js 20.x
- Playwright version 1.53.0
- Playwright/test version 1.53.0
- Chromium version 138.0.7204.168

**Changes in syn-nodejs-playwright-3.0**

- Multi-browser support – You can now run your nodejs puppeteer
  canaries in either Firefox or Chrome
- Support for visual monitoring

### syn-nodejs-playwright-2.0

**Major dependencies**:

- AWS Lambda runtime Node.js 20.x
- Playwright version 1.49.1
- Playwright/test version 1.49.1
- Chromium version 131.0.6778.264

**Changes in syn-nodejs-playwright-2.0**

- The mismatch between total duration and sum of timings for a given request
  in HAR file is fixed.
- Supports dry runs for the canary which allows for adhoc executions or
  performing a safe canary update.

### syn-nodejs-playwright-1.0

**Major dependencies**:

- AWS Lambda runtime Node.js 20.x
- Playwright version 1.44.1
- Playwright/test version 1.44.1
- Chromium version 126.0.6478.126

**Features**:

- **PlayWright support** – You can write
  canary scripts by using the Playwright automation framework. You can bring your
  existing Playwright scripts to run as canaries, and enhance them with AWS
  monitoring capabilities.
- **CloudWatch Logs integration** – You can query
  and filter for logs through the CloudWatch Synthetics console. Each log message
  contains unique `canaryRunId`, making it easy to search for logs for
  a particular canary run.
- **Metrics and canary artifacts** – You
  can monitor canary run pass rate through CloudWatch metrics, and configure alarms to
  alert you when canaries detect issues.
- **Screenshots and steps association** –
  You can capture screenshots using native Playwright functionality to visualize
  the stages of a canary script on each run. Screenshots are automatically
  associated with canary steps, and are uploaded to Amazon S3 buckets.
- **Multiple tabs**– You can create
  canaries that open multiple browser tabs, and access screenshots from each tab.
  You can create multi-tab and multi-step user workflows in Synthetics.
