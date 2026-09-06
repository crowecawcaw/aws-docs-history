

# Share customer-managed prefix lists
<a name="sharing-managed-prefix-lists"></a>

With AWS Resource Access Manager (AWS RAM), the owner of a customer-managed prefix list can share the prefix list with the following:
+ Specific AWS accounts inside or outside of its organization in AWS Organizations
+ An organizational unit inside its organization in AWS Organizations
+ An entire organization in AWS Organizations

Consumers with whom a prefix list has been shared can view the prefix list and its entries, and they can reference the prefix list in their AWS resources.

For more information about AWS RAM, see the [AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/). For more information quotas, see [Service quotas](https://docs.aws.amazon.com/general/latest/gr/ram.html#limits_ram) in the AWS RAM User Guide.

**Important**  
There are no additional charges for sharing prefix lists.

**Topics**
+ [Shared prefix list permissions](sharing-perms.md)
+ [Work with shared prefix lists](work-with-shared-prefixes.md)