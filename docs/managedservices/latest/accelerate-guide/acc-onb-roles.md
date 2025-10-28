# The template to create AMS roles

The following AMS role grants permissions to your AMS cloud architect (CA). The following zip file contains Terraform code and AWS CloudFormation template that simplifies creating
the IAM role, permissions policy, and trust policy. For more information, consult with your CA.

| Role Name                             | Required by                          | Sample Templates                                                                                       |
| ------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aws_managedservices_onboarding_role` | AMS personnel during onboarding only | [onboarding_role_minimal.zip](samples/onboarding_role_minimal.md "samples/onboarding_role_minimal.md") | ###### Note After you select and download a sample template (one per role), you will upload these as definitions of AWS CloudFormation stacks in [Create aws_managedservices_onboarding_role with AWS CloudFormation for Accelerate](acc-onb-create-roles-with-cf.md "acc-onb-create-roles-with-cf.md"). |
