

# Release: Elastic Beanstalk Cluster Mode for running multiple applications on shared infrastructure on September 17, 2026
<a name="release-2026-09-17-cluster-mode"></a>

AWS Elastic Beanstalk introduces Cluster Mode, a new deployment mode that lets you run and manage multiple applications on shared infrastructure in your account, powered by Amazon Elastic Kubernetes Service (Amazon EKS).

**Release date:** September 17, 2026

## Changes
<a name="release-2026-09-17-cluster-mode.changes"></a>

Provide your source code, a Dockerfile, or a container image in Amazon ECR, and Elastic Beanstalk handles containerization, provisioning, and ongoing operations through the console, CLI, and APIs you already use. A new Elastic Beanstalk GitHub Action deploys your application directly from your repository as part of your CI/CD pipeline.

Elastic Beanstalk now offers two deployment modes. Standard Mode is the existing Elastic Beanstalk experience and continues to support all currently available platforms, including .NET, Node.js, and Python. Cluster Mode runs multiple applications on pooled infrastructure in your account, powered by Amazon EKS, instead of a dedicated environment per application. This can lower your per-application compute cost as your applications scale or your application count grows. Cluster Mode supports event-driven autoscaling, OpenTelemetry-based observability to Amazon CloudWatch and third-party providers, AWS Secrets Manager integration, and HTTPS by default via AWS Certificate Manager.

To get started, create an environment in the Elastic Beanstalk console and select Cluster Mode. You can also deploy with the AWS CLI, the GitHub Action, or the agent skills.

Cluster Mode is available in all commercial AWS Regions where Elastic Beanstalk is available. Elastic Beanstalk is HIPAA eligible and in scope for programs including PCI DSS, SOC, FedRAMP, and IRAP. There is no additional charge for Cluster Mode. You pay for the AWS resources your applications consume, including the Amazon EKS cluster and Amazon EKS Auto Mode charges for the infrastructure Elastic Beanstalk provisions on your behalf.

To learn more, see the [AWS News blog](https://aws.amazon.com/blogs/aws/aws-elastic-beanstalk-introduces-cluster-mode/), the [*AWS Elastic Beanstalk Developer Guide*](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts-cluster.html), and the [Elastic Beanstalk product page](https://aws.amazon.com/elasticbeanstalk/), or download the [agent skills](https://github.com/aws/agent-toolkit-for-aws/blob/main/skills/core-skills/aws-containers/SKILL.md).