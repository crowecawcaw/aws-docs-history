# Logging AWS Compute Optimizer Automation API calls using

AWS CloudTrail

AWS Compute Optimizer Automation is integrated with [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md"), a service that provides a record of actions taken by a user, role, or an
AWS service. CloudTrail captures all
API calls for Compute Optimizer Automation as events. The calls captured include calls from the Compute Optimizer Automation console
and code calls to the Compute Optimizer Automation API operations. Using the information collected by CloudTrail, you can
determine the request that was made to Compute Optimizer Automation, the IP address from which the request was
made, when it was made, and additional details.

Every event or log entry contains information about who generated the request. The identity
information helps you determine the following:

- Whether the request was made with root user or user credentials.
- Whether the request was made on behalf of an IAM Identity Center user.
- Whether the request was made with temporary security credentials for a role or federated
  user.
- Whether the request was made by another AWS service.
  CloudTrail is active in your AWS account when you create the account and you automatically have
  access to the CloudTrail **Event history**. The CloudTrail **Event
  history** provides a viewable, searchable, downloadable, and immutable record of the
  past 90 days of recorded management events in an AWS Region. For more information, see [Working
  with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the _AWS CloudTrail User Guide_. There are no CloudTrail
  charges for viewing the **Event history**.

For an ongoing record of events in your AWS account past 90 days, create a trail or a
[CloudTrail
Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") event data store.

**CloudTrail trails**

A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket. All trails created using the AWS Management Console are multi-Region. You can create a single-Region or a multi-Region trail by using the AWS CLI. Creating a multi-Region trail is recommended because you capture activity in all AWS Regions in your account. If you create a single-Region trail, you can view only the events logged in the trail's AWS Region. For more information about trails, see [Creating a trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md") and [Creating a trail for an organization](../../../awscloudtrail/latest/userguide/creating-trail-organization.md "../../../awscloudtrail/latest/userguide/creating-trail-organization.md") in the _AWS CloudTrail User Guide_.

You can deliver one copy of your ongoing management events to your Amazon S3 bucket at no charge from CloudTrail by creating a trail, however, there are Amazon S3 storage charges. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/"). For information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

**CloudTrail Lake event data stores**

_CloudTrail Lake_ lets you run SQL-based queries on your events. CloudTrail Lake converts existing events in row-based JSON format to [Apache ORC](https://orc.apache.org/ "https://orc.apache.org/") format. ORC is a columnar storage format that is optimized for fast retrieval of data. Events are aggregated into _event data stores_, which are immutable collections of events based on criteria that you select by applying [advanced event selectors](../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors "../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors"). The selectors that you apply to an event data store control which events persist and are available for you to query. For more information about CloudTrail Lake, see [Working with AWS CloudTrail Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") in the _AWS CloudTrail User Guide_.

CloudTrail Lake event data stores and queries incur costs. When you create an event data store, you choose the [pricing option](../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option") you want to use for the event data store. The pricing option determines the cost for ingesting and storing events, and the default and maximum retention period for the event data store. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

## Compute Optimizer Automation management events in CloudTrail

[Management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events") provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

AWS Compute Optimizer Automation logs all Compute Optimizer Automation control plane operations as management events. For a list
of the AWS Compute Optimizer Automation control plane operations that Compute Optimizer Automation logs to CloudTrail, see the
[AWS Compute Optimizer Automation API Reference](../../../Provide API url.md "../../../Provide API url.md").

## Compute Optimizer Automation event examples

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

The following example shows a CloudTrail event that demonstrates the `ThrottlingException` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-06T20:23:42Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-06T19:50:12Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "GetEnrollmentConfiguration",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "2f3a4012-f005-4d83-9042-1639a80c54ce",
    "eventID": "29ea5225-2dd6-486f-9bfe-caf7a81c3bab",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "errorCode": "ThrottlingException",
    "requestParameters": null,
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}

```

The following example shows a CloudTrail event that demonstrates the `AccessDenied` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/ReadOnly/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/ReadOnly",
                "accountId": "111122223333",
                "userName": "ReadOnly"
            },
            "attributes": {
                "creationDate": "2025-11-06T19:48:45Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-06T19:50:12Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "GetEnrollmentConfiguration",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "3f4a5013-f106-4e84-9143-1740b91d55df",
    "eventID": "30fb6336-3ee7-597g-0cgf-dbg8b92d4cbc",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "errorCode": "AccessDenied",
    "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ReadOnly/john-doe is not authorized to perform: aco-automation:GetEnrollmentConfiguration because no identity-based policy allows the aco-automation:GetEnrollmentConfiguration action",
    "requestParameters": null,
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}

```

The following example shows a CloudTrail event that demonstrates the `NetworkEvent` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-07T04:23:51Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-05T20:23:48Z",
    "eventSource": "aco-automation.amazonaws.com",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "4g5b6024-g217-5f95-0254-2851c02e66eg",
    "eventID": "41gc7447-4ff8-608h-1dgh-ech9c03e5dcd",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "eventName": "GetEnrollmentConfiguration",
    "requestParameters": null,
    "responseElements": null,
    "sharedEventID": "c50cba87-2fb0-4458-b9fb-3c5e0f077718",
    "vpcEndpointId": "AWS Internal",
    "vpcEndpointAccountId": "AWS Internal",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }

}

```

The following example shows a CloudTrail event that demonstrates the `GetEnrollmentConfiguration` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
       "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/AuthenticatedComputeOptimizerRole/MettleCanary",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROASVBPKTAKQR6L32DI4",
                "arn": "arn:aws:iam::111122223333:role/AuthenticatedComputeOptimizerRole",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-05T20:23:45Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-05T20:23:48Z",
    "eventSource": "aco-automation.amazonaws.com",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "5h6c7135-h328-6ga6-1365-3962d13f77fh",
    "eventID": "52hd8558-5gg9-719i-2ehi-fdi0d14f6ede",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "eventName": "GetEnrollmentConfiguration",
    "requestParameters": null,
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}

```

The following example shows a CloudTrail event that demonstrates the `ListAccounts` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
       "type": "AssumedRole",
       "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/AuthenticatedComputeOptimizerRole/MettleCanary",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/AuthenticatedComputeOptimizerRole",
                "accountId": "111122223333",
                "userName": "AuthenticatedComputeOptimizerRole"
            },
            "attributes": {
                "creationDate": "2025-11-05T20:23:45Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-05T20:23:48Z",
    "eventSource": "aco-automation.amazonaws.com",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "6i7d8246-i439-7hb7-2476-4073e24g88gi",
    "eventID": "63ie9669-6hh0-820j-3fij-gej1e25g7fef",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "eventName": "ListAccounts",
    "requestParameters": {
        "maxResults": 50
    },
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}

```

The following example shows a CloudTrail event that demonstrates the `GetAutomationRule` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "abcdef01234567890;:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "abcdef01234567890;",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-06T04:19:48Z",
                "mfaAuthenticated": "false"
            }
        }
    },
"eventTime": "2025-11-06T04:24:01Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "GetAutomationRule",
    "awsRegion": "us-east-1",
        "eventTime": "2025-11-06T04:24:01Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "GetAutomationRule",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "7j8e9357-j540-8ic8-3587-5184f35h99hj",
    "eventID": "74jf0770-7ii1-931k-4gjk-hfk2f36h8gfg",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {
        "ruleArn": "arn:aws:compute-optimizer::123456789012:automation-rule/123AbcdEfGHi1jkL"
    },
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}

```

The following example shows a CloudTrail event that demonstrates the `ListAutomationRules` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "abcdef01234567890;:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-06T04:19:48Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-06T04:21:59Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "ListAutomationRules",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "8k9f0468-k651-9jd9-4698-6295g46i00ik",
    "eventID": "85kg1881-8jj2-042l-5hkl-igl3g47i9hgh",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": null,
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}

```

The following example shows a CloudTrail event that demonstrates the `ListTagsForResource` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "abcdef01234567890;:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-06T04:19:48Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-06T04:33:00Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "ListTagsForResource",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "9l0g1579-l762-0ke0-5709-7306h57j11jl",
    "eventID": "96lh2992-9kk3-153m-6ilm-jhm4h58j0ihi",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {
        "resourceArn": "arn:aws:compute-optimizer::111122223333:automation-rule/035Pcy46SStQHe0A"
    },
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}

```

The following example shows a CloudTrail event that demonstrates the `ListAutomationRulePreview` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "abcdef01234567890;:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-06T19:31:22Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-06T19:31:28Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "ListAutomationRulePreview",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "0m1h2680-m873-1lf1-6810-8417i68k22km",
    "eventID": "07mi3003-0ll4-264n-7jmn-kin5i69k1jij",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true, Note: Please be mindful when interacting with displayed links.
"recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {
        "ruleType": "OrganizationRule",
        "organizationScope": {
            "accountIds": [
                "535045952558"
            ]
        },
        "recommendedActionTypes": [
            "UpgradeEbsVolumeType",
            "SnapshotAndDeleteUnattachedEbsVolume"
        ],
        "criteria": {
            "region": [{
                "comparison": "StringEquals",
                "values": [
                    "us-east-1",
                    "us-west-2"
                ]
            }],
            "resourceArn": [{
                "comparison": "StringLike",
                "values": [
                    "vol-"
                ]
            }]
        },
        "maxResults": 100
    },
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}

```

The following example shows a CloudTrail event that demonstrates the `ListAutomationRulePreviewSummaries` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "abcdef01234567890;:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-06T19:14:49Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-06T19:21:52Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "ListAutomationRulePreviewSummaries",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "1n2i3791-n984-2mg2-7921-9528j79l33ln",
    "eventID": "18nj4114-1mm5-375o-8kon-ljo6j70l2kjk",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",

    "requestParameters": {
        "ruleType": "AccountRule",
        "recommendedActionTypes": [
            "SnapshotAndDeleteUnattachedEbsVolume"
        ]
    },
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}

```

The following example shows a CloudTrail event that demonstrates the `ListRecommendedActions` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "abcdef01234567890;:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-06T04:19:48Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-06T04:27:20Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "ListRecommendedActions",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "2o3j4802-o095-3nh3-8032-0639k80m44mo",
    "eventID": "29ok5225-2nn6-486p-9lop-mqp7k81m3lkl",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": null,
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}

```

The following example shows a CloudTrail event that demonstrates the `ListRecommendedActionSummaries` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "abcdef01234567890;:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-06T04:19:48Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-06T04:31:59Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "ListRecommendedActionSummaries",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "3p4k5913-p106-4oi4-9143-1740l91n55np",
    "eventID": "30pl6336-3oo7-597q-0dqp-nrq8l92n4mlm",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": null,
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}


```

The following example shows a CloudTrail event that demonstrates the `GetAutomationEvent` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "abcdef01234567890;:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-06T04:19:48Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-06T04:25:20Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "GetAutomationEvent",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "4q5l6024-q217-5pj5-0254-2851m02o66oq",
    "eventID": "41qm7447-4pp8-608r-1eqr-srr9m03o5nmn",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {
        "eventId": "a12cb3d4e5f67g0h"
    },
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}


```

The following example shows a CloudTrail event that demonstrates the `ListAutomationEvents` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "abcdef01234567890;:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-06T04:19:48Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-06T04:24:32Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "ListAutomationEvents",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "5r6m7135-r328-6qk6-1365-3962n13p77pr",
    "eventID": "52rn8558-5qq9-719s-2frs-tss0n14p6ono",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": null,
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}


```

The following example shows a CloudTrail event that demonstrates the `ListAutomationEventSteps` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "abcdef01234567890;:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-06T04:19:48Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-06T04:28:10Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "ListAutomationEventSteps",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "6s7n8246-s439-7rl7-2476-4073o24q88qs",
    "eventID": "63so9669-6rr0-820t-3gst-utt1o25q7pop",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {
        "eventId": "a12cb3d4e5f67g0h"
    },
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}

```

The following example shows a CloudTrail event that demonstrates the `ListAutomationEventSummaries` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "abcdef01234567890;:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-06T04:19:48Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-06T04:31:03Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "ListAutomationEventSummaries",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "7t8o9357-t540-8sm8-3587-5184p35r99rt",
    "eventID": "74tp0770-7ss1-931u-4htu-vuv2p36r8qpq",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": null,
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}

```

The following example shows a CloudTrail event that demonstrates the `UpdateEnrollmentConfiguration` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
       "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/AuthenticatedComputeOptimizerRole/MettleCanary",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/AuthenticatedComputeOptimizerRole",
                "accountId": "111122223333",
                "userName": "`USER NAME`"
            },
            "attributes": {
                "creationDate": "2025-11-05T20:23:45Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-05T20:23:46Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "UpdateEnrollmentConfiguration",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "8u9p0468-u651-9tn9-4698-6295q46s00su",
    "eventID": "85uq1881-8tt2-042v-5iuv-wvw3q47s9rqr",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {
        "status": "Active",
        "clientToken": "12345abc-12ab-1234-123a-EXAMPLEeb16b"
    },
    "responseElements": {
        "status": "Active",
        "lastUpdatedTimestamp": "Nov 5, 2025, 8:23:46 PM"
    },
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}

```

The following example shows a CloudTrail event that demonstrates the `AssociateAccounts` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
       "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/AuthenticatedComputeOptimizerRole/MettleCanary",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/AuthenticatedComputeOptimizerRole",
                "accountId": "111122223333",
                "userName": "AuthenticatedComputeOptimizerRole"
            },
            "attributes": {
                "creationDate": "2025-11-05T20:23:45Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-05T20:23:45Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "AssociateAccounts",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "9v0q1579-v762-0uo0-5709-7306r57t11tv",
    "eventID": "96vr2992-9uu3-153w-6jvw-xwx4r58t0srs",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "errorCode": "InvalidParameterValueException",
    "errorMessage": "The management account or the delegated administrator doesn't have access to this member account.",
    "requestParameters": {
        "accountIds": [
            "123456789012"
        ],
        "clientToken": "12345abc-12ab-1234-123a-EXAMPLEeb16b"
    },
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}

```

The following example shows a CloudTrail event that demonstrates the `DisassociateAccounts` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
       "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/AuthenticatedComputeOptimizerRole/MettleCanary",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/AuthenticatedComputeOptimizerRole",
                "accountId": "111122223333",
                "userName": "AuthenticatedComputeOptimizerRole"
            },
            "attributes": {
                "creationDate": "2025-11-05T20:23:45Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-05T20:23:47Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "DisassociateAccounts",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "0w1r2680-w873-1vp1-6810-8417s68u22uw",
    "eventID": "07ws3003-0vv4-264x-7kwx-yxy5s69u1tst",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {
        "accountIds": [
            "123456789012"
        ],
        "clientToken": "12345abc-12ab-1234-123a-EXAMPLEeb16b"
    },
    "responseElements": {
        "accountIds": [
            "123456789012"
        ]
    },
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}

```

The following example shows a CloudTrail event that demonstrates the `CreateAutomationRule` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "abcdef01234567890;:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/*****************",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-06T04:19:48Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-06T04:20:00Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "CreateAutomationRule",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "1x2s3791-x984-2wq2-7921-9528t79v33vx",
    "eventID": "18xt4114-1ww5-375y-8lxy-zyz6t70v2utu",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {
        "ruleName": "TestRule",
        "ruleType": "AccountRule",
        "recommendedActionTypes": [
            "SnapshotAndDeleteUnattachedEbsVolume"
        ],
        "schedule": {
            "scheduleExpression": "cron(0 2 * * ? *)",
            "scheduleExpressionTimezone": "UTC",
            "executionWindowInMinutes": 60
        },
        "status": "Active",
        "clientToken": "12345abc-12ab-1234-123a-EXAMPLEeb16b"
    },
    "responseElements": {
        "ruleArn": "arn:aws:compute-optimizer::123456789012:automation-rule/123AbcdEfGHi1jkL",
        "ruleId": "123AbcdEfGHi1jkL",
        "name": "SourabTestRule",
        "ruleType": "AccountRule",
        "ruleRevision": 1,
        "priority": "1E-30",
        "recommendedActionTypes": [
            "SnapshotAndDeleteUnattachedEbsVolume"
        ],
         "criteria": {
            "region": [{
                "comparison": "StringEquals",
                "values": [
                    "us-east-1"
                ]
            }]
        },
        "clientToken": "12345abc-12ab-1234-123a-EXAMPLEeb16b"
    },
    "responseElements": {
        "ruleArn": "arn:aws:compute-optimizer:us-east-1:111122223333:automation-rule/123AbcdEfGHi1jkL"
    },
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}


```

The following example shows a CloudTrail event that demonstrates the `DeleteAutomationRule` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "abcdef01234567890;:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-06T04:19:48Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-06T04:26:15Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "DeleteAutomationRule",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "3z4u5913-z106-4ys4-9143-1740v91x55xz",
    "eventID": "30zv6336-3yy7-597a-0eza-b1b8v92x4wvw",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {
        "ruleArn": "arn:aws:compute-optimizer::111122223333:automation-rule/123AbcdEfGHi1jkL"
    },
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}


```

The following example shows a CloudTrail event that demonstrates the `UpdateAutomationRule` operation.

```

        {
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "abcdef01234567890;:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-06T04:19:48Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-06T04:22:30Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "UpdateAutomationRule",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "2y3t4802-y095-3xr3-8032-0639u80w44wy",
    "eventID": "29yu5225-2xx6-486z-9myz-a0a7u81w3vuv",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {
        "ruleArn": "arn:aws:compute-optimizer:us-east-1:123456789012:automation-rule/123AbcdEfGHi1jkL",
        "status": "Active"
    },
    "responseElements": {
        "ruleArn": "arn:aws:compute-optimizer:us-east-1:123456789012:automation-rule/123AbcdEfGHi1jkL"
    },
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}

```

The following example shows a CloudTrail event that demonstrates the `TagResource` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "abcdef01234567890;:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-06T04:19:48Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-06T04:22:37Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "TagResource",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/Compute_Optimizer_Automation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x86_64 lang/java#17.0.16 md/OpenJDK_64-Bit_Server_VM#17.0.16+8-LTS md/vendor#Amazon.com_Inc. md/en_US md/kotlin/1.9.21-release-633 exec-env/AWS_Lambda_java17 m/E,N,i",
    "requestID": "6c7x8246-c439-7bv7-2476-4073y24a99ab",
    "eventID": "63cy9669-6bb0-820d-3hcd-ede2y25a7bab",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {
        "resourceArn": "arn:aws:compute-optimizer::111122223333:automation-rule/123AbcdEfGHi1jkL",
        "ruleRevision": 1,
        "tags": [{
            "key": "test",
            "value": "cloudtrail"
        }]
    },
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}

```

The following example shows a CloudTrail event that demonstrates the `UntagResource` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "abcdef01234567890;:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`"
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-06T04:19:48Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-06T04:33:09Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "UntagResource",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/Compute_Optimizer_Automation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x86_64 lang/java#17.0.16 md/OpenJDK_64-Bit_Server_VM#17.0.16+8-LTS md/vendor#Amazon.com_Inc. md/en_US md/kotlin/1.9.21-release-633 exec-env/AWS_Lambda_java17 m/E,N,i",
    "requestID": "7d8y9357-d540-8cw8-3587-5184z35b00bc",
    "eventID": "74dz0770-7cc1-931e-4ide-fef3z36b8cbc",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {
        "resourceArn": "arn:aws:compute-optimizer::111122223333:automation-rule/123AbcdEfGHi1jkL",
        "ruleRevision": 2,
        "tagKeys": [
            "test"
        ]
    },
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}

```

The following example shows a CloudTrail event that demonstrates the `RollbackAutomationEvent` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "abcdef01234567890;:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-06T19:31:22Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-06T19:35:59Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "RollbackAutomationEvent",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/Compute_Optimizer_Automation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x86_64 lang/java#17.0.16 md/OpenJDK_64-Bit_Server_VM#17.0.16+8-LTS md/vendor#Amazon.com_Inc. md/en_US md/kotlin/1.9.21-release-633 exec-env/AWS_Lambda_java17 m/E,N,i",
    "requestID": "8e9z0468-e651-9dx9-4698-6295a46c11cd",
    "eventID": "85ea1881-8dd2-042f-5jef-gfg4a47c9dcd",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {
        "eventId": "a52cb5d6d8f24e0c",
        "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    },
    "responseElements": {
        "eventId": "a52cb5d6d8f24e0c",
        "eventStatus": "ROLLBACK_READY"
    },
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}

```

The following example shows a CloudTrail event that demonstrates the `StartAutomationEvent` operation.

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "abcdef01234567890;:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "`ACCESS KEY ID`"
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-06T04:19:48Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-06T04:27:46Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "StartAutomationEvent",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/Compute_Optimizer_Automation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x86_64 lang/java#17.0.16 md/OpenJDK_64-Bit_Server_VM#17.0.16+8-LTS md/vendor#Amazon.com_Inc. md/en_US md/kotlin/1.9.21-release-633 exec-env/AWS_Lambda_java17 m/E,N,i",
    "requestID": "9f0a1579-f762-0ey0-5709-7306b57d22de",
    "eventID": "96fb2992-9ee3-153g-6kfg-hgh5b58d0ede",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {
        "recommendedActionId": "aa112223333a4444"
    },
    "responseElements": {
            "recommendedActionId": "aa112223333a4444",
            "eventId": "a12cb3d4e5f67g0h",
            "status": "READY"
        }
    },
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}

```

For information about CloudTrail record contents, see [CloudTrail
record contents](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md") in the _AWS CloudTrail User Guide_.
