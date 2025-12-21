# Patching libraries to instrument downstream

calls

###### Note

X-Ray SDK/Daemon Maintenance Notice – On February 25th, 2026, the AWS X-Ray SDKs/Daemon will enter maintenance mode, where AWS will limit X-Ray SDK and Daemon releases to address security issues only. For more information on the support timeline, see
[X-Ray SDK and Daemon Support timeline](xray-sdk-daemon-timeline.md "xray-sdk-daemon-timeline.md"). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

To instrument downstream calls, use the X-Ray SDK for Ruby to patch the libraries that your
application uses. The X-Ray SDK for Ruby can patch the following libraries.

###### Supported Libraries

- `net/http` – Instrument HTTP clients.
- `aws-sdk` –
  Instrument AWS SDK for Ruby clients.
  When you use a patched library, the X-Ray SDK for Ruby creates a subsegment for the call and
  records information from the request and response. A segment must be available for the SDK to
  create the subsegment, either from the SDK middleware or a call to
  `XRay.recorder.begin_segment`.

To patch libraries, specify them in the configuration object that you pass to the X-Ray recorder.

###### Example main.rb – Patch libraries

```
require 'aws-xray-sdk'

config = {
  name: 'my app',
  `patch: %I[net_http aws_sdk]`
}

XRay.recorder.configure(config)
```
