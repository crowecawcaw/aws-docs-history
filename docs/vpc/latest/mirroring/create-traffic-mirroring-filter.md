# Create, modify, or delete a traffic mirror filter

Use a traffic mirror filter and its rules to determine the traffic that is mirrored. A
traffic mirror filter contains one or more traffic mirror rules. For more information, see
[Understand traffic mirror filter concepts](traffic-mirroring-filters.md "traffic-mirroring-filters.md").

Rules are evaluated from the lowest value to the highest value. The first rule that
matches the traffic determines the action to take.

Before you can delete a traffic mirror filter, you must remove it from any traffic mirror sessions.

###### To create, modify, or delete a traffic mirror filter using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Traffic Mirroring**,
   **Mirror filters**.
3. To delete a filter, select the traffic mirror filter, and then choose **Actions**,
   **Delete**.
4. When prompted for confirmation, enter `delete`, and then choose
   **Delete**.
5. To modify a filter, select the ID of the traffic mirror filter to open its details page. For each rule to add, choose either **Inbound rules** , **Add inbound
   rule** or **Outbound rules**, and then choose **Actions** and modify the the rule.
6. To create a filter, choose **Create traffic mirror filter**.
7. (Optional) For **Name tag**, enter a name for the traffic mirror
   filter.
8. (Optional) For **Description**, enter a description for the
   traffic mirror filter.
9. (Optional) If you need to mirror Amazon DNS traffic, select
   **amazon-dns**.
10. For each rule, inbound or outbound, choose **Add rule**, and then
    specify the following information:
    - **Number**: The rule priority.
    - **Rule action**: Indicates whether to accept or reject the
      packets.
    - **Protocol**: The protocol.
    - (Optional) **Source port range**: The source port range.
    - (Optional) **Destination port range**: The destination port
      range.
    - **Source CIDR block**: The source CIDR block. The source and destination
      CIDR blocks must both be either IPv4 ranges or IPv6 ranges.
    - **Destination CIDR block**: The destination CIDR block. The source and
      destination CIDR blocks must both be either IPv4 ranges or IPv6 ranges.
    - **Description**: A description for the rule.

11. (Optional) For each tag to add, choose **Add new tag** and enter the tag key
    and tag value.
12. Choose **Create**.

###### To create a traffic mirror filter using the AWS CLI

Use the [create-traffic-mirror-filter](../../../cli/latest/reference/ec2/create-traffic-mirror-filter.md "../../../cli/latest/reference/ec2/create-traffic-mirror-filter.md") command.

###### To delete a traffic mirror filter using the AWS CLI

Use the [delete-traffic-mirror-filter](../../../cli/latest/reference/ec2/delete-traffic-mirror-filter.md "../../../cli/latest/reference/ec2/delete-traffic-mirror-filter.md") command.
