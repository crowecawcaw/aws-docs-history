# Working with users

**Creating users:** You create users in your secret as
key-value pairs. When you use the **Plaintext** option in the Secrets Manager
console, you should specify sign-in credential data in the following format.

```
{
  "username": "alice",
  "password": "alice-secret"
}
```

**Revoking user access:** To revoke a user's credentials to access a cluster, we
recommend that you first remove or enforce an ACL on the cluster, and then
disassociate the secret. This is because of the following:

- Removing a user does not close existing connections.
- Changes to your secret take up to 10 minutes to propagate.
  For information about using an ACL with Amazon MSK, see [Apache Kafka ACLs](msk-acls.md "msk-acls.md").

For clusters using ZooKeeper mode, we recommend that you restrict access to your ZooKeeper nodes to prevent users from modifying
ACLs. For more information, see [Control access to Apache ZooKeeper nodes in your Amazon MSK cluster](zookeeper-security.md "zookeeper-security.md").
