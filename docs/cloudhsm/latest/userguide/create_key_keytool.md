# Create new AWS CloudHSM keys with keytool

You can use keytool to generate any type of key supported by the AWS CloudHSM JCE SDK. See a full
list of keys and lengths in the [Supported Keys](java-lib-supported.md#java-keys "java-lib-supported.md#java-keys")
article in the Java Library.

###### Important

A key generated through keytool is generated in software, and then imported
into AWS CloudHSM as an extractable, persistent key.

Instructions for creating non-extractable keys directly on the hardware security module
(HSM), and then using them with keytool or Jarsigner, are shown in the code sample
in [Registering Pre-existing
Keys with AWS CloudHSM Key Store](register-pre-existing-keys-with-keystore.md "register-pre-existing-keys-with-keystore.md"). We strongly recommend generating
non-exportable keys outside of keytool, and then importing corresponding
certificates to the key store. If you use extractable RSA or EC keys through keytool
and jarsigner, the providers export keys from the AWS CloudHSM and then use the key locally
for signing operations.

If you have multiple client instances connected to your CloudHSM cluster, be aware
that importing a certificate on one client instance’s key store won't automatically
make the certificates available on other client instances. To register the key and
associated certificates on each client instance you need to run a Java application
as described in [Generate a CSR using
Keytool](generate_csr_using_keytool.md "generate_csr_using_keytool.md"). Alternatively, you can make the necessary changes on one client
and copy the resulting key store file to every other client instance.

**Example 1:** To generate a symmetric AES-256 key and save it in a key store file named, "example_keystore.store",
in the working directory. Replace `<secret label>` with a unique label.

```
keytool -genseckey -alias `<secret label>` -keyalg aes \
		-keysize 256 -keystore example_keystore.store \
		-storetype CloudHSM -J-classpath '-J/opt/cloudhsm/java/*' \
		-J-Djava.library.path=/opt/cloudhsm/lib/
```

**Example 2:** To generate an RSA 2048 key pair and save it in a key store file named, "example_keystore.store"
in the working directory. Replace `<RSA key pair label>` with a unique label.

```
keytool -genkeypair -alias `<RSA key pair label>` \
        -keyalg rsa -keysize 2048 \
        -sigalg sha512withrsa \
        -keystore example_keystore.store \
        -storetype CLOUDHSM \
        -J-classpath '-J/opt/cloudhsm/java/*' \
        -J-Djava.library.path=/opt/cloudhsm/lib/

```

**Example 3:** To generate a p256 ED key and save it in a key store file named, "example_keystore.store" in the
working directory. Replace `<ec key pair label>` with a unique label.

```
keytool -genkeypair -alias `<ec key pair label>` \
        -keyalg ec -keysize 256 \
        -sigalg SHA512withECDSA \
        -keystore example_keystore.store \
        -storetype CLOUDHSM \
        -J-classpath '-J/opt/cloudhsm/java/*' \
        -J-Djava.library.path=/opt/cloudhsm/lib/

```

You can find a list of [supported signature algorithms](java-lib-supported.md#java-sign-verify "java-lib-supported.md#java-sign-verify") in the Java library.
