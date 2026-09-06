

# Authenticating with IAM
<a name="auth-iam"></a>

**Topics**
+ [Overview](#auth-iam-overview)
+ [Limitations](#auth-iam-limits)
+ [Setup](#auth-iam-setup)
+ [Connecting](#auth-iam-Connecting)

## Overview
<a name="auth-iam-overview"></a>

With IAM Authentication you can authenticate a connection to ElastiCache for Valkey or Redis OSS using AWS IAM identities, when your cache is configured to use Valkey or Redis OSS version 7 or above. This allows you to strengthen your security model and simplify many administrative security tasks. You can also use IAM Authentication to configure fine-grained access control for each individual ElastiCache cache and ElastiCache user, following least-privilege permissions principles. IAM Authentication for ElastiCache works by providing a short-lived IAM authentication token instead of a long-lived ElastiCache user password in the Valkey or Redis OSS `AUTH` or `HELLO` command. For more information about the IAM authentication token, refer to the [Signature Version 4 signing process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the the AWS General Reference Guide and the code example below. 

You can use IAM identities and their associated policies to further restrict Valkey or Redis OSS access. You can also grant access to users from their federated Identity providers directly to Valkey or Redis OSS caches.

To use AWS IAM with ElastiCache, you first need to create an ElastiCache user with authentication mode set to IAM. Then you can create or reuse an IAM identity. The IAM identity needs an associated policy to grant the `elasticache:Connect` action to the ElastiCache cache and ElastiCache user. Once configured, you can create an IAM authentication token using the AWS credentials of the IAM user or role. Finally you need to provide the short-lived IAM authentication token as a password in your Valkey or Redis OSS Client when connecting to your cache. A Valkey or Redis OSS client with support for credentials provider can auto-generate the temporary credentials automatically for each new connection. ElastiCache will perform IAM authentication for connection requests of IAM-enabled ElastiCache users and will validate the connection requests with IAM. 

## Limitations
<a name="auth-iam-limits"></a>

When using IAM authentication, the following limitations apply:
+ IAM authentication is available when using ElastiCache for Valkey 7.2 and above or Redis OSS version 7.0 and above.
+ IAM authentication requires in-transit encryption (TLS) to be enabled on your cache. For more information, see [ElastiCache in-transit encryption (TLS)](in-transit-encryption.md).
+ For IAM-enabled ElastiCache users the username and user id properties must be identical.
+ The IAM authentication token is valid for 15 minutes. If the connection is re-authenticated with an expired token, the authentication request will be rejected. For long-lived connections, we recommend using a Valkey or Redis OSS client that supports a credentials provider interface to automatically generate fresh tokens before expiry.
+ An IAM authenticated connection to ElastiCache for Valkey or Redis OSS will automatically be disconnected after 12 hours. The connection can be prolonged for 12 hours by sending an `AUTH` or `HELLO` command with a new IAM authentication token.
+ IAM re-authentication (`AUTH` or `HELLO` commands) is not supported inside `MULTI`/`EXEC` or Lua script blocks. However, you can run regular data commands inside `MULTI`/`EXEC` blocks on an IAM-authenticated connection.
+ Currently, IAM authentication supports the following global condition context keys:
  + When using IAM authentication with serverless caches, `aws:VpcSourceIp`, `aws:SourceVpc`, `aws:SourceVpce`, `aws:CurrentTime`, `aws:EpochTime`, and `aws:ResourceTag/%s` (from associated serverless caches and users) are supported.
  + When using IAM authentication with replication groups, `aws:SourceIp` and `aws:ResourceTag/%s` (from associated replication groups and users) are supported.

  For more information about global condition context keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the IAM User Guide.

**Note**  
Cache names are converted to lowercase at cache creation time. Ensure authenticating code supplies the cache name in lowercase to avoid authentication errors.

## Setup
<a name="auth-iam-setup"></a>

To setup IAM authentication:

1. Create a cache

   ```
   aws elasticache create-serverless-cache \
     --serverless-cache-name cache-01  \
     --description "ElastiCache IAM auth application" \
     --engine redis
   ```

1. Create an IAM trust policy document, as shown below, for your role that allows your account to assume the new role. Save the policy to a file named *trust-policy.json*.

------
#### [ JSON ]

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "AWS": "arn:aws:iam::{{123456789012}}:role/{{my-application-role}}"
               },
               "Action": "sts:AssumeRole"
           }
       ]
   }
   ```

**Note**  
Replace `{{my-application-role}}` with the IAM role or user that needs to connect to your cache. Use a least-privilege principal rather than the account root to limit which identities can assume this role.

------

1. Create an IAM policy document, as shown below. Save the policy to a file named *policy.json*.

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect" : "Allow",
         "Action" : [
           "elasticache:Connect"
         ],
         "Resource" : [
           "arn:aws:elasticache:us-east-1:123456789012:serverlesscache:cache-01",
           "arn:aws:elasticache:us-east-1:123456789012:user:iam-user-01"
         ]
       }
     ]
   }
   ```

------

1. Create an IAM role.

   ```
   aws iam create-role \
   --role-name "elasticache-iam-auth-app" \
   --assume-role-policy-document file://trust-policy.json
   ```

1. Create the IAM policy.

   ```
   aws iam create-policy \
     --policy-name "elasticache-allow-all" \
     --policy-document file://policy.json
   ```

1. Attach the IAM policy to the role.

   ```
   aws iam attach-role-policy \
    --role-name "elasticache-iam-auth-app" \
    --policy-arn "arn:aws:iam::123456789012:policy/elasticache-allow-all"
   ```

1. Create a new IAM-enabled user.

   ```
   aws elasticache create-user \
     --user-name iam-user-01 \
     --user-id iam-user-01 \
     --authentication-mode Type=iam \
     --engine redis \
     --access-string "on ~* +@all"
   ```

1. Create a user group and attach the user.

   ```
   aws elasticache create-user-group \
     --user-group-id iam-user-group-01 \
     --engine redis \
     --user-ids default iam-user-01
   
   aws elasticache modify-serverless-cache \
     --serverless-cache-name cache-01  \
     --user-group-id iam-user-group-01
   ```

## Connecting
<a name="auth-iam-Connecting"></a>

**Connect with token as password**

You first need to generate the short-lived IAM authentication token using an [AWS SigV4 pre-signed request](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html). After that you provide the IAM authentication token as a password when connecting to a Valkey or Redis OSS cache, as shown in the example below. 

```
String userId = "{{insert user id}}";
String cacheName = "{{insert cache name}}";
boolean isServerless = {{true}};
String region = "{{insert region}}";

// Create a default AWS Credentials provider.
// This will look for AWS credentials defined in environment variables or system properties.
AwsCredentialsProvider awsCredentialsProvider = DefaultCredentialsProvider.create();

// Create an IAM authentication token request and signed it using the AWS credentials.
// The pre-signed request URL is used as an IAM authentication token for ElastiCache with Redis OSS.
IAMAuthTokenRequest iamAuthTokenRequest = new IAMAuthTokenRequest(userId, cacheName, region, isServerless);
String iamAuthToken = iamAuthTokenRequest.toSignedRequestUri(awsCredentialsProvider.resolveCredentials());

// Construct Redis OSS URL with IAM Auth credentials provider
RedisURI redisURI = RedisURI.builder()
    .withHost(host)
    .withPort(port)
    .withSsl(ssl)
    .withAuthentication(userId, iamAuthToken)
    .build();

// Create a new Lettuce Redis OSS client
RedisClient client = RedisClient.create(redisURI);
client.connect();
```

Below is the definition for `IAMAuthTokenRequest`.

```
public class IAMAuthTokenRequest {
    private static final SdkHttpMethod REQUEST_METHOD = SdkHttpMethod.GET;
    private static final String REQUEST_PROTOCOL = "http://";
    private static final String PARAM_ACTION = "Action";
    private static final String PARAM_USER = "User";
    private static final String PARAM_RESOURCE_TYPE = "ResourceType";
    private static final String RESOURCE_TYPE_SERVERLESS_CACHE = "ServerlessCache";
    private static final String ACTION_NAME = "connect";
    private static final String SERVICE_NAME = "elasticache";
    private static final Duration TOKEN_EXPIRY_DURATION = Duration.ofSeconds(900);

    private final String userId;
    private final String cacheName;
    private final String region;
    private final boolean isServerless;

    public IAMAuthTokenRequest(String userId, String cacheName, String region, boolean isServerless) {
        this.userId = userId;
        this.cacheName = cacheName;
        this.region = region;
        this.isServerless = isServerless;
    }

    public String toSignedRequestUri(AwsCredentials credentials) {
        SdkHttpFullRequest request = getSignableRequest();
        SdkHttpFullRequest signedRequest = sign(request, credentials);
        return signedRequest.getUri().toString().replace(REQUEST_PROTOCOL, "");
    }

    private SdkHttpFullRequest getSignableRequest() {
        SdkHttpFullRequest.Builder builder = SdkHttpFullRequest.builder()
            .method(REQUEST_METHOD)
            .uri(getRequestUri())
            .appendRawQueryParameter(PARAM_ACTION, ACTION_NAME)
            .appendRawQueryParameter(PARAM_USER, userId);
        if (isServerless) {
            builder.appendRawQueryParameter(PARAM_RESOURCE_TYPE, RESOURCE_TYPE_SERVERLESS_CACHE);
        }
        return builder.build();
    }

    private URI getRequestUri() {
        return URI.create(String.format("%s%s/", REQUEST_PROTOCOL, cacheName));
    }

    private SdkHttpFullRequest sign(SdkHttpFullRequest request, AwsCredentials credentials) {
        AwsV4HttpSigner signer = AwsV4HttpSigner.create();
        SignedRequest signedRequest = signer.sign(r -> r.identity(credentials)
            .request(request)
            .putProperty(AwsV4HttpSigner.SERVICE_SIGNING_NAME, SERVICE_NAME)
            .putProperty(AwsV4HttpSigner.REGION_NAME, region)
            .putProperty(AwsV4HttpSigner.AUTH_LOCATION, AwsV4HttpSigner.AuthLocation.QUERY_STRING)
            .putProperty(AwsV4HttpSigner.EXPIRATION_DURATION, TOKEN_EXPIRY_DURATION)
            .build()
        );
        return (SdkHttpFullRequest) signedRequest.request();
    }
}
```

**Connect with credentials provider**

The code below shows how to authenticate with ElastiCache using the IAM authentication credentials provider.

```
String userId = "{{insert user id}}";
String cacheName = "{{insert cache name}}";
boolean isServerless = {{true}};
String region = "{{insert region}}";

// Create a default AWS Credentials provider.
// This will look for AWS credentials defined in environment variables or system properties.
AwsCredentialsProvider awsCredentialsProvider = DefaultCredentialsProvider.create();

// Create an IAM authentication token request. Once this request is signed it can be used as an
// IAM authentication token for ElastiCache with Redis OSS.
IAMAuthTokenRequest iamAuthTokenRequest = new IAMAuthTokenRequest(userId, cacheName, region, isServerless);

// Create a Redis OSS credentials provider using IAM credentials.
RedisCredentialsProvider redisCredentialsProvider = new RedisIAMAuthCredentialsProvider(
    userId, iamAuthTokenRequest, awsCredentialsProvider);
    
// Construct Redis OSS URL with IAM Auth credentials provider
RedisURI redisURI = RedisURI.builder()
    .withHost(host)
    .withPort(port)
    .withSsl(ssl)
    .withAuthentication(redisCredentialsProvider)
    .build();

// Create a new Lettuce Redis OSS client
RedisClient client = RedisClient.create(redisURI);
client.connect();
```

Below is an example of a Lettuce Redis OSS client that wraps the IAMAuthTokenRequest in a credentials provider to auto-generate temporary credentials when needed.

```
public class RedisIAMAuthCredentialsProvider implements RedisCredentialsProvider {
    private static final long TOKEN_EXPIRY_SECONDS = 900;

    private final AwsCredentialsProvider awsCredentialsProvider;
    private final String userId;
    private final IAMAuthTokenRequest iamAuthTokenRequest;
    private final Supplier<String> iamAuthTokenSupplier;

    public RedisIAMAuthCredentialsProvider(String userId,
        IAMAuthTokenRequest iamAuthTokenRequest,
        AwsCredentialsProvider awsCredentialsProvider) {
        this.userId = userId;
        this.awsCredentialsProvider = awsCredentialsProvider;
        this.iamAuthTokenRequest = iamAuthTokenRequest;      
        this.iamAuthTokenSupplier = Suppliers.memoizeWithExpiration(this::getIamAuthToken, TOKEN_EXPIRY_SECONDS, TimeUnit.SECONDS);
    }

    @Override
    public Mono<RedisCredentials> resolveCredentials() {
        return Mono.just(RedisCredentials.just(userId, iamAuthTokenSupplier.get()));
    }

    private String getIamAuthToken() {
        return iamAuthTokenRequest.toSignedRequestUri(awsCredentialsProvider.resolveCredentials());
    }
}
```