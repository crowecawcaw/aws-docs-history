# Using your rightsizing recommendations

You can see the following top-level key performance indicators (KPIs) in your
rightsizing recommendations:

- **Optimization opportunities** – The number of
  recommendations available based on your resources and usage
- **Estimated monthly savings** – The sum of the
  projected monthly savings associated with each of the recommendations
  provided
- **Estimated savings (%)** – The available savings
  relative to the direct instance costs (On-Demand) associated with the instances
  in the recommendation list

###### To filter your rightsizing recommendations

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, under **Legacy pages**, choose
   **Rightsizing**.
3. On the **Rightsizing recommendations** page, under
   **Recommendation parameters**, filter your recommendations
   by selecting any or all of the following check boxes:
   - Idle instances
   - Underutilized instances
   - Include Savings Plans and Reserved Instances

4. Under **Findings**, use the search bar to filter by the
   following parameters:
   - Account ID (option available from the management account)
   - Region
   - Cost allocation tag

###### To view your rightsizing recommendations details

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, under **Legacy pages**, choose
   **Rightsizing**.
3. On the **Rightsizing recommendations** page, under
   **Findings**, choose a recommendation to view the
   details.

## Enhancing your recommendations using

CloudWatch metrics

We can examine your memory utilization if you enable your Amazon CloudWatch agent.

To enable memory utilization, see [Installing the CloudWatch Agent](../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.md "../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.md").

###### Important

When you create a CloudWatch configuration file, use the default namespace and
default names for the collected metrics.

For **InstanceID**, choose `append_Dimension`. Do
not add additional dimensions for individual memory or disk metrics. Disk
utilization is currently not examined.

For Linux instances, choose `mem_used_percent` as your metric for
your CloudWatch agent to collect. For Windows instances, choose `"%
 Committed Bytes In Use"`.

For more information about the CloudWatch agent, see [Collecting Metrics and Logs from Amazon EC2 Instances and On-Premises Servers with
the CloudWatch Agent](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md") in the _Amazon CloudWatch User Guide_.
