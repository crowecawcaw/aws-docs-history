# Guidance for setting up for custom paths

The content in the customized path in an HLS output must be appropriate for the system that
is downstream of MediaLive. Following is some guidance for using the _base
URL_ fields for different downstream systems.

**Setting up for custom paths if you control the downstream
system**

You might control the downstream system. For example, the downstream systems might be Amazon S3
or MediaStore that sends content to Amazon CloudFront. Your handling of the HLS files might require that you
move one or more of the sets of files around. In this case, you could complete these _base URL_ fields to match the paths of the final location of the
files.

**Setting up for custom paths if the downstream packager is
MediaPackage**

If the downstream package is MediaPackage, leave the **Base URL** fields empty.
MediaPackage doesn’t use this information.

**Setting up for custom paths if you use a third-party downstream
system**

If you use a third-party downstream system, the downstream system must tell you whether to
complete these **Base URL** fields.
