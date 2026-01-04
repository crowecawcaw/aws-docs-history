# LSSUS01-BP02 Use energy efficient hardware and

services

Select energy-efficient hardware architectures and managed services
that optimize power consumption while maintaining research computing
performance. Prioritize modern processor architectures and cloud
services that incorporate built-in sustainability optimizations to
reduce the environmental impact of computational workloads.
Implement hardware and service selection strategies that balance
performance requirements with energy efficiency goals.

**Desired outcome:** Achieve
significant energy consumption reduction in research computing
operations while maintaining or improving computational performance.
Implement hardware and service architectures that provide optimal
performance-per-watt ratios for life sciences workloads.

**Common anti-patterns:**

- You default to traditional x86 architectures without evaluating
  energy-efficient alternatives.
- You don't consider managed services that provide built-in
  sustainability optimizations.
- You don't evaluate the total cost of ownership including energy
  consumption.
- You run custom infrastructure instead of using optimized managed
  services.
- You don't monitor and measure energy efficiency metrics across
  your compute infrastructure.

**Benefits of establishing this best
practice:**

- Reduce energy consumption by up to 60% through modern processor
  architectures like AWS Graviton.
- Lower operational costs through improved performance-per-watt
  ratios.
- Improve research productivity with automatically optimized
  resource allocation.
- Support organizational sustainability goals and regulatory
  adherence requirements.
- Benefit from continuous service improvements and optimizations
  provided by managed services.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Energy-efficient hardware selection is crucial for life sciences
organizations seeking to reduce their environmental impact while
maintaining research computing capabilities. Modern processor
architectures like AWS Graviton processors offer significant
energy efficiency improvements over traditional x86 architectures,
particularly for compute-intensive workloads common in genomics,
proteomics, and molecular modeling. These efficiency gains
compound over time, making hardware selection a critical
sustainability decision.

Managed services provide additional sustainability benefits by
incorporating built-in optimizations that individual organizations
would struggle to implement independently. Services like AWS HealthOmics, AWS HealthLake, and AWS Batch continuously
optimize resource utilization, automatically scale based on
demand, and use the latest energy-efficient infrastructure
improvements. This approach allows research teams to focus on
scientific outcomes while benefiting from ongoing sustainability
improvements.

### Implementation steps

1. Evaluate and migrate to energy-efficient processor
   architectures:
   - Assess workload compatibility with AWS Graviton
     processors for ARM-based computing.
   - Use Amazon EC2 M6g, C6g, and R6g instances for
     general-purpose, compute-optimized, and memory-optimized
     workloads.
   - Benchmark performance and energy consumption for
     representative research workloads.
   - Consider AWS Graviton3 processors for the latest
     efficiency improvements.

2. Use managed services with built-in sustainability
   optimizations:
   - Migrate genomics workflows to AWS HealthOmics for
     automated resource optimization.
   - Use AWS HealthLake for healthcare data processing
     with built-in efficiency features.
   - Implement AWS Batch for containerized workloads with
     automatic scaling and optimization.
   - Consider Amazon SageMaker AI for machine learning workloads
     with energy-efficient training.

3. Optimize service configurations for energy efficiency:
   - Enable AWS Auto Scaling to automatically adjust capacity
     based on demand.
   - Configure AWS Lambda for event-driven processing to
     minimize idle resource consumption.
   - Use Amazon ECS with AWS Fargate for serverless container
     execution.
   - Implement AWS Step Functions for efficient workflow
     orchestration.

4. Monitor and measure energy efficiency improvements:
   - Track performance-per-watt metrics using Amazon CloudWatch custom metrics.
   - Monitor cost savings and energy reduction.
   - Implement AWS Config rules to adhere to energy
     efficiency policies.

5. Establish continuous optimization processes:
   - Regularly review AWS service updates for new energy
     efficiency features.
   - Conduct periodic assessments of hardware and service
     selection decisions.
   - Set up automated alerts for suboptimal resource
     utilization patterns.
   - Create feedback loops to incorporate energy efficiency
     learnings into future architecture decisions.

## Resources

**Related best practices:**

- [LSSUS01-BP01
  Design high-performance computing workloads to minimize energy
  usage](sustainability/research-computing-optimization/lssus01-bp01.md "sustainability/research-computing-optimization/lssus01-bp01.md")
- [LSSUS02-BP01
  Implement sustainability proxy metrics pipeline for research
  workloads](sustainability/sustainability-metric-tracking-and-reporting/lssus02-bp01.md "sustainability/sustainability-metric-tracking-and-reporting/lssus02-bp01.md")

**Related documents:**

- [Improving
  Sustainability and Price Performance Using AWS Graviton–Based
  Instances with Pinterest](https://aws.amazon.com/solutions/case-studies/pinterest-graviton-case-study/ "https://aws.amazon.com/solutions/case-studies/pinterest-graviton-case-study/")

**Related videos:**

- [How
  to optimize workloads for sustainability using AWS
  Graviton-based EC2 instances](https://www.youtube.com/watch?v=pzSvcsduijM&t=804s "https://www.youtube.com/watch?v=pzSvcsduijM&t=804s")

**Related examples:**

- [AWS Graviton Getting Started](https://github.com/aws/aws-graviton-getting-started "https://github.com/aws/aws-graviton-getting-started")
- [AWS HealthOmics Workflows](https://github.com/aws-samples/amazon-omics-tutorials "https://github.com/aws-samples/amazon-omics-tutorials")
