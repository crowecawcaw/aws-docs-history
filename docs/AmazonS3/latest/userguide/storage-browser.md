# Working with Storage Browser for Amazon S3

[Storage Browser for S3](https://aws.amazon.com/s3/features/storage-browser/ "https://aws.amazon.com/s3/features/storage-browser/") is an open source component that you can add to your web application
to provide your end users with a simple graphical interface for data stored in Amazon
S3. With Storage Browser for S3, you can provide authorized end users access to browse, download,
upload, copy, and delete data in S3 directly from your own applications.

Storage Browser for S3 supports the following operations for files: `LIST`,
`GET`, `PUT`, `COPY`, `UPLOAD`, and
`DELETE`. To deliver high throughput data transfer, Storage Browser for S3 only displays
the data that your end users are authorized to access and optimizes upload requests.
Storage Browser also optimizes performance for faster load times, calculates checksums
of the data that your end users upload, and accepts objects after confirming that your data integrity
was maintained (in transit) over the public internet. You can control access to your data based on
your end user’s identity using AWS security and identity services, or your own managed
services. You can also customize Storage Browser to match your existing application’s
design and branding.

Storage Browser for S3 is only available for web and intranet applications on the React framework.
You can use Storage Browser to access Amazon S3 objects in all storage classes except
S3 Glacier Flexible Retrieval, S3 Glacier Deep Archive, S3 Intelligent-Tiering Archive
Access tier, and S3 Intelligent-Tiering Deep Archive Access tier.

Storage Browser for S3 is available to use with your web applications in the [AWS Amplify React](https://ui.docs.amplify.aws/ "https://ui.docs.amplify.aws/") library. For more information
about Storage Browser, see [Storage Browser for S3](https://aws.amazon.com/s3/features/storage-browser/ "https://aws.amazon.com/s3/features/storage-browser/").

###### Topics

- [Using Storage Browser for S3](using-storagebrowser.md "using-storagebrowser.md")
- [Installing Storage Browser for S3](installing-storagebrowser.md "installing-storagebrowser.md")
- [Setting up Storage Browser for S3](setup-storagebrowser.md "setup-storagebrowser.md")
- [Configuring Storage Browser for S3](s3config-storagebrowser.md "s3config-storagebrowser.md")
- [Troubleshooting Storage Browser for S3](troubleshooting-storagebrowser.md "troubleshooting-storagebrowser.md")
