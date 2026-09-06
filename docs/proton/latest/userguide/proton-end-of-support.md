

End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October 7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure will remain intact. For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# AWS Proton Service Deprecation and Migration Guide
<a name="proton-end-of-support"></a>

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.

## Service Status Until Deprecation
<a name="service-status-until-deprecation"></a>

Until October 7, 2026, existing AWS Proton customers can continue to use the service normally. During this period, AWS will:

1. Provide security patches and critical bug fixes

1. Maintain service availability and performance

1. Continue to offer support through AWS Support channels

1. Not add new features to the service

## Important Migration Information
<a name="important-migration-information"></a>

AWS Proton is primarily a CI/CD tool for deploying infrastructure. When AWS Proton is deprecated, your deployed CloudFormation stacks and the resources they manage will remain intact and continue to function. The deprecation affects only the delivery pipelines and the AWS Proton service itself, not your deployed infrastructure.

## Alternative Solutions
<a name="alternative-solutions"></a>

We've identified several alternatives to AWS Proton that can help you maintain your infrastructure as code and CI/CD capabilities.

### CloudFormation Git Sync
<a name="cloudformation-git-sync"></a>

**Best for:** Teams using CloudFormation who want a GitOps workflow

Git sync enables platform teams to model CloudFormation templates in a git repository that development teams can fork. Developers update parameter files, push changes to their forked repository, and Git sync updates the stack.

#### Key Benefits:
<a name="cloudformation-git-sync-key-benefits"></a>

1. Similar developer experience to AWS Proton

1. Leverages existing CloudFormation knowledge

1. Clear separation between platform and developer teams

#### Limitations:
<a name="cloudformation-git-sync-limitations"></a>

1. No concept of environments

1. No advanced pipeline features

1. Relies on GitHub features that may not be available in other Git providers

Learn more: [Git sync](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/git-sync.html) 

### Harmonix On AWS
<a name="harmonix-on-aws"></a>

**Best for:** Enterprises needing a comprehensive internal developer portal

Harmonix is an AWS Partner solution based on Backstage.io and provides an AWS plugin that allows teams to create templates, environments, and services similar to Proton.

#### Key Benefits:
<a name="harmonix-on-aws-key-benefits"></a>

1. Similar functionality to AWS Proton

1. Built on the popular Backstage framework

1. Complete developer portal experience

#### Limitations:
<a name="harmonix-on-aws-limitations"></a>

1. Not maintained by an AWS service team

1. Reference implementation that may require customization

Learn more: [https://harmonixonaws.io/](https://harmonixonaws.io/) 

### AWS CodePipeline and AWS CodeBuild
<a name="codepipeline-and-codebuild"></a>

**Best for:** Teams needing maximum flexibility and control

Use the AWS foundational CI/CD services to replicate AWS Proton functionality with greater flexibility and control.

#### Key Benefits:
<a name="codepipeline-and-codebuild-key-benefits"></a>

1. Maximum flexibility

1. Deep integration with AWS services

1. Active maintenance and new features

#### Limitations:
<a name="codepipeline-and-codebuild-limitations"></a>

1. Requires more implementation work

1. Less out-of-box developer self-service

#### Learn more:
<a name="codepipeline-and-codebuild-learn-more"></a>

[What is AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)

[What is AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)

### GitHub Actions
<a name="github-actions"></a>

**Best for:** Smaller teams using GitHub who want simplicity

#### >Key Benefits
<a name="github-actions-key-benefits"></a>

1. Easy integration with GitHub repositories

1. Simple setup for GitHub users

1. Large marketplace of reusable actions

#### Limitations:
<a name="github-actions-limitations"></a>

1. Tied to GitHub ecosystem

1. May require more work for platform team controls

#### Learn more:
<a name="github-actions-learn-more"></a>

[GitHub Actions documentation](https://docs.github.com/en/actions)

CI/CD example: [Integrating with GitHub Actions – CI/CD pipeline to deploy a Web App to Amazon EC2](https://aws.amazon.com/blogs/devops/integrating-with-github-actions-ci-cd-pipeline-to-deploy-a-web-app-to-amazon-ec2/)

## Migration Guidance
<a name="migration-guidance"></a>

The migration process depends on your implementation and chosen alternative. General steps:

1. Inventory your Proton resources:

1. Select an alternative solution:

1. Extract your template data:

1. Implement your chosen alternative:

1. Migrate production workloads:

For specific migration assistance, contact AWS Support or your account team.

## FAQs
<a name="faqs"></a>

**Q: Why is AWS discontinuing AWS Proton?** A: We've identified better opportunities to meet customer needs for Infrastructure as Code policy enforcement through other AWS and AWS Partner solutions.

**Q: Will my existing infrastructure continue to function after the deprecation date?** A: Yes. AWS Proton is primarily a CI/CD tool. Your deployed CloudFormation stacks and the resources they manage will remain intact and continue to function. The deprecation affects only the delivery pipelines, not your deployed infrastructure.

**Q: How can I get help with migration?** A: AWS Support can assist with your migration.  Please contact [AWS Support](https://console.aws.amazon.com/support), or you can reach out to your AWS account manager for assistance.  

**Q: Which alternative should I choose?** A: The best alternative depends on your specific use case:

1. For a simple GitOps workflow: CloudFormation Git Sync

1. For enterprises needing a developer portal: Harmonix On AWS

1. For maximum flexibility: AWS CodePipeline and AWS CodeBuild

1. For teams already on GitHub: GitHub Actions

**Q: What happens if I don't migrate by October 7, 2026?** A: You'll no longer be able to access AWS Proton. Your existing infrastructure will continue to function, but you won't be able to use AWS Proton to manage or update it.

**Q: How long will my data be retained?** A: Until October 7, 2026. After this date, all data will be deleted.

If you have additional questions, please contact AWS Support.