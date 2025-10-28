# Sharing your rightsizing recommendations

You can download a rightsizing recommendations report in CSV format.

###### To download your recommendations

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, under **Legacy pages**, choose
   **Rightsizing**.
3. Under **Findings**, choose **Download
   CSV**.
   The following is a list of fields in the downloadable CSV file from the
   **Rightsizing recommendations** page. The fields are repeated if
   there are multiple rightsizing options available. The file also contains all of your
   relevant cost allocation tags.

- **Account ID** – The AWS account ID that owns the
  instance that the recommendation is based off of.
- **Account Name** – The name of the account that owns
  the instance that the recommendation is based off of.
- **Instance ID** – The unique instance
  identifier.
- **Instance Name** – The name you've given to the
  instance.
- **Instance Type** – The instance family and size of
  the original instance.
- **Instance Name** – The name you've given an instance.
  This field will show as blank if you haven't given the instance a name.
- **OS** – The operating system or platform of the
  current instance.
- **Region** – The AWS Region that the instance is
  running in.
- **Running Hours** – The total number of running hours
  of the instance over the last 14 days.
- **RI Hours** – The subset of the total running hours
  that are covered by an AWS reservation over the look-back period.
- **OD Hours** – The subset of the total running hours
  that are On-Demand over the look-back period.
- **SP Hours** – The subset of the total running hours
  that are covered by Savings Plans over the look-back period.
- **CPU Utilization** – The maximum CPU utilization of
  the instance over the look-back period.
- **Memory Utilization** – The maximum memory
  utilization of the instance over the look-back period (if available from the
  Amazon CloudWatch agent).
- **Disk Utilization** – The maximum disk utilization of
  the instance over the look-back period (if available from the CloudWatch agent -
  currently not supported).
- **Network Capacity** – The maximum network
  input/output operations per second capacity of the current instance. This isn't
  a measure of actual instance use or performance, only capacity. It's not
  considered in the recommendation.
- **EBS Read Throughput** – The maximum number of read
  operations per second.
- **EBS Write Throughput** – The maximum number of write
  operations per second.
- **EBS Read Bandwidth** – The maximum volume of read
  KiB per second.
- **EBS Write Bandwidth** – The maximum volume of write
  KiB per second.
- **Recommended Action** – The recommended action,
  either modify or terminate the instance.
- **Recommended Instance Type 1** – The instance family
  and size of the recommended instance type. For termination recommendations, this
  field is empty.
- **Recommended Instance Type 1 Estimated Saving** – The
  projected savings based on the recommended action, instance type, associated
  rates, and your current Reserved Instance (RI) portfolio.
- **Recommended Instance Type 1 Projected CPU** – The
  projected value of the CPU utilization based on utilization of current instance
  CPU and recommended instance specifications.
- **Recommended Instance Type 1 Projected Memory** – The
  projected value of the memory utilization based on utilization of current
  instance memory and recommended instance specifications.
- **Recommended Instance Type 1 Projected Disk** – The
  projected value of the disk utilization based on utilization of current instance
  disk and recommended instance specifications.
- **Recommended Instance Type 1 Network Capacity** – The
  maximum network input/output operations per second capacity of the recommended
  instance. This isn't a measure of actual instance use or performance, only
  capacity. It's not considered in the recommendation.
