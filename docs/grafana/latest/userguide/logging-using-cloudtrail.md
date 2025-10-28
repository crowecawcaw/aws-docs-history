# Logging Amazon Managed Grafana API calls using

AWS CloudTrail

Amazon Managed Grafana is integrated with [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md"), a
service that provides a record of actions taken by a user, role, or an AWS service. CloudTrail
captures all API calls for Amazon Managed Grafana as events. The calls captured include calls from the
Amazon Managed Grafana console and code calls to the Amazon Managed Grafana API operations.

Amazon Managed Grafana also captures some calls that use Grafana APIs. The calls captured are those
that change data, such as calls that create, update, or delete resources. For more
information about Grafana APIs that are supported in Amazon Managed Grafana, see [Using Grafana HTTP APIs](Using-Grafana-APIs.md "Using-Grafana-APIs.md").

Using the information collected by CloudTrail, you can determine the request that was made to
Amazon Managed Grafana, the IP address from which the request was made, when it was made, and additional
details.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root user or user credentials.
- Whether the request was made on behalf of an IAM Identity Center user.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.
  CloudTrail is active in your AWS account when you create the account and you automatically
  have access to the CloudTrail **Event history**. The CloudTrail **Event
  history** provides a viewable, searchable, downloadable, and immutable record
  of the past 90 days of recorded management events in an AWS Region. For more information,
  see [Working with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the
  _AWS CloudTrail User Guide_. There are no CloudTrail charges for viewing the
  **Event history**.

For an ongoing record of events in your AWS account past 90 days, create a trail or a
[CloudTrail Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") event data store.

**CloudTrail trails**

A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket. All trails created using the AWS Management Console are multi-Region. You can create a single-Region or a multi-Region trail by using the AWS CLI. Creating a multi-Region trail is recommended because you capture activity in all AWS Regions in your account. If you create a single-Region trail, you can view only the events logged in the trail's AWS Region. For more information about trails, see [Creating a trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md") and [Creating a trail for an organization](../../../awscloudtrail/latest/userguide/creating-trail-organization.md "../../../awscloudtrail/latest/userguide/creating-trail-organization.md") in the _AWS CloudTrail User Guide_.

You can deliver one copy of your ongoing management events to your Amazon S3 bucket at no charge from CloudTrail by creating a trail, however, there are Amazon S3 storage charges. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/"). For information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

**CloudTrail Lake event data stores**

_CloudTrail Lake_ lets you run SQL-based queries on your events. CloudTrail Lake converts existing events in row-based JSON format to [Apache ORC](https://orc.apache.org/ "https://orc.apache.org/") format. ORC is a columnar storage format that is optimized for fast retrieval of data. Events are aggregated into _event data stores_, which are immutable collections of events based on criteria that you select by applying [advanced event selectors](../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors "../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors"). The selectors that you apply to an event data store control which events persist and are available for you to query. For more information about CloudTrail Lake, see [Working with AWS CloudTrail Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") in the _AWS CloudTrail User Guide_.

CloudTrail Lake event data stores and queries incur costs. When you create an event data store, you choose the [pricing option](../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option") you want to use for the event data store. The pricing option determines the cost for ingesting and storing events, and the default and maximum retention period for the event data store. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

## Amazon Managed Grafana management events in

CloudTrail

[Management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events") provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

Amazon Managed Grafana logs all Amazon Managed Grafana control plane operations as management events. For a
list of the Amazon Managed Grafana control plane operations that Amazon Managed Grafana logs to CloudTrail, see the
[Amazon Managed Grafana API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

## Amazon Managed Grafana event examples

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

The following example shows a CloudTrail log entry for a CreateWorkspace action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "ANPAJ2UCCR6DPCEXAMPLE:sdbt-example",
        "arn": "arn:aws:sts::123456789012:assumed-role/Admin/sdbt-example",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "ANPAJ2UCCR6DPCEXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/Admin",
                "accountId": "123456789012",
                "userName": "Admin"
            },
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2020-11-26T20:59:21Z"
            }
        }
    },
    "eventTime": "2020-11-26T21:10:48Z",
    "eventSource": "grafana.amazonaws.com",
    "eventName": "CreateWorkspace",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "205.251.233.179",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:82.0) Gecko/20100101 Firefox/82.0",
    "requestParameters": {
        "permissionType": "Service Managed",
        "workspaceNotificationDestinations": [
            "SNS"
        ],
        "workspaceDescription": "",
        "clientToken": "12345678-abcd-1234-5678-111122223333",
        "workspaceDataSources": [
            "SITEWISE",
            "XRAY",
            "CLOUDWATCH",
            "ELASTICSEARCH",
            "PROMETHEUS",
            "TIMESTREAM"
        ],
        "accountAccessType": "CURRENT_ACCOUNT",
        "workspaceName": "CloudTrailTest",
        "workspaceRoleArn": "arn:aws:iam::123456789012:role/service-role/AmazonGrafanaServiceRole-27O5976ol"
    },
    "responseElements": {
        "Access-Control-Expose-Headers": "x-amzn-RequestId,x-amzn-ErrorType,x-amzn-ErrorMessage,Date",
        "workspace": {
            "accountAccessType": "CURRENT_ACCOUNT",
            "created": 1606425045.22,
            "dataSources": [
                "SITEWISE",
                "XRAY",
                "CLOUDWATCH",
                "ELASTICSEARCH",
                "PROMETHEUS",
                "TIMESTREAM"
            ],
            "description": "",
            "grafanaVersion": "7.3.1",
            "id": "g-a187c473d3",
            "modified": 1606425045.22,
            "name": "CloudTrailTest",
            "notificationDestinations": [
                "SNS"
            ],
            "permissionType": "Service Managed",
            "status": "CREATING",
            "workspaceRoleArn": "arn:aws:iam::123456789012:role/service-role/AmazonGrafanaServiceRole-27O5976ol"
        }
    },
    "requestID": "12345678-5533-4e10-b486-e9c7b219f2fd",
    "eventID": "12345678-2710-4359-ad90-b902dbfb606b",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "123456789012"
}
```

The following example shows a CloudTrail log entry for an UpdateWorkspaceAuthentication
action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAU2UJBF3NRO35YZ3GV:CODETEST_Series_GrafanaApiTestHydraCanary12-o6aeXqaXS_1090259374",
        "arn": "arn:aws:sts::332073610971:assumed-role/HydraInvocationRole-4912743f1277b7c3c67cb29518f8bc413ae/CODETEST_Series_GrafanaApiTestHydraCanary12-o6aeXqaXS_1090259374",
        "accountId": "111122223333",
        "accessKeyId": "AIDACKCEVSQ6C2EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAU2UJBF3NRO35YZ3GV",
                "arn": "arn:aws:iam::111122223333:role/HydraInvocationRole-4912743f1277b7c3c67cb29518f8bc413ae",
                "accountId": "332073610971",
                "userName": "TestInvocationRole-4912743f1277b7c3c67cb29518f8bc413ae"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2021-08-04T20:50:24Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2021-08-04T21:29:25Z",
    "eventSource": "gamma-grafana.amazonaws.com",
    "eventName": "UpdateWorkspaceAuthentication",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "34.215.72.249",
    "userAgent": "aws-internal/3 aws-sdk-java/1.11.1030 Linux/4.14.231-180.360.amzn2.x86_64 OpenJDK_64-Bit_Server_VM/11.0.11+9-LTS java/11.0.11 vendor/Amazon.com_Inc. cfg/retry-mode/legacy exec-env/AWS_Lambda_java11",
    "requestParameters": {
        "authenticationProviders": [
            "AWS_SSO",
            "SAML"
        ],
        "samlConfiguration": {
            "idpMetadata": {
                "url": "https://portal.sso.us-east-1.amazonaws.com/saml/metadata/NjMwMDg2NDc4OTA3X2lucy1jY2E2ZGU3ZDlmYjdiM2Vh"
            }
        },
        "workspaceId": "g-84ea23c1b4"
    },
    "responseElements": {
        "authentication": {
            "awsSso": {
                "ssoClientId": "gAROcWGs9-LoqCMIQ56XyEXAMPLE"
            },
            "providers": [
                "AWS_SSO",
                "SAML"
            ],
            "saml": {
                "configuration": {
                    "idpMetadata": {
                        "url": "https://portal.sso.us-east-1.amazonaws.com/saml/metadata/NjMwMDg2NDc4OTA3X2lucy1jY2E2ZGU3ZDlmYjdiM2Vh"
                    },
                    "loginValidityDuration": 60
                },
                "status": "CONFIGURED"
            }
        }
    },
    "requestID": "96adb1de-7fa5-487e-b6c6-6b0d4495cb71",
    "eventID": "406bc825-bc52-475c-9c91-4c0d8a07c1fa",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```

For information about CloudTrail record contents, see [CloudTrail record contents](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md") in the _AWS CloudTrail User Guide_.

## Grafana API event

examples

Amazon Managed Grafana also logs some Grafana API calls in CloudTrail. The calls captured are those that
change data, such as calls that create, update, or delete resources. For more
information about Grafana APIs that are supported in Amazon Managed Grafana, see [Using Grafana HTTP APIs](Using-Grafana-APIs.md "Using-Grafana-APIs.md").

**User signs in to Amazon Managed Grafana workspace using
AWS IAM Identity Center**

```
{
    "Records": [
        {
            "eventVersion": "1.08",
            "userIdentity": {
                "type": "SAMLUser",
                "userName": "johndoe"
            },
            "eventTime": "2021-07-09T02:31:59Z",
            "eventSource": "grafana.amazonaws.com",
            "eventName": "login-auth.sso",
            "awsRegion": "us-west-2",
            "sourceIPAddress": "192.0.2.0,198.51.100.0",
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "requestParameters": null,
            "responseElements": null,
            "eventID": "176bf326-0302-4190-8dbf-dfdf481d8198",
            "readOnly": false,
            "eventType": "AwsServiceEvent",
            "managementEvent": true,
            "eventCategory": "Management",
            "recipientAccountId": "111122223333",
            "serviceEventDetails": {
                "timestamp": "2021-07-09T02:31:59.045984031Z",
                "user": {
                    "userId": 1,
                    "orgId": 1,
                    "name": "johndoe",
                    "isAnonymous": false
                },
                "action": "login-auth.sso",
                "requestUri": "",
                "request": {
                    "query": {
                        "code": [
                            "eyJraWQiOiJrZXktMTU2Njk2ODEyMSIsImFsZyI6IkhTMzg0In0.eyJwbGFpbnRleHQiOiJZUzEwYWtaWHpBZUowTDlQcW5ROGFmZUw2YUZMRklPWUtkX2RRMmhmUUFFIiwiZXhwIjoxNjI1Nzk4MjE4LCJ0eXBlIjoiYXV0aENvZGUifQ.F6MCLvokeXFv1zEwaSg66wdfnNh0dEnLIKBZ4c1dhfNHX_XQywkSq3aqqUg4CsB7"
                        ],
                        "state": [
                            "QUFBQURtdGxlUzB4TlRZNE9UVTFOekkyM2RUWUFUaHZHYXcyOU9ULUVaWHhNUXAwX184N25RVGVWMmd0enFpVE1iWlRPV0M0X09HaDZscjcweDZNbUE3blRjamNISk9RQ2hCUktrY093ZW52aDNWZ2R5UXVndnc4R2g0RkxsamkwMGNvektWbS1KYWRVYnZ0X3AtSU5JRzIxZjFvcWgxN19vM0lPaW9vY1FBVlhLVmEzRE5CRjQxTU1fM3VmYzNWdW53aGZ0QVdFWHBUWTNWTkxrcllKQ3I1akFOUmV1Zlh4Y3ZjQi1XOEVMa0RPUFBqM094VGgta2hHdVFxSDB4YXZKMng"
                        ]
                    }
                },
                "result": {
                    "statusType": "failure"
                },
                "ipAddress": "192.0.2.0,198.51.100.0",
                "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
                "grafanaVersion": "7.5.7",
                "additionalData": {
                    "GiraffeCustomerAccount": "111122223333",
                    "GiraffeWorkspaceId": "g-123EXAMPLE",
                    "extUserInfo": "{\"OAuthToken\":null,\"AuthModule\":\"auth.sso\",\"AuthId\":\"92670be4c1-e524608b-82f2-452d-a707-161c1e5f4706\",\"UserId\":0,\"Email\":\"\",\"Login\":\"johndoe\",\"Name\":\"johndoe\",\"Groups\":null,\"OrgRoles\":{\"1\":\"Admin\"},\"IsGrafanaAdmin\":false,\"IsDisabled\":false}"
                }
            }
        }
    ]
}
```

**Grafana API POST /api/auth/keys**

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "userName": "api_key"
    },
    "eventTime": "2021-07-09T02:16:32Z",
    "eventSource": "grafana.amazonaws.com",
    "eventName": "create",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.0,198.51.100.1",
    "userAgent": "python-requests/2.24.0",
    "errorCode": "200",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "157bbf19-6ba4-4704-bc3b-d3e334b3a2b8",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "111122223333",
    "serviceEventDetails": {
        "timestamp": "2021-07-09T02:16:32.419795511Z",
        "user": {
            "orgId": 1,
            "orgRole": "Admin",
            "name": "api_key",
            "apiKeyId": "23",
            "isAnonymous": false
        },
        "action": "create",
        "resources": [
            {
                "ID": 0,
                "type": "api-key"
            }
        ],
        "requestUri": "",
        "request": {
            "body": "{\"name\":\"keyname\",\"role\":\"Admin\",\"secondsToLive\":60}"
        },
        "result": {
            "statusType": "success",
            "statusCode": "200"
        },
        "ipAddress": "192.0.2.0,198.51.100.1",
        "userAgent": "python-requests/2.24.0",
        "grafanaVersion": "7.5.7",
        "additionalData": {
            "GiraffeCustomerAccount": "111122223333",
            "GiraffeWorkspaceId": "g-123EXAMPLE"
        }
    }
}
```

**Grafana API DELETE /api/auth/keys/:id**

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "userName": "api_key"
    },
    "eventTime": "2021-07-09T02:16:33Z",
    "eventSource": "grafana.amazonaws.com",
    "eventName": "delete",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.0,198.51.100.2",
    "userAgent": "python-requests/2.24.0",
    "errorCode": "200",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "df1aafb3-28c6-4836-a64b-4d34538edc51",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "111122223333",
    "serviceEventDetails": {
        "timestamp": "2021-07-09T02:16:33.045041594Z",
        "user": {
            "orgId": 1,
            "orgRole": "Admin",
            "name": "api_key",
            "apiKeyId": "23",
            "isAnonymous": false
        },
        "action": "delete",
        "resources": [
            {
                "ID": 0,
                "type": "api-key"
            }
        ],
        "requestUri": "",
        "request": {
            "params": {
                ":id": "24"
            }
        },
        "result": {
            "statusType": "success",
            "statusCode": "200"
        },
        "ipAddress": "192.0.2.0,198.51.100.2",
        "userAgent": "python-requests/2.24.0",
        "grafanaVersion": "7.5.7",
        "additionalData": {
            "GiraffeCustomerAccount": "111122223333",
            "GiraffeWorkspaceId": "g-123EXAMPLE"
        }
    }
}
```

**Grafana API POST /api/alerts/:id/pause**

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "userName": "api_key"
    },
    "eventTime": "2021-07-09T02:16:40Z",
    "eventSource": "grafana.amazonaws.com",
    "eventName": "pause",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.0,198.51.100.3",
    "userAgent": "python-requests/2.24.0",
    "errorCode": "200",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "d533a7ba-f193-45ac-a88c-75ed0594509b",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "111122223333",
    "serviceEventDetails": {
        "timestamp": "2021-07-09T02:16:40.261226856Z",
        "user": {
            "orgId": 1,
            "orgRole": "Admin",
            "name": "api_key",
            "apiKeyId": "23",
            "isAnonymous": false
        },
        "action": "pause",
        "resources": [
            {
                "ID": 0,
                "type": "alert"
            }
        ],
        "requestUri": "",
        "request": {
            "params": {
                ":alertId": "1"
            },
            "body": "{\"paused\":true}"
        },
        "result": {
            "statusType": "success",
            "statusCode": "200"
        },
        "ipAddress": "192.0.2.0,198.51.100.3",
        "userAgent": "python-requests/2.24.0",
        "grafanaVersion": "7.5.7",
        "additionalData": {
            "GiraffeCustomerAccount": "111122223333",
            "GiraffeWorkspaceId": "g-123EXAMPLE"
        }
    }
}
```

**Grafana POST /api/alerts/test**

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "userName": "api_key"
    },
    "eventTime": "2021-07-09T02:16:39Z",
    "eventSource": "grafana.amazonaws.com",
    "eventName": "test",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.0,10.0.42.208",
    "userAgent": "python-requests/2.24.0",
    "errorCode": "400",
    "errorMessage": "The dashboard needs to be saved at least once before you can test an alert rule",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "7094644d-8230-4774-a092-8a128eb6dec9",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "111122223333",
    "serviceEventDetails": {
        "timestamp": "2021-07-09T02:16:39.622607860Z",
        "user": {
            "orgId": 1,
            "orgRole": "Admin",
            "name": "api_key",
            "apiKeyId": "23",
            "isAnonymous": false
        },
        "action": "test",
        "resources": [
            {
                "ID": 0,
                "type": "panel"
            }
        ],
        "requestUri": "",
        "request": {},
        "result": {
            "statusType": "failure",
            "statusCode": "400",
            "failureMessage": "The dashboard needs to be saved at least once before you test an alert rule"
        },
        "ipAddress": "192.0.2.0, 10.0.42.208",
        "userAgent": "python-requests/2.24.0",
        "grafanaVersion": "7.5.7",
        "additionalData": {
            "GiraffeCustomerAccount": "111122223333",
            "GiraffeWorkspaceId": "g-123EXAMPLE"
        }
    }
}
```

**Grafana API POST /api/alert-notifications**

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "userName": "api_key"
    },
    "eventTime": "2021-07-09T02:16:40Z",
    "eventSource": "grafana.amazonaws.com",
    "eventName": "create",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.0,198.51.100.0",
    "userAgent": "python-requests/2.24.0",
    "errorCode": "200",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "1ce099b3-c427-4338-9f42-d38d1ef64efe",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "111122223333",
    "serviceEventDetails": {
        "timestamp": "2021-07-09T02:16:40.888295790Z",
        "user": {
            "orgId": 1,
            "orgRole": "Admin",
            "name": "api_key",
            "apiKeyId": "23",
            "isAnonymous": false
        },
        "action": "create",
        "resources": [
            {
                "ID": 0,
                "type": "alert-notification"
            }
        ],
        "requestUri": "",
        "request": {
            "body": "{\"name\":\"alert notification name\",\"type\":\"Slack\"}"
        },
        "result": {
            "statusType": "success",
            "statusCode": "200"
        },
        "ipAddress": "192.0.2.0,198.51.100.0",
        "userAgent": "python-requests/2.24.0",
        "grafanaVersion": "7.5.7",
        "additionalData": {
            "GiraffeCustomerAccount": "111122223333",
            "GiraffeWorkspaceId": "g-123EXAMPLE"
        }
    }
}
```

**Grafana API PUT
/api/alert-notifications/uid/:uid**

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "userName": "api_key"
    },
    "eventTime": "2021-07-09T02:16:42Z",
    "eventSource": "grafana.amazonaws.com",
    "eventName": "update",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.0,198.51.100.3",
    "userAgent": "python-requests/2.24.0",
    "errorCode": "200",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "cebfeb38-5007-495c-bd29-c8077797acac",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "111122223333",
    "serviceEventDetails": {
        "timestamp": "2021-07-09T02:16:42.792652648Z",
        "user": {
            "orgId": 1,
            "orgRole": "Admin",
            "name": "api_key",
            "apiKeyId": "23",
            "isAnonymous": false
        },
        "action": "update",
        "resources": [
            {
                "ID": 0,
                "type": "alert-notification"
            }
        ],
        "requestUri": "",
        "request": {
            "params": {
                ":uid": "WvDWDSinz"
            },
            "body": "{\"name\":\"DIFFERENT alert notification name\",\"type\":\"AWS SNS\"}"
        },
        "result": {
            "statusType": "success",
            "statusCode": "200"
        },
        "ipAddress": "192.0.2.0,198.51.100.3",
        "userAgent": "python-requests/2.24.0",
        "grafanaVersion": "7.5.7",
        "additionalData": {
            "GiraffeCustomerAccount": "111122223333",
            "GiraffeWorkspaceId": "g-123EXAMPLE"
        }
    }
}
```

**Grafana API POST /api/annotations**

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "userName": "api_key"
    },
    "eventTime": "2021-07-09T02:16:45Z",
    "eventSource": "grafana.amazonaws.com",
    "eventName": "create",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.0,198.51.100.1",
    "userAgent": "python-requests/2.24.0",
    "errorCode": "200",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "13bf3bef-966c-4913-a760-ade365a4a08f",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "111122223333",
    "serviceEventDetails": {
        "timestamp": "2021-07-09T02:16:45.394513179Z",
        "user": {
            "orgId": 1,
            "orgRole": "Admin",
            "name": "api_key",
            "apiKeyId": "23",
            "isAnonymous": false
        },
        "action": "create",
        "resources": [
            {
                "ID": 0,
                "type": "annotation"
            }
        ],
        "requestUri": "",
        "request": {
            "body": "{\"dashboardId\":36,\"panelId\":2,\"tags\":[\"tag1\",\"tag2\"],\"what\":\"Event Name\"}"
        },
        "result": {
            "statusType": "success",
            "statusCode": "200"
        },
        "ipAddress": "192.0.2.0,198.51.100.1",
        "userAgent": "python-requests/2.24.0",
        "grafanaVersion": "7.5.7",
        "additionalData": {
            "GiraffeCustomerAccount": "111122223333",
            "GiraffeWorkspaceId": "g-123EXAMPLE"
        }
    }
}
```

**Grafana API DELETE
/api/dashboards/uid/:uid**

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "userName": "api_key"
    },
    "eventTime": "2021-07-09T02:17:09Z",
    "eventSource": "grafana.amazonaws.com",
    "eventName": "delete",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.0,198.51.100.7",
    "userAgent": "python-requests/2.24.0",
    "errorCode": "200",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "d6ad9134-5fbc-403c-a76d-4ed9a81065b6",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "111122223333",
    "serviceEventDetails": {
        "timestamp": "2021-07-09T02:17:09.200112003Z",
        "user": {
            "orgId": 1,
            "orgRole": "Admin",
            "name": "api_key",
            "apiKeyId": "23",
            "isAnonymous": false
        },
        "action": "delete",
        "resources": [
            {
                "ID": 0,
                "type": "dashboard"
            }
        ],
        "requestUri": "",
        "request": {
            "params": {
                ":uid": "GLzWvIi7z"
            }
        },
        "result": {
            "statusType": "success",
            "statusCode": "200"
        },
        "ipAddress": "192.0.2.0,198.51.100.7",
        "userAgent": "python-requests/2.24.0",
        "grafanaVersion": "7.5.7",
        "additionalData": {
            "GiraffeCustomerAccount": "111122223333",
            "GiraffeWorkspaceId": "g-123EXAMPLE"
        }
    }
}
```

**Grafana API PUT
/api/datasources/:datasourceId**

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "userName": "api_key"
    },
    "eventTime": "2021-07-09T02:16:36Z",
    "eventSource": "grafana.amazonaws.com",
    "eventName": "update",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.0,10.0.108.94",
    "userAgent": "python-requests/2.24.0",
    "errorCode": "200",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "92877483-bdf6-44f5-803e-1ac8ad997113",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "111122223333",
    "serviceEventDetails": {
        "timestamp": "2021-07-09T02:16:36.918660585Z",
        "user": {
            "orgId": 1,
            "orgRole": "Admin",
            "name": "api_key",
            "apiKeyId": "23",
            "isAnonymous": false
        },
        "action": "update",
        "resources": [
            {
                "ID": 0,
                "type": "datasource"
            }
        ],
        "requestUri": "",
        "request": {
            "params": {
                ":id": "108"
            },
            "body": "{\"access\":\"proxy\",\"basicAuth\":false,\"name\":\"test_amp_datasource_NEW_name\",\"type\":\"Amazon Managed Prometheus\",\"url\":\"http://amp.amazonaws.com\"}"
        },
        "result": {
            "statusType": "success",
            "statusCode": "200"
        },
        "ipAddress": "192.0.2.0,10.0.108.94",
        "userAgent": "python-requests/2.24.0",
        "grafanaVersion": "7.5.7",
        "additionalData": {
            "GiraffeCustomerAccount": "111122223333",
            "GiraffeWorkspaceId": "g-123EXAMPLE"
        }
    }
}
```

**Grafana API DELETE
/api/teams/:teamId/groups/:groupId**

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "userName": "api_key"
    },
    "eventTime": "2021-07-09T02:17:07Z",
    "eventSource": "grafana.amazonaws.com",
    "eventName": "delete",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.0,198.51.100.2",
    "userAgent": "python-requests/2.24.0",
    "errorCode": "200",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "b41d3967-daab-44d1-994a-a437556add82",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "111122223333",
    "serviceEventDetails": {
        "timestamp": "2021-07-09T02:17:07.296142539Z",
        "user": {
            "orgId": 1,
            "orgRole": "Admin",
            "name": "api_key",
            "apiKeyId": "23",
            "isAnonymous": false
        },
        "action": "delete",
        "resources": [
            {
                "ID": 0,
                "type": "team"
            }
        ],
        "requestUri": "",
        "request": {
            "params": {
                ":groupId": "cn=editors,ou=groups,dc=grafana,dc=org",
                ":teamId": "35"
            }
        },
        "result": {
            "statusType": "success",
            "statusCode": "200"
        },
        "ipAddress": "192.0.2.0,198.51.100.2",
        "userAgent": "python-requests/2.24.0",
        "grafanaVersion": "7.5.7",
        "additionalData": {
            "GiraffeCustomerAccount": "111122223333",
            "GiraffeWorkspaceId": "g-123EXAMPLE"
        }
    }
}
```

**Grafana API PUT /api/folders/:uid**

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "userName": "api_key"
    },
    "eventTime": "2021-07-09T02:16:56Z",
    "eventSource": "grafana.amazonaws.com",
    "eventName": "update",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.0,198.51.100.1",
    "userAgent": "python-requests/2.24.0",
    "errorCode": "412",
    "errorMessage": "the folder has been changed by someone else",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "414c98c8-aa53-45e4-940d-bea55716eaf6",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "111122223333",
    "serviceEventDetails": {
        "timestamp": "2021-07-09T02:16:56.382646826Z",
        "user": {
            "orgId": 1,
            "orgRole": "Admin",
            "name": "api_key",
            "apiKeyId": "23",
            "isAnonymous": false
        },
        "action": "update",
        "resources": [
            {
                "ID": 0,
                "type": "folder"
            }
        ],
        "requestUri": "",
        "request": {
            "params": {
                ":uid": "lnsZvSi7z"
            },
            "body": "{\"title\":\"NEW Folder Name\"}"
        },
        "result": {
            "statusType": "failure",
            "statusCode": "412",
            "failureMessage": "the folder has been changed by someone else"
        },
        "ipAddress": "192.0.2.0,198.51.100.1",
        "userAgent": "python-requests/2.24.0",
        "grafanaVersion": "7.5.7",
        "additionalData": {
            "GiraffeCustomerAccount": "111122223333",
            "GiraffeWorkspaceId": "g-123EXAMPLE"
        }
    }
}
```

**Grafana API POST /api/teams**

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "userName": "api_key"
    },
    "eventTime": "2021-07-09T02:17:02Z",
    "eventSource": "grafana.amazonaws.com",
    "eventName": "create",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.0,10.0.40.206",
    "userAgent": "python-requests/2.24.0",
    "errorCode": "200",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "8d40bd79-76a8-490c-b7bb-74205253b707",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "111122223333",
    "serviceEventDetails": {
        "timestamp": "2021-07-09T02:17:02.845022379Z",
        "user": {
            "orgId": 1,
            "orgRole": "Admin",
            "name": "api_key",
            "apiKeyId": "23",
            "isAnonymous": false
        },
        "action": "create",
        "resources": [
            {
                "ID": 0,
                "type": "team"
            }
        ],
        "requestUri": "",
        "request": {
            "body": "{\"name\":\"TeamName\"}"
        },
        "result": {
            "statusType": "success",
            "statusCode": "200"
        },
        "ipAddress": "192.0.2.0,10.0.40.206",
        "userAgent": "python-requests/2.24.0",
        "grafanaVersion": "7.5.7",
        "additionalData": {
            "GiraffeCustomerAccount": "111122223333",
            "GiraffeWorkspaceId": "g-123EXAMPLE"
        }
    }
}
```
