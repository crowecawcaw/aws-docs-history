# SUS02-BP03 Stop the creation and maintenance of unused

assets

Decommission unused assets in your workload to reduce
the number of cloud resources required to support your
demand and minimize waste.

**Common anti-patterns:**

- You do not analyze your application for assets that are redundant or no longer required.
- You do not remove assets that are redundant or no longer required.

**Benefits of establishing this best practice:** Removing
unused assets frees resources and improves the overall efficiency of the workload.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Unused assets consume cloud resources like storage space and compute power. By identifying and eliminating these assets, you can free up these resources, resulting in a more efficient cloud architecture. Perform regular analysis on application assets such as pre-compiled reports, datasets, static images, and asset access patterns to identify redundancy, underutilization, and potential decommission targets. Remove those redundant assets to reduce the resource waste in your workload.

### Implementation steps

- **Conduct an inventory:** Conduct a comprehensive inventory to identify all assets within your workload.
- **Analyze usage:** Use continuous monitoring to identify static assets that are no longer required.
- **Remove unused assets:** Develop a plan to remove assets that are no longer required.
  - Before removing any asset, evaluate the impact of removing it on the architecture.
  - Consolidate overlapping generated assets to remove redundant processing.
  - Update your applications to no longer produce and store assets that are not required.

- **Communicate with third parties:** Instruct third parties to stop producing and storing assets managed on your behalf that are no longer required. Ask to consolidate redundant assets.
- **Use lifecycle policies:** Use lifecycle policies to automatically delete unused assets.
  - You can use [Amazon S3 Lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") to manage your objects throughout their lifecycle.
  - You can use [Amazon Data Lifecycle Manager](../../../ebs/latest/userguide/snapshot-lifecycle.md "../../../ebs/latest/userguide/snapshot-lifecycle.md") to automate the creation, retention, and deletion of Amazon EBS snapshots and Amazon EBS-backed AMIs.

- **Review and optimize:** Regularly review your workload to identify and remove any unused assets.

## Resources

**Related documents:**

- [Optimizing
  your AWS Infrastructure for Sustainability, Part II:
  Storage](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage/ "https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage/")
- [How do I terminate active resources that I no longer need on my AWS account?](https://aws.amazon.com/premiumsupport/knowledge-center/terminate-resources-account-closure/ "https://aws.amazon.com/premiumsupport/knowledge-center/terminate-resources-account-closure/")

**Related videos:**

- [AWS re:Invent 2023 - Sustainable architecture: Past, present, and future](https://www.youtube.com/watch?v=2xpUQ-Q4QcM "https://www.youtube.com/watch?v=2xpUQ-Q4QcM")
- [AWS re:Invent 2022 - Preserving and maximizing the value of digital media assets using Amazon S3](https://www.youtube.com/watch?v=8OI0Uu-YvD8 "https://www.youtube.com/watch?v=8OI0Uu-YvD8")
- [AWS re:Invent 2023 - Optimize costs in your multi-account environments](https://www.youtube.com/watch?v=ie_Mqb-eC4A "https://www.youtube.com/watch?v=ie_Mqb-eC4A")
