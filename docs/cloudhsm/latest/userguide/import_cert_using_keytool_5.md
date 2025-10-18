# Use keytool to import intermediate and root
 certificates into AWS CloudHSM key store

To import a CA certificate in AWS CloudHSM, you must enable verification of a full certificate
 chain on a newly imported certificate. The following command shows an example. 


Linux

```
`$` keytool -import -trustcacerts -alias rootCAcert \
	-file rootCAcert.cert -keystore example_keystore.store \
	-storetype CLOUDHSM \
	-J-classpath '-J/opt/cloudhsm/java/*'

```


Windows

```
`PS C:\>` keytool -import -trustcacerts -alias rootCAcert `
	-file rootCAcert.cert -keystore example_keystore.store `
	-storetype CLOUDHSM `
	-J-classpath '-J"C:\Program Files\Amazon\CloudHSM\java\*"'

```


If you connect multiple client instances to your AWS CloudHSM cluster, importing a
 certificate on one client instance’s key store won't automatically make the
 certificate available on other client instances. You must import the certificate on
 each client instance.
