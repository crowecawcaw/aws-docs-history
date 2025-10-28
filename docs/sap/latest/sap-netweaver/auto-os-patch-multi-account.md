# Considerations for multiple accounts

When you run SAP workloads in AWS, you must consider an AWS account strategy that meets the security controls of your organization. For example, you might separate SAP from non-SAP workloads and separate production from non-production environments. AWS Systems Manager does not support multi-account patching.

In every AWS account with SAP workloads, patch baselines should be created and patch execution should be performed to ensure that patching is applied to all SAP systems. In a multi-account environment, this should also follow the SAP best practice of patching in the development account, then test, and finally in the production AWS account.
