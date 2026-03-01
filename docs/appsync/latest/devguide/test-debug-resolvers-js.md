# Testing and debugging resolvers in AWS AppSync (JavaScript)

AWS AppSync executes resolvers on a GraphQL field against a data source. When working with pipeline
resolvers, functions interact with your data sources. As described in the [JavaScript resolvers overview](resolver-reference-overview-js.md "resolver-reference-overview-js.md"),
functions communicate with data sources by using request and response handlers written in JavaScript and running
on the `APPSYNC_JS` runtime. This enables you to provide custom logic and conditions before and after
communicating with the data source.

To help developers write, test, and debug these resolvers, the AWS AppSync console also provides tools to create
a GraphQL request and response with mock data down to the individual field resolver. Additionally, you can
perform queries, mutations, and subscriptions in the AWS AppSync console and see a detailed log stream of the
entire request from Amazon CloudWatch. This includes results from the data source.

## Testing with mock data

When a GraphQL resolver is invoked, it contains a `context` object that has relevant
information about the request. This includes arguments from a client, identity information, and data from
the parent GraphQL field. It also stores the results from the data source, which can be used in the response
handler. For more information about this structure and the available helper utilities to use when
programming, see the [Resolver context object
reference](resolver-context-reference-js.md "resolver-context-reference-js.md").

When writing or editing a resolver function, you can pass a _mock_ or _test
context_ object into the console editor. This enables you to see how both the request and the
response handlers
evaluate without actually running against a data source. For example, you can pass a test `firstname:
 Shaggy` argument and see how it evaluates when using `ctx.args.firstname` in your
template code. You could also test the evaluation of any utility helpers such as `util.autoId()`
or `util.time.nowISO8601()`.

### Testing resolvers

This example will use the AWS AppSync console to test resolvers.

1. Sign in to the AWS Management Console and open the [AppSync
   console](https://console.aws.amazon.com/appsync/ "https://console.aws.amazon.com/appsync/").
   1. In the **APIs dashboard**, choose your GraphQL
      API.
   2. In the **Sidebar**, choose **Functions**.

2. Choose an existing
   function.
3. At the top of the **Update function** page, choose **Select test context**, then choose **Create new
   context**.
4. Select a sample context object or populate the JSON manually in the **Configure test context** window below.
5. Enter a **Text context name**.
6. Choose the **Save** button.
7. To evaluate your
   resolver using this mocked context object, choose **Run
   Test**.

For a more practical example, suppose you have an app storing a GraphQL type of `Dog` that
uses automatic ID generation for objects and stores them in Amazon DynamoDB. You also want to write some
values from the arguments of a GraphQL mutation and allow only specific users to see a response. The
following snippet shows what the schema might look like:

```
type Dog {
  breed: String
  color: String
}

type Mutation {
  addDog(firstname: String, age: Int): Dog
}
```

You can write an AWS AppSync function and add it to your `addDog` resolver to handle the
mutation. To test your AWS AppSync function, you can populate a context object like the following example.
The following has arguments from the client of `name` and `age`, and a
`username` populated in the `identity` object:

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

You can test your AWS AppSync
function using the following code:

```
import { util } from '@aws-appsync/utils';

export function request(ctx) {
  return {
    operation: 'PutItem',
    key: util.dynamodb.toMapValues({ id: util.autoId() }),
    attributeValues: util.dynamodb.toMapValues(ctx.args),
  };
}

export function response(ctx) {
  if (ctx.identity.username === 'Nadia') {
    console.log("This request is allowed")
    return ctx.result;
  }
  util.unauthorized();
}
```

The evaluated request and
response handler has the data from your test context object and the generated value
from `util.autoId()`. Additionally, if you were to change the `username` to a
value other than `Nadia`, the results won’t be returned because the authorization check would
fail. For more information about fine-grained access control, see [Authorization use cases](security-authorization-use-cases.md#aws-appsync-security-authorization-use-cases "security-authorization-use-cases.md#aws-appsync-security-authorization-use-cases").

### Testing request and response handlers with AWS AppSync's APIs

You can use the
`EvaluateCode`
API command to remotely test your
code with mocked
data. To get started with the command, make sure you have added the
`appsync:evaluateMappingCode`
permission to your policy. For example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "appsync:evaluateCode",
 "Resource": "arn:aws:appsync:us-east-1:111122223333:*"
 }
 ]
}`

```

You can leverage the command by using the [AWS CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/") or
[AWS SDKs](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/"). For example, take the
`Dog` schema and its
AWS AppSync function request and
response handlers from the previous section. Using the CLI on your local station, save
the code to a
file named
`code.js`,
then save the `context` object to a file named `context.json`. From your shell,
run the following command:

```
$ aws appsync evaluate-code \
  --code file://code.js \
  --function response \
  --context file://context.json \
  --runtime name=APPSYNC_JS,runtimeVersion=1.0.0
```

The response contains an `evaluationResult` containing the payload returned by your
handler. It also contains a `logs` object, that holds the list of logs that were generated by
your handler during the evaluation. This makes it easy to debug your code execution and see information
about your evaluation to help troubleshoot. For example:

```
{
    "evaluationResult": "{\"breed\":\"Miniature Schnauzer\",\"color\":\"black_grey\"}",
    "logs": [
        "INFO - code.js:13:5: \"This request is allowed\""
    ]
}
```

The
`evaluationResult` can
be parsed as JSON, which gives:

```
{
  "breed": "Miniature Schnauzer",
  "color": "black_grey"
}
```

Using the SDK, you can easily incorporate tests from your favorite test suite to validate your
handlers'
behavior. We recommend creating tests using the [Jest Testing
Framework](https://jestjs.io/ "https://jestjs.io/"), but any testing suite works. The following snippet shows a hypothetical
validation run. Note that we expect the evaluation response to be valid JSON, so we use
`JSON.parse` to retrieve JSON from the string response:

```
const AWS = require('aws-sdk')
const fs = require('fs')
const client = new AWS.AppSync({ region: 'us-east-2' })
const runtime = {name:'APPSYNC_JS',runtimeVersion:'1.0.0')

test('request correctly calls DynamoDB', async () => {
  const code = fs.readFileSync('./code.js', 'utf8')
  const context = fs.readFileSync('./context.json', 'utf8')
  const contextJSON = JSON.parse(context)

  const response = await client.evaluateCode({ code, context, runtime, function: 'request' }).promise()
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
Snapshots: 0 totalTime: 1.511 s, estimated 2 s
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
response logs for the operation are streamed to this section and you can view them in the console.
