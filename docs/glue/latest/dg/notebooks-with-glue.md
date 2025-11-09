# Managing notebooks

###### Note

Development Endpoints are only supported for versions of AWS Glue prior to 2.0. For an interactive environment where you can author and test ETL scripts, use
[Notebooks on AWS Glue Studio](../ug/notebooks-chapter.md "../ug/notebooks-chapter.md").

A notebook enables interactive development and testing of your ETL (extract, transform, and
load) scripts on a development endpoint. AWS Glue provides an interface to SageMaker AI Jupyter notebooks. With AWS Glue, you create and manage SageMaker AI notebooks.
You can also open SageMaker AI notebooks from the AWS Glue console.

In addition, you can use Apache Spark with SageMaker AI on AWS Glue development endpoints which support SageMaker AI (but not AWS Glue ETL jobs).
SageMaker Spark is an open source Apache Spark library for SageMaker AI. For more information, see [Using Apache Spark with Amazon SageMaker](../../../sagemaker/latest/dg/apache-spark.md "../../../sagemaker/latest/dg/apache-spark.md").

|                                                                                                                             |        |      |      |         |         |      |                |             |      |                       |             |      |                         |             |      |                  |             |      |                      |                  |      |                      |                  |      |                       |              |      |                          |
| --------------------------------------------------------------------------------------------------------------------------- | ------ | ---- | ---- | ------- | ------- | ---- | -------------- | ----------- | ---- | --------------------- | ----------- | ---- | ----------------------- | ----------- | ---- | ---------------- | ----------- | ---- | -------------------- | ---------------- | ---- | -------------------- | ---------------- | ---- | --------------------- | ------------ | ---- | ------------------------ | ---------------- | ---- | --------------------- | ---------------- | ---- | ---------------- | -------------- | ---- | ------------------ | -------------- | ---- | ---------------- | ----------- | ---- | --------------- | ----------- | --- |
| ImportantManaging SageMaker AI notebooks with AWS Glue development endpoints is available in the following AWS Regions:<br> | Region | Code | <br> | --<br>• | --<br>• | <br> | US East (Ohio) | `us-east-2` | <br> | US East (N. Virginia) | `us-east-1` | <br> | US West (N. California) | `us-west-1` | <br> | US West (Oregon) | `us-west-2` | <br> | Asia Pacific (Tokyo) | `ap-northeast-1` | <br> | Asia Pacific (Seoul) | `ap-northeast-2` | <br> | Asia Pacific (Mumbai) | `ap-south-1` | <br> | Asia Pacific (Singapore) | `ap-southeast-1` | <br> | Asia Pacific (Sydney) | `ap-southeast-2` | <br> | Canada (Central) | `ca-central-1` | <br> | Europe (Frankfurt) | `eu-central-1` | <br> | Europe (Ireland) | `eu-west-1` | <br> | Europe (London) | `eu-west-2` |     |

###### Topics
