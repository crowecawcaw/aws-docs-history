The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Testing in a sandbox

Partners can use a sandbox to test and validate their AWS Partner Central API interactions in a secure and isolated environment,
ensuring smooth operation before promoting their solution to the production environment. AWS offers a
dynamic sandbox to AWS Partner Central API users that returns responses similar to the production environment.
AWS does not provide a user interface to the sandbox environment. Therefore, partners
need to rely on the programmatic responses to test their solutions.

## Access to the sandbox environment

Partners gain access to the testing environment as soon as they link
their AWS account to the Partner Central account. For more information, see
[Linking your AWS account to AWS Partner Central account](../getting-started/account-linking.md "../getting-started/account-linking.md"). Each request
includes a `catalog` parameter, which determines the data
environment. When `catalog` is set to `AWS`, it
references production data, and when it's set to `Sandbox`, it
references sandbox data.

## Important details about the sandbox environment

1. Data refresh: Once per year, AWS refreshes the data in the sandbox environment
   (typically at the beginning of the year). After this refresh, you may lose some of the
   data in your testing environment.
2. Testing scope: The sandbox environment is typically used for functional testing and not
   for testing scalability or performance.

###### Topics

- [Testing in a sandbox for the AWS Partner Central Account API](testing-sandbox-account.md "testing-sandbox-account.md")
- [Testing in a sandbox for the AWS Partner Central Selling API](testing-sandbox.md "testing-sandbox.md")
- [Testing in a sandbox for the AWS Partner Central Benefits API](testing-sandbox-benefits.md "testing-sandbox-benefits.md")
- [Testing in a sandbox for the AWS Partner Central Channel API](testing-sandbox-channel.md "testing-sandbox-channel.md")
- [Testing in a sandbox for the AWS Partner Central Revenue Measurement API](testing-sandbox-prm.md "testing-sandbox-prm.md")
