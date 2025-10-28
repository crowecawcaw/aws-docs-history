# Modify IPAM operating Regions

Operating Regions are AWS Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the AWS Regions you select as operating Regions.

Adding an operating region to an IPAM allows you to manage IP address space across multiple AWS Regions. This can improve IP address utilization, enable regional segmentation, and support geographically distributed infrastructure. Expanding the IPAM's Regional scope provides greater flexibility and control over your overall IP address management.

AWS Management Console

###### To modify the IPAM operating Regions

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **IPAMs**.
3. In the content pane, select your IPAM.
4. Choose **Actions** > **Edit**.
5. Under **IPAM settings**, choose the **Operating Regions** you want to use for the IPAM.
6. Choose **Save changes**.

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

Use the following AWS CLI commands to view and modify IPAM operating Regions:

1. View current IPAMs: [describe-ipams](../../../cli/latest/reference/ec2/describe-ipams.md "../../../cli/latest/reference/ec2/describe-ipams.md")
2. Add or remove IPAM operating Regions: [modify-ipam](../../../cli/latest/reference/ec2/modify-ipam.md "../../../cli/latest/reference/ec2/modify-ipam.md")
3. View your updated IPAMs: [describe-ipams](../../../cli/latest/reference/ec2/describe-ipams.md "../../../cli/latest/reference/ec2/describe-ipams.md")
