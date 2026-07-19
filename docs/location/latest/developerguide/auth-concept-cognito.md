# Amazon Cognito concepts

Amazon Cognito provides temporary AWS credentials to your application users, enabling
them to call Amazon Location Service APIs without requiring IAM user accounts. Amazon Cognito is
particularly useful when you need access to all Amazon Location Service APIs (including Geofences
and Trackers) or want to combine multiple authentication providers.

**Identity pool**

A Amazon Cognito resource that maps user identities to temporary AWS
credentials. Identity pools support both authenticated users (signed
in through a user pool or external provider) and unauthenticated
guest users.

**Unauthenticated role**

An IAM role assumed by guest users who access your application
without signing in. The permissions attached to this role determine
what Amazon Location Service APIs and resources anonymous users can access.

**Authenticated role**

An IAM role assumed by users who sign in through a Amazon Cognito user
pool, social identity provider, or SAML federation. Authenticated
roles typically have broader permissions than unauthenticated
roles.

**Token exchange**

The process by which your application exchanges a Amazon Cognito identity
for temporary AWS credentials (access key, secret key, and session
token). The AWS SDKs and the Amazon Location Service authentication helper library
handle this exchange automatically.
