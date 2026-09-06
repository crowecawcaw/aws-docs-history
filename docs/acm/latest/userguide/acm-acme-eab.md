

# External account bindings
<a name="acm-acme-eab"></a>

External account bindings (EABs) are credentials that authorize ACME clients to register accounts with an ACME endpoint. An ACME client cannot request certificates from an endpoint without first registering an account, and registration requires valid EAB credentials. When a PKI administrator creates an EAB, they associate it with an IAM role that controls what certificate operations the ACME client can perform. The administrator then distributes the EAB credentials out-of-band to the teams or systems that need certificates.

Each EAB produces a key identifier (key ID) and a MAC key. The ACME client uses these credentials during account registration to prove authorization. After the ACME account is created, the account operates independently of the EAB. Revoking or deleting an EAB does not affect existing ACME accounts created with it.

## IAM role requirements
<a name="acm-acme-eab-iam-role"></a>

Each EAB is associated with an IAM role. This role determines what the ACME client can do when issuing or revoking certificates. The role must meet the following requirements:

Trust policy  
The role must allow the ACME service principal (`acm-acme.amazonaws.com`) to assume it. The trust policy must grant `sts:AssumeRole`, `sts:TagSession`, and `sts:SetSourceIdentity`. The condition on `sts:SourceIdentity` allows only the sessions that ACM establishes for ACME:  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "acm-acme.amazonaws.com"
            },
            "Action": [
                "sts:AssumeRole",
                "sts:TagSession",
                "sts:SetSourceIdentity"
            ],
            "Condition": {
                "StringLikeIfExists": {
                    "sts:SourceIdentity": "acm-acme-*"
                }
            }
        }
    ]
}
```
For the role session name, source identity, and session tag values that ACM sets, see [IAM for ACME certificate automation](security-iam-acme.md).

Permissions  
The role needs `acm:RequestCertificate` (for issuing) or `acm:RevokeCertificate` (for revoking), or both. These are the same permissions and condition keys used with standard ACM APIs. For more information, see [Use condition keys with ACM](acm-conditions.md).

PassRole  
The administrator creating the EAB needs `iam:PassRole` permission for the role.

For complete IAM policy examples, see [IAM for ACME certificate automation](security-iam-acme.md).

## How the EAB role is used
<a name="acm-acme-eab-role-assumption"></a>

When an ACME client issues or revokes a certificate, ACM uses the IAM role associated with the client's EAB to authorize the operation. Because issuance and revocation run under this role, ACME behaves like the standard ACM API:
+ The same IAM policies and condition keys you use for direct ACM API calls apply to ACME issuance and revocation.
+ AWS Organizations Service Control Policies (SCPs) are enforced at issuance time.
+ Issuance and revocation operations are recorded in CloudTrail.
+ ACM sets a role session name and source identity (and session tags) when it assumes the role, which you can reference with the `sts:RoleSessionName` and `sts:SourceIdentity` condition keys in the role's trust policy. For the values ACM uses, see [IAM for ACME certificate automation](security-iam-acme.md).

## Credential retrieval
<a name="acm-acme-eab-credentials"></a>

After creating an EAB, retrieve its credentials by using `GetAcmeExternalAccountBindingCredentials`. This returns:
+ **Key ID:** A unique identifier for the EAB (used as the `kid` in ACME EAB).
+ **MAC Key:** A secret key used to create the HMAC signature during account registration (used as the `hmacKey`).

**Important**  
Treat the MAC key as a secret. Distribute it only to the ACME clients that you authorize to use the endpoint.

## Optional expiration
<a name="acm-acme-eab-expiration"></a>

You can configure an expiration for the EAB credentials:
+ **Value:** A positive integer.
+ **Type:** `MINUTES`, `HOURS`, or `DAYS`.

If the credentials are not used before expiration, they become invalid. If no expiration is set, credentials remain valid until the EAB is revoked or deleted.

## EAB and ACME account lifecycle
<a name="acm-acme-eab-lifecycle"></a>

Once an ACME client registers an account using EAB credentials, the ACME account and EAB have independent lifecycles:
+ Revoking an EAB does not affect existing ACME accounts created with it.
+ Deleting an EAB does not deactivate accounts.
+ An ACME account can continue issuing certificates after its originating EAB is revoked.

**Note**  
To stop an ACME account from issuing more certificates, manage the account directly. You can revoke the account with the `RevokeAcmeAccount` API, or the account holder can deactivate it through the ACME protocol.

## Creating an external account binding
<a name="acm-acme-eab-create"></a>

You can create an EAB by using the ACM console or the AWS CLI.

### To create an EAB (console)
<a name="acm-acme-eab-create-console"></a>

1. Sign in to the AWS Management Console and open the ACM console.

1. In the left navigation pane, under **ACME**, choose **Endpoints**.

1. Select the endpoint.

1. Choose the **External account bindings** tab.

1. Choose **Create external account binding**.

1. For **IAM role**, enter or select the ARN of the role. The role must have the correct trust policy.

1. (Optional) Configure an expiration for the credentials.

1. (Optional) Under **Tags**, add one or more tags to the external account binding.

1. Choose **Create**.

1. Copy the Key ID and MAC key.

**Important**  
Treat the MAC key as a secret. You can retrieve the key identifier and MAC key again at any time by calling `GetAcmeExternalAccountBindingCredentials`.

### To create an EAB (AWS CLI)
<a name="acm-acme-eab-create-cli"></a>

Run the following command to create an EAB:

```
aws acm create-acme-external-account-binding \
    --acme-endpoint-arn arn:aws:acm:{{region}}:{{111122223333}}:acme-endpoint/{{00000000-0000-0000-0000-000000000000}} \
    --role-arn arn:aws:iam::{{111122223333}}:role/{{AcmeIssuanceRole}} \
    --expiration '{"Value": 7, "Type": "DAYS"}'
```

Then retrieve the credentials:

```
aws acm get-acme-external-account-binding-credentials \
    --acme-external-account-binding-arn arn:aws:acm:{{region}}:{{111122223333}}:acme-endpoint/{{00000000-0000-0000-0000-000000000000}}/acme-external-account-binding/{{22222222-2222-2222-2222-222222222222}}
```

The response contains the key identifier and MAC key that you provide to the ACME client. You can retrieve these credentials again at any time by calling `GetAcmeExternalAccountBindingCredentials`.

```
{
    "KeyId": "{{e06b7974-a684-4cc2-b4b1-1fd87ac81baa}}",
    "MacKey": "{{txvweHF1-COvXAKNlGk-58SX6ZVzEaaXaBPrwNAKCTo}}"
}
```

## Managing external account bindings
<a name="acm-acme-eab-manage"></a>

You can perform the following management operations on EABs:

Describe  
View EAB details including role ARN, expiration, creation time, and last used.

List  
View all EABs for an endpoint.

Revoke  
Invalidate the EAB credentials. This does not affect existing ACME accounts created with the EAB. To manage those accounts, revoke them with the `RevokeAcmeAccount` API, or have the account holder deactivate them through the ACME protocol.

Delete  
Remove the EAB resource entirely. Any ACME accounts already registered with the EAB continue to exist; deleting the EAB only prevents new ACME accounts from being registered with it.