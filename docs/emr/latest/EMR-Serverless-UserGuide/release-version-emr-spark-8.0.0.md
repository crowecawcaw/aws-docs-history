

# `AWS runtime for Apache Spark` (emr-spark-8.0.0)
<a name="release-version-emr-spark-8.0.0"></a>

The following table lists the application versions available with `AWS runtime for Apache Spark` (emr-spark-8.0.0).


**Application version information**  

| Application | Version | 
| --- | --- | 
| Spark | 4.0.2-amzn-0 | 
| Iceberg | 1.10.1-amzn-0 | 
| Delta | 4.0.0-amzn-1-spark | 
| Hudi | 1.1.0-amzn-0 | 

****`AWS runtime for Apache Spark` (emr-spark-8.0.0) release notes****
+ **GA release** – This is the general availability release of `AWS runtime for Apache Spark` featuring Apache Spark 4.0.2. This release is available on EMR Serverless, EMR on EC2, and EMR on EKS.
+ **Regional Availability** - Available in all AWS Regions where EMR Serverless is available, except Middle East (Bahrain) and Middle East (UAE) regions.
+ **Known limitations** - Spark Connect secure endpoint with Native FGAC support is not available in this release.
+ **Additional Documentation** - For additional Apache Spark documentation, see [Apache Spark 4.0.2 Release Documentation](https://spark.apache.org/releases/spark-release-4-0-2.html).

To get started with Apache Spark 4.0.2, create an EMR Serverless application using the AWS CLI:

```
aws emr-serverless create-application --type SPARK \
  --release-label emr-spark-8.0.0 \
  --name spark4-serverless \
  --region us-east-1
```
+ This release supersedes the preview release (emr-spark-8.0-preview). The preview was limited to Spark 4.0.1 and lacked FGAC, Hudi, data connectors, and Persistent Spark History Server.
+ The `--type` parameter for `create-application` uses `SPARK` (uppercase).