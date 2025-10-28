# Testing Lambda functions in the console

You can test your Lambda function in the console by invoking your function with a test event.
A _test event_ is a JSON input to your function. If your function doesn't
require input, the event can be an empty document `({})`.

When you run a test in the console, Lambda synchronously invokes your function with
the test event. The function runtime converts the event JSON into an object and passes it
to your code's handler method for processing.

###### Create a test event

Before you can test in the console, you need to create a private or shareable test event.

## Invoking functions with test events

###### To test a function

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Choose the name of the function that you want to test.
3. Choose the **Test** tab.
4. Under **Test event**, choose **Create new event** or **Edit saved event** and then choose the saved event that you want to use.
5. Optionally - choose a **Template** for the event JSON.
6. Choose **Test**.
7. To review the test results, under **Execution result**, expand
   **Details**.

To invoke your function without saving your test event, choose **Test**
before saving. This creates an unsaved test event that Lambda preserves only for the duration of the
session.

For the Node.js, Python, and Ruby runtimes, you can also access your existing saved and unsaved test events on the **Code**
tab. Use the **TEST EVENTS** section to create, edit, and run tests.

## Creating private test events

Private test events are available only to the event creator, and they require no
additional permissions to use. You can create and save up to 10 private test events per function.

###### To create a private test event

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Choose the name of the function that you want to test.
3. Choose the **Test** tab.
4. Under **Test event**, do the following:
   1. Choose a **Template**.
   2. Enter a **Name** for the test.
   3. In the text entry box, enter the JSON test event.
   4. Under **Event sharing settings**, choose
      **Private**.

5. Choose **Save changes**.

For the Node.js, Python, and Ruby runtimes, you can also create test events on the **Code**
tab. Use the **TEST EVENTS** section to create, edit, and run tests.

## Creating shareable test events

Shareable test events are test events that you can share with other users in the same AWS account.
You can edit other users' shareable test events and invoke your function with them.

Lambda saves shareable test events as schemas in an [Amazon EventBridge (CloudWatch Events)
schema registry](../../../eventbridge/latest/userguide/eb-schema-registry.md "../../../eventbridge/latest/userguide/eb-schema-registry.md") named `lambda-testevent-schemas`. As Lambda utilizes this registry
to store and call shareable test events you create, we recommend that you do not edit this registry or create a registry
using the `lambda-testevent-schemas` name.

To see, share, and edit shareable test events, you must have permissions for all of the
following [EventBridge (CloudWatch Events) schema registry API operations](../../../eventbridge/latest/schema-reference/operations.md "../../../eventbridge/latest/schema-reference/operations.md"):

- [`schemas.CreateRegistry`](../../../eventbridge/latest/schema-reference/v1-registries-name-registryname.md#CreateRegistry "../../../eventbridge/latest/schema-reference/v1-registries-name-registryname.md#CreateRegistry")
- [`schemas.CreateSchema`](../../../eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-name-schemaname.md#CreateSchema "../../../eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-name-schemaname.md#CreateSchema")
- [`schemas.DeleteSchema`](../../../eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-name-schemaname.md#DeleteSchema "../../../eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-name-schemaname.md#DeleteSchema")
- [`schemas.DeleteSchemaVersion`](../../../eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-name-schemaname-version-schemaversion.md#DeleteSchemaVersion "../../../eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-name-schemaname-version-schemaversion.md#DeleteSchemaVersion")
- [`schemas.DescribeRegistry`](../../../eventbridge/latest/schema-reference/v1-registries-name-registryname.md#DescribeRegistry "../../../eventbridge/latest/schema-reference/v1-registries-name-registryname.md#DescribeRegistry")
- [`schemas.DescribeSchema`](../../../eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-name-schemaname.md#DescribeSchema "../../../eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-name-schemaname.md#DescribeSchema")
- [`schemas.GetDiscoveredSchema`](../../../eventbridge/latest/schema-reference/v1-discover.md#GetDiscoveredSchema "../../../eventbridge/latest/schema-reference/v1-discover.md#GetDiscoveredSchema")
- [`schemas.ListSchemaVersions`](../../../eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-name-schemaname-versions.md#ListSchemaVersions "../../../eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-name-schemaname-versions.md#ListSchemaVersions")
- [`schemas.UpdateSchema`](../../../eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-name-schemaname.md#UpdateSchema "../../../eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-name-schemaname.md#UpdateSchema")

Note that saving edits made to a shareable test event overwrites that event.

If you cannot create, edit, or see shareable test events, check that your account has the
required permissions for these operations. If you have the required permissions but still
cannot access shareable test events, check for any [resource-based policies](access-control-resource-based.md "access-control-resource-based.md") that might limit
access to the EventBridge (CloudWatch Events) registry.

###### To create a shareable test event

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Choose the name of the function that you want to test.
3. Choose the **Test** tab.
4. Under **Test event**, do the following:
   1. Choose a **Template**.
   2. Enter a **Name** for the test.
   3. In the text entry box, enter the JSON test event.
   4. Under **Event sharing settings**, choose
      **Shareable**.

5. Choose **Save changes**.

###### Use shareable test events with AWS Serverless Application Model.

You can use AWS SAM to invoke shareable test events. See [`sam remote test-event`](../../../serverless-application-model/latest/developerguide/using-sam-cli-remote-test-event.md "../../../serverless-application-model/latest/developerguide/using-sam-cli-remote-test-event.md") in the [AWS Serverless Application Model Developer Guide](../../../serverless-application-model/latest/developerguide/using-sam-cli-remote-test-event.md "../../../serverless-application-model/latest/developerguide/using-sam-cli-remote-test-event.md")

## Deleting shareable test event schemas

When you delete shareable test events, Lambda removes
them from the `lambda-testevent-schemas` registry. If you remove the last shareable test event from the registry, Lambda
deletes the registry.

If you delete the function, Lambda does not delete any associated shareable test event schemas. You must clean
up these resources manually from the [EventBridge (CloudWatch Events) console](https://console.aws.amazon.com/events "https://console.aws.amazon.com/events").
