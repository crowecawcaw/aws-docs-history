**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Using the network topology map

The network security director network topology map provides a visual representation of your network resources and their connections.
This visualization helps you understand how your resources are connected and identify potential security issues in your network architecture.
The network topology map is available for findings after the latest network analysis completes.

## Understanding the network topology map

The network topology map uses nodes and connections to represent your network resources and their relationships:

- **Nodes** represent individual resources such as Amazon EC2 instances, Application Load Balancers, AWS WAF protection packs (web ACLs), and other network components.
- **Connections** represent the relationships between resources, such as traffic flow or protection relationships.
- **Colors** indicate the severity level of resources, with darker colors representing higher severity levels.

The topology map helps you visualize:

- Which resources are exposed to the internet
- How traffic flows between resources
- Which security protections are in place
- Where potential security issues exist

## Navigating the network topology map

You can interact with the network topology map in several ways:

- **Zoom** - Use the zoom controls or your mouse wheel to zoom in and out of the map.
- **Pan** - Click and drag to move around the map.
- **Select** - Click on a node to view details about that resource.
- **Filter** - Use the filter options to focus on specific resource types or finding severity.

###### To filter the network topology map

1. In the network topology map view, locate the filter controls in the top-right corner.
2. Select the filter type you want to apply:
   - **Resource type** - Filter by specific resource types such as Amazon EC2 instances, Application Load Balancers, or AWS WAF web ACLs.
   - **Severity level** - Filter by severity level to focus on resources with specific severity ratings.
   - **Tags** - Filter by resource tags to focus on resources with specific tags.

3. Apply your selected filters to update the map view.

## Analyzing resources in the topology map

The network topology map allows you to analyze your resources and their security configuration:

###### To analyze a resource in the topology map

1. Click on a resource node in the topology map.
2. In the resource details panel that appears, review the following information:
   - **Resource details** - Basic information about the resource, including its ID, type, and tags.
   - **Severity level** - The overall severity level assigned to the resource.
   - **Findings** - Security findings associated with the resource.
   - **Connected resources** - Other resources that are connected to this resource.

3. To view detailed remediation recommendations for a finding, expand the finding and review the suggested steps.

By analyzing resources in the topology map, you can identify security findings and understand how they relate to your overall network architecture.

## Identifying security patterns in the topology map

The network topology map can help you identify common security patterns and issues:

**Internet exposure**

Resources in the topology map with a globe icon have an identified communication path to an Internet gateway. These resources have increased threat exposure due to a public communication path.

**Missing protections**

Resources that should have AWS WAF or security group protections but don't will appear with fewer connections to security services.

**Overly permissive access**

Security groups or NACLs that allow broad access will be highlighted with higher severity levels.

**Unused security resources**

Security resources like AWS WAF web ACLs that aren't connected to any other resources may be unused and could be removed.

Use these patterns to identify areas where you can improve your network security configuration.

After exploring your network topology, you may want to investigate specific findings in more detail. Continue to [Find remediation steps for your highest severity resources](nsd-remediation-steps.md "nsd-remediation-steps.md") to learn how to find detailed remediation recommendations for your resources.
