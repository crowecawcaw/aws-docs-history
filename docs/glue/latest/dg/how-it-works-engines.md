# AWS Glue for Spark and AWS Glue for Ray

In AWS Glue on Apache Spark (AWS Glue ETL), you can use PySpark to write Python code to handle data at scale.
Spark is a familiar solution for this problem, but data engineers with Python-focused backgrounds can find
the transition unintuitive. The Spark DataFrame model is not seamlessly "Pythonic", which reflects the Scala
language and Java runtime it is built upon.

In AWS Glue, you can use Python shell jobs to run native Python data integrations. These jobs run on a single
Amazon EC2 instance and are limited by the capacity of that instance. This restricts the throughput of the data
you can process, and becomes expensive to maintain when dealing with big data.

AWS Glue for Ray allows you to scale up Python workloads without substantial investment into learning Spark.
You can take advantage of certain scenarios where Ray performs better. By offering you a choice, you can use
the strengths of both Spark and Ray.

AWS Glue ETL and AWS Glue for Ray are different underneath, so they support different features. Please check
the documentation to determine supported features.

## What is AWS Glue for Ray?

Ray is an open-source distributed computation framework that you can use to scale up workloads, with a focus
on Python. For more information about Ray, see the [Ray website](https://www.ray.io/ "https://www.ray.io/"). AWS Glue
Ray jobs and interactive sessions allow you to use Ray within AWS Glue.

You can use AWS Glue for Ray to write Python scripts for computations that will run in parallel across
multiple machines. In Ray jobs and interactive sessions, you can use familiar Python
libraries, like pandas, to make your workflows easy to write and run. For more information about Ray datasets, see [Ray Datasets](https://docs.ray.io/en/latest/data/dataset.html "https://docs.ray.io/en/latest/data/dataset.html") in the Ray documentation. For
more information about pandas, see the [Pandas website](https://pandas.pydata.org/ "https://pandas.pydata.org/").

When you use AWS Glue for Ray, you can run your pandas workflows against big data at enterprise
scale—with only a few lines of code. You can create a Ray job from the AWS Glue console or the AWS
SDK. You can also open an AWS Glue interactive session to run your code on a serverless Ray environment. Visual
jobs in AWS Glue Studio are not yet supported.

AWS Glue for Ray jobs allow you to run a script on a schedule or in response to an event from Amazon EventBridge. Jobs store
log information and monitoring statistics in CloudWatch that enable you to understand the health and reliability
of your script. For more information about the AWS Glue job system, see [Working with Ray jobs in AWS Glue](ray-jobs-section.md "ray-jobs-section.md").

Ray automates the work of scaling Python code by distributing the processing across a cluster of machines
that it reconfigures in real time, based on the load. This can lead to improved performance per dollar for
certain workloads. With Ray jobs, we have built auto scaling natively into the AWS Glue job model, so you can
fully take advantage of this feature. Ray jobs run on AWS Graviton, leading to higher overall price
performance.

In addition to cost savings, you can use native auto scaling to run Ray workloads without investing time
into cluster maintenance, tuning, and administration. You can use familiar open-source libraries out of the
box, such as pandas, and the AWS SDK for Pandas. These improve iteration speed while you're developing on
AWS Glue for Ray. When you use AWS Glue for Ray, you will be able to rapidly develop and run cost-effective data
integration workloads.
