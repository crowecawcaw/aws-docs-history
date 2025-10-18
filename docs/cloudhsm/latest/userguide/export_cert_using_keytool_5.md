# Export a certificate from AWS CloudHSM using keytool

The following example generates a certificate in binary X.509 format. To export a human
 readable certificate from AWS CloudHSM, add `-rfc` to the
 `-exportcert` command. 


Linux

```
`$` keytool -exportcert -alias `<key pair label>` \
	-file my_exported_certificate.crt \
	-keystore example_keystore.store \
	-storetype CLOUDHSM \
	-J-classpath '-J/opt/cloudhsm/java/*'

```


Windows

```
`PS C:\>` keytool -exportcert -alias `<key pair label>` `
	-file my_exported_certificate.crt `
	-keystore example_keystore.store `
	-storetype CLOUDHSM `
	-J-classpath '-J"C:\Program Files\Amazon\CloudHSM\java\*"'

```
