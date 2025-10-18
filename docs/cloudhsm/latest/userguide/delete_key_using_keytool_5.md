# Delete an AWS CloudHSM key using keytool

The AWS CloudHSM key store doesn't support deleting keys. You can delete keys using the destroy
 method of the [Destroyable interface](https://devdocs.io/openjdk%7E8/javax/security/auth/destroyable#destroy-- "https://devdocs.io/openjdk%7E8/javax/security/auth/destroyable#destroy--").


```
((Destroyable) key).destroy();
```
