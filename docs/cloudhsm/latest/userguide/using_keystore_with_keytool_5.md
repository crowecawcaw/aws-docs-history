

# Use AWS CloudHSM key store with keytool using Client SDK 5
<a name="using_keystore_with_keytool_5"></a>

 [ Keytool](https://docs.oracle.com/en/java/javase/25/docs/specs/man/keytool.html) is a popular command line utility for common key and certificate tasks. A complete tutorial on keytool is out of scope for AWS CloudHSM documentation. This article explains the specific parameters you should use with various keytool functions when utilizing AWS CloudHSM as the root of trust through the AWS CloudHSM key store.

When using keytool with the AWS CloudHSM key store, specify the following arguments to any keytool command:

**ML-DSA and keytool**  
Keytool supports ML-DSA in JDK 24 or later.  
The following keytool commands are supported with ML-DSA keys:  
**-certreq** – Generate a certificate signing request for an ML-DSA key.
**-importcert** – Import a certificate for an ML-DSA key.
**-exportcert** – Export a certificate for an ML-DSA key.
The following command is not supported with ML-DSA keys:  
**-genkeypair** – AWS CloudHSM does not support ML-DSA key import, and keytool generates keys in software before importing. Use `KeyPairGenerator` or the CloudHSM CLI to generate ML-DSA key pairs.

------
#### [ Linux ]

```
-storetype CLOUDHSM -J-classpath{{< '-J/opt/cloudhsm/java/*'>}}
```

------
#### [ Windows ]

```
-storetype CLOUDHSM -J-classpath{{<'-J"C:\Program Files\Amazon\CloudHSM\java\*"'>}}
```

------

If you want to create a new key store file using AWS CloudHSM key store, see [Use the AWS CloudHSM KeyStore for AWS CloudHSM Client SDK 3](alternative-keystore.md#using_cloudhsm_keystore). To use an existing key store, specify its name (including path) using the –keystore argument to keytool. If you specify a non-existent key store file in a keytool command, the AWS CloudHSM key store creates a new key store file.