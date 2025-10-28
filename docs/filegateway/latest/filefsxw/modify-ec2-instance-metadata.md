Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Modify Amazon EC2 instance metadata

options

The instance metadata service (IMDS) is an on-instance component that provides secure
access to Amazon EC2 instance metadata. An instance can be configured to accept incoming metadata
requests that use IMDS Version 1 (IMDSv1) or require that all metadata requests use IMDS
Version 2 (IMDSv2). IMDSv2 uses session-oriented requests and mitigates several types of
vulnerabilities that could be used to try to access the IMDS. For information about IMDSv2,
see [How Instance
Metadata Service Version 2 works](../../../AWSEC2/latest/UserGuide/instance-metadata-v2-how-it-works.md "../../../AWSEC2/latest/UserGuide/instance-metadata-v2-how-it-works.md") in the _Amazon Elastic Compute Cloud User
Guide_.

We recommend that you require IMDSv2 for all Amazon EC2 instances that host Storage Gateway. IMDSv2 is
required by default on all newly launched gateway instances. If you have existing instances
that are still configured to accept IMDSv1 metadata requests, see [Require the use of IMDSv2](../../../AWSEC2/latest/UserGuide/configuring-IMDS-existing-instances.md#modify-require-IMDSv2 "../../../AWSEC2/latest/UserGuide/configuring-IMDS-existing-instances.md#modify-require-IMDSv2") in the _Amazon Elastic Compute Cloud User Guide_ for
instructions to modify your instance metadata options to require the use of IMDSv2. Applying
this change does not require an instance reboot.
