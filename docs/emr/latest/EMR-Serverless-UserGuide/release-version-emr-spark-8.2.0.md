

# `AWS runtime for Apache Spark` (emr-spark-8.2.0)

The following table lists the application versions available with `AWS runtime for Apache Spark` (emr-spark-8.2.0).


**Application version information**  

| Application | Version | 
| --- | --- | 
| Spark | 4.1.3-amzn-0 | 
| Iceberg | 1.11.0-amzn-0 | 
| Delta | 4.2.0-amzn-0 | 
| Hudi | 1.1.1-amzn-0 | 

****`AWS runtime for Apache Spark` (emr-spark-8.2.0) release notes****
+ **Changes and enhancements**
  + **Scaling Profiles for Spark** — You can now choose how quickly EMR Serverless scales Spark executors. Set the Spark property `spark.emr-serverless.scalingProfile` to `performance-optimized`, `balanced`, or `cost-optimized`, or set it as an application default. Applications that use this release default to `balanced`. Spark dynamic allocation settings that you set yourself override the profile. For more information, see [Using Scaling Profiles](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/scaling-profiles.html).
  + **Lake Formation governed user-defined functions** — EMR Serverless applications that use AWS Lake Formation can now run AWS Glue user-defined functions (UDFs) that are governed by Lake Formation, including in Lake Formation row filter expressions. Governed UDFs can process data before Lake Formation applies row, column, and cell-level filters. For more information, see [Using user-defined functions with Lake Formation fine-grained access control](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless-lf-udf.html).