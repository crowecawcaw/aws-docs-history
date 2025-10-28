# Amazon SNS data encryption

Data protection refers to protecting data while in-transit (as it travels to and from Amazon SNS)
and at rest (while it is stored on disks in Amazon SNS data centers). You can protect data in transit
using Secure Sockets Layer (SSL) or client-side encryption. By default, Amazon SNS stores messages
and files using disk encryption. You can protect data at rest by requesting Amazon SNS to encrypt
your messages before saving them to the encrypted file system in its data centers. Amazon SNS
recommends using SSE for optimized data encryption.
