

# ACM API actions supported in CloudTrail logging
<a name="acm-supported-actions-in-cloudtrail"></a>

ACM supports logging the following actions as events in CloudTrail log files:

Every event or log entry contains information about who generated the request. The identity information helps you determine the following: 
+ Whether the request was made with AWS account root user or AWS Identity and Access Management (IAM) user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service

For more information, see the [CloudTrail userIdentity Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

ACM records management events and data events in CloudTrail.

**Management events**
+ [Adding tags to a certificate ([AddTagsToCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_AddTagsToCertificate.html))](#ct-acm-addtags)
+ [Changing an ACME account key ([ChangeAccountKey](https://docs.aws.amazon.com/acm/latest/APIReference/API_ChangeAccountKey.html))](#ct-acme-changeaccountkey)
+ [Creating an ACME domain validation ([CreateAcmeDomainValidation](https://docs.aws.amazon.com/acm/latest/APIReference/API_CreateAcmeDomainValidation.html))](#ct-acme-createacmedomainvalidation)
+ [Creating an ACME endpoint ([CreateAcmeEndpoint](https://docs.aws.amazon.com/acm/latest/APIReference/API_CreateAcmeEndpoint.html))](#ct-acme-createacmeendpoint)
+ [Creating an ACME external account binding ([CreateAcmeExternalAccountBinding](https://docs.aws.amazon.com/acm/latest/APIReference/API_CreateAcmeExternalAccountBinding.html))](#ct-acme-createacmeexternalaccountbinding)
+ [Deleting an ACME domain validation ([DeleteAcmeDomainValidation](https://docs.aws.amazon.com/acm/latest/APIReference/API_DeleteAcmeDomainValidation.html))](#ct-acme-deleteacmedomainvalidation)
+ [Deleting an ACME endpoint ([DeleteAcmeEndpoint](https://docs.aws.amazon.com/acm/latest/APIReference/API_DeleteAcmeEndpoint.html))](#ct-acme-deleteacmeendpoint)
+ [Deleting an ACME external account binding ([DeleteAcmeExternalAccountBinding](https://docs.aws.amazon.com/acm/latest/APIReference/API_DeleteAcmeExternalAccountBinding.html))](#ct-acme-deleteacmeexternalaccountbinding)
+ [Deleting a certificate ([DeleteCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DeleteCertificate.html))](#ct-acm-delete)
+ [Describing an ACME account ([DescribeAcmeAccount](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeAcmeAccount.html))](#ct-acme-describeacmeaccount)
+ [Describing an ACME domain validation ([DescribeAcmeDomainValidation](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeAcmeDomainValidation.html))](#ct-acme-describeacmedomainvalidation)
+ [Describing an ACME endpoint ([DescribeAcmeEndpoint](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeAcmeEndpoint.html))](#ct-acme-describeacmeendpoint)
+ [Describing an ACME external account binding ([DescribeAcmeExternalAccountBinding](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeAcmeExternalAccountBinding.html))](#ct-acme-describeacmeexternalaccountbinding)
+ [Describing a certificate ([DescribeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html))](#ct-acm-describe)
+ [Exporting a certificate ([ExportCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ExportCertificate.html))](#ct-acm-export)
+ [Retrieving external account binding credentials ([GetAcmeExternalAccountBindingCredentials](https://docs.aws.amazon.com/acm/latest/APIReference/API_GetAcmeExternalAccountBindingCredentials.html))](#ct-acme-getacmeexternalaccountbindingcredentials)
+ [Retrieving a certificate ([GetCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_GetCertificate.html))](#ct-acm-get)
+ [Import a certificate ([ImportCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ImportCertificate.html))](#ct-acm-import)
+ [Listing ACME accounts ([ListAcmeAccounts](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListAcmeAccounts.html))](#ct-acme-listacmeaccounts)
+ [Listing ACME domain validations ([ListAcmeDomainValidations](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListAcmeDomainValidations.html))](#ct-acme-listacmedomainvalidations)
+ [Listing ACME endpoints ([ListAcmeEndpoints](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListAcmeEndpoints.html))](#ct-acme-listacmeendpoints)
+ [Listing ACME external account bindings ([ListAcmeExternalAccountBindings](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListAcmeExternalAccountBindings.html))](#ct-acme-listacmeexternalaccountbindings)
+ [Listing certificates ([ListCertificates](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListCertificates.html))](#ct-acm-list)
+ [Listing tags for a certificate ([ListTagsForCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListTagsForCertificate.html))](#ct-acm-listtags)
+ [Listing tags for a resource ([ListTagsForResource](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListTagsForResource.html))](#ct-acm-listtagsforresource)
+ [Managing an ACME account ([ManageAccount](https://docs.aws.amazon.com/acm/latest/APIReference/API_ManageAccount.html))](#ct-acme-manageaccount)
+ [Registering an ACME account ([NewAccount](https://docs.aws.amazon.com/acm/latest/APIReference/API_NewAccount.html))](#ct-acme-newaccount)
+ [Removing tags from a certificate ([RemoveTagsFromCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RemoveTagsFromCertificate.html))](#ct-acm-removetag)
+ [Requesting a certificate ([RequestCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RequestCertificate.html))](#ct-acm-request)
+ [Resending validation email ([ResendValidationEmail](https://docs.aws.amazon.com/acm/latest/APIReference/API_ResendValidationEmail.html))](#ct-acm-resendmail)
+ [Revoking an ACME account ([RevokeAcmeAccount](https://docs.aws.amazon.com/acm/latest/APIReference/API_RevokeAcmeAccount.html))](#ct-acme-revokeacmeaccount)
+ [Revoking an ACME external account binding ([RevokeAcmeExternalAccountBinding](https://docs.aws.amazon.com/acm/latest/APIReference/API_RevokeAcmeExternalAccountBinding.html))](#ct-acme-revokeacmeexternalaccountbinding)
+ [Revoke a certificate ([RevokeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RevokeCertificate.html))](#ct-acm-revoke)
+ [Searching certificates ([SearchCertificates](https://docs.aws.amazon.com/acm/latest/APIReference/API_SearchCertificates.html))](#ct-acm-search)
+ [Tagging a resource ([TagResource](https://docs.aws.amazon.com/acm/latest/APIReference/API_TagResource.html))](#ct-acm-tagresource)
+ [Removing tags from a resource ([UntagResource](https://docs.aws.amazon.com/acm/latest/APIReference/API_UntagResource.html))](#ct-acm-untagresource)
+ [Updating an ACME domain validation ([UpdateAcmeDomainValidation](https://docs.aws.amazon.com/acm/latest/APIReference/API_UpdateAcmeDomainValidation.html))](#ct-acme-updateacmedomainvalidation)
+ [Updating an ACME endpoint ([UpdateAcmeEndpoint](https://docs.aws.amazon.com/acm/latest/APIReference/API_UpdateAcmeEndpoint.html))](#ct-acme-updateacmeendpoint)

**Data events**
+ [Finalizing an order (FinalizeOrder)](#ct-acme-finalizeorder)
+ [Downloading a certificate (GetCertificate)](#ct-acme-getcertificate)
+ [Retrieving the directory (GetDirectory)](#ct-acme-getdirectory)
+ [Retrieving an order (GetOrder)](#ct-acme-getorder)
+ [Listing orders (ListOrders)](#ct-acme-listorders)
+ [Managing an authorization (ManageAuthorization)](#ct-acme-manageauthorization)
+ [Requesting a nonce (NewNonce)](#ct-acme-newnonce)
+ [Creating an order (NewOrder)](#ct-acme-neworder)
+ [Revoking a certificate (RevokeCertificate)](#ct-acme-revokecertificate)

## Management events
<a name="ct-management-events"></a>

ACM logs the following operations as CloudTrail management events. Management events are logged by default.

### Adding tags to a certificate ([AddTagsToCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_AddTagsToCertificate.html))
<a name="ct-acm-addtags"></a>

The following CloudTrail example shows the results of a call to the [AddTagsToCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_AddTagsToCertificate.html) API. 

```
{

   "Records":[
      {
         "eventVersion":"1.04",
         "userIdentity":{
            "type":"IAMUser",
            "principalId":"AIDACKCEVSQ6C2EXAMPLE",
            "arn":"arn:aws:iam::123456789012:user/Alice",
            "accountId":"123456789012",
            "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
            "userName":"Alice"
         },
         "eventTime":"2016-04-06T13:53:53Z",
         "eventSource":"acm.amazonaws.com",
         "eventName":"AddTagsToCertificate",
         "awsRegion":"us-east-1",
         "sourceIPAddress":"192.0.2.0",
         "userAgent":"aws-cli/1.10.16",
         "requestParameters":{
            "tags":[
               {
                  "value":"Alice",
                  "key":"Admin"
               }
            ],
            "certificateArn":"arn:aws:acm:us-east-1:123456789012:certificate/fedcba98-7654-3210-fedc-ba9876543210"
         },
         "responseElements":null,
         "requestID":"fedcba98-7654-3210-fedc-ba9876543210",
         "eventID":"fedcba98-7654-3210-fedc-ba9876543210",
         "eventType":"AwsApiCall",
         "recipientAccountId":"123456789012"
      }
   ]
}
```

### Changing an ACME account key ([ChangeAccountKey](https://docs.aws.amazon.com/acm/latest/APIReference/API_ChangeAccountKey.html))
<a name="ct-acme-changeaccountkey"></a>

The following CloudTrail example shows a log entry for the `ChangeAccountKey` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "Unknown",
    "principalId": "anonymous",
    "arn": "anonymous",
    "accountId": "123456789012",
    "userName": "anonymous"
  },
  "eventTime": "2026-06-10T20:29:57Z",
  "eventSource": "acm-acme.amazonaws.com",
  "eventName": "ChangeAccountKey",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "serverUuid": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "innerJws": "EXAMPLE"
  },
  "responseElements": {
    "location": "https://acm-acme-enroll.us-east-1.api.aws/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acct/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "status": "valid",
    "orders": "https://acm-acme-enroll.us-east-1.api.aws/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acct/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222/orders"
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme-enroll.us-east-1.api.aws"
  }
}
```

### Creating an ACME domain validation ([CreateAcmeDomainValidation](https://docs.aws.amazon.com/acm/latest/APIReference/API_CreateAcmeDomainValidation.html))
<a name="ct-acme-createacmedomainvalidation"></a>

The following CloudTrail example shows a log entry for the `CreateAcmeDomainValidation` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:example-session",
    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/example-session",
    "accountId": "123456789012",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/example-role",
        "accountId": "123456789012",
        "userName": "example-role"
      },
      "attributes": {
        "creationDate": "2026-06-10T20:28:43Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-06-10T20:28:45Z",
  "eventSource": "acm.amazonaws.com",
  "eventName": "CreateAcmeDomainValidation",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "idempotencyToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "acmeEndpointArn": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "domainName": "example.com",
    "prevalidationOptions": {
      "dnsPrevalidation": {
        "domainScope": {
          "exactDomain": "ENABLED"
        },
        "hostedZoneId": "Z00443972VKAL6HT44MI"
      }
    }
  },
  "responseElements": {
    "acmeDomainValidationArn": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acme-domain-validation/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    },
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeDomainValidation",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acme-domain-validation/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme.us-east-1.api.aws"
  }
}
```

### Creating an ACME endpoint ([CreateAcmeEndpoint](https://docs.aws.amazon.com/acm/latest/APIReference/API_CreateAcmeEndpoint.html))
<a name="ct-acme-createacmeendpoint"></a>

The following CloudTrail example shows a log entry for the `CreateAcmeEndpoint` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:example-session",
    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/example-session",
    "accountId": "123456789012",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/example-role",
        "accountId": "123456789012",
        "userName": "example-role"
      },
      "attributes": {
        "creationDate": "2026-06-10T20:28:43Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-06-10T20:28:45Z",
  "eventSource": "acm.amazonaws.com",
  "eventName": "CreateAcmeEndpoint",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "idempotencyToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "authorizationBehavior": "PRE_APPROVED",
    "certificateAuthority": {
      "publicCertificateAuthority": {
      }
    }
  },
  "responseElements": {
    "acmeEndpointArn": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme.us-east-1.api.aws"
  }
}
```

### Creating an ACME external account binding ([CreateAcmeExternalAccountBinding](https://docs.aws.amazon.com/acm/latest/APIReference/API_CreateAcmeExternalAccountBinding.html))
<a name="ct-acme-createacmeexternalaccountbinding"></a>

The following CloudTrail example shows a log entry for the `CreateAcmeExternalAccountBinding` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:example-session",
    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/example-session",
    "accountId": "123456789012",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/example-role",
        "accountId": "123456789012",
        "userName": "example-role"
      },
      "attributes": {
        "creationDate": "2026-06-10T20:28:43Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-06-10T20:28:45Z",
  "eventSource": "acm.amazonaws.com",
  "eventName": "CreateAcmeExternalAccountBinding",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "idempotencyToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "acmeEndpointArn": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "roleArn": "arn:aws:iam::123456789012:role/example-role",
    "expiration": {
      "value": 1,
      "type": "DAYS"
    }
  },
  "responseElements": {
    "externalAccountBinding": {
      "acmeExternalAccountBindingArn": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acme-external-account-binding/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
      "acmeEndpointArn": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
      "roleArn": "arn:aws:iam::123456789012:role/example-role",
      "expiresAt": "2026-06-11T20:28:45Z"
    }
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    },
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeExternalAccountBinding",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acme-external-account-binding/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme.us-east-1.api.aws"
  }
}
```

### Deleting an ACME domain validation ([DeleteAcmeDomainValidation](https://docs.aws.amazon.com/acm/latest/APIReference/API_DeleteAcmeDomainValidation.html))
<a name="ct-acme-deleteacmedomainvalidation"></a>

The following CloudTrail example shows a log entry for the `DeleteAcmeDomainValidation` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:example-session",
    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/example-session",
    "accountId": "123456789012",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/example-role",
        "accountId": "123456789012",
        "userName": "example-role"
      },
      "attributes": {
        "creationDate": "2026-06-10T20:28:43Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-06-10T20:28:45Z",
  "eventSource": "acm.amazonaws.com",
  "eventName": "DeleteAcmeDomainValidation",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "acmeDomainValidationArn": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acme-domain-validation/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeDomainValidation",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acme-domain-validation/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme.us-east-1.api.aws"
  }
}
```

### Deleting an ACME endpoint ([DeleteAcmeEndpoint](https://docs.aws.amazon.com/acm/latest/APIReference/API_DeleteAcmeEndpoint.html))
<a name="ct-acme-deleteacmeendpoint"></a>

The following CloudTrail example shows a log entry for the `DeleteAcmeEndpoint` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:example-session",
    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/example-session",
    "accountId": "123456789012",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/example-role",
        "accountId": "123456789012",
        "userName": "example-role"
      },
      "attributes": {
        "creationDate": "2026-06-10T20:28:43Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-06-10T20:28:45Z",
  "eventSource": "acm.amazonaws.com",
  "eventName": "DeleteAcmeEndpoint",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "acmeEndpointArn": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme.us-east-1.api.aws"
  }
}
```

### Deleting an ACME external account binding ([DeleteAcmeExternalAccountBinding](https://docs.aws.amazon.com/acm/latest/APIReference/API_DeleteAcmeExternalAccountBinding.html))
<a name="ct-acme-deleteacmeexternalaccountbinding"></a>

The following CloudTrail example shows a log entry for the `DeleteAcmeExternalAccountBinding` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:example-session",
    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/example-session",
    "accountId": "123456789012",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/example-role",
        "accountId": "123456789012",
        "userName": "example-role"
      },
      "attributes": {
        "creationDate": "2026-06-10T20:28:43Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-06-10T20:28:45Z",
  "eventSource": "acm.amazonaws.com",
  "eventName": "DeleteAcmeExternalAccountBinding",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "acmeExternalAccountBindingArn": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acme-external-account-binding/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeExternalAccountBinding",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acme-external-account-binding/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme.us-east-1.api.aws"
  }
}
```

### Deleting a certificate ([DeleteCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DeleteCertificate.html))
<a name="ct-acm-delete"></a>

The following CloudTrail example shows the results of a call to the [DeleteCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DeleteCertificate.html) API. 

```
{

   "Records":[
      {
         "eventVersion":"1.04",
         "userIdentity":{
            "type":"IAMUser",
            "principalId":"AIDACKCEVSQ6C2EXAMPLE",
            "arn":"arn:aws:iam::123456789012:user/Alice",
            "accountId":"123456789012",
            "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
            "userName":"Alice"
         },
         "eventTime":"2016-03-18T00:00:26Z",
         "eventSource":"acm.amazonaws.com",
         "eventName":"DeleteCertificate",
         "awsRegion":"us-east-1",
         "sourceIPAddress":"192.0.2.0",
         "userAgent":"aws-cli/1.9.15",
         "requestParameters":{
            "certificateArn":"arn:aws:acm:us-east-1:123456789012:certificate/fedcba98-7654-3210-fedc-ba9876543210"
         },
         "responseElements":null,
         "requestID":"01234567-89ab-cdef-0123-456789abcdef",
         "eventID":"01234567-89ab-cdef-0123-456789abcdef",
         "eventType":"AwsApiCall",
         "recipientAccountId":"123456789012"
      }
   ]
}
```

### Describing an ACME account ([DescribeAcmeAccount](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeAcmeAccount.html))
<a name="ct-acme-describeacmeaccount"></a>

The following CloudTrail example shows a log entry for the `DescribeAcmeAccount` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:example-session",
    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/example-session",
    "accountId": "123456789012",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/example-role",
        "accountId": "123456789012",
        "userName": "example-role"
      },
      "attributes": {
        "creationDate": "2026-06-10T20:28:43Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-06-10T20:28:46Z",
  "eventSource": "acm.amazonaws.com",
  "eventName": "DescribeAcmeAccount",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "acmeEndpointArn": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "accountUrl": "https://acm-acme-enroll.us-east-1.api.aws/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acct/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": true,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme.us-east-1.api.aws"
  }
}
```

### Describing an ACME domain validation ([DescribeAcmeDomainValidation](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeAcmeDomainValidation.html))
<a name="ct-acme-describeacmedomainvalidation"></a>

The following CloudTrail example shows a log entry for the `DescribeAcmeDomainValidation` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:example-session",
    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/example-session",
    "accountId": "123456789012",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/example-role",
        "accountId": "123456789012",
        "userName": "example-role"
      },
      "attributes": {
        "creationDate": "2026-06-10T20:28:43Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-06-10T20:29:37Z",
  "eventSource": "acm.amazonaws.com",
  "eventName": "DescribeAcmeDomainValidation",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "acmeDomainValidationArn": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acme-domain-validation/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": true,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeDomainValidation",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acme-domain-validation/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme.us-east-1.api.aws"
  }
}
```

### Describing an ACME endpoint ([DescribeAcmeEndpoint](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeAcmeEndpoint.html))
<a name="ct-acme-describeacmeendpoint"></a>

The following CloudTrail example shows a log entry for the `DescribeAcmeEndpoint` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:example-session",
    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/example-session",
    "accountId": "123456789012",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/example-role",
        "accountId": "123456789012",
        "userName": "example-role"
      },
      "attributes": {
        "creationDate": "2026-06-10T20:28:43Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-06-10T20:28:45Z",
  "eventSource": "acm.amazonaws.com",
  "eventName": "DescribeAcmeEndpoint",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "acmeEndpointArn": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": true,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme.us-east-1.api.aws"
  }
}
```

### Describing an ACME external account binding ([DescribeAcmeExternalAccountBinding](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeAcmeExternalAccountBinding.html))
<a name="ct-acme-describeacmeexternalaccountbinding"></a>

The following CloudTrail example shows a log entry for the `DescribeAcmeExternalAccountBinding` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:example-session",
    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/example-session",
    "accountId": "123456789012",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/example-role",
        "accountId": "123456789012",
        "userName": "example-role"
      },
      "attributes": {
        "creationDate": "2026-06-10T20:28:43Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-06-10T20:29:06Z",
  "eventSource": "acm.amazonaws.com",
  "eventName": "DescribeAcmeExternalAccountBinding",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "acmeExternalAccountBindingArn": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acme-external-account-binding/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": true,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeExternalAccountBinding",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acme-external-account-binding/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme.us-east-1.api.aws"
  }
}
```

### Describing a certificate ([DescribeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html))
<a name="ct-acm-describe"></a>

The following CloudTrail example shows the results of a call to the [DescribeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html) API. 

**Note**  
The CloudTrail log for the `DescribeCertificate` operation does not display information about the ACM certificate you specify. You can view information about the certificate by using the console, the AWS Command Line Interface, or the [DescribeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html) API. 

```
{
   "Records":[
      {
         "eventVersion":"1.04",
         "userIdentity":{
            "type":"IAMUser",
            "principalId":"AIDACKCEVSQ6C2EXAMPLE",
            "arn":"arn:aws:iam::123456789012:user/Alice",
            "accountId":"123456789012",
            "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
            "userName":"Alice"
         },
         "eventTime":"2016-03-18T00:00:42Z",
         "eventSource":"acm.amazonaws.com",
         "eventName":"DescribeCertificate",
         "awsRegion":"us-east-1",
         "sourceIPAddress":"192.0.2.0",
         "userAgent":"aws-cli/1.9.15",
         "requestParameters":{
            "certificateArn":"arn:aws:acm:us-east-1:123456789012:certificate/fedcba98-7654-3210-fedc-ba9876543210"
         },
         "responseElements":null,
         "requestID":"fedcba98-7654-3210-fedc-ba9876543210",
         "eventID":"fedcba98-7654-3210-fedc-ba9876543210",
         "eventType":"AwsApiCall",
         "recipientAccountId":"123456789012"
      }
   ]
}
```

### Exporting a certificate ([ExportCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ExportCertificate.html))
<a name="ct-acm-export"></a>

The following CloudTrail example shows the results of a call to the [ExportCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ExportCertificate.html) API. 

```
{
   "Records":[
      {
         "version":"0",
         "id":"01234567-89ab-cdef-0123-456789abcdef",
         "detail-type":"AWS API Call via CloudTrail",
         "source":"aws.acm",
         "account":"123456789012",
         "time":"2018-05-24T15:28:11Z",
         "region":"us-east-1",
         "resources":[

         ],
         "detail":{
            "eventVersion":"1.04",
            "userIdentity":{
               "type":"Root",
               "principalId":"123456789012",
               "arn":"arn:aws:iam::123456789012:user/Alice",
               "accountId":"123456789012",
               "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
               "userName":"Alice"
            },
            "eventTime":"2018-05-24T15:28:11Z",
            "eventSource":"acm.amazonaws.com",
            "eventName":"ExportCertificate",
            "awsRegion":"us-east-1",
            "sourceIPAddress":"192.0.2.0",
            "userAgent":"aws-cli/1.15.4 Python/2.7.9 Windows/8 botocore/1.10.4",
            "requestParameters":{
              "certificateArn":"arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012",
               "passphrase": "HIDDEN_DUE_TO_SECURITY_REASONS"
            },
            "responseElements":{
                "certificateChain":
                "-----BEGIN CERTIFICATE----- 
                {{base64 certificate}} 
                -----END CERTIFICATE-----               
                -----BEGIN CERTIFICATE----- 
                {{base64 certificate}} 
                -----END CERTIFICATE-----",
                "privateKey":"**********",
                "certificate": 
                "-----BEGIN CERTIFICATE----- 
                {{base64 certificate}} 
                -----END CERTIFICATE-----",
                "privateKey": "HIDDEN_DUE_TO_SECURITY_REASONS"
            },
            "requestID":"01234567-89ab-cdef-0123-456789abcdef",
            "eventID":"fedcba98-7654-3210-fedc-ba9876543210",
            "readOnly": false,
            "eventType":"AwsApiCall"
                "managementEvent": true,
                "recipientAccountId": "123456789012",
                "eventCategory": "Management",
                "tlsDetails": {
                     "tlsVersion": "TLSv1.3",
                     "cipherSuite": "TLS_AES_128_GCM_SHA256",
                     "clientProvidedHostHeader": "acm.us-east-1.amazonaws.com"
                 },
                 "sessionCredentialFromConsole": "true"
}
```

### Retrieving external account binding credentials ([GetAcmeExternalAccountBindingCredentials](https://docs.aws.amazon.com/acm/latest/APIReference/API_GetAcmeExternalAccountBindingCredentials.html))
<a name="ct-acme-getacmeexternalaccountbindingcredentials"></a>

The following CloudTrail example shows a log entry for the `GetAcmeExternalAccountBindingCredentials` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:example-session",
    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/example-session",
    "accountId": "123456789012",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/example-role",
        "accountId": "123456789012",
        "userName": "example-role"
      },
      "attributes": {
        "creationDate": "2026-06-10T20:28:43Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-06-10T20:29:26Z",
  "eventSource": "acm.amazonaws.com",
  "eventName": "GetAcmeExternalAccountBindingCredentials",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "acmeExternalAccountBindingArn": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acme-external-account-binding/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": true,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeExternalAccountBinding",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acme-external-account-binding/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme.us-east-1.api.aws"
  }
}
```

### Retrieving a certificate ([GetCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_GetCertificate.html))
<a name="ct-acm-get"></a>

The following CloudTrail example shows the results of a call to the [GetCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_GetCertificate.html) API. 

```
{

   "Records":[
      {
         "eventVersion":"1.04",
         "userIdentity":{
            "type":"IAMUser",
            "principalId":"AIDACKCEVSQ6C2EXAMPLE",
            "arn":"arn:aws:iam::123456789012:user/Alice",
            "accountId":"123456789012",
            "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
            "userName":"Alice"
         },
         "eventTime":"2016-03-18T00:00:41Z",
         "eventSource":"acm.amazonaws.com",
         "eventName":"GetCertificate",
         "awsRegion":"us-east-1",
         "sourceIPAddress":"192.0.2.0",
         "userAgent":"aws-cli/1.9.15",
         "requestParameters":{
            "certificateArn":"arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012"
         },
         "responseElements":{
            "certificateChain":

            "-----BEGIN CERTIFICATE-----
            {{Base64-encoded certificate chain}}
            -----END CERTIFICATE-----",
            "certificate":
            "-----BEGIN CERTIFICATE-----
            {{Base64-encoded certificate}}
            -----END CERTIFICATE-----"

         },
         "requestID":"744dd891-ec9c-11e5-ac34-d1e4dfe1a11b",
         "eventID":"7aa4f909-00dd-478a-9a00-b2709bcad2bb",
         "eventType":"AwsApiCall",
         "recipientAccountId":"123456789012"
      }
   ]
}
```

### Import a certificate ([ImportCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ImportCertificate.html))
<a name="ct-acm-import"></a>

The following example shows the CloudTrail log entry that records a call to the ACM [ImportCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ImportCertificate.html) API operation. 

```
{
   "eventVersion":"1.04",
   "userIdentity":{
      "type":"IAMUser",
      "principalId":"AIDACKCEVSQ6C2EXAMPLE",
      "arn":"arn:aws:iam::111122223333:user/Alice",
      "accountId":"111122223333",
      "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
      "userName":"Alice"
   },
   "eventTime":"2016-10-04T16:01:30Z",
   "eventSource":"acm.amazonaws.com",
   "eventName":"ImportCertificate",
   "awsRegion":"ap-southeast-2",
   "sourceIPAddress":"54.240.193.129",
   "userAgent":"Coral/Netty",
   "requestParameters":{
      "privateKey":{
         "hb":[
            "byte",
            "byte",
            "byte",
            "..."
         ],
         "offset":0,
         "isReadOnly":false,
         "bigEndian":true,
         "nativeByteOrder":false,
         "mark":-1,
         "position":0,
         "limit":1674,
         "capacity":1674,
         "address":0
      },
      "certificateChain":{
         "hb":[
            "byte",
            "byte",
            "byte",
            "..."
         ],
         "offset":0,
         "isReadOnly":false,
         "bigEndian":true,
         "nativeByteOrder":false,
         "mark":-1,
         "position":0,
         "limit":2105,
         "capacity":2105,
         "address":0
      },
      "certificate":{
         "hb":[
            "byte",
            "byte",
            "byte",
            "..."
         ],
         "offset":0,
         "isReadOnly":false,
         "bigEndian":true,
         "nativeByteOrder":false,
         "mark":-1,
         "position":0,
         "limit":2503,
         "capacity":2503,
         "address":0
      }
   },
   "responseElements":{
      "certificateArn":"arn:aws:acm:ap-southeast-2:111122223333:certificate/01234567-89ab-cdef-0123-456789abcdef"
   },
   "requestID":"01234567-89ab-cdef-0123-456789abcdef",
   "eventID":"01234567-89ab-cdef-0123-456789abcdef",
   "eventType":"AwsApiCall",
   "recipientAccountId":"111122223333"
}
```

### Listing ACME accounts ([ListAcmeAccounts](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListAcmeAccounts.html))
<a name="ct-acme-listacmeaccounts"></a>

The following CloudTrail example shows a log entry for the `ListAcmeAccounts` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:example-session",
    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/example-session",
    "accountId": "123456789012",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/example-role",
        "accountId": "123456789012",
        "userName": "example-role"
      },
      "attributes": {
        "creationDate": "2026-06-10T20:28:43Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-06-10T20:29:37Z",
  "eventSource": "acm.amazonaws.com",
  "eventName": "ListAcmeAccounts",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "acmeEndpointArn": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": true,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme.us-east-1.api.aws"
  }
}
```

### Listing ACME domain validations ([ListAcmeDomainValidations](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListAcmeDomainValidations.html))
<a name="ct-acme-listacmedomainvalidations"></a>

The following CloudTrail example shows a log entry for the `ListAcmeDomainValidations` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:example-session",
    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/example-session",
    "accountId": "123456789012",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/example-role",
        "accountId": "123456789012",
        "userName": "example-role"
      },
      "attributes": {
        "creationDate": "2026-06-10T20:28:43Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-06-10T20:29:57Z",
  "eventSource": "acm.amazonaws.com",
  "eventName": "ListAcmeDomainValidations",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "acmeEndpointArn": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": true,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme.us-east-1.api.aws"
  }
}
```

### Listing ACME endpoints ([ListAcmeEndpoints](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListAcmeEndpoints.html))
<a name="ct-acme-listacmeendpoints"></a>

The following CloudTrail example shows a log entry for the `ListAcmeEndpoints` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:example-session",
    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/example-session",
    "accountId": "123456789012",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/example-role",
        "accountId": "123456789012",
        "userName": "example-role"
      },
      "attributes": {
        "creationDate": "2026-06-10T20:28:43Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-06-10T20:28:56Z",
  "eventSource": "acm.amazonaws.com",
  "eventName": "ListAcmeEndpoints",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme.us-east-1.api.aws"
  }
}
```

### Listing ACME external account bindings ([ListAcmeExternalAccountBindings](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListAcmeExternalAccountBindings.html))
<a name="ct-acme-listacmeexternalaccountbindings"></a>

The following CloudTrail example shows a log entry for the `ListAcmeExternalAccountBindings` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:example-session",
    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/example-session",
    "accountId": "123456789012",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/example-role",
        "accountId": "123456789012",
        "userName": "example-role"
      },
      "attributes": {
        "creationDate": "2026-06-10T20:28:43Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-06-10T20:29:15Z",
  "eventSource": "acm.amazonaws.com",
  "eventName": "ListAcmeExternalAccountBindings",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "acmeEndpointArn": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": true,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme.us-east-1.api.aws"
  }
}
```

### Listing certificates ([ListCertificates](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListCertificates.html))
<a name="ct-acm-list"></a>

The following CloudTrail example shows the results of a call to the [ListCertificates](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListCertificates.html) API. 

**Note**  
The CloudTrail log for the `ListCertificates` operation does not display your ACM certificates. You can view the certificate list by using the console, the AWS Command Line Interface, or the [ListCertificates](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListCertificates.html) API. 

```
{
   "Records":[
      {
         "eventVersion":"1.04",
         "userIdentity":{
            "type":"IAMUser",
            "principalId":"AIDACKCEVSQ6C2EXAMPLE",
            "arn":"arn:aws:iam::123456789012:user/Alice",
            "accountId":"123456789012",
            "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
            "userName":"Alice"
         },
         "eventTime":"2016-03-18T00:00:43Z",
         "eventSource":"acm.amazonaws.com",
         "eventName":"ListCertificates",
         "awsRegion":"us-east-1",
         "sourceIPAddress":"192.0.2.0",
         "userAgent":"aws-cli/1.9.15",
         "requestParameters":{
            "maxItems":1000,
            "certificateStatuses":[
               "ISSUED"
            ]
         },
         "responseElements":null,
         "requestID":"74c99844-ec9c-11e5-ac34-d1e4dfe1a11b",
         "eventID":"cdfe1051-88aa-4aa3-8c33-a325270bff21",
         "eventType":"AwsApiCall",
         "recipientAccountId":"123456789012"
      }
   ]
}
```

### Listing tags for a certificate ([ListTagsForCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListTagsForCertificate.html))
<a name="ct-acm-listtags"></a>

The following CloudTrail example shows the results of a call to the [ListTagsForCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListTagsForCertificate.html) API. 

**Note**  
The CloudTrail log for the `ListTagsForCertificate` operation does not display your tags. You can view the tag list by using the console, the AWS Command Line Interface, or the [ListTagsForCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListTagsForCertificate.html) API. 

```
{
   "Records":[
      {
         "eventVersion":"1.04",
         "userIdentity":{
            "type":"IAMUser",
            "principalId":"AIDACKCEVSQ6C2EXAMPLE",
            "arn":"arn:aws:iam::123456789012:user/Alice",
            "accountId":"123456789012",
            "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
            "userName":"Alice"
         },
         "eventTime":"2016-04-06T13:30:11Z",
         "eventSource":"acm.amazonaws.com",
         "eventName":"ListTagsForCertificate",
         "awsRegion":"us-east-1",
         "sourceIPAddress":"192.0.2.0",
         "userAgent":"aws-cli/1.10.16",
         "requestParameters":{
            "certificateArn":"arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012"
         },
         "responseElements":null,
         "requestID":"b010767f-fbfb-11e5-b596-79e9a97a2544",
         "eventID":"32181be6-a4a0-48d3-8014-c0d972b5163b",
         "eventType":"AwsApiCall",
         "recipientAccountId":"123456789012"
      }
   ]
}
```

### Listing tags for a resource ([ListTagsForResource](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListTagsForResource.html))
<a name="ct-acm-listtagsforresource"></a>

The following example shows a CloudTrail log entry for the [ListTagsForResource](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListTagsForResource.html) API. 

The CloudTrail log for the `ListTagsForResource` operation does not display tags in the response elements.

```
{
         "eventVersion":"1.04",
         "userIdentity":{
            "type":"IAMUser",
            "principalId":"AIDACKCEVSQ6C2EXAMPLE",
            "arn":"arn:aws:iam::123456789012:user/Alice",
            "accountId":"123456789012",
            "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
            "userName":"Alice"
         },
         "eventTime":"2026-01-15T20:43:00Z",
         "eventSource":"acm.amazonaws.com",
         "eventName":"ListTagsForResource",
         "awsRegion":"us-east-1",
         "sourceIPAddress":"192.0.2.0",
         "userAgent":"aws-cli/2.0",
         "requestParameters":{
            "resourceArn":"arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-abc123"
         },
         "responseElements":null,
         "requestID":"fedcba98-7654-3210-fedc-ba9876543212",
         "eventID":"12345678-1234-1234-1234-123456789014",
         "eventType":"AwsApiCall",
         "recipientAccountId":"123456789012"
}
```

### Managing an ACME account ([ManageAccount](https://docs.aws.amazon.com/acm/latest/APIReference/API_ManageAccount.html))
<a name="ct-acme-manageaccount"></a>

The following CloudTrail example shows a log entry for the `ManageAccount` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "Unknown",
    "principalId": "anonymous",
    "arn": "anonymous",
    "accountId": "123456789012",
    "userName": "anonymous"
  },
  "eventTime": "2026-06-10T20:30:40Z",
  "eventSource": "acm-acme.amazonaws.com",
  "eventName": "ManageAccount",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "serverUuid": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "accountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
  },
  "responseElements": {
    "location": "https://acm-acme-enroll.us-east-1.api.aws/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acct/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "status": "valid",
    "contact": "HIDDEN_DUE_TO_SECURITY_REASONS",
    "orders": "https://acm-acme-enroll.us-east-1.api.aws/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acct/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222/orders"
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme-enroll.us-east-1.api.aws"
  }
}
```

### Registering an ACME account ([NewAccount](https://docs.aws.amazon.com/acm/latest/APIReference/API_NewAccount.html))
<a name="ct-acme-newaccount"></a>

The following CloudTrail example shows a log entry for the `NewAccount` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "Unknown",
    "principalId": "anonymous",
    "arn": "anonymous",
    "accountId": "123456789012",
    "userName": "anonymous"
  },
  "eventTime": "2026-06-10T20:30:39Z",
  "eventSource": "acm-acme.amazonaws.com",
  "eventName": "NewAccount",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "serverUuid": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "contact": "HIDDEN_DUE_TO_SECURITY_REASONS",
    "externalAccountBinding": {
      "jwsProtected": "EXAMPLE",
      "payload": "EXAMPLE",
      "signature": "EXAMPLE"
    }
  },
  "responseElements": {
    "location": "https://acm-acme-enroll.us-east-1.api.aws/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acct/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "status": "valid",
    "contact": "HIDDEN_DUE_TO_SECURITY_REASONS",
    "orders": "https://acm-acme-enroll.us-east-1.api.aws/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acct/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222/orders",
    "externalAccountBinding": {
      "jwsProtected": "EXAMPLE",
      "payload": "EXAMPLE",
      "signature": "EXAMPLE"
    },
    "statusCode": 201
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme-enroll.us-east-1.api.aws"
  }
}
```

### Removing tags from a certificate ([RemoveTagsFromCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RemoveTagsFromCertificate.html))
<a name="ct-acm-removetag"></a>

The following CloudTrail example shows the results of a call to the [RemoveTagsFromCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RemoveTagsFromCertificate.html) API. 

```
{
   "Records":[
      {
         "eventVersion":"1.04",
         "userIdentity":{
            "type":"IAMUser",
            "principalId":"AIDACKCEVSQ6C2EXAMPLE",
            "arn":"arn:aws:iam::123456789012:user/Alice",
            "accountId":"123456789012",
            "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
            "userName":"Alice"
         },
         "eventTime":"2016-04-06T14:10:01Z",
         "eventSource":"acm.amazonaws.com",
         "eventName":"RemoveTagsFromCertificate",
         "awsRegion":"us-east-1",
         "sourceIPAddress":"192.0.2.0",
         "userAgent":"aws-cli/1.10.16",
         "requestParameters":{
            "certificateArn":"arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012",
            "tags":[
               {
                  "value":"Bob",
                  "key":"Admin"
               }
            ]
         },
         "responseElements":null,
         "requestID":"40ded461-fc01-11e5-a747-85804766d6c9",
         "eventID":"0cfa142e-ef74-4b21-9515-47197780c424",
         "eventType":"AwsApiCall",
         "recipientAccountId":"123456789012"
      }
   ]
}
```

### Requesting a certificate ([RequestCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RequestCertificate.html))
<a name="ct-acm-request"></a>

The following CloudTrail example shows the results of a call to the [RequestCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RequestCertificate.html) API. 

```
{
   "Records":[
      {
         "eventVersion":"1.04",
         "userIdentity":{
            "type":"IAMUser",
            "principalId":"AIDACKCEVSQ6C2EXAMPLE",
            "arn":"arn:aws:iam::123456789012:user/Alice",
            "accountId":"123456789012",
            "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
            "userName":"Alice"
         },
         "eventTime":"2016-03-18T00:00:49Z",
         "eventSource":"acm.amazonaws.com",
         "eventName":"RequestCertificate",
         "awsRegion":"us-east-1",
         "sourceIPAddress":"192.0.2.0",
         "userAgent":"aws-cli/1.9.15",
         "requestParameters":{
            "domainName":"example.com",
            "validationMethod": "DNS",
            "idempotencyToken":"8186023d89681c3ad5",
            "options": {
            "export": "ENABLED"
        },
        "keyAlgorithm": "RSA_2048"
         },
         "responseElements":{
            "certificateArn":"arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012"
         },
         "requestID":"77dacef3-ec9c-11e5-ac34-d1e4dfe1a11b",
         "eventID":"a4954cdb-8f38-44c7-8927-a38ad4be3ac8",
         "eventType":"AwsApiCall",
         "tlsDetails": {
           "tlsVersion": "TLSv1.3",
           "cipherSuite": "TLS_AES_128_GCM_SHA256",
           "clientProvidedHostHeader": "acm.us-east-1.amazonaws.com"
          },
         "recipientAccountId":"123456789012"
      }
   ]
}
```

### Resending validation email ([ResendValidationEmail](https://docs.aws.amazon.com/acm/latest/APIReference/API_ResendValidationEmail.html))
<a name="ct-acm-resendmail"></a>

The following CloudTrail example shows the results of a call to the [ResendValidationEmail](https://docs.aws.amazon.com/acm/latest/APIReference/API_ResendValidationEmail.html) API. 

```
{
   "Records":[
      {
         "eventVersion":"1.04",
         "userIdentity":{
            "type":"IAMUser",
            "principalId":"AIDACKCEVSQ6C2EXAMPLE",
            "arn":"arn:aws:iam::123456789012:user/Alice",
            "accountId":"123456789012",
            "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
            "userName":"Alice"
         },
         "eventTime":"2016-03-17T23:58:25Z",
         "eventSource":"acm.amazonaws.com",
         "eventName":"ResendValidationEmail",
         "awsRegion":"us-east-1",
         "sourceIPAddress":"192.0.2.0",
         "userAgent":"aws-cli/1.9.15",
         "requestParameters":{
            "domain":"example.com",
            "certificateArn":"arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012",
            "validationDomain":"example.com"
         },
         "responseElements":null,
         "requestID":"23760b88-ec9c-11e5-b6f4-cb861a6f0a28",
         "eventID":"41c11b06-ca91-4c1c-8c61-af349ea8bab8",
         "eventType":"AwsApiCall",
         "recipientAccountId":"123456789012"
      }
   ]
}
```

### Revoking an ACME account ([RevokeAcmeAccount](https://docs.aws.amazon.com/acm/latest/APIReference/API_RevokeAcmeAccount.html))
<a name="ct-acme-revokeacmeaccount"></a>

The following CloudTrail example shows a log entry for the `RevokeAcmeAccount` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:example-session",
    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/example-session",
    "accountId": "123456789012",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/example-role",
        "accountId": "123456789012",
        "userName": "example-role"
      },
      "attributes": {
        "creationDate": "2026-06-10T20:28:43Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-06-10T20:28:46Z",
  "eventSource": "acm.amazonaws.com",
  "eventName": "RevokeAcmeAccount",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "acmeEndpointArn": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "accountUrl": "https://acm-acme-enroll.us-east-1.api.aws/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acct/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme.us-east-1.api.aws"
  }
}
```

### Revoking an ACME external account binding ([RevokeAcmeExternalAccountBinding](https://docs.aws.amazon.com/acm/latest/APIReference/API_RevokeAcmeExternalAccountBinding.html))
<a name="ct-acme-revokeacmeexternalaccountbinding"></a>

The following CloudTrail example shows a log entry for the `RevokeAcmeExternalAccountBinding` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:example-session",
    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/example-session",
    "accountId": "123456789012",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/example-role",
        "accountId": "123456789012",
        "userName": "example-role"
      },
      "attributes": {
        "creationDate": "2026-06-10T20:28:43Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-06-10T20:28:56Z",
  "eventSource": "acm.amazonaws.com",
  "eventName": "RevokeAcmeExternalAccountBinding",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "acmeExternalAccountBindingArn": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acme-external-account-binding/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeExternalAccountBinding",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acme-external-account-binding/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme.us-east-1.api.aws"
  }
}
```

### Revoke a certificate ([RevokeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RevokeCertificate.html))
<a name="ct-acm-revoke"></a>

The following CloudTrail example shows the results of a call to the [RevokeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RevokeCertificate.html) API. 

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE:Role-Session-Name",
        "arn": arn:aws:sts::111122223333:assumed-role/Role-Name/Role-Session-Name",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDACKCEVSQ6C2EXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/Admin",
                "accountId": "123456789012",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2016-01-01T19:35:52Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime":"2016-01-01T21:11:45Z",
    "eventSource": "acm.amazonaws.com",
    "eventName": "RevokeCertificate",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "requestParameters": {
        "certificateArn": "arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012",
        "revocationReason": "UNSPECIFIED"
    },
    "responseElements": {
        "certificateArn": "arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012"
    },
    "requestID": "01234567-89ab-cdef-0123-456789abcdef",
    "eventID": "01234567-89ab-cdef-0123-456789abcdef",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "acm.us-east-1.amazonaws.com"
    },
    "sessionCredentialFromConsole": "true"
}
```

### Searching certificates ([SearchCertificates](https://docs.aws.amazon.com/acm/latest/APIReference/API_SearchCertificates.html))
<a name="ct-acm-search"></a>

The following CloudTrail example shows the results of a call to the [SearchCertificates](https://docs.aws.amazon.com/acm/latest/APIReference/API_SearchCertificates.html) API. 

```
{

   "Records":[
      {
         "eventVersion":"1.04",
         "userIdentity":{
            "type":"IAMUser",
            "principalId":"AIDACKCEVSQ6C2EXAMPLE",
            "arn":"arn:aws:iam::123456789012:user/Alice",
            "accountId":"123456789012",
            "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
            "userName":"Alice"
         },
         "eventTime":"2016-04-06T13:53:53Z",
         "eventSource":"acm.amazonaws.com",
         "eventName":"SearchCertificates",
         "awsRegion":"us-east-1",
         "sourceIPAddress":"192.0.2.0",
         "userAgent":"aws-cli/1.10.16",
         "readOnly":true,
         "requestParameters":{
            "maxResults":10,
            "sortBy":"CREATED_AT",
            "sortOrder":"DESCENDING"
         },
         "responseElements":null,
         "requestID":"01234567-89ab-cdef-0123-456789abcdef",
         "eventID":"01234567-89ab-cdef-0123-456789abcdef",
         "eventType":"AwsApiCall",
         "recipientAccountId":"123456789012"
      }
   ]
}
```

### Tagging a resource ([TagResource](https://docs.aws.amazon.com/acm/latest/APIReference/API_TagResource.html))
<a name="ct-acm-tagresource"></a>

The following example shows a CloudTrail log entry for the [TagResource](https://docs.aws.amazon.com/acm/latest/APIReference/API_TagResource.html) API. 

```
{
         "eventVersion":"1.04",
         "userIdentity":{
            "type":"IAMUser",
            "principalId":"AIDACKCEVSQ6C2EXAMPLE",
            "arn":"arn:aws:iam::123456789012:user/Alice",
            "accountId":"123456789012",
            "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
            "userName":"Alice"
         },
         "eventTime":"2026-01-15T20:41:00Z",
         "eventSource":"acm.amazonaws.com",
         "eventName":"TagResource",
         "awsRegion":"us-east-1",
         "sourceIPAddress":"192.0.2.0",
         "userAgent":"aws-cli/2.0",
         "requestParameters":{
            "resourceArn":"arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-abc123",
            "tags":[
               {
                  "key":"Environment",
                  "value":"Production"
               }
            ]
         },
         "responseElements":null,
         "requestID":"fedcba98-7654-3210-fedc-ba9876543210",
         "eventID":"12345678-1234-1234-1234-123456789012",
         "eventType":"AwsApiCall",
         "recipientAccountId":"123456789012"
}
```

### Removing tags from a resource ([UntagResource](https://docs.aws.amazon.com/acm/latest/APIReference/API_UntagResource.html))
<a name="ct-acm-untagresource"></a>

The following example shows a CloudTrail log entry for the [UntagResource](https://docs.aws.amazon.com/acm/latest/APIReference/API_UntagResource.html) API. 

```
{
         "eventVersion":"1.04",
         "userIdentity":{
            "type":"IAMUser",
            "principalId":"AIDACKCEVSQ6C2EXAMPLE",
            "arn":"arn:aws:iam::123456789012:user/Alice",
            "accountId":"123456789012",
            "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
            "userName":"Alice"
         },
         "eventTime":"2026-01-15T20:42:00Z",
         "eventSource":"acm.amazonaws.com",
         "eventName":"UntagResource",
         "awsRegion":"us-east-1",
         "sourceIPAddress":"192.0.2.0",
         "userAgent":"aws-cli/2.0",
         "requestParameters":{
            "resourceArn":"arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-abc123",
            "tagKeys":["Environment"]
         },
         "responseElements":null,
         "requestID":"fedcba98-7654-3210-fedc-ba9876543211",
         "eventID":"12345678-1234-1234-1234-123456789013",
         "eventType":"AwsApiCall",
         "recipientAccountId":"123456789012"
}
```

### Updating an ACME domain validation ([UpdateAcmeDomainValidation](https://docs.aws.amazon.com/acm/latest/APIReference/API_UpdateAcmeDomainValidation.html))
<a name="ct-acme-updateacmedomainvalidation"></a>

The following CloudTrail example shows a log entry for the `UpdateAcmeDomainValidation` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:example-session",
    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/example-session",
    "accountId": "123456789012",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/example-role",
        "accountId": "123456789012",
        "userName": "example-role"
      },
      "attributes": {
        "creationDate": "2026-06-10T20:28:43Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-06-10T20:29:46Z",
  "eventSource": "acm.amazonaws.com",
  "eventName": "UpdateAcmeDomainValidation",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "acmeDomainValidationArn": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acme-domain-validation/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeDomainValidation",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/acme-domain-validation/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme.us-east-1.api.aws"
  }
}
```

### Updating an ACME endpoint ([UpdateAcmeEndpoint](https://docs.aws.amazon.com/acm/latest/APIReference/API_UpdateAcmeEndpoint.html))
<a name="ct-acme-updateacmeendpoint"></a>

The following CloudTrail example shows a log entry for the `UpdateAcmeEndpoint` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:example-session",
    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/example-session",
    "accountId": "123456789012",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/example-role",
        "accountId": "123456789012",
        "userName": "example-role"
      },
      "attributes": {
        "creationDate": "2026-06-10T20:28:43Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-06-10T20:28:56Z",
  "eventSource": "acm.amazonaws.com",
  "eventName": "UpdateAcmeEndpoint",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "acmeEndpointArn": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme.us-east-1.api.aws"
  }
}
```

## Data events
<a name="ct-data-events"></a>

ACM logs the following ACME protocol operations as CloudTrail data events. Unlike management events, data events are not logged by default. To record them, configure data event logging in your CloudTrail trail or event data store.

### Finalizing an order (FinalizeOrder)
<a name="ct-acme-finalizeorder"></a>

The following CloudTrail example shows a data event log entry for the `FinalizeOrder` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:example-session",
    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/example-session",
    "accountId": "123456789012",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/example-role",
        "accountId": "123456789012",
        "userName": "example-role"
      },
      "attributes": {
        "creationDate": "2026-06-10T20:29:27Z",
        "mfaAuthenticated": "false"
      },
      "sourceIdentity": "acm-acme-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    },
    "invokedBy": "acm-acme.amazonaws.com"
  },
  "eventTime": "2026-06-10T20:29:27Z",
  "eventSource": "acm-acme.amazonaws.com",
  "eventName": "FinalizeOrder",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "acm-acme.amazonaws.com",
  "userAgent": "acm-acme.amazonaws.com",
  "requestParameters": {
    "serverUuid": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "orderId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "csr": "EXAMPLE"
  },
  "responseElements": {
    "status": "processing",
    "expires": "2026-06-17T20:29:27Z",
    "identifiers": [
      {
        "type": "dns",
        "value": "example.example.com"
      }
    ],
    "authorizations": [
      "https://acm-acme-enroll.us-east-1.api.aws/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/authz/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"
    ],
    "finalize": "https://acm-acme-enroll.us-east-1.api.aws/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/order/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222/finalize",
    "location": "https://acm-acme-enroll.us-east-1.api.aws/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/order/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "statusCode": 200
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE66666"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": false,
  "recipientAccountId": "123456789012",
  "eventCategory": "Data"
}
```

### Downloading a certificate (GetCertificate)
<a name="ct-acme-getcertificate"></a>

The following CloudTrail example shows a data event log entry for the `GetCertificate` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "Unknown",
    "principalId": "anonymous",
    "arn": "anonymous",
    "accountId": "123456789012",
    "userName": "anonymous"
  },
  "eventTime": "2026-06-10T20:29:56Z",
  "eventSource": "acm-acme.amazonaws.com",
  "eventName": "GetCertificate",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "serverUuid": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "certId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE77777"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
  "readOnly": true,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE66666"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": false,
  "recipientAccountId": "123456789012",
  "eventCategory": "Data",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme-enroll.us-east-1.api.aws"
  }
}
```

### Retrieving the directory (GetDirectory)
<a name="ct-acme-getdirectory"></a>

The following CloudTrail example shows a data event log entry for the `GetDirectory` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "Unknown",
    "principalId": "anonymous",
    "arn": "anonymous",
    "accountId": "123456789012",
    "userName": "anonymous"
  },
  "eventTime": "2026-06-10T20:30:39Z",
  "eventSource": "acm-acme.amazonaws.com",
  "eventName": "GetDirectory",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "serverUuid": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
  "readOnly": true,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE66666"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": false,
  "recipientAccountId": "123456789012",
  "eventCategory": "Data",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme-enroll.us-east-1.api.aws"
  }
}
```

### Retrieving an order (GetOrder)
<a name="ct-acme-getorder"></a>

The following CloudTrail example shows a data event log entry for the `GetOrder` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "Unknown",
    "principalId": "anonymous",
    "arn": "anonymous",
    "accountId": "123456789012",
    "userName": "anonymous"
  },
  "eventTime": "2026-06-10T20:30:38Z",
  "eventSource": "acm-acme.amazonaws.com",
  "eventName": "GetOrder",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "serverUuid": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "orderId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
  "readOnly": true,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE66666"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": false,
  "recipientAccountId": "123456789012",
  "eventCategory": "Data",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme-enroll.us-east-1.api.aws"
  }
}
```

### Listing orders (ListOrders)
<a name="ct-acme-listorders"></a>

The following CloudTrail example shows a data event log entry for the `ListOrders` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "Unknown",
    "principalId": "anonymous",
    "arn": "anonymous",
    "accountId": "123456789012",
    "userName": "anonymous"
  },
  "eventTime": "2026-06-10T20:29:57Z",
  "eventSource": "acm-acme.amazonaws.com",
  "eventName": "ListOrders",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "serverUuid": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "accountId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE88888"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
  "readOnly": true,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE66666"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": false,
  "recipientAccountId": "123456789012",
  "eventCategory": "Data",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme-enroll.us-east-1.api.aws"
  }
}
```

### Managing an authorization (ManageAuthorization)
<a name="ct-acme-manageauthorization"></a>

The following CloudTrail example shows a data event log entry for the `ManageAuthorization` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "Unknown",
    "principalId": "anonymous",
    "arn": "anonymous",
    "accountId": "123456789012",
    "userName": "anonymous"
  },
  "eventTime": "2026-06-10T20:30:40Z",
  "eventSource": "acm-acme.amazonaws.com",
  "eventName": "ManageAuthorization",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "serverUuid": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "authorizationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE99999"
  },
  "responseElements": {
    "location": "https://acm-acme-enroll.us-east-1.api.aws/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/authz/a1b2c3d4-5678-90ab-cdef-EXAMPLE99999",
    "status": "valid",
    "expires": "2026-06-17T20:30:40Z",
    "identifier": {
      "type": "dns",
      "value": "example.example.com"
    },
    "challenges": []
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE66666"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": false,
  "recipientAccountId": "123456789012",
  "eventCategory": "Data",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme-enroll.us-east-1.api.aws"
  }
}
```

### Requesting a nonce (NewNonce)
<a name="ct-acme-newnonce"></a>

The following CloudTrail example shows a data event log entry for the `NewNonce` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "Unknown",
    "principalId": "anonymous",
    "arn": "anonymous",
    "accountId": "123456789012",
    "userName": "anonymous"
  },
  "eventTime": "2026-06-10T20:30:39Z",
  "eventSource": "acm-acme.amazonaws.com",
  "eventName": "NewNonce",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "serverUuid": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE66666"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": false,
  "recipientAccountId": "123456789012",
  "eventCategory": "Data",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme-enroll.us-east-1.api.aws"
  }
}
```

### Creating an order (NewOrder)
<a name="ct-acme-neworder"></a>

The following CloudTrail example shows a data event log entry for the `NewOrder` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "Unknown",
    "principalId": "anonymous",
    "arn": "anonymous",
    "accountId": "123456789012",
    "userName": "anonymous"
  },
  "eventTime": "2026-06-10T20:29:26Z",
  "eventSource": "acm-acme.amazonaws.com",
  "eventName": "NewOrder",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.0",
  "requestParameters": {
    "serverUuid": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "identifiers": [
      {
        "type": "dns",
        "value": "example.example.com"
      }
    ]
  },
  "responseElements": {
    "status": "ready",
    "expires": "2026-06-17T20:29:26Z",
    "identifiers": [
      {
        "type": "dns",
        "value": "example.example.com"
      }
    ],
    "authorizations": [
      "https://acm-acme-enroll.us-east-1.api.aws/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/authz/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"
    ],
    "finalize": "https://acm-acme-enroll.us-east-1.api.aws/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/order/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222/finalize",
    "location": "https://acm-acme-enroll.us-east-1.api.aws/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/order/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "statusCode": 201
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE66666"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": false,
  "recipientAccountId": "123456789012",
  "eventCategory": "Data",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "acm-acme-enroll.us-east-1.api.aws"
  }
}
```

### Revoking a certificate (RevokeCertificate)
<a name="ct-acme-revokecertificate"></a>

The following CloudTrail example shows a data event log entry for the `RevokeCertificate` operation.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:example-session",
    "arn": "arn:aws:sts::123456789012:assumed-role/example-role/example-session",
    "accountId": "123456789012",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/example-role",
        "accountId": "123456789012",
        "userName": "example-role"
      },
      "attributes": {
        "creationDate": "2026-06-10T20:30:37Z",
        "mfaAuthenticated": "false"
      },
      "sourceIdentity": "acm-acme-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    },
    "invokedBy": "acm-acme.amazonaws.com"
  },
  "eventTime": "2026-06-10T20:30:37Z",
  "eventSource": "acm-acme.amazonaws.com",
  "eventName": "RevokeCertificate",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "acm-acme.amazonaws.com",
  "userAgent": "acm-acme.amazonaws.com",
  "requestParameters": {
    "serverUuid": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "certificate": "EXAMPLE"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::CertificateManager::AcmeEndpoint",
      "ARN": "arn:aws:acm:us-east-1:123456789012:acme-endpoint/a1b2c3d4-5678-90ab-cdef-EXAMPLE66666"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": false,
  "recipientAccountId": "123456789012",
  "eventCategory": "Data"
}
```