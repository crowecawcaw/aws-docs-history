

# Auditing cross-partition identity federation
<a name="id_roles_providers_outbound_cross_partition_auditing"></a>

The `GetWebIdentityToken` CloudTrail event captures the token request in the source account. The `AssumeRoleWithWebIdentity` CloudTrail event captures the role assumption request in the destination account. Match `webIdentityTokenId` values to connect the source and destination events, and use `sourcePrincipalArn` and `sourceRegion` to identify who requested the token and where it was issued.

For cross-partition identity federation, the events include the following information:
+ `webIdentityTokenId` appears under `responseElements` in the source event and under `requestParameters` in the destination event.
+ `additionalEventData.crossPartitionData.sourcePrincipalArn` in the destination event identifies the ARN of the source IAM principal that requested the token.
+ `additionalEventData.crossPartitionData.sourceRegion` in the destination event identifies the source AWS Region where AWS STS issued the token.

Use these fields together to trace a destination role assumption back to the source token request. Matching `webIdentityTokenId` values connect the `AssumeRoleWithWebIdentity` event to the corresponding `GetWebIdentityToken` event. The `sourcePrincipalArn` and `sourceRegion` fields identify who requested the token and where it was issued.

**Example: Token request in the source account**

The following example shows a `GetWebIdentityToken` event in the source account.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
      "type": "AssumedRole",
      "principalId": "AROA123456789EXAMPLE:workload-session",
      "arn": "arn:aws:sts::123456789012:assumed-role/SourceWorkloadRole/workload-session",
      "accountId": "123456789012",
      "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
      "sessionContext": {
          "sessionIssuer": {
              "type": "Role",
              "principalId": "AROA123456789EXAMPLE",
              "arn": "arn:aws:iam::123456789012:role/SourceWorkloadRole",
              "accountId": "123456789012",
              "userName": "SourceWorkloadRole"
          },
          "attributes": {
              "creationDate": "2026-10-02T01:03:26Z",
              "mfaAuthenticated": "false"
          }
      }
  },
  "eventTime": "2026-10-02T01:05:02Z",
  "eventSource": "sts.amazonaws.com",
  "eventName": "GetWebIdentityToken",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.101",
  "userAgent": "aws-cli/2.34.4 md/command#sts.get-web-identity-token",
  "requestParameters": {
      "audience": [
          "your-audience"
      ],
      "durationSeconds": 300,
      "signingAlgorithm": "ES384"
  },
  "responseElements": {
      "webIdentityTokenId": "6e70a1d6-7cbd-44f5-9b94-d0540EXAMPLE",
      "expiration": "2026-10-02T01:10:02Z"
  },
  "additionalEventData": {
      "RequestDetails": {
          "endpointType": "regional",
          "awsServingRegion": "us-east-1"
      }
  },
  "requestID": "aEXAMPLE-384d-46d2-b82e-a07f8EXAMPLE",
  "eventID": "aEXAMPLE-cd24-4544-b61b-fc668EXAMPLE",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management",
  "tlsDetails": {
      "tlsVersion": "TLSv1.3",
      "cipherSuite": "TLS_AES_128_GCM_SHA256",
      "clientProvidedHostHeader": "sts.us-east-1.amazonaws.com"
  }
}
```

**Example: Role assumption in the destination account**

The following example shows the corresponding `AssumeRoleWithWebIdentity` event. Its `requestParameters.webIdentityTokenId` value matches the token identifier in the source event.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
      "type": "WebIdentityUser",
      "principalId": "arn:aws-cn:iam::111122223333:oidc-provider/a1d2b0fd-1177-4468-9351-2fEXAMPLE723.tokens.sts.global.api.aws:your-audience:arn:aws:iam::123456789012:role/SourceWorkloadRole",
      "userName": "arn:aws:iam::123456789012:role/SourceWorkloadRole",
      "identityProvider": "arn:aws-cn:iam::111122223333:oidc-provider/a1d2b0fd-1177-4468-9351-2fEXAMPLE723.tokens.sts.global.api.aws"
  },
  "eventTime": "2026-10-02T01:05:06Z",
  "eventSource": "sts.amazonaws.com",
  "eventName": "AssumeRoleWithWebIdentity",
  "awsRegion": "cn-north-1",
  "sourceIPAddress": "192.0.2.101",
  "userAgent": "aws-cli/2.34.4 md/command#sts.assume-role-with-web-identity",
  "requestParameters": {
      "roleArn": "arn:aws-cn:iam::111122223333:role/DestinationWorkloadRole",
      "roleSessionName": "cross-partition-session",
      "webIdentityTokenId": "6e70a1d6-7cbd-44f5-9b94-d0540EXAMPLE"
  },
  "responseElements": {
      "credentials": {
          "accessKeyId": "ASIAI44QH8DHBEXAMPLE",
          "sessionToken": "{{<encoded session token blob>}}",
          "expiration": "2026-10-02T02:05:06Z"
      },
      "subjectFromWebIdentityToken": "arn:aws:iam::123456789012:role/SourceWorkloadRole",
      "assumedRoleUser": {
          "assumedRoleId": "AROA987654321EXAMPLE:cross-partition-session",
          "arn": "arn:aws-cn:sts::111122223333:assumed-role/DestinationWorkloadRole/cross-partition-session"
      },
      "provider": "arn:aws-cn:iam::111122223333:oidc-provider/a1d2b0fd-1177-4468-9351-2fEXAMPLE723.tokens.sts.global.api.aws",
      "audience": "your-audience",
      "packedPolicySize": 31,
      "sessionTokenSize": 1296,
      "sessionTokenUtilization": 31
  },
  "additionalEventData": {
      "RequestDetails": {
          "endpointType": "regional",
          "awsServingRegion": "cn-north-1"
      },
      "crossPartitionData": {
          "sourcePrincipalArn": "arn:aws:iam::123456789012:role/SourceWorkloadRole",
          "sourceRegion": "us-east-1"
      },
      "identityProviderConnectionVerificationMethod": "IAMTrustStore"
  },
  "requestID": "aEXAMPLE-bc02-4669-a0ea-dd53fEXAMPLE",
  "eventID": "aEXAMPLE-99a1-4df4-b279-5c647EXAMPLE",
  "readOnly": true,
  "resources": [
      {
          "accountId": "111122223333",
          "type": "AWS::IAM::Role",
          "ARN": "arn:aws-cn:iam::111122223333:role/DestinationWorkloadRole"
      }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
      "tlsVersion": "TLSv1.3",
      "cipherSuite": "TLS_AES_128_GCM_SHA256",
      "clientProvidedHostHeader": "sts.cn-north-1.amazonaws.com.cn"
  }
}
```