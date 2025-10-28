# Authorization with Amazon Cognito identities

There are two types of Amazon Cognito identities: unauthenticated and authenticated. If
your app supports unauthenticated Amazon Cognito identities, no authentication is performed,
so you don't know who the user is.

**Unauthenticated Identities:** For unauthenticated
Amazon Cognito identities, you grant permissions by attaching an IAM role to an
unauthenticated identity pool. We recommend that you only grant access to those
resources you want available to unknown users.

###### Important

For unauthenticated Amazon Cognito users connecting to AWS IoT Core, we recommend that you
give access to very limited resources in IAM policies.

**Authenticated Identities:** For authenticated Amazon Cognito
identities, you need to specify permissions in two places:

- Attach an IAM policy to the authenticated Amazon Cognito Identity pool and

- Attach an AWS IoT Core policy to the Amazon Cognito Identity (authenticated user).

## Policy examples for

unauthenticated and authenticated Amazon Cognito users connecting to
AWS IoT Core

The following example shows permissions in both the IAM policy and the IoT
policy of an Amazon Cognito identity. The authenticated user wants to publish to a device
specific topic (e.g. device/DEVICE_ID/status).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iot:Connect"
 ],
 "Resource": [
 "arn:aws:iot:us-east-1:123456789012:client/`Client_ID`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iot:Publish"
 ],
 "Resource": [
 "arn:aws:iot:us-east-1:123456789012:topic/device/`Device_ID`/status"
 ]
 }
 ]
}`

```

The following example shows the permissions in an IAM policy of an Amazon Cognito
unauthenticated role. The unauthenticated user wants to publish to non-device
specific topics that do not require authentication.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iot:Connect"
 ],
 "Resource": [
 "arn:aws:iot:us-east-1:123456789012:client/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iot:Publish"
 ],
 "Resource": [
 "arn:aws:iot:us-east-1:123456789012:topic/`non_device_specific_topic`"
 ]
 }
 ]
}`

```

## GitHub examples

The following example web applications on GitHub show how to incorporate policy
attachment to authenticated users into the user signup and authentication
process.

- [MQTT publish/subscribe React web application using AWS Amplify and
  the AWS IoT Device SDK for JavaScript](https://github.com/aws-samples/aws-amplify-react-iot-pub-sub-using-cp "https://github.com/aws-samples/aws-amplify-react-iot-pub-sub-using-cp")
- [MQTT publish/subscribe React web application using AWS Amplify, the
  AWS IoT Device SDK for JavaScript, and a Lambda function](https://github.com/aws-samples/aws-amplify-react-iot-pub-sub-using-lambda "https://github.com/aws-samples/aws-amplify-react-iot-pub-sub-using-lambda")
  Amplify is a set of tools and services that helps you build web and mobile
  applications that integrate with AWS services. For more information about
  Amplify, see [Amplify Framework
  Documentation,](https://docs.amplify.aws/ "https://docs.amplify.aws/").

Both examples perform the following steps.

1. When a user signs up for an account, the application creates an Amazon Cognito user
   pool and identity.
2. When a user authenticates, the application creates and attaches a policy
   to the identity. This gives the user publish and subscribe
   permissions.
3. The user can use the application to publish and subscribe to MQTT
   topics.
   The first example uses the `AttachPolicy` API operation directly inside
   the authentication operation. The following example demonstrates how to implement
   this API call inside a React web application that uses Amplify and the
   AWS IoT Device SDK for JavaScript.

```

function attachPolicy(id, policyName) {
    var Iot = new AWS.Iot({region: AWSConfiguration.region, apiVersion: AWSConfiguration.apiVersion, endpoint: AWSConfiguration.endpoint});
    var params = {policyName: policyName, target: id};

    console.log("Attach IoT Policy: " + policyName + " with cognito identity id: " + id);
    Iot.attachPolicy(params, function(err, data) {
         if (err) {
               if (err.code !== 'ResourceAlreadyExistsException') {
                  console.log(err);
               }
          }
         else  {
            console.log("Successfully attached policy with the identity", data);
         }
     });
}

```

This code appears in the [AuthDisplay.js](https://github.com/aws-samples/aws-amplify-react-iot-pub-sub-using-cp/blob/d1c307b36357be934db9dda020140fa337709cd9/src/AuthDisplay.js#L45 "https://github.com/aws-samples/aws-amplify-react-iot-pub-sub-using-cp/blob/d1c307b36357be934db9dda020140fa337709cd9/src/AuthDisplay.js#L45") file.

The second example implements the `AttachPolicy` API operation in a
Lambda function. The following example shows how the Lambda uses this API call.

```

iot.attachPolicy(params, function(err, data) {
     if (err) {
           if (err.code !== 'ResourceAlreadyExistsException') {
              console.log(err);
              res.json({error: err, url: req.url, body: req.body});
           }
      }
     else  {
        console.log(data);
        res.json({success: 'Create and attach policy call succeed!', url: req.url, body: req.body});
     }
 });

```

This code appears inside the `iot.GetPolicy` function in the [app.js](https://github.com/aws-samples/aws-amplify-react-iot-pub-sub-using-lambda/blob/e493039581d2aff0faa3949086deead20a2c5385/amplify/backend/function/amplifyiotlambda/src/app.js#L50 "https://github.com/aws-samples/aws-amplify-react-iot-pub-sub-using-lambda/blob/e493039581d2aff0faa3949086deead20a2c5385/amplify/backend/function/amplifyiotlambda/src/app.js#L50") file.

###### Note

When you call the function with AWS credentials that you obtain through
Amazon Cognito Identity pools, the context object in your Lambda function contains a value for
`context.cognito_identity_id`. For more information, see the
following.

- [AWS Lambda context object
  in Node.js](../../../lambda/latest/dg/nodejs-context.md "../../../lambda/latest/dg/nodejs-context.md")
- [AWS Lambda context object
  in Python](../../../lambda/latest/dg/python-context.md "../../../lambda/latest/dg/python-context.md")
- [AWS Lambda context object
  in Ruby](../../../lambda/latest/dg/ruby-context.md "../../../lambda/latest/dg/ruby-context.md")
- [AWS Lambda context object
  in Java](../../../lambda/latest/dg/java-context.md "../../../lambda/latest/dg/java-context.md")
- [AWS Lambda context object
  in Go](../../../lambda/latest/dg/golang-context.md "../../../lambda/latest/dg/golang-context.md")
- [AWS Lambda context object
  in C#](../../../lambda/latest/dg/csharp-context.md "../../../lambda/latest/dg/csharp-context.md")
- [AWS Lambda context
  object in PowerShell](../../../lambda/latest/dg/powershell-context.md "../../../lambda/latest/dg/powershell-context.md")
