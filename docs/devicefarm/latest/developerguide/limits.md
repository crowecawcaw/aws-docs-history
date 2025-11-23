# Limits in AWS Device Farm

###### Topics

- [Service limits](#service-limits "#service-limits")
- [File limits](#file-limits "#file-limits")
- [API limits](#api-limits "#api-limits")
- [Appium endpoint limits](#appium-endpoint-limits "#appium-endpoint-limits")
- [Custom environment variable limits](#custom-environment-variable-limits "#custom-environment-variable-limits")

## Service limits

- There is no limit to the number of devices that you can include in a test run. However, the maximum number of devices that Device Farm will test simultaneously during a test run is five. This number may be increased upon request and evaluated on per-case basis by the service team.
- There is no limit to the number of runs that you can schedule. Note that they can only remain queued for up to 24 hours.
- There is a 150-minute hard limit to the duration of a remote access session.
- There is a 150-minute hard limit to the duration of an automated test run
- The maximum number of in-flight jobs, including pending queued jobs across your account, is 250. This is a soft limit.
- There's no limit to the number of devices you can include in a test run. The number of devices (jobs) that can execute your tests in parallel at any given time is equal to your account-level concurrency. The default account-level concurrency for metered use in Device Farm is five.
- The metered concurrency limit may be increased upon request up to a certain threshold depending on the use case. The default account-level concurrency for unmetered use is equal to the number of slots you are subscribed to for that platform.

For more information concerning the default metered concurrency limits or quotas in general, see the [Quotas](../../../general/latest/gr/devicefarm.md "../../../general/latest/gr/devicefarm.md") page.

- An automation run that doesn't use a [custom test environment](custom-test-environments.md "custom-test-environments.md") can only have up to 250 individual test cases in it. Otherwise, the run may be skipped.

## File limits

- The maximum file size of an app that you can upload is 4 GB. Note that we do not currently accept .aab format files for Android.
- The maximum size of Device Farm's automatically-generated video during your test run is 1GB. Any video exceeding this size will have all remaining video content truncated. Customers can still use their own video recording solution, if present, and store it outside of Device Farm's managed storage.
- The maximum size of Device Farm's automatically-generated device log (logcat on Android or syslog on iOS) during your test run is 1GB. Any log exceeding this size will have all remaining logs truncated. For logs larger than 1 GB, Customers can store these logs outside of Device Farm's managed storage.
- The maximum size cumulative of Device Farm's custom environment mode customer artifacts is 1GB. If this size is exceeded by your artifacts, then none of the artifacts will be available.
- If the cumulative size of all artifacts generated during a test run exceeds 4GB, then some artifacts may be dropped (including the video, device logs, and customer artifacts).

## API limits

- Device Farm follows a token-bucket algorithm to throttle API call rates. For example, imagine creating a bucket that holds tokens. Each token represents one transaction, and one API call uses up a token. Tokens are added to the bucket at a fixed rate (e.g., 10 tokens per second), and the bucket has a maximum capacity (e.g., 100 tokens). When a request or packet arrives, it must claim a token from the bucket to be processed. If there are enough tokens, the request is allowed through and tokens are removed. If there aren't enough tokens, the request is either delayed or dropped, depending on the implementation.

In Device Farm, this is how the algorithm is implemented:

    + The **Burst API requests** is the maximum number of requests the service is able to respond to for a specified API in a specified customer account ID. In other words, this is the capacity of the bucket. You can call the API as many times as there are tokens remaining in the bucket, and each request consumes one token.
    + The **Transactions-per-second (TPS) rate** is the minimum rate at which your API requests can be executed. In other words, this is the rate at which the bucket refills with tokens per second. For example, if an API has a burst number of ten but a TPS of one, you could call it ten times instantly. However, the bucket would only regain tokens at a rate of one token per second, resulting in being throttled to one call per second unless you stopped calling the API to let the bucket refill.

Here are the rates for Device Farm APIs:

- For List and Get APIs, the **Burst API requests** capacity is `50`, and the **Transactions-per-second (TPS) rate** is `10`.
- For all other APIs, the **Burst API requests** capacity is `10`,
  and the **Transactions-per-second (TPS) rate** is `1`.

## Appium endpoint limits

The following limits apply to all Appium endpoint sessions.
For questions and guidance on how to best handle limits,
please open a support case.

- Every Appium command has an execution duration limit of 4 minutes, after which the command times out.
- The endpoint accepts input payload sizes of up to 20MB, and allows output payload sizes of up to 20MB. Any request with a larger input or output size than this will receive a WebDriver error of `'unsupported operation'`.
- Requests execute sequentially on the device in the order that they are received. As a result, we highly recommend sending commands sequentially, and waiting for each command's response before sending a new one. That said, certain Appium server commands can be sent in parallel, specifically:
  - [getStatus](https://appium.io/docs/en/2.19/commands/base-driver/#getstatus "https://appium.io/docs/en/2.19/commands/base-driver/#getstatus")
  - [getSessions](https://appium.io/docs/en/2.19/commands/base-driver/#getsessions "https://appium.io/docs/en/2.19/commands/base-driver/#getsessions")

- The endpoint does not support the [WebDriver BiDi protocol](https://appium.io/docs/en/2.19/guides/caps/#bidi-protocol-support "https://appium.io/docs/en/2.19/guides/caps/#bidi-protocol-support") at this time.
- The endpoint does not support Appium Plugins or drivers other than the XCUITest and UIAutomator2 drivers.
- A maximum of 3 apps can be used as auxiliary apps with a remote access session creation request. That said, there is no limit on how many apps can be installed during a session using the [`InstallToRemoteAccessSession`](../APIReference/API_InstallToRemoteAccessSession.md "../APIReference/API_InstallToRemoteAccessSession.md") API.

## Custom environment variable limits

The following limits apply to all custom environment variables.
For questions and guidance on how to best handle limits,
please open a support case.

- A maxiumum of 32 variables can be configured on a given Device Farm project or run.
- Variable names cannot exceed 256 characters in length.
- Variable names are subject to the limitations imposed by `bash`. Namely, they must contain only alphanumeric and underscore characters, and cannot start with a number.
- Variable names beginning with `$DEVICEFARM_` are reserved for internal service use.
- Variable values cannot exceed 256 characters in length.
- Environment variables cannot be used to configure test host compute selection in the test spec file.
