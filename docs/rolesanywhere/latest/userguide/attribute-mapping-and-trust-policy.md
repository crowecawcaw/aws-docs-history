# Attribute mapping and trust policy

It is recommended to have condition statements in the Assume Role Policy Document to
restrict authorization based on attributes that are extracted from an end-entity X.509 certificate.
For more information about the role trust policy, see [Trust policy](trust-model.md#trust-policy "trust-model.md#trust-policy").

The attribute mapping field of a profile controls which attributes from an
authenticating X.509 certificate will be mapped for principal tags. Therefore, while adding
condition statements to an Assume Role Policy Document, be cautious that the specifiers used
in mapping rules for authorization need to be mapped accordingly.

The following example shows trust policies that add a condition based on the `Issuer
 Common Name (CN)` of the certificate.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "rolesanywhere.amazonaws.com"
 },
 "Action": [
 "sts:AssumeRole",
 "sts:TagSession",
 "sts:SetSourceIdentity"
 ],
 "Condition": {
 "StringEquals": {
 "aws:PrincipalTag/x509Issuer/CN": "Bob"
 },
 "ArnEquals": {
 "aws:SourceArn": [
 "arn:aws:rolesanywhere:`us-east-1`:`123456789012`:trust-anchor/`TA_ID`"
 ]
 }
 }
 }
 ]
}`

```

If a profile is used with an Attribute Mapping field that lacks `specifier: CN`
or `specifier: *` in the mappingRules for `x509Issuer`, the first
condition in the Assume Role Policy Document will evaluate as `false` because
there will be no value mapped `aws:PrincipalTag/x509Issuer/CN`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "rolesanywhere.amazonaws.com"
 },
 "Action": [
 "sts:AssumeRole",
 "sts:TagSession",
 "sts:SetSourceIdentity"
 ],
 "Condition": {
 "StringNotEquals": {
 "aws:PrincipalTag/x509Issuer/CN": "Bob"
 },
 "ArnEquals": {
 "aws:SourceArn": [
 "arn:aws:rolesanywhere:`us-east-1`:`123456789012`:trust-anchor/`TA_ID`"
 ]
 }
 }
 }
 ]
}`

```

Likewise, if the condition is `StringNotEquals`, the condition
will evaluate to `true` using the same profile. This happens because the
condition is disregarded when the principal tag is dropped due to attribute mapping APIs.

Having the Attribute Mapping field provided below in a profile, the `StringEquals`
condition for `x509Issuer/CN` will assess to `false`, or the
`StringNotEquals` condition will assess to `true`.

```
"attributeMappings": [
  {
    "mappingRules": [
        {
            "specifier": "O"
        }
    ],
    "certificateField": "x509Issuer"
  },
  {
    "mappingRules": [
        {
            "specifier": "DNS"
        },
        {
            "specifier": "URI"
        },
        {
            "specifier": "Name/*"
        }
    ],
    "certificateField": "x509SAN"
  },
  {
    "mappingRules": [
        {
            "specifier": "*"
        }
    ],
    "certificateField": "x509Subject"
  }
]
```
