# Credentials required by the AWS CLI, the AWS SDK, or the Amazon Keyspaces SigV4 plugin for Cassandra client drivers

The following credentials are required to authenticate the IAM user or role:

`AWS_ACCESS_KEY_ID`

Specifies an AWS access key associated with an IAM user or
role.

The access key `aws_access_key_id` is required to connect to Amazon Keyspaces programmatically.

`AWS_SECRET_ACCESS_KEY`

Specifies the secret key associated with the access key. This is
essentially the "password" for the access key.

The `aws_secret_access_key` is required to connect to Amazon Keyspaces programmatically.

`AWS_SESSION_TOKEN` – Optional

Specifies the session token value that is required if you are using
temporary security credentials that you retrieved directly from AWS Security Token Service
operations. For more information, see [Create temporary credentials to connect to Amazon Keyspaces using an IAM role and the SigV4 plugin](temporary.credentials.md "temporary.credentials.md").

If you are connecting with an IAM user, the `aws_session_token` is not required.
