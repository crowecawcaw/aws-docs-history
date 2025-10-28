# SUS06-BP03 Keep your workload up-to-date

Keep your workload up-to-date to adopt efficient features, remove
issues, and improve the overall efficiency of your workload.

**Common anti-patterns:**

- You assume your current architecture is static and will not be
  updated over time.
- You do not have any systems or a regular cadence to evaluate if
  updated software and packages are compatible with your workload.

**Benefits of establishing this best
practice:** By establishing a process to keep your workload
up to date, you can adopt new features and capabilities, resolve
issues, and improve workload efficiency.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Up to date operating systems, runtimes, middlewares, libraries,
and applications can improve workload efficiency and make it
easier to adopt more efficient technologies. Up to date software
might also include features to measure the sustainability impact
of your workload more accurately, as vendors deliver features to
meet their own sustainability goals. Adopt a regular cadence to
keep your workload up to date with the latest features and
releases.

### Implementation steps

- **Define a process:** Use a
  process and schedule to evaluate new features or instances for
  your workload. Take advantage of agility in the cloud to
  quickly test how new features can improve your workload to:
  - Reduce sustainability impacts.
  - Gain performance efficiencies.
  - Remove barriers for a planned improvement.
  - Improve your ability to measure and manage sustainability
    impacts.

- **Conduct an inventory:**
  Inventory your workload software and architecture and identify
  components that need to be updated.
  - You can use
    [AWS Systems Manager Inventory](../../../systems-manager/latest/userguide/systems-manager-inventory.md "../../../systems-manager/latest/userguide/systems-manager-inventory.md") to collect operating
    system (OS), application, and instance metadata from your
    Amazon EC2 instances and quickly understand which
    instances are running the software and configurations
    required by your software policy and which instances need
    to be updated.

- **Learn the update procedure:**
  Understand how to update the components of your workload.

| Workload component
| How to update
|
| --- | --- |
| Machine images | Use [EC2 Image Builder](https://aws.amazon.com/image-builder/ "https://aws.amazon.com/image-builder/") to manage updates to [Amazon Machine Images (AMIs)](../../../AWSEC2/latest/UserGuide/AMIs.md "../../../AWSEC2/latest/UserGuide/AMIs.md") for Linux or Windows server images. |
| Container images | Use [Amazon Elastic Container Registry (Amazon ECR)](../../../AmazonECR/latest/userguide/what-is-ecr.md "../../../AmazonECR/latest/userguide/what-is-ecr.md") with your existing pipeline to [manage Amazon Elastic Container Service (Amazon ECS) images](../../../AmazonECR/latest/userguide/ECR_on_ECS.md "../../../AmazonECR/latest/userguide/ECR_on_ECS.md"). |
| AWS Lambda | AWS Lambda includes [version management features.](../../../lambda/latest/dg/configuration-versions.md "../../../lambda/latest/dg/configuration-versions.md") | <br>• **Use automation:** Automate updates to reduce the level of effort to deploy new features and limit errors caused by manual processes. + You can use [CI/CD](https://aws.amazon.com/blogs/devops/complete-ci-cd-with-aws-codecommit-aws-codebuild-aws-codedeploy-and-aws-codepipeline/ "https://aws.amazon.com/blogs/devops/complete-ci-cd-with-aws-codecommit-aws-codebuild-aws-codedeploy-and-aws-codepipeline/") to automatically update AMIs, container images, and other artifacts related to your cloud application. + You can use tools such as [AWS Systems Manager Patch Manager](../../../systems-manager/latest/userguide/systems-manager-patch.md "../../../systems-manager/latest/userguide/systems-manager-patch.md") to automate the process of system updates, and schedule the activity using [AWS Systems Manager Maintenance Windows](../../../systems-manager/latest/userguide/systems-manager-maintenance.md "../../../systems-manager/latest/userguide/systems-manager-maintenance.md"). ## Resources **Related documents:** <br>• [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture") <br>• [What's New with AWS](https://aws.amazon.com/new/?ref=wellarchitected&ref=wellarchitected "https://aws.amazon.com/new/?ref=wellarchitected&ref=wellarchitected") <br>• [AWS Developer Tools](https://aws.amazon.com/products/developer-tools/ "https://aws.amazon.com/products/developer-tools/") **Related videos:** <br>• [AWS re:Invent 2022 - Optimize your AWS workloads with best-practice guidance](https://www.youtube.com/watch?v=t8yl1TrnuIk "https://www.youtube.com/watch?v=t8yl1TrnuIk") <br>• [All Things Patch: AWS Systems Manager](https://www.youtube.com/watch?v=PhIiVsCEBu8 "https://www.youtube.com/watch?v=PhIiVsCEBu8")
