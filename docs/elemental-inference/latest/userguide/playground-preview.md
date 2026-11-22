

# Previewing all features

Before you start an All features preview, make sure that you have the following:
+ An MP4 video file in Amazon S3, and an Amazon S3 folder for the output.
+ A source video at 60 frames per second (fps) or less.
+ The playground service role, with access to your input and output buckets, and the user permissions for a preview. For more information, see [Permissions](playground-permissions.md).
+ No other preview running in your account in the same AWS Region.
+ Fewer active feeds in the Region than your Active feeds per account quota. The preview's feed counts toward this quota while the preview runs. For more information, see [Quotas for AWS Elemental Inference](quotas.md).