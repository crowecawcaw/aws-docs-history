# Cloud Financial Management

| CMCOST_5: Have you defined a tagging strategy for your connected mobility<br>workloads? |
| --------------------------------------------------------------------------------------- |
|                                                                                         |

Resource classification allows you to categorize resources, providing clarity on
usage and enabling you to allocate costs accurately to different departments or projects.
Targeted Cost Allocation with tags, you can pinpoint specific resources and their costs,
allowing for precise billing and enabling you to identify areas where cost-saving measures
can be implemented effectively.

**[CMCOST\_BP5.1] Define and implement an organizational tagging
strategy, and require key tags.**

- Engage with relevant stakeholders across line which could include line of business
  teams, financial and governance teams, cloud operations teams, and other stakeholders.
  Define the use cases needed for tagging, define required versus optional tags, discuss
  ways to enforce tagging, and who will own the tagging of resources. As an example, you
  might want to define a tag to track resources used for a specific OEM to allow you to
  allocate costs appropriately.
- Publish a common and consistent naming schema. This should
  include naming and value conventions, publishing required
  and optional tags, and define and publish the process for
  adding new tags, or modifying existing tags.
- Implement your tagging strategy:
  - For manually managed resources you can use AWS Config
    which can be used to look for required tags, and if
    missing, apply them to resources using Lambda.
  - When using infrastructure as code (IaC), use the CloudFormation resources tag
    property to define tags to add required tags on resource creation. This action helps
    ensure that required tags are configured before resource creation. Use AWS CloudFormation
    Hooks to check before resource creation, and warn or prevent resource creation when
    missing key tags.

- Enforcing your tagging can be done using tagging policies and service control
  policies (SCP) in combination.
  - Tagging policies allow you to define and standardize your tag keys, including
    capitalization, and what values are allowed to be used within the specific tag.
  - Service control policies allow you to block resource creation when required
    tags are missing.
