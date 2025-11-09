# MIDACOST04-BP01 Perform an analysis on the historical manufacturing workloads

Make data-driven resource provisioning decisions based on accurate historical usage
patterns in manufacturing environments. This involves analyzing at least one full production
cycle's data, considering seasonal variations, and accounting for planned maintenance windows
in resource forecasting.

**Desired outcome:** Data-driven resource provisioning
decisions based on accurate historical usage patterns in manufacturing environments.

**Common anti-patterns:**

- Using IT-only metrics without considering manufacturing operations data
- Basing forecasts on insufficient historical data (needs at least one full production
  cycle)
- Ignoring seasonal production variations in resource planning
- Not differentiating between development, testing, and production environment needs
- Failing to account for planned maintenance windows in resource forecasting
- Using the same forecasting model for both batch and continuous production processes
- Overlooking equipment upgrade cycles in long-term resource planning
- Not considering quality control and compliance requirements in resource forecasting

**Benefits of establishing this best practice:**

- Improved capacity planning
- Reduced overprovisioning
- Better alignment with production patterns
- Optimized resource costs

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Before you begin, you will need:

- At least one full production cycle's data
- Historical resource usage patterns across seasons
- Manufacturing schedules and maintenance windows documented

Key decisions needed:

- Forecast horizon based on production cycles
- Resource allocation thresholds for different workload types
- Scaling trigger points aligned with manufacturing needs
- Data retention requirements for compliance

Systematically collect and analyze resource utilization data from manufacturing
systems to identify usage patterns and correlations with production cycles. Use these
insights to create forecasting models that align with actual manufacturing operations,
considering both IT and OT systems for comprehensive resource planning.

### Implementation steps

1. Collect historical data on:
   - Resource utilization
   - Production cycles
   - Seasonal variations
   - Peak usage periods

2. Analyze patterns and trends:
   - Daily/weekly/monthly patterns
   - Production correlation
   - Seasonal impacts

3. Create baseline metrics.
4. Develop forecasting models.
5. Validate predictions against actual usage.

## Key AWS services

- Quick Suite
- AWS Cost Explorer
- Amazon CloudWatch
- AWS Systems Manager
- Amazon SageMaker AI

## Resources

**Related documents:**

- [Quick Suite](../../../quicksight/latest/user/creating-visuals.md "../../../quicksight/latest/user/creating-visuals.md")
- [Analyzing your costs and usage with AWS Cost Explorer](../../../cost-management/latest/userguide/ce-what-is.md "../../../cost-management/latest/userguide/ce-what-is.md")
- [Metrics in Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md")
- [AWS Systems Manager Inventory](../../../systems-manager/latest/userguide/systems-manager-inventory.md "../../../systems-manager/latest/userguide/systems-manager-inventory.md")
- [AWS Compute Optimizer](../../../compute-optimizer/latest/ug/best-practices-for-compute-optimizer.md "../../../compute-optimizer/latest/ug/best-practices-for-compute-optimizer.md")
- [Use the
  SageMaker AI AI DeepAR forecasting algorithm](../../../sagemaker/latest/dg/deepar.md "../../../sagemaker/latest/dg/deepar.md")
- [Time Series Forecasts in Amazon SageMaker AI Canvas](../../../sagemaker/latest/dg/canvas-time-series.md "../../../sagemaker/latest/dg/canvas-time-series.md")
