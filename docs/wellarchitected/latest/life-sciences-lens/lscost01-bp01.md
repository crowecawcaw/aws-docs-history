# LSCOST01-BP01 Establish and implement a comprehensive financial

governance framework

A financial governance framework in life sciences cloud management
establishes the structure, policies, and processes for making
financial decisions related to cloud usage. It verifies that cloud
spending aligns with research priorities, regulatory requirements,
and overall business objectives.

**Desired outcome:** A mature,
organization-wide financial governance environment that provides
complete visibility and control over cloud spending across each life
sciences research initiative, enabling predictable budget
management, automated cost optimization, and strategic alignment
between cloud investments and research outcomes while adhering to
regulatory and organizational financial policies.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Build a
[Cloud
Center of Excellence (CCoE)](../../../prescriptive-guidance/latest/cloud-center-of-excellence/introduction.md "../../../prescriptive-guidance/latest/cloud-center-of-excellence/introduction.md") with representatives from
research, IT, finance, and security.

Develop a cloud cost allocation model that ties expenses to
specific research projects or therapeutic areas.

Implement tagging policies and service control policies (SCPs) to
enforce tagging strategies across your organization.

Establish approval workflows for high-cost cloud resources with
different thresholds for various research stages. For
example, consider using
[AWS Budgets](../../../cost-management/latest/userguide/budgets-managing-costs.md "../../../cost-management/latest/userguide/budgets-managing-costs.md") for cost management and
[Service Catalog](https://aws.amazon.com/servicecatalog/ "https://aws.amazon.com/servicecatalog/") for deployment of pre-approved services.

### Implementation steps

1. Form the Cloud Center of Excellence (CCoE):
   - Identify key stakeholders from your organization's
     departments.
   - Define roles and responsibilities for each CCoE member.
   - Schedule regular CCoE meetings to oversee the framework
     implementation.

2. Develop the cloud cost allocation model:
   - Map out existing research projects and therapeutic
     areas.
   - Create a cost structure that links cloud expenses to
     specific initiatives.
   - Design a reporting system to track and allocate costs
     accurately.

3. Implement tagging policies:
   - Define a comprehensive tagging strategy for cloud
     resources.
   - Create service control policies (SCPs) to enforce the
     tagging rules.
   - Configure automated tagging where possible to improve
     consistency.

4. Establish approval workflows:
   - Define thresholds for high-cost cloud resources at
     different research stages
   - Set up AWS Budgets for cost management:
     - Create budget alerts for various spending
       thresholds.
     - Configure notifications for key stakeholders when
       budgets are approaching limits.

   - Implement Service Catalog:
     - Create a portfolio of pre-approved services and
       resources.
     - Set up governance and access controls for the
       Service Catalog.

5. Continuous improvement:
   - Stay informed about new cloud services and cost
     optimization strategies.
   - Regularly update the framework to incorporate best
     practices and new technologies.
