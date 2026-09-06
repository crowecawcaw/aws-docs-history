

# Physical Key Exchange
<a name="keys-physicalkeyexchange"></a>

You can use Physical Key Exchange to securely convert paper-based cryptographic key components into electronic format when your partners or vendors do not support electronic key exchange. Trained AWS key custodians perform key ceremonies in PCI PIN and P2PE certified AWS-operated secure facilities, converting paper key components into electronic format using an offline HSM. The service uses ECDH-based key exchange to deliver an ECDH-wrapped TR-31 key block, which you import directly into your AWS Payment Cryptography account. 

**Note**  
We recommend using standards-based [Importing and exporting keys](keys-importexport.md) whenever possible. Use Physical Key Exchange only when your partners or vendors do not support electronic key exchange methods such as [ANSI X9.24 TR-34](terminology.md#terms.tr34), [RSA wrap/unwrap](terminology.md#terms.rsawrap), or [ECDH](terminology.md#terms.ecdh).

## How Physical Key Exchange works
<a name="pke-how-it-works"></a>

To initiate paper key exchange, a [CloudFormation template](https://github.com/aws-samples/samples-for-payment-cryptography-service/tree/main/physical-key-exchange) guides you through the prerequisite setup, including creating an ECC key pair and an S3 bucket in your account. You or your partner then ships paper key components to the AWS secure facility, where trained AWS key custodians perform the key ceremony using an offline HSM. The output is an ECDH-wrapped TR-31 key block uploaded to your S3 bucket, which you import into your account using the [Import keys using asymmetric techniques (ECDH)](keys-import.md#keys-import-ecdh) method. Physical Key Exchange supports importing KEK (key usage K1) or BDK (key usage B0) keys in both TDES and AES key algorithms.

The following diagram shows the end-to-end Physical Key Exchange process.

![Physical Key Exchange process flow](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/images/physical-key-exchange.png)


1. **Initiation** – You submit a support ticket or work with your account manager to submit a request.

1. **Customer setup** – AWS Payment Cryptography provides a CloudFormation template for you to complete the following prerequisite steps:
   + Create an ECC P521 key pair within your AWS Payment Cryptography account and retrieve the public key certificate.
   + Create an Amazon S3 bucket with a policy granting the AWS Payment Cryptography service principal read/write access.
   + Store the ECC public certificate and signing root CA in the Amazon S3 bucket.
   + Provide key attributes: key usage, key modes of use, and number of paper key components to be sent.

1. **Share S3 bucket name** – The customer shares the S3 bucket name created by the CloudFormation stack, where the public key certificate, certificate chain, and key attributes are stored for AWS Payment Cryptography to initiate the key exchange.

1. **Shipping coordination** – AWS Payment Cryptography provides shipping details for the US-based secure facility. You or your partner ships paper key components to the AWS key custodians.

1. **Component receipt** – AWS key custodians receive each paper component and send a separate acknowledgement for each component.

1. **Key ceremony** – AWS key custodians perform the key ceremony using an offline HSM. The resulting TR-31 key block, wrapped using an ECDH-derived AES-256 key, the ECC public certificate from the offline HSM, and its signing certificate are uploaded to your Amazon S3 bucket.

1. **Completion** – AWS Payment Cryptography sends a confirmation that the key ceremony is complete. You can then import the ECDH wrapped TR-31 key block into your AWS Payment Cryptography account using the [Import keys using asymmetric techniques (ECDH)](keys-import.md#keys-import-ecdh) method.

1. **Billing** – You are billed per key exchanged upon successful completion of the key ceremony.

## Security and compliance
<a name="pke-security"></a>

Physical Key Exchange operates in AWS secure facilities designed to meet PCI PIN and PCI P2PE physical and logical security requirements. The following controls are in place:

Dual control and separation of duties  
AWS key custodians are assigned from different teams with separate reporting structures. Processes are in place to ensure key ceremonies steps are carried out under dual control.

Offline HSM  
Key ceremonies are performed using certified PCI PTS HSM-listed hardware security modules that operate offline with no network connectivity. Your key never exists in cleartext outside the HSM boundary.

Cryptographic key delivery  
Key material is transferred from the offline HSM to your AWS Payment Cryptography account using ECDH-based key exchange, ensuring end-to-end cryptographic protection.

Audit and compliance  
AWS has processes in place to meet applicable compliance requirements that are assessed periodically for PCI PIN and P2PE attestations. Review the compliance package in AWS Artifact for reports that you have reference in your own PCI assessments.