

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Reboot a cluster in Timestream for InfluxDB 3
<a name="rebooting-a-cluster"></a>

 You can reboot your cluster in Amazon Timestream in the event of a cluster health issue.  

## Reboot a cluster using the AWS Management Console
<a name="using-the-aws-management-console-2"></a>

1.  Sign in to the AWS Management Console and open the Amazon Timestream for InfluxDB console. 

1.  In the navigation pane, choose **InfluxDB Databases**. 

1.  Select the cluster you want to reboot. 

1.  Choose **Restart database** from the Actions menu. 

1.  Choose **Confirm and Restart**. 

 Rebooting a DB cluster restarts the database engine service in all the instances that are part of the cluster. Rebooting a DB cluster results in a momentary outage, during which the DB cluster status is set to rebooting. 

## Rebooting a cluster using the AWS CLI
<a name="using-the-aws-cli-2"></a>

To reboot a cluster using the AWS CLI:

```
aws timestream-influxdb reboot-db-cluster \
  --region us-east-1 \
  --identifier "my-influxdb3-cluster"
```