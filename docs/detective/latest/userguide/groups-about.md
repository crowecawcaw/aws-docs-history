# Analyzing finding groups

Amazon Detective finding groups let you examine multiple activities as they relate to a potential
security event. A finding group in Amazon Detective is created when Detective detects a pattern or
relationship among multiple findings that suggest they are related to the same potential
security incident. This grouping helps in managing and investigating related findings more
efficiently.

You can analyze the root cause for high severity GuardDuty findings using finding groups. If a
threat actor is attempting to compromise your AWS environment, they typically perform a
sequence of actions that lead to multiple security findings and unusual behaviors. These
actions are often spread across time and entities. When security findings are investigated
in isolation, it can lead to a misinterpretation of their significance, and difficulty in
finding the root cause. Amazon Detective addresses this problem by applying a graph analysis
technique that infers relationships between findings and entities, and groups them together.
We recommend treating finding groups as the starting point for investigating the involved
entities and findings.

Detective analyzes data from findings and groups them with other findings that are
likely to be related based on resources they share. For example, findings related to actions
taken by the same IAM role sessions or originating from the same IP address are very
likely to be part of the same underlying activity. It's valuable to investigate findings and
evidence as a group, even if the associations made by Detective aren't related.

Finding groups are created based on the following criteria.

- Temporal Proximity – Findings that occur within a close time frame are
  often grouped together, as they are likely related to the same incident.
- Common Entities – Findings involving the same entities, such as IP
  addresses, users, or resources, are grouped together. This helps in understanding
  the scope of the incident across different parts of the environment.
- Patterns and Behaviors – Detective analyzes patterns and behaviors in the
  findings, such as similar types of attacks or suspicious activities, to determine
  relationships and group them accordingly.
- Tactics, Techniques, and Procedures (TTPs) – Findings that share similar
  TTPs, as described in frameworks like MITRE ATT&CK, are grouped together to
  highlight potential coordinated attacks.
  These criteria help streamline the investigation process so you can focus on correlated
  findings that likely represent the same security incident.

In addition to findings, each group includes entities involved in the findings.
The entities can include resources outside of AWS such as IP Addresses or user
agents.

###### Note

After an initial GuardDuty finding occurs that is related to another finding, the finding group
with all related findings and all involved entities is created within 48 hours.
