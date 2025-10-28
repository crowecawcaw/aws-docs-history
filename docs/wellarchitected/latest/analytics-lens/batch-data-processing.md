# Batch data processing

Most analytics applications require frequent batch processing that allows them to process
data in batches at varying intervals. For example, processing daily sales aggregations by
individual store and then writing that data to the data warehouse on a nightly basis can allow
business intelligence (BI) reporting queries to run faster. Batch systems must be built to scale
for all sizes of data and to scale seamlessly to the size of the dataset being processed by
various job runs.

It is important for the batch processing system to be able to
support disparate source and target systems. These include
processing various data formats, seamlessly scaling out to process
peak data volumes, orchestrating jobs using workﬂow, providing a
simple way to monitor the jobs, and most importantly offering an
ease-of-use development framework that accelerates job
development. Business requirements might dictate that batch data
processing jobs be bound by an SLA, or have certain budget
thresholds. Use these requirements to determine the
characteristics of the batch processing architecture.

On AWS, analytic services such as Amazon EMR, Amazon Redshift,
Lake Formation blueprints, and
[AWS Glue](https://aws.amazon.com/glue/ "https://aws.amazon.com/glue/")
family services, namely Glue ETL,
[Glue
Workﬂows,](../../../glue/latest/dg/workflows_overview.md "../../../glue/latest/dg/workflows_overview.md") and
[AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/ "https://aws.amazon.com/glue/features/databrew/") allow you to run batch data processing jobs
at scale for all batch data processing use cases and for various
personas. These personas include data engineers, data analysts,
and data scientists. While there are some overlapping capabilities
between these services, knowing the core competencies and when to
use which service or services allows you to accomplish your
objectives in the most effective way.
