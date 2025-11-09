# Setting up trusted identity propagation for

Studio

Setting up trusted identity propagation for Amazon SageMaker Studio requires your Amazon SageMaker AI domain
to have IAM Identity Center authentication method configured. This section guides you through the
prerequisites and steps needed to enable and configure trusted identity propagation for your
Studio users.

###### Topics

- [Prerequisites](#trustedidentitypropagation-setup-prerequisites "#trustedidentitypropagation-setup-prerequisites")
- [Enable trusted identity
  propagation for your Amazon SageMaker AI domain](#trustedidentitypropagation-setup-enable "#trustedidentitypropagation-setup-enable")
- [Configure your SageMaker AI execution
  role](#trustedidentitypropagation-setup-permissions "#trustedidentitypropagation-setup-permissions")

## Prerequisites

Before setting up trusted identity propagation for SageMaker AI, set up your IAM Identity Center using the
following instructions.

###### Note

Ensure that your IAM Identity Center and domain are in the same region.

- [IAM Identity Center trusted identity propagation prerequisites](../../../singlesignon/latest/userguide/trustedidentitypropagation-overall-prerequisites.md#trustedidentitypropagation-prerequisites "../../../singlesignon/latest/userguide/trustedidentitypropagation-overall-prerequisites.md#trustedidentitypropagation-prerequisites")
- [Set
  up IAM Identity Center](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md")
- [Add users
  to your IAM Identity Center directory](../../../singlesignon/latest/userguide/addusers.md "../../../singlesignon/latest/userguide/addusers.md")

## Enable trusted identity

propagation for your Amazon SageMaker AI domain

###### Important

- You can only enable trusted identity propagation for domains with AWS IAM Identity Center
  authentication method configured.
- Your IAM Identity Center and Amazon SageMaker AI domain must be in the same AWS Region.

Use one of the following options to learn how to enable trusted identity propagation for
a new or existing domain.

New domain - console

###### Enable trusted identity propagation for a new domain using the SageMaker AI

console

1. Open the [Amazon SageMaker AI
   console](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker").
2. Navigate to **Domains**.
3. [Create a custom domain](onboard-custom.md "onboard-custom.md"). The domain must have the **AWS IAM Identity Center** authentication method configured.
4. In the **Trusted identity propagation** section,
   choose to **Enable the trusted identity propagation for all
   users on this domain**.
5. Complete the custom creation process.

Existing domain - console

###### Enable trusted identity propagation for an existing domain using the SageMaker AI

console

###### Note

For trusted identity propagation to work properly after it is enabled for an
existing domain, users will need to restart their existing IAM Identity Center sessions. To do so,
either:

- Users will need to log out and log back in to their existing IAM Identity Center
  sessions
- Administrators can [end active sessions
  for their workforce users](../../../singlesignon/latest/userguide/end-active-sessions.md "../../../singlesignon/latest/userguide/end-active-sessions.md").

1. Open the [Amazon SageMaker AI
   console](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker").
2. Navigate to **Domains**.
3. Select your existing domain. The domain must have the **AWS IAM Identity Center** authentication method configured.
4. In the **Domain settings** tab, choose **Edit** in the **Authentication and
   permissions** section.
5. Choose to **Enable the trusted identity propagation for
   all users on this domain**.
6. Complete the domain configuration.

Existing domain - AWS CLI
Enable trusted identity propagation for an existing domain using the
AWS CLI

###### Note

For trusted identity propagation to work properly after it is enabled for an
existing domain, users will need to restart their existing IAM Identity Center sessions. To do so,
either:

- Users will need to log out and log back in to their existing IAM Identity Center
  sessions
- Administrators can [end active sessions
  for their workforce users](../../../singlesignon/latest/userguide/end-active-sessions.md "../../../singlesignon/latest/userguide/end-active-sessions.md").

```
aws sagemaker update-domain \
    --region $REGION \
    --domain-id $DOMAIN_ID \
    --domain-settings "TrustedIdentityPropagationSettings={Status=ENABLED}"
```

- `DOMAIN_ID` is the Amazon SageMaker AI domain ID. See [View
  domains](domain-view.md "domain-view.md") for more information.
- `REGION` is the AWS Region of your Amazon SageMaker AI domain. You can find
  this at the top right of any AWS console page.

## Configure your SageMaker AI execution

role

To enable trusted identity propagation for your Studio users, all trusted identity
propagation roles need the set the following context permissions. Update the trust policy
for all roles to include the `sts:AssumeRole` and `sts:SetContext`
actions. Use the following policy when you [update your role trust
policy](../../../IAM/latest/UserGuide/id_roles_update-role-trust-policy.md "../../../IAM/latest/UserGuide/id_roles_update-role-trust-policy.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "sagemaker.amazonaws.com"
 ]
 },
 "Action": [
 "sts:AssumeRole",
 "sts:SetContext"
 ]
 }
 ]
}`

```
