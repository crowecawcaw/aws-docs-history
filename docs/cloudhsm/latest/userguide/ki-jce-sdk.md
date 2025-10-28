# Known issues for the JCE SDK for AWS CloudHSM

The following issues impact the JCE SDK for AWS CloudHSM.

###### Topics

- [Issue: When working with asymmetric key pairs, you see occupied
  key capacity even when you are not explicitly creating or importing keys](#ki-jce-1 "#ki-jce-1")
- [Issue: The JCE KeyStore is read only](#ki-jce-3 "#ki-jce-3")
- [Issue: Buffers for AES-GCM encryption cannot exceed 16,000 bytes](#ki-jce-4 "#ki-jce-4")
- [Issue: Elliptic-curve Diffie-Hellman (ECDH) key derivation is
  executed partially within the HSM](#ki-jce-5 "#ki-jce-5")
- [Issue: KeyGenerator and KeyAttribute incorrectly interprets key size parameter as number of bytes instead of bits](#ki-jce-6 "#ki-jce-6")
- [Issue: Client SDK 5 throws the warning “An illegal reflective access operation has occurred”](#ki-jce-7 "#ki-jce-7")
- [Issue: JCE session pool is exhausted](#ki-jce-8 "#ki-jce-8")
- [Issue: Client SDK 5 memory leak with getKey operations](#ki-jce-9 "#ki-jce-9")

## Issue: When working with asymmetric key pairs, you see occupied

key capacity even when you are not explicitly creating or importing keys

- **Impact:** This issue can cause your HSMs to unexpectedly run out of key
  space and occurs when your application uses a standard JCE key object for
  crypto operations instead of a `CaviumKey` object. When you use a
  standard JCE key object, `CaviumProvider` implicitly imports that
  key into the HSM as a session key and does not delete this key until the
  application exits. As a result, keys build up while the application is
  running and can cause your HSMs to run out of free key space, thus freezing
  your application.
- **Workaround:** When using the `CaviumSignature`
  class, `CaviumCipher` class, `CaviumMac` class, or the
  `CaviumKeyAgreement` class, you should supply the key as a
  `CaviumKey` instead of a standard JCE key object.

You can manually convert a normal key to a `CaviumKey` using the
[`ImportKey`](https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/KeyUtilitiesRunner.java "https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/KeyUtilitiesRunner.java") class, and can then manually delete the
key after the operation is complete.

- **Resolution status:** We are updating the
  `CaviumProvider` to properly manage implicit imports. The fix
  will be announced on the version history page once available.

## Issue: The JCE KeyStore is read only

- **Impact:** You cannot store an object type that is not
  supported by the HSM in the JCE keystore today. Specifically, you cannot store
  certificates in the keystore. This precludes interoperability with tools like
  jarsigner, which expect to find the certificate in the keystore.
- **Workaround:** You can rework your code to load certificates
  from local files or from an S3 bucket location instead of from the keystore.
- **Resolution status:** You can use AWS CloudHSM keystore to store certificates.

## Issue: Buffers for AES-GCM encryption cannot exceed 16,000 bytes

Multi-part AES-GCM encryption is not supported.

- **Impact:** You cannot use AES-GCM to encrypt data larger than
  16,000 bytes.
- **Workaround:** You can use an alternative mechanism, such as
  AES-CBC, or you can divide your data into pieces and encrypt each piece
  individually. If you divide the data, you must manage the divided ciphertext and its
  decryption. Because FIPS requires that the initialization vector (IV) for AES-GCM be
  generated on the HSM, the IV for each AES-GCM-encrypted piece of data will be
  different.
- **Resolution status:** We are fixing the SDK to fail explicitly
  if the data buffer is too large. We are evaluating alternatives that support larger
  buffers without relying on multi-part encryption. Updates will be announced in the
  AWS CloudHSM forum and on the version history page.

## Issue: Elliptic-curve Diffie-Hellman (ECDH) key derivation is

executed partially within the HSM

Your EC private key remains within the HSM at all times,
but the key derivation process is performed in multiple steps. As a result, intermediate
results from each step are available on the client. An ECDH key derivation sample is
available in the [Java code samples](java-samples_3.md "java-samples_3.md").

- **Impact:** Client SDK 3 adds ECDH functionality to the
  JCE. When you use the `KeyAgreement` class to derive a SecretKey, it is first
  available on the client and is then imported into the HSM. A key handle is then
  returned to your application.
- **Workaround:** If you are implementing SSL/TLS Offload in AWS CloudHSM,
  this limitation may not be an issue. If your application requires your key to remain
  within an FIPS boundary at all times, consider using an alternative protocol that
  does not rely on ECDH key derivation.
- **Resolution status:** SDK 5.16 now supports ECDH with Key Derivation
  which is performed entirely within the HSM.

## Issue: KeyGenerator and KeyAttribute incorrectly interprets key size parameter as number of bytes instead of bits

When generating a key using the `init` function of the [KeyGenerator class](https://docs.oracle.com/javase/8/docs/api/javax/crypto/KeyGenerator.html#init-int- "https://docs.oracle.com/javase/8/docs/api/javax/crypto/KeyGenerator.html#init-int-")
or the `SIZE` attribute of the [AWS CloudHSM KeyAttribute enum](java-lib-attributes_5.md "java-lib-attributes_5.md"), the
API incorrectly expects the argument to be the number of key bytes, when it should instead be the number of key bits.

- **Impact:** Client SDK versions 5.4.0 through 5.4.2 incorrectly expects the key size to be provided to the specified APIs as bytes.
- **Workaround:** Convert the key size from bits to bytes before using the KeyGenerator class or KeyAttribute enum to generate keys using
  the AWS CloudHSM JCE provider if using Client SDK versions 5.4.0 through 5.4.2.
- **Resolution status:** Upgrade your client SDK version to 5.5.0 or later, which includes a fix to correctly expect key sizes in bits when
  using the KeyGenerator class or KeyAttribute enum to generate keys.

## Issue: Client SDK 5 throws the warning “An illegal reflective access operation has occurred”

When using Client SDK 5 with Java 11, CloudHSM throws the following Java warning:

```
`WARNING: An illegal reflective access operation has occurred
WARNING: Illegal reflective access by com.amazonaws.cloudhsm.jce.provider.CloudHsmKeyStore (file:/opt/cloudhsm/java/cloudhsm-jce-5.6.0.jar) to field java.security .KeyStore.keyStoreSpi
WARNING: Please consider reporting this to the maintainers of com.amazonaws.cloudhsm.jce.provider.CloudHsmKeyStore
WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
WARNING: All illegal access operations will be denied in a future release`
```

This issue is fixed in Client SDK version 5.8 and later.

## Issue: JCE session pool is exhausted

**Impact:** You may not be able to perform operations in JCE after seeing the following message:

```
`com.amazonaws.cloudhsm.jce.jni.exception.InternalException: There are too many operations
happening at the same time: Reached max number of sessions in session pool: 1000`
```

**Workarounds:**

- Restart your JCE application if you’re experiencing impact.
- When performing an operation, you may need to complete the JCE operation before losing reference to the operation.

###### Note

Depending on the operation, a completion method may be needed.

| Operation        | Completion method(s)                                                                   |
| ---------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cipher           | `doFinal()` in encrypt or decrypt mode `wrap()` in wrap mode `unwrap()` in unwrap mode |
| KeyAgreement     | `generateSecret()` or `generateSecret(String)`                                         |
| KeyPairGenerator | `generateKeyPair()`, `genKeyPair()`, or `reset()`                                      |
| KeyStore         | No method needed                                                                       |
| MAC              | `doFinal()` or `reset()`                                                               |
| MessageDigest    | `digest()` or `reset()`                                                                |
| SecretKeyFactory | No method needed                                                                       |
| SecureRandom     | No method needed                                                                       |
| Signature        | `sign()` in sign mode `verify()` in verify mode                                        | **Resolution status:** We have resolved this issue in Client SDK 5.9.0 and later. To fix this issue, upgrade your Client SDK to one of these versions. ## Issue: Client SDK 5 memory leak with getKey operations <br>• **Impact:** The API `getKey` operation has a memory leak in JCE in Client SDK versions 5.10.0 and earlier. If you’re using the `getKey` API multiple times in your application, it will lead to increased memory growth and consequently increase the memory footprint in your application. Over time this may cause throttling errors or require the application to be restarted. <br>• **Workaround:** We recommend upgrading to Client SDK 5.11.0. If this can't be done, we recommend not calling the `getKey` API multiple times in your application. Rather, reuse the previously returned key from the prior `getKey` operation as much as possible. <br>• **Resolution status:** Upgrade your client SDK version to 5.11.0 or later, which includes a fix for this issue. |
