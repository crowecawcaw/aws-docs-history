# Grant permission

You must grant stream permission to your IAM roles in order to ingest streams in
Amazon Kinesis Video Streams with WebRTC.

###### Note

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

Both Master and Viewer roles must also have `DescribeStream`,
`GetDataEndpoint`, and `PutMedia` permissions to ingest media
to Kinesis Video Streams.

Refer to the sample IAM policy below for Master participants:
