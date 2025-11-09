# Requesting Sentieon licenses for private workflows

If your private workflow uses Sentieon software, you need a Senieon license.
Follow these steps to request and set up a license for the Sentieon software:

- Request a Sentieon license
  - Send an email to the Sentieon support group (support@sentieon.com) to request a software license.
    - Provide your AWS Canonical User ID in the email.
    - Find your AWS Canonical User ID by following [these
      instructions](../../../accounts/latest/reference/manage-acct-identifiers.md#FindCanonicalId "../../../accounts/latest/reference/manage-acct-identifiers.md#FindCanonicalId").

- Update your HealthOmics service role to grant it access to the Sentieon licensing server proxy and Sentieon Omics bucket
  in your Region. The following example grants access in `us-east-1`. If required, replace this text with your Region.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObjectAcl",
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::omics-ap-`us-east-1`/*",
 "arn:aws:s3:::sentieon-omics-license-`us-east-1`/*"
 ]
 }
 ]
 }`

```

- Generate an AWS support case to get access to the Sentieon license server proxy.
  - To create a support case, navigate to [support.console.aws.amazon.com.](https://support.console.aws.amazon.com "https://support.console.aws.amazon.com")
  - Provide your AWS account and Region in the support case. Your account is added to the allowlist for
    the licensing server proxy.

- Build your private workflow using the Sentieon container and the Sentieon license script.
  - For additional instructions on using Sentieon tools inside private workflows, see [Sentieon-Amazon-Omics](https://github.com/Sentieon/sentieon-amazon-omics "https://github.com/Sentieon/sentieon-amazon-omics") in GitHub.

- Sentieon software version 202112.07 and higher support the HealthOmics licensing server proxy. To use
  Sentieon software versions earlier than 202112.07, contact Sentieon support.
