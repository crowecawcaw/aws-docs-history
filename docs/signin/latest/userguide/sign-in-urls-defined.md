# Determine your sign-in URL

Use one of the following URLs to access AWS depending on what kind of AWS user you
are. For more information, see [Determine your user type](user-types-list.md "user-types-list.md").

###### Topics

- [AWS account root user sign-in URL](#root-user-url "#root-user-url")
- [AWS access portal](#access-portal-url "#access-portal-url")
- [IAM user sign-in URL](#IAM-user-url "#IAM-user-url")
- [Federated identity URL](#federated-identities-url "#federated-identities-url")
- [AWS Builder ID URL](#builder-id-url "#builder-id-url")

## AWS account root user sign-in URL

The root user accesses the AWS Management Console from the AWS sign-in page: `https://console.aws.amazon.com/`.

This sign-in page also has the option of signing in as an IAM user.

## AWS access portal

The AWS access portal is a specific sign-in URL for users in IAM Identity Center to sign in and access
your account. When an administrator creates the user in IAM Identity Center the administrator chooses
whether the user receives either an email invitation to join IAM Identity Center or a message from the
administrator or help desk employee that contains a one-time password and AWS access portal
URL. The format of specific sign-in URL is like the following examples:

```
https://`d-xxxxxxxxxx`.awsapps.com/start
```

or

```
https://`your_subdomain`.awsapps.com/start
```

The specific sign-in URL varies because your administrator can customize it. The
specific sign-in URL might begin with the letter D followed by 10 randomized numbers and
letters. Your subdomain might also be used in the sign-in URL and may include your company
name like the following example:

![AWS access portal URL example.](images/URL-example-aws-access-portal-AnyCompany.png)

###### Note

We recommend that you bookmark the specific sign-in URL for your AWS access portal so
that you can access it later.

For more information about your AWS access portal, see [Using the
AWS access portal](../../../singlesignon/latest/userguide/using-the-portal.md "../../../singlesignon/latest/userguide/using-the-portal.md").

## IAM user sign-in URL

IAM users can access the AWS Management Console with a specific IAM user sign-in URL. The
IAM user sign-in URL combines your AWS account ID or alias and
`signin.aws.amazon.com/console`

An example of what an IAM user sign-in URL looks like:

```
https://`account_alias_or_id`.signin.aws.amazon.com/console/
```

If your account ID is 111122223333, your sign-in URL would be:

![IAM user sign-in URL example.](images/URL-example-IAM-user-sign-in.png)

If you're experiencing issues accessing your AWS account with your IAM user sign-in
URL, see [Resilience in
AWS Identity and Access Management](../../../IAM/latest/UserGuide/disaster-recovery-resiliency.md "../../../IAM/latest/UserGuide/disaster-recovery-resiliency.md") for more information.

## Federated identity URL

The sign-in URL for a federated identity varies. The external identity or external
Identity Provider (IdP) determines the sign-in URL for federated identities. The external
identity could be Windows Active Directory, Login with Amazon, Facebook, or Google. Contact
your administrator for more details on how to sign in as a federated identity.

For more information about federated identities, see [About web identity
federation](../../../IAM/latest/UserGuide/id_roles_providers_oidc.md "../../../IAM/latest/UserGuide/id_roles_providers_oidc.md").

## AWS Builder ID URL

The URL for your AWS Builder ID profile is [https://profile.aws.amazon.com/](https://profile.aws.amazon.com/ "https://profile.aws.amazon.com/").
When using your AWS Builder ID, the sign-in URL depends on what service you want to access. For
example, to sign in to Amazon CodeCatalyst, go to [https://codecatalyst.aws/login](https://codecatalyst.aws/login "https://codecatalyst.aws/login").
