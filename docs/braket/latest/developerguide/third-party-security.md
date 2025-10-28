# Security of Amazon Braket Hardware Providers

QPUs on Amazon Braket are hosted by third-party hardware providers. When you run your
quantum task on a QPU, Amazon Braket uses the DeviceARN as an identifier when sending
the circuit to the specified QPU for processing.

If you use Amazon Braket for access to quantum computing hardware operated by one of
the third-party hardware providers, your circuit and its associated data are processed
by hardware providers outside of facilities operated by AWS. Information about the
physical location and AWS Region where each QPU is available can be found in the
**Device Details** section of the Amazon Braket console.

Your content is anonymized. Only the content necessary to process the circuit is sent
to third parties. AWS account information is not transmitted to third parties.

All data is encrypted at rest and in transit. Data is decrypted for processing only.
Amazon Braket third-party providers are not permitted to store or use your content for
purposes other than processing your circuit. Once the circuit completes, the results
are returned to Amazon Braket and stored in your S3 bucket.

The security of Amazon Braket third-party quantum hardware providers is audited
periodically, to ensure that standards of network security, access control, data protection,
and physical security are met.
