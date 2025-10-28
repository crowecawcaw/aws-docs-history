# Best practice 8.3 – Define and measure the computing performance metrics

Define how you will measure performance of the analytics
solutions for each step in the process. For example, if the
computing solution is a transient Amazon EMR cluster, you
can take the following approach. Define the performance as
the Amazon EMR job runtime from the launch of the EMR
cluster, process the job, then shut down the cluster. As
another example, if the computing solution is an Amazon Redshift cluster that is shared by a business unit, you can
define the performance as the runtime duration for each SQL
query.

## Suggestion 8.3.1 – Define performance efficiency metrics

Collect and use metrics to scale the resources to meet
business requirements. By doing so, your team can track
unexpected spikes to make future improvements.

## Suggestion 8.3.2 – Continually identify under-performing components and ﬁne-tune the infrastructure or application logic

After you have deﬁned the performance measurement, you should identify which infrastructure components or jobs are running below the performance criteria. Performance ﬁne-tuning varies for each AWS service, but generally, optimizing queries or workloads can enhance performance without necessitating infrastructure modifications. For example, if it is an Amazon EMR cluster running a Spark application, you could explore tuning your Spark configuration. If after fine-tuning you still need more performance, you can change to a larger cluster instance type, or increase the number of cluster nodes.

For an Amazon Redshift cluster, you can ﬁne-tune the SQL queries that are running below the performance criteria and if required, increase the number of cluster nodes to increase parallel computing capacity.
