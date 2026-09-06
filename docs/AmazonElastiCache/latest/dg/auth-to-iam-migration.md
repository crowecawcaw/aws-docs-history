

# Migrating from password-based authentication (AUTH) to IAM authentication
<a name="auth-to-iam-migration"></a>

This guide describes how to migrate your Amazon ElastiCache node-based cluster or serverless cache from password-based authentication (AUTH) to AWS Identity and Access Management (IAM) authentication without service interruption.

**Note**  
We recommend testing this migration in a non-production environment before applying changes to your production environment.

## Overview
<a name="auth-to-iam-overview"></a>

IAM authentication provides enhanced security by eliminating the need for long-lived passwords. Instead, applications generate short-lived authentication tokens (valid for up to 15 minutes) using the [AWS Signature Version 4 signing process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).

## Prerequisites
<a name="auth-to-iam-prereqs"></a>

Before you begin, verify the following:
+ Your cache is running Redis OSS 7.0 or later, or Valkey. IAM authentication is not supported on earlier engine versions.
+ In-transit encryption (TLS) is enabled on your cache. IAM authentication requires TLS. For more information, see [ElastiCache in-transit encryption (TLS)](in-transit-encryption.md).
+ You have the necessary IAM permissions to create users and modify user groups. For more information, see [How Amazon ElastiCache works with IAM](security_iam_service-with-iam.md).
+ The IAM role or user that your application uses has an IAM policy that allows the `elasticache:Connect` action for the target cache and IAM user. For more information, see [Authenticating with IAM](auth-iam.md).
+ No additional IAM authentication limitations apply to your application. For the full list of limitations, see [Authenticating with IAM](auth-iam.md).

## Migration process
<a name="auth-to-iam-process"></a>

The migration process involves creating both a password-based and an IAM-authenticated user, verifying connectivity, and then transitioning your applications to IAM authentication.

### Step 1: Create users
<a name="auth-to-iam-create-users"></a>

Create two ElastiCache users so that your cache supports both password-based and IAM authentication during the migration period.

**Create a password-based authentication user**

**Note**  
If you already have a password-based user configured, you can skip creating a new one and use your existing user.

Use the following AWS CLI command to create a password-based user.

For Linux, macOS, or Unix:

```
aws elasticache create-user \
  --user-id {{<user-id>}} \
  --user-name default \
  --engine {{<engine>}} \
  --passwords "{{<your-existing-auth-password>}}" \
  --access-string "on ~* +@all"
```

For Windows:

```
aws elasticache create-user ^
  --user-id {{<user-id>}} ^
  --user-name default ^
  --engine {{<engine>}} ^
  --passwords "{{<your-existing-auth-password>}}" ^
  --access-string "on ~* +@all"
```

Replace:
+ {{<user-id>}} – A unique ID for this user.
+ {{<engine>}} – The engine your cache uses: `valkey` or `redis`.
+ {{<your-existing-auth-password>}} – The AUTH token currently configured on your cache.

**Create an IAM-authenticated user**

Use the following AWS CLI command to create an IAM-authenticated user.

For Linux, macOS, or Unix:

```
aws elasticache create-user \
  --user-id {{<iam-user-id>}} \
  --user-name {{<iam-user-name>}} \
  --authentication-mode Type=iam \
  --engine {{<engine>}} \
  --access-string "on ~* +@all"
```

For Windows:

```
aws elasticache create-user ^
  --user-id {{<iam-user-id>}} ^
  --user-name {{<iam-user-name>}} ^
  --authentication-mode Type=iam ^
  --engine {{<engine>}} ^
  --access-string "on ~* +@all"
```

Replace:
+ {{<iam-user-id>}} – A unique ID for the IAM user.
+ {{<iam-user-name>}} – The username for the IAM user.
+ {{<engine>}} – The engine your cache uses: `valkey` or `redis`.

### Step 2: Create and attach user group
<a name="auth-to-iam-user-group"></a>

If you already have a user group containing your password-based user, add the IAM-authenticated user to that existing group:

For Linux, macOS, or Unix:

```
aws elasticache modify-user-group \
  --user-group-id {{<user-group-id>}} \
  --user-ids-to-add {{<iam-user-id>}}
```

For Windows:

```
aws elasticache modify-user-group ^
  --user-group-id {{<user-group-id>}} ^
  --user-ids-to-add {{<iam-user-id>}}
```

Replace:
+ {{<user-group-id>}} – The ID of your existing user group.
+ {{<iam-user-id>}} – The user ID of the IAM-authenticated user created in Step 1.

Then skip to [Step 3: Verify both authentication methods](#auth-to-iam-verify-dual).

Otherwise, create a new user group, add both users, and attach the group to your cache.

Use the following AWS CLI commands to create a user group with both users:

For Linux, macOS, or Unix:

```
aws elasticache create-user-group \
  --user-group-id {{<user-group-id>}} \
  --engine {{<engine>}} \
  --user-ids {{<user-id>}} {{<iam-user-id>}}
```

For Windows:

```
aws elasticache create-user-group ^
  --user-group-id {{<user-group-id>}} ^
  --engine {{<engine>}} ^
  --user-ids {{<user-id>}} {{<iam-user-id>}}
```

Replace:
+ {{<user-group-id>}} – A unique ID for the user group.
+ {{<engine>}} – The engine your cache uses: `valkey` or `redis`.
+ {{<user-id>}}, {{<iam-user-id>}} – The user IDs created in Step 1.

Then modify your cache to use the new user group.

For node-based clusters:

For Linux, macOS, or Unix:

```
aws elasticache modify-replication-group \
  --replication-group-id {{<replication-group-id>}} \
  --auth-token-update-strategy DELETE \
  --user-group-ids-to-add {{<user-group-id>}}
```

For Windows:

```
aws elasticache modify-replication-group ^
  --replication-group-id {{<replication-group-id>}} ^
  --auth-token-update-strategy DELETE ^
  --user-group-ids-to-add {{<user-group-id>}}
```

Replace:
+ {{<replication-group-id>}} – The ID of your replication group.
+ {{<user-group-id>}} – The user group ID you created above.

For serverless caches:

For Linux, macOS, or Unix:

```
aws elasticache modify-serverless-cache \
  --serverless-cache-name {{<serverless-cache-name>}} \
  --user-group-id {{<user-group-id>}}
```

For Windows:

```
aws elasticache modify-serverless-cache ^
  --serverless-cache-name {{<serverless-cache-name>}} ^
  --user-group-id {{<user-group-id>}}
```

Replace:
+ {{<serverless-cache-name>}} – The name of your serverless cache.
+ {{<user-group-id>}} – The user group ID you created above.

### Step 3: Verify both authentication methods
<a name="auth-to-iam-verify-dual"></a>

After completing Step 2, your cache supports both authentication methods. Verify that applications can connect using both methods before proceeding.
+ Applications using password-based authentication can continue connecting with the password.
+ Applications configured for IAM authentication can connect using IAM tokens.

### Step 4: Connect with IAM
<a name="auth-to-iam-connect"></a>

**Generate an IAM authentication token**

Generate a short-lived IAM authentication token using an [AWS SigV4 pre-signed request](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html). The following Python example demonstrates token generation.

```
import boto3
from botocore.auth import SigV4QueryAuth
from botocore.awsrequest import AWSRequest

cache_name = "<cache-name>"
user = "<username>"
region = "<region>"
expires = 900

session = boto3.Session()
credentials = session.get_credentials().get_frozen_credentials()

req = AWSRequest(
    method="GET",
    url=f"http://{cache_name}/",
    params={"Action": "connect", "User": user}
)
SigV4QueryAuth(credentials, "elasticache", region, expires=expires).add_auth(req)

token = req.url.replace("http://", "")
print(token)
```

**Note**  
The generated token is valid for up to 15 minutes from creation.

**Connect using valkey-cli**

Connect to your ElastiCache cache using the generated token. You can use either **valkey-cli** or **redis-cli** to connect to Valkey clusters. For Redis OSS clusters, use **redis-cli**.

```
valkey-cli -h {{<host>}} -p 6379 --tls
```

For cluster mode enabled clusters, add the `--cluster` flag:

```
valkey-cli -h {{<host>}} -p 6379 --tls --cluster
```

Then authenticate with the following command:

```
AUTH {{<username>}} {{<token>}}
```

Replace:
+ {{<host>}} – The endpoint of your cache.
+ {{<username>}} – The username of the IAM-authenticated user.
+ {{<token>}} – The IAM authentication token you generated.

Expected output:

```
OK
```

Run the following command to validate the username:

```
ACL WHOAMI
```

### Step 5: Application integration
<a name="auth-to-iam-app-integration"></a>

For Java applications, use the default AWS Credentials provider chain to generate temporary security credentials. For more information, see [Authenticating with IAM](auth-iam.md). For other languages, generate the IAM authentication token using the [AWS Signature Version 4 signing process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) and pass it as the password in your client's `AUTH` command.

## Completing the migration
<a name="auth-to-iam-completing"></a>

After your applications can connect using IAM authentication, complete the following steps to finalize the migration.

### Step 1: Configure IAM authentication with fallback
<a name="auth-to-iam-fallback"></a>

Before removing the password-based user, update your application code to use IAM authentication as the primary method while keeping the password-based user as a fallback.

In your application code:
+ Configure your client to authenticate using IAM-generated tokens as the primary method.
+ Add a fallback mechanism so that if IAM authentication fails (for example, due to token expiry or a generation error), the client retries using the password-based AUTH credential.
+ Log all authentication attempts, including fallbacks and retries, so you can monitor whether any connections are falling back to password-based auth.

### Step 2: Monitor and verify
<a name="auth-to-iam-monitor"></a>

Review your application logs and the `IamAuthenticationExpirations` and `IamAuthenticationThrottling` Amazon CloudWatch metrics over at least 24–48 hours to confirm all connections are through IAM.

A non-zero value for either metric warrants investigation:
+ `IamAuthenticationExpirations` – An IAM authenticated connection is automatically disconnected after 12 hours. The connection can be prolonged by sending an `AUTH` or `HELLO` command with a new IAM authentication token.
+ `IamAuthenticationThrottling` – Indicates too many authentication requests, which might mean your application is generating tokens too aggressively or has connection pooling issues.

For node-based clusters, you can perform additional engine-level checks:
+ `ACL LOG` – Check for failed authentication attempts. Look for entries with `reason=auth`.
+ `CLIENT LIST` – Verify connected users. Check the `user=` field to confirm clients are using the IAM user.

`ACL LOG` and `CLIENT LIST` are available on node-based clusters only. For ElastiCache Serverless deployments, rely on application-side logging and Amazon CloudWatch metrics.

### Step 3: Remove the password-based user
<a name="auth-to-iam-remove-user"></a>

Once you confirm that all applications use IAM authentication, remove the password-based user from the user group.

**Valkey caches**

Remove the password-based user directly:

For Linux, macOS, or Unix:

```
aws elasticache modify-user-group \
   --user-group-id {{<user-group-id>}} \
   --user-ids-to-remove {{<password-user-id>}}
```

For Windows:

```
aws elasticache modify-user-group ^
   --user-group-id {{<user-group-id>}} ^
   --user-ids-to-remove {{<password-user-id>}}
```

**Redis OSS caches**

For Redis OSS caches, the user group must always contain a user with the username `default`. If the password-based user you created in Step 1 has the username `default`, you must create a disabled placeholder user to replace it before removing it:

For Linux, macOS, or Unix:

```
aws elasticache create-user \
   --user-id {{<disabled-default-id>}} \
   --user-name default \
   --engine redis \
   --no-password-required \
   --access-string "off ~* -@all"
```

For Windows:

```
aws elasticache create-user ^
   --user-id {{<disabled-default-id>}} ^
   --user-name default ^
   --engine redis ^
   --no-password-required ^
   --access-string "off ~* -@all"
```

Then add the disabled user to the group and remove the password-based user:

For Linux, macOS, or Unix:

```
aws elasticache modify-user-group \
   --user-group-id {{<user-group-id>}} \
   --user-ids-to-add {{<disabled-default-id>}} \
   --user-ids-to-remove {{<password-user-id>}}
```

For Windows:

```
aws elasticache modify-user-group ^
   --user-group-id {{<user-group-id>}} ^
   --user-ids-to-add {{<disabled-default-id>}} ^
   --user-ids-to-remove {{<password-user-id>}}
```

If the password-based user you created in Step 1 does not have the username `default`, you can remove it directly using the same command shown for Valkey caches above.

Replace:
+ {{<disabled-default-id>}} – A unique ID for the disabled placeholder user (Redis OSS only).
+ {{<user-group-id>}} – The ID of the user group associated with your cache.
+ {{<password-user-id>}} – The user ID of the password-based user to remove.

**Note**  
Do not delete the password-based user after removing it from the user group. Keep it available in case you need to roll back to password-based authentication.

### Step 4: Confirm post-removal
<a name="auth-to-iam-confirm"></a>

After removing the password-based user from the user group, monitor the `AuthenticationFailures` Amazon CloudWatch metric. A sustained value of zero confirms no authentication failures occurring, including any residual password-based attempts. Set a CloudWatch alarm on this metric to detect unexpected attempts.

For node-based clusters, you can also verify using `ACL LOG` and `CLIENT LIST`. For serverless caches, rely on application-side logging and CloudWatch metrics.

## Rollback procedure
<a name="auth-to-iam-rollback"></a>

Re-add the password-based user to the user group, then restore password-based authentication in your application while you investigate.

For Valkey caches:

For Linux, macOS, or Unix:

```
aws elasticache modify-user-group \
   --user-group-id {{<user-group-id>}} \
   --user-ids-to-add {{<password-user-id>}}
```

For Windows:

```
aws elasticache modify-user-group ^
   --user-group-id {{<user-group-id>}} ^
   --user-ids-to-add {{<password-user-id>}}
```

For Redis OSS caches where the password-based user does not have the username `default`, use the same command above.

For Redis OSS caches where you created a disabled placeholder user in [Step 3: Remove the password-based user](#auth-to-iam-remove-user), add the password-based user and remove the disabled placeholder user in a single operation:

For Linux, macOS, or Unix:

```
aws elasticache modify-user-group \
   --user-group-id {{<user-group-id>}} \
   --user-ids-to-add {{<password-user-id>}} \
   --user-ids-to-remove {{<disabled-default-id>}}
```

For Windows:

```
aws elasticache modify-user-group ^
   --user-group-id {{<user-group-id>}} ^
   --user-ids-to-add {{<password-user-id>}} ^
   --user-ids-to-remove {{<disabled-default-id>}}
```

Replace:
+ {{<user-group-id>}} – The ID of the user group associated with your cache.
+ {{<password-user-id>}} – The user ID of the password-based user to re-add.
+ {{<disabled-default-id>}} – The user ID of the disabled placeholder user (Redis OSS only).