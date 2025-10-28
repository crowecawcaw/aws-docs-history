# Sign in through the AWS Command Line Interface

We recommend that you configure a user in IAM Identity Center if you plan to use the AWS Command Line Interface. The AWS
access portal user interface makes it easy for IAM Identity Center users to select an AWS account and use the
AWS CLI to get temporary security credentials. For more information about how to get these credentials, see [Region availability for AWS Builder ID](sign-in-builder-id.md#regions-aws_builder_id "sign-in-builder-id.md#regions-aws_builder_id").
You can also configure the AWS CLI directly to
authenticate users with IAM Identity Center.

###### To sign in through the AWS CLI with IAM Identity Center credentials

- Check that you've completed the [Prerequisites](../../../cli/latest/userguide/sso-configure-profile-token.md#sso-configure-profile-prereqs "../../../cli/latest/userguide/sso-configure-profile-token.md#sso-configure-profile-prereqs").
- If you're signing in for the first time, [configure your profile with the `aws configure sso` wizard](../../../cli/latest/userguide/sso-configure-profile-token.md#sso-configure-profile-token-auto-sso "../../../cli/latest/userguide/sso-configure-profile-token.md#sso-configure-profile-token-auto-sso").
- After you configure your profile, run the following command, then follow the prompts in
  your terminal.

```
`$` `aws sso login --profile` `my-profile`
```

## Additional information

If you want more information about signing-in using the command-line, refer to the
following resources.

- For details on using IAM Identity Center credentials, see [Getting IAM Identity Center user
  credentials for the AWS CLI or AWS SDKs](../../../singlesignon/latest/userguide/howtogetcredentials.md "../../../singlesignon/latest/userguide/howtogetcredentials.md").
- For details on configuration, see [Configuring the AWS CLI to
  use IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md").
- For more details on the AWS CLI sign-in process, see [Signing in and getting credentials](../../../cli/latest/userguide/sso-using-profile.md#sso-using-profile-sign-in "../../../cli/latest/userguide/sso-using-profile.md#sso-using-profile-sign-in").
