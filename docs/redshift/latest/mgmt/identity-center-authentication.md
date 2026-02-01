Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Connect to Redshift with Identity-enhanced IAM role sessions

You can use IAM Identity Center to provide federated access to your Amazon Redshift clusters and
serverless workgroups. This approach allows users to authenticate using their Identity Center
credentials.

Amazon Redshift provides `GetIdentityCenterAuthToken` API operations to generate
authorized token that contains user identity information. These APIs are available
for both provisioned clusters and serverless workgroups. The tokens enable
seamless single sign-on access to Amazon Redshift databases using your existing Identity Center setup.

## Prerequisites

Before using Identity Center authentication with Amazon Redshift, ensure you have the following:

- **Identity Center setup:** Your account must have
  IAM Identity Center configured with user identities and appropriate application assignments.
  For setup instructions, see [Setting up IAM Identity Center](../../../singlesignon/latest/userguide/enable-identity-center.md "../../../singlesignon/latest/userguide/enable-identity-center.md").

###### Important

If you want to connect to Redshift, you must use redshift:connect scope.

- **Identity-enhanced credentials:** Your application must
  use identity-enhanced credentials that contain embedded user identity information.
  For more information, see [Using identity-enhanced IAM role sessions](../../../singlesignon/latest/userguide/trustedidentitypropagation-identity-enhanced-iam-role-sessions.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-identity-enhanced-iam-role-sessions.md").
- **IAM permissions:** Your IAM role or user must have
  permissions to call the `GetIdentityCenterAuthToken` API and access the
  specified clusters or workgroups. Required permissions:
  - For provisioned clusters: `redshift:GetIdentityCenterAuthToken` on cluster ARNs
    (format: `arn:aws:redshift:region:account:cluster:cluster-name`)
  - For serverless workgroups: `redshift-serverless:GetIdentityCenterAuthToken` on workgroup ARNs
    (format: `arn:aws:redshift-serverless:region:account:workgroup/workgroup-name`)

- **Compatible drivers:** Use Amazon Redshift JDBC or ODBC drivers
  that support Identity Center authorized tokens:
  - JDBC drivers: See [Installing and configuring the Amazon Redshift JDBC driver version 2.0](jdbc20-install.md "jdbc20-install.md")
  - ODBC drivers: See [Installing and configuring the Amazon Redshift ODBC driver version 2.0](odbc20-install.md "odbc20-install.md")

## How Identity Center authentication works

Identity Center authentication for Amazon Redshift uses the following workflow:

1. Your application calls the `GetIdentityCenterAuthToken` API
   using identity-enhanced credentials that contain embedded user identity information.
2. Amazon Redshift validates the Identity Center identity and generates an encrypted authorized token
   scoped to specific clusters or workgroups. See example IAM policies.
3. Your application uses this token to connect to the specified Amazon Redshift cluster or workgroup.
4. The Amazon Redshift data plane validates the token and grants access based on the Identity Center
   user's permissions within the Identity Center application.

###### Important

This API requires identity-enhanced credentials. For more information, see [Using identity-enhanced IAM role sessions](../../../singlesignon/latest/userguide/trustedidentitypropagation-identity-enhanced-iam-role-sessions.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-identity-enhanced-iam-role-sessions.md").

If you call the API without identity-enhanced credentials, you will receive an `UnsupportedOperationFault` error.

## GetIdentityCenterAuthToken API operations

Amazon Redshift provides two separate `GetIdentityCenterAuthToken` API operations: one for
provisioned clusters and one for serverless workgroups. Both operations have the same name but accept
different parameters depending on the target resource type.

### GetIdentityCenterAuthToken for provisioned clusters

For provisioned Amazon Redshift clusters, use the `GetIdentityCenterAuthToken` API
in the Amazon Redshift service to generate authorized token.

#### Request syntax

```

{
   "ClusterIds": [ "string" ]
}

```

#### Request parameters

ClusterIds

A list of Amazon Redshift cluster identifiers that the token will be authorized to access.
The token can only be used to authenticate with the clusters specified in this list.

Type: Array of strings

Length constraints: Minimum of 1 item. Maximum of 20 items.

Required: Yes

#### CLI examples

**Example: Get authorized token for a single cluster**

```
aws redshift get-identity-center-auth-token \
    --cluster-ids my-redshift-cluster
```

**Example: Get authorized token for multiple clusters**

```
aws redshift get-identity-center-auth-token \
    --cluster-ids my-cluster-1 my-cluster-2
```

### GetIdentityCenterAuthToken for serverless workgroups

For Amazon Redshift Serverless workgroups, use the `GetIdentityCenterAuthToken` API
in the Amazon Redshift Serverless service to generate authorized token.

#### Request syntax

```

{
   "WorkgroupNames": [ "string" ]
}

```

#### Request parameters

WorkgroupNames

A list of Amazon Redshift Serverless workgroup names that the token will be authorized to access.
The token can only be used to authenticate with the workgroups specified in this list.

Type: Array of strings

Length constraints: Minimum of 1 item. Maximum of 20 items.

Required: Yes

#### CLI examples

**Example: Get authorized token for a single workgroup**

```
aws redshift-serverless get-identity-center-auth-token \
    --workgroup-names my-workgroup
```

**Example: Get authorized token for multiple workgroups**

```
aws redshift-serverless get-identity-center-auth-token \
    --workgroup-names workgroup-1 workgroup-2
```

### Response syntax

Both APIs return the same response structure:

```

{
   "AuthorizedToken": "string",
   "ExpirationTime": "timestamp"
}

```

#### Response parameters

AuthorizedToken

An encrypted authorized token that contains the user identity information
and the list of authorized clusters or workgroups. This token should be
treated as sensitive data.

Type: String

ExpirationTime

The date and time when the token expires, in UTC. Tokens are valid for
1 hour from the time of generation.

Type: Timestamp

#### Example response

```
{
    "AuthorizedToken": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyQGV4YW1wbGUuY29tIiwiaWF0IjoxNjQwOTk1MjAwLCJleHAiOjE2NDA5OTg4MDAsImNsdXN0ZXJzIjpbIm15LWNsdXN0ZXIiXX0...",
    "ExpirationTime": "2024-01-01T12:00:00Z"
}
```

## Driver integration

Amazon Redshift drivers support Identity Center authentication through direct token usage:

### Direct token usage

After calling the `GetIdentityCenterAuthToken` API to obtain a token,
use the `IdpTokenAuthPlugin` with the `SUBJECT_TOKEN` token type.

Connection Configuration:

```

plugin_name = com.amazon.redshift.plugin.IdpTokenAuthPlugin
token_type = SUBJECT_TOKEN
token = {encrypted_token_from_api_response}

```

For detailed information about Identity Center authentication plugins and driver configuration,
see [Connecting to an Amazon Redshift cluster](connecting-to-cluster.md "connecting-to-cluster.md").

### Java code example

Sample Java code to connect using Identity Center authentication:

```

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;

// Get token from GetIdentityCenterAuthToken API
String token = "your_encrypted_token_from_api_response";

// Configure connection properties
Properties props = new Properties();
props.setProperty("user", "your_username");
props.setProperty("plugin_name", "com.amazon.redshift.plugin.IdpTokenAuthPlugin");
props.setProperty("token_type", "SUBJECT_TOKEN");
props.setProperty("token", token);

// Connect to Redshift
String url = "jdbc:redshift://your-cluster.region.redshift.amazonaws.com:5439/your_database";
try (Connection conn = DriverManager.getConnection(url, props)) {
    // Use connection
    System.out.println("Connected successfully!");
} catch (SQLException e) {
    e.printStackTrace();
}

```

## IAM policy requirements

To use Identity Center authentication with Amazon Redshift, specific IAM permissions are required
beyond the standard permissions needed for connecting to Amazon Redshift clusters and workgroups.

### API permissions

For provisioned clusters, your enhanced IAM role session must have:

- `redshift:GetIdentityCenterAuthToken` on cluster ARNs
  (format: `arn:aws:redshift:region:account:cluster:cluster-name`)

For serverless workgroups, your enhanced IAM role session must have:

- `redshift-serverless:GetIdentityCenterAuthToken` on workgroup ARNs
  (format: `arn:aws:redshift-serverless:region:account:workgroup/workgroup-name`)

### Example IAM policies

**Example policy for provisioned clusters:**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "redshift:GetIdentityCenterAuthToken"
            ],
            "Resource": [
                "arn:aws:redshift:us-east-1:123456789012:cluster:my-cluster"
            ]
        }
    ]
}
```

**Example policy for serverless workgroups:**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "redshift-serverless:GetIdentityCenterAuthToken"
            ],
            "Resource": [
                "arn:aws:redshift-serverless:us-east-1:123456789012:workgroup/my-workgroup"
            ]
        }
    ]
}
```

**Example policy for multiple resources:**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "redshift:GetIdentityCenterAuthToken"
            ],
            "Resource": [
                "arn:aws:redshift:*:123456789012:cluster/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "redshift-serverless:GetIdentityCenterAuthToken"
            ],
            "Resource": [
                "arn:aws:redshift-serverless:*:123456789012:workgroup/*"
            ]
        }
    ]
}
```

## Regional availability

Identity Center authentication is available in the following AWS regions:

- Commercial regions: All supported Amazon Redshift regions
- AWS GovCloud: Available in us-gov-east-1 and us-gov-west-1
- China regions: Available in cn-north-1 and cn-northwest-1

###### Note

Feature availability may vary during initial rollout.
