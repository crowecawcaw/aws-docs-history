

# SMSEC04-BP04 Encrypt content at rest when delivering via physical medium
<a name="smsec04-bp04"></a>

Deploy secure physical media delivery solutions for large-scale content transfer using hardware-encrypted storage devices and secure logistics processes.

**Desired outcome:**
+ Content is migrated to Amazon S3 from an off-site location
+ Content is encrypted such that only you can access it after it has been delivered and has been erased from transfer devices
+ Content is inaccessible in transit

**Common anti-patterns:**
+ Organizations ship unencrypted hard drives containing source content to cloud facilities without chain-of-custody tracking or tamper-evident packaging, leaving content exposed if devices are intercepted.
+ Teams store encryption keys on the same physical device as the encrypted content, negating the protection that encryption provides if the device is lost or stolen.
+ Organizations use consumer-grade storage devices without hardware encryption for content transfer, relying on software-level encryption that can be bypassed with physical access to the drive.
+ Teams fail to verify that data has been securely erased from transfer devices after content ingestion, leaving copies of source content on devices that are returned to third-party logistics providers.
+ Organizations don't validate content integrity after physical transfer, missing corruption or tampering that may have occurred during shipping.

**Benefits of establishing this best practice:**
+ Hardware-encrypted devices with tamper-evident packaging keep content inaccessible if devices are intercepted, lost, or stolen during shipping.
+ Encryption keys managed through AWS Key Management Service (KMS) are never stored on the physical device, so possession of the device alone can't grant access to the content.
+ Tracked shipping with electronic displays showing destination addresses and National Institute of Standards and Technology (NIST)-aligned data erasure after transfer provide auditable evidence of secure handling for content licensors.
+ Petabyte-scale content libraries can be securely transferred without requiring high-bandwidth network connections or extended transfer windows that increase exposure time.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

When working with large content libraries, it's possible that transmitting content over the network isn't feasible. This is especially important to consider if the connectivity between the studio and the video processing infrastructure is non-existent or if the bandwidth requirement to transmit the footage is beyond the available bandwidth the network provider can provide. AWS offers AWS Snowball Edge, a petabyte-scale data transport solution that uses secure appliances to transfer large amounts of data into and out of the AWS Cloud. AWS Snowball Edge encrypts all data with 256-bit encryption. You manage your encryption keys by using AWS Key Management Service (AWS KMS). Your keys are never stored on the device and all memory is erased when it is disconnected and returned to AWS. A user must have access to the customer managed key (AWS KMS key) that is associated with the Snowball Edge device when it was requested to access the data stored in the Snowball Edge device, which reduces concerns of data being intercepted in transit. Snowball Edge devices come with an electronic screen that displays the customer and AWS shipping destination, which minimizes shipping discrepancies. Lastly, after your data has been transferred to AWS, your data is erased from the device using standards defined by National Institute of Standards and Technology.

### Implementation steps
<a name="implementation-steps"></a>

1. **Set up data transfer:** [Set up data to be transferred](https://docs.aws.amazon.com/snowball/latest/developer-guide/how-it-works.html) with AWS Snowball Edge.

1. **Encrypt the data:** Use AWS KMS to encrypt the data.

1. **Upload data to the device:** Upload data to the Snowball Edge device.

1. **Ship the device to AWS:** Ship the device to AWS for data ingestion.

1. **Validate data transfer:** Implement data transfer and content validation process.

1. **Verify secure erasure:** Validate secure data erasure and compliance.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSEC04-BP02 Encrypt content ingest traffic using TLS](smsec04-bp02.html)

**Related documents**
+ [AWS Snowball Edge How It Works](https://docs.aws.amazon.com/snowball/latest/developer-guide/how-it-works.html)

**Related services**
+ [Amazon S3](https://aws.amazon.com/s3/)
+ [AWS Snowball](https://aws.amazon.com/snowball/)
+ [AWS Key Management Service](https://aws.amazon.com/kms/)