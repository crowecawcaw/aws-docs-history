# Create the EMR security

configuration

**Creating an Amazon EMR Security Configuration for Apache
Ranger**

Before you launch an Amazon EMR cluster integrated with Apache Ranger, create a
security configuration.

Console

###### To create a security configuration that specifies the AWS

Ranger integration option

1. In the Amazon EMR console, select **Security
   configurations**, then
   **Create**.
2. Type a **Name** for the security
   configuration. You use this name to specify the security
   configuration when you create a cluster.
3. Under **AWS Ranger Integration**, select
   **Enable fine-grained access control managed by
   Apache Ranger**.
4. Select your **IAM role for Apache Ranger** to
   apply. For more information, see [IAM roles for native integration with Apache
   Ranger](emr-ranger-iam.md "emr-ranger-iam.md").
5. Select your **IAM role for other AWS
   services** to apply.
6. Configure the plugins to connect to the Ranger Admin server by
   entering the Secrets Manager ARN for the Admin server and the
   address.
7. Select the applications to configure Ranger plugins. Enter
   the Secrets Manager ARN that contains the private TLS certificate
   for the plugin.

If you do not configure Apache Spark or Apache Hive, and they
are selected as an application for your cluster, the request
fails. 8. Set up other security configuration options as appropriate and
choose **Create**. You must enable Kerberos
authentication using the cluster-dedicated or external
KDC.

###### Note

You cannot currently use the console to create a security
configuration that specifies the AWS Ranger integration option in
the AWS GovCloud (US) Region. Security configuration can be done using
the CLI.

CLI

###### To create a security configuration for Apache Ranger

integration

1. Replace `<ACCOUNT
ID>` with your AWS account
   ID.
2. Replace `<REGION>`
   with the Region that the resource is in.
3. Specify a value for `TicketLifetimeInHours` to
   determine the period for which a Kerberos ticket issued by the
   KDC is valid.
4. Specify the address of the Ranger Admin server for
   `AdminServerURL`.

```
{
    "AuthenticationConfiguration": {
        "KerberosConfiguration": {
            "Provider": "ClusterDedicatedKdc",
            "ClusterDedicatedKdcConfiguration": {
                "TicketLifetimeInHours": 24
            }
        }
    },
    "AuthorizationConfiguration":{
      "RangerConfiguration":{
         "AdminServerURL":"https://_`<RANGER ADMIN SERVER IP>`_:6182",
         "RoleForRangerPluginsARN":"arn:aws:iam::_`<ACCOUNT ID>`_:role/_`<RANGER PLUGIN DATA ACCESS ROLE NAME>`_",
         "RoleForOtherAWSServicesARN":"arn:aws:iam::_`<ACCOUNT ID>`_:role/_`<USER ACCESS ROLE NAME>`_",
         "AdminServerSecretARN":"arn:aws:secretsmanager:_`<REGION>`_:_`<ACCOUNT ID>`_:secret:_`<SECRET NAME THAT PROVIDES ADMIN SERVERS PUBLIC TLS CERTIFICATE WITHOUT VERSION>`_",
         "RangerPluginConfigurations":[
            {
               "App":"Spark",
               "ClientSecretARN":"arn:aws:secretsmanager:_`<REGION>`_:_`<ACCOUNT ID>`_:secret:_`<SECRET NAME THAT PROVIDES SPARK PLUGIN PRIVATE TLS CERTIFICATE WITHOUT VERSION>`_",
               "PolicyRepositoryName":"`<SPARK SERVICE NAME eg. amazon-emr-spark>`"
            },
            {
               "App":"Hive",
               "ClientSecretARN":"arn:aws:secretsmanager:_`<REGION>`_:_`<ACCOUNT ID>`_:secret:_`<SECRET NAME THAT PROVIDES Hive PLUGIN PRIVATE TLS CERTIFICATE WITHOUT VERSION>`_",
               "PolicyRepositoryName":"`<HIVE SERVICE NAME eg. Hivedev>`"
            },
            {
               "App":"EMRFS-S3",
               "ClientSecretARN":"arn:aws:secretsmanager:_`<REGION>`_:_`<ACCOUNT ID>`_:secret:_`<SECRET NAME THAT PROVIDES EMRFS S3 PLUGIN PRIVATE TLS CERTIFICATE WITHOUT VERSION>`_",
               "PolicyRepositoryName":"`<EMRFS S3 SERVICE NAME eg amazon-emr-emrfs>`"
            },
	      {
               "App":"Trino",
               "ClientSecretARN":"arn:aws:secretsmanager:_`<REGION>`_:_`<ACCOUNT ID>`_:secret:_`<SECRET NAME THAT PROVIDES TRINO PLUGIN PRIVATE TLS CERTIFICATE WITHOUT VERSION>`_",
               "PolicyRepositoryName":"`<TRINO SERVICE NAME eg amazon-emr-trino>`"
            }
         ],
         "AuditConfiguration":{
            "Destinations":{
               "AmazonCloudWatchLogs":{
                  "CloudWatchLogGroup":"arn:aws:logs:`<REGION>`:_`<ACCOUNT ID>`_:log-group:_`<LOG GROUP NAME FOR AUDIT EVENTS>`_"
               }
            }
         }
      }
   }
}
```

The PolicyRespositoryNames are the service names that are specified in
your Apache Ranger Admin.

Create an Amazon EMR security configuration with the following command.
Replace security-configuration with a name of your choice. Select this
configuration by name when you create your cluster.

```
aws emr create-security-configuration \
--security-configuration file://./security-configuration.json \
--name security-configuration
```

**Configure Additional Security Features**

To securely integrate Amazon EMR with Apache Ranger, configure the following EMR
security features:

- Enable Kerberos authentication using the cluster-dedicated or external
  KDC. For instructions, see [Use Kerberos for
  authentication with Amazon EMR](emr-kerberos.md "emr-kerberos.md").
- (Optional) Enable encryption in transit or at rest. For more information,
  see [Encryption options for Amazon EMR](emr-data-encryption-options.md "emr-data-encryption-options.md").
  For more information, see [Security in Amazon EMR](emr-security.md "emr-security.md").
