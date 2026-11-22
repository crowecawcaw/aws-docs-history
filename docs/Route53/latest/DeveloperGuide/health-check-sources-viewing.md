

# Viewing health check sources

The following procedure describes how to view your health check sources by using the Route 53 console.<a name="health-check-sources-viewing-proc"></a>

**To view your health check sources**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Health checks**. Then choose the **Health check sources** tab.

The page lists your health check sources with their status. A health check source can have one of the following statuses:

****Pending****  
Route 53 accepts the request to create the source and starts creating it.

****Creating****  
Route 53 is creating the health check source. Creating a source can take a few minutes.

****Available****  
The health check source is ready. You can use a source in a health check only when it is in the **Available** status.

****Create failed****  
Route 53 couldn't create the health check source.

****Delete pending****  
Route 53 accepts the request to delete the source and starts deleting it.

****Deleting****  
Route 53 is deleting the health check source.

****Deleted****  
Route 53 deleted the health check source.

****Delete failed****  
Route 53 couldn't delete the health check source.