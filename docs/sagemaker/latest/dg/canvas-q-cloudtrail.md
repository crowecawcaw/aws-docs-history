# Logging Q Developer conversations with AWS CloudTrail

AWS CloudTrail is a service that records actions taken by users, roles, or AWS services in
Amazon SageMaker AI. CloudTrail captures API calls resulting from your interactions with Amazon Q Developer (a
conversational AI assistant) while using SageMaker Canvas (a no-code ML interface). CloudTrail data shows
request details, the IP address of the requester, who made the request, and when.

Your interactions with Q Developer are sent as `SendConversation` API
calls to the SageMaker AI Data Science Assistant service, which is an internal service that
Canvas leverages on the backend. The event source for `SendConversation`
API calls is `sagemaker-data-science-assistant.amazonaws.com`.

###### Note

For privacy and security reasons, the content of your conversations is hidden in
the logs, appearing as `HIDDEN_DUE_TO_SECURITY_REASONS` in the request
and response elements.

To learn more about CloudTrail, see the [_AWS CloudTrail User Guide_](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md"). To learn more about CloudTrail
in SageMaker AI, see [Logging Amazon SageMaker AI API calls using
AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

The following is an example log file entry for the `SendConversation`
API:

```
{
    "eventVersion":"1.10",
    "userIdentity": {
        "type":"AssumedRole",
        "principalId":"AROA123456789EXAMPLE:user-Isengard",
        "arn":"arn:aws:sts::111122223333:assumed-role/Admin/user",
        "accountId":"111122223333",
        "accessKeyId":"ASIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type":"Role",
                "principalId":"AROA123456789EXAMPLE",
                "arn":"arn:aws:iam::111122223333:role/Admin",
                "accountId":"111122223333",
                "userName":"Admin"
            },
            "attributes": {
                "creationDate":"2024-11-11T22:04:37Z",
                "mfaAuthenticated":"false"
            }
        }
    },
    "eventTime":"2024-11-11T22:09:22Z",
    "eventSource":"sagemaker-data-science-assistant.amazonaws.com",
    "eventName":"SendConversation",
    "awsRegion":"us-west-2",
    "sourceIPAddress":"192.0.2.0",
    "userAgent":"Boto3/1.33.13 md/Botocore#1.33.13 ua/2.0 os/linux#5.10.227-198.884.amzn2int.x86_64 md/arch#x86_64 lang/python#3.7.16 md/pyimpl#CPython cfg/retry-mode#legacy Botocore/1.33.13",
    "requestParameters": {
        "conversation": [
            {
                "utteranceId":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
                "utterance":"HIDDEN_DUE_TO_SECURITY_REASONS",
                "timestamp":"Feb 4, 2020, 7:46:29 AM",
                "utteranceType":"User"
            }
        ],
        "utteranceId":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    },
    "responseElements": {
        "responseCode":"CHAT_RESPONSE",
        "conversationId":"1234567890abcdef0",
        "response": {
            "chat": {
                "body":"HIDDEN_DUE_TO_SECURITY_REASONS"
            }
        }
    },
    "requestID":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "eventID":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "readOnly":false,
    "eventType":"AwsApiCall",
    "managementEvent":true,
    "recipientAccountId":"123456789012",
    "eventCategory":"Management",
    "tlsDetails": {
        "tlsVersion":"TLSv1.2",
        "cipherSuite":"ECDHE-RSA-AES128-GCM-SHA256",
        "clientProvidedHostHeader":"gamma.us-west-2.data-science-assistant.sagemaker.aws.dev"
    }
}
```
