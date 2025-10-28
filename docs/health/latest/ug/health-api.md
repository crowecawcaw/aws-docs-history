# Integrating AWS Health with other systems using the

AWS Health API

AWS Health is a RESTful web service that uses HTTPS as a transport and JSON as a message
serialization format. Your application code can make requests directly to the AWS Health
API. When you use the REST API directly, you must write the necessary code to sign and
authenticate your requests. For more information about the AWS Health operations and
parameters, see the [AWS Health API Reference](../APIReference.md "../APIReference.md").

###### Note

You must have a Business, Enterprise On-Ramp, or Enterprise Support plan from [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/") to use the AWS Health API. If you call the
AWS Health API from an AWS account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, you
receive a `SubscriptionRequiredException` error.

You can use the AWS SDKs to wrap the AWS Health REST API calls, which can simplify your
application development. You specify your AWS credentials, and these libraries take care
of authentication and request signing for you.

AWS Health also provides a AWS Health Dashboard in the AWS Management Console that you can use to view and search for
events and affected entities. See [Getting started with your
AWS Health Dashboard](getting-started-health-dashboard.md "getting-started-health-dashboard.md").

###### Topics

- [Signing AWS Health API requests](#signing "#signing")
- [Choosing endpoints for AWS Health API requests](#endpoints "#endpoints")
- [Demos: Retrieving the last seven days of
  AWS Health event data programmatically](using-global-endpoints-demo.md "using-global-endpoints-demo.md")
- [Tutorial: Using the AWS Health API with Java
  examples](code-sample-java.md "code-sample-java.md")

## Signing AWS Health API requests

When you use the AWS SDKs or the AWS Command Line Interface (AWS CLI) to make requests to AWS, these
tools automatically sign the requests for you with the access key that you specify when
you configure the tools. For example, if you use the AWS SDK for Java for the previous high
availability endpoint demo, you don't need to sign requests yourself.

###### Java code examples

For more examples on how to use the AWS Health API with the AWS SDK for Java, see this
[example code](code-sample-java.md "code-sample-java.md").

When you make requests, we strongly recommend that you don't use your AWS root
account credentials for regular access to AWS Health. You can use the credentials for
an IAM user. For more information, see [Lock Away Your AWS Account Root User Access Keys](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials") in
the _IAM User Guide_.

If you don’t use the AWS SDKs or the AWS CLI, then you must sign your requests
yourself. We recommend that you use AWS Signature Version 4. For more information, see
[Signing AWS API
Requests](../../../general/latest/gr/signing_aws_api_requests.md "../../../general/latest/gr/signing_aws_api_requests.md") in the _AWS General Reference_.

## Choosing endpoints for AWS Health API requests

The AWS Health API follows a multi-Region application architecture and has two regional
endpoints in an active-passive configuration. To support active-passive DNS failover,
AWS Health provides a single, global endpoint. You can perform a DNS lookup on the
global endpoint to determine the active endpoint and corresponding signing AWS Region.
This helps you know which endpoint to use in your code, so that you can get the latest
information from AWS Health.

When you make a request to the global endpoint, you must specify your AWS access
credentials to the regional endpoint that you target and configure the signing for your
Region. Otherwise, your authentication might fail. For more information, see [Signing AWS Health API requests](#signing "#signing").

For IPv6-only requests, we recommend performing a DNS lookup on the global endpoint to determine the active AWS Region and then calling the IPv6 supported dual-stack endpoint for that Region.

The following table represents the default configuration.

| Description | Signing Region                                                           | Endpoint                                                                                      | Protocol |
| ----------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active      | us-east-1                                                                | health.us-east-1.amazonaws.com (IPv4-only) health.us-east-1.api.aws (IPv4 and IPv6 supported) | HTTPS    |
| Passive     | us-east-2                                                                | health.us-east-2.amazonaws.com (IPv4-only) health.us-east-2.api.aws (IPv4 and IPv6 supported) | HTTPS    |
| Global      | us-east-1 NoteThis is the signing Region of the current active endpoint. | global.health.amazonaws.com                                                                   | HTTPS    | To determine if an endpoint is the _active endpoint_, do a DNS lookup on the _global endpoint_ CNAME, and then extract the AWS Region from the resolved name. ###### Example : DNS lookup on global endpoint The following command completes a DNS lookup on the global.health.amazonaws.com endpoint. The command then returns the us-east-1 Region endpoint. This output tells you which endpoint you should use for AWS Health. ``` `dig global.health.amazonaws.com | grep CNAME` `global.health.amazonaws.com. 10 IN CNAME health.us-east-1.amazonaws.com` ``` ###### Tip Both the active and passive endpoints return AWS Health data. However, the latest AWS Health data is only available from the active endpoint. Data from the passive endpoint will be eventually consistent with the active endpoint. We recommend that you restart any workflows when the active endpoint changes. |
