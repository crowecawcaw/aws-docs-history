Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Data encryption

Data protection refers to protecting data while in transit (as it travels to and from Amazon Redshift) and at rest (while it is stored on disks in Amazon Redshift data centers).
You can protect data in transit by using SSL or by using client-side encryption. You have the following
options of protecting data at rest in Amazon Redshift.

- **Use server-side encryption** – You request
  Amazon Redshift to encrypt your data before saving it on disks in its data
  centers and decrypt it when you download the objects.
- **Use client-side encryption** – You can encrypt data
  client-side and upload the encrypted data to Amazon Redshift. In this case, you
  manage the encryption process, the encryption keys, and related tools.
