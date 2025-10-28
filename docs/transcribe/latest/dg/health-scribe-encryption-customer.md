# Creating a customer managed key

You can create a symmetric customer managed key by using the AWS Management Console, or the AWS KMS APIs. To
create a symmetric customer managed key, follow the steps for [Creating symmetric customer managed key](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in
the AWS Key Management Service Developer Guide.

Key policies control access to your customer managed key. Every customer managed key must have exactly one key policy,
which contains statements that determine who can use the key and how they can use it. When you create your customer managed
key, you can specify a key policy. For more information, see [Managing access to customer managed
keys](../../../kms/latest/developerguide/control-access-overview.md#managing-access "../../../kms/latest/developerguide/control-access-overview.md#managing-access") in the AWS Key Management Service Developer Guide.

## AWS KMS key policies for AWS HealthScribe

If you are using a key in the same account as the IAM role you specify as the `DataAccessRole` in your [StartMedicalScribeJob](../APIReference/API_StartMedicalScribeJob.md "../APIReference/API_StartMedicalScribeJob.md") or
`ResourceAccessRole` in your [StartMedicalScribeStream](../APIReference/API_streaming_StartMedicalScribeStream.md "../APIReference/API_streaming_StartMedicalScribeStream.md")
request, you don't need to update the Key Policy. To use your customer managed key in a different account as your DataAccessRole (for transcription jobs)
or ResourceAccessRole (for streaming), you must trust the respective role in the Key Policy for the following actions:

- [`kms:Encrypt`](../../../kms/latest/APIReference/API_Encrypt.md "../../../kms/latest/APIReference/API_Encrypt.md")
  — Allows encryption using the customer managed key
- [`kms:Decrypt`](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md")
  — Allows decryption using the customer managed key
- [`kms:DescribeKey`](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md")
  — Provides the customer managed key details to allow AWS HealthScribe to validate the key

The following is an example key policy you can use to grant your ResourceAccessRole cross account permissions
to use your customer managed key for AWS HealthScribe streaming. To use this policy for
transcription jobs, update the `Principal` to use the DataAccessRole ARN, and remove or modify the encryption context.

## IAM policy permissions for access roles

The IAM policy attached to your DataAccessRole or ResourceAccessRole must grant permissions to perform the necessary AWS KMS actions,
regardless of whether the customer-managed key and role are in the same or different accounts.
Also, the role's trust policy must grant AWS HealthScribe permission to assume the role.

The following IAM policy example shows how to grant a ResourceAccessRole permissions for AWS HealthScribe streaming.
To use this policy for transcription jobs, replace `transcribe.streaming.amazonaws.com` with
`transcribe.amazonaws.com` and remove or modify the encryption context.

The following is trust policy example for the ResourceAccessRole. For DataAccessRole, replace
`transcribe.streaming.amazonaws.com` with `transcribe.amazonaws.com`.

For more information about [specifying permissions in a
policy](../../../kms/latest/developerguide/control-access-overview.md#overview-policy-elements "../../../kms/latest/developerguide/control-access-overview.md#overview-policy-elements") or [troubleshooting key access](../../../kms/latest/developerguide/policy-evaluation.md#example-no-iam "../../../kms/latest/developerguide/policy-evaluation.md#example-no-iam"), see the AWS Key Management Service Developer Guide.
