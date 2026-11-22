

# Using AWS analytics services

Amazon Athena and Amazon Redshift Spectrum use your Lake Formation permissions directly. You grant the IAM user or role that runs queries, as described in Step 2 of [Getting started with HealthLake analytics](integrating-analytics-getting-started.md), and you don't turn on full table access. Apache Spark on Amazon EMR reads the tables with its own runtime role, and it also needs full table access. Complete Steps 2 and 3 for the runtime role. For the engine-specific setup, see the following topics.


**AWS analytics services for HealthLake data**  

| Service | Use it to | Topic | 
| --- | --- | --- | 
| Amazon Athena | Run serverless SQL with no infrastructure to manage | [Setting up Amazon Athena](integrating-athena.md) | 
| Amazon Redshift Spectrum | Query from Amazon Redshift and join HealthLake data with your warehouse data | [Setting up Amazon Redshift Spectrum](integrating-redshift-spectrum.md) | 
| Apache Spark on Amazon EMR | Process data at large scale with Spark | [Setting up Apache Spark on Amazon EMR](integrating-spark.md) | 

**Note**  
You can also use these services from a Amazon SageMaker Unified Studio project. Grant the Lake Formation permissions in Step 2 of [Getting started with HealthLake analytics](integrating-analytics-getting-started.md) to the project's IAM role. You then query the tables the same way as described on each service's page.

**Topics**
+ [Amazon Athena](integrating-athena.md)
+ [Redshift Spectrum](integrating-redshift-spectrum.md)
+ [Apache Spark on Amazon EMR](integrating-spark.md)