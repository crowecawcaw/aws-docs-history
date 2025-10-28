# Validating VPC

endpoint configuration

After you install the security agent manually or through GuardDuty automated configuration, you
can use this document to validate that the VPC endpoint configuration. You can also use
these steps after troubleshooting any [runtime coverage issue](runtime-monitoring-assessing-coverage.md "runtime-monitoring-assessing-coverage.md")
for a resource type. You can ensure that the steps worked as expected and the coverage status would potentially
show up as **Healthy**.

Use the following steps to validate that VPC endpoint configuration for your resource type
is set up correctly in the VPC owner account:

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Virtual private cloud**, choose
   **Your VPCs**.
3. On the **Your VPCs** page, choose **IPv4 CIDR**
   associated with your **VPC ID**.
4. In the navigation pane, under **Virtual private cloud**, choose
   **Endpoints**.
5. In the **Endpoints** table, select the row that has the
   **Service name** similar to
   **com.amazonaws.`us-east-1`.guardduty-data**.
   The Region (`us-east-1`) might be different for your endpoint.
6. A panel for endpoint details will appear. Under the **Security
   Groups** tab, select the associated **Group ID** link
   for more details.
7. In the **Security Groups** table, select the row that with the
   associated **Security group ID** to view the details.
8. Under the **Inbound rules** tab, ensure that there is an ingress
   policy with **Port range** as **443** and
   **Source** as the value copied from the
   **IPv4 CIDR**. Inbound rules
   control the incoming traffic that is allowed to reach the instance. The following
   image shows the inbound rules for a security group that is associated with the VPC
   used by the GuardDuty security agent.

If you don't already have a security group that has an in-bound port 443 enabled,
[Create a security group](../../../AWSEC2/latest/UserGuide/working-with-security-groups.md#creating-security-group "../../../AWSEC2/latest/UserGuide/working-with-security-groups.md#creating-security-group") in the
_Amazon EC2 User Guide_.

If there is an issue while restricting the in-bound permissions to your VPC (or
cluster), provide the support to in-bound 443 port from any IP address
(0.0.0.0/0).
