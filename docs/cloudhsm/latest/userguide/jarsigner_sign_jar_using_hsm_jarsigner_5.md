# Sign a JAR file using AWS CloudHSM and Jarsigner

## Sign and verify with RSA or ECDSA keys

Use the following command to sign a JAR file using an RSA or ECDSA key with AWS CloudHSM and jarsigner:

Linux;
For OpenJDK 17, OpenJDK 21, and OpenJDK 25

```
jarsigner -keystore example_keystore.store \
	-signedjar signthisclass_signed.jar \
	-sigalg sha512withrsa \
	-storetype CloudHSM \
	-J-classpath '-J/opt/cloudhsm/java/*' \
	-J-Djava.library.path=/opt/cloudhsm/lib \
	signthisclass.jar `<key pair label>`

```

Windows
For OpenJDK 17, OpenJDK 21, and OpenJDK 25

```
jarsigner -keystore example_keystore.store `
	-signedjar signthisclass_signed.jar `
	-sigalg sha512withrsa `
	-storetype CloudHSM `
	-J-classpath '-JC:\Program Files\Amazon\CloudHSM\java\*'`
	 "-J-Djava.library.path='C:\Program Files\Amazon\CloudHSM\lib\'" `
	signthisclass.jar `<key pair label>`

```

Use the following command to verify a signed JAR:

Linux
For OpenJDK 17, OpenJDK 21, and OpenJDK 25

```
jarsigner -verify \
	-keystore example_keystore.store \
	-sigalg sha512withrsa \
	-storetype CloudHSM \
	-J-classpath '-J/opt/cloudhsm/java/*' \
	-J-Djava.library.path=/opt/cloudhsm/lib \
	signthisclass_signed.jar `<key pair label>`

```

Windows
For OpenJDK 17, OpenJDK 21, and OpenJDK 25

```
jarsigner -verify `
	-keystore example_keystore.store `
	-sigalg sha512withrsa `
	-storetype CloudHSM `
	-J-classpath '-JC:\Program Files\Amazon\CloudHSM\java\*'`
	"-J-Djava.library.path='C:\Program Files\Amazon\CloudHSM\lib\'" `
	signthisclass_signed.jar `<key pair label>`

```

## Sign and verify with ML-DSA keys

Use the following command to sign a JAR file using an ML-DSA key with AWS CloudHSM and jarsigner:

Linux
For OpenJDK 26 or later

```
jarsigner -keystore example_keystore.store \
	-signedjar signthisclass_signed.jar \
	-sigalg ML-DSA-44 \
	-storetype CloudHSM \
	-J-classpath '-J/opt/cloudhsm/java/*' \
	-J-Djava.library.path=/opt/cloudhsm/lib \
	signthisclass.jar `<key pair label>`

```

Windows
For OpenJDK 26 or later

```
jarsigner -keystore example_keystore.store `
	-signedjar signthisclass_signed.jar `
	-sigalg ML-DSA-44 `
	-storetype CloudHSM `
	-J-classpath '-JC:\Program Files\Amazon\CloudHSM\java\*'`
	 "-J-Djava.library.path='C:\Program Files\Amazon\CloudHSM\lib\'" `
	signthisclass.jar `<key pair label>`

```

Use the following command to verify a JAR signed with an ML-DSA key:

Linux
For OpenJDK 26 or later

```
jarsigner -verify \
	-keystore example_keystore.store \
	-sigalg ML-DSA-44 \
	-storetype CloudHSM \
	-J-classpath '-J/opt/cloudhsm/java/*' \
	-J-Djava.library.path=/opt/cloudhsm/lib \
	signthisclass_signed.jar `<key pair label>`

```

Windows
For OpenJDK 26 or later

```
jarsigner -verify `
	-keystore example_keystore.store `
	-sigalg ML-DSA-44 `
	-storetype CloudHSM `
	-J-classpath '-JC:\Program Files\Amazon\CloudHSM\java\*'`
	"-J-Djava.library.path='C:\Program Files\Amazon\CloudHSM\lib\'" `
	signthisclass_signed.jar `<key pair label>`

```

## Sign and verify with Ed25519 keys

Use the following command to sign a JAR file using an Ed25519 key with AWS CloudHSM and jarsigner:

Linux
For OpenJDK 17, OpenJDK 21, and OpenJDK 25

```
jarsigner -keystore example_keystore.store \
	-signedjar signthisclass_signed.jar \
	-sigalg Ed25519 \
	-storetype CloudHSM \
	-J-classpath '-J/opt/cloudhsm/java/*' \
	-J-Djava.library.path=/opt/cloudhsm/lib \
	signthisclass.jar `<key pair label>`

```

Windows
For OpenJDK 17, OpenJDK 21, and OpenJDK 25

```
jarsigner -keystore example_keystore.store `
	-signedjar signthisclass_signed.jar `
	-sigalg Ed25519 `
	-storetype CloudHSM `
	-J-classpath '-JC:\Program Files\Amazon\CloudHSM\java\*'`
	 "-J-Djava.library.path='C:\Program Files\Amazon\CloudHSM\lib\'" `
	signthisclass.jar `<key pair label>`

```

Use the following command to verify a JAR signed with an Ed25519 key:

Linux
For OpenJDK 17, OpenJDK 21, and OpenJDK 25

```
jarsigner -verify \
	-keystore example_keystore.store \
	-sigalg Ed25519 \
	-storetype CloudHSM \
	-J-classpath '-J/opt/cloudhsm/java/*' \
	-J-Djava.library.path=/opt/cloudhsm/lib \
	signthisclass_signed.jar `<key pair label>`

```

Windows
For OpenJDK 17, OpenJDK 21, and OpenJDK 25

```
jarsigner -verify `
	-keystore example_keystore.store `
	-sigalg Ed25519 `
	-storetype CloudHSM `
	-J-classpath '-JC:\Program Files\Amazon\CloudHSM\java\*'`
	"-J-Djava.library.path='C:\Program Files\Amazon\CloudHSM\lib\'" `
	signthisclass_signed.jar `<key pair label>`

```
