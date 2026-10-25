

# Source authentication for online migration to ElastiCache Serverless
<a name="migration-to-serverless-auth"></a>

If your source cache requires authentication, ElastiCache needs credentials to connect to it. You store the credentials in AWS Secrets Manager and give ElastiCache the secret's ARN when you prepare the migration. ElastiCache does not accept credentials directly.

If your source cache accepts unauthenticated connections, you can skip the authentication configuration.

## Storing source credentials
<a name="w2aac20c13c35b7"></a>

Store your source cache credentials in a Secrets Manager secret. You can use a secret you already manage, or create one for the migration. If you create the secret from the ElastiCache console as part of setting up the migration, ElastiCache configures its access for you.

In the console, you choose one of three authentication methods:

Use an existing secret  
Choose an existing secret from Secrets Manager.

Create and use a new secret  
ElastiCache will create a secret to store your specified credentials.

None  
Source doesn't require authentication.

When you create and use a new secret, you also choose the AWS KMS key that encrypts it: "Choose an existing customer managed KMS key for the new secret. The KMS key you choose must be configured to grant ElastiCache decrypt access."

The secret's contents depend on how your source authenticates.

If your source authenticates users by name, store a user name and a password in the following format:

```
{"username":"migration_user","password":"your-password"}
```

Where:
+ `migration_user` is the name of the user that ElastiCache connects as on your source. It must be 1-120 characters, with no spaces or other whitespace.
+ `your-password` is that user's password. It must be 16-128 characters and cannot contain the characters `, " / @`.

If your source uses a single password with no user names, store the password on its own:

```
{"password":"your-password"}
```

Where:
+ `your-password` is the password for your source cache. It must be 16-128 characters and can contain only letters, digits, and the characters `! & # $ ^ < > -`.

The prepare step validates the secret's format, whether you created the secret or ElastiCache created it for you. An empty secret, a secret that is not valid JSON, a secret with no `password` field, or a user name or password that does not meet the requirements above each fail with a specific message. If your source password does not meet them, change it on your source before you prepare the migration.

### Granting ElastiCache access to the secret
<a name="w2aac20c13c35b7c31"></a>

ElastiCache reads the secret with its own service credentials, so the secret needs a resource policy. Grant `secretsmanager:GetSecretValue` to the `elasticache.amazonaws.com` service principal.

If the secret is encrypted with a customer managed AWS KMS key, grant that service principal permission to use the key in the key policy.

**Your secret cannot use the default AWS managed key for Secrets Manager.** That key cannot be granted to the ElastiCache service principal, so encrypt the secret with a customer managed key.

If the resource policy or the key policy leaves out the service principal, ElastiCache cannot retrieve the credentials, and the prepare step fails with an access denied message.

The IAM identity that calls `PrepareMigration` also needs `secretsmanager:GetSecretValue` on the secret, and `kms:Decrypt` on the key that encrypts it. ElastiCache first reads the secret with your credentials to confirm that you have access, and then with its own service credentials. If either read is denied, the prepare step fails with the same access denied message, so check both your own permissions and the secret's resource and key policies.

## Permissions for the migration user
<a name="w2aac20c13c35b9"></a>

The credentials you store decide which user ElastiCache connects as. What that user is allowed to do on your source determines whether the migration can finish.

If your source uses a single password and no user names, ElastiCache connects with that password and there is nothing further to configure.

If your source authenticates users by name and controls what each one can do, create a user for the migration and grant it the following permissions. Run this command against every node in your source, or use whatever mechanism your source has for applying access control across the cluster:

```
valkey-cli ACL SETUSER migration_user on '>your-password' -@all \
  +ping +info +hello \
  +cluster|nodes +cluster|shards +cluster|slots +cluster|info \
  +acl|list +acl|dryrun \
  +psync +sync +replconf \
  +multi +exec +client|pause +client|kill +client|unpause
```

This block applies as written to every source version that supports ACLs: Redis OSS 6.0 and later, and all supported Valkey versions.

Where:
+ `-@all` removes every command, and the commands added after it are the only ones this user can run. The user cannot write to your source and cannot change your source's access control configuration.
+ `+ping`, `+info`, `+hello`, and the `+cluster` commands let ElastiCache connect to your source and discover its topology.
+ `+acl|list` lets ElastiCache read your source's access control configuration. It does not allow changes to it.
+ `+acl|dryrun` lets ElastiCache verify the rest of these grants during the prepare step without running the commands, on Redis OSS 7.0 and later and on Valkey. Redis OSS 6.0 and 6.2 accept the grant, and ElastiCache does not use it there.
+ `+psync`, `+sync`, and `+replconf` are the replication commands ElastiCache uses to synchronize your data.
+ `+multi`, `+exec`, `+client|pause`, `+client|kill`, and `+client|unpause` are required. ElastiCache uses these commands to run the cutover and validates them when you prepare the migration, except `+client|unpause` on Redis OSS 6.0 and 6.2.

Your application's own users must exist on both your source and your target. During a migration, client authentication commands are forwarded to your source. After cutover, your target answers them. If your source and your target do not have a consistent ACL configuration, your application can encounter authentication errors during the migration.

ElastiCache verifies these grants when you prepare the migration and again when you start the data sync, and a missing grant fails that step. The failure event might not name the missing permission. It can report instead that ElastiCache is unable to connect to your source, so if your source is reachable, check the migration user's grants against this list. After you prepare the migration, do not change or remove the migration user or its permissions. Doing so during a migration can cause data loss or make your cache unavailable.

## Providing the secret when you prepare a migration
<a name="w2aac20c13c35c11"></a>

Pass the secret ARN in the source authentication configuration:

```
aws elasticache prepare-migration \
    --serverless-cache-name {{my-cache}} \
    --customer-node-endpoint-list "Address='{{10.0.0.10}}',Port={{6379}}" \
    --source-authentication-configuration \
        SecretManagerConfig={SecretArn={{arn:aws:secretsmanager:region:account:secret:my-secret}}}
```

Where:
+ `my-cache` is the name of the ElastiCache Serverless cache you are migrating into.
+ `10.0.0.10` and `6379` are the private address and port of one node in your source cache. ElastiCache discovers the rest of your topology from this node.
+ `arn:aws:secretsmanager:region:account:secret:my-secret` is the ARN of the secret that holds your source credentials.

ElastiCache validates connectivity and credentials during the prepare step. If it cannot connect, the prepare step fails. ElastiCache reports a failure event on the cache that names the reason. The migration is rolled back, so the `Migration` object is removed and your cache returns to `available`. Correct the address, the network configuration, or the secret access, then try again.

## Encryption in transit
<a name="w2aac20c13c35c13"></a>

If your source cache requires TLS, set `SourceTlsMode` to `verify-ca` in the `SourceTlsConfiguration` parameter when you prepare the migration, and pass your CA certificates in `SourceTlsCertificate`.

Provide the PEM-encoded CA certificates that issued your source's server certificate. Provide them whether a public or private certificate authority issued your source's certificate, or the certificate is self-signed. If you omit them, the migration fails.

To find the cause of that failure, read the events on your target cache. The failure might not identify the certificate authority as the reason.

The prepare step validates the certificate value. It fails if the value is not a valid PEM-encoded X.509 certificate, is longer than 5,000 characters, contains a private key, or holds a certificate that is expired or not yet valid. The 5,000 character limit counts the whole value, including the BEGIN and END lines and the line breaks, so a chain of several certificates can exceed it.

ElastiCache verifies that your source's server certificate chains to a CA certificate you provided. It does not check the host name in the certificate, so your source address can be an IP address or a host name.

```
aws elasticache prepare-migration \
    --serverless-cache-name {{my-cache}} \
    --customer-node-endpoint-list "Address='{{10.0.0.10}}',Port={{6379}}" \
    --source-tls-configuration SourceTlsMode=verify-ca,SourceTlsCertificate="$(cat {{ca.pem}})"
```

Where:
+ `ca.pem` is a file that holds your PEM-encoded CA certificates. The file must contain only the PEM certificate blocks, with no other text.

If your source also requires authentication, add the `--source-authentication-configuration` parameter shown earlier on this page.

If your source accepts unencrypted connections, set `SourceTlsMode` to `none`. Provide a certificate only with `verify-ca`. A certificate with `none`, or with no TLS mode set, fails the prepare step.

## Related topics
<a name="w2aac20c13c35c15"></a>
+ [Prerequisites for online migration to ElastiCache Serverless](migration-to-serverless-prerequisites.md)
+ [Online migration to ElastiCache Serverless](migration-to-serverless.md)
+ [Migrate your data to ElastiCache Serverless](migration-to-serverless-procedure.md)
+ [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md)