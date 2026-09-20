

# Rotating sign-in credentials
<a name="msk-password-rotation"></a>

Amazon MSK supports password-only rotation, where an associated secret keeps a single username and rotation changes only the password. This corresponds to the Secrets Manager [single-user rotation strategy](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets_strategies.html#rotating-secrets-one-user-one-password). After the updated password propagates to the brokers, new authentication attempts require the new password, and the previous password stops authenticating.

## Changing a username in an associated secret
<a name="msk-password-rotation-username-change"></a>

If the username is changed in a secret that is already associated with a cluster, Amazon MSK loads the new credentials while previously cached credentials might remain available on the brokers. This continued availability is not a supported or guaranteed overlap period for credential rotation.

Amazon MSK does not provide a defined retention period for these cached credentials, so their availability throughout a client transition cannot be relied on. Amazon MSK reads only the `AWSCURRENT` version of an associated secret and does not use `AWSPREVIOUS` as a second active credential. Once a previous credential is removed from the brokers, it cannot be reloaded from Secrets Manager.

## Replacing a username
<a name="msk-password-rotation-replace-username"></a>

To replace a username without the authentication gap caused by disassociating and re-associating the same secret, create a separate secret containing the new username and associate it with the cluster using the [BatchAssociateScramSecret](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-scram-secrets.html#BatchAssociateScramSecret) operation.

Configure the required Kafka ACLs, wait for the new credential to propagate, verify that it works, and migrate your clients. After completing the migration, revoke the previous user's access and disassociate the old secret using the [BatchDisassociateScramSecret](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-scram-secrets.html#BatchDisassociateScramSecret) operation.

This approach keeps both credentials intentionally associated during the transition instead of depending on a previously loaded credential remaining on the brokers.

## Removing retained credentials
<a name="msk-password-rotation-remove-retained-credentials"></a>

You can use the same staged approach to remove credentials retained after a username was changed in a secret that was already associated with a cluster. Associate replacement secrets and migrate your clients before disassociating the affected secrets.

Disassociation will then remove the current and previously retained credentials associated with each old secret without interrupting clients that have migrated to the replacement credentials.