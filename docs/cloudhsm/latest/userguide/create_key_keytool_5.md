# Create new AWS CloudHSM keys with keytool

You can use keytool to generate RSA, AES, and DESede type of key supported by the AWS CloudHSM JCE
SDK.

###### Important

A key generated through keytool is generated in software, and then imported
into AWS CloudHSM as an extractable, persistent key.

We strongly recommend generating non-exportable
keys outside of keytool, and then importing corresponding certificates to the key
store. If you use extractable RSA or EC keys through keytool and Jarsigner, the
providers export keys from the AWS CloudHSM and then use the key locally for signing
operations.

If you have multiple client instances connected to your AWS CloudHSM cluster, be aware
that importing a certificate on one client instance’s key store won't automatically
make the certificates available on other client instances. To register the key and
associated certificates on each client instance you need to run a Java application
as described in [Generate an AWS CloudHSM CSR using keytool](generate_csr_using_keytool_5.md "generate_csr_using_keytool_5.md"). Alternatively, you can make the necessary changes on one client
and copy the resulting key store file to every other client instance.

**Example 1:** To generate a symmetric AES-256 key and save it in a key store file named, "example_keystore.store",
in the working directory. Replace `<secret label>` with a unique label.

Linux

```
`$` keytool -genseckey -alias `<secret label>` -keyalg aes \
	-keysize 256 -keystore example_keystore.store \
	-storetype CloudHSM -J-classpath '-J/opt/cloudhsm/java/*' \

```

Windows

```
`PS C:\>` keytool -genseckey -alias `<secret label>` -keyalg aes `
	-keysize 256 -keystore example_keystore.store `
	-storetype CloudHSM -J-classpath '-J"C:\Program Files\Amazon\CloudHSM\java\*"'

```

**Example 2:** To generate an RSA 2048 key pair and save it in a key store file named, "example_keystore.store"
in the working directory. Replace `<RSA key pair label>` with a unique label.

Linux

```
`$` keytool -genkeypair -alias `<RSA key pair label>` \
	-keyalg rsa -keysize 2048 \
	-sigalg sha512withrsa \
	-keystore example_keystore.store \
	-storetype CLOUDHSM \
	-J-classpath '-J/opt/cloudhsm/java/*'

```

Windows

```
`PS C:\>` keytool -genkeypair -alias `<RSA key pair label>` `
	-keyalg rsa -keysize 2048 `
	-sigalg sha512withrsa `
	-keystore example_keystore.store `
	-storetype CLOUDHSM `
	-J-classpath '-J"C:\Program Files\Amazon\CloudHSM\java\*"'

```

You can find a list of [supported signature algorithms](java-lib-supported_5.md#java-sign-verify_5 "java-lib-supported_5.md#java-sign-verify_5") in the Java library.
