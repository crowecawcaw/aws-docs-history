# Using credentials in your application

After the session starts, your application or launch script can call AWS services using the
credentials you configured. You do not need to change your code. The AWS SDK automatically
discovers and uses the credentials.

To verify that credentials are available, run the following command from your application
or launch script:

```
aws sts get-caller-identity
```

The AWS CLI and all AWS SDKs automatically discover session credentials and refresh
them before they expire. You do not need to manage credential rotation in your application
code.

For more information about how the AWS SDK discovers credentials, see
[Credential providers](../../../sdkref/latest/guide/standardized-credentials.md "../../../sdkref/latest/guide/standardized-credentials.md")
in the _AWS SDKs and Tools Reference Guide_.

###### Important

Do not set `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, or
`AWS_SESSION_TOKEN` environment variables in your session's
`AdditionalEnvironmentVariables`. These take precedence and prevent your
application from using the IAM role credentials.
