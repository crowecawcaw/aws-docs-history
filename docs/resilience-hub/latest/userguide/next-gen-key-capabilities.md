# Key capabilities at a glance

Next generation Resilience Hub provides the following key capabilities:

- **Application modeling** – Model your applications
  using a hierarchy that matches how your organization thinks about them. Systems represent your
  business applications, user journeys describe critical end-user paths within a system, and
  services are the building blocks comprising AWS resources that support user journeys. You
  define where to find your AWS resources (AWS CloudFormation stacks, Terraform state files, resource
  tags, or Amazon EKS clusters), and Resilience Hub automatically discovers and maps them into a
  topology showing how resources connect.
- **Dependency discovery** – Continuously
  discovers and maps dependencies for your services, including AWS services, internal endpoints,
  and third-party endpoints.
- **Failure mode assessments (GenAI-powered)** – Analyzes
  your services against resilience policies and AWS Well-Architected best practices to identify
  potential failure modes and recommend improvements.
- **Resilience tests** – Tests your services to verify
  recovery objectives are met and dependencies behave as expected, such as Availability Zone
  impairment, Regional impairment, and dependency failure.
- **Resilience policies** – Modular, composable
  requirements for availability SLO, Multi-Region disaster recovery, Multi-AZ disaster recovery,
  and data recovery objective.
- **AWS Organizations integration** – Centralized
  governance across multiple accounts with delegated administrator support and organization-wide
  resilience policies.
  For enterprise-scale deployments, Next generation Resilience Hub integrates with AWS Organizations to
  provide centralized resilience management across your entire organization from a single delegated
  administrator account. You get organization-wide visibility into resilience posture and
  aggregated dashboards without logging in to individual accounts.
