# Use AWS CloudHSM key store with keytool using

Client SDK 3

[Keytool](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/keytool.html "https://docs.oracle.com/javase/8/docs/technotes/tools/unix/keytool.html") is a popular command line utility for common key and certificate
tasks on Linux systems. A complete tutorial on keytool is out of scope for AWS CloudHSM
documentation. This article explains the specific parameters you should use with various
keytool functions when utilizing AWS CloudHSM as the root of trust through the AWS CloudHSM key
store.

When using keytool with the AWS CloudHSM key store, specify the following arguments to any
keytool command:

```
-storetype CLOUDHSM \
		-J-classpath '-J/opt/cloudhsm/java/*' \
		-J-Djava.library.path=/opt/cloudhsm/lib
```

If you want to create a new key store file using AWS CloudHSM key store, see [Use the AWS CloudHSM KeyStore for AWS CloudHSM
Client SDK 3](alternative-keystore.md#using_cloudhsm_keystore "alternative-keystore.md#using_cloudhsm_keystore"). To use an existing key
store, specify its name (including path) using the –keystore argument to keytool. If you
specify a non-existent key store file in a keytool command, the AWS CloudHSM key store creates a
new key store file.
