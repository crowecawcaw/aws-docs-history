# Patching libraries to instrument downstream

calls

###### Note

End-of-support notice – On February 25th, 2027, AWS X-Ray will discontinue support for AWS X-Ray SDKs and daemon. After February 25th, 2027, you will no longer receive updates or releases. For more information on the support timeline, see
[X-Ray SDK and daemon end of support timeline](xray-daemon-eos.md "xray-daemon-eos.md"). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

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
