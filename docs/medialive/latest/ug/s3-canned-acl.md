# Using ACLs for delivery to Amazon S3

In a MediaLive channel, you might have one or more outputs where the destination is a bucket in
Amazon Simple Storage Service (Amazon S3). If the bucket is owned by another AWS account (another organization), you
typically want the other account to become the owner of the output files.

You can transfer ownership by setting up MediaLive to include a specific access control list
(ACL) when delivering to the bucket.

For more information on preparing to use an ACL, see the following:

- For an Archive or Frame capture output – [Controlling access to the
  output](archive-op-origin-server-s3.md#setting-dss-archive-canned-acl "archive-op-origin-server-s3.md#setting-dss-archive-canned-acl")
- For an HLS output – [Controlling access to the
  output](origin-server-hls-s3.md#setting-dss-hls-canned-acl "origin-server-hls-s3.md#setting-dss-hls-canned-acl")
  On the console, the field for enabling the feature is in the section for each output
  group. The field is described in the following sections:

- For Archive outputs – [Fields for the output
  destination](archive-destinations.md "archive-destinations.md")
- For Frame capture outputs – [Frame capture
  destination](framecapture-destinations.md "framecapture-destinations.md")
- For HLS outputs – [Fields for the output destination –
  sending to Amazon S3](hls-destinations-s3.md "hls-destinations-s3.md")
