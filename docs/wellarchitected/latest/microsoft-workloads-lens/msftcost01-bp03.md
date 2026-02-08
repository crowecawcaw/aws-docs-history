# MSFTCOST01-BP03 Run platform-specific tools

Platform-specific tools, such as Azure Resource Discovery Tool, are
useful for environment understanding. This is a PowerShell script
provided by AWS that generates an inventory report including
detailed metrics of an Azure environment to which you have read
access for the previous 30 days. Especially useful for non-virtual
machine(VM) resources.

**Desired outcome:** Generate a
comprehensive 30-day inventory report using platform-specific tools
to provide detailed resource metrics, asset visibility, and usage
patterns across the Azure environment, enabling informed decisions
for cloud resource management and optimization, while documenting
key metrics that would be essential for planning a potential AWS
migration.

**Common anti-patterns:**

- Manual Resource Tracking: Relying solely on manual methods or
  spreadsheets to track cloud resources and their usage, instead
  of leveraging automated platform-specific tools. This approach
  is error-prone, time-consuming, and often results in incomplete
  or outdated information about the environment.
- One-Size-Fits-All: Using generic assessmetn tools that are not
  tailored to the specific cloud platform (in this case, Azure).
  This can lead to missed insights, inability to capture
  platform-specific metrics, and incomplete understanding of
  resource utilization and costs, especially for non-VM resources
  that may have unique characteristics in Azure.

**Benefits of establishing this best
practice:**

- Comprehensive Resource Visibility: Platform-specific tools
  provide detailed, accurate insights into all resources within
  the Azure environment, including often overlooked non-VM
  resources. This comprehensive view enables better resource
  management, cost optimization, and capacity planning.
- Time and Effort Efficiency: Automated platform-specific tools
  can quickly generate detailed reports that would take
  significantly longer to compile manually. This efficiency allows
  IT teams to focus on analyzing the data and making strategic
  decisions rather than spending time on data collection and
  organization.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

To implement this best practice, start by identifying and
selecting appropriate platform-specific tools for Azure, such as
Resource Discovery. Ensure you have the necessary read permissions
across your Azure environment. Schedule regular automated runs of
these tools, ideally on a monthly basis, to capture a rolling
30-day window of resource utilization. Set up a process to review
and analyze the generated reports, focusing on resource
allocation, usage patterns, and potential optimization
opportunities. Integrate these insights into your cloud management
and decision-making processes, and use the data to inform capacity
planning, cost optimization strategies, and potential migration
assessments. Regularly update and refine your use of these tools
as your Azure environment evolves and as new features become
available.

### Implementation steps

1. Verify the required access permissions across all target
   Azure subscriptions and resource groups
2. Install and configure the chosen platform-specific tool (for
   example, Azure Resource Discovery Tool)
3. Save the output data
4. Contact your AWS account team to help analyzing Azure
   resources in preparation for potential AWS migration
   scenarios

## Resources

**Related tools:**

- [Azure
  Resource Discovery Tool](https://github.com/awslabs/resource-discovery-for-azure "https://github.com/awslabs/resource-discovery-for-azure")
