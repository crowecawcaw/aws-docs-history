

# Logging IAM Identity Center SCIM API calls with AWS CloudTrail
<a name="scim-logging-using-cloudtrail"></a>

[IAM Identity Center SCIM](other-idps.md) is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures API calls for SCIM as events. Using the information collected by CloudTrail, you can determine the information about the requested action, the date and time of the action, request parameters, and so on. To learn more about CloudTrail, see [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

**Note**  
CloudTrail is enabled on your AWS account when you create the account. However, you might need to rotate your access token to see events from SCIM, if your token was created prior to September 2024.  
For more information, see [Rotate an access token](rotate-token.md).

SCIM supports logging for the following operations as events in CloudTrail:
+ [CreateGroup](https://docs.aws.amazon.com/singlesignon/latest/developerguide/creategroup.html)
+ [CreateUser](https://docs.aws.amazon.com/singlesignon/latest/developerguide/createuser.html)
+ [DeleteGroup](https://docs.aws.amazon.com/singlesignon/latest/developerguide/deletegroup.html)
+ [DeleteUser](https://docs.aws.amazon.com/singlesignon/latest/developerguide/deleteuser.html)
+ [GetGroup](https://docs.aws.amazon.com/singlesignon/latest/developerguide/getgroup.html)
+ [GetSchema](https://docs.aws.amazon.com/singlesignon/latest/developerguide/getschema.html)
+ [GetUser](https://docs.aws.amazon.com/singlesignon/latest/developerguide/getuser.html)
+ [ListGroups](https://docs.aws.amazon.com/singlesignon/latest/developerguide/listgroups.html)
+ [ListResourceTypes](https://docs.aws.amazon.com/singlesignon/latest/developerguide/listresourcetypes.html)
+ [ListSchemas](https://docs.aws.amazon.com/singlesignon/latest/developerguide/listschemas.html)
+ [ListUsers](https://docs.aws.amazon.com/singlesignon/latest/developerguide/listusers.html)
+ [PatchGroup](https://docs.aws.amazon.com/singlesignon/latest/developerguide/patchgroup.html)
+ [PatchUser](https://docs.aws.amazon.com/singlesignon/latest/developerguide/patchuser.html)
+ [PutUser](https://docs.aws.amazon.com/singlesignon/latest/developerguide/putuser.html)
+ [ServiceProviderConfig](https://docs.aws.amazon.com/singlesignon/latest/developerguide/serviceproviderconfig.html)

## Example CloudTrail events
<a name="scim-logging-using-cloudtrail-examples"></a>

The following examples demonstrate typical CloudTrail event logs generated during SCIM operations with IAM Identity Center. These examples show the structure and content of events for successful operations and common error scenarios, helping you understand how to interpret CloudTrail logs when troubleshooting SCIM provisioning issues.

### Successful `CreateUser` operation
<a name="scim-successful-createuser-example"></a>

This CloudTrail event shows a successful `CreateUser` operation performed through the SCIM API. The event captures both the request parameters (with sensitive information masked) and the response elements, including the newly-created user's ID. This type of event is generated when an identity provider successfully provisions a new user to IAM Identity Center using the SCIM protocol.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "WebIdentityUser",
    "accountId": "123456789012",
    "accessKeyId": "xxxx"
  },
  "eventTime": "xxxx",
  "eventSource": "identitystore-scim.amazonaws.com",
  "eventName": "CreateUser",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "xx.xxx.xxx.xxx",
  "userAgent": "Go-http-client/2.0",
  "requestParameters": {
    "httpBody": {
      "displayName": "HIDDEN_DUE_TO_SECURITY_REASONS",
      "schemas" : [
        "urn:ietf:params:scim:schemas:core:2.0:User"
      ],
      "name": {
        "familyName": "HIDDEN_DUE_TO_SECURITY_REASONS",
        "givenName": "HIDDEN_DUE_TO_SECURITY_REASONS"
      },
      "active": true,
      "userName": "HIDDEN_DUE_TO_SECURITY_REASONS"
    },
    "tenantId": "xxxx"
  },
  "responseElements": {
    "meta" : {
      "created" : "Oct 10, 2024, 1:23:45 PM",
      "lastModified" : "Oct 10, 2024, 1:23:45 PM",
      "resourceType" : "User"
    },
    "displayName" : "HIDDEN_DUE_TO_SECURITY_REASONS",
    "schemas" : [
      "urn:ietf:params:scim:schemas:core:2.0:User"
    ],
    "name": {
      "familyName": "HIDDEN_DUE_TO_SECURITY_REASONS",
      "givenName": "HIDDEN_DUE_TO_SECURITY_REASONS"
    },
    "active": true,  
    "id" : "c4488478-a0e1-700e-3d75-96c6bb641596",
    "userName": "HIDDEN_DUE_TO_SECURITY_REASONS"
  },
  "requestID": "xxxx",
  "eventID": "xxxx",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "clientProvidedHostHeader": "scim.us-east-1.amazonaws.com"
  }
}
```

### Failed `PatchGroup` operation: Missing required path attribute
<a name="scim-failed-patchgroup-example"></a>

This CloudTrail event shows a failed `PatchGroup` operation that resulted in a `ValidationException` with the error message `"Missing path in PATCH request"`. The error occurred because the `PATCH` operation requires a path attribute to specify which group attribute to modify, but this attribute was missing from the request.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "Unknown",
    "accountId": "123456789012",
    "accessKeyId": "xxxx"
  },
  "eventTime": "xxxx",
  "eventSource": "identitystore-scim.amazonaws.com",
  "eventName": "PatchGroup",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "xxx.xxx.xxx.xxx",
  "userAgent": "Go-http-client/2.0",
  "errorCode": "ValidationException",
  "errorMessage": "Missing path in PATCH request",
  "requestParameters": {
    "httpBody": {
      "operations": [
        {
          "op": "REMOVE",
          "value": "HIDDEN_DUE_TO_SECURITY_REASONS"
        }
      ],
      "schemas": [
        "HIDDEN_DUE_TO_SECURITY_REASONS"
      ]
    },
    "tenantId": "xxxx",
    "id": "xxxx"
  },
  "responseElements": null,
  "requestID": "xxxx",
  "eventID": "xxxx",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "clientProvidedHostHeader": "scim.us-east-1.amazonaws.com"
  }
}
```

### Failed `CreateGroup` operation: Group name already exists
<a name="scim-failed-creategroup-example"></a>

This CloudTrail event shows a failed `CreateGroup` operation that resulted in a `ConflictException` with the error message `"Duplicate GroupDisplayName"`. This error occurs when attempting to create a group with a display name that already exists in IAM Identity Center. The identity provider must use a unique group name or update the existing group instead of creating a new one.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "Unknown",
    "accountId": "123456789012",
    "accessKeyId": "xxxx"
  },
  "eventTime": "xxxx",
  "eventSource": "identitystore-scim.amazonaws.com",
  "eventName": "CreateGroup",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "xxx.xxx.xxx.xxx",
  "userAgent": "Go-http-client/2.0",
  "errorCode": "ConflictException",
  "errorMessage": "Duplicate GroupDisplayName",
  "requestParameters": {
    "httpBody": {
      "displayName": "HIDDEN_DUE_TO_SECURITY_REASONS"
    },
    "tenantId": "xxxx"
  },
  "responseElements": null,
  "requestID": "xxxx",
  "eventID": "xxxx",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "clientProvidedHostHeader": "scim.us-east-1.amazonaws.com"
  }
}
```

### Failed `PatchUser` operation: Multiple email addresses not supported
<a name="scim-failed-patchuser-example"></a>

This CloudTrail event shows a failed `PatchUser` operation that resulted in a `ValidationException` with the error message `"List attribute emails exceeds allowed limit of 1"`. This error occurs when attempting to assign multiple email addresses to a user, as IAM Identity Center supports only one email address per user. The identity provider must configure SCIM mapping to send only a single email address for each user.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "Unknown",
    "accountId": "123456789012",
    "accessKeyId": "xxxx"
  },
  "eventTime": "xxxx",
  "eventSource": "identitystore-scim.amazonaws.com",
  "eventName": "PatchUser",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "xxx.xxx.xxx.xxx",
  "userAgent": "Go-http-client/2.0",
  "errorCode": "ValidationException",
  "errorMessage": "List attribute emails exceeds allowed limit of 1",
  "requestParameters": {
    "httpBody": {
      "operations": [
        {
          "op": "REPLACE",
          "path": "emails",
          "value": "HIDDEN_DUE_TO_SECURITY_REASONS"
        }
      ],
      "schemas": [
        "HIDDEN_DUE_TO_SECURITY_REASONS"
      ]
    },
    "tenantId": "xxxx",
    "id": "xxxx"
  },
  "responseElements": null,
  "requestID": "xxxx",
  "eventID": "xxxx",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "clientProvidedHostHeader": "scim.us-east-1.amazonaws.com"
  }
}
```

## Common SCIM API validation errors in IAM Identity Center
<a name="scim-cloudtrail-common-errors"></a>

The following validation error messages commonly appear in CloudTrail events when using the SCIM API with IAM Identity Center. These validation errors typically occur during user and group provisioning operations.

For detailed guidance on resolving these errors and properly configuring SCIM provisioning, see this [AWS re:Post article](https://repost.aws//knowledge-center/iam-identity-center-provision).
+ List attribute email exceeds allowed limit of 1
+ List attribute addresses allowed limit of 1
+ 1 validation errors detected: Value at '\*name.familyName\*' failed to satisfy constraint: Member must satisfy regular expression pattern: [\\\\p{L}\\\\p{M}\\\\p{S}\\\\p{N}\\\\p{P}\\\\t\\\\n\\\\r ]\+
+ 2 validation errors detected: Value at 'name.familyName' failed to satisfy constraint: Member must have length greater than or equal to 1; Value at 'name.familyName' failed to satisfy constraint: Member must satisfy regular expression pattern: [\\\\p{L}\\\\p{M}\\\\p{S}\\\\p{N}\\\\p{P}\\\\t\\\\n\\\\r ]\+
+ 2 validation errors detected: Value at 'urn:ietf:params:scim:schemas:extension:enterprise:2.0:User.manager.value' failed to satisfy constraint: Member must have length greater than or equal to 1; Value at 'urn:ietf:params:scim:schemas:extension:enterprise:2.0:User.manager.value' failed to satisfy constraint: Member must satisfy regular expression pattern: [\\\\p{L}\\\\p{M}\\\\p{S}\\\\p{N}\\\\p{P}\\\\t\\\\n\\\\r ]\+",
+ Invalid JSON from RequestBody
+ Invalid Filter format