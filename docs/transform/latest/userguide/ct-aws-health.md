

# Upgrading resources in AWS Health planned lifecycle events

AWS Health tells you about planned lifecycle events for the resources in your AWS account. Examples are an AWS Lambda runtime deprecation or the end of standard support for an Amazon Elastic Kubernetes Service (Amazon EKS) Kubernetes version. The `aws-health-readiness` analysis finds where your infrastructure code sets these versions, so that you can upgrade them before the deadline.

Each finding names the version, the file and line that set it, its lifecycle dates, and a recommended version. It also names the AWS managed transformation that can upgrade it. When the analysis can read AWS Health in your account, the finding also lists your affected resources that appear in the repository.

## What the analysis checks
<a name="ct-aws-health-coverage"></a>

The analysis checks the following versions. Each one links to the AWS managed transformation that upgrades it.


| Resource and version | Transformation | 
| --- | --- | 
| Lambda Node.js runtimes | AWS/lambda-nodejs-runtime-upgrade | 
| Lambda Python runtimes | AWS/python-version-upgrade | 
| Lambda Ruby runtimes | AWS/ruby-upgrade | 
| Lambda .NET runtimes | AWS/dotnet-lambda-upgrade | 
| Lambda Java runtimes | AWS/java-version-upgrade | 
| Amazon EKS Kubernetes versions of clusters and node groups | AWS/eks-kubernetes-version-upgrade | 
| AWS Elastic Beanstalk PHP platform branches | AWS/php-version-upgrade | 

The analysis reads these versions from infrastructure as code, such as Terraform, AWS CloudFormation, the AWS CDK, Pulumi, and `eksctl`. It also reads the EB CLI configuration and scripts that call the AWS CLI or the EB CLI. When a version is set by reference, such as a Terraform variable or an AWS CloudFormation parameter, the AWS Transform agent follows the reference to its value.

A repository can have Lambda handler code but no infrastructure code. In that case, the analysis reports the language version that the project pins, for example in `.nvmrc` or `pyproject.toml`. The titles of these findings end with *(likely, from code)*.

**Note**  
The analysis doesn't check other planned lifecycle events. For example, it doesn't check Amazon RDS, Amazon Aurora, or Amazon ElastiCache engine versions, OS-only Lambda runtimes, or Elastic Beanstalk platforms other than PHP.

## How the analysis decides what needs action
<a name="ct-aws-health-decision"></a>

A version needs action when it is deprecated or retired, or when its next lifecycle date is within 180 days. Other versions are listed as checked and fine. Versions with no lifecycle date yet, and preview runtimes, are also listed as fine.

The lifecycle dates come from the following public AWS pages. Each report shows the day that the dates were last checked.
+ Lambda: [Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html)
+ Amazon EKS: [Understand the Kubernetes version lifecycle on EKS](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html)
+ Elastic Beanstalk: [Elastic Beanstalk platform release schedule](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-schedule.html)

The recommended version is a supported version with more than 180 days to its next lifecycle date. For Lambda and Elastic Beanstalk, it runs on Amazon Linux 2023. For Amazon EKS, the finding tells you to upgrade one minor version at a time.

Findings come from your code, not from AWS Health. A resource that AWS Health lists doesn't get a finding unless a repository sets its version.

Each run writes a report, `aws-health-lifecycle-analysis/REPORT.md`. It lists the versions that need action, the versions that are fine, and notes about the run. Its first line is `Status: COMPLETE`, or `Status: PARTIAL` when a version isn't in the lifecycle tables or a reference couldn't be followed.

## Starting from the AWS Health console
<a name="ct-aws-health-start"></a>

You can open continuous modernization from the AWS Health Dashboard and set up the analysis in a few steps.

Before you start, make sure that you can use the AWS Transform console and web application. The first time, setting up AWS Transform in your account needs permissions to create its profile. For more information, see [Setting up AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/transform-setup.html).

1. Open your [AWS Health Dashboard](https://health.aws.amazon.com/health/home).

1. On the continuous modernization banner, choose **Upgrade with Continuous Modernization**. The AWS Transform console opens in a new tab for the account that you're signed in to.

1. (First time only) On the **Enable web application** page, choose **Quick start**, and then choose **Enable**. This sets up AWS Transform in US East (N. Virginia). If the console says that setup is taking longer than expected, open the link from AWS Health again in a few minutes.

1. (First time only) On the **Turn on IAM access to continue** page, choose **Turn on and continue**. If the console says that AWS Transform isn't ready in this Region, check your profile on the **Settings** page, and then open the link again.

1. On the **Get started** page of the web application, review the planned lifecycle events from AWS Health.

1. On the same page, choose the upgrade button, for example **Upgrade 3 functions**. If the page lists no events, choose **Set up continuous modernization**.

1. On the **Set up continuous modernization** page, under **Connect your repositories**, choose a connected source, or connect GitHub, GitLab, or Bitbucket.

1. Under **Keep them continuously modern**, for **Resolve AWS Health notices**, choose how often the analysis runs. The default is **Weekly**. Choose **Once** to run it one time.

   The same section also sets up other analyses for your repositories, such as technical debt and modernization readiness. Review their settings, or turn them off, before you continue.

1. (Optional) Under **Additional settings**, for **Where it runs**, choose **AWS managed** or **Customer owned**.

1. At the bottom of the page, choose **Begin continuous analysis**. The analyses start, and they can take several minutes or longer to finish. You can follow them on the **Analyses** tab.

**Note**  
The **Get started** page reads AWS Health with your sign-in credentials. It lists every planned lifecycle event in your account, including events that the analysis doesn't check. If the page can't read AWS Health, it doesn't list events, and you can still set up the analysis.

If you're signed in to a different account or Region in the AWS Transform console, the console asks you to switch before it opens the link.

## Running the analysis
<a name="ct-aws-health-run"></a>

You can also run the analysis like any other analysis type. In the web application, open the **Analyses** tab, and for **Analysis type**, choose **AWS Health readiness**. With the AWS Transform CLI, use `--type aws-health-readiness`:

```bash
atx ct analysis run --type aws-health-readiness --source {{name}} [--repo {{source}}::{{repo}}] [--wait]
```

The analysis runs on every compute option, and you can schedule it. For more information, see [Remote execution](ct-working-with.md#ct-remote-execution) and [Scheduling recurring analysis](ct-working-with.md#ct-scheduling).

## Permissions and AWS Support plan
<a name="ct-aws-health-permissions"></a>

Reading AWS Health is optional. Without it, the analysis gives the same findings, but the findings don't name your affected resources.

To read AWS Health, the analysis needs the following permissions. AWS Health actions don't support resource-level permissions, so the resource is `*`.

```json
{
  "Version": "2012-10-17", 		 	 	 
  "Statement": [
    {
      "Sid": "AwsHealthRead",
      "Effect": "Allow",
      "Action": [
        "health:DescribeEvents",
        "health:DescribeEventDetails",
        "health:DescribeAffectedEntities"
      ],
      "Resource": "*"
    }
  ]
}
```

The analysis reads AWS Health with the credentials that run it:
+ On your local machine, it uses your AWS credentials.
+ On AWS Batch or Amazon EC2, it uses the job role of the stack. Add the permissions to the role if they're missing.
+ On AWS Transform-managed infrastructure, it uses the execution role. For a schedule, see [Execution role for AWS Transform-managed schedules](ct-working-with.md#ct-schedule-execution-role). The web application warns you when the role can't read AWS Health.

The AWS Health API requires an AWS Support plan that includes it, such as Business Support or Enterprise Support. Without one, the analysis continues without AWS Health. For more information, see [Accessing the AWS Health API](https://docs.aws.amazon.com/health/latest/ug/health-api.html) in the *AWS Health User Guide*.

The analysis reads only the events of your own account, not the organizational view. It calls the AWS Health API in US East (N. Virginia).

## Reviewing and remediating findings
<a name="ct-aws-health-findings"></a>

Findings appear on the **Findings** tab with severity `high`. Their category is `runtime-lifecycle` for Lambda and `platform-lifecycle` for Amazon EKS and Elastic Beanstalk.

The following is an example finding title:

```
AWS Lambda runtime python3.9 deprecated, function create blocked 2027-07-29
```

To fix a finding, create a remediation. Remediation runs on a deployed AWS Batch or Amazon EC2 stack. For more information, see [Creating remediations](ct-working-with.md#ct-creating-remediations).

**Important**  
`AWS/php-version-upgrade` upgrades your application code. It doesn't change your Elastic Beanstalk environment. After the upgrade, set the environment's solution stack name or platform ARN to the new platform branch.

**Note**  
`AWS/eks-kubernetes-version-upgrade` changes infrastructure code only. It never changes a running cluster. Apply the updated code to upgrade the cluster.

A transformation might upgrade to a version other than the one that the finding recommends. Check the version in the pull request before you merge it.