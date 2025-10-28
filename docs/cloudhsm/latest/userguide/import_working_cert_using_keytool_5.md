# Import a working certificate into

AWS CloudHSM key store using keytool

Once a certificate signing request (CSR) is signed, you can import it into the
AWS CloudHSM key store and associate it with the appropriate key pair. The following
command provides an example.

Linux

```
`$` keytool -importcert -noprompt -alias `<key pair label>` \
	-file my_certificate.crt \
	-keystore example_keystore.store \
	-storetype CLOUDHSM \
	-J-classpath '-J/opt/cloudhsm/java/*'

```

Windows

```
`PS C:\>` keytool -importcert -noprompt -alias `<key pair label>` `
	-file my_certificate.crt `
	-keystore example_keystore.store `
	-storetype CLOUDHSM `
	-J-classpath '-J"C:\Program Files\Amazon\CloudHSM\java\*"'

```

The alias should be a key pair with an associated certificate in the key store. If
the key is generated outside of keytool, or is generated on a different client
instance, you must first import the key and certificate metadata into the key store.

The certificate chain must be verifiable. If you can't verify the certificate, you
might need to import the signing (certificate authority) certificate into the key
store so the chain can be verified.
