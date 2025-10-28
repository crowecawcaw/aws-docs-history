# Configuration notes

**Use AWS Glue Data Catalog as a central metastore for your batch processing
jobs, regardless of which AWS analytics service you use as a processing engine.**
Batch processing jobs cater to a variety of workloads ranging from running several times an
hour or day, to running monthly or quarterly. The data volumes vary significantly and so do
the consumption patterns on the processed dataset. Always work backwards to understand the
business SLAs and develop your job accordingly. The central Data Catalog makes it easy for you
to use the right analytic service to meet your business SLAs and other objectives, thereby
creating a central analytic ecosystem.

**Avoid lifting and shifting server-based batch processing systems to
AWS.** By lifting and shifting traditional batch processing systems into AWS,
you risk running overprovisioned resources on Amazon EC2. For example, traditional Hadoop clusters
are often overprovisioned and idle in an on-premises setting. Use AWS Managed Services, such as
AWS Glue, Amazon EMR, and Amazon Redshift, to simplify your architecture using a modern data architecture
pattern and remove the undifferentiated heavy lifting of managing clustered and distributed
environments.

**Automate and orchestrate everywhere.** In a traditional batch
data processing environment, it’s a best practice to automate and schedule your jobs in the
system. In AWS, you should use automation and orchestration for your batch data processing
jobs in conjunction with the AWS APIs to spin up and tear down entire compute environments,
so that you are only charged when the compute services are in use. For example, when a job is
scheduled, a workﬂow service, such as AWS Step Functions, would use the AWS SDK to provision a new
EMR cluster, submit the work, and shut down the cluster after the job is complete. Similarly,
you can use Terraform or a CloudFormation template to achieve similar functionality.

**Use Spot Instances and Graviton-based instance types on EMR to save
costs and get better price performance ratio**. Use Spot Instances when you have
ﬂexible SLAs that are resilient to job reruns upon failure and when there is a need to process
very large volumes of data. Use Spot Fleet, EC2 Fleet, and Spot Instance features in Amazon EMR to
manage Spot Instances.

**Continually monitor and improve batch processing jobs.** Batch
processing systems evolve rapidly as data source volumes increase, new batch processing jobs
are authored, and new batch processing frameworks are launched. Instrument your jobs with
metrics, timeouts, and alarms to have the metrics and insight to make informed decisions on
batch data processing system changes.
