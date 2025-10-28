# Defining your Lambda function

When AWS IoT Core invokes your authorizer, it triggers the associated Lambda
associated with the authorizer with an event that contains the following JSON
object. The example JSON object contains all of the possible fields. Any fields
that aren't relevant to the connection request aren't included.

```
{
    "token" :"aToken",
    "signatureVerified": Boolean, // Indicates whether the device gateway has validated the signature.
    "protocols": ["tls", "http", "mqtt"], // Indicates which protocols to expect for the request.
    "protocolData": {
        "tls" : {
            "serverName": "serverName" // The server name indication (SNI) `host_name` string.
        },
        "http": {
            "headers": {
                "#{name}": "#{value}"
            },
            "queryString": "?#{name}=#{value}"
        },
        "mqtt": {
            "username": "myUserName",
            "password": "myPassword", // A base64-encoded string.
            "clientId": "myClientId" // Included in the event only when the device sends the value.
        }
    },
    "connectionMetadata": {
        "id": UUID // The connection ID. You can use this for logging.
    },
}
```

The Lambda function should use this information to authenticate the incoming
connection and decide what actions are permitted in the connection. The function
should send a response that contains the following values.

- `isAuthenticated`: A Boolean value that indicates whether the
  request is authenticated.
- `principalId`: An alphanumeric string that acts as an
  identifier for the token sent by the custom authorization request. The
  value must be an alphanumeric string with at least one, and no more than
  128, characters and match this regular expression (regex) pattern:
  `([a-zA-Z0-9]){1,128}`. Special characters that are not
  alphanumeric are not allowed for use with the `principalId`
  in AWS IoT Core. Refer to the documentation for other AWS services if
  non-alphanumeric special characters are allowed for the
  `principalId`.
- `policyDocuments`: A list of JSON-formatted AWS IoT Core policy
  documents For more information about creating AWS IoT Core policies, see
  [AWS IoT Core policies](iot-policies.md "iot-policies.md"). The maximum number of policy
  documents is 10 policy documents. Each policy document can contain a
  maximum of 2,048 characters.
- `disconnectAfterInSeconds`: An integer that specifies the
  maximum duration (in seconds) of the connection to the AWS IoT Core
  gateway. The minimum value is 300 seconds, and the maximum value is
  86,400 seconds. The default value is 86,400.

###### Note

The value of `disconnectAfterInSeconds` (returned by
the Lambda function) is set when the connection establishes. This
value cannot be modified during subsequent policy refresh Lambda
invocations.

- `refreshAfterInSeconds`: An integer that specifies the
  interval between policy refreshes. When this interval passes, AWS IoT Core
  invokes the Lambda function to allow for policy refreshes. The minimum
  value is 300 seconds, and the maximum value is 86,400 seconds.
   The following JSON object contains an example of a response that your Lambda
  function can send.

`{
 "isAuthenticated":true, //A Boolean that determines whether client can connect.
 "principalId": "xxxxxxxx",  //A string that identifies the connection in logs.
 "disconnectAfterInSeconds": 86400, 
 "refreshAfterInSeconds": 300, 
  "policyDocuments": [
       {
         "Version": "2012-10-17", 
         "Statement": [
            {
               "Action": "iot:Publish",
               "Effect": "Allow",
               "Resource": "arn:aws:iot:us-east-1:<your_aws_account_id>:topic/customauthtesting"
             }
          ]
        }
     ]
 }`

The `policyDocument` value must contain a valid AWS IoT Core policy
document. For more information about AWS IoT Core policies, see [AWS IoT Core policies](iot-policies.md "iot-policies.md").  In MQTT over TLS and MQTT over WebSockets
connections, AWS IoT Core caches this policy for the interval specified in the
value of the `refreshAfterInSeconds` field. In the case of HTTP
connections the Lambda function is called for every authorization request unless
your device is using HTTP persistent connections (also called HTTP keep-alive or
HTTP connection reuse) you can choose to enable caching when configuring the
authorizer. During this interval, AWS IoT Core authorizes actions in an established
connection against this cached policy without triggering your Lambda function
again. If failures occur during custom authentication, AWS IoT Core terminates the
connection. AWS IoT Core also terminates the connection if it has been open for
longer than the value specified in the
`disconnectAfterInSeconds`parameter.

The following JavaScript contains a sample Node.js Lambda function that looks
for a password in the MQTT Connect message with a value of `test` and
returns a policy that grants permission to connect to AWS IoT Core with a client
named `myClientName` and publish to a topic that contains the same
client name. If it doesn't find the expected password, it returns a policy that
denies those two actions.

```
// A simple Lambda function for an authorizer. It demonstrates
// how to parse an MQTT password and generate a response.

exports.handler = function(event, context, callback) {
    var uname = event.protocolData.mqtt.username;
    var pwd = event.protocolData.mqtt.password;
    var buff = new Buffer(pwd, 'base64');
    var passwd = buff.toString('ascii');
    switch (passwd) {
        case 'test':
            callback(null, generateAuthResponse(passwd, 'Allow'));
            break;
        default:
            callback(null, generateAuthResponse(passwd, 'Deny'));  
    }
};

// Helper function to generate the authorization response.
var generateAuthResponse = function(token, effect) {
    var authResponse = {};
    authResponse.isAuthenticated = true;
    authResponse.principalId = 'TEST123';

    var policyDocument = {};
    policyDocument.Version = '2012-10-17		 	 	 ';
    policyDocument.Statement = [];
    var publishStatement = {};
    var connectStatement = {};
    connectStatement.Action = ["iot:Connect"];
    connectStatement.Effect = effect;
    connectStatement.Resource = ["arn:aws:iot:us-east-1:123456789012:client/myClientName"];
    publishStatement.Action = ["iot:Publish"];
    publishStatement.Effect = effect;
    publishStatement.Resource = ["arn:aws:iot:us-east-1:123456789012:topic/telemetry/myClientName"];
    policyDocument.Statement[0] = connectStatement;
    policyDocument.Statement[1] = publishStatement;
    authResponse.policyDocuments = [policyDocument];
    authResponse.disconnectAfterInSeconds = 3600;
    authResponse.refreshAfterInSeconds = 300;

    return authResponse;
}
```

The preceding Lambda function returns the following JSON when it receives the
expected password of `test` in the MQTT Connect message. The values
of the `password` and `principalId` properties will be the
values from the MQTT Connect message.

```
{
  "password": "`password`",
  "isAuthenticated": true,
  "principalId": "`principalId`",
  "policyDocuments": [
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Action": "iot:Connect",
          "Effect": "Allow",
          "Resource": "*"
        },
        {
          "Action": "iot:Publish",
          "Effect": "Allow",
          "Resource": "arn:aws:iot:`region`:`accountId`:topic/telemetry/${iot:ClientId}"
        },
        {
          "Action": "iot:Subscribe",
          "Effect": "Allow",
          "Resource": "arn:aws:iot:`region`:`accountId`:topicfilter/telemetry/${iot:ClientId}"
        },
        {
          "Action": "iot:Receive",
          "Effect": "Allow",
          "Resource": "arn:aws:iot:`region`:`accountId`:topic/telemetry/${iot:ClientId}"
        }
      ]
    }
  ],
  "disconnectAfterInSeconds": 3600,
  "refreshAfterInSeconds": 300
}
```
