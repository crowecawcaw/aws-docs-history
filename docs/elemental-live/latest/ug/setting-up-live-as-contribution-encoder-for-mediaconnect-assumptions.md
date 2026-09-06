

# Assumptions
<a name="setting-up-live-as-contribution-encoder-for-mediaconnect-assumptions"></a>

This section assumes the following:
+ We assume that you know how to use the AWS console, AWS Identity and Access Management, and AWS Elemental MediaConnect, and that you have access to the user guides for the AWS services:
  + [What Is AWS Elemental MediaConnect?](https://docs.aws.amazon.com/mediaconnect/latest/ug/what-is.html) in the *AWS Elemental MediaConnect User Guide*
  + [What Is IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) in the *IAM User Guide*
  + [What Is AWS Secrets Manager?](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) in the *AWS Secrets Manager User Guide*.
+ We assume that you have already set up permissions for MediaConnect— you have created at least one AWS user and given permissions to those users so that they can use the features of MediaConnect. Specifically, for the purposes of this procedure, the user can create a MediaConnect flow. You have also set up MediaConnect as a trusted entity with Secrets Manager; see [Step 3: Create an IAM Role with a Trusted Relationship](https://docs.aws.amazon.com/mediaconnect/latest/ug/encryption-static-key-set-up.html#encryption-static-key-set-up-create-iam-role.html) in the *AWS Elemental MediaConnect User Guide*.
+ We don't assume that you have set up Elemental Live with permissions in AWS. Setting up those permissions is one of the steps in this section.