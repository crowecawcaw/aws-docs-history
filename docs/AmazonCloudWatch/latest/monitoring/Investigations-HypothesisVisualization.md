# Understanding hypothesis
 visualizations

When CloudWatch investigations generates hypotheses that include multiple resources, the investigation view
 provides a visual representation of the causal relationships between those resources.
 This visual hypothesis view helps you quickly understand complex issues without reading
 lengthy text explanations.

The hypothesis visualization displays resources as nodes connected by the pathways
 identified by CloudWatch investigations. For example, if a hypothesis involves Lambda function A affecting
 DynamoDB table B, you'll see two nodes visualizing the relationship.

**Key features of hypothesis visualizations:**


* **Resource nodes** - Each AWS resource
 mentioned in the hypothesis appears as a distinct node, labeled with the
 resource type and identifier.
* **Connections** - Connections between nodes
 indicate the relationships that CloudWatch investigations has identified.
* **Visual context** - The layout helps you
 understand the scope and complexity of multi-resource issues at a glance.
This visual representation is particularly valuable for:


* Understanding distributed system failures that span multiple services
* Identifying upstream and downstream impact relationships
* Quickly assessing the scope of an issue before diving into detailed
 analysis
###### Note

Hypothesis visualizations are automatically generated when CloudWatch investigations identifies causal
 relationships between multiple resources.
