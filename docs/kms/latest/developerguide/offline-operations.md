# Example offline operations

After [downloading the public key](download-public-key.md "download-public-key.md") of your
asymmetric KMS key pair, you can share it with others and use it to perform offline
operations.

AWS CloudTrail logs that record every AWS KMS operation, including the request, response, date,
time, and authorized user, do not record the use of the public key outside of AWS KMS.

This topic provides example offline operations and details the tools AWS KMS provides to
make offline operations easier.

###### Topics

- [Deriving shared secrets offline](#key-spec-ecc-offline "#key-spec-ecc-offline")
- [Offline verification with ML-DSA key
  pairs](#mldsa-offline-verification "#mldsa-offline-verification")
- [Offline verification with SM2 key pairs
  (China Regions only)](#key-spec-sm-offline-verification "#key-spec-sm-offline-verification")

## Deriving shared secrets offline

You can [download the public key](download-public-key.md "download-public-key.md") of your ECC
key pair for use in offline operations, that is, operations outside of AWS KMS.

The following [OpenSSL](https://openssl.org/ "https://openssl.org/") walkthrough demonstrates
one method of deriving a shared secret outside of AWS KMS using the public key of an ECC
KMS key pair and a private key created with OpenSSL.

1. Create an ECC key pair in OpenSSL and prepare it for use with AWS KMS.

```
// Create an ECC key pair in OpenSSL and save the private key in openssl_ecc_key_priv.pem
export OPENSSL_CURVE_NAME="P-256"
export KMS_CURVE_NAME="ECC_NIST_P256"

export OPENSSL_KEY1_PRIV_PEM="openssl_ecc_key1_priv.pem"
openssl ecparam -name ${OPENSSL_CURVE_NAME} -genkey -out ${OPENSSL_KEY1_PRIV_PEM}

// Derive the public key from the private key
export OPENSSL_KEY1_PUB_PEM="openssl_ecc_key1_pub.pem"
openssl ec -in ${OPENSSL_KEY1_PRIV_PEM} -pubout -outform pem \
    -out ${OPENSSL_KEY1_PUB_PEM}

// View the PEM file containing the public key and extract the public key as a
// Base64 encoded string into OPENSSL_KEY1_PUB_BASE64 for use with AWS KMS
export OPENSSL_KEY1_PUB_BASE64=`cat ${OPENSSL_KEY1_PUB_PEM} | \
    tee /dev/stderr | grep -v "PUBLIC KEY" | tr -d "\n"`
```

2. Create an ECC key agreement key pair in AWS KMS and prepare it for use with
   OpenSSL.

```
// Create a KMS key on the same curve as the key pair from step 1
// with a key usage of KEY_AGREEMENT
// Save its ARN in KMS_KEY1_ARN.
export KMS_KEY1_ARN=`aws kms create-key --key-spec ${KMS_CURVE_NAME} \
    --key-usage KEY_AGREEMENT | tee /dev/stderr | jq -r .KeyMetadata.Arn`

// Download the public key and save the Base64-encoded version in KMS_KEY1_PUB_BASE64
export KMS_KEY1_PUB_BASE64=`aws kms get-public-key --key-id ${KMS_KEY1_ARN} | \
    tee /dev/stderr | jq -r .PublicKey`

// Create a PEM file for the public KMS key for use with OpenSSL
export KMS_KEY1_PUB_PEM="aws_kms_ecdh_key1_pub.pem"
echo "-----BEGIN PUBLIC KEY-----" > ${KMS_KEY1_PUB_PEM}
echo ${KMS_KEY1_PUB_BASE64} | fold -w 64 >> ${KMS_KEY1_PUB_PEM}
echo "-----END PUBLIC KEY-----" >> ${KMS_KEY1_PUB_PEM}
```

3. Derive shared secret in OpenSSL using the private key in OpenSSL and the public
   KMS key.

```
export OPENSSL_SHARED_SECRET1_BIN="openssl_shared_secret1.bin"
openssl pkeyutl -derive -inkey ${OPENSSL_KEY1_PRIV_PEM} \
    -peerkey ${KMS_KEY1_PUB_PEM} -out ${OPENSSL_SHARED_SECRET1_BIN}
```

[Show moreShow less](# "#")

## Offline verification with ML-DSA key

pairs

AWS KMS supports a hedged variant of ML-DSA signing, as described in [Federal Information Processing Standards
(FIPS) 204 standard](https://csrc.nist.gov/pubs/fips/204/final "https://csrc.nist.gov/pubs/fips/204/final") section 3.4 for messages up to 4 KB bytes.

To sign messages larger than 4 KB, you perform the message pre-processing step outside
of AWS KMS. This hashing step creates a 64-byte message representative μ, as defined in NIST
FIPS 204, section 6.2.

AWS KMS has a message type called `EXTERNAL_MU` for messages larger than 4 KB.
When you use this instead of the `RAW` message type, AWS KMS:

- Assumes you've already performed the hashing step
- Skips its internal hashing process
- Works with messages of any size

When you verify a message, the method that you use depends on the size restriction of
the external system or library and whether it supports the 64-byte message representative
μ:

- If the message is smaller than the size restriction, use the `RAW`
  message type.
- If the message is larger than the size restriction, use the representative μ in the
  external system.

The following sections demonstrate how to sign messages using AWS KMS and verify messages
using OpenSSL. We provide examples for both messages under and over the 4 KB message size
limit imposed by AWS KMS. OpenSSL doesn't impose a limit on message size for
verification.

For both examples, first get the public key from AWS KMS. Use the following AWS CLI
command:

```
aws kms get-public-key \
    --key-id _<1234abcd-12ab-34cd-56ef-1234567890ab>_ \
    --output text \
    --query PublicKey | base64 --decode > public_key.der
```

### Message size less than

4KB

For messages under 4 KB, use the `RAW` message type with AWS KMS. While you
can use `EXTERNAL_MU`, it isn't necessary for messages within the size
limit.

Use the following AWS CLI command to sign the message:

```
aws kms sign \
    --key-id _<1234abcd-12ab-34cd-56ef-1234567890ab>_ \
    --message '`your message`' \
    --message-type RAW \
    --signing-algorithm ML_DSA_SHAKE_256 \
    --output text \
    --query Signature | base64 --decode > ExampleSignature.bin
```

To verify this message using OpenSSL use the following command:

```
echo -n 'your message' | ./openssl dgst -verify public_key.der -signature ExampleSignature.bin
```

### Message size more than

4KB

To sign messages larger than 4KB, use the `EXTERNAL_MU` message type. When
you use `EXTERNAL_MU`, you pre-hash the message externally to a 64-byte
representative μ as defined in NIST FIPS 204 section 6.2 and pass it to the signing or
verifying operations. Note that this is different from the "Pre-hash MLDSA" or HashML-DSA
defined in NIST FIPS 204 section 5.4.

1. First, construct a message prefix. The prefix contains a domain separator, the
   length of any context, and the context. The default for the domain separator and
   context length is zero.
2. Prepend the message prefix to the message.
3. Use SHAKE256 to hash the public key and prepend it to the result of step 2.
4. Finally, hash the result of step 3 to produce a 64-byte
   `EXTERNAL_MU`.

The following example uses OpenSSL 3.5 to construct the
`EXTERNAL_MU`:

```
{
    openssl asn1parse -inform DER -in public_key.der -strparse 17 -noout -out - 2>/dev/null |
    openssl dgst -provider default -shake256 -xoflen 64 -binary;
    printf '\x00\x00';
    echo -n "your message"
} | openssl dgst -provider default -shake256 -xoflen 64 -binary > mu.bin
```

After you create the `mu.bin` file, call the AWS KMS API with the following
command to sign the message:

```
aws kms sign \
    --key-id _<1234abcd-12ab-34cd-56ef-1234567890ab>_ \
    --message fileb://mu.bin \
    --message-type EXTERNAL_MU \
    --signing-algorithm ML_DSA_SHAKE_256 \
    --output text \
    --query Signature | base64 --decode > ExampleSignature.bin
```

The resulting signature is the same as a `RAW` signature on the original
message. You can use the same OpenSSL 3.5 command to verify the message:

```
echo -n 'your message' | ./openssl dgst -verify public_key.der -signature ExampleSignature.bin
```

## Offline verification with SM2 key pairs

(China Regions only)

To verify a signature outside of AWS KMS with an SM2 public key, you must specify the
distinguishing ID. When you pass a raw message, [`MessageType:RAW`](../APIReference/API_Sign.md#KMS-Sign-request-MessageType "../APIReference/API_Sign.md#KMS-Sign-request-MessageType"), to the [Sign](../APIReference/API_Sign.md "../APIReference/API_Sign.md") API, AWS KMS uses the default distinguishing ID,
`1234567812345678`, defined by OSCCA in GM/T 0009-2012. You cannot specify your
own distinguishing ID within AWS KMS.

However, if you are generating a message digest outside of AWS, you can specify your
own distinguishing ID, then pass the message digest, [`MessageType:DIGEST`](../APIReference/API_Sign.md#API_Sign_RequestSyntax "../APIReference/API_Sign.md#API_Sign_RequestSyntax"), to AWS KMS to sign. To do this, change the
`DEFAULT_DISTINGUISHING_ID` value in the `SM2OfflineOperationHelper`
class. The distinguishing ID you specify can be any string up to 8,192 characters long.
After AWS KMS signs the message digest, you need either the message digest or the message and
the distinguishing ID used to compute the digest to verify it offline.

###### Important

The `SM2OfflineOperationHelper` reference code is designed to be compatible
with [Bouncy
Castle](https://www.bouncycastle.org/documentation/documentation-java/ "https://www.bouncycastle.org/documentation/documentation-java/") version 1.68. For help with other versions, contact [bouncycastle.org](https://www.bouncycastle.org "https://www.bouncycastle.org").

### `SM2OfflineOperationHelper`

class

To help you with offline operations with SM2 keys, the
`SM2OfflineOperationHelper` class for Java has methods that perform the tasks
for you. You can use this helper class as a model for other cryptographic
providers.

Within AWS KMS, the raw ciphertext conversions and SM2DSA message digest calculations
occur automatically. Not all cryptographic providers implement SM2 in the same way. Some
libraries, like [OpenSSL](https://openssl.org/ "https://openssl.org/") versions 1.1.1 and
later, perform these actions automatically. AWS KMS confirmed this behavior in testing with
OpenSSL version 3.0. Use the following `SM2OfflineOperationHelper` class with
libraries, like [Bouncy Castle](https://www.bouncycastle.org/java.html "https://www.bouncycastle.org/java.html"),
that require you to perform these conversions and calculations manually.

The `SM2OfflineOperationHelper` class provides methods for the following
offline operations:

- Message digest calculation

To generate a message digest offline that you can use for offline
verification, or that you can pass to AWS KMS to sign, use the
`calculateSM2Digest` method. The `calculateSM2Digest`
method generates a message digest with the SM3 hashing algorithm. The [GetPublicKey](../APIReference/API_GetPublicKey.md "../APIReference/API_GetPublicKey.md") API returns your
public key in binary format. You must parse the binary key into a Java
PublicKey. Provide the parsed public key with the message. The method
automatically combines your message with the default distinguishing ID,
`1234567812345678`, but you can set your own distinguishing ID by
changing the `DEFAULT_DISTINGUISHING_ID` value.

- Verify

To verify a signature offline, use the `offlineSM2DSAVerify`
method. The `offlineSM2DSAVerify` method uses the message digest
calculated from the specified distinguishing ID, and original message you
provide to verify the digital signature. The [GetPublicKey](../APIReference/API_GetPublicKey.md "../APIReference/API_GetPublicKey.md") API returns your
public key in binary format. You must parse the binary key into a Java
PublicKey. Provide the parsed public key with the original message and the
signature you want to verify. For more details, see [Offline verification with SM2 key
pairs](#key-spec-sm-offline-verification "#key-spec-sm-offline-verification").

- Encrypt

To encrypt plaintext offline, use the `offlineSM2PKEEncrypt`
method. This method ensures the ciphertext is in a format AWS KMS can decrypt. The
`offlineSM2PKEEncrypt` method encrypts the plaintext, and then
converts the raw ciphertext produced by SM2PKE to the ASN.1 format. The [GetPublicKey](../APIReference/API_GetPublicKey.md "../APIReference/API_GetPublicKey.md") API returns your
public key in binary format. You must parse the binary key into a Java
PublicKey. Provide the parsed public key with the plaintext that you want to
encrypt.

If you're unsure whether you need to perform the conversion, use the
following OpenSSL operation to test the format of your ciphertext. If the
operation fails, you need to convert the ciphertext to the ASN.1 format.

```
openssl asn1parse -inform DER -in `ciphertext.der`
```

By default, the `SM2OfflineOperationHelper` class uses the default
distinguishing ID, `1234567812345678`, when generating message digests for
SM2DSA operations.

```
package com.amazon.kms.utils;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import java.io.IOException;
import java.math.BigInteger;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.security.InvalidKeyException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.NoSuchProviderException;
import java.security.PrivateKey;
import java.security.PublicKey;

import org.bouncycastle.crypto.CryptoException;
import org.bouncycastle.jce.interfaces.ECPublicKey;

import java.util.Arrays;

import org.bouncycastle.asn1.ASN1EncodableVector;
import org.bouncycastle.asn1.ASN1Integer;
import org.bouncycastle.asn1.DEROctetString;
import org.bouncycastle.asn1.DERSequence;
import org.bouncycastle.asn1.gm.GMNamedCurves;
import org.bouncycastle.asn1.x9.X9ECParameters;
import org.bouncycastle.crypto.CipherParameters;
import org.bouncycastle.crypto.params.ParametersWithID;
import org.bouncycastle.crypto.params.ParametersWithRandom;
import org.bouncycastle.crypto.signers.SM2Signer;
import org.bouncycastle.jcajce.provider.asymmetric.util.ECUtil;

public class SM2OfflineOperationHelper {
    // You can change the DEFAULT_DISTINGUISHING_ID value to set your own distinguishing ID,
    // the DEFAULT_DISTINGUISHING_ID can be any string up to 8,192 characters long.
    private static final byte[] DEFAULT_DISTINGUISHING_ID = "1234567812345678".getBytes(StandardCharsets.UTF_8);
    private static final X9ECParameters SM2_X9EC_PARAMETERS = GMNamedCurves.getByName("sm2p256v1");

    // ***calculateSM2Digest***
    // Calculate message digest
    public static byte[] calculateSM2Digest(final PublicKey publicKey, final byte[] message) throws
            NoSuchProviderException, NoSuchAlgorithmException {
        final ECPublicKey ecPublicKey = (ECPublicKey) publicKey;

        // Generate SM3 hash of default distinguishing ID, 1234567812345678
        final int entlenA = DEFAULT_DISTINGUISHING_ID.length * 8;
        final byte [] entla = new byte[] { (byte) (entlenA & 0xFF00), (byte) (entlenA & 0x00FF) };
        final byte [] a = SM2_X9EC_PARAMETERS.getCurve().getA().getEncoded();
        final byte [] b = SM2_X9EC_PARAMETERS.getCurve().getB().getEncoded();
        final byte [] xg = SM2_X9EC_PARAMETERS.getG().getXCoord().getEncoded();
        final byte [] yg = SM2_X9EC_PARAMETERS.getG().getYCoord().getEncoded();
        final byte[] xa = ecPublicKey.getQ().getXCoord().getEncoded();
        final byte[] ya = ecPublicKey.getQ().getYCoord().getEncoded();
        final byte[] za = MessageDigest.getInstance("SM3", "BC")
                .digest(ByteBuffer.allocate(entla.length + DEFAULT_DISTINGUISHING_ID.length + a.length + b.length + xg.length + yg.length +
                        xa.length + ya.length).put(entla).put(DEFAULT_DISTINGUISHING_ID).put(a).put(b).put(xg).put(yg).put(xa).put(ya)
                        .array());

        // Combine hashed distinguishing ID with original message to generate final digest
        return MessageDigest.getInstance("SM3", "BC")
                .digest(ByteBuffer.allocate(za.length + message.length).put(za).put(message)
                        .array());
    }

    // ***offlineSM2DSAVerify***
    // Verify digital signature with SM2 public key
    public static boolean offlineSM2DSAVerify(final PublicKey publicKey, final byte [] message,
            final byte [] signature) throws InvalidKeyException {
        final SM2Signer signer = new SM2Signer();
        CipherParameters cipherParameters = ECUtil.generatePublicKeyParameter(publicKey);
        cipherParameters = new ParametersWithID(cipherParameters, DEFAULT_DISTINGUISHING_ID);
        signer.init(false, cipherParameters);
        signer.update(message, 0, message.length);
        return signer.verifySignature(signature);
    }

    // ***offlineSM2PKEEncrypt***
    // Encrypt data with SM2 public key
    public static byte[] offlineSM2PKEEncrypt(final PublicKey publicKey, final byte [] plaintext) throws
            NoSuchPaddingException, NoSuchAlgorithmException, NoSuchProviderException, InvalidKeyException,
            BadPaddingException, IllegalBlockSizeException, IOException {
        final Cipher sm2Cipher = Cipher.getInstance("SM2", "BC");
        sm2Cipher.init(Cipher.ENCRYPT_MODE, publicKey);

        // By default, Bouncy Castle returns raw ciphertext in the c1c2c3 format
        final byte [] cipherText = sm2Cipher.doFinal(plaintext);

        // Convert the raw ciphertext to the ASN.1 format before passing it to AWS KMS
        final ASN1EncodableVector asn1EncodableVector = new ASN1EncodableVector();
        final int coordinateLength = (SM2_X9EC_PARAMETERS.getCurve().getFieldSize() + 7) / 8 * 2 + 1;
        final int sm3HashLength = 32;
        final int xCoordinateInCipherText = 33;
        final int yCoordinateInCipherText = 65;
        byte[] coords = new byte[coordinateLength];
        byte[] sm3Hash = new byte[sm3HashLength];
        byte[] remainingCipherText = new byte[cipherText.length - coordinateLength - sm3HashLength];

        // Split components out of the ciphertext
        System.arraycopy(cipherText, 0, coords, 0, coordinateLength);
        System.arraycopy(cipherText, cipherText.length - sm3HashLength, sm3Hash, 0, sm3HashLength);
        System.arraycopy(cipherText, coordinateLength, remainingCipherText, 0,cipherText.length - coordinateLength - sm3HashLength);

        // Build standard SM2PKE ASN.1 ciphertext vector
        asn1EncodableVector.add(new ASN1Integer(new BigInteger(1, Arrays.copyOfRange(coords, 1, xCoordinateInCipherText))));
        asn1EncodableVector.add(new ASN1Integer(new BigInteger(1, Arrays.copyOfRange(coords, xCoordinateInCipherText, yCoordinateInCipherText))));
        asn1EncodableVector.add(new DEROctetString(sm3Hash));
        asn1EncodableVector.add(new DEROctetString(remainingCipherText));

        return new DERSequence(asn1EncodableVector).getEncoded("DER");
    }
}
```

[Show moreShow less](# "#")
