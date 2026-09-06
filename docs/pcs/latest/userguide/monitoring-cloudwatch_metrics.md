

# Monitoring AWS PCS metrics using CloudWatch
<a name="monitoring-cloudwatch_metrics"></a>

You can monitor AWS PCS cluster health using Amazon CloudWatch, which collects data from your cluster and turns it into near real-time metrics. These statistics are retained for a period of 15 months, so that you can access historical information and gain a better perspective on how your cluster is performing. Cluster metrics are sent to CloudWatch at 1-minute periods. For more information about CloudWatch, see [What Is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) in the *Amazon CloudWatch User Guide*.

AWS PCS publishes the following metrics into the **AWS/PCS** namespace in CloudWatch. They have a single dimension, `ClusterId`.


| Name | Description | Units | 
| --- | --- | --- | 
| ActualCapacity | IdleCapacity \+ UtilizedCapacity | Count | 
| CapacityUtilization | UtilizedCapacity / ActualCapacity | Count | 
| DesiredCapacity | ActualCapacity \+ PendingCapacity | Count | 
| IdleCapacity | Count of instances that are running but not allocated to jobs | Count | 
| UtilizedCapacity | Count of instances that are running and allocated to jobs | Count | 