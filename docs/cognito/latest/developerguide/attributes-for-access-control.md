# Using attributes for access control

Attributes for access control is the Amazon Cognito identity pools implementation of
attribute-based access control (ABAC). You can use IAM policies to control access to AWS
resources through Amazon Cognito identity pools based on user attributes. These attributes can be
drawn from social and corporate identity providers. You can map attributes within providers’
access and ID tokens or SAML assertions to tags that can be referenced in the IAM
permissions policies.

You can choose default mappings or create your own custom mappings in Amazon Cognito identity
pools. The default mappings allow you to write IAM policies based on a fixed set of user
attributes. Custom mappings allow you to select a custom set of user attributes that are
referenced in the IAM permissions policies. The **Attribute names** in
the Amazon Cognito console are mapped to **Tag key for principal**, which
are the tags that are referenced in the IAM permissions policy.

For example, let's say that you own a media streaming service with a free and a paid
membership. You store the media files in Amazon S3 and tag them with free or premium tags. You
can use attributes for access control to allow access to free and paid content based on user
membership level, which is part of the user's profile. You can map the membership attribute
to a tag key for principal to be passed on to the IAM permissions policy. This way you can
create a single permissions policy and conditionally allow access to premium content based
on the value of membership level and tag on the content files.

###### Topics

- [Using attributes for access
  control with Amazon Cognito identity pools](#using-afac-with-cognito-identity-pools "#using-afac-with-cognito-identity-pools")
- [Using attributes
  for access control policy example](#using-attributes-for-access-control-policy-example "#using-attributes-for-access-control-policy-example")
- [Turn off attributes for access control (console)](#disable-afac "#disable-afac")
- [Default provider mappings](#provider-mappings "#provider-mappings")
  Using attributes to control access has several benefits:

- Permissions management is more efficient when you use attributes for access
  control. You can create a basic permissions policy that uses user attributes instead
  of creating multiple policies for different job functions.
- You don't need to update your policies whenever you add or remove resources or
  users for your application. The permissions policy will only grant the access to
  users with the matching user attributes. For example, you might need to control the
  access to certain S3 buckets based on the job title of users. In that case, you can
  create a permissions policy to allow access to these files only for users within the
  defined job title. For more information, see [IAM Tutorial: Use SAML
  session tags for ABAC](../../../IAM/latest/UserGuide/tutorial_abac-saml.md "../../../IAM/latest/UserGuide/tutorial_abac-saml.md").
- Attributes can be passed as principal tags to a policy that allows or denies
  permissions based on the values of those attributes.

## Using attributes for access

control with Amazon Cognito identity pools

Before you can use attributes for access control, ensure that you meet the following
prerequisites:

- [An AWS account](getting-started-with-identity-pools.md#aws-sign-up-identity-pools "getting-started-with-identity-pools.md#aws-sign-up-identity-pools")
- [User pool](cognito-user-pool-as-user-directory.md "cognito-user-pool-as-user-directory.md")
- [Identity pool](getting-started-with-identity-pools.md#create-identity-pools "getting-started-with-identity-pools.md#create-identity-pools")
- [Set up an SDK](getting-started-with-identity-pools.md#install-the-mobile-or-javascript-sdk "getting-started-with-identity-pools.md#install-the-mobile-or-javascript-sdk")
- [Integrated identity providers](getting-started-with-identity-pools.md##integrate-the-identity-providers "getting-started-with-identity-pools.md##integrate-the-identity-providers")
- [Credentials](getting-started-with-identity-pools.md#get-credentials "getting-started-with-identity-pools.md#get-credentials")

To use attributes for access control, the **Claim** that you set
as the source of data sets the value of the **Tag Key** that you
choose. Amazon Cognito applies the tag key and value to your user's session. Your IAM
policies can evaluate your user's access from the
`${aws:PrincipalTag/`tagkey`}`
condition. IAM evaluates the value of your user's tag against the policy.

You must prepare IAM roles whose credentials you want to pass to your users. The
trust policy of these roles must permit Amazon Cognito to assume the role for your user. For
attributes for access control, you must also allow Amazon Cognito to apply principal tags to your
user's temporary session. Grant permission to assume the role with the action [AssumeRoleWithWebIdentity](../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md "../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md"). Grant permission to tag users' sessions with the
[permission-only action](../../../service-authorization/latest/reference/list_awssecuritytokenservice.md#awssecuritytokenservice-actions-as-permissions "../../../service-authorization/latest/reference/list_awssecuritytokenservice.md#awssecuritytokenservice-actions-as-permissions")
`sts:TagSession`. For more information, see [Passing session
tags in AWS Security Token Service](../../../IAM/latest/UserGuide/id_session-tags.md "../../../IAM/latest/UserGuide/id_session-tags.md") in the _AWS Identity and Access Management User
Guide_. For an example trust policy that grants
`sts:AssumeRoleWithWebIdentity` and `sts:TagSession`
permissions to the Amazon Cognito service principal `cognito-identity.amazonaws.com`,
see [Using attributes
for access control policy example](#using-attributes-for-access-control-policy-example "#using-attributes-for-access-control-policy-example").

###### To configure attributes for access control in the console

1. Sign in to the [Amazon Cognito
   console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home") and select **Identity pools**. Select an
   identity pool.
2. Choose the **User access** tab.
3. Locate **Identity providers**. Choose the identity provider
   that you want to edit. If you want to add a new IdP, select **Add
   identity provider**.
4. To change the principal tags that Amazon Cognito assigns when it issues credentials to
   users who have authenticated with this provider, choose
   **Edit** in **Attributes for access
   control**.
   1. To apply no principal tags, choose
      **Inactive**.
   2. To apply principal tags based on `sub` and `aud`
      claims, choose **Use default mappings**.
   3. To create your own custom schema of attributes to principal tags,
      choose **Use custom mappings**. Then enter a
      **Tag key** that you want to source from each
      **Claim** that you want to represent in a
      tag.

5. Select **Save changes**.

## Using attributes

for access control policy example

Consider a scenario where an employee from the legal department of a company needs to
list all files in buckets that belong to their department and are classified with their
security level. Assume the token that this employee gets from the identity provider
contains the following claims.

**Claims**

```

            { .
              .
            "sub" : "57e7b692-4f66-480d-98b8-45a6729b4c88",
            "department" : "legal",
            "clearance" : "confidential",
             .
             .
            }

```

These attributes can be mapped to tags and referenced in IAM permissions policies as
principal tags. You can now manage access by changing the user profile on the identity
provider's end. Alternatively, you can change attributes on the resource side by using
names or tags without changing the policy itself.

The following permissions policy does two things:

- Allows list access to all S3 buckets that end with a prefix that matches the
  user’s department name.
- Allows read access on files in these buckets as long as the clearance tag on
  the file matches user’s clearance attribute.

**Permissions policy**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "s3:List*",
 "Resource": "arn:aws:s3:::*-${aws:PrincipalTag/department}"
 },
 {
 "Effect": "Allow",
 "Action": "s3:GetObject*",
 "Resource": "arn:aws:s3:::*-${aws:PrincipalTag/department}/*",
 "Condition": {
 "StringEquals": {
 "s3:ExistingObjectTag/clearance": "${aws:PrincipalTag/clearance}"
 }
 }
 }
 ]
}`

```

The trust policy determines who can assume this role. The trust relationship policy
allows the use of `sts:AssumeRoleWithWebIdentity` and
`sts:TagSession` to allow access. It adds conditions to restrict the
policy to the identity pool that you created and it makes sure that it’s for an
authenticated role.

**Trust policy**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Federated": "cognito-identity.amazonaws.com"
 },
 "Action": [
 "sts:AssumeRoleWithWebIdentity",
 "sts:TagSession"
 ],
 "Condition": {
 "StringEquals": {
 "cognito-identity.amazonaws.com:aud": "IDENTITY-POOL-ID"
 },
 "ForAnyValue:StringLike": {
 "cognito-identity.amazonaws.com:amr": "authenticated"
 }
 }
 }
 ]
}`

```

## Turn off attributes for access control (console)

Follow this procedure to deactivate attributes for access control.

###### To deactivate attributes for access control in the console

1. Sign in to the [Amazon Cognito
   console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home") and select **Identity pools**. Select an
   identity pool.
2. Choose the **User access** tab.
3. Locate **Identity providers**. Choose the identity provider
   that you want to edit.
4. Choose **Edit** in **Attributes for access
   control**.
5. To apply no principal tags, choose **Inactive**.
6. Select **Save changes**.

## Default provider mappings

The following table has the default mapping information for the authentication
providers that Amazon Cognito supports.

| Provider                 | Token type           | Principal tag values                                                                                                                  | Example                                                                                                       |
| ------------------------ | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon Cognito user pool | ID token             | aud(client ID) and sub(user ID)                                                                                                       | "6jk8ltokc7ac9es6jrtg9q572f", "57e7b692-4f66-480d-98b8-45a6729b4c88"                                          |
| Facebook                 | Access token         | aud(app_id), sub(user_id)                                                                                                             | "492844718097981", "112177216992379"                                                                          |
| Google                   | ID token             | aud(client ID) and sub(user ID)                                                                                                       | "620493171733-eebk7c0hcp5lj3e1tlqp1gntt3k0rncv.apps.googleusercontent.com", "109220063452404746097"           |
| SAML                     | Assertions           | "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier" , "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name" | "auth0                                                                                                        | 5e28d196f8f55a0eaaa95de3", "user123@gmail.com"                                                                                                                             |
| Apple                    | ID token             | aud(client ID) and sub (user ID)                                                                                                      | "com.amazonaws.ec2-54-80-172-243.compute-1.client", "001968.a6ca34e9c1e742458a26cf8005854be9.0733"            |
| Amazon                   | Access token         | aud (Client ID on Amzn Dev Ac), user_id(user ID)                                                                                      | "amzn1.application-oa2-client.9d70d9382d3446108aaee3dd763a0fa6", "amzn1.account.AGHNIFJQMFSBG3G6XCPVB35ORQAA" |
| Standard OIDC providers  | ID and access tokens | aud (as client_id), sub (as user ID)                                                                                                  | "620493171733-eebk7c0hcp5lj3e1tlqp1gntt3k0rncv.apps.googleusercontent.com", "109220063452404746097"           |
| Twitter                  | Access token         | aud (app ID; app Secret), sub (user ID)                                                                                               | "DfwifTtKEX1FiIBRnOTlR0CFK;Xgj5xb8xIrIVCPjXgLIdkW7fXmwcJJrFvnoK9gwZkLexo1y5z1", "1269003884292222976"         |
| DevAuth                  | Map                  | Not applicable                                                                                                                        | "tag1", "tag2"                                                                                                | ###### Note The default attribute mappings option is automatically populated for the **Tag Key for Principal** and **Attribute** names. You can't change default mappings. |
