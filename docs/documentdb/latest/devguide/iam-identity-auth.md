# Authentication using IAM identity

Amazon DocumentDB users and applications can use IAM users and roles to authenticate into an Amazon DocumentDB cluster.
Amazon DocumentDB IAM authentication is a password-less authentication method. Also, client applications do not send the password secrets to the Amazon DocumentDB cluster when using IAM roles/users.
Instead, client connections are authenticated by AWS STS using temporary security tokens.
Non-administrative users and applications can now use the same IAM identity ARN when connecting to different Amazon DocumentDB clusters and other AWS services.

You can also choose to use both password-based and IAM authentication to authenticate users and applications to an Amazon DocumentDB cluster.
IAM authentication is available only in Amazon DocumentDB instance-based cluster version 5.0.
IAM authentication using IAM identity ARNs is not supported for the Amazon DocumentDB primary user.

###### Note

The primary user can only be authenticated using existing password-based authentication.

###### Topics

- [Getting started with authentication using IAM users and roles](#iam-identity-auth-get-started "#iam-identity-auth-get-started")
- [Configuring AWS compute types to authenticate to Amazon DocumentDB using AWS IAM](#iam-identity-auth-compute-types "#iam-identity-auth-compute-types")
- [Monitoring IAM authentication requests](#iam-identity-auth-monitoring "#iam-identity-auth-monitoring")
- [Using IAM authentication](#iam-identity-auth-using "#iam-identity-auth-using")
- [Drivers supporting IAM](#iam-identity-drivers "#iam-identity-drivers")
- [IAM identity authentication FAQ](#iam-identity-auth-faq "#iam-identity-auth-faq")

## Getting started with authentication using IAM users and roles

Amazon DocumentDB users and roles with IAM identities are created and managed in an `$external` database.

**Creating a user**

Connect as the primary user, then create an IAM user and role:

```
use $external;
db.createUser(
    {
        user: "arn:aws:iam::123456789123:user/iamuser",
        mechanisms: ["MONGODB-AWS"],
        roles: [ { role: "readWrite", db: "readWriteDB" } ]
    }
);
```

Alternatively, add an Amazon DocumentDB user using an IAM role:

```
use $external;
db.createUser(
    {
        user: "arn:aws:iam::123456789123:role/iamrole",
        mechanisms: ["MONGODB-AWS"],
        roles: [ { role: "readWrite", db: "readWriteDB" } ]
    }
);
```

**Modifying an IAM user or role**

Modify an existing IAM user:

```
use $external;
db.updateUser(
  "arn:aws:iam::123456789123:user/iamuser",
  {
    roles: [ { role: "read", db: "readDB" } ]
  }
);
```

Modify an existing IAM role:

```
use $external;
db.updateUser(
  "arn:aws:iam::123456789123:role/iamrole",
  {
    roles: [ { role: "read", db: "readDB" } ]
  }
);
```

To grant or revoke roles from an IAM user:

```
use $external;
db.grantRolesToUser(
  "arn:aws:iam::123456789123:user/iamuser",
  [ { db: "admin", role: "readWriteAnyDatabase" } ]
);
```

```
use $external;
db.revokeRolesFromUser(
  "arn:aws:iam::123456789123:user/iamuser",
  [ { db: "admin", role: "readWriteAnyDatabase" } ]
);
```

To grant or revoke roles from an IAM role:

```
use $external;
db.grantRolesToUser(
  "arn:aws:iam::123456789123:user/iamrole",
  [ { db: "admin", role: "readWriteAnyDatabase" } ]
);
```

```
use $external;
db.revokeRolesFromUser(
  "arn:aws:iam::123456789123:user/iamrole",
  [ { db: "admin", role: "readWriteAnyDatabase" } ]
);
```

**Dropping an IAM user or role**

To drop an existing IAM user:

```
use $external;
db.dropUser("arn:aws:iam::123456789123:user/iamuser");
```

To drop an existing IAM role:

```
use $external;
db.dropUser("arn:aws:iam::123456789123:role/iamrole");
```

**Configure a connection URI to authenticate using AWS IAM**

To authenticate using AWS IAM, use the following URI parameters: `authSource` as `$external` and `authMechanism` as `MONGODB-AWS`.
If you are using an IAM user, the username and password fields are replaced by an Access Key and Secret Key respectively.
If you are assuming an IAM role, attached to the environment you are in (for example, AWS Lambda function, Amazon EC2 instance).
You don’t need to specifically pass any credential when authenticating using the `MONGODB-AWS` mechanism.
If you are using MongoDB drivers that support the `MONGODB-AWS` authentication mechanism, the drivers also have the ability to retrieve IAM role credentials from the compute instance (for example, Amazon EC2, Lambda function, and others).
The following example uses a mongo shell to authenticate using `MONGODB-AWS` by passing an Access Key and Secret Key (of an IAM user) manually to demonstrate authentication against Amazon DocumentDB.

The following example uses Python code to authenticate using `MONGODB-AWS` without explicitly passing any credentials (using an IAM Role attached to the environment) to demonstrate authentication against Amazon DocumentDB.

```
##Create a MongoDB client, open a connection to Amazon DocumentDB using an IAM role
    client = pymongo.MongoClient(‘mongodb://<DocDBEndpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false&authSource=%24external&authMechanism=MONGODB-AWS')
```

The following example uses a mongo shell to authenticate using `MONGODB-AWS` mechanism by passing an Access Key and Secret Key (of an IAM user) manually to demonstrate authentication against Amazon DocumentDB.

```
$ mongo 'mongodb://<access_key>:<secret_key>@<cluster_endpoint>:<db_port>/test?authSource=%24external&authMechanism=MONGODB-AWS'
```

The following example uses a mongo shell to authenticate using `MONGODB-AWS` without explicitly passing any credentials (using IAM Role attached to the environment) to demonstrate authentication against Amazon DocumentDB.

```
$ mongo 'mongodb://<cluster_endpoint>:<db_port>/test?authSource=%24external&authMechanism=MONGODB-AWS'
```

## Configuring AWS compute types to authenticate to Amazon DocumentDB using AWS IAM

**Using Amazon EC2/AWS Lambda/AWS Fargate**

Amazon EC2 uses the following environment variables.
If you have a IAM role attached to the EC2 instance or an execution IAM role associated with a Lambda function or an Amazon ECS task, then these variables are automatically populated and the driver can fetch these values from environment:

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_SESSION_TOKEN
```

For more information about environment variables, see [Using Lambda environment variables](../../../lambda/latest/dg/configuration-envvars.md "../../../lambda/latest/dg/configuration-envvars.md") in the _AWS Lambda Developer Guide_.

**Using Amazon EKS**

Assigning a role to your Amazon Elastic Kubernetes Service (Amazon EKS) pods will automatically setup the following two environment variables:

```
AWS_WEB_IDENTITY_TOKEN_FILE - path of web identity token file
AWS_ROLE_ARN - Name of IAM role to connect with
```

With the help of these variables, manually assume the role from your code using the AWS SDK call for `AssumeRoleWithWebIdentity`:

- Omit the `ProviderID` parameter.
- Find the value of the `WebIdentityToken` parameter in the file described in the `AWS_WEB_IDENTITY_TOKEN_FILE` environment variable.

For more info on Amazon EKS, see [What is Amazon EKS](../../../eks/latest/userguide/what-is-eks.md "../../../eks/latest/userguide/what-is-eks.md") in the _Amazon EKS User Guide_.

## Monitoring IAM authentication requests

**Using Amazon DocumentDB auditing**

Go to the audit log folder in Amazon CloudWatch, and use different search patterns to get the logs for IAM authentication.
For example, use `{ $.param.mechanism = "MONGODB-AWS" }` as the search pattern for “Search all log streams”.

For more info on supported events in auditing, see [Auditing Amazon DocumentDB events](event-auditing.md "event-auditing.md").

**Using Amazon CloudWatch metrics**

**`StsGetCallerIdentityCalls`**: This metric shows how many `GetCallerIdentity` calls an Amazon DocumentDB instance is making to the regionalized AWS Security Token Service (AWS STS) endpoint.
Please refer to the `MONGODB-AWS` authentication specification on why database instances need to make STS `GetCallerIdentity` calls.

## Using IAM authentication

When you don’t want to manage the username and password in your own database, you can use IAM authentication.
IAM authentication is available only in Amazon DocumentDB instance-based cluster version 5.0.

IAM authentication has a dependency on the STS service.
We recommend you evaluate whether you can lower your connection rate when you are using IAM authentication for the connection and getting an STS throttling exception.

For IAM quotas, see [IAM and AWS STS quotas](../../../IAM/latest/UserGuide/reference_iam-quotas.md "../../../IAM/latest/UserGuide/reference_iam-quotas.md") in the _IAM User Guide_.

## Drivers supporting IAM

Drivers that support Amazon DocumentDB 5.0 and the `MONGODB-AWS` authentication mechanism should work with the IAM authentication implementation in Amazon DocumentDB.

###### Important

There is a known limitation with Node.js drivers older than version 6.13.1, which are currently not supported by IAM identity authentication for Amazon DocumentDB.
Node.js drivers and tools that use Node.js driver (for example, mongosh) must be upgraded to use Node.js driver version 6.13.1 or above.

## IAM identity authentication FAQ

**Are there any samples I can refer to?**

See these pages for sample use cases and configurations:

- [How human users can authenticate to Amazon DocumentDB using IAM Users and IAM Roles](https://github.com/aws-samples/amazon-documentdb-samples/tree/master/samples/iam_user_sample_code "https://github.com/aws-samples/amazon-documentdb-samples/tree/master/samples/iam_user_sample_code")
- [Password-less authentication to Amazon DocumentDB using IAM Roles](https://github.com/aws-samples/amazon-documentdb-samples/tree/master/samples/iam_role_sample_code "https://github.com/aws-samples/amazon-documentdb-samples/tree/master/samples/iam_role_sample_code")

**I am getting an error while using my Python driver: “pymongo.errors.ConfigurationError: MONGODB-AWS authentication requires pymongo-auth-aws”. How can I resolve this?**

Please make sure you use the following statement while installing the Python driver with IAM authentication:

`pip install 'pymongo[aws]'`

This will install the additional AWS dependencies required for IAM authentication to work.

**Will my connection drop when my IAM role temporary credentials expire?**

No, the temporary IAM credentials are only used for establishing connection and authentication.
Then all further authorization happens in the Amazon DocumentDB cluster. Even if IAM credentials rotate/expire, the connection will not drop or get stale.
