

# Deleting a health check source

The following procedure describes how to delete a health check source by using the Route 53 console.

**Note**  
Before you can delete a health check source, disassociate all health checks that use it. You can't delete a source while health checks remain associated with it.<a name="health-check-sources-deleting-proc"></a>

**To delete a health check source**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Health checks**. Then choose the **Health check sources** tab.

1. Select the health check source that you want to delete.

1. Choose **Delete**, and then confirm the deletion.

Deletion runs in the background. The source remains listed with a deleting status until the deletion completes.