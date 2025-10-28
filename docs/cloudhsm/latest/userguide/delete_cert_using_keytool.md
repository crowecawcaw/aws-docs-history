# Use keytool to delete certificates from AWS CloudHSM

key store

The following command shows an example of how to delete an AWS CloudHSM certificate from a Java
keytool key store.

```
keytool -delete -alias mydomain -keystore \
        -keystore example_keystore.store \
        -storetype CLOUDHSM \
        -J-classpath '-J/opt/cloudhsm/java/*' \
        -J-Djava.library.path=/opt/cloudhsm/lib/

```

If you connect multiple client instances to your AWS CloudHSM cluster, deleting a
certificate on one client instance’s key store won't automatically remove the
certificate from other client instances. You must delete the certificate on each
client instance.
