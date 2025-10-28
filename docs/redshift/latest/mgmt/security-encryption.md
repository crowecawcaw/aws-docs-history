Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

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
