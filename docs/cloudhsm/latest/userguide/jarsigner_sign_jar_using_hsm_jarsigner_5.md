# Sign a JAR file using

AWS CloudHSM and Jarsigner

Use the following command to sign a JAR file using AWS CloudHSM and Jarsigner:

Linux;
For OpenJDK 8

```
jarsigner -keystore example_keystore.store \
	-signedjar signthisclass_signed.jar \
	-sigalg sha512withrsa \
	-storetype CloudHSM \
	-J-classpath '-J/opt/cloudhsm/java/*:/usr/lib/jvm/java-1.8.0/lib/tools.jar' \
	-J-Djava.library.path=/opt/cloudhsm/lib \
	signthisclass.jar `<key pair label>`

```

For OpenJDK 11, OpenJDK 17, and OpenJDK 21

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
For OpenJDK8

```
jarsigner -keystore example_keystore.store `
	-signedjar signthisclass_signed.jar `
	-sigalg sha512withrsa `
	-storetype CloudHSM `
	-J-classpath '-JC:\Program Files\Amazon\CloudHSM\java\*;C:\Program Files\Java\jdk1.8.0_331\lib\tools.jar' `
	 "-J-Djava.library.path='C:\Program Files\Amazon\CloudHSM\lib\'" `
	signthisclass.jar `<key pair label>`

```

For OpenJDK 11, OpenJDK 17, and OpenJDK 21

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
For OpenJDK8

```
jarsigner -verify \
	-keystore example_keystore.store \
	-sigalg sha512withrsa \
	-storetype CloudHSM \
	-J-classpath '-J/opt/cloudhsm/java/*:/usr/lib/jvm/java-1.8.0/lib/tools.jar' \
	-J-Djava.library.path=/opt/cloudhsm/lib \
	signthisclass_signed.jar `<key pair label>`

```

For OpenJDK 11, OpenJDK 17, and OpenJDK 21

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
For OpenJDK 8

```
jarsigner -verify `
	-keystore example_keystore.store `
	-sigalg sha512withrsa `
	-storetype CloudHSM `
	-J-classpath '-JC:\Program Files\Amazon\CloudHSM\java\*;C:\Program Files\Java\jdk1.8.0_331\lib\tools.jar' `
	"-J-Djava.library.path='C:\Program Files\Amazon\CloudHSM\lib\'" `
	signthisclass_signed.jar `<key pair label>`

```

For OpenJDK 11, OpenJDK 17, and OpenJDK 21

```
jarsigner -verify `
	-keystore example_keystore.store `
	-sigalg sha512withrsa `
	-storetype CloudHSM `
	-J-classpath '-JC:\Program Files\Amazon\CloudHSM\java\*`
	"-J-Djava.library.path='C:\Program Files\Amazon\CloudHSM\lib\'" `
	signthisclass_signed.jar `<key pair label>`

```
