# Best Practice 2.4 – Use multiple

environments

Use multiple SAP environments to experiment, develop, and test your workload. Use
increasing levels of controls as environments approach production to gain confidence your
workload will operate as intended when deployed. Generally, a three-tier environment for
development, test, and production is minimum for SAP landscapes.

**Suggestion 2.4.1 - Use temporary environments for
experimentation**

Provide technology testing and developer teams with sandbox or temporary environments
with minimized controls to enable experimentation and risk mitigation.

- AWS Documentation: [AWS
  Launch Wizard for SAP](https://aws.amazon.com/launchwizard/ "https://aws.amazon.com/launchwizard/")
- SAP on AWS Blog: [Infrastructure as Code Example: Terraform and SAP on AWS](https://aws.amazon.com/blogs/awsforsap/terraform-your-sap-infrastructure-on-aws/ "https://aws.amazon.com/blogs/awsforsap/terraform-your-sap-infrastructure-on-aws/")
- SAP on AWS Blog: [Automate Start or Stop of Distributed SAP HANA systems using AWS Systems
  Manager](https://aws.amazon.com/blogs/awsforsap/automate-start-or-stop-of-distributed-sap-hana-systems-using-aws-systems-manager/ "https://aws.amazon.com/blogs/awsforsap/automate-start-or-stop-of-distributed-sap-hana-systems-using-aws-systems-manager/")

**Suggestion 2.4.2 - Provide development environments to allow work in
parallel and improved agility**

Provide non-production environments to allow work in parallel, increasing development
and test agility. Implement more rigorous controls in the environments approaching
production to allow developers the necessary means for innovation. Generally, a three-tier
environment for Development, Test and Production is minimum for SAP environments.

**Suggestion 2.4.3 - Provide a consolidated test environment that
replicates production as closely as possible to improve release quality**

Test and staging environments should mirror as closely as possible the interfaces,
security, resilience, and performance characteristics of your production environment to
identify architectural and code interaction problems before being released. Consider
shutting down secondary resources in clusters or scaling down (both horizontally and
vertically) application server performance of this environment when not in use to improve
landscape cost efficiency.

**Suggestion 2.4.4 - Use infrastructure as code (IaC) and
configuration management systems to deploy environments consistently**

Use infrastructure as code (IaC) and configuration management systems to deploy
environments that are configured consistent with the controls present in production to
ensure systems operate as expected when deployed. Use tagging and resource groups to label
and enhance environment metadata such that it can be used for automation and compliance
purposes.

- AWS Documentation: [AWS Launch
  Wizard for SAP](https://aws.amazon.com/launchwizard/ "https://aws.amazon.com/launchwizard/")
- SAP on AWS Blog: [Infrastructure as Code Example: Terraform and SAP on AWS](https://aws.amazon.com/blogs/awsforsap/terraform-your-sap-infrastructure-on-aws/ "https://aws.amazon.com/blogs/awsforsap/terraform-your-sap-infrastructure-on-aws/")
- AWS Documentation: [What are AWS
  Resource Groups?](../../../ARG/latest/userguide/welcome.md "../../../ARG/latest/userguide/welcome.md")
- SAP on AWS Blog: [Tagging Recommendations for SAP on AWS](https://aws.amazon.com/blogs/awsforsap/tagging-recommendations-for-sap-on-aws/ "https://aws.amazon.com/blogs/awsforsap/tagging-recommendations-for-sap-on-aws/")

**Suggestion 2.4.5 - Turn off non-production environments when not in
use**

When environments are not in use, turn them off to avoid costs associated with idle
resources (for example, development systems on evenings and weekends).

- SAP on AWS Blog: [Automate Start or Stop of Distributed SAP HANA systems using AWS Systems
  Manager](https://aws.amazon.com/blogs/awsforsap/automate-start-or-stop-of-distributed-sap-hana-systems-using-aws-systems-manager/ "https://aws.amazon.com/blogs/awsforsap/automate-start-or-stop-of-distributed-sap-hana-systems-using-aws-systems-manager/")
