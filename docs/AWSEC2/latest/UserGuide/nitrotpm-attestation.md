# Amazon EC2 instance attestation

Attestation is a process that allows you to cryptographically prove to any party that only trusted software,
drivers, and boot processes are running on an Amazon EC2 instance. Amazon EC2 instance attestation is powered by the Nitro
Trusted Platform Module (NitroTPM) and _Attestable AMIs_.

The first step to attestation is to **build an Attestable AMI** and determine the
_reference measurements_ of that AMI. An Attestable AMI is an AMI built from the ground up for attestation. The
reference measurements are measurements of all of your software and configurations that you have included in your AMI. For
more information about how you can obtain the reference measurements, see [Build the sample image description](build-sample-ami.md "build-sample-ami.md").

![Generating a reference measurements with Attestable AMIs.](images/attestable-ami.PNG)
The next step is to launch a [Nitro-TPM enabled EC2 instance](enable-nitrotpm-prerequisites.md#nitrotpm-instancetypes "enable-nitrotpm-prerequisites.md#nitrotpm-instancetypes")
with the Attestable AMI. After you have launched the instance, you can use the [NitroTPM tools](attestation-get-doc.md "attestation-get-doc.md") to generate the _Attestation Document_. Then you can compare the actual measurements
of your EC2 instance from the Attestation Document against the reference measurements to check if the instance has the software and
configurations that you trust.

By comparing the reference measurements generated during the Attestable AMI creation process with the measurements included
in an instance's Attestation Document, you can validate that only software and code that you trust are running on the instance.

![Generating a Attestation Document.](images/attestation-document.PNG)

## Integration with AWS KMS

To make the process of comparing measurements easier, you can use AWS Key Management Service (AWS KMS) as a verifier for
Attestation Documents. With AWS KMS, you can create attestation-based KMS key policies that allow specific operations with the
KMS key only if you provide an Attestation Document with measurements that match the reference measurements. To do this, you
add specific condition keys to your KMS key policies that use the reference measurements as the condition key values,
and then specify which KMS operations are allowed if the condition key is satisfied.

When you perform KMS operations using the KMS key, you must attach an Attestation Document to the KMS request. AWS KMS then
validates the measurements from the Attestation Document against the reference measurements in the KMS key policy, and allows key access
only if the measurements match.

Additionally, when you generate the Attestation Document for an instance, you must specify a public key for a key pair
that you own. The specified public key is included in the Attestation Document. When AWS KMS validates the Attestation Document and allows a
decryption operation, it automatically encrypts the response with the public key included in the Attestation Document before
it is returned. This ensures that the response can be decrypted and used only with the matching private key
for the public key included in the Attestation Document.

This ensures that only instances running trusted software and code can perform cryptographic operations
using a KMS key.

## Attesting isolated compute environments

In general, you can build and configure an EC2 instance to be an **isolated compute
environment**, which provides no interactive access and no mechanism for your administrators and
users to access the data that is being processed in the EC2 instance. With EC2 instance attestation you can
prove to a third-party or service that your instance is running as an isolated compute environment. For more
information, see [Isolate data from your own operators](isolate-data-operators.md "isolate-data-operators.md").

For an example, see the [sample Amazon Linux 2023 image description](build-sample-ami.md "build-sample-ami.md") that creates
an isolated compute environment. You can use this sample image description as a starting point and customize it to meet
your requirements.

## AWS shared responsibility model

NitroTPM and Attestable AMIs are building blocks that can help you to set up and configure attestation on
your EC2 instances. You are responsible for configuring the AMI to meet your respective use case. For more
information, see [AWS Shared
Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/").

###### Topics

- [Attestable AMIs](attestable-ami.md "attestable-ami.md")
- [Prepare AWS KMS for attestation](prepare-attestation-service.md "prepare-attestation-service.md")
- [Get the NitroTPM Attestation Document](attestation-get-doc.md "attestation-get-doc.md")
- [Integrating with AWS KMS](attestation-attest.md "attestation-attest.md")
- [Isolate data from your own operators](isolate-data-operators.md "isolate-data-operators.md")
