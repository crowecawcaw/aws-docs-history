

# Release: Elastic Beanstalk GitHub Action for automated deployments on February 11, 2026
<a name="release-2026-02-11-github-action"></a>

AWS Elastic Beanstalk announces the Elastic Beanstalk Deploy GitHub Action, enabling automated application deployments to Elastic Beanstalk directly from GitHub Actions workflows.

**Release date:** February 11, 2026

## Changes
<a name="release-2026-02-11-github-action.changes"></a>

Elastic Beanstalk now offers the Elastic Beanstalk Deploy GitHub Action, which you can use to automate deployments to Elastic Beanstalk environments as part of your CI/CD pipeline. The action automatically creates Elastic Beanstalk applications and environments if they don't already exist, and handles deployment package management, Amazon S3 artifact uploads, and version management.

Key features include:
+ **Automated deployments** – Deploy applications to Elastic Beanstalk environments with a single action in your GitHub Actions workflow.
+ **Environment creation** – Automatically create Elastic Beanstalk applications and environments if they don't already exist.
+ **Health monitoring** – Track real-time deployment events and environment health status directly in your GitHub Actions logs.
+ **Deployment package management** – Automatically create deployment packages from your repository or use pre-built packages (.zip, .war, .jar).

This GitHub Action can be used with Elastic Beanstalk in all AWS Regions where the service is available.

For more information, see the [Elastic Beanstalk Deploy GitHub Action](https://github.com/aws-actions/aws-elasticbeanstalk-deploy) on GitHub.