# Amazon EKS Best Practices Guide

###### Tip

[Explore](https://aws-experience.com/emea/smb/events/series/get-hands-on-with-amazon-eks?trk=4a9b4147-2490-4c63-bc9f-f8a84b122c8c&sc_channel=el "https://aws-experience.com/emea/smb/events/series/get-hands-on-with-amazon-eks?trk=4a9b4147-2490-4c63-bc9f-f8a84b122c8c&sc_channel=el") best practices through Amazon EKS workshops.

Welcome to the EKS Best Practices Guides. The primary goal of this
project is to offer a set of best practices for day 2 operations for
Amazon EKS. We elected to publish this guidance to GitHub so we could
iterate quickly, provide timely and effective recommendations for
variety of concerns, and easily incorporate suggestions from the broader
community.

We currently have published guides for the following topics:

- [Best Practices for Security](security.md "security.md")
- [Best Practices for Reliability](reliability.md "reliability.md")
- [Best Practices for Cluster Autoscaling: Karpenter](karpenter.md "karpenter.md")
- [Best Practices for Cluster Autoscaling: cluster-autoscaler](cas.md "cas.md")
- [Best Practices for Cluster Autoscaling: EKS Auto Mode](automode.md "automode.md")
- [Best Practices for Networking](networking.md "networking.md")
- [Best Practices for Scalability](scalability.md "scalability.md")
- [Best Practices for Cluster Upgrades](cluster-upgrades.md "cluster-upgrades.md")
- [Best Practices for Cost Optimization](cost-opt.md "cost-opt.md")
- [Best Practices for Running Windows Containers](windows.md "windows.md")
- [Best Practices for Hybrid Deployments](hybrid.md "hybrid.md")
- [Best Practices for Running AI/ML Workloads](aiml.md "aiml.md")
  We also open sourced a Python based CLI (Command Line Interface) called
  [hardeneks](https://github.com/aws-samples/hardeneks "https://github.com/aws-samples/hardeneks") to check some of the
  recommendations from this guide.

In the future we will be publishing best practices guidance for
performance, cost optimization, and operational excellence.

## Related guides

In addition to the
[EKS
User Guide](../userguide/what-is-eks.md "../userguide/what-is-eks.md"), AWS has published several other guides that may help you
with your implementation of EKS.

- [EMR
  Containers Best Practices Guides](https://aws.github.io/aws-emr-containers-best-practices/ "https://aws.github.io/aws-emr-containers-best-practices/")
- [Data on EKS](https://awslabs.github.io/data-on-eks/ "https://awslabs.github.io/data-on-eks/")
- [AWS
  Observability Best Practices](https://aws-observability.github.io/observability-best-practices/ "https://aws-observability.github.io/observability-best-practices/")
- [Amazon EKS
  Blueprints for Terraform](https://aws-ia.github.io/terraform-aws-eks-blueprints/ "https://aws-ia.github.io/terraform-aws-eks-blueprints/")
- [Amazon EKS
  Blueprints Quick Start](https://aws-quickstart.github.io/cdk-eks-blueprints/ "https://aws-quickstart.github.io/cdk-eks-blueprints/")

## Contributing

We encourage you to contribute to these guides. If you have implemented
a practice that has proven to be effective, please share it with us by
opening an issue or a pull request. Similarly, if you discover an error
or flaw in the guidance we’ve already published, please submit a PR to
correct it. The guidelines for submitting PRs can be found in our
[Contributing
Guidelines](https://github.com/aws/aws-eks-best-practices/blob/master/CONTRIBUTING.md "https://github.com/aws/aws-eks-best-practices/blob/master/CONTRIBUTING.md").
