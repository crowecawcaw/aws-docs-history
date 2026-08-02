# IAM for ACME certificate automation

ACME certificate automation uses IAM roles to authorize certificate issuance
and revocation. This section describes the permissions model for ACME.

## PKI administrator permissions

PKI administrators who create and manage ACME resources need the following
permissions:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "acm:CreateAcmeEndpoint",
                "acm:DescribeAcmeEndpoint",
                "acm:ListAcmeEndpoints",
                "acm:UpdateAcmeEndpoint",
                "acm:DeleteAcmeEndpoint",
                "acm:CreateAcmeExternalAccountBinding",
                "acm:DescribeAcmeExternalAccountBinding",
                "acm:ListAcmeExternalAccountBindings",
                "acm:GetAcmeExternalAccountBindingCredentials",
                "acm:RevokeAcmeExternalAccountBinding",
                "acm:DeleteAcmeExternalAccountBinding",
                "acm:CreateAcmeDomainValidation",
                "acm:DescribeAcmeDomainValidation",
                "acm:ListAcmeDomainValidations",
                "acm:UpdateAcmeDomainValidation",
                "acm:DeleteAcmeDomainValidation"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::`account-id`:role/`AcmeIssuanceRole`",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "acm-acme.amazonaws.com"
                }
            }
        }
    ]
}
```

## EAB role requirements

Each external account binding is associated with an IAM role. ACM uses this role
to authorize certificate issuance and revocation for ACME clients that
authenticate with the binding's credentials.

**Trust policy**

The role must trust the ACME service principal, granting
`sts:AssumeRole`, `sts:TagSession`, and
`sts:SetSourceIdentity`. The following trust policy also uses a condition on
`sts:SourceIdentity` to allow only sessions that ACM establishes for
ACME (source identities that begin with `acm-acme-`):

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

**Permissions policy**

The role needs permissions for the certificate operations you want to allow. The
same ACM actions and condition keys that apply to direct API calls apply here:

```
{
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Action": [
            "acm:RequestCertificate",
            "acm:RevokeCertificate"
        ],
        "Resource": "*"
    }]
}
```

You can restrict issuance using the same condition keys supported by
`acm:RequestCertificate`, such as
`acm:DomainNames` or `acm:KeyAlgorithm`. For more information, see
[Use condition keys with ACM](acm-conditions.md "acm-conditions.md").

**Role session name and source identity**

When ACM assumes the role, it sets a role session name and a source identity that
appear in CloudTrail logs and that you can reference with the `sts:RoleSessionName`
and `sts:SourceIdentity` condition keys:

- **At certificate issuance and revocation** –
  the role session name is `acme-request-`request-id``
 and the source identity is
 `acm-acme-`acme-account-id``.
- **When validating the role at external account binding
  creation** – the role session name is `acme-verification`
  and the source identity is `acm-acme-verification`.

Both source identities begin with `acm-acme-`, so the
`sts:SourceIdentity` condition in the trust policy allows both. ACM also
attaches session tags on the assumed-role session, including
`acme-endpoint-arn`, `acme-account-url`, and
`acme-operation`.

## SCP compatibility

Because the ACME service makes standard ACM API calls using the assumed
role, AWS Organizations Service Control Policies (SCPs) are enforced at certificate
issuance time. If an SCP denies `acm:RequestCertificate` for the account,
ACME certificate issuance also fails. This provides the same governance
controls for ACME-issued certificates as for certificates issued directly
through the ACM API.
