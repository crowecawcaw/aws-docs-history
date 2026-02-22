# Migrate to OpenTelemetry Node.js

This section explains how to migrate your Node.js applications from X-Ray SDK to OpenTelemetry. It covers both automatic and manual instrumentation approaches, and provides specific examples for common use cases.

The X-Ray Node.js SDK helps you manually instrument your Node.js applications for tracing. This section provides code examples for migrating from X-Ray to OpenTelemetry instrumentation.

###### Sections

- [Zero code automatic instrumentation solutions](#zero-code-instrumentation "#zero-code-instrumentation")
- [Manual instrumentation solutions](#manual-instrumentation "#manual-instrumentation")
- [Tracing incoming requests](#tracing-incoming-requests "#tracing-incoming-requests")
- [AWS SDK JavaScript V3 instrumentation](#aws-sdk-instrumentation "#aws-sdk-instrumentation")
- [Instrumenting outgoing HTTP calls](#http-instrumentation "#http-instrumentation")
- [Instrumentation support for other libraries](#other-libraries "#other-libraries")
- [Manually creating trace data](#manual-trace-creation "#manual-trace-creation")
- [Lambda instrumentation](#lambda-instrumentation "#lambda-instrumentation")

## Zero code automatic instrumentation solutions

To trace requests with the X-Ray SDK for Node.js, you must modify your application code. With OpenTelemetry, you can use zero-code auto-instrumentation solutions to trace requests.

**Zero code automatic instrumentation with OpenTelemetry-based automatic instrumentations.**

1. Using the AWS Distro for OpenTelemetry (ADOT) auto-instrumentation for Node.js – For automatic instrumentation for Node.js application, see [Tracing and Metrics with the AWS Distro for OpenTelemetry JavaScript Auto-Instrumentation](https://aws-otel.github.io/docs/getting-started/js-sdk/trace-metric-auto-instr "https://aws-otel.github.io/docs/getting-started/js-sdk/trace-metric-auto-instr").

(Optional) You can also enable CloudWatch Application Signals when automatically instrumenting your applications on AWS with the ADOT JavaScript auto-instrumentation to monitor current application health and track long-term application
performance against your business objectives. Application Signals provides you with a unified, application-centric view of your applications, services, and dependencies, and helps you monitor and triage application health. For more information, see [Application Signals](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.md"). 2. Using the OpenTelemetry JavaScript zero-code automatic instrumentation – For automatic instrumentation with the OpenTelemetry JavaScript, see [JavaScript zero-code instrumentation](https://opentelemetry.io/docs/zero-code/js/ "https://opentelemetry.io/docs/zero-code/js/") .

## Manual instrumentation solutions

Tracing setup with X-Ray SDK
When the X-Ray SDK for Node.js was used, the `aws-xray-sdk` package was required to configure the X-Ray SDK with service plug-ins or local sampling rules before using the SDK to instrument your code.

```

var AWSXRay = require('aws-xray-sdk');

AWSXRay.config([AWSXRay.plugins.EC2Plugin,AWSXRay.plugins.ElasticBeanstalkPlugin]);
AWSXRay.middleware.setSamplingRules(<path to file>);

```

Tracing setup with OpenTelemetry SDK###### Note

AWS X-Ray Remote Sampling is currently not available to be configured for OpenTelemetry JS. However, support for X-Ray Remote Sampling is currently available through the ADOT Auto-Instrumentation for Node.js.

For the code example below, you will need the following dependencies:

```

npm install --save \
  @opentelemetry/api \
  @opentelemetry/sdk-node \
  @opentelemetry/exporter-trace-otlp-proto \
  @opentelemetry/propagator-aws-xray \
  @opentelemetry/resource-detector-aws

```

You must set up and configure the OpenTelemetry SDK before running your application code. This can be done by using the [–-require](https://nodejs.org/api/cli.html#-r---require-module "https://nodejs.org/api/cli.html#-r---require-module") flag. Create a file named
_instrumentation.js_, which will contain your OpenTelemetry instrumentation configuration and setup.

It is recommend that you configure the following components:

- OTLPTraceExporter – Required for exporting traces to the CloudWatch Agent/OpenTelemetry Collector
- AWSXRayPropagator – Required for propagating the Trace Context to AWS Services that are integrated with X-Ray
- Resource Detectors (for example, Amazon EC2 Resource Detector) - To detect metadata of the host running your application

```

/*instrumentation.js*/
// Require dependencies
const { NodeSDK } = require('@opentelemetry/sdk-node');
const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-proto');
const { AWSXRayPropagator } = require("@opentelemetry/propagator-aws-xray");
const { detectResources } = require('@opentelemetry/resources');
const { awsEc2Detector } = require('@opentelemetry/resource-detector-aws');

const resource = detectResources({
    detectors: [awsEc2Detector],
});

const _traceExporter = new OTLPTraceExporter({
    url: 'http://localhost:4318/v1/traces'
});

const sdk = new NodeSDK({
    resource: resource,
    textMapPropagator: new AWSXRayPropagator(),
    traceExporter: _traceExporter
});

sdk.start();

```

Then, you can run your application with your OpenTelemetry setup like:

```

node --require ./instrumentation.js app.js

```

You can use OpenTelemetry SDK library instrumentations to automatically create spans for libraries such as the AWS SDK. Enabling these will automatically create spans for modules such as the AWS SDK for JavaScript v3. OpenTelemetry provides the option to enable all library instrumentations or specify which library instrumentations to enable.

To enable all instrumentations, install the `@opentelemetry/auto-instrumentations-node` package:

```

npm install @opentelemetry/auto-instrumentations-node

```

Next, update the configuration to enable all library instrumentations as shown below.

```
const { getNodeAutoInstrumentations } = require('@opentelemetry/auto-instrumentations-node');

...

const sdk = new NodeSDK({
    resource: resource,
     instrumentations: [getNodeAutoInstrumentations()],
     textMapPropagator: new AWSXRayPropagator(),
    traceExporter: _traceExporter
});
```

Tracing setup with ADOT auto-instrumentation for Node.js
You can use the ADOT auto-instrumentation for Node.js to automatically configure OpenTelemetry for your Node.js applications. By using ADOT Auto-Instrumentation, you do not need
to make manual code changes to trace incoming requests, or to trace libraries such as the AWS SDK or HTTP clients. For more information, see [Tracing and metrics with the AWS Distro for OpenTelemetry JavaScript Auto-Instrumentation](https://aws-otel.github.io/docs/getting-started/js-sdk/trace-metric-auto-instr "https://aws-otel.github.io/docs/getting-started/js-sdk/trace-metric-auto-instr").

ADOT auto-instrumentation for Node.js supports:

- X-Ray remote sampling through environment variable – `export OTEL_TRACES_SAMPLER=xray`
- X-Ray trace context propagation (enabled by default)
- Resource detection (resource detection for Amazon EC2, Amazon ECS, and Amazon EKS environments are enabled by default)
- Automatic library instrumentations for all supported OpenTelemetry instrumentations, which can be disabled/enabled selectively through `OTEL_NODE_ENABLED_INSTRUMENTATIONS` and `OTEL_NODE_DISABLED_INSTRUMENTATIONS` environment variables
- Manual creation of Spans

## Tracing incoming requests

With X-Ray SDK
**Express.js**

With the X-Ray SDK to trace incoming HTTP requests received by _Express.js_ applications, the two middlewares `AWSXRay.express.openSegment(<name>)` and `AWSXRay.express.closeSegment()` were required to wrap all of your defined routes in order to trace them.

```

app.use(xrayExpress.openSegment('defaultName'));

...

app.use(xrayExpress.closeSegment());

```

**Restify**

To trace incoming HTTP requests received by `Restify` applications, the middleware from the X-Ray SDK was used by running enable from the `aws-xray-sdk-restify` module on the Restify Server:

```

var AWSXRay = require('aws-xray-sdk');
var AWSXRayRestify = require('aws-xray-sdk-restify');

var restify = require('restify');
var server = restify.createServer();
AWSXRayRestify.enable(server, 'MyApp'));

```

With OpenTelemetry SDK **Express.js**

Tracing support for incoming requests for `Express.js` is provided by the [OpenTelemetry HTTP instrumentation](https://github.com/open-telemetry/opentelemetry-js/tree/main/experimental/packages/opentelemetry-instrumentation-http "https://github.com/open-telemetry/opentelemetry-js/tree/main/experimental/packages/opentelemetry-instrumentation-http") and
[OpenTelemetry express instrumentation](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/plugins/node/opentelemetry-instrumentation-express "https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/plugins/node/opentelemetry-instrumentation-express"). Install the following dependencies with `npm`:

```

npm install --save @opentelemetry/instrumentation-http @opentelemetry/instrumentation-express

```

Update the OpenTelemetry SDK Configuration to enable instrumentation for the express module:

```

const { HttpInstrumentation } = require('@opentelemetry/instrumentation-http');
const { ExpressInstrumentation } = require('@opentelemetry/instrumentation-express');
...

const sdk = new NodeSDK({
  ...

  instrumentations: [
    ...
    // Express instrumentation requires HTTP instrumentation
    new HttpInstrumentation(),
    new ExpressInstrumentation(),
  ],
});

```

**Restify**

For Restify applications, you will need the [OpenTelemetry Restify instrumentation](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/plugins/node/opentelemetry-instrumentation-restify "https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/plugins/node/opentelemetry-instrumentation-restify"). Install the following dependency:

```

npm install --save @opentelemetry/instrumentation-restify

```

Update the OpenTelemetry SDK Configuration to enable instrumentation for the restify module:

```

const { RestifyInstrumentation } = require('@opentelemetry/instrumentation-restify');
...

const sdk = new NodeSDK({
  ...

  instrumentations: [
    ...
    new RestifyInstrumentation(),
  ],
});

```

## AWS SDK JavaScript V3 instrumentation

With X-Ray SDK
To instrument outgoing AWS requests from AWS SDK, you instrumented clients like the following example:

```

import { S3, PutObjectCommand } from '@aws-sdk/client-s3';

const s3 = AWSXRay.captureAWSv3Client(new S3({}));

await s3.send(new PutObjectCommand({
  Bucket: bucketName,
  Key: keyName,
  Body: 'Hello!',
}));

```

With OpenTelemetry SDKTracing support for downstream AWS SDK calls to DynamoDB, Amazon S3, and others is provided by the OpenTelemetry AWS SDK instrumentation. Install the following dependency with `npm`:

```

npm install --save @opentelemetry/instrumentation-aws-sdk

```

Update the OpenTelemetry SDK Configuration with the AWS SDK instrumentation.

```

import { AwsInstrumentation } from '@opentelemetry/instrumentation-aws-sdk';
...

const sdk = new NodeSDK({
  ...

  instrumentations: [
    ...
    new AwsInstrumentation()
  ],
});

```

## Instrumenting outgoing HTTP calls

With X-Ray SDK
To instrument outgoing HTTP requests with X-Ray, it was required to instrument clients. For example, see below.

Individual HTTP clients

```

var AWSXRay = require('aws-xray-sdk');
var http = AWSXRay.captureHTTPs(require('http'));

```

All HTTP clients (global)

```
var AWSXRay = require('aws-xray-sdk');
AWSXRay.captureHTTPsGlobal(require('http'));
var http = require('http');
```

With OpenTelemetry SDK Tracing support for Node.js HTTP clients is provided by the OpenTelemetry HTTP Instrumentation. Install the following dependency with `npm`:

```

npm install --save @opentelemetry/instrumentation-http

```

Update the OpenTelemetry SDK Configuration as follows:

```

const { HttpInstrumentation } = require('@opentelemetry/instrumentation-http');
...

const sdk = new NodeSDK({
  ...

  instrumentations: [
    ...
    new HttpInstrumentation(),
  ],
});

```

## Instrumentation support for other libraries

You can find the full list of supported library instrumentations for OpenTelemetry JavaScript under [Supported instrumentations](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/metapackages/auto-instrumentations-node#supported-instrumentations "https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/metapackages/auto-instrumentations-node#supported-instrumentations") .

Alternatively, you can search the OpenTelemetry registry to find out if OpenTelemetry supports instrumentation for your library under [Registry](https://opentelemetry.io/ecosystem/registry/ "https://opentelemetry.io/ecosystem/registry/").

## Manually creating trace data

With X-Ray SDK
Using X-Ray, the `aws-xray-sdk` package code was required to manually create segments and their child sub-segments to trace your application.

```

var AWSXRay = require('aws-xray-sdk');

AWSXRay.enableManualMode();

var segment = new AWSXRay.Segment('myApplication');

captureFunc('1', function(subsegment1) {
  captureFunc('2', function(subsegment2) {

  }, subsegment1);
}, segment);

segment.close();
segment.flush();

```

With OpenTelemetry SDK You can create and use custom spans to monitor the performance of internal activities that are not captured by instrumentation libraries. Note that only spans of kind Server are converted into X-Ray segments,
all other spans are converted into X-Ray sub-segments. For more information, see [Segments](xray-concepts.md#xray-concepts-segments "xray-concepts.md#xray-concepts-segments").

You will need a Tracer instance after you have configured the OpenTelemetry SDK in Tracing Setup to create Spans. You can create as many Tracer instances as needed, but it is common to have one Tracer for an entire application.

```

const { trace, SpanKind } = require('@opentelemetry/api');

// Get a tracer instance
const tracer = trace.getTracer('your-tracer-name');

...

  // This span will appear as a segment in X-Ray
  tracer.startActiveSpan('server', { kind: SpanKind.SERVER }, span => {
    // Do work here

    // This span will appear as a subsegment in X-Ray
    tracer.startActiveSpan('operation2', { kind: SpanKind.INTERNAL }, innerSpan => {
      // Do more work here

      innerSpan.end();
    });
    span.end();
  });

```

**Adding annotations and metadata to traces with OpenTelemetry SDK**

You can also add custom key-value pairs as attributes in your spans. Note that by default, all these span attributes will be converted into metadata in X-Ray raw data. To ensure that an attribute is converted into an
annotation and not metadata, add the attribute's key to the list of the `aws.xray.annotations` attribute. For more information, see [Enable The Customized X-Ray Annotations](https://aws-otel.github.io/docs/getting-started/x-ray#enable-the-customized-x-ray-annotations "https://aws-otel.github.io/docs/getting-started/x-ray#enable-the-customized-x-ray-annotations").

```

  tracer.startActiveSpan('server', { kind: SpanKind.SERVER }, span => {
    span.setAttribute('metadataKey', 'metadataValue');
    span.setAttribute('annotationKey', 'annotationValue');

    // The following ensures that "annotationKey: annotationValue" is an annotation in X-Ray raw data.
    span.setAttribute('aws.xray.annotations', ['annotationKey']);

    // Do work here

    span.end();
  });

```

## Lambda instrumentation

With X-Ray SDK
After you enable _Active Tracing_ for your Lambda function, the X-Ray SDK was required without additional configuration. Lambda creates a segment representing the Lambda handler invocation, and you created sub-segments or instrument libraries using the X-Ray SDK without any additional configuration.

With OpenTelemetry SDK You can automatically instrument your Lambda with AWS vended Lambda layers. There are two solutions:

- (Recommended) AWS Lambda Layer for OpenTelemetry

###### Note

This Lambda layer has CloudWatch Application Signals enabled by default, which enables performance and health monitoring for your Lambda application by collecting both metrics and traces. If you only want tracing, you should set the
Lambda environment variable `OTEL_AWS_APPLICATION_SIGNALS_ENABLED=false`. For more information, see [Enable your applications on Lambda](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable-LambdaMain.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable-LambdaMain.md") .

- AWS managed Lambda layer for ADOT JS. For more information, see [AWS Distro for OpenTelemetry Lambda Support For JavaScript](https://aws-otel.github.io/docs/getting-started/lambda/lambda-js "https://aws-otel.github.io/docs/getting-started/lambda/lambda-js").

**Manually creating Spans with Lambda instrumentation**

While the ADOT JavaScript Lambda Layer provides automatic instrumentation for your Lambda function, you might find the need to perform manual instrumentation in your Lambda, for example, to provide custom data or to instrument
code within the Lambda function itself that is not covered by library instrumentations.

To perform manual instrumentation alongside the automatic instrumentation, you will need to add `@opentelemetry/api` as a dependency. The version of this dependency is recommended to be the same version of the same dependency that is used by the ADOT JavaScript SDK.
You can use the OpenTelemetry API to manually create spans in your Lambda function.

To add the `@opentelemetry/api` dependency using NPM:

```

npm install @opentelemetry/api

```
