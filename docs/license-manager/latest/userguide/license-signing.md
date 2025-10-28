# Cryptographic signing of licenses in License Manager

License Manager can cryptographically sign licenses issued by an ISV or through AWS Marketplace on
behalf of an ISV. Signing permits vendors to validate the integrity and origin of a
license within the application itself, even in an offline environment.

To sign licenses, License Manager uses an asymmetric AWS KMS key belonging to an
ISV and protected in AWS Key Management Service (AWS KMS). This customer managed CMK consists of a
mathematically related public key and private key pair. When a user requests a license,
License Manager generates a JSON object listing the license entitlements, and signs this object
with the private key. The signature and the plaintext JSON object are returned to the
user. Any party presented with these objects can use the public key to validate that the
text of the license has not been altered and that the license was signed by the owner of
the private key. The private part of the key pair never leaves AWS KMS. For more
information about asymmetric cryptography in AWS KMS, see [Using symmetric and asymmetric keys](symmetric-asymmetric.md "symmetric-asymmetric.md").

###### Note

License Manager calls the AWS KMS [`Sign`](../../../kms/latest/APIReference/API_Sign.md "../../../kms/latest/APIReference/API_Sign.md") and [`Verify`](../../../kms/latest/APIReference/API_Verify.md "../../../kms/latest/APIReference/API_Verify.md") API operations when signing and verifying
licenses. The CMK must have a key usage value of [SIGN_VERIFY](../../../kms/latest/developerguide/concepts.md#key-usage "../../../kms/latest/developerguide/concepts.md#key-usage") for it to be used
by these operations. This variety of CMK cannot be used for encryption and
decryption.

The following workflow describes the issuance of cryptographically signed
licenses:

1. In the AWS KMS console, API, or SDK, the license administrator creates an
   asymmetric customer managed CMK. The CMK must have a key usage of sign and
   verify, and support the RSASSA-PSS SHA-256 signing algorithm. For more
   information, see [Creating
   asymmetric CMKs](../../../kms/latest/developerguide/create-keys.md#create-asymmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-asymmetric-cmk") and [How to choose your CMK
   configuration](../../../kms/latest/developerguide/symm-asymm-choose.md "../../../kms/latest/developerguide/symm-asymm-choose.md").
2. In License Manager, the license administrator creates a consumption configuration that
   includes an AWS KMS ARN or ID. The configuration may specify either or both the
   **Borrow** and **Provisional** options.
   For more information, see [Creating a block of seller issued licenses](create-vended-license.md "create-vended-license.md").
3. An end-user obtains the license using the [`CheckoutLicense`](../APIReference/API_CheckoutLicense.md "../APIReference/API_CheckoutLicense.md") or [`CheckoutBorrowLicense`](../APIReference/API_CheckoutBorrowLicense.md "../APIReference/API_CheckoutBorrowLicense.md") API operation. The
   `CheckoutBorrowLicense` operation is allowed only on licenses
   with **Borrow** configured. It returns a digital signature as
   part of its response along with the JSON object listing entitlements. The
   plaintext JSON resembles the following:

```
{
   "entitlementsAllowed":[
      {
         "name":"EntitlementCount",
         "unit":"Count",
         "value":"1"
      }
   ],
   "expiration":"2020-12-01T00:47:35",
   "issuedAt":"2020-11-30T23:47:35",
   "licenseArn":"arn:aws:license-manager::123456789012:license:l-6585590917ad46858328ff02dEXAMPLE",
   "licenseConsumptionToken":"306eb19afd354ba79c3687b9bEXAMPLE",
   "nodeId":"100.20.15.10",
   "checkoutMetadata":{
      "Mac":"ABCDEFGHI"
   }
}
```
