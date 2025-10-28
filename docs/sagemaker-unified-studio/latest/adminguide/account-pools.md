# Account pools in Amazon SageMaker Unified Studio

In Amazon SageMaker Unified Studio, you can configure your domain to create project profiles where an account
pool provides AWS account and AWS Region information. An account pool is a list of
authorized associated accounts and regions. This allows you to create project profiles that
can be used to create projects across multiple accounts and regions, while controlling which
accounts and regions are available for use.

There are two ways to create project profiles with account pools that you configure for
validation of authorized accounts at the time of project creation.

- Static list of account and region pairs
- Custom Lambda handler to authorize account and region pair information
  The custom handler accesses customer information and then dynamically generates a list of
  authorized associated account and region pairs based on a set of rules in the Lambda
  function. Amazon SageMaker Unified Studio then resolves the list of account and region pairs in the account pool
  at project creation time.

For more information about associated accounts in Amazon SageMaker Unified Studio, see [Associated accounts in Amazon SageMaker Unified Studio](associated-accounts.md "associated-accounts.md").

###### Topics

- [Considerations](account-pools-considerations.md "account-pools-considerations.md")
- [Use cases](account-pools-usecases.md "account-pools-usecases.md")
- [Create an account pool](account-pools-create.md "account-pools-create.md")
- [View an account pool](account-pools-view.md "account-pools-view.md")
- [List account pools for a domain](account-pools-list.md "account-pools-list.md")
- [View the list of accounts in an account pool](account-pools-list-accounts.md "account-pools-list-accounts.md")
- [Delete an account pool](account-pools-delete.md "account-pools-delete.md")
- [Create a project profile with an account pool](account-pools-create-profile.md "account-pools-create-profile.md")
