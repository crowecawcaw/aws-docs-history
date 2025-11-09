# MIDACOST02-BP06 Implement manufacturing-aware cost controls

Establish effective guardrails that help prevent unnecessary spending while maintaining
operational efficiency and flexibility for production demands. This includes implementing
approval workflows that don't hinder urgent production needs and differentiating between cost
controls for different environments (production, development, testing).

**Desired outcome:** Effective guardrails that help prevent
unnecessary spending while maintaining operational efficiency and flexibility for production
demands.

**Common anti-patterns:**

- Applying blanket cost controls without considering critical manufacturing systems
- Implementing rigid resource limits that don't account for production variability
- Neglecting to create separate cost control policies for research and development, production, and
  quality assurance environments
- Failing to align cost control measures with manufacturing cycles and seasonal demands
- Implementing approval workflows that cause delays in scaling resources for urgent
  production needs
- Not differentiating between cost controls for operational data and long-term
  compliance data storage
- Implementing strict policies that hinder engineering research and development or applying overly
  permissive policies that lead to over provisioning
- Not training employees on best practices of deploying right-sized
  infrastructure/services that balance cost and performance

**Benefits of establishing this Best Practice:**

- Avoided cost overruns
- Controlled resource provisioning
- Enhanced budget compliance
- Improved cost predictability

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Establish mechanisms to monitor, control, and optimize cloud spending for manufacturing
workloads while verifying that critical operational systems maintain necessary resources.

### Implementation steps

1. Define cost control mechanisms:
   - Budget thresholds
   - Resource limits
   - Approval workflows

2. Implement automated enforcement.
3. Create exception processes.
4. Monitor control effectiveness.
5. Regular review and adjustment.

## Key AWS services

- AWS Budgets
- AWS Cost Explorer
- AWS Service Quotas
- AWS Organizations
- AWS CloudFormation
- AWS Control Tower

## Resources

**Related documents:**

- [Managing your costs with AWS Budgets](../../../cost-management/latest/userguide/budgets-managing-costs.md "../../../cost-management/latest/userguide/budgets-managing-costs.md")
- [Analyzing your costs and usage with AWS Cost Explorer](../../../cost-management/latest/userguide/ce-what-is.md "../../../cost-management/latest/userguide/ce-what-is.md")
- [AWS Service Quotas](../../../servicequotas/latest/userguide/intro.md "../../../servicequotas/latest/userguide/intro.md")
- [AWS Cost Management](../../../cost-management/latest/userguide/manage-cost-categories.md "../../../cost-management/latest/userguide/manage-cost-categories.md")
