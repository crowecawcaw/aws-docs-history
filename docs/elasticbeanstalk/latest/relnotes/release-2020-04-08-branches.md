

# Release: Elastic Beanstalk formally supports platform branches on April 8, 2020
<a name="release-2020-04-08-branches"></a>

AWS Elastic Beanstalk made API and console changes to formally add the concept of platform branches. A platform branch has a support lifecycle and consistes of successive platform version updates.

**Release date:** April 8, 2020

## Changes
<a name="release-2020-04-08-branches.changes"></a>

Today we added formal support to the concept of *platform branches*. When you create or update an Elastic Beanstalk environment and select a platform version, you now see a hierarchy of three levels: a platform (for example, **Tomcat**), a platform branch (for example, **Tomcat 8.5 with Java 8 running on 64bit Amazon Linux**), and a platform version (for example, **3.3.2**).

We also made some API changes. We added a new API action, [ListPlatformBranches](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListPlatformBranches.html). You can use this action to query Elastic Beanstalk for available platform branches. The action provides several filtering criteria to help you narrow down your query. And we extended [ListPlatformVersions](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListPlatformVersions.html) and [DescribePlatformVersion](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribePlatformVersion.html) to provide platform branch and platform version lifecycle information.

## Background
<a name="release-2020-04-08-branches.bg"></a>

Elastic Beanstalk supports multiple platforms that you can use to build your applications. A platform is a combination of an operating system (OS), runtime, web server, application server, and Elastic Beanstalk components. Each platform has multiple platform versions—combinations of specific component versions. You deploy your application code to a specific platform version.

A *platform branch* is a line of successive platform versions sharing specific (typically major) versions of some of their components, such as the operating system (OS), runtime, or Elastic Beanstalk components. An Elastic Beanstalk platform may support several concurrent platform branches. When we release platform updates, we provide a new platform version for each platform branch. A platform branch has a support lifecycle—it can be in beta, a regular supported branch, or a retiring (deprecated) branch.

For definitions of platform branch and other platform-related terms, see [Elastic Beanstalk Platforms Glossary](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-glossary.html) in the *AWS Elastic Beanstalk Developer Guide*.