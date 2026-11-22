

# Evaluate network paths

Performance Monitor provides visibility into network paths through the **Top network paths** view. This view shows all monitored paths ranked by impact score, to help you quickly identify which paths need attention.

**Top network paths view**

The **Top network paths** view displays paths at the Availability Zone level. Each row represents a path between a source Availability Zone and a destination Availability Zone or AWS service. You can see the following information:
+ **Network path** – The source and destination, for example, `(N. Virginia) us-east-1a to (Oregon) us-west-2b`.
+ **Impact score and level** – The normalized degradation score and classification (High, Medium, Low, or None). For details about how Performance Monitor calculates the impact score and what each impact level means, see [Components and features of Performance Monitor](CloudWatch-PerformanceMonitor-components.md).
+ **Traffic volume** – Total bytes transferred across the path.
+ **p95 latency** – The 95th percentile latency for the path over the selected time period.
+ **Bytes in and bytes out** – Traffic volume in each direction.
+ **Path type** – Classification of the path (Inter-Region, Intra-Region, Intra-AZ, or AZ-Service-AZ).
+ **Associated VPCs** – The VPCs contributing traffic to this path.
+ **Associated accounts** – The AWS accounts involved.
+ **Tags** – Resource tags associated with the subnets and instances.

**Subnet flows**

You can expand any Availability Zone to Availability Zone path to see the subnet-level flows within it. Each subnet flow shows the following:
+ Source subnet to destination subnet or service
+ Traffic percentage (this subnet's contribution to the parent path)
+ Per-subnet bytes and impact score
+ Specific VPC and account for the subnet

Subnet flows are always contained within their parent path. A subnet belongs to exactly one Availability Zone, so it can only appear in paths originating from or terminating at its Availability Zone.

**Filter and sort paths**

You can filter the **Top network paths** view by Region, impact level (High, Medium, Low, or None), impact score range, VPC, account, path type, and VPC and subnet tags. By default, paths are sorted by impact score, highest first.

**View the history of a network path**

To see how a network path performed over time, choose the Availability Zone path in the **Top network paths** view, and then choose a time granularity. Performance Monitor shows the historical trend of the impact score and round-trip time for the path. To analyze these metrics further in CloudWatch, choose **View in Metrics**. You can also create a CloudWatch alarm on the path's impact score in one step from this view.