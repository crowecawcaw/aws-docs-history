

# EMR Serverless 6.15.0
<a name="release-version-6150"></a>

The following table lists the application versions available with EMR Serverless 6.15.0.


| Application | Version | 
| --- | --- | 
| Apache Spark | 3.4.1 | 
| Apache Hive | 3.1.3 | 
| Apache Tez | 0.10.2 | 

**EMR Serverless 6.15.0 release notes**
+ **TLS support** – With Amazon EMR Serverless releases 6.15.0 and higher, enable mutual-TLS encrypted communication between workers in your Spark job runs. When enabled, EMR Serverless automatically generates a unique certificate for each worker that it provisions under a job runs that workers utilize during TLS handshake to authenticate each other and establish an encrypted channel to process data securely. For more information about mutual-TLS encryption, refer to [Inter-worker encryption](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/interworker-encryption.html).