

# Trusted identity propagation

IAM Roles Anywhere supports trusted identity propagation (TIP), which adds the identity from a certificate to your sessions. AWS Security Token Service (AWS STS) puts the identity in `aws:OriginIdentity` condition keys. It takes the identity from an assertion that IAM Roles Anywhere signs after it checks the certificate. The caller can't set these keys. Session tags are different: any principal that can tag a role's sessions can set them. You can use the keys in role trust policies, identity-based policies, resource-based policies, and organization policies. For how TIP context carries across role sessions and AWS services, and how AWS CloudTrail records it, see [Trusted identity propagation with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_tip.html) in the *IAM User Guide*.

When you create a profile on the console, trusted identity propagation is on by default. To create the profile without it, turn off **Enable trusted identity propagation** in the **Trusted identity propagation** section. With the API or the AWS Command Line Interface (AWS CLI), a profile uses trusted identity propagation only if the request turns it on. Existing profiles keep their current setting.

**Important**  
When you enable trusted identity propagation (TIP) for IAM Roles Anywhere, you select one X.509 certificate attribute in the profile to use as the end-user or workload identifier. AWS maps the selected certificate attribute to an identity context key carried in the temporary AWS credentials issued for the session.  
You can use this identity information to manage access to AWS resources through IAM policies and data grants. AWS uses it to authorize requests, record activity in AWS CloudTrail and service logs, calculate fees, and enable cost allocation. The identity information travels with requests to the AWS accounts and Regions that the session accesses. AWS may also process it in default Regions required to fulfill a request.  
This context key does not constitute your content. AWS recommends that certificate attributes used with TIP do not include personally identifying, confidential, or sensitive information.

## Context keys
<a name="trusted-identity-propagation-keys"></a>

The following table lists the condition keys that trusted identity propagation adds to sessions.


| Key | Value | 
| --- | --- | 
| aws:OriginIdentity/Subject | The end-user or workload identifier: the value of the certificate field that the profile uses as its TIP Subject. For more information, see [TIP Subject](#trusted-identity-propagation-tip-subject). | 
| aws:OriginIdentity/SubjectType | user or workload, as declared on the profile. If the profile doesn't declare a subject type, sessions don't have this key. | 
| aws:OriginIdentity/Issuer | The SHA-384 hash of the certificate authority (CA) certificate in the trust anchor that the certificate chain validated to. The hash is of the DER-encoded certificate, in lowercase hexadecimal. | 
| aws:OriginIdentity/FederatedProviderArn | The Amazon Resource Name (ARN) of the trust anchor that authenticated the certificate. | 

## TIP Subject
<a name="trusted-identity-propagation-tip-subject"></a>

The trusted identity propagation Subject (TIP Subject) is the value of `aws:OriginIdentity/Subject`. It comes from one certificate field, the TIP Subject source, which you choose for the profile:
+ `x509Subject/CN` (default) – The common name (CN) in the certificate's Subject.
+ `x509SAN/URI` – The first URI in the certificate's Subject Alternative Name (SAN) extension, such as a Secure Production Identity Framework for Everyone (SPIFFE) ID.

On the console, you choose the TIP Subject source in the **Subject** field. In the IAM Roles Anywhere API, it's the `subjectSource` field of the `tipConfiguration` parameter in [CreateProfile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_CreateProfile.html) and [UpdateProfile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_UpdateProfile.html).

The profile needs a mapping rule for its TIP Subject source:
+ For `x509Subject/CN`, a rule for the `x509Subject` field with the specifier `CN` or `*`.
+ For `x509SAN/URI`, a rule for the `x509SAN` field with the specifier `URI`.

**Note**  
The default attribute mappings include both rules: `*` for `x509Subject` and `URI` for `x509SAN`. When trusted identity propagation is on for a profile, IAM Roles Anywhere doesn't issue a session in the following cases:  
The profile has no mapping rule for the TIP Subject source.
The certificate doesn't have a TIP Subject.
The TIP Subject is longer than 256 characters, or has characters other than letters, numbers, spaces, and `_ . : / = + - @`.

For more information about mapping rules, see [Certificate attribute mapping](attribute-mapping.md).

## Turn on TIP (console)
<a name="trusted-identity-propagation-console"></a>

When you create a profile, the **Trusted identity propagation** section has **Enable trusted identity propagation** turned on by default, with **x509Subject / CN** as the **Subject**. To use the first URI in the SAN extension instead, choose **x509SAN / URI** for **Subject**. To add a subject type, select **Include subject type**. To create the profile without trusted identity propagation, turn off **Enable trusted identity propagation**. For the steps to create a profile, see [Step 2: Configure roles](getting-started.md#getting-started-step2).

To turn on trusted identity propagation for an existing profile, so that you can use the `aws:OriginIdentity` condition keys in your policies, use the following steps.

**To turn on trusted identity propagation**

1. Open the [IAM Roles Anywhere console](https://console.aws.amazon.com/rolesanywhere/home) and choose the profile.

1. In the **Trusted identity propagation** section, choose **Enable**.

1. For **Subject**, keep **x509Subject / CN** (the default) or choose **x509SAN / URI**.

1. (Optional) Select **Include subject type** and choose **Workload** or **User**.

1. In the **Enable trusted identity propagation** dialog box, choose **Enable**.

To change the settings, choose **Edit**. To turn off trusted identity propagation, choose **Disable**. Sessions issued before the change keep their keys until they expire.

## Turn on TIP (AWS CLI)
<a name="trusted-identity-propagation-cli"></a>

When you run `create-profile` with the AWS CLI, the profile uses trusted identity propagation only if you include `--tip-configuration status=ENABLED`. If you omit the `--tip-configuration` option, the profile doesn't use it.

The following AWS CLI command turns on trusted identity propagation for an existing profile. Replace {{profile-id}} with the ID of the profile:

```bash
$ aws rolesanywhere update-profile \
    --profile-id {{profile-id}} \
    --tip-configuration status=ENABLED,subjectSource=x509SAN/URI,subjectType=workload
```

The `--tip-configuration` option replaces the profile's whole trusted identity propagation configuration. A field that you omit from `--tip-configuration` returns to its default: no subject type, and the TIP Subject source `x509Subject/CN`. An `update-profile` command without `--tip-configuration` doesn't change the configuration, as with the profile's other settings. To turn off trusted identity propagation, use `status=DISABLED`. The `get-profile` command returns the configuration.

## Example – Allow one workload identity from one CA
<a name="trusted-identity-propagation-policy"></a>

The following identity-based policy allows a workload to read objects from an Amazon Simple Storage Service (Amazon S3) bucket only if its certificate has a specific SPIFFE ID and was issued by your CA. The example assumes that the profile uses `x509SAN/URI` as its TIP Subject source, so the TIP Subject is the SPIFFE ID in the first URI in the certificate's SAN extension. Sessions from profiles that don't use trusted identity propagation don't have `aws:OriginIdentity` keys, so this policy doesn't allow them.

Replace the following values in the policy:
+ {{amzn-s3-demo-bucket}} – The name of your bucket.
+ The `aws:OriginIdentity/Subject` value – The TIP Subject of the workload: the first URI in the SAN extension of its certificate.
+ The `aws:OriginIdentity/Issuer` value – The Issuer value of your CA certificate. The OpenSSL command after the policy computes it.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadExampleObjectWithTIP",
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*",
      "Condition": {
        "StringEquals": {
          "aws:OriginIdentity/Subject": "{{spiffe://example.com/example-workload}}",
          "aws:OriginIdentity/Issuer": "{{0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef}}"
        }
      }
    }
  ]
}
```

To compute the Issuer value, replace {{ca-cert.pem}} with the path to your CA certificate file and run the following OpenSSL command:

```bash
$ openssl x509 -in {{ca-cert.pem}} -outform DER | openssl dgst -sha384 -r | cut -d' ' -f1
```

The Issuer value is a hash of the whole CA certificate, so it changes when you rotate the CA certificate in the trust anchor. Policies that check the old value stop matching. Update them when you rotate the certificate.