# Using AWS X-Ray to trace requests in AWS AppSync

You can use [AWS X-Ray](../../../xray/latest/devguide/aws-xray.md "../../../xray/latest/devguide/aws-xray.md") to trace requests as they are
executed in AWS AppSync. You can use X-Ray with AWS AppSync in all AWS Regions where
X-Ray is available. X-Ray gives you a detailed overview of an entire GraphQL request. This
enables you to analyze latencies in your APIs and their underlying resolvers and data sources.
You can use an X-Ray service map to view the latency of a request, including any AWS services
that are integrated with X-Ray. You can also configure sampling rules to tell X-Ray which
requests to record, and at what sampling rates, according to criteria that you specify.

For more information about sampling in X-Ray, see [Configuring Sampling
Rules in the AWS X-Ray Console](../../../xray/latest/devguide/xray-console-sampling.md "../../../xray/latest/devguide/xray-console-sampling.md").

## Setup and Configuration

You can enable X-Ray tracing for a GraphQL API through the AWS AppSync
console.

1. Sign in to the AWS AppSync console.
2. Choose **Settings** from the navigation panel.
3. Under **X-Ray**, turn on **Enable
   X-Ray**.
4. Choose **Save**. X-Ray tracing is now enabled for
   your API.

If you’re using the AWS CLI or AWS CloudFormation, you can also enable X-Ray tracing
when you create a new AWS AppSync API, or update an existing AWS AppSync API, by
setting the `xrayEnabled` property to `true`.

When X-Ray tracing is enabled for an AWS AppSync API, an AWS Identity and Access Management [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") is automatically created in your account with the
appropriate permissions. This allows AWS AppSync to send traces to X-Ray in a secure
way.

## Tracing Your API with X-Ray

### Sampling

By using sampling rules, you can control the amount of data that you record in
AWS AppSync, and can modify sampling behavior on the fly without modifying or
redeploying your code. For example, this rule samples requests to the GraphQL API with
the API ID `3n572shhcpfokwhdnq1ogu59v6`.

- **Rule name** — `test-sample`
- **Priority** — `10`
- **Reservoir size** — `10`
- **Fixed rate** — `10`
- **Service name** — `*`
- **Service type** —
  `AWS::AppSync::GraphQLAPI`
- **HTTP method** — `*`
- **Resource ARN** —
  `arn:aws:appsync:us-west-2:123456789012:apis/3n572shhcpfokwhdnq1ogu59v6`
- **Host** — `*`

### Understanding Traces

When you enable X-Ray tracing for your GraphQL API, you can use the X-Ray trace
detail page to examine detailed latency information about requests made to your API. The
following example shows the trace view along with the service map for this specific
request. The request was made to an API called `postAPI` with a Post type,
whose data is contained in an Amazon DynamoDB table called
`PostTable-Example`.

The following trace image corresponds to the following GraphQL query:

```
query getPost {
    getPost(id: "1") {
      id
      title
    }
}
```

The resolver for the `getPost` query uses the underlying DynamoDB data
source. The following trace view shows the call to DynamoDB, as well as the latencies of
various parts of the query’s execution:

![Trace view showing client request, postAPI, and DynamoDB with durations and request details.](images/xray-getpost-trace-view.png)

- In the preceding image, `/getPost` represents the complete path to
  the element that is being resolved. In this case, because `getPost` is
  a field on the root `Query` type, it appears directly after the root of
  the path.
- `requestMappingTemplateEvaluation` represents the time spent by
  AWS AppSync evaluating the request mapping template for this element in the
  query.
- `Query.getPost` represents a type and field (in `Type.field`
  format). It can contain multiple subsegments, depending on the structure of the
  API and the request being traced.
  - `DynamoDB` represents the data source that is attached to this
    resolver. It contains the latency for the network call to DynamoDB to resolve
    the field.
  - `responseMappingTemplateEvaluation` represents the time spent by
    AWS AppSync evaluating the response mapping template for this element in
    the query.

When you view traces in X-Ray, you can get additional contextual and metadata
information about the subsegments in the AWS AppSync segment by choosing the
subsegments and exploring the detailed view.

For certain deeply nested or complex queries, note that the segment delivered to
X-Ray by AWS AppSync can be larger than the maximum size allowed for segment
documents, as defined in [AWS X-Ray
Segment Documents](../../../xray/latest/devguide/xray-api-segmentdocuments.md "../../../xray/latest/devguide/xray-api-segmentdocuments.md"). X-Ray doesn’t display segments that exceed the
limit.
