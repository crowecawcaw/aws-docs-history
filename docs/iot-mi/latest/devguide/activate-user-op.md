# Implement the AWS.ActivateUser operation

The `AWS.ActivateUser` operation is required for managed integrations for AWS IoT Device Management to retrieve
a user identifier from an end user's OAuth2.0 token. Managed integrations for AWS IoT Device Management will pass the OAuth
token within the request header, and expects your connector to include the globally unique
user identifier in the response payload. This operation occurs after a successful account
linking flow.

The following list outlines the requirements for your connector to facilitate a
successful `AWS.Activate` user flow.

- Your C2C connector Lambda can process an `AWS.ActivateUser` operation
  request message from managed integrations for AWS IoT Device Management.
- Your C2C connector Lambda can determine a unique user identifier from a provided
  OAuth2.0 token. Normally, it can be extracted either from the token itself, if it's a
  JWT token, or requested from the Authorization server by the token.

###### `AWS.ActivateUser` workflow

1. Managed integrations for AWS IoT Device Management invokes your C2C connector Lambda with the following
   payload:

```
{
   "header": {
        "auth": {
            "token": "ashriu32yr97feqy7afsaf",
            "type": "OAuth2.0"
        }
   },
   "payload": {
        "operationName": "AWS.ActivateUser",
        "operationVersion": "1.0.0",
        "connectorId": "`Your-Connector-ID`",
}
}

```

2. The C2C connector determines the user ID, either from the token or by querying
   your third-party resource server, to include in the `AWS.ActivateUser`
   response.
3. The C2C connector responds to `AWS.ActivateUser` operation Lambda
   invocation, including the default payload as well as the corresponding user identifier
   within the `userId` field.

```
{
     "header": {
          "responseCode":200
     },
     "payload": {
          "responseMessage": "Successfully activated user with connector-id ``Your-Connector-Id`.”,
          "userId": "123456"
     }
}

```
