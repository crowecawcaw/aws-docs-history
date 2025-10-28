# FSISUS14: Do you have multi-architecture images for grid computing systems?

Multi-architecture image support for a particular workload makes it easier for you
to build different images and thus different architectures and operating systems from
the same source and refer to them all by the same abstract manifest. The manifest
specifies the layers of system content that make up the image as well as its runtime
characteristics and configuration. Having a multi-architecture image increases the
flexibility of the workload thus increases the opportunity to use hardware that may be
more sustainable.

## FSISUS14-BP01 Use instances with higher energy efficiency

**Prescriptive guidance**

- [AWS Graviton-based instances](../../../whitepapers/latest/aws-graviton-performance-testing/what-is-aws-graviton.md "../../../whitepapers/latest/aws-graviton-performance-testing/what-is-aws-graviton.md") use up to 60% less energy than comparable EC2 instances.

## FSISUS14-BP02 Design applications that can use different Amazon EC2 instance types

**Prescriptive guidance**

- This is what we would call a flexible workload. In contrast, inflexible
  workloads rely only on a few instance types. These instances types may be less
  energy efficient than others.
- Flexible workloads are ideal for Spot Instances. Running workloads on Spot
  Instances is generally considered more energy efficient than On-Demand Instances
  because Spot is overhead required for the Amazon EC2 On-Demand service to run.
- Use Amazon EC2's spare capacity with Spot Instances to extract the same value, which
  increases the total value generated from the Amazon EC2 environment as a whole.

## FSISUS14-BP03 Adopt a serverless, [event-driven

architecture](../../../lambda/latest/operatorguide/event-driven-architectures.md "../../../lambda/latest/operatorguide/event-driven-architectures.md")

**Prescriptive guidance**

- Consider using a serverless, event-driven architecture to maximize overall
  resource utilization. Serverless architecture removes the requirement to run and
  maintain physical servers since AWS handles this on your behalf.
- The cost of serverless architectures generally correlates with the level of
  usage, thus increases your workload's cost efficiency.
- **Implementation guidance:** Maximize energy efficiency
  as well as availability by building multi-architecture workloads that can run on a
  variety of Spot Instances. It is important to account for error precision when
  expanding compiler options on varying processors.
- **Service recommendations:** Use the following services
  to achieve your goal:
  - [Amazon Simple Queue Service and Amazon EC2 Spot Instances](https://aws.amazon.com/blogs/compute/running-cost-effective-queue-workers-with-amazon-sqs-and-amazon-ec2-spot-instances/ "https://aws.amazon.com/blogs/compute/running-cost-effective-queue-workers-with-amazon-sqs-and-amazon-ec2-spot-instances/")
  - [AWS CodeBuild](https://aws.amazon.com/blogs/devops/creating-multi-architecture-docker-images-to-support-graviton2-using-aws-codebuild-and-aws-codepipeline/ "https://aws.amazon.com/blogs/devops/creating-multi-architecture-docker-images-to-support-graviton2-using-aws-codebuild-and-aws-codepipeline/")

- Determine which of your workloads is suitable for use of floating-point
  accuracy, performance, and efficiency. Consider testing with a cluster of instances
  to see how well it performs at scale.
- **Implementation guidance:** For intensive financial
  simulations and calculations, test the number of bits that are required to achieve
  your floating point precision and consider reducing number of bits by selecting
  different floating-point formats, including bfloat16, that's supported by AWS
  Graviton.
- **Service recommendations:** Use the following services
  to achieve your goal:
  - [AWS Batch](https://aws.amazon.com/batch/ "https://aws.amazon.com/batch/")
  - [AWS Parallel
    Cluster](https://aws.amazon.com/hpc/parallelcluster/ "https://aws.amazon.com/hpc/parallelcluster/")
