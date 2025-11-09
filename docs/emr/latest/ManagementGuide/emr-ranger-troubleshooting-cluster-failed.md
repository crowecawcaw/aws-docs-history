# EMR cluster failed to

provision

There are several reasons why an Amazon EMR cluster may fail to start. Here are a few
ways to diagnose the issue.

**Check EMR provisioning logs**

Amazon EMR uses Puppet to install and configure applications on a cluster. Looking at
the logs will provide details as to if there are any errors during the provisioning
phase of a cluster. The logs are accessible on cluster or S3 if logs are configured
to be pushed to S3.

The logs are stored in
`/var/log/provision-node/apps-phase/0/{UUID}/puppet.log` on the disk
and `s3://<LOG LOCATION>/<CLUSTER ID>/node/<EC2 INSTANCE
 ID>/provision-node/apps-phase/0/{UUID}/puppet.log.gz.`

**Common Error Messages**

| Error message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Cause                                                                                                                                                                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`Puppet (err): Systemd start for emr-record-server<br>failed! journalctl log for<br>emr-record-server:`**                                                                                                                                                                                                                                                                                                                                                                                                                                                       | EMR Record Server failed to start. See EMR Record Server logs<br>below.                                                                                                                                                                                                                                        |
| **`Puppet (err): Systemd start for emr-record-server<br>failed! journalctl log for<br>emrsecretagent:`**                                                                                                                                                                                                                                                                                                                                                                                                                                                          | EMR Secret Agent failed to start. See Check Secret Agent logs<br>below.                                                                                                                                                                                                                                        |
| **`/Stage[main]/Ranger_plugins::Ranger_hive_plugin/Ranger_plugins::Prepare_two_way_tls[configure<br>2-way TLS in Hive plugin]/Exec[create keystore and<br>truststore for Ranger Hive plugin]/returns (notice):<br>140408606197664:error:0906D06C:PEM routines:PEM_read_bio:no<br>start line:pem_lib.c:707:Expecting: ANY PRIVATE<br>KEY`**                                                                                                                                                                                                                        | The private TLS certificate in Secret Manager for the Apache<br>Ranger plugin certificate is not in the correct format or is not<br>a private certificate. See [TLS certificates for Apache Ranger integration with Amazon EMR](emr-ranger-admin-tls.md "emr-ranger-admin-tls.md") for certificate<br>formats. |
| **`/Stage[main]/Ranger_plugins::Ranger_s3_plugin/Ranger_plugins::Prepare_two_way_tls[configure<br>2-way TLS in Ranger s3 plugin]/Exec[create keystore and<br>truststore for Ranger amazon-emr-s3 plugin]/returns<br>(notice): An error occurred (AccessDeniedException) when<br>calling the GetSecretValue operation: User:<br>arn:aws:sts::XXXXXXXXXXX:assumed-role/EMR_EC2_DefaultRole/i-XXXXXXXXXXXX<br>is not authorized to perform: secretsmanager:GetSecretValue<br>on resource:<br>arn:aws:secretsmanager:us-east-1:XXXXXXXXXX:secret:AdminServer-XXXXX`** | The EC2 Instance profile role does not have the correct<br>permissions to retrieve the TLS certificates from Secrets<br>Agent.                                                                                                                                                                                 |

**Check SecretAgent logs**

Secret Agent logs are located at `/emr/secretagent/log/` on an EMR
node, or in the `s3://<LOG LOCATION>/<CLUSTER ID>/node/<EC2
 INSTANCE ID>/daemons/secretagent/` directory in S3.

**Common Error Messages**

| Error message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Cause                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`Exception in thread "main"<br>com.amazonaws.services.securitytoken.model.AWSSecurityTokenServiceException:<br>User:<br>arn:aws:sts::XXXXXXXXXXXX:assumed-role/EMR_EC2_DefaultRole/i-XXXXXXXXXXXXXXX<br>is not authorized to perform: sts:AssumeRole on resource:<br>arn:aws:iam::XXXXXXXXXXXX:role/*RangerPluginDataAccessRole*<br>(Service: AWSSecurityTokenService; Status Code: 403; Error<br>Code: AccessDenied; Request ID:<br>XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX; Proxy:<br>null)`** | The above exception means that the EMR EC2 instance profile<br>role does not have permissions to assume the role **RangerPluginDataAccessRole**. See [IAM roles for native integration with Apache<br>Ranger](emr-ranger-iam.md "emr-ranger-iam.md"). |
| **`ERROR qtp54617902-149: Web App Exception<br>Occurred`**<br>**`javax.ws.rs.NotAllowedException: HTTP 405 Method<br>Not Allowed`**                                                                                                                                                                                                                                                                                                                                                             | These errors can be safely ignored.                                                                                                                                                                                                                   |

**Check Record Server Logs (for SparkSQL)**

EMR Record Server logs are available at /var/log/emr-record-server/ on an EMR
node, or they can be found in the s3://<LOG LOCATION>/<CLUSTER
 ID>/node/<EC2 INSTANCE ID>/daemons/emr-record-server/ directory in
S3.

**Common Error Messages**

| Error message                                                                                                                                                          | Cause                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`InstanceMetadataServiceResourceFetcher:105<br>• []<br>Fail to retrieve token`**<br>**`com.amazonaws.SdkClientException: Failed to connect<br>to service endpoint`** | The EMR SecretAgent failed to come up or is having an issue.<br>Inspect the SecretAgent logs for errors and the puppet script to<br>determine if there were any provisioning errors. |
