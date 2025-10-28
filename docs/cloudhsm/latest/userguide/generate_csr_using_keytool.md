# Generate an AWS CloudHSM CSR using keytool

You receive the greatest flexibility in generating a certificate signing request
(CSR) if you use the [OpenSSL Dynamic Engine for AWS CloudHSM Client SDK 5](openssl-library.md "openssl-library.md"). The following command uses keytool to generate a CSR for a key pair with the
alias, `example-key-pair`.

```
keytool -certreq -alias `<key pair label>` \
        -file example_csr.csr \
        -keystore example_keystore.store \
        -storetype CLOUDHSM \
        -J-classpath '-J/opt/cloudhsm/java/*' \
        -J-Djava.library.path=/opt/cloudhsm/lib/

```

###### Note

To use a key pair from keytool, that key pair must have an entry in the
specified key store file. If you want to use a key pair that was generated
outside of keytool, you must import the key and certificate metadata into the
key store. For instructions on importing the keystore data see [Importing Intermediate and root
certificates into AWS CloudHSM Key Store using Keytool](import_cert_using_keytool.md "import_cert_using_keytool.md").
