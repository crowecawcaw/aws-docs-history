# Considerations

The following considerations apply for account pools in Amazon SageMaker Unified Studio.

- Account pools contain a list of accounts where each account has an associated
  region.
- You can have up to 100 account pools per domain. For details, see [Quotas and limits for Amazon SageMaker Unified Studio](quotas.md "quotas.md").
- Account pools are not supported by Amazon Datazone domains.
- You can configure custom project profiles to use account pools using either
  the console or the CLI. Steps for the creation, update, and deletion of account
  pools are only supported in the AWS CLI.
  For more information about creating a custom project profile with an account pool, see
  [Project profiles in Amazon SageMaker Unified Studio](project-profiles.md "project-profiles.md").
