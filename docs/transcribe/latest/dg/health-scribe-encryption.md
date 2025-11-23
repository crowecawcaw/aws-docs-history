# Data Encryption at rest for AWS HealthScribe

By default, AWS HealthScribe provides encryption at rest to protect sensitive customer data using
AWS HealthScribe managed AWS Key Management Service (AWS KMS) keys. Encryption of data at rest by default helps reduce the operational overhead and complexity involved in protecting
sensitive data. Also, it enables you to build secure applications that meet strict encryption compliance and
regulatory requirements. When you create an
AWS HealthScribe transcription job or start a stream, you can specify a customer managed key. This adds a second layer of
encryption.

- **AWS HealthScribe managed AWS KMS keys** — AWS HealthScribe uses AWS HealthScribe managed AWS Key Management Service (AWS KMS)
  keys by default to automatically encrypt intermediate files. You can't disable this layer of encryption or
  choose an alternate encryption type. You can't view, manage, or use the keys, or audit their use. However, you don't have to take any action or change any programs to
  protect the keys that encrypt your data.
- **Customer managed keys** — AWS HealthScribe supports the use of a symmetric customer managed
  key that you create, own, and manage to add a second layer of encryption over the existing AWS owned encryption. Because
  you have full control of this layer of encryption, you can perform such tasks as:

      + Establishing and maintaining key policies
      + Establishing and maintaining IAM policies and grants
      + Enabling and disabling key policies
      + Rotating key cryptographic material
      + Adding tags
      + Creating key aliases
      + Scheduling keys for deletion

  For more information, see [customer
  managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the AWS Key Management Service Developer Guide.

###### Note

AWS HealthScribe automatically enables encryption at rest using AWS-owned keys to protect
personally identifiable data at no charge. However, AWS KMS charges apply for using a customer managed key. For
more information about pricing, see [AWS Key Management Service pricing](https://aws.amazon.com//kms/pricing/ "https://aws.amazon.com//kms/pricing/").

For more information on AWS KMS, see [What is AWS Key Management Service](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").

###### Topics

- [Creating a customer managed key](health-scribe-encryption-customer.md "health-scribe-encryption-customer.md")
- [Specifying a customer managed key for AWS
  HealthScribe](#health-scribe-encryption-managed "#health-scribe-encryption-managed")
- [AWS KMS encryption context](#health-scribe-encryption-context "#health-scribe-encryption-context")
- [Monitoring your encryption keys for AWS HealthScribe](#hscribe-monitoring-keys "#hscribe-monitoring-keys")

## Specifying a customer managed key for AWS

HealthScribe

You can specify a customer managed key as a second layer encryption for transcription jobs or streaming.

- For transcription jobs, you specify your key in the [OutputEncryptionKMSKeyId](../APIReference/API_StartMedicalScribeJob.md#transcribe-StartMedicalScribeJob-request-OutputEncryptionKMSKeyId "../APIReference/API_StartMedicalScribeJob.md#transcribe-StartMedicalScribeJob-request-OutputEncryptionKMSKeyId") of your [StartMedicalScribeJob](../APIReference/API_StartMedicalScribeJob.md "../APIReference/API_StartMedicalScribeJob.md") API operation.
- For streaming, you specify the key in the [MedicalScribeEncryptionSettings](../APIReference/API_streaming_MedicalScribeEncryptionSettings.md "../APIReference/API_streaming_MedicalScribeEncryptionSettings.md") in your [MedicalScribeConfigurationEvent](../APIReference/API_streaming_MedicalScribeConfigurationEvent.md "../APIReference/API_streaming_MedicalScribeConfigurationEvent.md").

## AWS KMS encryption context

AWS KMS encryption context is a map of plain text, non-secret key:value pairs. This map represents additional
authenticated data, known as encryption context pairs, which provide an added layer of security for your data. AWS HealthScribe requires a symmetric encryption key to encrypt AWS HealthScribe output into a
customer-specified Amazon S3 bucket. To learn more, see [Asymmetric keys in AWS KMS](../../../kms/latest/developerguide/symmetric-asymmetric.md "../../../kms/latest/developerguide/symmetric-asymmetric.md").

When creating your encryption context pairs, _do not_ include sensitive information. Encryption
context is not secret — it is visible in plain text within your CloudTrail logs (so you can use it to identify
and categorize your cryptographic operations). Your encryption context pair can include special characters, such as
underscores (`_`), dashes (`-`), slashes (`/`, `\`) and colons (`:`).

###### Tip

It can be useful to relate the values in your encryption context pair to the data being encrypted. Although not
required, we recommend you use non-sensitive metadata related to your encrypted content, such as file names, header
values, or unencrypted database fields.

To use output encryption with the API, set the [KMSEncryptionContext](../APIReference/API_StartMedicalScribeJob.md#transcribe-StartMedicalScribeJob-request-KMSEncryptionContext "../APIReference/API_StartMedicalScribeJob.md#transcribe-StartMedicalScribeJob-request-KMSEncryptionContext") parameter in the [StartMedicalScribeJob](../APIReference/API_StartMedicalScribeJob.md "../APIReference/API_StartMedicalScribeJob.md") operation. In order
to provide encryption context for the output encryption operation, the [OutputEncryptionKMSKeyId](../APIReference/API_StartMedicalScribeJob.md#transcribe-StartMedicalScribeJob-request-OutputEncryptionKMSKeyId "../APIReference/API_StartMedicalScribeJob.md#transcribe-StartMedicalScribeJob-request-OutputEncryptionKMSKeyId") parameter must reference a symmetric AWS KMS key ID.

For streaming, you specify the key value pairs for the `KmsEncryptionContext` in the [MedicalScribeEncryptionSettings](../APIReference/API_streaming_MedicalScribeEncryptionSettings.md "../APIReference/API_streaming_MedicalScribeEncryptionSettings.md") in your [MedicalScribeConfigurationEvent](../APIReference/API_streaming_MedicalScribeConfigurationEvent.md "../APIReference/API_streaming_MedicalScribeConfigurationEvent.md").

You can use [AWS KMS condition keys](../../../kms/latest/developerguide/policy-conditions.md#conditions-kms "../../../kms/latest/developerguide/policy-conditions.md#conditions-kms") with IAM policies to control access to a symmetric
encryption AWS KMS key based on the encryption context that was used in the request for a [cryptographic
operation](../../../kms/latest/developerguide/concepts.md#cryptographic-operations "../../../kms/latest/developerguide/concepts.md#cryptographic-operations"). For an example encryption context policy, see [AWS KMS encryption
context policy](security_iam_id-based-policy-examples.md#kms-context-policy "security_iam_id-based-policy-examples.md#kms-context-policy").

Using encryption context is optional, but recommended. For more information, see [Encryption context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context").

### AWS HealthScribe encryption context

AWS HealthScribe uses the same encryption context in all AWS Key Management Service cryptographic operations. The encryption context is a map of String to String that can be customized to anything you want.

```
"encryptionContext": {
   "ECKey": "ECValue"
   ...
}
```

For AWS HealthScribe streams, the following is the default service generated encryption context. It applies this context on top of any encryption context that you provide.

```
"encryptionContext": {
  "aws:<region>:transcribe:medical-scribe:session-id": "1234abcd-12ab-34cd-56ef-123456SAMPLE"
}
```

For AWS HealthScribe transcription jobs, the following is the default service generated encryption context. It applies this context on top of any encryption context that you provide.

```
"encryptionContext": {
  "aws:<region>:transcribe:medical-scribe:job-name": "<job-name>",
  "aws:<region>:transcribe:medical-scribe:start-time-epoch-ms": "<job-start-time>"
}
```

If you don’t provide any encryption context, only service generated encryption context will be used for all AWS KMS cryptographic operations.

**Monitoring AWS HealthScribe with encryption context**

When you use a symmetric customer managed key to encrypt your data at rest in AWS HealthScribe, you can also use the encryption context in audit records and logs to identify
how the customer managed key is being used. The encryption context also appears in logs generated by AWS CloudTrail or CloudWatch Logs.

**Using encryption context to control access to your customer managed key**

You can use the encryption context in key policies and IAM policies as conditions to control access to your symmetric customer managed key.

The following are example key policy statements to grant access to a customer managed key for a specific encryption context.
The condition in this policy statement requires that the KMS key usages have an encryption context constraint that specifies the encryption context.

## Monitoring your encryption keys for AWS HealthScribe

When you use an AWS Key Management Service customer managed key with AWS HealthScribe, you can use AWS CloudTrail or CloudWatch logs to track requests that AWS HealthScribe sends to AWS KMS.

The following examples are CloudTrail Encrypt and Decrypt events you can use that allow you to monitor how AWS HealthScribe uses of your customer managed key.

**Encrypt**

```
{
   "eventVersion":"1.09",
   "userIdentity":{
      "type":"AssumedRole",
      "principalId":"AROAIGDTESTANDEXAMPLE:Sampleuser01",
      "arn":"arn:aws:sts::`123456789012`:assumed-role/Admin/Sampleuser01",
      "accountId":"`123456789012`",
      "accessKeyId":"AKIAIOSFODNN7EXAMPLE3",
      "sessionContext":{
         "sessionIssuer":{
            "type":"Role",
            "principalId":"AROAIGDTESTANDEXAMPLE:Sampleuser01",
            "arn":"arn:aws:sts::`123456789012`:assumed-role/Admin/Sampleuser01",
            "accountId":"`123456789012`",
            "userName":"Admin"
         },
         "attributes":{
            "creationDate":"2024-08-16T01:10:05Z",
            "mfaAuthenticated":"false"
         }
      },
      "invokedBy":"transcribe.streaming.amazonaws.com"
   },
   "eventTime":"2024-08-16T01:10:05Z",
   "eventSource":"kms.amazonaws.com",
   "eventName":"Encrypt",
   "awsRegion":"us-east-1",
   "sourceIPAddress":"transcribe.streaming.amazonaws.com",
   "userAgent":"transcribe.streaming.amazonaws.com",
   "requestParameters":{
      "encryptionContext":{
         "aws:us-east-1:transcribe:medical-scribe:session-id":"1234abcd-12ab-34cd-56ef-123456SAMPLE"
      },
      "encryptionAlgorithm":"SYMMETRIC_DEFAULT",
      "keyId":"`1234abcd-12ab-34cd-56ef-1234567890ab`"
   },
   "responseElements":null,
   "requestID":"cbe0ac33-8cca-49e5-9bb5-dc2b8dfcb389",
   "eventID":"1b9fedde-aa96-48cc-9dd9-a2cce2964b3c",
   "readOnly":true,
   "resources":[
      {
         "accountId":"`123456789012`",
         "type":"AWS::KMS::Key",
         "ARN":"arn:aws:kms:us-west-2:`123456789012`:key/`1234abcd-12ab-34cd-56ef-123456SAMPLE`"
      }
   ],
   "eventType":"AwsApiCall",
   "managementEvent":true,
   "recipientAccountId":"`123456789012`",
   "eventCategory":"Management"
}


```

**Decrypt**

```
{
   "eventVersion":"1.09",
   "userIdentity":{
      "type":"AssumedRole",
      "principalId":"AROAIGDTESTANDEXAMPLE:Sampleuser01",
      "arn":"arn:aws:sts::`123456789012`:assumed-role/Admin/Sampleuser01",
      "accountId":"`123456789012`",
      "accessKeyId":"AKIAIOSFODNN7EXAMPLE3",
      "sessionContext":{
         "sessionIssuer":{
            "type":"Role",
            "principalId":"AROAIGDTESTANDEXAMPLE:Sampleuser01",
            "arn":"arn:aws:sts::`123456789012`:assumed-role/Admin/Sampleuser01",
            "accountId":"`123456789012`",
            "userName":"Admin"
         },
         "attributes":{
            "creationDate":"2024-08-16T20:47:04Z",
            "mfaAuthenticated":"false"
         }
      },
      "invokedBy":"transcribe.streaming.amazonaws.com"
   },
   "eventTime":"2024-08-16T20:47:04Z",
   "eventSource":"kms.amazonaws.com",
   "eventName":"Decrypt",
   "awsRegion":"us-east-1",
   "sourceIPAddress":"transcribe.streaming.amazonaws.com",
   "userAgent":"transcribe.streaming.amazonaws.com",
   "requestParameters":{
      "keyId":"mrk-de27f019178f4fbf86512ab03ba860be",
      "encryptionAlgorithm":"SYMMETRIC_DEFAULT",
      "encryptionContext":{
         "aws:us-east-1:transcribe:medical-scribe:session-id":"1234abcd-12ab-34cd-56ef-123456SAMPLE"
      }
   },
   "responseElements":null,
   "requestID":"8b7fb865-48be-4e03-ac3d-e7bee3ba30a1",
   "eventID":"68b7a263-d410-4701-9e2b-20c196628966",
   "readOnly":true,
   "resources":[
      {
         "accountId":"`123456789012`",
         "type":"AWS::KMS::Key",
         "ARN":"arn:aws:kms:us-west-2:`123456789012`:key/`1234abcd-12ab-34cd-56ef-123456SAMPLE`"
      }
   ],
   "eventType":"AwsApiCall",
   "managementEvent":true,
   "recipientAccountId":"`123456789012`",
   "eventCategory":"Management"
}
```
