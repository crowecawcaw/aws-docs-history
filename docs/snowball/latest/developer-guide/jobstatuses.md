AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Statuses of Snowball Edge jobs

Each AWS Snowball Edge device job has a _status_, which changes to denote the
current state of the job. This job status information doesn't reflect the health, the
current processing state, or the storage used for the associated devices.

###### To see the status of a job

1. Log into the [AWS Snow Family Management Console](https://console.aws.amazon.com/snowfamily/home "https://console.aws.amazon.com/snowfamily/home").
2. On the **Job dashboard**, choose the job.
3. Click on your job name within the console.
4. The Job Status pane will be located near the top and reflects the status of the job.

| AWS Snowball Edge device job statuses | Console Identifier       | API Identifier                                                                                                                                                        | Status Description |
| ------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Job created                           | `New`                    | Your job has just been created. This status is the only one during<br>which you can cancel a job or its job parts, if the job is an export<br>job.                    |
| Preparing appliance                   | `PreparingAppliance`     | AWS is preparing a device for your job.                                                                                                                               |
| Exporting                             | `InProgress`             | AWS is exporting your data from Amazon S3 onto a device.                                                                                                              |
| Preparing shipment                    | `PreparingShipment`      | AWS is preparing to ship a device to you. The expected<br>shipping tracking information is provided for customers in the<br>status.                                   |
| In transit to you                     | `InTransitToCustomer`    | The device has been shipped to the address you provided during job<br>creation.                                                                                       |
| Delivered to you                      | `WithCustomer`           | The device has arrived at the address you provided during job<br>creation.                                                                                            |
| In transit to AWS                     | `InTransitToAWS`         | You have shipped the device back to AWS.                                                                                                                              |
| At sorting facility                   | `WithAWSSortingFacility` | The device for this job is at our internal sorting facility. Any<br>additional processing for import jobs into Amazon S3 will begin soon,<br>typically within 2 days. |
| At AWS                                | `WithAWS`                | Your shipment has arrived at AWS. If you're importing data, your<br>import typically begins within a day of its arrival.                                              |
| Importing                             | `InProgress`             | AWS is importing your data into Amazon Simple Storage Service (Amazon S3).                                                                                            |
| Completed                             | `Complete`               | Your job or a part of your job has completed successfully.                                                                                                            |
| Canceled                              | `Cancelled`              | Your job has been canceled.                                                                                                                                           |

## Statuses of Snowball Edge cluster jobs

Each cluster has a _status_, which changes to denote the
current general progress state of the cluster. Each individual node of the cluster
has its own job status.

This cluster status information doesn't reflect the health, the current processing
state, or the storage used for the cluster or its nodes.

| Console Identifier | API Identifier   | Status Description                                                                                                                                                                   |
| ------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Awaiting Quorum    | `AwaitingQuorum` | The cluster hasn't been created yet, because there aren't enough<br>nodes to begin processing the cluster request. For a cluster to be<br>created, it must have at least five nodes. |
| Pending            | `Pending`        | Your cluster has been created, and we're getting its nodes ready<br>to ship out. You can track the status of each node with that node's<br>job status.                               |
| Delivered to you   | `InUse`          | At least one node of the cluster is at the address you provided<br>during job creation.                                                                                              |
| Completed          | `Complete`       | All the nodes of the cluster have been returned to AWS.                                                                                                                              |
| Canceled           | `Cancelled`      | The request to make a cluster was canceled. Cluster requests can<br>only be canceled before they enter the Pending state.                                                            |
