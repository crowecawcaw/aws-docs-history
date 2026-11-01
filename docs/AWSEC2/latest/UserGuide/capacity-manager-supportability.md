

# Check supportability
<a name="capacity-manager-supportability"></a>

Use real-time supportability checks to score a configuration against current Amazon EC2 capacity when you plan or scale up a workload. You define your flexibility: the instance types and Availability Zones your workload can use, and how much capacity you need. In return, you get a score for each option plus one for the set as a whole. These checks help you decide where to flex: confirm that a launch is supportable, find where capacity is strongest across your options, or diagnose a launch failure, all without launching instances or incurring cost.

**Note**  
Real-time supportability checks are available only to AWS Support customers on the [Unified Operations plan](https://docs.aws.amazon.com/awssupport/latest/user/unified-operations-intro.html). Account-level Amazon EC2 Capacity Manager is all you need — no organization-level setup is required.

Workloads that scale up large amounts of capacity rely on flexibility to get it: the more instance types and Availability Zones a workload can use, the more options Amazon EC2 has to fulfill the request. Real-time supportability checks show how well each option, and your set as a whole, can support a request, so you can see where to add flexibility before you scale up. A check reflects capacity at a point in time. It doesn't reserve capacity or guarantee that a later launch will succeed.

**Note**  
You can't share the results of real-time supportability checks with third parties. For more information about the terms that govern your use of this data, see the [AWS Service Terms](https://aws.amazon.com/service-terms/) on the AWS website.

**Topics**
+ [How to check capacity](capacity-manager-check-capacity.md)
+ [What the scores mean](capacity-manager-score-meaning.md)
+ [What to do based on your score](capacity-manager-score-actions.md)
+ [EC2 Capacity Manager quotas](capacity-manager-check-quotas.md)
+ [Relationship to Spot placement score](capacity-manager-sps.md)