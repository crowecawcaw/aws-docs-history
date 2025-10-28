# Create an account pool

To use the AWS CLI to create an account pool, you run the
**create-account-pool** command and provide the source.

- **For Lambda handler sources**: Provide the
  Lambda function and an IAM role with permissions to invoke the lambda, and
  trusts the `datazone.amazonaws.com` service principal.
- **For static account sources**: Provide a list of
  account and region pairs as key-value pairs in the command.
  Once configured in your domain, account pools automatically provide account and region
  information when creating new projects.

###### Topics

- [Create an account pool with a custom handler source](account-pools-create-handler.md "account-pools-create-handler.md")
- [Create an account pool with a static
  list of account and region pairs](account-pools-create-static.md "account-pools-create-static.md")
