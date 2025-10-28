# Onboard to re:Post Private through IAM Identity Center

re:Post Private integrates with AWS IAM Identity Center to provide identity federation for your workforce. Through IAM Identity Center, users are redirected to their existing company directory to sign in with their existing credentials. Then, they're seamlessly signed in to their private re:Post. This makes sure that security settings such as password policies and two-factor
authentication are enforced. Using IAM Identity Center doesn’t impact your existing IAM configuration.

If you don’t have an existing user directory or prefer not to federate, then IAM Identity Center offers an integrated user directory that you can use to create users and groups for re:Post Private. re:Post Private doesn’t support the use of IAM users and roles to assign permissions within a private re:Post. User permissions within a private re:Post are configured by an administrator on their private re:Post application.

For more information about IAM Identity Center, see [What is AWS IAM Identity Center (successor to AWS Single Sign-On)](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md"). For more information about getting started with
IAM Identity Center, see [Getting started](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md"). To use IAM Identity Center, you must also have AWS Organizations activated for the account.

###### Important

re:Post Private supports only [organization instances of IAM Identity Center](../../../singlesignon/latest/userguide/organization-instances-identity-center.md "../../../singlesignon/latest/userguide/organization-instances-identity-center.md").
