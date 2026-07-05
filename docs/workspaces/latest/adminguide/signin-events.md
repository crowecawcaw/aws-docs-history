# Understanding AWS sign-in events for WorkSpaces Personal users

AWS CloudTrail logs successful and unsuccessful sign-in events for WorkSpaces Personal users. These events are generated for all authentication methods supported by the WorkSpaces Personal user login flow, including password-based authentication and smart cards. Each event captures when a user is prompted to solve a specific credential challenge or factor, as well as the status of that particular credential verification request. A user is signed in only after completing all required credential challenges, which results in a `UserAuthentication` event being logged.

###### Note

Prior to the rollout of the new user login flow in late 2025 / early 2026, these CloudTrail events were only generated for smart card users. With the introduction of the new user login flow, these events are now recorded for all supported authentication types. The `CredentialType` field in each event identifies the authentication method used (for example, `PASSWORD` or `SMARTCARD`).

These CloudTrail events are specific to the WorkSpaces Personal directory-based sign-in flow. Other authentication methods, such as SAML federation and TOTP-based MFA, are handled by IAM Sign-In and do not generate these WorkSpaces-specific events. For information about CloudTrail events from IAM Sign-In, see [Logging IAM and AWS STS API calls with AWS CloudTrail](../../../IAM/latest/UserGuide/cloudtrail-integration.md "../../../IAM/latest/UserGuide/cloudtrail-integration.md") in the _IAM User Guide_.

The following table captures each of the sign-in CloudTrail event names and their
purposes.

| Event name               | Event purpose                                                                                                                                                                                                                                                                                    |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `CredentialChallenge`    | Notifies that AWS sign-in has requested that the user solve a<br>specific credential challenge and specifies the<br>`CredentialType` that is required (for example,<br>`PASSWORD` or `SMARTCARD`).                                                                                               |
| `CredentialVerification` | Notifies that the user has attempted to solve a specific<br>`CredentialChallenge` request, and specifies whether<br>that credential has succeeded or failed.                                                                                                                                     |
| `UserAuthentication`     | Notifies that all authentication requirements that the user was<br>challenged with have been successfully completed and that the user<br>was successfully signed in. When users fail to successfully complete<br>the required credential challenges, no<br>`UserAuthentication` event is logged. |

The following table captures additional useful event data fields contained within
specific sign-in CloudTrail events.

| Event name       | Event purpose                                                                                                                                                                                                                                                                                    | Sign-in event applicability                                                 | Example values                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `AuthWorkflowID` | Correlates all events emitted across an entire sign-in sequence.<br>For each user sign-in, multiple events can be emitted by AWS<br>sign-in.                                                                                                                                                     | `CredentialChallenge`,<br>`CredentialVerification`,<br>`UserAuthentication` | "AuthWorkflowID": "9de74b32-8362-4a01-a524-de21df59fd83"                                             |
| `CredentialType` | Specifies the type of credential used for the authentication attempt.                                                                                                                                                                                                                            | `CredentialChallenge`,<br>`CredentialVerification`,<br>`UserAuthentication` | "CredentialType": "PASSWORD" or "CredentialType": "SMARTCARD" (possible values: PASSWORD, SMARTCARD) |
| `LoginTo`        | Notifies that all authentication requirements that the user was<br>challenged with have been successfully completed and that the user<br>was successfully signed in. When users fail to successfully complete<br>the required credential challenges, no<br>`UserAuthentication` event is logged. | `UserAuthentication`                                                        | "LoginTo": "https://clients.amazonaws.com/workspaces“                                                |

## Example events for AWS sign-in scenarios

The following examples show the expected sequence of CloudTrail events for different
sign-in scenarios.

###### Contents

- [Successful sign-in when authenticating with password](#successful-password-signin "#successful-password-signin")
- [Successful sign-in when authenticating with smart card](#successful-signin "#successful-signin")
- [Failed sign-in when authenticating with only a smart card](#failed-signin "#failed-signin")

### Successful sign-in when authenticating with password

The following sequence of events captures an example of a successful
password-based sign-in through the WorkSpaces Personal user login flow.

**CredentialChallenge**

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "Unknown",
        "principalId": "123456789012",
        "arn": "",
        "accountId": "123456789012",
        "accessKeyId": "",
        "userName": "exampleuser"
    },
    "eventTime": "2026-04-14T23:56:26Z",
    "eventSource": "signin.amazonaws.com",
    "eventName": "CredentialChallenge",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "198.51.100.1",
    "userAgent": "Mozilla/5.0 ...",
    "requestParameters": null,
    "responseElements": null,
    "additionalEventData": {
        "AuthWorkflowID": "9de74b32-8362-4a01-a524-de21df59fd83",
        "CredentialType": "PASSWORD"
    },
    "requestID": "2da067db-b2ad-42de-bfb3-16ac48d08435",
    "eventID": "01dc9ac8-2e6b-4ef7-9390-a76b3935620e",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "123456789012",
    "serviceEventDetails": {
        "CredentialChallenge": "Success"
    }
}

```

**Successful CredentialVerification**

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "Unknown",
        "principalId": "123456789012",
        "arn": "",
        "accountId": "123456789012",
        "accessKeyId": "",
        "userName": "exampleuser"
    },
    "eventTime": "2026-04-14T23:56:29Z",
    "eventSource": "signin.amazonaws.com",
    "eventName": "CredentialVerification",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "198.51.100.1",
    "userAgent": "Mozilla/5.0 ...",
    "requestParameters": null,
    "responseElements": null,
    "additionalEventData": {
        "AuthWorkflowID": "9de74b32-8362-4a01-a524-de21df59fd83",
        "CredentialType": "PASSWORD"
    },
    "requestID": "3b178a74-4c5c-4fa8-8730-c2995e751f78",
    "eventID": "2127ca9e-40d2-49bb-b6c4-fe07be79b2a5",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "123456789012",
    "serviceEventDetails": {
        "CredentialVerification": "Success"
    }
}

```

**Successful UserAuthentication**

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "Unknown",
        "principalId": "123456789012",
        "arn": "",
        "accountId": "123456789012",
        "accessKeyId": "",
        "userName": "exampleuser"
    },
    "eventTime": "2026-04-14T23:56:29Z",
    "eventSource": "signin.amazonaws.com",
    "eventName": "UserAuthentication",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "198.51.100.1",
    "userAgent": "Mozilla/5.0 ...",
    "requestParameters": null,
    "responseElements": null,
    "additionalEventData": {
        "AuthWorkflowID": "9de74b32-8362-4a01-a524-de21df59fd83",
        "LoginTo": "https://clients.amazonaws.com/workspaces",
        "CredentialType": "PASSWORD"
    },
    "requestID": "3b178a74-4c5c-4fa8-8730-c2995e751f78",
    "eventID": "25616659-7efb-46dd-804e-305bed7db3ac",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "123456789012",
    "serviceEventDetails": {
        "UserAuthentication": "Success"
    }
}

```

### Successful sign-in when authenticating with smart card

The following sequence of events captures an example of a successful smart
card sign-in.

**CredentialChallenge**

```

{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "principalId": "509318101470",
        "arn": "",
        "accountId": "509318101470",
        "accessKeyId": ""
    },
    "eventTime": "2021-07-30T17:23:29Z",
    "eventSource": "signin.amazonaws.com",
    "eventName": "CredentialChallenge",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
    "requestParameters": null,
    "responseElements": null,
    "additionalEventData": {
        "AuthWorkflowID": "6602f256-3b76-4977-96dc-306a7283269e",
        "CredentialType": "SMARTCARD"
    },
    "requestID": "65551a6d-654a-4be8-90b5-bbfef7187d3a",
    "eventID": "fb603838-f119-4304-9fdc-c0f947a82116",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "509318101470",
    "serviceEventDetails": {
        CredentialChallenge": "Success"
    }
}

```

**Successful CredentialVerification**

```

{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "principalId": "509318101470",
        "arn": "",
        "accountId": "509318101470",
        "accessKeyId": ""
    },
    "eventTime": "2021-07-30T17:23:39Z",
    "eventSource": "signin.amazonaws.com",
    "eventName": "CredentialVerification",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
    "requestParameters": null,
    "responseElements": null,
    "additionalEventData": {
        "AuthWorkflowID": "6602f256-3b76-4977-96dc-306a7283269e",
        "CredentialType": "SMARTCARD"
    },
    "requestID": "81869203-1404-4bf2-a1a4-3d30aa08d8d5",
    "eventID": "84c0a2ff-413f-4d0f-9108-f72c90a41b6c",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "509318101470",
    "serviceEventDetails": {
        CredentialVerification": "Success"
    }
}

```

**Successful UserAuthentication**

```

{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "principalId": "509318101470",
        "arn": "",
        "accountId": "509318101470",
        "accessKeyId": ""
    },
    "eventTime": "2021-07-30T17:23:39Z",
    "eventSource": "signin.amazonaws.com",
    "eventName": "UserAuthentication",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
    "requestParameters": null,
    "responseElements": null,
    "additionalEventData": {
        "AuthWorkflowID": "6602f256-3b76-4977-96dc-306a7283269e",
        "LoginTo": "https://clients.amazonaws.com/workspaces",
        "CredentialType": "SMARTCARD"
    },
    "requestID": "81869203-1404-4bf2-a1a4-3d30aa08d8d5",
    "eventID": "acc0dba8-8e8b-414b-a52d-6b7cd51d38f6",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "509318101470",
    "serviceEventDetails": {
        UserAuthentication": "Success"
    }
}

```

### Failed sign-in when authenticating with only a smart card

The following sequence of events captures an example of failed smart card
sign-in.

**CredentialChallenge**

```

{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "principalId": "509318101470",
        "arn": "",
        "accountId": "509318101470",
        "accessKeyId": ""
    },
    "eventTime": "2021-07-30T17:23:06Z",
    "eventSource": "signin.amazonaws.com",
    "eventName": "CredentialChallenge",
    "awaRegion": "us-east-1",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
    "requestParameters": null,
    "responseElements": null,
    "additionalEventData": {
        "AuthWorkflowID": "73dfd26b-f812-4bd2-82e9-0b2abb358cdb",
        "CredentialType": "SMARTCARD"
    },
    "requestID": "73eb499d-91a8-4c18-9c5d-281fd45ab50a",
    "eventID": "f30a50ec-71cf-415a-a5ab-e287edc800da",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "509318101470",
    "serviceEventDetails": {
        CredentialChallenge": "Success"
    }
}

```

**Failed CredentialVerification**

```

{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "principalId": "509318101470",
        "arn": "",
        "accountId": "509318101470",
        "accessKeyId": ""
    },
    "eventTime": "2021-07-30T17:23:13Z",
    "eventSource": "signin.amazonaws.com",
    "eventName": "CredentialVerification",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
    "requestParameters": null,
    "responseElements": null,
    "additionalEventData": {
        "AuthWorkflowID": "73dfd26b-f812-4bd2-82e9-0b2abb358cdb",
        "CredentialType": "SMARTCARD"
    },
    "requestID": "051ca316-0b0d-4d38-940b-5fe5794fda03",
    "eventID": "4e6fbfc7-0479-48da-b7dc-e875155a8177",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "509318101470",
    "serviceEventDetails": {
        CredentialVerification": "Failure"
    }
}

```
