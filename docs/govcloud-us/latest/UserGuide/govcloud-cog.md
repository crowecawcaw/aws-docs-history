# Amazon Cognito in AWS GovCloud (US)

Amazon Cognito provides authentication, authorization, and user management for your web and mobile apps. Your users can sign in directly with a user name and password, or through a third party such as Facebook, Amazon, Google or Apple. The two main components of Amazon Cognito are user pools and identity pools. User pools are user directories that provide sign-up and sign-in options for your app users. Identity pools enable you to grant your users access to other AWS services. You can use identity pools and user pools separately or together.

## How Amazon Cognito differs for AWS GovCloud (US)

Below listed are the differences between the AWS GovCloud (US) and the standard AWS Regions.

- Amazon Pinpoint integration with user pools isn't suported in AWS GovCloud (US).
- Amazon Cognito in AWS GovCloud (US) uses FIPS endpoints only.
  - The API service endpoints are
    `cognito-idp-fips.us-gov-west-1.amazonaws.com` and
    `cognito-idp-fips.us-gov-east-1.amazonaws.com`. For more
    information about FIPS in AWS, see [Federal Information Processing Standard
    (FIPS) 140-3](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").
  - Hosted UI endpoints have a URL path in the format
    ``<your_user_pool_domain>`.auth-fips.us-gov-west-1.amazoncognito.com`
or
``<your_user_pool_domain>`.auth-fips.us-gov-east-1.amazoncognito.com`.

- Custom domains for user pools aren't supported in AWS GovCloud (US).
- Identity pools might be unable to assume IAM roles in AWS GovCloud (US-East)
  when the length of your role name plus role session name are longer than 24
  characters. This length doesn't include the path. For best results in this
  Region, use roles with name lengths of no greater than 20 characters and session
  name lengths of no greater than four characters.
- Amazon Cognito Sync isn't available in AWS GovCloud (US) Regions.

The IAM roles that you assign to users with Amazon Cognito identity pools must have a trust
policy that allows Amazon Cognito to generate temporary sessions. In AWS GovCloud (US), your trust
policies must grant `AssumeRoleWithWebIdentity` permission to the
`cognito-identity-us-gov.amazonaws.com` service principal. The following
example trust policy allows the identity pool
`us-gov-west-1:12345678-corner-cafe-123456790ab` to grant IAM credentials
to unauthenticated guest users.

For AWS GovCloud (US-East), replace `cognito-identity-us-gov.amazonaws.com`
with `cognito-identity.us-gov-east-1.amazonaws.com`.

## Documentation for Amazon Cognito

[Amazon Cognito documentation](../../../cognito.md "../../../cognito.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon Cognito metadata may be moved or stored outside of the AWS GovCloud
  (US) Region, or, in rare cases, accessed by certain AWS support personnel and
  system administrators who are not U.S. citizens.

For example, user pool domains, custom attribute names, resource server
identifiers and custom scopes may be included as part of the public Cognito
sign-in and sign-up functionality.
