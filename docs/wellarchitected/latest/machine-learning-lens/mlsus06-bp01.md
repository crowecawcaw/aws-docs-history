# MLSUS06-BP01 Measure material efficiency

Measure efficiency of your workload in provisioned resources per
unit of work to determine not only the business success of the
workload, but also its material efficiency. Use this measure as a
baseline for your sustainability improvement process.

**Desired outcome:** You can quantify
and track the resources required by your machine learning workload
to deliver its business outcomes. By measuring resources per unit of
work, you create a sustainable baseline that allows you to track
improvements over time, make data-driven decisions about resource
optimization, and demonstrate the environmental impact of your
sustainability efforts.

**Common anti-patterns:**

- Focusing exclusively on business metrics without considering
  resource consumption.
- Measuring total resource usage without normalizing by business
  outcomes.
- Making optimization decisions without quantitative data on
  resource efficiency.

**Benefits of establishing this best
practice:**

- Creates a clear way to measure sustainability progress over
  time.
- Enables comparison of different implementations based on
  material efficiency.
- Provides data to demonstrate ROI on sustainability improvements.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Material efficiency is a critical aspect of sustainable machine
learning workloads. By measuring the resources provisioned per
unit of work, you gain visibility into how efficiently your
workload uses cloud resources to deliver business value. This
approach normalizes your sustainability metrics across different
workload sizes, usage patterns, and business outcomes.

When implementing material efficiency measurements, you should
first determine what constitutes a _unit of
work_ for your specific ML workload. This could be a
model training run, a prediction request, a processed transaction,
or another relevant business outcome. Then, establish which
resources to track. Typically, this is compute (vCPU minutes),
storage (GB), and network (GB transferred). By dividing your
provisioned resources by these units of work, you create a
normalized efficiency metric that can be tracked over time.

For example, a recommendation engine might track vCPU minutes per
recommendation delivered, or a fraud detection system could
measure GB of storage per fraudulent transaction identified.
Tracking these metrics can determine if changes to your
architecture, algorithms, or deployment strategies are improving
efficiency or creating waste.

### Implementation steps

1. **Define your unit of work**.
   Identify what business outcomes your ML workload produces,
   such as model training completions, predictions made,
   insights generated, or transactions processed. Verify that
   this metric directly relates to business value delivered.
2. **Establish resource
   metrics**. Track key resource consumption metrics
   using Amazon CloudWatch. For ML workloads, important metrics
   include compute utilization (vCPU minutes), memory usage,
   storage consumption (GB), and network transfer (GB). AWS Cost Explorer can identify key cost drivers in your ML
   workload.
3. **Calculate baseline
   efficiency**. Divide your resource consumption
   metrics by your units of work to create efficiency ratios
   (for example, vCPU minutes per prediction, GB storage per
   model training run, or network transfer per transaction).
   Document these values as your baseline for future
   comparisons.
4. **Set improvement targets**.
   Based on your baseline measurements, set realistic targets
   for reducing resource consumption per unit of work. Consider
   both absolute reductions (total resources) and percentage
   improvements over the baseline.
5. **Implement monitoring and
   reporting**. Use Amazon CloudWatch dashboards to
   visualize your efficiency metrics over time. Set up alerts
   for significant deviations from expected efficiency. Amazon SageMaker AI provides built-in monitoring capabilities for ML
   workloads to track resource utilization.
6. **Quantify improvement
   benefits**. When implementing changes, calculate
   both the immediate resource savings and the projected
   long-term benefits. Include the return on investment from
   your improvement activities to demonstrate value to
   stakeholders.
7. **Review and optimize
   regularly**. Schedule regular reviews of your
   efficiency metrics to identify new optimization
   opportunities. As your workload evolves, your baseline and
   targets may need adjustment.

## Resources

**Related documents:**

- [Analyzing
  your costs and usage with AWS Cost Explorer](../../../awsaccountbilling/latest/aboutv2/ce-what-is.md "../../../awsaccountbilling/latest/aboutv2/ce-what-is.md")
- [Data
  and model quality monitoring with Amazon SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [AWS Trusted Advisor](../../../awssupport/latest/user/trusted-advisor.md "../../../awssupport/latest/user/trusted-advisor.md")
- [Measure
  results and replicate successes](../sustainability-pillar/measure-results-and-replicate-successes.md "../sustainability-pillar/measure-results-and-replicate-successes.md")
- [AWS Well-Architected Framework - Sustainability Pillar](../sustainability-pillar/sustainability-pillar.md "../sustainability-pillar/sustainability-pillar.md")
- [Cloud
  Financial Management with AWS](https://aws.amazon.com/aws-cost-management/ "https://aws.amazon.com/aws-cost-management/")
