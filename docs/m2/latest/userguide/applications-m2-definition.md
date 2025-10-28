AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Mainframe Modernization application definition

reference

In AWS Mainframe Modernization, you configure migrated mainframe applications in an application definition
JSON file, which is specific to the runtime engine you choose. An application definition
contains both general information and engine-specific information. This topic describes both
the AWS Blu Age and Rocket Software (formerly Micro Focus) application definitions and identifies all required and
optional elements.

###### Contents

- [General header section](applications-m2-definition.md#applications-m2-definition-general "applications-m2-definition.md#applications-m2-definition-general")
- [Definition section overview](applications-m2-definition.md#applications-m2-definition-overview "applications-m2-definition.md#applications-m2-definition-overview")
- [AWS Blu Age application definition
  sample](applications-m2-definition.md#applications-m2-definition-ba "applications-m2-definition.md#applications-m2-definition-ba")
- [AWS Blu Age definition details](applications-m2-definition.md#applications-m2-definition-ba-details "applications-m2-definition.md#applications-m2-definition-ba-details")
  - [Listener(s) -
    required](applications-m2-definition.md#applications-m2-definition-ba-details-listener "applications-m2-definition.md#applications-m2-definition-ba-details-listener")
  - [AWS Blu Age application
  * required](applications-m2-definition.md#applications-m2-definition-ba-details-application "applications-m2-definition.md#applications-m2-definition-ba-details-application")
  - [Blusam -
    optional](applications-m2-definition.md#applications-m2-definition-ba-details-blusam "applications-m2-definition.md#applications-m2-definition-ba-details-blusam")
  - [AWS Blu Age message queues -
    optional](applications-m2-definition.md#applications-m2-definition-ba-message-queues "applications-m2-definition.md#applications-m2-definition-ba-message-queues")
  - [AWS Blu Age Application
    storage EFS config - optional](applications-m2-definition.md#applications-m2-definitions-ba--details-efs "applications-m2-definition.md#applications-m2-definitions-ba--details-efs")

- [Rocket Software (formerly Micro Focus) application
  definition](applications-m2-definition.md#applications-m2-definition-mf "applications-m2-definition.md#applications-m2-definition-mf")
- [Rocket Software definition details](applications-m2-definition.md#applications-m2-definition-mf-details "applications-m2-definition.md#applications-m2-definition-mf-details")
  - [Listener(s) -
    required](applications-m2-definition.md#applications-m2-definition-mf-details-listeners "applications-m2-definition.md#applications-m2-definition-mf-details-listeners")
  - [Data set locations
  * required](applications-m2-definition.md#applications-m2-definition-mf-details-datasets "applications-m2-definition.md#applications-m2-definition-mf-details-datasets")
  - [Amazon Cognito
    authentication and authorization handler - optional](applications-m2-definition.md#applications-m2-definition-mf-details-cognito "applications-m2-definition.md#applications-m2-definition-mf-details-cognito")
  - [LDAP and Active
    Directory handler - optional](applications-m2-definition.md#applications-m2-definition-mf-details-ldap-ad "applications-m2-definition.md#applications-m2-definition-mf-details-ldap-ad")
  - [Batch settings -
    required](applications-m2-definition.md#applications-m2-definition-mf-details-batch "applications-m2-definition.md#applications-m2-definition-mf-details-batch")
  - [CICS settings -
    required](applications-m2-definition.md#applications-m2-definition-mf-details-cics "applications-m2-definition.md#applications-m2-definition-mf-details-cics")
  - [Printers - optional](applications-m2-definition.md#applications-m2-definition-mf-details-printers "applications-m2-definition.md#applications-m2-definition-mf-details-printers")
  - [XA resources -
    optional](applications-m2-definition.md#applications-m2-definition-mf-details-xa "applications-m2-definition.md#applications-m2-definition-mf-details-xa")
  - [Runtime settings -
    optional](applications-m2-definition.md#applications-m2-definition-mf-details-runtime-settings "applications-m2-definition.md#applications-m2-definition-mf-details-runtime-settings")

## General header section

Each application definition starts with general information about the template version
and source locations. The current version of the application definition is 2.0.

Use the following structure to specify the template version and source
locations.

```
"template-version": "2.0",
    "source-locations": [
        {
            "source-id": "s3-source",
            "source-type": "s3",
            "properties": {
                "s3-bucket": "mainframe-deployment-bucket",
                "s3-key-prefix": "v1"
            }
        }
    ]
```

###### Note

You can use the following syntax if you want to input S3 ARN as s3-bucket :

```
"template-version": "2.0",
  "source-locations": [
      {
          "source-id": "s3-source",
          "source-type": "s3",
          "properties": {
              "s3-bucket": "arn:aws:s3:::mainframe-deployment-bucket",
              "s3-key-prefix": "v1"
          }
      }
  ]
```

**template-version**

(Required) Specifies the version of the application definition file. Do
not change this value. Currently, the only allowed value is 2.0. Specify
`template-version` with a string.

**source-locations**

Specifies the locations of the files and other resources that the
application requires during runtime.

**source-id**

Specifies a name for the location. This name is used to reference the
source location as needed in the application definition JSON.

**source-type**

Specifies the type of the source. Currently, the only allowed value is
s3.

**properties**

Provides the details of the source location. Each property is specified
with a string.

- `s3-bucket` - Required. Specifies the name of the Amazon S3
  bucket where the files are stored.
- `s3-key-prefix` - Required. Specifies the name of the
  folder in the Amazon S3 bucket where the files are stored.

## Definition section overview

Specifies the resource definitions of the services, settings, data, and other typical
resources that the application needs to run. When you update an application definition,
AWS Mainframe Modernization detects changes by comparing the `source-locations` and
`definition` lists from both the previous and the current versions of the
application definition JSON file.

The definition section is engine-specific and subject to change. The following
sections show sample engine-specific application definitions for both engines.

## AWS Blu Age application definition

sample

```
{
 "template-version": "2.0",
 "source-locations": [
        {
            "source-id": "s3-source",
            "source-type": "s3",
            "properties": {
                "s3-bucket": "mainframe-deployment-bucket-aaa",
                "s3-key-prefix": "v1"
            }
        }
    ],
    "definition" : {
        "listeners": [{
            "port": 8194,
            "type": "http"
        }],
        "ba-application": {
            "app-location": "${s3-source}/murachs-v6/"
        },
        "blusam": {
            "db": {
                "nb-threads": 8,
                "batch-size": 10000,
                "name": "blusam",
                "secret-manager-arn": "arn:aws:secretsmanager:us-west-2:111122223333:secret:blusam-FfmXLG"
            },
            "redis": {
                "hostname": "blusam.c3geul.ng.0001.usw2.cache.amazonaws.com",
                "port": 6379,
                "useSsl": true,
                "secret-manager-arn": "arn:aws:secretsmanager:us-west-2:111122223333:secret:bluesamredis-nioefm"
            }
        }
    }
}
```

## AWS Blu Age definition details

### Listener(s) -

required

Specify the port you will use to access the application through the AWS Mainframe Modernization-created
Elastic Load Balancing. Use the following structure:

```
"listeners": [{
            "port": 8194,
            "type": "http"
}],
```

**port**

(Required) You can use any available port except for the well-known
ports of 0 to 1023. We recommend using the range from 8192 to 8199. Make
sure there’s no other listeners or applications operating on this
port.

**type**

(Required) Currently, only `http` is supported.

### AWS Blu Age application

- required

Specify the location where the engine picks up the application image file using
the following structure.

```
"ba-application": {
            "app-location": "${s3-source}/murachs-v6/",
            "files-directory": "/m2/mount/myfolder",
            "enable-jics": <true|false>,
            "enable-batch-restart": <true|false>,
            "shared-app-location": "${s3-source}/shared/"
},
```

**app-location**

The specific location in Amazon S3 where the application image file is
stored.

**files-directory**

(Optional) The location of the input/output files for batches. Must be
a subfolder of the Amazon EFS or Amazon FSx mount point setup at environment
level. The subfolder must be owned by a suitable user for use by the
**Blu Age** application running inside
AWS Mainframe Modernization. To achieve this, when attaching the drive to a Linux Amazon EC2
instance, a group with ID `101` and a user with ID
`3001` must be created, and the desired folder must be
owned by this user. _For example, this way, the
`testclient` folder can be used by **Blu Age** AWS Mainframe Modernization Managed._

```
groupadd -g 101 mygroup
useradd -M -g mygroup -p mypassword -u 3001 myuser
mkdir testclient
chown myuser:mygroup testclient
```

**enable-jics**

(Optional) Specifies whether to enable JICS. Defaults to true. Setting
this to false prevents the JICS database from being spawned.

**enable-batch-restart**

(Optional) Specifies whether to enable restart feature for batch jobs.
Defaults to false. For more information regarding batch restart
configurations, see AWS Blu Age engine properties prefixed
`jcl.checkpoint` in [Configuration properties for the managed application with AWS Blu Age
engine](applications-m2-ba-config-props.md#gapwalk-app-props "applications-m2-ba-config-props.md#gapwalk-app-props").

**shared-app-location**

(Optional) Further location in Amazon S3 where shared application elements
are stored. It can contain the same kind of application structure as
app-location.

### Blusam -

optional

Specify the Blusam database and Redis cache using the following structure.

```
"blusam": {
            "db": {
                "nb-threads": 8,
                "batch-size": 10000,
                "name": "blusam",
                "secret-manager-arn": "arn:aws:secretsmanager:us-west-2:111122223333:secret:blusam-FfmXLG"
            },
            "redis": {
                "hostname": "blusam.c3geul.ng.0001.usw2.cache.amazonaws.com",
                "port": 6379,
                "useSsl": true,
                "secret-manager-arn": "arn:aws:secretsmanager:us-west-2:111122223333:secret:bluesamredis-nioefm"
            }
}
```

**db**

Specifies the properties of the database used with the application.
The database must be an Aurora PostgreSQL database. You can specify the
following properties:

- `nb-threads` - (Optional) Specifies how many
  dedicated threads are used for the write-behind mechanism that
  the Blusam engine relies on. The default is 8.
- `batch-size` - (Optional) Specifies the threshold
  that the write-behind mechanism uses to start batch storage
  operations. The threshold represents the number of modified
  records that will start a batch storage operation to ensure that
  modified records are persisted. The trigger itself is based on a
  combination of batch-size and an elapsed time of one second,
  whichever is reached first. The default is 10000.
- `name` - (Optional) Specifies the name of the
  database.
- `secret-manager-arn` - Specifies the Amazon
  Resource Name (ARN) of the secret that contains the database
  credentials. For more information, see [Step 4: Create and configure an AWS Secrets Manager
  database secret](tutorial-runtime-mf.md#tutorial-runtime-mf-secret "tutorial-runtime-mf.md#tutorial-runtime-mf-secret").

**Redis**

Specifies the properties of the Redis cache that the application uses
to store temporary data that it needs in a central location to improve
performance. We recommend that you both encrypt and password-protect the
Redis cache.

- `hostname` - Specifies the location of the Redis
  cache.
- `port` - Specifies the port, typically 6379, where
  the Redis cache sends and receives communication.
- `useSsl` - Specifies whether the Redis cache is
  encrypted. If the cache is not encrypted, set
  `useSsl` to false.
- `secret-manager-arn` - Specifies the Amazon
  Resource Name (ARN) of the secret that contains the Redis cache
  password. If the Redis cache is not password-protected, do not
  specify `secret-manager-arn`. For more information,
  see [Step 4: Create and configure an AWS Secrets Manager
  database secret](tutorial-runtime-mf.md#tutorial-runtime-mf-secret "tutorial-runtime-mf.md#tutorial-runtime-mf-secret").

### AWS Blu Age message queues -

optional

Specify the JMS-MQ connection details for AWS Blu Age application.

```
"message-queues": [
  {
      "product-type": "JMS-MQ",
      "queue-manager": "QMgr1",
      "channel": "mqChannel1",
      "hostname": "mqserver-host1",
      "port": 1414,
      "user-id": "app-user1",
      "ssl-cipher": "*TLS12ORHIGHER",
      "secret-manager-arn": "arn:aws:secretsmanager:us-west-2:123456789012:secret:sample/mq/test-279PTa"
  },
  {
      "product-type": "JMS-MQ",
      "queue-manager": "QMgr2",
      "channel": "mqChannel2",
      "hostname": "mqserver-host2",
      "port": 1412,
      "user-id": "app-user2",
      "ssl-cipher": "*TLS12ORHIGHER",
      "secret-manager-arn": "arn:aws:secretsmanager:us-west-2:123456789012:secret:sample/mq/test-279PTa"
  }
]
```

**product-type**

(Required) Specifies the product type. Currently, this can only be
"JMS-MQ" for AWS Blu Age applications.

**queue-manager**

(Required) Specifies the name of the queue manager.

**channel**

(Required) Specifies the name of the server-connection channel.

**hostname**

(Required) Specifies the hostname of the message queue server.

**port**

(Required) Specifies the listener port number the server is listening
on.

**user-id**

(Optional) Specifies the user account ID permitted to perform message
queue operations on the specified channel.

**ssl-cipher**

(Optional) Specifies the SSL cipher specification for the
connection.

**secret-manager-arn**

(Optional) Specifies the Amazon Resource Name (ARN) of Secrets Manager that
provides the password of the specified user.

### AWS Blu Age Application

storage EFS config - optional

Specify the application storage EFS Access point details using the following
structure.

```
"ba-application": {
            "file-permission-mask": "UMASK002"
},
"efs-configs": [
           {
            "file-system-id": "fs-01376dfsvfvrsvsr",
            "mount-point": "/m2/mount/efs-ap2",
            "access-point-id": fsap-0eaesefvrefrewgv8"
           }
]
```

**file-system-id**

(Required) The ID of EFS file system that the access point applies to.
Pattern: "fs-([0-9a-f]{8,40}){1,128}$"

**mount-point**

(Required) The mount point for the application level file system. This
must be different than the environment level storage mount point.

**access-point-id**

(Required) The ID of the access point, assigned by Amazon EFS. Pattern:
"^fsap-([0-9a-f]{8,40}){1,128}$"

**file-permission-mask**

(Optional) Defines the file creation mask for files created by the
application process. For example, when the value is set to
`UMASK006`, all the files will have permission 660. This
will mean that only the file owner and file group will have the read and
write access, while other users don't have any permissions.

###### Note

The value set for this field is only considered when using application level EFS storage.

###### Note

When efs config is provided, files-directory must be specified in the application
definition section. It must be a subfolder of the Amazon EFS mount point set up at
application level.

## Rocket Software (formerly Micro Focus) application

definition

The following sample definition section is for the Rocket Software runtime engine, and contains
both required and optional elements.

```
{
 "template-version": "2.0",
 "source-locations": [
        {
            "source-id": "s3-source",
            "source-type": "s3",
            "properties": {
                "s3-bucket": "mainframe-deployment-bucket-aaa",
                "s3-key-prefix": "v1"
            }
        }
    ],
    "definition" : {
        "listeners": [{
            "port": 5101,
            "type": "tn3270"
        }],
        "dataset-location": {
            "db-locations": [{
                "name": "Database1",
                "secret-manager-arn": "arn:aws:secrets:1234:us-east-1:secret:123456"
            }]
        },
        "cognito-auth-handler": {
            "user-pool-id": "cognito-idp.us-west-2.amazonaws.com/us-west-2_rvYFnQIxL",
            "client-id": "58k05jb8grukjjsudm5hhn1v87",
            "identity-pool-id": "us-west-2:64464b12-0bfb-4dea-ab35-5c22c6c245f6"
        },
        "ldap-ad-auth-handler": {
            "ldap-ad-connection-secrets": [LIST OF AD-SECRETS]
        },
        "batch-settings": {
            "initiators": [{
                "classes": ["A", "B"],
                "description": "initiator...."
            }],
            "jcl-file-location": "${s3-source}/batch/jcl",
            "program-path": "/m2/mount/libs/loadlib:$EFS_MOUNT/emergency/loadlib",
            "system-procedure-libraries":"SYS1.PROCLIB;SYS2.PROCLIB",
            "aliases": [
               {"alias": "FDSSORT", "program": "SORT"},
               {"alias": "MFADRDSU", "program": "ADRDSSU"}
            ]
        },
        "cics-settings": {
            "binary-file-location": "${s3-source}/cics/binaries",
            "csd-file-location": "${s3-source}/cics/def",
            "system-initialization-table": "BNKCICV"
        },
        "jes-printers": [
           {
             "name": "printerName",
              "classes": [
                 "A",
                 "B"
             ],
             "description": "printer desc....",
             "exit-module": {
                 "name": "lrsprte6"
                }
             }
         ],
        "xa-resources" : [{
            "name": "XASQL",
            "secret-manager-arn": "arn:aws:secrets:1234:us-east-1:secret:123456",
            "xa-connection-type": "postgres",
            "module": "${s3-source}/xa/ESPGSQLXA64.so"
        }],
        "runtime-settings": {
          "base-configuration-location": "${s3-source}/exported.json",
          "environment-variables": {
            "ES_JES_RESTART": "N",
            "EFS_MOUNT": "/m2/mount/efs",
            "LRSQ_ADDRESS": "<lrsq-address>"
          }
        }
    }
}
```

## Rocket Software definition details

The content in the definition section of the Rocket Software application definition file varies,
depending on the resources that your migrated mainframe application requires at
runtime.

### Listener(s) -

required

Specify a listener using the following structure:

```
"listeners": [{
    "port": 5101,
    "type": "tn3270"
}],
```

**port**

For tn3270, the default is 5101. For other types of service listeners,
the port varies. You can use any available port except for the
well-known ports of 0 to 1023. Each listener should have a distinctive
port. Listeners should not share ports. For more information, see [Listener Control](https://www.microfocus.com/documentation/enterprise-developer/ed70/ES-UNIX/GUID-63F6D8B0-024F-48D1-956A-1E079E4BD891.html "https://www.microfocus.com/documentation/enterprise-developer/ed70/ES-UNIX/GUID-63F6D8B0-024F-48D1-956A-1E079E4BD891.html") in the _Micro Focus Enterprise Server_
documentation.

**type**

Specifies the type of service listener. For more information, see
[Listeners](https://www.microfocus.com/documentation/enterprise-developer/ed70/ES-UNIX/HTPHMDSAL100.html "https://www.microfocus.com/documentation/enterprise-developer/ed70/ES-UNIX/HTPHMDSAL100.html") in the _Micro Focus Enterprise Server_
documentation.

### Data set locations

- required

Specify the data set location using the following structure.

```
"dataset-location": {
            "db-locations": [{
                "name": "Database1",
                "secret-manager-arn": "arn:aws:secrets:1234:us-east-1:secret:123456"
            }],
 }
```

**db-locations**

Specifies the location of the data sets that the migrated application
creates. Currently, AWS Mainframe Modernization supports only data sets from a single VSAM
database.

- `name` - Specifies the name of the database
  instance that contains the data sets that the migrated
  application creates.
- `secret-manager-arn` - Specifies the Amazon
  Resource Name (ARN) of the secret that contains the database
  credentials.

### Amazon Cognito

authentication and authorization handler - optional

AWS Mainframe Modernization uses Amazon Cognito for authentication and authorization for migrated applications.
Specify the Amazon Cognito authentication handler using the following structure.

```
"cognito-auth-handler": {
            "user-pool-id": "cognito-idp.`Region`.amazonaws.com/`Region`_rvYFnQIxL",
            "client-id": "58k05jb8grukjjsudm5hhn1v87",
            "identity-pool-id": "`Region`:64464b12-0bfb-4dea-ab35-5c22c6c245f6"
}
```

**user-pool-id**

Specifies the Amazon Cognito user pool that AWS Mainframe Modernization uses to authenticate users of
the migrated application.
The AWS Region for the user pool should match the AWS Region for the AWS Mainframe Modernization application.

**client-id**

Specifies the migrated application that the authenticated user can
access.

**identity-pool-id**

Specifies the Amazon Cognito identity pool where the authenticated user
exchanges a user pool token for credentials that allow the user to
access AWS Mainframe Modernization.
The AWS Region for the identity pool should match the AWS Region for the AWS Mainframe Modernization application.

### LDAP and Active

Directory handler - optional

You can integrate your application with Active Directory (AD) or any type of LDAP
server to make it possible for users of the application to use their LDAP/AD
credentials for authorization and authentication.

###### To integrate your application with AD

1. Follow the steps described in [Configuring Active Directory for Enterprise Server Security](https://www.microfocus.com/documentation/server-cobol/51/chessa64.htm "https://www.microfocus.com/documentation/server-cobol/51/chessa64.htm") in
   the Micro Focus Enterprise Server documentation.
2. Create an AWS Secrets Manager secret with your AD/LDAP details for each AD/LDAP
   server that you want to use with your application. For information on how to
   create a secret, see [Create an
   AWS Secrets Manager secret](../../../secretsmanager/latest/userguide.md "../../../secretsmanager/latest/userguide.md") in the AWS Secrets Manager User Guide. For secret
   type, choose **Other type of secret** and include the
   following key-value pairs.

```
{
    "connectionPath"       : "<HOST-ADDRESS>:<PORT>",
    "authorizedId"         : "<USER-FULL-DN>",
    "password"             : "<PASSWORD>",
    "baseDn"               : "<BASE-FULL-DN>",
    "userClassDn"          : "<USER-TYPE>",
    "userContainerDn"      : "<USER-CONTAINER-DN>",
    "groupContainerDn"     : "<GROUP-CONTAINER-DN>",
    "resourceContainerDn"  : "<RESOURCE-CONTAINER-DN>"
}
```

###### Security recommendations

    * For `connectionPath`, AWS Mainframe Modernization supports the LDAP and
     LDAP over SSL (LDAPS) protocols. We recommend using LDAPS
     because it is more secure and prevents credentials from
     appearing in network transmissions.
    * For `authorizedId` and `password`, we
     recommend that you specify the credentials of a user with no
     more permissions than the most restrictive read-only and
     verification permissions that are required for your application
     to run.
    * We recommend rotating the AD/LDAP credentials on a regular
     basis.
    * Do not create AD users with the username `awsuser`
     or `mfuser`. These two usernames are reserved for
     AWS use.

The following is an example.

```
{
    "connectionPath" : "ldaps://msad4.m2.example.people.aws.dev:636",
    "authorizedId" : "CN=LDAPUser,OU=Users,OU=msad4,DC=msad4,DC=m2,DC=example,DC=people,DC=aws,DC=dev",
    "password" : "ADPassword",
    "userContainerDn" : "CN=Enterprise Server Users,CN=Micro Focus,CN=Program Data,OU=msad4,DC=msad4,DC=m2,DC=example,DC=people,DC=aws,DC=dev",
    "groupContainerDn" : "CN=Enterprise Server Groups,CN=Micro Focus,CN=Program Data,OU=msad4,DC=msad4,DC=m2,DC=example,DC=people,DC=aws,DC=dev",
    "resourceContainerDn" : "CN=Enterprise Server Resources,CN=Micro Focus,CN=Program Data,OU=msad4,DC=msad4,DC=m2,DC=example,DC=people,DC=aws,DC=dev"
}
```

Create the secret with a customer-managed KMS key. You must grant AWS Mainframe Modernization
the `GetSecretValue` and `DescribeSecret` permissions
on the secret, and `Decrypt` and `DescribeKey`
permissions on the KMS key. For more information, see [Permissions for the KMS key](../../../secretsmanager/latest/userguide/security-encryption.md#security-encryption-authz "../../../secretsmanager/latest/userguide/security-encryption.md#security-encryption-authz") in the AWS Secrets Manager User Guide. 3. Add the following to your application definition.

```
"ldap-ad-auth-handler": {
    "ldap-ad-connection-secrets": [LIST OF AD/LDAP SECRETS]
}
```

The following is an example.

```
"ldap-ad-auth-handler": {
    "ldap-ad-connection-secrets": ["arn:aws:secrets:1234:us-east-1:secret:123456"]
}
```

If the application is integrated with LDAP and has been started, you must provide
credentials to execute at least one application related operations mentioned in the
list of supported authorizations.

The LDAP/AD authentication handler is available for Micro Focus (Rocket) 8.0.11
and later versions.

###### Note

Currently, the LDAP administrator has to provide "alter" permissions on the
`casstart` utility in the "OPERCMDS" enterprise server resources
in their LDAP directory. This needs to be done for all the required default
users (e.g., CICSUSER - if the application is CICS related) to start the
application successfully.

###### To provide LDAP user credentials for authentication and authorization

1. Create an AWS Secrets Manager with the following keys and values:

```
{
  "username" : "<USERNAME>",
  "password" : "<PASSWORD>"
}
```

###### Important

You should have the rights to execute `DescribeSecrets` and
`GetSecretValue` on the Secrets Manager being used. Also,
associate a KMS key and necessary permissions for the AWS Secrets Manager, as
mentioned in [Choosing a AWS KMS key](../../../secretsmanager/latest/userguide/security-encryption.md#security-encryption-choose-key "../../../secretsmanager/latest/userguide/security-encryption.md#security-encryption-choose-key"). 2. Choose the Secrets Manager parameter.

AWS console
While executing operations from AWS console, there will be an option to
choose the Secrets Manager that needs to be passed.

AWS CLI (or SDK)
While executing operations from AWS CLI (or SDK) the API
parameter `auth-secrets-manager-arn` should be passed
with the Secrets Manager ARN.

Here is the list of application operations that currently support
authorization:

- `StartBatchJob`
- `CancelBatchJobExecution`
- `ListBatchJobRestartPoints`

### Batch settings -

required

Specify the details required by the batch jobs that run as part of the application
using the following structure.

```
"batch-settings": {
            "initiators": [{
                "classes": ["A", "B"],
                "description": "initiator...."
            }],
            "jcl-file-location": "${s3-source}/batch/jcl",
            "program-path": "/m2/mount/libs/loadlib:$EFS_MOUNT/emergency/loadlib",
            "system-procedure-libraries":"SYS1.PROCLIB;SYS2.PROCLIB",
            "aliases": [
               {"alias": "FDSSORT", "program": "SORT"},
               {"alias": "MFADRDSU", "program": "ADRDSSU"}
    ]
}
```

**initiators**

Specifies a batch initiator that starts when the migrated application
starts successfully and continues running until the application stops.
You can define one or multiple classes per initiator. You can also
define multiple initiators. For example:

```
"batch-settings": {
            "initiators": [
                {
                  "classes": ["A", "B"],
                  "description": "initiator...."
                },
                {
                  "classes": ["C", "D"],
                  "description": "initiator...."
                }

        ],
 }
```

For more information, see [To define a batch initiator or printer SEP](https://www.microfocus.com/documentation/enterprise-developer/ed70/ES-UNIX/HHMTTHJCLE08.html "https://www.microfocus.com/documentation/enterprise-developer/ed70/ES-UNIX/HHMTTHJCLE08.html") in the
_Micro Focus Enterprise Server_ documentation.

- `classes` - Specifies the job classes that the
  initiator can run. You can use up to 36 characters. You can use
  the following characters: A-Z or 0-9.
- `description` - Describes what the initiator is
  for.

**jcl-file-location**

Specifies the location of the JCL (Job Control Language) files that
are required by the batch jobs the migrated application runs.

**program-path**

Specifies the path required to run batch jobs when a program in a JCL
is not in the default location. The different path names are separated
with a colon (:).

###### Note

The program path can only be an EFS path.

**system-procedure-libraries**

Specifies the default partitioned data sets that will be searched for
JCL procedures. The procedure is, however, not found in the JCL or via
the JCLLIB statements. These data sets must be cataloged and the catalog
name must be used. And the entries are separated with a semi-colon
(;).

**aliases**

Defines a mapping for the utility and program names used in JCL to the
implementation name of the utility. AWS and 3rd party batch utilities (e.g.
M2SFTP, M2WAIT, Syncsort, etc.) can optionally have aliases to eliminate
the need to change the JCL. For example:

- FDSSORT Alias FDSSORT for SORT and Alias FDSICET for
  ICETOOL
- ADRDSSU Alias MFADRDSU for ADRDSSU
- Syncsort Alias DMXMFSRT for SORT

### CICS settings -

required

Specify the details required for the CICS transactions that run as part of the
application using the following structure.

```
"cics-settings": {
            "binary-file-location": "${s3-source}/cics/binaries",
            "csd-file-location": "${s3-source}/cics/def",
            "system-initialization-table": "BNKCICV"
}
```

**binary-file-location**

Specifies the location of the CICS transaction program files.

**csd-file-location**

Specifies the location of the CICS resource definition (CSD) file for
this application. For more information, see [CICS Resource Definitions](https://www.microfocus.com/documentation/enterprise-developer/ed80/ES-UNIX/HRMTRHCSDS01.html "https://www.microfocus.com/documentation/enterprise-developer/ed80/ES-UNIX/HRMTRHCSDS01.html") in the
_Micro Focus Enterprise Server_ documentation.

**system-initialization-table**

Specifies the system initialization table (SIT) that the migrated
application uses. The name of the SIT table can be up to 8 characters.
You can use A-Z, 0-9, $, @, and #. For more information, see [CICS Resource Definitions](https://www.microfocus.com/documentation/enterprise-developer/ed70/ES-UNIX/HRMTRHCSDS01.html "https://www.microfocus.com/documentation/enterprise-developer/ed70/ES-UNIX/HRMTRHCSDS01.html") in the
_Micro Focus Enterprise Server_ documentation.

### Printers - optional

Specify a jes printer using the following structure.

```
"jes-printers": [
    {
        "name": "printerName",
        "classes": [
            "A",
            "B"
        ],
        "description": "printer desc....",
        "exit-module": {
            "name": "lrsprte6",
            "module" : "program"
        }
    }
],
```

###### Note

There can be a maximum of 25 printers configured for a given application.

**name**

(Required) Specifies the name to associate with this printer resource.
Names must be unique for each printer, and a limit of 128 alphanumeric
characters can be used.

**classes**

(Required) Specifies the output classes applicable to this printer
resource. A limit of 36 alphanumeric characters can be used.

**description**

(Optional) Additional descriptive text for the printer.

**exit-module**

(Optional) Specifies a custom module for print exit. There are no
default values, if not specified, no exit module will be used. You can
use either a managed print exit module or supply your own. Managed print
exit modules are defined using reserved name `lrsprte6` for
LRS queue or supply your own using the module parameter to specify the
location and name.

The structure of `exit-module` has two components:

- `name`- (Required), if `exit-module` is
  used. The name of the entry of the exit module. There is a limit
  on the exit module entry name of up to 8 characters.
- `module` - (Optional) The S3 location of the print
  exit module binary.

You can see more examples of defining the exit module in the [Printers](mf-app-config.md#mf-app-config-integations-printers "mf-app-config.md#mf-app-config-integations-printers") section.

### XA resources -

optional

Specify the details required for the XA resources that the application requires
using the following structure.

```
"xa-resources" : [{
            "name": "XASQL",
            "secret-manager-arn": "arn:aws:secrets:1234:us-east-1:secret:123456",
            "xa-connection-type": "postgres",
            "module": "${s3-source}/xa/ESPGSQLXA64.so"
}]
```

###### Note

XA resource definition has been updated to include an optional
`xa-connection-type` field. If not provided, the connection type
is assumed to be “postgres”.

**name**

(Required) Specifies the name of the XA resource.

**secret-manager-arn**

(Required) Specifies the Amazon Resource Name (ARN) for the secret
that contains the credentials for connecting to the database.

**xa-connection-type**

(Optional) Specifies the XA resource connection type.

**module**

(Required) Specifies the location of the RM switch module executable
file. For more information, see [Planning and Designing XARs](https://www.microfocus.com/documentation/enterprise-developer/ed60/ES-WIN/GUID-91C0E7E4-C012-4DF2-8996-CF6C52437FB7.html "https://www.microfocus.com/documentation/enterprise-developer/ed60/ES-WIN/GUID-91C0E7E4-C012-4DF2-8996-CF6C52437FB7.html") in the
_Micro Focus Enterprise Server_ documentation.

### Runtime settings -

optional

Specify the details required for runtime settings to manage permitted environment
variables using the following structure.

```
"runtime-settings": {
          "base-configuration-location": "${s3-source}/exported.json",
          "environment-variables": {
            "ES_JES_RESTART": "N",
            "EFS_MOUNT": "/m2/mount/efs"
    }
}
```

**base-configuration-location**

(Optional) Specifies the location for bulk import for a Micro Focus server
configuration. This file should be a valid JSON and present in the same
S3 location as the application artifacts location defined above. To
export configuration from an existing application, see [To export a region from ESCWA](https://www.microfocus.com/documentation/enterprise-developer/ed90/ED-Eclipse/GUID-6CDD00CC-4086-4602-8EE2-0C07E04ACC6A.html "https://www.microfocus.com/documentation/enterprise-developer/ed90/ED-Eclipse/GUID-6CDD00CC-4086-4602-8EE2-0C07E04ACC6A.html")
_section_ in the _Rocket software documentation_.

**environment-variables**

Specifies Micro Focus supported environment variables that are applied
to this application’s runtime.

- `ES_JES_RESTART` is a Rocket Software environment variable
  that enables JCL restart processing. Optionally, you can also
  use `ES_ALLOC_OVERRIDE` as a Rocket Software environment
  variable.
- `EFS_MOUNT` is a custom environment variable that your
  application might use to identify where the environment's EFS
  mount is located.

You can access all the [Rocket Software environment variables](https://www.microfocus.com/documentation/enterprise-developer/ed80/ES-UNIX/GUID-F0C24B4E-9720-47C1-A77C-2E9B30CC4328.html "https://www.microfocus.com/documentation/enterprise-developer/ed80/ES-UNIX/GUID-F0C24B4E-9720-47C1-A77C-2E9B30CC4328.html") in the _Rocket Enterprise Server for UNIX
guide._
