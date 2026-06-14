# Prerequisites for SageMaker Profiler

The following list shows the prerequisites to start using SageMaker Profiler.

- A SageMaker AI domain set up with Amazon VPC in your AWS account.

For instructions on setting up a domain, see [Onboard to Amazon SageMaker AI
domain using quick setup](onboard-quick-start.md "onboard-quick-start.md"). You also need to add domain user
profiles for individual users to access the Profiler UI application. For
more information, see [Add user profiles](domain-user-profile-add.md "domain-user-profile-add.md").

- Amazon EFS must be enabled on your domain. Profiler requires an Amazon EFS file
  system to function. For domains created through quick setup after June 1, 2026,
  EFS is not created by default during domain creation. To enable EFS after domain
  creation, see [Amazon EFS creation and
  auto-mounting in Amazon SageMaker Studio](studio-updated-automount.md "studio-updated-automount.md").
- The following list is the minimum set of permissions for using the
  Profiler UI application.

  - `sagemaker:CreateApp`
  - `sagemaker:DeleteApp`
  - `sagemaker:DescribeTrainingJob`
  - `sagemaker:Search`
  - `s3:GetObject`
  - `s3:ListBucket`
