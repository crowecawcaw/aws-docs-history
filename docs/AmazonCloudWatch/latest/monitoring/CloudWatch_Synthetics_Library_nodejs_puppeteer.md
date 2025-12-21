# Runtime versions using Node.js

and Puppeteer

The first runtime version for Node.js and Puppeteer was named `syn-1.0`.
Later runtime versions have
the naming convention
`syn-`language`-`majorversion`.`minorversion``. 
 Starting with `syn-nodejs-puppeteer-3.0`, the naming convention 
 is 
 `syn-`language`-`framework`-`majorversion`.`minorversion``

An additional `-beta` suffix shows
that the runtime version is currently in a beta preview release.

Runtime versions with the same
major version number are backward compatible.

The Lambda code in a canary is configured to have a maximum memory of 1 GB.
Each run of a canary times out after a configured timeout value. If no timeout
value is specified for a canary, CloudWatch chooses a timeout value
based on the canary's frequency. If you configure a timeout value, make it no shorter than
15 seconds to allow for Lambda cold starts and the time it takes to boot up the canary
instrumentation.

## syn-nodejs-puppeteer-13.0

`syn-nodejs-puppeteer-13.0` is the most recent Synthetics runtime for Node.js and Puppeteer.

###### Important

Starting Synthetics `syn-nodejs-puppeteer-8.0` and later, runtimes use AWS SDK for JavaScript V3.
If you need to migrate a canary from an earlier runtime, follow the aws-sdk-js-v3 Migration Workshop on GitHub. For more information about AWS SDK for JavaScript version 3, see
[this blog post](https://aws.amazon.com/blogs/developer/modular-aws-sdk-for-javascript-is-now-generally-available/ "https://aws.amazon.com/blogs/developer/modular-aws-sdk-for-javascript-is-now-generally-available/").

For more information, see the following:

- [Puppeteer Change log](https://pptr.dev/CHANGELOG#24250-2025-10-15 "https://pptr.dev/CHANGELOG#24250-2025-10-15")
- [Puppeteer API reference](https://github.com/puppeteer/puppeteer/blob/puppeteer-v24.2.0/docs/api/index.md "https://github.com/puppeteer/puppeteer/blob/puppeteer-v24.2.0/docs/api/index.md")

**Major dependencies**:

- Lambda runtime Node.js 22.x
- Puppeteer-core version 24.25.0
- Chromium version 142.0.7444.175
- Firefox version 145.x

**Changes in syn-nodejs-puppeteer-13.0**

- Applied security patches and updated Puppeteer and browser versions.
- Bug fix – Fixed intermittent runtime extension crash issue caused by concurrent map access

The following earlier runtime versions for Node.js and Puppeteer are still supported.

### syn-nodejs-puppeteer-12.0

For more information, see the following:

- [Puppeteer Change log](https://pptr.dev/CHANGELOG#24221-2025-09-23 "https://pptr.dev/CHANGELOG#24221-2025-09-23")
- [Puppeteer API reference](https://github.com/puppeteer/puppeteer/blob/puppeteer-v24.22.1/docs/api/index.md "https://github.com/puppeteer/puppeteer/blob/puppeteer-v24.22.1/docs/api/index.md")

**Major dependencies**:

- Lambda runtime Node.js 22.x
- Puppeteer-core version 24.22.1
- Chromium version 140.0.7339.185
- Firefox version 143.0.1

**Changes in syn-nodejs-puppeteer-12.0**

- Applied security patches and updated Puppeteer and browser versions.
- Bug fix for Restricted header redaction – Fixed an issue where in some situations restricted headers were not being redacted in executeHttpStep(). Behavior is now consistent with Puppeteer 10.0.
- Bug fix for includeResponseBody configuration – Fixed an issue where HAR file generation can misapply the includeResponseBody configuration setting in certain situations. HAR now ensures response bodies are excluded when setting is configured.
- Request capture lifecycle fixed – Fixed an issue where in some situations the HTTP request capturer may cause continuous aggregation of requests. Recording now terminates correctly after each step execution.

### syn-nodejs-puppeteer-11.0

For more information, see the following:

- [Puppeteer Change log](https://pptr.dev/CHANGELOG "https://pptr.dev/CHANGELOG")
- [Puppeteer API reference](https://github.com/puppeteer/puppeteer/blob/puppeteer-v24.2.0/docs/api/index.md "https://github.com/puppeteer/puppeteer/blob/puppeteer-v24.2.0/docs/api/index.md")

**Major dependencies**:

- Lambda runtime Node.js 20.x
- Puppeteer-core version 24.15.0
- Chromium version 138.0.7204.168

**Changes in syn-nodejs-puppeteer-11.0**

- Multi-browser support – You can now run Node.js Puppeteer canaries in either Firefox or Chrome
- Simplified packaging – Package scripts directly under root without using the Node.js/node_modules directory structure
- Screenshot integration – Capture screenshots using native Puppeteer functions to visualize canary script stages. Synthetics automatically associates
  screenshots with canary steps and uploads them to Amazon S3
- Enhanced log querying – Query and filter logs through the CloudWatch Insights console. Each log message includes a unique `canaryRunId` for easier searching
- Configuration file support – Define and update Synthetics settings using a synthetics.json file. This separation of configuration from script logic improves
  maintenance and reusability
- Multiple tabs support – Create canaries that open multiple browser tabs and access screenshots from each tab. Build multi-tab and multi-step user workflows in Synthetics
- Security fixes
- Visual monitoring bug fixes
- Added support for structured JSON logging with configurable log levels – Logs are now emitted in JSON format to enable easier parsing and querying
  in CloudWatch. Log level is configurable (for example, DEBUG, INFO, TRACE) through environment variables allowing users to control verbosity based on their needs
- Support for ES syntax

### syn-nodejs-puppeteer-10.0

For more information, see the following:

- [Puppeteer Change log](https://pptr.dev/CHANGELOG "https://pptr.dev/CHANGELOG")
- [Puppeteer API reference](https://github.com/puppeteer/puppeteer/blob/puppeteer-v24.2.0/docs/api/index.md "https://github.com/puppeteer/puppeteer/blob/puppeteer-v24.2.0/docs/api/index.md")

**Major dependencies**:

- Lambda runtime Node.js 20.x
- Puppeteer-core version 24.2.0
- Chromium version 131.0.6778.264

**Changes in syn-nodejs-puppeteer-10.0**

- The bug related to closing the browser that took excessively long is fixed.
- Supports dry runs for the canary which allows for adhoc executions or performing a safe canary update.

### syn-nodejs-puppeteer-9.1

**Major dependencies**:

- Lambda runtime Node.js 20.x
- Puppeteer-core version 22.12.1
- Chromium version 126.0.6478.126

**Changes in syn-nodejs-puppeteer-9.1** – Bug fixes related to date ranges and pending requests in HAR files are fixed.

### syn-nodejs-puppeteer-9.0

**Major dependencies**:

- Lambda runtime Node.js 20.x
- Puppeteer-core version 22.12.1
- Chromium version 126.0.6478.126

**Changes in syn-nodejs-puppeteer-9.0** – The bug fix to enable visual monitoring capabilities is fixed.

### syn-nodejs-puppeteer-8.0

###### Warning

Because of a bug, the `syn-nodejs-puppeteer-8.0` runtime doesn't support visual monitoring in canaries. Upgrade to [syn-nodejs-puppeteer-9.0](#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-9.0 "#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-9.0")
for the bug fix for visual monitoring.

###### Important

Lambda Node.js 18 and later runtimes use AWS SDK for JavaScript V3. If you need to migrate a canary
from an earlier runtime, follow the [aws-sdk-js-v3 Migration Workshop](https://github.com/aws-samples/aws-sdk-js-v3-workshop "https://github.com/aws-samples/aws-sdk-js-v3-workshop") on GitHub.
For more information about AWS SDK for JavaScript version 3, see
[this blog post](https://aws.amazon.com/blogs/developer/modular-aws-sdk-for-javascript-is-now-generally-available/ "https://aws.amazon.com/blogs/developer/modular-aws-sdk-for-javascript-is-now-generally-available/").

**Major dependencies**:

- Lambda runtime Node.js 20.x
- Puppeteer-core version 22.10.0
- Chromium version 125.0.6422.112

**Updates in syn-nodejs-puppeteer-8.0**:

- **Support for two-factor authentication**
- **Bug fixes** related to some service clients losing data
  in Node.js SDK V3 responses is fixed.

### syn-nodejs-puppeteer-7.0

**Major dependencies**:

- Lambda runtime Node.js 18.x
- Puppeteer-core version 21.9.0
- Chromium version 121.0.6167.139

**Code size**:

The size of code and dependencies that you can package into this runtime is 80 MB.

**Updates in syn-nodejs-puppeteer-7.0**:

- **Updated versions of the bundled libraries in Puppeteer and Chromium**— The Puppeteer and Chromium dependencies
  are updated to new versions.

###### Important

Moving from Puppeteer 19.7.0 to Puppeteer 21.9.0 introduces breaking changes regarding testing and filters. For more information, see the **BREAKING CHANGES**
sections in [puppeteer: v20.0.0](https://github.com/puppeteer/puppeteer/releases/tag/puppeteer-v20.0.0 "https://github.com/puppeteer/puppeteer/releases/tag/puppeteer-v20.0.0") and
[puppeteer-core: v21.0.0](https://github.com/puppeteer/puppeteer/releases/tag/puppeteer-core-v21.0.0 "https://github.com/puppeteer/puppeteer/releases/tag/puppeteer-core-v21.0.0").

**Recommended upgrade to AWS SDK v3**

The Lambda nodejs18.x runtime doesn't support AWS SDK v2. We
strongly recommend that you migrate to AWS SDK v3.

### syn-nodejs-puppeteer-6.2

**Major dependencies**:

- Lambda runtime Node.js 18.x
- Puppeteer-core version 19.7.0
- Chromium version 111.0.5563.146

**Changes in syn-nodejs-puppeteer-6.2**:

- **Updated versions of the bundled libraries in Chromium**
- **Ephemeral storage monitoring**— This runtime adds ephemeral storage monitoring
  in customer accounts.
- **Bug fixes**

### syn-nodejs-puppeteer-5.2

**Major dependencies**:

- Lambda runtime Node.js 16.x
- Puppeteer-core version 19.7.0
- Chromium version 111.0.5563.146

**Updates in syn-nodejs-puppeteer-5.2**:

- **Updated versions of the bundled libraries in Chromium**
- **Bug fixes**

The following runtimes for Node.js and Puppeteer have been deprecated. For information about
runtime deprecation dates, see [CloudWatch Synthetics runtime deprecation dates](CloudWatch_Synthetics_Canaries_Library.md#runtime_deprecation_dates "CloudWatch_Synthetics_Canaries_Library.md#runtime_deprecation_dates").

### syn-nodejs-puppeteer-6.1

**Major dependencies**:

- Lambda runtime Node.js 18.x
- Puppeteer-core version 19.7.0
- Chromium version 111.0.5563.146

**Updates in syn-nodejs-puppeteer-6.1**:

- **Stability improvements**— Added
  auto-retry logic for handling intermittent Puppeteer launch errors.
- **Dependency upgrades**— Upgrades for some
  third-party dependency packages.
- **Canaries without Amazon S3 permissions**— Bug fixes, such that
  canaries that don't have any Amazon S3 permissions can still run. These canaries with no Amazon S3 permissions
  won't be able to upload screenshots or other artifacts to Amazon S3. For more information about permissions
  for canaries, see [Required roles and permissions for canaries](CloudWatch_Synthetics_Canaries_CanaryPermissions.md "CloudWatch_Synthetics_Canaries_CanaryPermissions.md").

###### Important

IMPORTANT: The included AWS SDK for JavaScript v2 dependency will be removed and
updated to use AWS SDK for JavaScript v3 in a future runtime release. When that happens, you can
update your canary code references. Alternatively, you can continue referencing and using the included
AWS SDK for JavaScript v2 dependency by adding it as a dependency to your source code zip file.

### syn-nodejs-puppeteer-6.0

**Major dependencies**:

- Lambda runtime Node.js 18.x
- Puppeteer-core version 19.7.0
- Chromium version 111.0.5563.146

**Updates in syn-nodejs-puppeteer-6.0**:

- **Dependency upgrade**— The Node.js dependency
  is upgraded to 18.x.
- **Intercept mode support**— Puppeteer cooperative intercept
  mode support was added to the Synthetics canary runtime library.
- **Tracing behavior change**— Changed default tracing
  behavior to trace only fetch and xhr requests, and not trace resource requests. You can enable the tracing of
  resource requests by configuring the `traceResourceRequests` option.
- **Duration metric refined**— The `Duration` metric
  now excludes the operation time the canary uses to upload artifacts, take screenshots, and generate
  CloudWatch metrics. `Duration` metric values are reported to CloudWatch, and you can also see them
  in the Synthetics console.
- **Bug fix**— Clean up core dump generated
  when Chromium crashes during a canary run.

###### Important

IMPORTANT: The included AWS SDK for JavaScript v2 dependency will be removed and
updated to use AWS SDK for JavaScript v3 in a future runtime release. When that happens, you can
update your canary code references. Alternatively, you can continue referencing and using the included
AWS SDK for JavaScript v2 dependency by adding it as a dependency to your source code zip file.

### syn-nodejs-puppeteer-5.1

**Major dependencies**:

- Lambda runtime Node.js 16.x
- Puppeteer-core version 19.7.0
- Chromium version 111.0.5563.146

**Bug fixes in syn-nodejs-puppeteer-5.1**:

- **Bug fix**— This runtime
  fixes a bug in `syn-nodejs-puppeteer-5.0` where the HAR files created by the canaries were
  missing request headers.

### syn-nodejs-puppeteer-5.0

**Major dependencies**:

- Lambda runtime Node.js 16.x
- Puppeteer-core version 19.7.0
- Chromium version 111.0.5563.146

**Updates in syn-nodejs-puppeteer-5.0**:

- **Dependency upgrade**— The Puppeteer-core
  version is updated to 19.7.0. The Chromium version is upgraded to 111.0.5563.146.

###### Important

The new Puppeteer-core version is not completely backward-compatible with previous versions
of Puppeteer. Some of the changes in this version can cause existing canaries that use deprecated
Puppeteer functions to fail. For more information, see the breaking changes in the change logs for
Puppeteer-core versions 19.7.0 through 6.0, in
[Puppeteer change logs](https://github.com/puppeteer/puppeteer/releases?q=breaking&expanded=true "https://github.com/puppeteer/puppeteer/releases?q=breaking&expanded=true").

### syn-nodejs-puppeteer-4.0

**Major dependencies**:

- Lambda runtime Node.js 16.x
- Puppeteer-core version 5.5.0
- Chromium version 92.0.4512

**Updates in syn-nodejs-puppeteer-4.0**:

- **Dependency upgrade**— The Node.js
  dependency is updated to 16.x.

### syn-nodejs-puppeteer-3.9

###### Important

This runtime version was deprecated on January 8, 2024. For more
information, see [CloudWatch Synthetics runtime support policy](CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support "CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support").

**Major dependencies**:

- Lambda runtime Node.js 14.x
- Puppeteer-core version 5.5.0
- Chromium version 92.0.4512

**Updates in syn-nodejs-puppeteer-3.9**:

- **Dependency upgrades**— Upgrades some
  third-party dependency packages.

### syn-nodejs-puppeteer-3.8

###### Important

This runtime version was deprecated on January 8, 2024. For more
information, see [CloudWatch Synthetics runtime support policy](CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support "CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support").

**Major dependencies**:

- Lambda runtime Node.js 14.x
- Puppeteer-core version 5.5.0
- Chromium version 92.0.4512

**Updates in syn-nodejs-puppeteer-3.8**:

- **Profile cleanup**— Chromium profiles
  are now cleaned up after each canary run.

**Bug fixes in syn-nodejs-puppeteer-3.8**:

- **Bug fixes**— Previously, visual
  monitoring canaries would sometimes stop working properly after a run with no screenshots. This is now fixed.

### syn-nodejs-puppeteer-3.7

###### Important

This runtime version was deprecated on January 8, 2024. For more
information, see [CloudWatch Synthetics runtime support policy](CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support "CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support").

**Major dependencies**:

- Lambda runtime Node.js 14.x
- Puppeteer-core version 5.5.0
- Chromium version 92.0.4512

**Updates in syn-nodejs-puppeteer-3.7**:

- **Logging enhancement**— The canary will
  upload logs to Amazon S3 even if it times out or crashes.
- **Lambda layer size reduced**— The size of the Lambda
  layer used for canaries is reduced by 34%.

**Bug fixes in syn-nodejs-puppeteer-3.7**:

- **Bug fixes**— Japanese, Simplified Chinese,
  and Traditional Chinese fonts will render properly.

### syn-nodejs-puppeteer-3.6

###### Important

This runtime version was deprecated on January 8, 2024. For more
information, see [CloudWatch Synthetics runtime support policy](CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support "CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support").

**Major dependencies**:

- Lambda runtime Node.js 14.x
- Puppeteer-core version 5.5.0
- Chromium version 92.0.4512

**Updates in syn-nodejs-puppeteer-3.6**:

- **More precise timestamps**— The start time

and stop time of canary runs are now precise to the millisecond.

### syn-nodejs-puppeteer-3.5

###### Important

This runtime version was deprecated on January 8, 2024. For more
information, see [CloudWatch Synthetics runtime support policy](CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support "CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support").

**Major dependencies**:

- Lambda runtime Node.js 14.x
- Puppeteer-core version 5.5.0
- Chromium version 92.0.4512

**Updates in syn-nodejs-puppeteer-3.5**:

- **Updated dependencies**— The only
  new features in this runtime are the updated dependencies.

### syn-nodejs-puppeteer-3.4

###### Important

This runtime version was deprecated on November 13, 2022. For more
information, see [CloudWatch Synthetics runtime support policy](CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support "CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support").

**Major dependencies**:

- Lambda runtime Node.js 12.x
- Puppeteer-core version 5.5.0
- Chromium version 88.0.4298.0

**Updates in syn-nodejs-puppeteer-3.4**:

- **Custom handler function**— You can now use a
  custom handler function for your canary scripts. Previous runtimes required the script entry point
  to include `.handler`.

You can also put canary scripts in any folder and pass the folder name as part of the handler. For
example, `MyFolder/MyScriptFile.functionname` can be used as an entry point.

- **Expanded HAR file information**— You can now see
  bad, pending, and incomplete requests in the HAR files produced by canaries.

### syn-nodejs-puppeteer-3.3

###### Important

This runtime version was deprecated on November 13, 2022. For more
information, see [CloudWatch Synthetics runtime support policy](CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support "CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support").

**Major dependencies**:

- Lambda runtime Node.js 12.x
- Puppeteer-core version 5.5.0
- Chromium version 88.0.4298.0

**Updates in syn-nodejs-puppeteer-3.3**:

- **More options for artifact encryption**— For canaries
  using this runtime or later, instead of using an AWS managed key to encrypt
  artifacts that the canary stores in Amazon S3, you can choose to use an AWS KMS customer managed key
  or an Amazon S3-managed key. For more information, see [Encrypting canary artifacts](CloudWatch_Synthetics_artifact_encryption.md "CloudWatch_Synthetics_artifact_encryption.md").

### syn-nodejs-puppeteer-3.2

###### Important

This runtime version was deprecated on November 13, 2022. For more
information, see [CloudWatch Synthetics runtime support policy](CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support "CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support").

**Major dependencies**:

- Lambda runtime Node.js 12.x
- Puppeteer-core version 5.5.0
- Chromium version 88.0.4298.0

**Updates in syn-nodejs-puppeteer-3.2**:

- **visual monitoring with screenshots**— Canaries using this runtime or later
  can compare a screenshot taken during a run with a baseline version of the same screenshot. If the screenshots are more
  different than a specified percentage threshold, the canary fails. For more information,
  see [Visual monitoring](CloudWatch_Synthetics_Canaries_Library_Nodejs.md#CloudWatch_Synthetics_Library_SyntheticsLogger_VisualTesting "CloudWatch_Synthetics_Canaries_Library_Nodejs.md#CloudWatch_Synthetics_Library_SyntheticsLogger_VisualTesting") or [Visual monitoring blueprint](CloudWatch_Synthetics_Canaries_Blueprints.md#CloudWatch_Synthetics_Canaries_Blueprints_VisualTesting "CloudWatch_Synthetics_Canaries_Blueprints.md#CloudWatch_Synthetics_Canaries_Blueprints_VisualTesting").
- **New functions regarding sensitive data** You can prevent
  sensitive data from
  appearing in canary logs and reports. For more information, see [SyntheticsLogHelper class](CloudWatch_Synthetics_Canaries_Library_Nodejs.md#CloudWatch_Synthetics_Library_SyntheticsLogHelper "CloudWatch_Synthetics_Canaries_Library_Nodejs.md#CloudWatch_Synthetics_Library_SyntheticsLogHelper").
- **Deprecated function** The `RequestResponseLogHelper`
  class is deprecated in favor of other new configuration options. For more information, see [RequestResponseLogHelper class](CloudWatch_Synthetics_Canaries_Library_Nodejs.md#CloudWatch_Synthetics_Library_RequestResponseLogHelper "CloudWatch_Synthetics_Canaries_Library_Nodejs.md#CloudWatch_Synthetics_Library_RequestResponseLogHelper").

### syn-nodejs-puppeteer-3.1

###### Important

This runtime version was deprecated on November 13, 2022. For more
information, see [CloudWatch Synthetics runtime support policy](CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support "CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support").

**Major dependencies**:

- Lambda runtime Node.js 12.x
- Puppeteer-core version 5.5.0
- Chromium version 88.0.4298.0

**Updates in syn-nodejs-puppeteer-3.1**:

- **Ability to configure CloudWatch metrics**— With this
  runtime, you can disable the metrics that you do not require. Otherwise, canaries publish
  various CloudWatch metrics for each canary run.
- **Screenshot linking**—
  You can link a screenshot to a canary step after the step has completed. To do this, you
  take the screenshot by using the **takeScreenshot** method, using the name of
  the step that you want to associate the screenshot with. For example, you might want
  to perform a step, add a wait time, and then take the screenshot.
- **Heartbeat monitor blueprint can monitor multiple URLs**—
  You can use the heartbeat monitoring blueprint in the CloudWatch console to monitor multiple
  URLs and see the status, duration, associated screenshots, and failure reason for each URL
  in the step summary of the canary run report.

### syn-nodejs-puppeteer-3.0

###### Important

This runtime version was deprecated on November 13, 2022. For more
information, see [CloudWatch Synthetics runtime support policy](CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support "CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support").

**Major dependencies**:

- Lambda runtime Node.js 12.x
- Puppeteer-core version 5.5.0
- Chromium version 88.0.4298.0

**Updates in syn-nodejs-puppeteer-3.0**:

- **Upgraded dependencies**— This
  version uses Puppeteer version 5.5.0, Node.js 12.x, and Chromium 88.0.4298.0.
- **Cross-Region bucket access**—
  You can now specify an S3 bucket in another Region as the bucket
  where your canary stores its log files, screenshots, and HAR files.
- **New functions available**—
  This version adds library functions to retrieve the canary name and the Synthetics
  runtime version.

For more information, see [Synthetics class](CloudWatch_Synthetics_Canaries_Library_Nodejs.md#CloudWatch_Synthetics_Library_Synthetics_Class_all "CloudWatch_Synthetics_Canaries_Library_Nodejs.md#CloudWatch_Synthetics_Library_Synthetics_Class_all").

### syn-nodejs-2.2

This section contains information about
the `syn-nodejs-2.2` runtime version.

###### Important

This runtime version was deprecated on May 28, 2021. For more
information, see [CloudWatch Synthetics runtime support policy](CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support "CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support").

**Major dependencies**:

- Lambda runtime Node.js 10.x
- Puppeteer-core version 3.3.0
- Chromium version 83.0.4103.0

**Changes in syn-nodejs-2.2**:

- **Monitor your canaries as HTTP steps**—
  You can now test multiple APIs in a single canary. Each API is tested as a separate HTTP
  step, and CloudWatch Synthetics monitors the status of each step using step metrics and the
  CloudWatch Synthetics step report. CloudWatch Synthetics creates `SuccessPercent`
  and `Duration` metrics for each HTTP step.

This functionality is implemented by the
**executeHttpStep(stepName, requestOptions, callback, stepConfig)** function.
For more information, see [executeHttpStep(stepName, requestOptions, [callback], [stepConfig])](CloudWatch_Synthetics_Canaries_Library_Nodejs.md#CloudWatch_Synthetics_Library_executeHttpStep "CloudWatch_Synthetics_Canaries_Library_Nodejs.md#CloudWatch_Synthetics_Library_executeHttpStep").

The API canary blueprint is updated to use this new feature.

- **HTTP request reporting**—
  You can now view detailed HTTP requests reports which capture details such as
  request/response headers, response body, status code, error and performance timings,
  TCP connection time, TLS handshake time, first byte time, and content transfer time.
  All HTTP requests which use the HTTP/HTTPS module under the hood are captured here.
  Headers and response body are not captured by default but can be
  enabled by setting configuration options.
- **Global and step-level configuration**—
  You can set CloudWatch Synthetics configurations at the global level, which are applied
  to all steps of canaries. You can also override these configurations at the
  step level by passing configuration key/value pairs to enable or disable certain
  options.

For more information, see [SyntheticsConfiguration class](CloudWatch_Synthetics_Canaries_Library_Nodejs.md#CloudWatch_Synthetics_Library_SyntheticsConfiguration "CloudWatch_Synthetics_Canaries_Library_Nodejs.md#CloudWatch_Synthetics_Library_SyntheticsConfiguration").

- **Continue on step failure configuration**—
  You can choose to continue canary execution when a step fails. For the
  `executeHttpStep` function, this is turned on by default.
  You can set this option once at global level or set it differently per-step.

### syn-nodejs-2.1

###### Important

This runtime version was deprecated on May 28, 2021. For more
information, see [CloudWatch Synthetics runtime support policy](CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support "CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support").

**Major dependencies**:

- Lambda runtime Node.js 10.x
- Puppeteer-core version 3.3.0
- Chromium version 83.0.4103.0

**Updates in syn-nodejs-2.1**:

- **Configurable screenshot behavior**— Provides the ability
  to turn off the capturing of screenshots by UI canaries. In canaries that use previous
  versions of the runtimes, UI canaries always capture screenshots before and after each
  step. With `syn-nodejs-2.1`, this is configurable. Turning off screenshots
  can reduce your Amazon S3 storage costs, and can help you comply with HIPAA regulations.
  For more information, see [SyntheticsConfiguration class](CloudWatch_Synthetics_Canaries_Library_Nodejs.md#CloudWatch_Synthetics_Library_SyntheticsConfiguration "CloudWatch_Synthetics_Canaries_Library_Nodejs.md#CloudWatch_Synthetics_Library_SyntheticsConfiguration").
- **Customize the Google Chrome launch parameters** You can now
  configure the arguments used when a canary launches a Google Chrome browser window.
  For more information, see [launch(options)](CloudWatch_Synthetics_Canaries_Library_Nodejs.md#CloudWatch_Synthetics_Library_LaunchOptions "CloudWatch_Synthetics_Canaries_Library_Nodejs.md#CloudWatch_Synthetics_Library_LaunchOptions").

There can be a small increase in canary duration when using syn-nodejs-2.0 or later, compared
to earlier versions of the canary runtimes.

### syn-nodejs-2.0

###### Important

This runtime version was deprecated on May 28, 2021. For more
information, see [CloudWatch Synthetics runtime support policy](CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support "CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support").

**Major dependencies**:

- Lambda runtime Node.js 10.x
- Puppeteer-core version 3.3.0
- Chromium version 83.0.4103.0

**Updates in syn-nodejs-2.0**:

- **Upgraded dependencies**— This runtime version
  uses Puppeteer-core version 3.3.0 and Chromium
  version 83.0.4103.0
- **Support for X-Ray active tracing.** When a
  canary has tracing enabled,
  X-Ray traces are sent for all calls made by the canary that use the browser, the AWS SDK,
  or HTTP or HTTPS modules. Canaries with tracing enabled appear on the X-Ray Trace Map,
  even when they
  don't send requests to other services or applications that have tracing enabled. For
  more information, see [Canaries and X-Ray tracing](CloudWatch_Synthetics_Canaries_tracing.md "CloudWatch_Synthetics_Canaries_tracing.md").
- **Synthetics reporting**— For each canary
  run, CloudWatch Synthetics creates a report named `SyntheticsReport-PASSED.json`
  or `SyntheticsReport-FAILED.json` which
  records data such as start time, end time, status, and failures. It also records the PASSED/FAILED
  status of each step of the canary script, and failures and screenshots captured for each step.
- **Broken link checker report**— The new version
  of the broken link checker included in this runtime creates a report that includes the links that were checked,
  status code, failure reason (if any), and source and destination page screenshots.
- **New CloudWatch metrics**— Synthetics
  publishes metrics named `2xx`, `4xx`,
  `5xx`, and
  `RequestFailed` in the `CloudWatchSynthetics` namespace. These metrics show
  the number of 200s, 400s, 500s, and request failures in the canary runs. With this runtime version,
  these metrics
  are reported only for UI canaries, and are not reported for API canaries. They are also reported
  for API canaries starting with runtime version `syn-nodejs-puppeteeer-2.2`.
- **Sortable HAR files**— You can now
  sort your HAR files by status code, request size, and duration.
- **Metrics timestamp**— CloudWatch metrics are now reported based
  on the Lambda invocation time instead of the canary run end time.

**Bug fixes in syn-nodejs-2.0**:

- Fixed the issue of canary artifact upload errors not being reported.
  Such errors are now surfaced as execution errors.
- Fixed the issue of redirected requests (3xx) being incorrectly logged as errors.
- Fixed the issue of screenshots being numbered starting from 0.
  They should now start with 1.
- Fixed the issue of screenshots being garbled for Chinese and Japanese fonts.

There can be a small increase in canary duration when using syn-nodejs-2.0 or later, compared
to earlier versions of the canary runtimes.

### syn-nodejs-2.0-beta

###### Important

This runtime version was deprecated on February 8, 2021. For more
information, see [CloudWatch Synthetics runtime support policy](CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support "CloudWatch_Synthetics_Canaries_Library.md#CloudWatch_Synthetics_Canaries_runtime_support").

**Major dependencies**:

- Lambda runtime Node.js 10.x
- Puppeteer-core version 3.3.0
- Chromium version 83.0.4103.0

**Changes in syn-nodejs-2.0-beta**:

- **Upgraded dependencies**— This runtime version
  uses Puppeteer-core version 3.3.0 and Chromium
  version 83.0.4103.0
- **Synthetics reporting**— For each canary
  run, CloudWatch Synthetics creates a report named `SyntheticsReport-PASSED.json`
  or `SyntheticsReport-FAILED.json` which
  records data such as start time, end time, status, and failures. It also records the PASSED/FAILED
  status of each step of the canary script, and failures and screenshots captured for each step.
- **Broken link checker report**— The new version
  of the broken link checker included in this runtime creates a report that includes the links that were checked,
  status code, failure reason (if any), and source and destination page screenshots.
- **New CloudWatch metrics**— Synthetics
  publishes metrics named `2xx`, `4xx`,
  `5xx`, and
  `RequestFailed` in the `CloudWatchSynthetics` namespace. These metrics show
  the number of 200s, 400s, 500s, and request failures in the canary runs.
  These metrics
  are reported only for UI canaries, and are not reported for API canaries.
- **Sortable HAR files**— You can now
  sort your HAR files by status code, request size, and duration.
- **Metrics timestamp**— CloudWatch metrics are now reported based
  on the Lambda invocation time instead of the canary run end time.

**Bug fixes in syn-nodejs-2.0-beta**:

- Fixed the issue of canary artifact upload errors not being reported.
  Such errors are now surfaced as execution errors.
- Fixed the issue of redirected requests (3xx) being incorrectly logged as errors.
- Fixed the issue of screenshots being numbered starting from 0.
  They should now start with 1.
- Fixed the issue of screenshots being garbled for Chinese and Japanese fonts.

### syn-1.0

The first Synthetics runtime version is `syn-1.0`.

**Major dependencies**:

- Lambda runtime Node.js 10.x
- Puppeteer-core version 1.14.0
- The Chromium version that matches Puppeteer-core 1.14.0
