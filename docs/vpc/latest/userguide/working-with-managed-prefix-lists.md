

# Customer-managed prefix lists
<a name="working-with-managed-prefix-lists"></a>

Customer-managed prefix lists allow you to define and maintain your own sets of IP address ranges, known as prefixes, within AWS. Instead of hardcoding these IP addresses into your various resources, you can create a centralized prefix list and reference it wherever needed. This not only simplifies the management of your IP addresses but also promotes consistency and reusability across your AWS landscape. 

 One of the standout features of customer-managed prefix lists is the ability to share them with other AWS accounts. By granting access to your prefix lists, you can enable other teams or organizations to use your defined IP address ranges in their own resources. This collaborative approach fosters a more cohesive and efficient cloud experience, where IP address management is shared and synchronized. 

In the sections that follow, we'll dive deeper into the practical aspects of working with customer-managed prefix lists, including step-by-step guidance on creating, managing, and sharing your IP address ranges.

**Note**  
You can automate prefix list management using Amazon VPC IPAM to automatically sync CIDRs based on rules you define. This eliminates manual updates when your infrastructure changes. For more information, see [Automate prefix list updates with IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/automate-prefix-list-updates.html) in the *Amazon VPC IPAM User Guide*.

**Topics**
+ [Work with customer-managed prefix lists](work-with-cust-managed-prefix-lists.md)