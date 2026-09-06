

# Viewing Amazon DocumentDB recommendations
<a name="view-docdb-recommendations"></a>

Amazon DocumentDB provides a list of automated recommendations for database resources, such as instances and clusters. These recommendations provide best practice guidance by analyzing your cluster and instance configurations.

As an example of these recommendations, see the following:


| Type | Description | Recommendation | Additional information | 
| --- | --- | --- | --- | 
| One instance | Cluster only contains one instance | Performance and availability: add another instance with the same instance class in a different Availability Zone. | [Amazon DocumentDB high availability and replication](replication.md) | 

Amazon DocumentDB generates recommendations for a resource when the resource is created or modified. Amazon DocumentDB also periodically scans your resources and generates recommendations.

**To view and take action on Amazon DocumentDB recommendations**

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb).

1. In the navigation pane, choose **Recommendations**:  
![Amazon DocumentDB console navigation pane with Recommendations option selected.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/recommendations-nav-1.png)

1. In the **Recommendations** dialog, expand the section of interest and select the recommended task.

   In the following example, the recommended task applies to an Amazon DocumentDB cluster with only one instance. The recommendation is to add another instance to improve performance and availability.  
![The Recommendations form showing a selected recommended task for an Amazon DocumentDB cluster.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/recommendations-1.png)

1. Choose **Apply now**.

   For this example, the **Add instances** dialog appears:  
![The Add instances form with options for instance settings.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/add-instances-1.png)

1. Modify your new instance's settings and choose **Create**.