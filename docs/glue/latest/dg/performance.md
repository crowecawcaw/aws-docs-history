# Improving AWS Glue performance

**Baseline strategy for performance tuning**

In order to improve AWS Glue performance, you may consider updating certain performance related AWS Glue parameters.
When preparing to tune parameters, use the following best practices:

- Determine your performance goals before beginning to identify problems.
- Use metrics to identify problems before attempting to change tuning parameters.
  For the most consistent results when tuning a job, develop a baseline strategy for your tuning work.

Generally, performance tuning is performed in the following workflow:

1. Determine performance goals.
2. Measure metrics.
3. Identify bottlenecks.
4. Reduce the impact of the bottlenecks.
5. Repeat steps 2-4 until you achieve the intended target.

## Tuning strategies for your job type

**Spark jobs**–follow the guidance in [Best practices for performance tuning AWS Glue for Apache Spark jobs](../../../prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/introduction.md "../../../prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/introduction.md") on AWS Prescriptive Guidance.

**Other jobs**–you can tune AWS Glue for Ray and AWS Glue Python shell jobs by adapting strategies available in other runtime environments.
