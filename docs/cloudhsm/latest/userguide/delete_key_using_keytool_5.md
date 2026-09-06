

# Delete an AWS CloudHSM key using keytool
<a name="delete_key_using_keytool_5"></a>

The AWS CloudHSM key store doesn't support deleting keys. You can delete keys using the destroy method of the [Destroyable interface](https://devdocs.io/openjdk%7E8/javax/security/auth/destroyable#destroy--).

```
((Destroyable) key).destroy();
```