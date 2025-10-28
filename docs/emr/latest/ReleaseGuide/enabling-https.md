# Enabling HTTPS with Apache Livy

This topic is relevant if you are running Amazon EMR 7.3.0 or an earlier release. Beginning with release 7.4.0, HTTPS is enabled with Apache Livy by default.

1. Provision an Amazon EMR cluster with transit encryption enabled. To learn more
   about encryption, see [Encrypt data at
   rest and in transit](../ManagementGuide/emr-data-encryption.md "../ManagementGuide/emr-data-encryption.md").
2. Create a file called `livy_ssl.sh` with the following
   contents.

```
#!/bin/bash

KEYSTORE_FILE=`awk '/ssl.server.keystore.location/{getline; print}' /etc/hadoop/conf/ssl-server.xml | sed -e 's/<[^>]*>//g' | tr -d ' \t\n\r\f'`
KEYSTORE_PASS=`awk '/ssl.server.keystore.password/{getline; print}' /etc/hadoop/conf/ssl-server.xml | sed -e 's/<[^>]*>//g' | tr -d ' \t\n\r\f'`
KEY_PASS=`awk '/ssl.server.keystore.keypassword/{getline; print}' /etc/hadoop/conf/ssl-server.xml | sed -e 's/<[^>]*>//g' | tr -d ' \t\n\r\f'`

echo "livy.keystore $KEYSTORE_FILE
livy.keystore.password $KEYSTORE_PASS
livy.key-password $KEY_PASS" | sudo tee -a /etc/livy/conf/livy.conf >/dev/null

sudo systemctl restart livy-server.service
```

3. Run the following script as an Amazon EMR step. This script modifies
   `/etc/livy/conf/livy.conf` to activate SSL.

```
--steps '[{"Args":["s3://`amzn-s3-demo-bucket`/livy_ssl.sh"],"Type":"CUSTOM_JAR","ActionOnFailure":"CONTINUE","Jar":"s3://us-east-1.elasticmapreduce/libs/script-runner/script-runner.jar","Properties":"","Name":"Custom JAR"}]'
```

4. Restart the Apache Livy service so that the changes take effect. To restart
   Apache Livy, see [Stopping and restarting processes](../ManagementGuide/emr-process-restart-stop-view.md#emr-process-restart "../ManagementGuide/emr-process-restart-stop-view.md#emr-process-restart").
5. Test that the clients can now communicate using HTTPS. To submit a job, for
   example, run the following code.

```
curl -k -X POST --data '{"file": "local:///usr/lib/spark/examples/jars/spark-examples.jar",
"className": "org.apache.spark.examples.SparkPi"}' \
-H "Content-Type: application/json" \
https://`EMR_Master_Node_Host`:8998/batches
```

If you've enabled HTTPS successfully, Livy sends a response indicating that
the command was accepted and that the batch job was submitted.

```
{"id":1,"name":null,"owner":null,"proxyUser":null,"state":"starting","appId":null,"appInfo":
{"driverLogUrl":null,"sparkUiUrl":null},"log":["stdout: ","\nstderr: ","\nYARN Diagnostics: "]}
```
