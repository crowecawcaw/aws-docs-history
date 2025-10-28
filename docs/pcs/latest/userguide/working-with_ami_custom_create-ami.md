# Step 5 – Create an AMI compatible

with AWS PCS

After you have installed the required software components, you create an AMI that you can
reuse to launch instances in AWS PCS compute node groups.

###### Important

AWS PCS currently requires a kernel with IPv4 support for local node
communication, even when you use AWS PCS in an IPv6-only network.

###### To create an AMI from your temporary instance

1. Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2 "https://console.aws.amazon.com/ec2").
2. In the navigation pane, choose **Instances**.
3. Select the temporary instance that you created. Choose **Actions**,
   **Image**, **Create image**.
4. For **Create image**, do the following:
   1. For **Image name**, enter a descriptive name for the AMI.
   2. (Optional) For **Image description**, enter a brief description of the
      purpose of the AMI.
   3. Choose **Create image**.

5. In the navigation pane, choose **AMIs**.
6. Locate the AMI that you created in the list. Wait for its status to change from
   **Pending** to **Available**, then use it with a AWS PCS
   compute node group.
