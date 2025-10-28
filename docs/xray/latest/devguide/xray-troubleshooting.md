# Troubleshooting AWS X-Ray

This topic lists common errors and issues that you might encounter when using the X-Ray
API, console, or SDKs. If you find an issue that is not listed here, you can use the
**Feedback** button on this page to report it.

###### Sections

- [X-Ray trace map and trace details pages](#xray-console-troubleshooting "#xray-console-troubleshooting")
- [X-Ray SDK for Java](#troubleshooting-java "#troubleshooting-java")
- [X-Ray SDK for Node.js](#troubleshooting-nodejs "#troubleshooting-nodejs")
- [The X-Ray daemon](#troubleshooting-daemon "#troubleshooting-daemon")

## X-Ray trace map and trace details pages

The following sections can help if you're having issues using the X-Ray trace map and Trace details page:

### I don't see all of my CloudWatch logs

How to configure logs so that they appear in the X-Ray trace map and trace details pages depends on the
service.

- API Gateway logs appear if logging is turned on in API Gateway.

Not all service map nodes support viewing the associated logs. View logs for the following node types:

- Lambda context
- Lambda function
- API Gateway stage
- Amazon ECS cluster
- Amazon ECS instance
- Amazon ECS service
- Amazon ECS task
- Amazon EKS cluster
- Amazon EKS namespace
- Amazon EKS node
- Amazon EKS pod
- Amazon EKS service

### I don't see all of my alarms on the X-Ray trace map

The X-Ray trace map shows only the alert icon for a node if any alarms that are associated with that node
are in the ALARM state.

The trace map associates alarms with nodes using the following logic:

- If the node represents an AWS service, then all alarms with the namespace associated with that service are associated with the node.
  For example, a node of type `AWS::Kinesis` is linked with all alarms that are based on metrics in the CloudWatch namespace `AWS/Kinesis`.
- If the node represents an AWS resource, then the alarms on that specific resource are linked. For example, a node of
  type `AWS::DynamoDB::Table` with the name “MyTable” is linked to all alarms that are based on a metric with the namespace
  `AWS/DynamoDB` and have the `TableName` dimension set to `MyTable`.
- If the node is of unknown type, which is identified by a dashed border around the
  name, then no alarms are associated with that node.

### I don't see some AWS

resources on the trace map

Not every AWS resource is represented by a dedicated node. Some AWS services are represented by a single node
for all requests to the service. The following resource types are displayed with a node per resource:

- `AWS::DynamoDB::Table`
- `AWS::Lambda::Function`

Lambda functions are represented by two nodes—one for the Lambda container, and one for the
function. This helps to identify cold start problems with Lambda functions. Lambda container nodes are
associated with alarms and dashboards in the same way as Lambda function nodes.

- `AWS::ApiGateway::Stage`
- `AWS::SQS::Queue`
- `AWS::SNS::Topic`

### There are too many nodes on the trace map

Use X-Ray groups to break your map into multiple maps. For more information, see
[Using Filter Expressions with Groups](xray-console-filters.md#groups "xray-console-filters.md#groups").

## X-Ray SDK for Java

**Error:**
_Exception in thread "Thread-1"
com.amazonaws.xray.exceptions.SegmentNotFoundException: Failed to begin subsegment named
'AmazonSNS': segment cannot be found._

This error indicates that the X-Ray SDK attempted to record an outgoing call to AWS,
but couldn't find an open segment. This can occur in the following situations:

- **A servlet filter is not configured** – The
  X-Ray SDK creates segments for incoming requests with a filter named
  `AWSXRayServletFilter`. [Configure a
  servlet filter](xray-sdk-java-filters.md "xray-sdk-java-filters.md") to instrument incoming requests.
- **You're using instrumented clients outside of servlet
  code** – If you use an instrumented client to make calls in startup code
  or other code that doesn't run in response to an incoming request, you must create a
  segment manually. See [Instrumenting startup code](scorekeep-startup.md "scorekeep-startup.md") for examples.
- **You're using instrumented clients in worker threads**
  – When you create a new thread, the X-Ray recorder loses its reference to the open
  segment. You can use the [`getTraceEntity`](../../../xray-sdk-for-java/latest/javadoc/com/amazonaws/xray/AWSXRayRecorder.md#getTraceEntity-- "../../../xray-sdk-for-java/latest/javadoc/com/amazonaws/xray/AWSXRayRecorder.md#getTraceEntity--") and [`setTraceEntity`](../../../xray-sdk-for-java/latest/javadoc/com/amazonaws/xray/AWSXRayRecorder.md#setTraceEntity-- "../../../xray-sdk-for-java/latest/javadoc/com/amazonaws/xray/AWSXRayRecorder.md#setTraceEntity--") methods to get a reference to the current segment
  or subsegment ([`Entity`](../../../xray-sdk-for-java/latest/javadoc/com/amazonaws/xray/entities/Entity.md "../../../xray-sdk-for-java/latest/javadoc/com/amazonaws/xray/entities/Entity.md")), and pass it back to the recorder inside of the thread.
  See [Using instrumented clients in worker threads](scorekeep-workerthreads.md "scorekeep-workerthreads.md") for
  an example.

## X-Ray SDK for Node.js

**Issue:**
_CLS does not work with Sequelize_

Pass the X-Ray SDK for Node.js namespace to Sequelize with the `cls` method.

```
var AWSXRay = require('aws-xray-sdk');
const Sequelize = require('sequelize');
`Sequelize.cls = AWSXRay.getNamespace();`
const sequelize = new Sequelize(`...`);
```

**Issue:**
_CLS does not work with Bluebird_

Use `cls-bluebird` to get Bluebird working with CLS.

```
var AWSXRay = require('aws-xray-sdk');
var Promise = require('bluebird');
var clsBluebird = require('cls-bluebird');
`clsBluebird(AWSXRay.getNamespace());`
```

## The X-Ray daemon

**Issue:**
_The daemon is using the wrong credentials_

The daemon uses the AWS SDK to load credentials. If you use multiple methods of providing
credentials, the method with the highest precedence is used. See [Running the daemon](xray-daemon.md#xray-daemon-running "xray-daemon.md#xray-daemon-running") for more
information.
