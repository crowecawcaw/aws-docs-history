

# Migrating existing secrets
<a name="mes-migrating"></a>

You have an option to migrate your existing partner secrets to managed external secrets. This can be done with an [UpdateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_UpdateSecret.html) call. You must update the secret value and metadata as mentioned in the guide. If you already have custom rotation logic set up for these secrets, you must first cancel the rotation using a [CancelRotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CancelRotateSecret.html) call.