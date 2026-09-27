

# `AWS runtime for Apache Spark` (emr-spark-8.1.0)
<a name="release-version-emr-spark-8.1.0"></a>

The following table lists the application versions available with `AWS runtime for Apache Spark` (emr-spark-8.1.0).


**Application version information**  

| Application | Version | 
| --- | --- | 
| Spark | 4.1.1-amzn-0 | 
| Iceberg | 1.11.0-amzn-0 | 
| Delta | 4.2.0-amzn-0 | 
| Hudi | 1.1.1-amzn-0 | 

****`AWS runtime for Apache Spark` (emr-spark-8.1.0) release notes****
+ **Changes and enhancements**
  + **Python 3.12 support** — Amazon EMR Serverless with `emr-spark-8.1.0` supports Python 3.12 for Apache Spark applications.
  + **Custom image release version validation** — When you use a custom image with this release, EMR Serverless verifies that it was built from the matching release's base image. If the image's release version doesn't match the application's release version, or the image has no release version, the request is rejected. The message identifies the base image version to use. Rebuild your custom image from the matching EMR Serverless base image.
  + **Increased Serverless storage data limit for Spark jobs** — This release raises the Serverless storage data limit for Spark jobs from 200 GiB to 1 TiB.
  + **Merged Spark configuration** — Starting with `emr-spark-8.1.0`, EMR Serverless merges Spark configuration instead of replacing it. It combines the configuration set at the application level with the configuration set for an individual job or session. When the same configuration is set at both levels, the job or session value takes precedence. In `emr-spark-8.0.0`, the job or session configuration replaces the application-level configuration entirely.

To get started with Apache Spark 4.1.1, create an EMR Serverless application using the AWS CLI:

```
aws emr-serverless create-application --type SPARK \
  --release-label emr-spark-8.1.0 \
  --name spark4-serverless \
  --region us-east-1
```
+ The `--type` parameter for `create-application` uses `SPARK` (uppercase).