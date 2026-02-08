# Implement the AWS.ActivateUser operation

The `AWS.ActivateUser` operation is required for Managed integrations for AWS IoT Device Management to retrieve
a user identifier from an end user. For OAuth 2.0, Managed integrations for AWS IoT Device Management will pass the OAuth
token within the request header. For General Authorization, Managed integrations for AWS IoT Device Management will pass the
AWS Secrets Manager reference. Your connector must include the globally unique
user identifier in the response payload.

###### Requirements

The following list outlines the requirements for your connector to facilitate a
successful `AWS.ActivateUser` flow:

- Your C2C connector Lambda can process an `AWS.ActivateUser` operation
  request message from Managed integrations for AWS IoT Device Management.
- Your C2C connector Lambda can determine a unique user identifier. For OAuth 2.0,
  this can be extracted from the token itself if it's a JWT token, or requested from the
  authorization server. For General Authorization, this may be retrieved from your
  third-party platform or derived from the authorization context.

###### `AWS.ActivateUser` Workflow

**Step 1: Managed Integrations Invokes Your Lambda**

Managed integrations for AWS IoT Device Management invokes your C2C connector Lambda with one of the following
payloads, depending on the authorization type:

**OAuth 2.0 Request:**

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
        "connectorId": "`Your-Connector-ID`"
   }
}

```

**General Authorization request:**

```
{
   "header": {
        "auth": {
            "secretsManager": {
                "arn": "string",
                "versionId": "string"
            },
            "type": "GeneralAuthorization"
        }
   },
   "payload": {
        "operationName": "AWS.ActivateUser",
        "operationVersion": "1.0.0",
        "connectorId": "`Your-Connector-ID`"
   }
}

```

**Step 2: Determine User ID**

The C2C connector determines the user ID to include in the `AWS.ActivateUser`
response.

- **For OAuth 2.0:** This is retrieved from the token or by querying your authorization server.
- **For General Authorization:** This may be retrieved from your third-party platform
  or derived from the authorization context.
  **Step 3: Respond with User Identifier**

The C2C connector responds to `AWS.ActivateUser` operation Lambda
invocation, including the default payload as well as the corresponding user identifier
within the `userId` field.

**Response Format:**

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
