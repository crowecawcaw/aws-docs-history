

# Improving AWS Glue performance


|  | 
| --- |
| For Apache Spark optimization in AWS Glue, see [Apache Spark Optimization Agent for Amazon EMR and AWS Glue](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-optimization-agent.html), which provides AI-powered recommendations for improving the performance and cost of your Spark jobs.<br />The Apache Spark Optimization Agent analyzes successful Apache Spark workloads on AWS Glue and Amazon EMR Serverless. It combines natural language interaction and analysis of your workload's run data to return prioritized configuration, infrastructure, and data recommendations that improve performance or reduce cost. | 

**Baseline strategy for performance tuning**

In order to improve AWS Glue performance, you may consider updating certain performance related AWS Glue parameters. When preparing to tune parameters, use the following best practices:
+ Determine your performance goals before beginning to identify problems.
+ Use metrics to identify problems before attempting to change tuning parameters.

For the most consistent results when tuning a job, develop a baseline strategy for your tuning work.

Generally, performance tuning is performed in the following workflow:

1. Determine performance goals.

1. Measure metrics.

1. Identify bottlenecks.

1. Reduce the impact of the bottlenecks.

1. Repeat steps 2-4 until you achieve the intended target.

## Tuning strategies for your job type
<a name="w2aac97c17"></a>

**Spark jobs**–follow the guidance in [Best practices for performance tuning AWS Glue for Apache Spark jobs](https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/introduction.html) on AWS Prescriptive Guidance.

**Other jobs**–you can tune AWS Glue for Ray and AWS Glue Python shell jobs by adapting strategies available in other runtime environments.