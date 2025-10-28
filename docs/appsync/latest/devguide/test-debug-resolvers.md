# Testing and debugging resolvers in AWS AppSync (VTL)

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please consider using the
APPSYNC_JS runtime and its guides [here](configuring-resolvers-js.md "configuring-resolvers-js.md").

AWS AppSync executes resolvers on a GraphQL field against a data source. As described in [Resolver mapping template
overview](resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview "resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview"), resolvers communicate with data sources by using a templating language. This enables you to
customize the behavior and apply logic and conditions before and after communicating with the data source. For
an introductory tutorial-style programming guide for writing resolvers, see the [Resolver mapping template
programming guide](resolver-mapping-template-reference-programming-guide.md#aws-appsync-resolver-mapping-template-reference-programming-guide "resolver-mapping-template-reference-programming-guide.md#aws-appsync-resolver-mapping-template-reference-programming-guide").

To help developers write, test, and debug these resolvers, the AWS AppSync console also provides tools to create
a GraphQL request and response with mock data down to the individual field resolver. Additionally, you can
perform queries, mutations, and subscriptions in the AWS AppSync console and see a detailed log stream from
Amazon CloudWatch of the entire request. This includes results from a data source.

## Testing with mock data

When a GraphQL resolver is invoked, it contains a `context` object that contains information
about the request. This includes arguments from a client, identity information, and data from the parent
GraphQL field. It also contains the results from the data source, which can be used in the response
template. For more information about this structure and the available helper utilities to use when
programming, see the [Resolver
Mapping Template Context Reference](resolver-context-reference.md#aws-appsync-resolver-mapping-template-context-reference "resolver-context-reference.md#aws-appsync-resolver-mapping-template-context-reference").

When writing or editing a resolver, you can pass a _mock_ or _test
context_ object into the console editor. This enables you to see how both the request and the
response templates evaluate without actually running against a data source. For example, you can pass a test
`firstname: Shaggy` argument and see how it evaluates when using
`$ctx.args.firstname` in your template code. You could also test the evaluation of any
utility helpers such as `$util.autoId()` or `util.time.nowISO8601()`.

### Testing resolvers

This example will use the AWS AppSync console to test resolvers.

1. Sign in to the AWS Management Console and open the [AppSync
   console](https://console.aws.amazon.com/appsync/ "https://console.aws.amazon.com/appsync/").
   1. In the **APIs dashboard**, choose your GraphQL
      API.
   2. In the **Sidebar**, choose **Schema**.

2. If you haven't done so already, under the type and next to the field, choose **Attach** to add your resolver.

For more information on how to build a conplete resolver, see [Configuring
resolvers](configuring-resolvers.md "configuring-resolvers.md").

Otherwise, select the resolver that's already in the field. 3. At the top of the **Edit resolver** page, choose **Select test context**, choose **Create new
context**. 4. Select a sample context object or populate the JSON manually in the **Execution context** window below. 5. Enter in a **Text context name**. 6. Choose the **Save** button. 7. At the top of the **Edit Resolver** page, choose **Run test**.

For a more practical example, suppose you have an app storing a GraphQL type of `Dog` that
uses automatic ID generation for objects and stores them in Amazon DynamoDB. You also want to write some
values from the arguments of a GraphQL mutation, and allow only specific users to see a response. The
following shows what the schema might look like:

```
type Dog {
  breed: String
  color: String
}

type Mutation {
  addDog(firstname: String, age: Int): Dog
}
```

When you add a resolver for the `addDog` mutation, you can populate a context object like
the following example. The following has arguments from the client of `name` and
`age`, and a `username` populated in the `identity` object:

```
{
    "arguments" : {
        "firstname": "Shaggy",
        "age": 4
    },
    "source" : {},
    "result" : {
        "breed" : "Miniature Schnauzer",
        "color" : "black_grey"
    },
    "identity": {
        "sub" : "uuid",
        "issuer" : " https://cognito-idp.{region}.amazonaws.com/{userPoolId}",
        "username" : "Nadia",
        "claims" : { },
        "sourceIp" :[  "x.x.x.x" ],
        "defaultAuthStrategy" : "ALLOW"
    }
}
```

You can test this using the following request and response mapping
templates:

**Request Template**

```
{
    "version" : "2017-02-28",
    "operation" : "PutItem",
    "key" : {
        "id" : { "S" : "$util.autoId()" }
    },
    "attributeValues" : $util.dynamodb.toMapValuesJson($ctx.args)
}
```

**Response Template**

```
#if ($context.identity.username == "Nadia")
  $util.toJson($ctx.result)
#else
  $util.unauthorized()
#end
```

The evaluated template has the data from your test context object and the generated value from
`$util.autoId()`. Additionally, if you were to change the `username` to a
value other than `Nadia`, the results won’t be returned because the authorization check would
fail. For more information about fine grained access control, see [Authorization use cases](security-authorization-use-cases.md#aws-appsync-security-authorization-use-cases "security-authorization-use-cases.md#aws-appsync-security-authorization-use-cases").

### Testing mapping templates with AWS AppSync's APIs

You can use the `EvaluateMappingTemplate` API command to remotely test
your mapping templates with mocked data. To get started with the command, make sure
you have added the `appsync:evaluateMappingTemplate` permission to your
policy. For example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "appsync:evaluateMappingTemplate",
 "Resource": "arn:aws:appsync:us-east-1:111122223333:*"
 }
 ]
}`

```

You can leverage the command by using the [AWS CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/") or [AWS SDKs](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/").
For example, take the `Dog` schema and its request/response mapping
templates from the previous section. Using the CLI on your local station, save the
request template to a file named `request.vtl`, then save the
`context` object to a file named `context.json`. From your
shell, run the following command:

```
aws appsync evaluate-mapping-template --template file://request.vtl --context file://context.json
```

The command returns the following response:

```
{
  "evaluationResult": "{\n    \"version\" : \"2017-02-28\",\n    \"operation\" : \"PutItem\",\n    \"key\" : {\n        \"id\" : { \"S\" : \"afcb4c85-49f8-40de-8f2b-248949176456\" }\n    },\n    \"attributeValues\" : {\"firstname\":{\"S\":\"Shaggy\"},\"age\":{\"N\":4}}\n}\n"
}
```

The `evaluationResult` contains the results of testing your provided
template with the provided `context`. You can also test your templates
using the AWS SDKs. Here's an example using the AWS SDK for JavaScript V2:

```
const AWS = require('aws-sdk')
const client = new AWS.AppSync({ region: 'us-east-2' })

const template = fs.readFileSync('./request.vtl', 'utf8')
const context = fs.readFileSync('./context.json', 'utf8')

client
  .evaluateMappingTemplate({ template, context })
  .promise()
  .then((data) => console.log(data))
```

Using the SDK, you can easily incorporate tests from your favorite test suite to
validate your template's behavior. We recommend creating tests using the [Jest Testing Framework](https://jestjs.io/ "https://jestjs.io/"), but any testing suite
works. The following snippet shows a hypothetical validation run. Note that we
expect the evaluation response to be valid JSON, so we use `JSON.parse`
to retrieve JSON from the string response:

```
const AWS = require('aws-sdk')
const fs = require('fs')
const client = new AWS.AppSync({ region: 'us-east-2' })

test('request correctly calls DynamoDB', async () => {
  const template = fs.readFileSync('./request.vtl', 'utf8')
  const context = fs.readFileSync('./context.json', 'utf8')
  const contextJSON = JSON.parse(context)

  const response = await client.evaluateMappingTemplate({ template, context }).promise()
  const result = JSON.parse(response.evaluationResult)

  expect(result.key.id.S).toBeDefined()
  expect(result.attributeValues.firstname.S).toEqual(contextJSON.arguments.firstname)
})
```

This yields the following result:

```
Ran all test suites.
> jest

PASS ./index.test.js
✓ request correctly calls DynamoDB (543 ms)

Test Suites: 1 passed, 1 total
Tests: 1 passed, 1 total
Snapshots: 0 total
Time: 1.511 s, estimated 2 s
```

## Debugging a live query

There’s no substitute for an end-to-end test and logging to debug a production
application. AWS AppSync lets you log errors and full request details using Amazon CloudWatch.
Additionally, you can use the AWS AppSync console to test GraphQL queries, mutations, and
subscriptions and live stream log data for each request back into the query editor to
debug in real time. For subscriptions, the logs display connection-time
information.

To perform this, you need to have Amazon CloudWatch logs enabled in advance, as described in [Monitoring and logging](monitoring.md#aws-appsync-monitoring "monitoring.md#aws-appsync-monitoring"). Next, in the AWS AppSync console, choose
the **Queries** tab and then enter a valid GraphQL query. In the lower-right
section, click and drag the **Logs** window to open the logs view. At the top
of the page, choose the play arrow icon to run your GraphQL query. In a few moments, your full request and
response logs for the operation are streamed to this section and you can view then in the console.
