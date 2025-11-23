# REL07-BP01 Use automation when obtaining or scaling

resources

A cornerstone of reliability in the cloud is the programmatic
definition, provisioning, and management of your infrastructure and
resources. Automation helps you streamline resource provisioning,
facilitate consistent and secure deployments, and scale resources
across your entire infrastructure.

**Desired outcome**: You manage your
infrastructure as code (IaC). You define and maintain your
infrastructure code in version control systems (VCS). You delegate
provisioning AWS resources to automated mechanisms and leverage
managed services like Application Load Balancer (ALB), Network Load
Balancer (NLB), and Auto Scaling groups. You provision your
resources using continuous integration/continuous delivery (CI/CD)
pipelines so that code changes automatically initiate resource
updates, including updates to your Auto Scaling configurations.

**Common anti-patterns**:

- You deploy resources manually using the command line or at the
  AWS Management Console (also known as _click-ops_).
- You tightly couple your application components or resources, and
  create inflexible architectures as a result.
- You implement inflexible scaling policies that do not adapt to
  changing business requirements, traffic patterns, or new
  resource types.
- You manually estimate capacity to meet anticipated demand.

**Benefits of establishing this best
practice**: Infrastructure as code (IaC) allows
infrastructure to be defined programmatically. This helps you manage
infrastructure changes through the same software development
lifecycle as application changes, which promotes consistency and
repeatability and reduces the risk of manual, error-prone tasks. You
can further streamline the process of provisioning and updating
resources through implementing IaC with automated delivery
pipelines. You can deploy infrastructure updates reliably and
efficiently without the need for manual intervention. This agility
is particularly important when scaling resources to meet fluctuating
demands.

You can achieve dynamic, automated resource scaling in conjunction
with IaC and delivery pipelines. By monitoring key metrics and
applying predefined scaling policies, Auto Scaling can automatically
provision or deprovision resources as needed, which improves
performance and cost-efficiency. This reduces the potential for
manual errors or delays in response to changes in application or
workload requirements.

The combination of IaC, automated delivery pipelines, and Auto
Scaling helps organizations provision, update, and scale their
environments with confidence. This automation is essential to
maintain a responsive, resilient, and efficiently-managed cloud
infrastructure.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

To set up automation with CI/CD pipelines and infrastructure as
code (IaC) for your AWS architecture, choose a version control
system such as Git to store your IaC templates and configuration.
These templates can be written using tools such as
[AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/"). To start, define your infrastructure
components (such as AWS VPCs, Amazon EC2 Auto Scaling Groups, and
Amazon RDS databases) within these templates.

Next, integrate these IaC templates with a CI/CD pipeline to
automate the deployment process.
[AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/") provides a seamless AWS-native solution, or
you can use other third-party CI/CD solutions. Create a pipeline
that activates when changes occur to your version control
repository. Configure the pipeline to include stages that lint and
validate your IaC templates, deploy the infrastructure to a
staging environment, run automated tests, and finally, deploy to
production. Incorporate approval steps where necessary to maintain
control over changes. This automated pipeline not only speeds up
deployment but also facilitates consistency and reliability across
environments.

Configure Auto Scaling of resources such as Amazon EC2 instances,
Amazon ECS tasks, and database replicas in your IaC to provide
automatic scale-out and scale-in as needed. This approach enhances
application availability and performance and optimizes cost by
dynamically adjusting resources based on demand. For a list of
supported resources, see
[Amazon EC2 Auto Scaling](../../../autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.md "../../../autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.md") and
[AWS Auto Scaling](../../../autoscaling/application/userguide/what-is-application-auto-scaling.md "../../../autoscaling/application/userguide/what-is-application-auto-scaling.md").

### Implementation steps

1. Create and use a source code repository to store the code
   that controls your infrastructure configuration. Commit
   changes to this repository to reflect any ongoing changes
   you want to make.
2. Select an infrastructure as code solution such as AWS CloudFormation to keep your infrastructure up to date and
   detect inconsistency (drift) from your intended state.
3. Integrate your IaC platform with your CI/CD pipeline to
   automate deployments.
4. Determine and collect the appropriate metrics for automatic
   scaling of resources.
5. Configure automatic scaling of resources using scale-out and
   scale-in policies appropriate for your workload components.
   Consider using scheduled scaling for predictable usage
   patterns.
6. Monitor deployments to detect failures and regressions.
   Implement rollback mechanisms within your CI/CD platform to
   revert changes if necessary.

## Resources

**Related documents:**

- [AWS Auto Scaling: How Scaling Plans Work](../../../autoscaling/plans/userguide/how-it-works.md "../../../autoscaling/plans/userguide/how-it-works.md")
- [AWS Marketplace: products that can be used with auto
  scaling](https://aws.amazon.com/marketplace/search/results?searchTerms=Auto+Scaling "https://aws.amazon.com/marketplace/search/results?searchTerms=Auto+Scaling")
- [Managing
  Throughput Capacity Automatically with DynamoDB Auto
  Scaling](../../../amazondynamodb/latest/developerguide/AutoScaling.md "../../../amazondynamodb/latest/developerguide/AutoScaling.md")
- [Using
  a load balancer with an Auto Scaling group](../../../autoscaling/ec2/userguide/autoscaling-load-balancer.md "../../../autoscaling/ec2/userguide/autoscaling-load-balancer.md")
- [What
  Is AWS Global Accelerator?](../../../global-accelerator/latest/dg/what-is-global-accelerator.md "../../../global-accelerator/latest/dg/what-is-global-accelerator.md")
- [What
  Is Amazon EC2 Auto Scaling?](../../../autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.md "../../../autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.md")
- [What
  is AWS Auto Scaling?](../../../autoscaling/plans/userguide/what-is-aws-auto-scaling.md "../../../autoscaling/plans/userguide/what-is-aws-auto-scaling.md")
- [What
  is Amazon CloudFront?](../../../AmazonCloudFront/latest/DeveloperGuide/Introduction.md "../../../AmazonCloudFront/latest/DeveloperGuide/Introduction.md")
- [What
  is Amazon Route 53?](../../../Route53/latest/DeveloperGuide/Welcome.md "../../../Route53/latest/DeveloperGuide/Welcome.md")
- [What
  is ELB?](../../../elasticloadbalancing/latest/userguide/what-is-load-balancing.md "../../../elasticloadbalancing/latest/userguide/what-is-load-balancing.md")
- [What
  is a Network Load Balancer?](../../../elasticloadbalancing/latest/network/introduction.md "../../../elasticloadbalancing/latest/network/introduction.md")
- [What
  is an Application Load Balancer?](../../../elasticloadbalancing/latest/application/introduction.md "../../../elasticloadbalancing/latest/application/introduction.md")
- [Integrating
  Jenkins with AWS CodeBuild and AWS CodeDeploy](https://aws.amazon.com/blogs/devops/setting-up-a-ci-cd-pipeline-by-integrating-jenkins-with-aws-codebuild-and-aws-codedeploy/ "https://aws.amazon.com/blogs/devops/setting-up-a-ci-cd-pipeline-by-integrating-jenkins-with-aws-codebuild-and-aws-codedeploy/")
- [Creating
  a four stage pipeline with AWS CodePipeline](../../../codepipeline/latest/userguide/tutorials-four-stage-pipeline.md "../../../codepipeline/latest/userguide/tutorials-four-stage-pipeline.md")

**Related videos:**

- [Back
  to Basics: Deploy Your Code to Amazon EC2](https://www.youtube.com/watch?v=f2wvEQ_sWS8 "https://www.youtube.com/watch?v=f2wvEQ_sWS8")
- [AWS Supports You | Starting Your Infrastructure as Code Solution Using
  AWS CloudFormation Templates](https://www.youtube.com/watch?v=bgfx76jr7tA "https://www.youtube.com/watch?v=bgfx76jr7tA")
- [Streamline
  Your Software Release Process Using AWS CodePipeline](https://www.youtube.com/watch?v=zMa5gTLrzmQ "https://www.youtube.com/watch?v=zMa5gTLrzmQ")
- [Monitor
  AWS Resources Using Amazon CloudWatch Dashboards](https://www.youtube.com/watch?v=I7EFLChc07M "https://www.youtube.com/watch?v=I7EFLChc07M")
- [Create
  Cross Account & Cross Region CloudWatch Dashboards | Amazon Web Services](https://www.youtube.com/watch?v=eIUZdaqColg "https://www.youtube.com/watch?v=eIUZdaqColg")
