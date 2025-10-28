End of support notice: On November 13, 2025, AWS will discontinue support for Amazon Elastic Transcoder. After November 13, 2025, you will no longer be able to access the Elastic Transcoder console or Elastic Transcoder resources.

For more information about transitioning to AWS Elemental MediaConvert, visit this [blog post](https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/ "https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/").

# Securing Your Content

This section discusses how to control access to your Elastic Transcoder resources, how to encrypt your
files while they are at rest, and how to apply Digital Rights Management (DRM) to your
files. Controlling access to your resources allows you to designate tasks such as creating
jobs to one of your IAM roles, while at the same time reserving the ability to update or
delete your pipeline and preset resources. Encrypting your files at rest provides an
additional level of content protection, especially for sensitive or strictly controlled
files, while DRM allows you further control over who can playback the files, beyond the
level provided by AWS permissions on resources.

IAM access controls are for when you want to be able to control who has access to your files and who
can affect resources such as pipelines and presets. File encryption (encryption at rest) is for when you
want a file to be stored in an encrypted state, and HLS and DRM are for when you want to be able to
control who has the ability to playback your files.

For more information on security best practices, see the
[IAM Best Practices](../../../IAM/latest/UserGuide/IAMBestPractices.md "../../../IAM/latest/UserGuide/IAMBestPractices.md") guide.

###### Topics

- [Controlling Access to Elastic Transcoder](access-control.md "access-control.md")
- [Data Encryption Options](encryption.md "encryption.md")
