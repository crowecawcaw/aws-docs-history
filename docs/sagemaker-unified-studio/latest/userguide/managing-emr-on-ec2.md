# Amazon EMR on EC2 connections in Amazon SageMaker Unified Studio

Whenever you are working with a project, you can manage that project's Amazon EC2 resources and
view both monitoring and logging data for those resources. You can create and configure Amazon EMR on
EC2 clusters, as well as terminate and remove those clusters. When clusters are running, data
regarding their metrics is automatically sent to CloudWatch, while logging data is preserved in the
Spark UI.

## Spark History Server

You can use the live Spark UI in a notebook session to view details such as tasks,
executors and logs about Spark jobs.

You can explore the Spark History Server for a cluster at any time. To do this, select
your cluster from the list of all clusters assigned to a project, which brings up the Detail
view for the cluster. On the Detail page view, select the **Applications**
tab and choose the '**Spark History Server** link.
