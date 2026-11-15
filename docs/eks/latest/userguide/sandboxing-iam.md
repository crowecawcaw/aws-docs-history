

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# IAM permissions for Nitro Sandboxes
<a name="sandboxing-iam"></a>

The following IAM permissions are required for specific Nitro Sandboxes features.

## Encrypted container images
<a name="sandboxing-iam-encrypted-images"></a>

The pod’s IAM role (through EKS Pod Identity) must have `kms:Decrypt` permission on the KMS key used to encrypt the image layers. The Nitro Sandbox does not use IRSA credentials for this call:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "kms:Decrypt",
      "Resource": "arn:aws:kms:region-code:111122223333:key/mrk-example"
    }
  ]
}
```

## Image signature verification
<a name="sandboxing-iam-signature"></a>

For image signature verification, the pod’s IAM role (through EKS Pod Identity) must have the following AWS Signer permissions:


| Action | Purpose | 
| --- | --- | 
|  `signer:GetRevocationStatus`  | Check whether an individual signing job or certificate has been revoked. | 
|  `signer:GetSigningProfile`  | Check whether the signing profile has been revoked with `RevokeSigningProfile`. Signatures produced by a revoked profile are rejected. Canceled profiles are treated as trusted because `CancelSigningProfile` is administrative retirement, not trust withdrawal. | 

**Both Signer actions are required**  
Both actions are required. If either call fails, or returns a permission error, signature verification fails closed and the agent denies container creation. Signature verification also requires network access from the Nitro Sandbox to the AWS Signer endpoint. Pods with `sandbox.amazonaws.com/network-isolated` set to `"true"` cannot use image signature verification.

## KMS attestation conditions
<a name="sandboxing-iam-kms-attestation"></a>

To release KMS-protected secrets only to attested sandboxes, add `kms:RecipientAttestation:PCR<PCR_ID>` conditions to your KMS key policy. Gate on PCR17 (the Cedar policy hash) set to the predicted value from `eks-nitro-sandbox-genpolicy` (included in the signed runtime binaries; see [Download and verify the runtime binaries](sandboxing-download-binaries.md)), and also add a `kms:RecipientAttestation:PCR8:ServiceName` condition set to `eks.amazonaws.com` so that only attestations from the EKS Nitro Sandbox service are accepted. Gating on PCR17 alone is not sufficient:

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/my-workload-role"
  },
  "Action": "kms:Decrypt",
  "Resource": "*",
  "Condition": {
    "StringEqualsIgnoreCase": {
      "kms:RecipientAttestation:PCR17": "<PCR17-value-from-genpolicy>",
      "kms:RecipientAttestation:PCR8:ServiceName": "eks.amazonaws.com"
    }
  }
}
```

The `eks-nitro-sandbox-genpolicy` command prints the predicted PCR17 value when it generates a policy. Use this value to configure your KMS key policy before deploying, without needing a running sandbox.

For more information, see [AWS KMS condition keys for AWS Nitro Enclaves](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclave.html) and the Nitro Sandbox security model in [Security model and parent instance trust assumptions](sandboxing-security-model.md).