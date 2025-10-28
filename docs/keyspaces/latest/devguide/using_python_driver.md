# Using a Cassandra Python client driver to

access Amazon Keyspaces programmatically

In this section, we show you how to connect to Amazon Keyspaces using a Python client
driver. To provide users and applications with credentials for programmatic access to
Amazon Keyspaces resources, you can do either of the following:

- Create service-specific credentials that are associated with a specific
  AWS Identity and Access Management (IAM) user.
- For enhanced security, we recommend to create IAM access keys
  for IAM users or roles that are used across all AWS services. The Amazon Keyspaces
  SigV4 authentication plugin for Cassandra client drivers enables you to
  authenticate calls to Amazon Keyspaces using IAM access keys instead of user name and
  password. For more information, see [Create and configure AWS credentials for Amazon Keyspaces](access.md "access.md").

###### Topics

- [Before you begin](#using_python_driver.BeforeYouBegin "#using_python_driver.BeforeYouBegin")
- [Connect to Amazon Keyspaces using the
  Python driver for Apache Cassandra and service-specific credentials](#python_ssc "#python_ssc")
- [Connect to Amazon Keyspaces using the DataStax
  Python driver for Apache Cassandra and the SigV4 authentication plugin](#python_SigV4 "#python_SigV4")

## Before you begin

You need to complete the following task before you can start.

Amazon Keyspaces requires the use of Transport Layer Security (TLS) to help secure
connections with clients. To connect to Amazon Keyspaces using TLS, you need to download Amazon
digital certificates and configure the Python driver to use TLS.

Download the following digital certificates and save
the files locally or in your home directory.

1. AmazonRootCA1
2. AmazonRootCA2
3. AmazonRootCA3
4. AmazonRootCA4
5. Starfield Class 2 Root (optional – for backward compatibility)

To download the certificates, you can use the following commands.

```
curl -O https://www.amazontrust.com/repository/AmazonRootCA1.pem
curl -O https://www.amazontrust.com/repository/AmazonRootCA2.pem
curl -O https://www.amazontrust.com/repository/AmazonRootCA3.pem
curl -O https://www.amazontrust.com/repository/AmazonRootCA4.pem
curl -O https://certs.secureserver.net/repository/sf-class2-root.crt
```

###### Note

Amazon Keyspaces previously used TLS certificates anchored to the Starfield Class 2 CA.
AWS is migrating all AWS Regions to certificates issued under Amazon Trust Services (Amazon Root CAs 1–4).
During this transition, configure clients to trust both Amazon Root CAs 1–4 and the Starfield root to ensure compatibility across all Regions.

Combine all downloaded certificates into a single `pem` file with the name
`keyspaces-bundle.pem` in our examples. You can do this by running the following command. Take note of the path to the
file, you need this later.

```
cat AmazonRootCA1.pem \
 AmazonRootCA2.pem \
 AmazonRootCA3.pem \
 AmazonRootCA4.pem \
 sf-class2-root.crt \
 > `keyspaces-bundle.pem`
```

## Connect to Amazon Keyspaces using the

Python driver for Apache Cassandra and service-specific credentials

The following code example shows you how to connect to Amazon Keyspaces with a
Python client driver and service-specific credentials.

```
from cassandra.cluster import Cluster
from ssl import SSLContext, PROTOCOL_TLSv1_2 , CERT_REQUIRED
from cassandra.auth import PlainTextAuthProvider

ssl_context = SSLContext(PROTOCOL_TLSv1_2 )

ssl_context.load_verify_locations('`path_to_file/keyspaces-bundle.pem`')

ssl_context.verify_mode = CERT_REQUIRED
auth_provider = PlainTextAuthProvider(username='`ServiceUserName`', password='`ServicePassword`')
cluster = Cluster(['`cassandra.us-east-2.amazonaws.com`'], ssl_context=ssl_context, auth_provider=auth_provider, port=9142)
session = cluster.connect()
r = session.execute('select * from system_schema.keyspaces')
print(r.current_rows)
```

Usage notes:

1. Replace
   `"`path_to_file/keyspaces-bundle.pem`"`
   with the path to the combined certificate file saved in the first step.
2. Ensure that the `ServiceUserName` and
   `ServicePassword` match the user
   name and password you obtained when you generated the
   service-specific credentials by following the steps to [Create service-specific
   credentials for programmatic access to Amazon Keyspaces](programmatic.credentials.md "programmatic.credentials.md").
3. For a list of available endpoints, see [Service endpoints for Amazon Keyspaces](programmatic.md "programmatic.md").

## Connect to Amazon Keyspaces using the DataStax

Python driver for Apache Cassandra and the SigV4 authentication plugin

The following section shows how to use the SigV4 authentication plugin
for the open-source DataStax Python driver for Apache Cassandra to access Amazon Keyspaces (for Apache Cassandra).

If you haven't already done so, begin with creating credentials for
your IAM role following the steps at [Create and configure AWS credentials for Amazon Keyspaces](access.md "access.md"). This
tutorial uses temporary credentials, which requires an IAM role. For more information
about temporary credentials, see [Create temporary credentials to connect to Amazon Keyspaces using an IAM role and the SigV4 plugin](temporary.credentials.md "temporary.credentials.md").

Then, add the Python SigV4 authentication plugin to your environment from the [GitHub repository](https://github.com/aws/aws-sigv4-auth-cassandra-python-driver-plugin "https://github.com/aws/aws-sigv4-auth-cassandra-python-driver-plugin").

```
pip install cassandra-sigv4
```

The following code example shows how to connect to Amazon Keyspaces by using the
open-source DataStax Python driver for Cassandra and the SigV4 authentication
plugin. The plugin depends on the AWS SDK for Python (Boto3). It uses
`boto3.session` to obtain temporary credentials.

```
from cassandra.cluster import Cluster
from ssl import SSLContext, PROTOCOL_TLSv1_2 , CERT_REQUIRED
from cassandra.auth import PlainTextAuthProvider
import boto3
from cassandra_sigv4.auth import SigV4AuthProvider

ssl_context = SSLContext(PROTOCOL_TLSv1_2)
ssl_context.load_verify_locations('`path_to_file/keyspaces-bundle.pem`')
ssl_context.verify_mode = CERT_REQUIRED

# use this if you want to use Boto to set the session parameters.
boto_session = boto3.Session(aws_access_key_id="`AKIAIOSFODNN7EXAMPLE`",
                             aws_secret_access_key="`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`",
                             aws_session_token="`AQoDYXdzEJr...<remainder of token>`",
                             region_name="`us-east-2`")
auth_provider = SigV4AuthProvider(boto_session)

# Use this instead of the above line if you want to use the Default Credentials and not bother with a session.
# auth_provider = SigV4AuthProvider()

cluster = Cluster(['`cassandra.us-east-2.amazonaws.com`'], ssl_context=ssl_context, auth_provider=auth_provider,
                  port=9142)
session = cluster.connect()
r = session.execute('select * from system_schema.keyspaces')
print(r.current_rows)
```

Usage notes:

1. Replace

`"`path_to_file/keyspaces-bundle.pem`"`
with the path to the certificate saved in the first step. 2. Ensure that the `aws_access_key_id`,
`aws_secret_access_key`, and the `aws_session_token` match the
`Access Key`, `Secret Access Key`, and `Session Token` you obtained using
`boto3.session`. For more information, see [Credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html") in the
_AWS SDK for Python (Boto3)_. 3. For a list of available endpoints, see [Service endpoints for Amazon Keyspaces](programmatic.md "programmatic.md").
