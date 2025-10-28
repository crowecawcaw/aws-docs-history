This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Specifying the Motion

Overlay File Location

Specify one of the following valid locations for your overlay file:

- Local to the AWS Elemental Server system.

For example:
`/data/assets/overlay_001.png`

- A remote server via a mount point.

For example:
`/data/mnt/assets/overlay_001.png`

- **AWS Elemental Server version 2.10 and later** An Amazon S3 bucket, using SSL.

For example:
`s3ssl://company.test/sample_bucket/overlay_001.png`

- **AWS Elemental Server version 2.10 and later** An Amazon S3 bucket, without SSL.

For example:
`s3://company.test/sample_bucket/overlay_001.png`
For Amazon S3, use sse=true to enable S3 Server Side Encryption (SSE) and rrs=true to enable Reduced Redundancy Storage (RRS). Default values for RRS and SSE are false.

###### Note

If your motion overlay is a series of `.png` images, the way you specify it
depends on the version of AWS Elemental Server you're running. In version 2.10 and
later, include the full filename of the first image, as in the examples in the
previous list. In version 2.9 and earlier, include the part of the filename that
is common to all the images. For example,
`/data/assets/overlay_`.
