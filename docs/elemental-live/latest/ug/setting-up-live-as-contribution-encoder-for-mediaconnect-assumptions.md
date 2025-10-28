# Assumptions

This section assumes the following:

- We assume that you know how to use the AWS console, AWS Identity and Access Management, and
  AWS Elemental MediaConnect, and that you have access to the user guides for the
  AWS services:
  - [What Is
    AWS Elemental MediaConnect?](../../../mediaconnect/latest/ug/what-is.md "../../../mediaconnect/latest/ug/what-is.md") in the
    _AWS Elemental MediaConnect User Guide_
  - [What Is
    IAM?](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") in the
    _IAM User Guide_
  - [What Is
    AWS Secrets Manager?](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") in the
    _AWS Secrets Manager User Guide_.

- We assume that you have already set up permissions for MediaConnect— you have
  created at least one AWS user and given permissions to those
  users so that they can use the features of MediaConnect. Specifically,
  for the purposes of this procedure, the user can create a MediaConnect
  flow. You have also set up MediaConnect as a trusted entity with
  Secrets Manager; see [Step 3: Create an IAM Role with a Trusted
  Relationship](../../../mediaconnect/latest/ug/encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role.html "../../../mediaconnect/latest/ug/encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role.html") in the
  _AWS Elemental MediaConnect User Guide_.
- We don't assume that you have set up Elemental Live with permissions in
  AWS. Setting up those permissions is one of the steps in this
  section.
