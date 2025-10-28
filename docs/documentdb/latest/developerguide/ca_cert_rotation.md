# Updating your Amazon DocumentDB TLS

certificates

###### Topics

- [Updating your application and Amazon DocumentDB cluster](#ca_cert_rotation-updating_application "#ca_cert_rotation-updating_application")
- [Automatic server certificate rotation](#ca-cert-rotation-auto "#ca-cert-rotation-auto")
- [Troubleshooting](#ca_cert_rotation-troubleshooting "#ca_cert_rotation-troubleshooting")
- [Frequently Asked Questions](#ca_cert_rotation-faq "#ca_cert_rotation-faq")
  The certificate authority (CA) certificate for Amazon DocumentDB clusters was updated in August of 2024.
  If you are using Amazon DocumentDB clusters with Transport Layer Security (TLS) enabled (the default setting) and you
  have not rotated your client application and server certificates, the following steps are
  required to mitigate connectivity issues between your application and your Amazon DocumentDB clusters.

- [Step 1: Download the new CA certificate and update your application](#ca_cert_rotation-updating_application_step1 "#ca_cert_rotation-updating_application_step1")
- [Step 2: Update the server certificate](#ca_cert_rotation-updating_application_step2 "#ca_cert_rotation-updating_application_step2")
  The CA and server certificates were updated as part of standard
  maintenance and security best practices for Amazon DocumentDB. Client applications must add the new CA certificates to their trust stores, and
  existing Amazon DocumentDB instances must be updated to use the new CA certificates before this
  expiration date.

## Updating your application and Amazon DocumentDB cluster

Follow the steps in this section to update your application's CA certificate bundle
([Step 1](ca_cert_rotation.md#ca_cert_rotation-updating_application_step1 "ca_cert_rotation.md#ca_cert_rotation-updating_application_step1")) and your cluster's server certificates ([Step 2](ca_cert_rotation.md#ca_cert_rotation-updating_application_step2 "ca_cert_rotation.md#ca_cert_rotation-updating_application_step2")). Before you apply the changes to your production environments, we
strongly recommend testing these steps in a development or staging environment.

###### Note

You must complete Steps 1 and 2 in each AWS Region in which you have Amazon DocumentDB
clusters.

### Step 1: Download the new CA certificate and update your application

Download the new CA certificate and update your application
to use the new CA certificate to create TLS connections to Amazon DocumentDB. Download the new CA
certificate bundle from [https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem](https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem "https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem"). This
operation downloads a file named `global-bundle.pem`.

###### Note

If you are accessing the keystore that contains both the old CA certificate
(`rds-ca-2019-root.pem`) and the new CA certificates
(`rds-ca-rsa2048-g1`, `rds-ca-rsa4096-g1`, `rds-ca-ecc384-g1`), verify that the keystore selects
`global-bundle`.

```
wget https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem
```

Next, update your applications to use the new certificate
bundle. The new CA bundle contains both the old CA certificate (rds-ca-2019) and the new CA certificates (rds-ca-rsa2048-g1, rds-ca-rsa4096-g1, rds-ca-ecc384-g1).
By having both CA certificates in the new CA bundle, you can update your application and cluster in two steps.

For Java applications, you must create a new trust store with the new CA certificate.
For instructions, see the Java tab in the [Connecting with TLS enabled](connect_programmatically.md#connect_programmatically-tls_enabled "connect_programmatically.md#connect_programmatically-tls_enabled") topic.

To verify that your application is
using the latest CA certificate bundle, see [How can I be sure that I'm using the
newest CA bundle?](#ca_cert_rotation-faq_question13 "#ca_cert_rotation-faq_question13") If you're already using the latest
CA certificate bundle in your application, you can skip to Step 2.

For examples of using a CA bundle with your application, see [Encrypting data in transit](security.encryption.md "security.encryption.md") and [Connecting with TLS enabled](connect_programmatically.md#connect_programmatically-tls_enabled "connect_programmatically.md#connect_programmatically-tls_enabled").

###### Note

Currently, the MongoDB Go Driver 1.2.1 only accepts one CA server certificate in
`sslcertificateauthorityfile`. Please see [Connecting with TLS enabled](connect_programmatically.md#connect_programmatically-tls_enabled "connect_programmatically.md#connect_programmatically-tls_enabled") for connecting to Amazon DocumentDB using Go when TLS is enabled.

### Step 2: Update the server certificate

After the application has been updated to use the new CA bundle, the next step is to
update the server certificate by modifying each instance in an Amazon DocumentDB cluster. To
modify instances to use the new server certificate, see the following instructions.

Amazon DocumentDB provides the following CAs to sign the DB server certificate for a DB instance:

- **rds-ca-ecc384-g1**—Uses a certificate authority with ECC 384 private key algorithm and SHA384 signing algorithm.
  This CA supports automatic server certificate rotation.
  This is only supported on Amazon DocumentDB 4.0 and 5.0.
- **rds-ca-rsa2048-g1**—Uses a certificate authority with RSA 2048 private key algorithm and SHA256 signing algorithm in most AWS regions.
  This CA supports automatic server certificate rotation.
- **rds-ca-rsa4096-g1**—Uses a certificate authority with RSA 4096 private key algorithm and SHA384 signing algorithm. This CA supports automatic server certificate rotation.

###### Note

If you are using the AWS CLI, you can see the validities of the certificate authorities listed above by using [describe-certificates](../../../cli/latest/reference/docdb/describe-certificates.md "../../../cli/latest/reference/docdb/describe-certificates.md").

These CA certificates are included in the regional and global certificate bundle.
When you use the rds-ca-rsa2048-g1, rds-ca-rsa4096-g1, or rds-ca-ecc384-g1 CA with a database, Amazon DocumentDB manages the DB server certificate on the database.
Amazon DocumentDB rotates the DB server certificate automatically before it expires.

###### Note

Amazon DocumentDB does not require a reboot for certificate rotation if your cluster is running on the following engine patch versions:

- Amazon DocumentDB 3.6: 1.0.208662 or greater
- Amazon DocumentDB 4.0: 2.0.10179 or greater
- Amazon DocumentDB 5.0: 3.0.4780 or greater
  You can determine the current Amazon DocumentDB engine patch version by running the following command: `db.runCommand({getEngineVersion: 1})`.

Before updating the server certificate, ensure that you have completed [Step 1](#ca_cert_rotation-updating_application_step1 "#ca_cert_rotation-updating_application_step1").

Using the AWS Management Console
Complete the following steps to identify and rotate the old server certificate
for your existing Amazon DocumentDB instances using the AWS Management Console.

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at
   [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the list of Regions in the upper-right corner of the screen, choose
   the AWS Region in which your clusters reside.
3. In the navigation pane on the left side of the console, choose
   **Clusters**.
4. You may need to identify which instances are still on the old server
   certificate (`rds-ca-2019`). You can do this in the
   **Certificate authority** column which is located on the far right of the **Clusters** table.
5. In the **Clusters** table, you’ll see the column
   **Cluster identifier** on the far left. Your instances are listed under
   clusters, similar to the screenshot below.

![Image of the Clusters navigation box showing a list of existing cluster links and their corresponding instance links.](images/choose-clusters.png) 6. Check the box to the left of the instance you are interested in. 7. Choose **Actions** and then choose
**Modify**. 8. Under **Certificate authority**, select the new server
certificate (`rds-ca-rsa2048-g1`) for this instance. 9. You can see a summary of the changes on the next page. Note that there is
an extra alert to remind you to ensure that your application is using the
latest certificate CA bundle before modifying the instance to avoid causing
an interruption in connectivity. 10. You can choose to apply the modification during your next maintenance
window or apply immediately. If your intention is to modify the server
certificate immediately, use the **Apply Immediately**
option. 11. Choose **Modify instance** to complete the
update.

Using the AWS CLI
Complete the following steps to identify and rotate the old server
certificate for your existing Amazon DocumentDB instances using the AWS CLI.

1. To modify the instances immediately, execute the following command for
   each instance in the cluster.

```
aws docdb modify-db-instance --db-instance-identifier `<yourInstanceIdentifier>` --ca-certificate-identifier rds-ca-rsa2048-g1 --apply-immediately
```

2. To modify the instances in your clusters to use the new CA certificate
   during your cluster’s next maintenance window, execute the following command
   for each instance in the cluster.

```
aws docdb modify-db-instance --db-instance-identifier `<yourInstanceIdentifier>` --ca-certificate-identifier rds-ca-rsa2048-g1 --no-apply-immediately
```

## Automatic server certificate rotation

Amazon DocumentDB supports automatic server certificate rotation.
The server certificate is the leaf certificate issued to each cluster instance.
As opposed to the root CA certificates, the server certificates have short (12 months) validity and Amazon DocumentDB automatically handles their rotation without any action from you.
Amazon DocumentDB uses the same root CA for this automatic rotation, so you don't need to download a new CA bundle.

###### Important

When connecting to your Amazon DocumentDB cluster, we recommend that you trust the root CA bundle as opposed to directly trusting each server certificate.
This will prevent connection errors after the server certificate is rotated.
See [Connecting with TLS enabled](connect_programmatically.md#connect_programmatically-tls_enabled "connect_programmatically.md#connect_programmatically-tls_enabled").

Amazon DocumentDB attempts to rotate your server certificate in your preferred maintenance window at the server certificate half life.
The new server certificate is valid for 12 months.

Use the [`describe-db-engine-versions`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-engine-versions.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-engine-versions.html") command and inspect the `SupportsCertificateRotationWithoutRestart` flag to identify whether the engine version supports rotating the certificate without restart.

###### Note

Amazon DocumentDB supports server certificate rotation without restarts if your cluster is running on the following engine patch versions:

- Amazon DocumentDB 3.6: 1.0.208662 or greater
- Amazon DocumentDB 4.0: 2.0.10179 or greater
- Amazon DocumentDB 5.0: 3.0.4780 or greater
  You can determine the current Amazon DocumentDB engine patch version by running this command: `db.runCommand({getEngineVersion: 1})`.

If you are using an older engine patch version, Amazon DocumentDB will rotate the server certificate and schedule a database restart event on your preferred maintenance window.

## Troubleshooting

If you are having issues connecting to your cluster as part of the certificate rotation,
we suggest the following:

- **Verify that your clients are using the latest certificate
  bundle.** See [How can I be sure that I'm using the
  newest CA bundle?](#ca_cert_rotation-faq_question13 "#ca_cert_rotation-faq_question13").
- **Verify that your instances are using the latest
  certificate.** See [How do I know which of my Amazon DocumentDB
  instances are using the old/new server certificate?](#ca_cert_rotation-faq_question5 "#ca_cert_rotation-faq_question5").
- **Verify that the latest certificate CA is being utilized by
  your application.** Some drivers, like Java and Go, require extra code to
  import multiple certificates from a certificate bundle to the trust store. For more
  information on connecting to Amazon DocumentDB with TLS, see [Connecting programmatically to Amazon DocumentDB](connect_programmatically.md "connect_programmatically.md").
- **Contact support.** If you have questions or issues,
  contact [Support](https://aws.amazon.com/premiumsupport "https://aws.amazon.com/premiumsupport").

## Frequently Asked Questions

The following are answers to some common questions about TLS certificates.

### What if I have questions or

issues?

If you have questions or issues, contact [Support](https://aws.amazon.com/premiumsupport "https://aws.amazon.com/premiumsupport").

### How do I know whether I'm using TLS to

connect to my Amazon DocumentDB cluster?

You can determine whether your cluster is using TLS by examining the `tls`
parameter for your cluster’s cluster parameter group. If the `tls` parameter
is set to `enabled`, you are using the TLS certificate to connect to your
cluster. For more information, see [Managing Amazon DocumentDB cluster parameter groups](cluster_parameter_groups.md "cluster_parameter_groups.md").

### Why are you updating the CA and server

certificates?

The Amazon DocumentDB CA and server certificates are being updated as part
of standard maintenance and security best practices for Amazon DocumentDB.

### What happens if I don't take any action

by the expiration date?

If you are using TLS to connect to your Amazon DocumentDB cluster with an expired CA certificate, your applications that connect via TLS will no longer be able to communicate with the Amazon DocumentDB cluster.

Amazon DocumentDB will not rotate your database certificates automatically before expiration.
You must update your applications and clusters to use the new CA certificates before or
after the expiration date.

### How do I know which of my Amazon DocumentDB

instances are using the old/new server certificate?

To identify the Amazon DocumentDB instances that still use the old server certificate, you can
use either the Amazon DocumentDB AWS Management Console or the AWS CLI.

###### To identify the instances in your clusters that are using the older

certificate

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the list of Regions in the upper-right corner of the screen, choose
   the AWS Region in which your instances reside.
3. In the navigation pane on the left side of the console, choose
   **Clusters**.
4. The **Certificate authority**
   column (near the far right of the table) shows which instances are still on the old server
   certificate (`rds-ca-2019`) and the new server certificate
   (`rds-ca-rsa2048-g1`).
   To identify the instances in your clusters that are using the older server
   certificate, use the `describe-db-clusters` command with the following
   .

```
aws docdb describe-db-instances \
    --filters Name=engine,Values=docdb \
    --query 'DBInstances[*].{CertificateVersion:CACertificateIdentifier,InstanceID:DBInstanceIdentifier}'

```

### How do I modify individual instances in

my Amazon DocumentDB cluster to update the server certificate?

We recommend that you update server certificates for all instances in a given cluster
at the same time. To modify the instances in your cluster, you can use either the
console or the AWS CLI.

###### Note

Before updating the server certificate, ensure that you have completed [Step 1](ca_cert_rotation.md#ca_cert_rotation-updating_application_step1 "ca_cert_rotation.md#ca_cert_rotation-updating_application_step1").

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the list of Regions in the upper-right corner of the screen, choose
   the AWS Region in which your clusters reside.
3. In the navigation pane on the left side of the console, choose
   **Clusters**.
4. The **Certificate authority** column (near the far right of the table)
   shows which instances are still on the old server certificate
   (`rds-ca-2019`).
5. In the **Clusters** table, under **Cluster identifier**, select an instance to modify.
6. Choose **Actions** and then choose
   **Modify**.
7. Under **Certificate
   authority**, select the new server certificate
   (`rds-ca-rsa2048-g1`) for this instance.
8. You can see a summary of the changes on the next page. Note that there is
   an extra alert to remind you to ensure that your application is using the
   latest certificate CA bundle before modifying the instance to avoid causing
   an interruption in connectivity.
9. You can choose to apply the modification during your next maintenance
   window or apply immediately.
10. Choose **Modify instance** to complete the
    update.
    Complete the following steps to identify and rotate the old server
    certificate for your existing Amazon DocumentDB instances using the AWS CLI.

11. To modify the instances immediately, execute the following command for
    each instance in the cluster.

```
aws docdb modify-db-instance --db-instance-identifier `<yourInstanceIdentifier>` --ca-certificate-identifier rds-ca-rsa2048-g1 --apply-immediately
```

2. To modify the instances in your clusters to use the new CA certificate
   during your cluster’s next maintenance window, execute the following command
   for each instance in the cluster.

```
aws docdb modify-db-instance --db-instance-identifier `<yourInstanceIdentifier>` --ca-certificate-identifier rds-ca-rsa2048-g1 --no-apply-immediately
```

### What happens if I add a new instance to

an existing cluster?

All new instances that are created use the old server
certificate and require TLS connections using the old CA certificate. Any new Amazon DocumentDB
instances created after January 25, 2024 will default to using the new
certificate rds-ca-rsa2048-g1.

### What happens if there is an instance

replacement or failover on my cluster?

If there is an instance replacement in your cluster, the new instance that is created
continues to use the same server certificate that the instance was previously using. We
recommend that you update server certificates for all instances at the same time. If a
failover occurs in the cluster, the server certificate on the new primary is
used.

### If I'm not using TLS to connect to my

cluster, do I still need to update each of my instances?

We highly recommend enabling TLS.
In the event that you do not enable TLS, we still recommend rotating the certificates on your Amazon DocumentDB instances in the event you plan to use TLS to connect to your clusters in the future.
If you never plan to use TLS to connect to your Amazon DocumentDB clusters, no action is needed.

### If I'm not using TLS to connect to my

cluster but I plan to in the future, what should I do?

If you created a cluster before January, 2024, follow
[Step 1](ca_cert_rotation.md#ca_cert_rotation-updating_application_step1 "ca_cert_rotation.md#ca_cert_rotation-updating_application_step1") and [Step 2](ca_cert_rotation.md#ca_cert_rotation-updating_application_step2 "ca_cert_rotation.md#ca_cert_rotation-updating_application_step2") in the previous section to ensure that your application is using the
updated CA bundle, and that each Amazon DocumentDB instance is using the latest server
certificate. If you create a cluster after January 25, 2024, your cluster will already
have the latest server certificate (rds-ca-rsa2048-g1). To verify that your application is using the latest
CA bundle, see [If I'm not using TLS to connect to my
cluster, do I still need to update each of my instances?](#ca_cert_rotation-faq_question10 "#ca_cert_rotation-faq_question10")

### Can the

deadline be extended beyond August, 2024?

If your applications are connecting via TLS, the deadline
cannot be extended.

### How can I be sure that I'm using the

newest CA bundle?

To verify that you have the newest bundle, use the following command.
To run this command, you must have java installed and the java tools need to be in the PATH variable of your shell.
For more information, see [Using Java](https://www.java.com/en/download/help/path.html "https://www.java.com/en/download/help/path.html")

```
keytool -printcert -v -file global-bundle.pem
```

```
keytool -printcert -v -file global-bundle.p7b
```

### Why do I see "RDS" in the name of the

CA bundle?

For certain management features, such as certificate management, Amazon DocumentDB uses
operational technology that is shared with Amazon Relational Database Service (Amazon RDS).

### When will the new certificate

expire?

The new server certificate will expire (generally) as follows:

- **rds-ca-rsa2048-g1**—Expires 2061
- **rds-ca-rsa4096-g1**—Expires 2121
- **rds-ca-ecc384-g1**—Expires 2121

### What kind of errors will I see if I don't take action before the certificate expires?

Error messages will vary depending on your driver. In general, you'll see certificate validation errors that contain the string "certificate has expired".

### If I applied the new server

certificate, can I revert it back to the old server certificate?

If you need to revert an instance to the old server certificate, we recommend that
you do so for all instances in the cluster. You can revert the server certificate for
each instance in a cluster by using the AWS Management Console or the AWS CLI.

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the list of Regions in the upper-right corner of the screen, choose
   the AWS Region in which your clusters reside.
3. In the navigation pane on the left side of the console, choose
   **Clusters**.
4. In the **Clusters** table, under **Cluster identifier**, select an instance to modify. Choose **Actions**, and
   then choose **Modify**.
5. Under **Certificate
   authority**, you can select the old server certificate
   (`rds-ca-2019`).
6. Choose **Continue** to view a summary of your
   modifications.
7. In this resulting page, you can choose to schedule your modifications to
   be applied in the next maintenance window or apply your modifications
   immediately. Make your selection, and choose **Modify
   instance**.

###### Note

If you choose to apply your modifications immediately, any changes in
the pending modifications queue are also applied. If any of the pending
modifications require downtime, choosing this option can cause unexpected
downtime.

```
aws docdb modify-db-instance --db-instance-identifier `<db_instance_name>` ca-certificate-identifier rds-ca-2019 `<--apply-immediately | --no-apply-immediately>`
```

If you choose `--no-apply-immediately`, the changes will be applied
during the cluster’s next maintenance window.

### If I restore from a snapshot or a

point in time restore, will it have the new server certificate?

If you restore a snapshot or perform a point-in-time restore
after August, 2024, the new cluster that is created will use the new CA
certificate.

### What if I’m having issues connecting

directly to my Amazon DocumentDB cluster from any Mac OS?

Mac OS has updated the requirements for trusted certificates. Trusted
certificates must now be valid for 397 days or fewer (see [https://support.apple.com/en-us/HT211025](https://support.apple.com/en-us/HT211025 "https://support.apple.com/en-us/HT211025")).

###### Note

This restriction is observed in newer versions of Mac OS.

Amazon DocumentDB instance certificates are
valid for over four years, longer than the Mac OS maximum. In order to connect
directly to an Amazon DocumentDB cluster from a computer running Mac OS, you must allow
invalid certificates when creating the TLS connection. In this case, invalid
certificates mean that the validity period is longer than 397 days. You should
understand the risks before allowing invalid certificates when connecting to your
Amazon DocumentDB cluster.

To connect to an Amazon DocumentDB cluster from Mac OS using the AWS CLI, use the
`tlsAllowInvalidCertificates` parameter.

```
mongo --tls --host <hostname> --username <username> --password <password> --port 27017 --tlsAllowInvalidCertificates
```
