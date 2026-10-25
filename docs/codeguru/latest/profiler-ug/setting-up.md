

# Setting up CodeGuru Profiler
<a name="setting-up"></a>

An Amazon CodeGuru Profiler proﬁling group is a group of applications for which data is meant to be aggregated and analyzed together. To create a proﬁling group, sign in to the AWS Management Console and set permissions for the CodeGuru Profiler proﬁling agent.

The proﬁling agent collects runtime data from your applications. Data that the agent collects is analyzed to provide flame graphs and hourly reports with recommendations for how you can optimize your applications.

You can create a profiling group using your own application or the demo application. For more information about using the demo application, see [Getting started with CodeGuru Profiler](getting-started.md).

Before you can start using CodeGuru Profiler, you must complete setup. If your application runs on AWS Lambda, then you can enable profiling from the Lambda console. If your application runs on a platform other than Lambda, then you can complete the setup process in the CodeGuru Profiler console.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Set up in the Lambda console](setting-up-short.md)
+ [Set up in the CodeGuru Profiler console](setting-up-long.md)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. There are two ways to sign up for AWS. If you want complete control over account configuration and where your content is stored, or if you have regulated workloads such as HIPAA or FedRAMP, use [Sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html). If you are a new user and want to use a login you already own to sign in to AWS and create an AWS environment with preconfigured defaults in select [AWS Regions](https://docs.aws.amazon.com/accounts/latest/reference/project-regions.html), use [Sign up for AWS](https://docs.aws.amazon.com/accounts/latest/reference/sign-in-new.html).