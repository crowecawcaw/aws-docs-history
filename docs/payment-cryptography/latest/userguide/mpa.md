

# Multi-party approval for AWS Payment Cryptography
<a name="mpa"></a>

AWS Payment Cryptography integrates with [Multi-party approval](https://docs.aws.amazon.com/mpa/latest/userguide/what-is.html) (MPA), a capability from Amazon Web Services Organizations, to help protect critical operations through a distributed approval process. With MPA, you can require that multiple trusted individuals approve specific AWS Payment Cryptography operations before they are carried out.

**Topics**
+ [Overview](#mpa-overview)
+ [Protected operations](#mpa-protected-operations)
+ [Prerequisites](#mpa-prerequisites)
+ [Enabling and disabling MPA](#mpa-enable-disable)
+ [Getting started](#mpa-getting-started)
+ [Example: Import a root certificate with MPA enabled](#mpa-example)
+ [AWS CloudTrail logging for MPA events](#mpa-cloudtrail)
+ [Checking request status and handling failures](#mpa-rejected-requests)

## Overview
<a name="mpa-overview"></a>

Multi-party approval adds an additional layer of security to sensitive AWS Payment Cryptography operations by requiring approval from a group of trusted individuals before the operation can proceed. This helps protect against unauthorized changes if a single set of credentials is compromised and prevents a single individual from unilaterally making a change.

An approval team is a group of approvers within your organization that you designate to approve or deny protected operation requests. The approval process is entirely managed by your organization's approvers. No AWS personnel are involved in approving or denying requests.

When MPA is enabled for a protected operation, the following occurs:

1. A requester initiates the protected operation.

1. MPA creates an approval session and notifies the approval team members.

1. Approval team members review the request and approve or deny it through the MPA portal.

1. Once the required minimum threshold of approvals is reached, the operation proceeds. If the request is denied by the approval team or the allowed session time expires before the approval threshold is met, the operation is not carried out. In both cases, the requester must submit a new request to retry the operation.

**Note**  
When importing a root CA certificate with MPA enabled, the `RequesterComment` parameter is mandatory. This comment is included in the approval notification sent to the approval team, providing context for the request.

## Protected operations
<a name="mpa-protected-operations"></a>

AWS Payment Cryptography supports MPA for the following operation:
+ [`ImportKey`](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html) with `RootCertificatePublicKey` key material — Importing a root public key certificate is a critical operation because root certificates establish the trust anchor for all subsequent key imports and exports using asymmetric key exchange such as TR-34. Requiring multi-party approval for this operation helps ensure that no single individual can unilaterally establish or change the root of trust for your AWS Payment Cryptography keys.

## Prerequisites
<a name="mpa-prerequisites"></a>

Before you can use MPA with AWS Payment Cryptography, you must complete the following prerequisites:
+ Set up MPA in your Amazon Web Services Organizations environment. For instructions, see [What is Multi-party approval?](https://docs.aws.amazon.com/mpa/latest/userguide/what-is.html) in the *Multi-party approval User Guide*.
+ Create at least one approval team with the required approvers.
+ Share the approval team with the AWS account that contains your AWS Payment Cryptography keys using AWS Resource Access Manager.
+ The management account in your organization must be opted in to Multi-party approval.

## Enabling and disabling MPA
<a name="mpa-enable-disable"></a>

After you have set up an approval team, you can enable MPA for AWS Payment Cryptography by associating the team with your account. You can also disable MPA by disassociating the team, although disassociation requires approval from the currently associated approval team.

**Enable MPA**  
Use the `AssociateMpaTeam` API action or the **associate-mpa-team** CLI command to associate an approval team with your AWS Payment Cryptography account. Once associated, the protected operations require approval from the team before they can proceed.

```
aws payment-cryptography associate-mpa-team \
    --team-arn arn:aws:mpa:{{us-east-1}}:{{111122223333}}:team/{{my-approval-team}}
```

**Disable MPA**  
Use the `DisassociateMpaTeam` API action or the **disassociate-mpa-team** CLI command to remove the approval team association. Disassociating a team is itself a protected operation that requires approval from the currently associated approval team.

```
aws payment-cryptography disassociate-mpa-team \
    --team-arn arn:aws:mpa:{{us-east-1}}:{{111122223333}}:team/{{my-approval-team}}
```

**Important**  
Disabling MPA requires approval from the currently associated approval team. This ensures that no single individual can unilaterally remove the multi-party approval protection.

**Note**  
The `--requester-comment` parameter is optional for **associate-mpa-team** and **disassociate-mpa-team**.

## Getting started
<a name="mpa-getting-started"></a>

To get started with MPA for AWS Payment Cryptography, see the [Multi-party approval User Guide](https://docs.aws.amazon.com/mpa/latest/userguide/what-is.html) for detailed setup instructions, including how to create approval teams, configure approval policies, and manage approval sessions.

## Example: Import a root certificate with MPA enabled
<a name="mpa-example"></a>

After MPA is enabled and an approval team is associated with the `ImportKey` operation for `RootCertificatePublicKey`, the import request requires approval before it can proceed.

1. A requester calls `import-key` to import a root public key certificate. To use this command, replace the {{italicized placeholder text}} in the example command with your own information.

   ```
   aws payment-cryptography import-key \
       --key-material='{"RootCertificatePublicKey": {
       "KeyAttributes": {
           "KeyAlgorithm": "RSA_4096",
           "KeyClass": "PUBLIC_KEY",
           "KeyModesOfUse": {"Verify": true},
           "KeyUsage": "TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE"
       },
       "PublicKeyCertificate": "{{LS0tLS1CRUdJTi...}}"}}' \
       --requester-comment "{{Importing new root CA certificate for TR-34 key exchange with partner XYZ}}"
   ```

   The response returns a key with `KeyState` set to `CREATE_IN_PROGRESS`, indicating the request is awaiting approval. The response also includes `MpaStatus` with details about the approval session:

   ```
   {
       "Key": {
           "KeyArn": "arn:aws:payment-cryptography:{{us-east-2}}:{{111122223333}}:key/{{kwapwa6qaifllw2h}}",
           "KeyAttributes": {
               "KeyUsage": "TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE",
               "KeyClass": "PUBLIC_KEY",
               "KeyAlgorithm": "RSA_4096"
           },
           "Enabled": true,
           "KeyState": "CREATE_IN_PROGRESS",
           "KeyOrigin": "EXTERNAL",
           "CreateTimestamp": "2026-04-27T10:15:30.000000+00:00",
           "UsageStartTimestamp": "2026-04-27T10:15:29.926000+00:00",
           "MpaStatus": {
               "MpaSessionArn": "arn:aws:mpa:{{us-east-1}}:{{111122223333}}:session/{{abc123def456}}",
               "Status": "PENDING",
               "InitiationDate": "2026-04-27T10:15:30.000000+00:00"
           }
       }
   }
   ```

1. Because MPA is enabled, the request does not complete immediately. Instead, AWS Payment Cryptography creates an approval session and returns a response indicating that approval is pending.

1. Approval team members receive a notification and review the request through the MPA portal. Once the required number of approvers approve the request, the import operation proceeds and the root certificate is imported.

## AWS CloudTrail logging for MPA events
<a name="mpa-cloudtrail"></a>

When MPA is enabled, AWS Payment Cryptography logs service events to [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) when an approval session completes. These events record the outcome of the approval process, including whether the request was approved or failed. You can use these logs to audit MPA activity and track the status of protected operations.

MPA-related CloudTrail events include the following fields in `serviceEventDetails`:
+ `keyArn` — The ARN of the key affected by the operation.
+ `operation` — The protected operation that was requested.
+ `mpaSessionArn` — The ARN of the MPA approval session.
+ `sessionStatus` — The outcome of the approval session (`APPROVED` or `FAILED`).

**Approved request**  
The following example shows a CloudTrail event for an `ImportKey` request that was approved by the MPA team:

```
{
    "eventVersion": "1.11",
    "eventTime": "2026-04-28T18:49:51Z",
    "eventName": "ImportKey",
    "eventSource": "payment-cryptography.amazonaws.com",
    "eventType": "AwsServiceEvent",
    "eventCategory": "Management",
    "awsRegion": "us-east-1",
    "readOnly": false,
    "managementEvent": true,
    "recipientAccountId": "{{111122223333}}",
    "userIdentity": {
        "accountId": "{{111122223333}}",
        "invokedBy": "payment-cryptography.amazonaws.com"
    },
    "resources": [
        {
            "ARN": "arn:aws:payment-cryptography:{{us-east-2}}:{{111122223333}}:key/{{spa2dclzmsihlj4o}}",
            "accountId": "{{111122223333}}",
            "type": "AWS::PaymentCryptography::Key"
        }
    ],
    "serviceEventDetails": {
        "keyArn": "arn:aws:payment-cryptography:{{us-east-2}}:{{111122223333}}:key/{{spa2dclzmsihlj4o}}",
        "operation": "ImportKey",
        "mpaSessionArn": "arn:aws:mpa:{{us-east-1}}:{{111122223333}}:session/{{my-approval-team/44c76e07-8937-4d7d-bb9a-a646322e2a1e}}",
        "sessionStatus": "APPROVED"
    }
}
```

**Failed request**  
The following example shows a CloudTrail event for an `ImportKey` request that was denied or timed out:

```
{
    "eventVersion": "1.11",
    "eventTime": "2026-04-28T18:50:35Z",
    "eventName": "ImportKey",
    "eventSource": "payment-cryptography.amazonaws.com",
    "eventType": "AwsServiceEvent",
    "eventCategory": "Management",
    "awsRegion": "us-east-1",
    "readOnly": false,
    "managementEvent": true,
    "recipientAccountId": "{{111122223333}}",
    "userIdentity": {
        "accountId": "{{111122223333}}",
        "invokedBy": "payment-cryptography.amazonaws.com"
    },
    "resources": [
        {
            "ARN": "arn:aws:payment-cryptography:{{us-east-2}}:{{111122223333}}:key/{{qj46ku4qimypxdo7}}",
            "accountId": "{{111122223333}}",
            "type": "AWS::PaymentCryptography::Key"
        }
    ],
    "serviceEventDetails": {
        "keyArn": "arn:aws:payment-cryptography:{{us-east-2}}:{{111122223333}}:key/{{qj46ku4qimypxdo7}}",
        "operation": "ImportKey",
        "mpaSessionArn": "arn:aws:mpa:{{us-east-1}}:{{111122223333}}:session/{{my-approval-team/b0ac1994-14e1-47a6-bf1a-0b6fc0b845f2}}",
        "sessionStatus": "FAILED"
    }
}
```

To learn more about AWS CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

## Checking request status and handling failures
<a name="mpa-rejected-requests"></a>

You can check the status of a pending MPA request by calling [`GetKey`](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetKey.html). The response includes the `MpaStatus` field with the current approval session details. To use this command, replace the {{italicized placeholder text}} in the example command with your own information.

```
aws payment-cryptography get-key \
    --key-identifier arn:aws:payment-cryptography:{{us-east-2}}:{{111122223333}}:key/{{kwapwa6qaifllw2h}}
```

While the request is pending approval, the response shows `KeyState` as `CREATE_IN_PROGRESS` and `MpaStatus.Status` as `PENDING`:

```
{
    "Key": {
        "KeyArn": "arn:aws:payment-cryptography:{{us-east-2}}:{{111122223333}}:key/{{kwapwa6qaifllw2h}}",
        "KeyAttributes": {
            "KeyUsage": "TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE",
            "KeyClass": "PUBLIC_KEY",
            "KeyAlgorithm": "RSA_4096"
        },
        "Enabled": true,
        "KeyState": "CREATE_IN_PROGRESS",
        "KeyOrigin": "EXTERNAL",
        "CreateTimestamp": "2026-04-27T10:15:30.000000+00:00",
        "UsageStartTimestamp": "2026-04-27T10:15:29.926000+00:00",
        "MpaStatus": {
            "MpaSessionArn": "arn:aws:mpa:{{us-east-1}}:{{111122223333}}:session/{{abc123def456}}",
            "Status": "PENDING",
            "InitiationDate": "2026-04-27T10:15:30.000000+00:00"
        }
    }
}
```

Once the required number of approvers approve the request, the `KeyState` moves to `CREATE_COMPLETE` and `MpaStatus.Status` moves to `APPROVED`. The key is now ready for use:

```
{
    "Key": {
        "KeyArn": "arn:aws:payment-cryptography:{{us-east-2}}:{{111122223333}}:key/{{kwapwa6qaifllw2h}}",
        "KeyAttributes": {
            "KeyUsage": "TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE",
            "KeyClass": "PUBLIC_KEY",
            "KeyAlgorithm": "RSA_4096"
        },
        "Enabled": true,
        "KeyState": "CREATE_COMPLETE",
        "KeyOrigin": "EXTERNAL",
        "CreateTimestamp": "2026-04-27T10:15:30.000000+00:00",
        "UsageStartTimestamp": "2026-04-27T10:15:29.926000+00:00",
        "MpaStatus": {
            "MpaSessionArn": "arn:aws:mpa:{{us-east-1}}:{{111122223333}}:session/{{abc123def456}}",
            "Status": "APPROVED",
            "InitiationDate": "2026-04-27T10:15:30.000000+00:00"
        }
    }
}
```

If the request is denied by the approval team or the session expires before the approval threshold is met, the `KeyState` changes to `CREATE_FAILED` and `MpaStatus.Status` changes to `FAILED`:

```
{
    "Key": {
        "KeyArn": "arn:aws:payment-cryptography:{{us-east-2}}:{{111122223333}}:key/{{kwapwa6qaifllw2h}}",
        "KeyAttributes": {
            "KeyUsage": "TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE",
            "KeyClass": "PUBLIC_KEY",
            "KeyAlgorithm": "RSA_4096"
        },
        "Enabled": true,
        "KeyState": "CREATE_FAILED",
        "KeyOrigin": "EXTERNAL",
        "CreateTimestamp": "2026-04-27T10:15:30.000000+00:00",
        "UsageStartTimestamp": "2026-04-27T10:15:29.926000+00:00",
        "MpaStatus": {
            "MpaSessionArn": "arn:aws:mpa:{{us-east-1}}:{{111122223333}}:session/{{abc123def456}}",
            "Status": "FAILED",
            "InitiationDate": "2026-04-27T10:15:30.000000+00:00",
            "StatusMessage": "Approval session expired or was denied"
        }
    }
}
```

A key in `CREATE_FAILED` status cannot be used for cryptographic operations. To retry the import, you must submit a new `ImportKey` request, which will create a new approval session.