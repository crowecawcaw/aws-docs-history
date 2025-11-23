# OPS06-BP02 Test deployments

Test release procedures in pre-production by using the same deployment configuration, security controls, steps, and procedures as in production. Validate that all deployed steps are completed as expected, such as inspecting files, configurations, and services. Further test all changes with functional, integration, and load tests, along with any monitoring such as health checks. By doing these tests, you can identify deployment issues early with an opportunity to plan and mitigate them prior to production.

You can create temporary parallel environments for testing every change. Automate the deployment of the test environments using infrastructure as code (IaC) to help reduce amount of work involved and ensure stability, consistency, and faster feature delivery.

**Desired outcome:** Your organization adopts a test-driven development culture that includes testing deployments. This ensures teams are focused on delivering business value rather than managing releases. Teams are engaged early upon identification of deployment risks to determine the appropriate course of mitigation.

**Common anti-patterns:**

- During production releases, untested deployments cause frequent issues that require troubleshooting and escalation.
- Your release contains infrastructure as code (IaC) that updates existing resources. You are unsure if the IaC runs successfully or causes impact to the resources.
- You deploy a new feature to your application. It doesn't work as intended and there is no visibility until it gets reported by impacted users.
- You update your certificates. You accidentally install the certificates to the wrong components, which goes undetected and impacts website visitors because a secure connection to the website can't be established.

**Benefits of establishing this best
practice:** Extensive testing in pre-production of deployment procedures, and the changes introduced by them, minimizes the potential impact to production caused by the deployments steps. This increases confidence during production release and minimizes operational support without slowing down velocity of the changes being delivered.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Testing your deployment process is as important as testing the changes that result from your deployment. This can be achieved by testing your deployment steps in a pre-production environment that mirrors production as closely as possible. Common issues, such as incomplete or incorrect deployment steps, or misconfigurations, can be caught as a result before going to production. In addition, you can test your recovery steps.

**Customer example**

As part of their continuous integration and continuous delivery (CI/CD) pipeline, AnyCompany Retail performs the defined steps needed to release infrastructure and software updates for its customers in a production-like environment. The pipeline is comprised of pre-checks to detect drift (detecting changes to resources performed outside of your IaC) in resources prior to deployment, as well as validate actions that the IaC takes upon its initiation. It validates deployment steps, like verifying that certain files and configurations are in place and services are in running states and are responding correctly to health checks on local host before re-registering with the load balancer. Additionally, all changes flag a number of automated tests, such as functional, security, regression, integration, and load tests.

### Implementation steps

1. Perform pre-install checks to mirror the pre-production environment to production.
   1. Use [drift detection](../../../AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.md") to detect when resources have been changed outside of CloudFormation.
   2. Use [change sets](../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.md") to validate that the intent of a stack update matches the actions that CloudFormation takes when the change set is initiated.

2. This triggers a manual approval step in [AWS CodePipeline](../../../codepipeline/latest/userguide/approvals.md "../../../codepipeline/latest/userguide/approvals.md") to authorize the deployment to the pre-production environment.
3. Use deployment configurations such as [AWS CodeDeploy AppSpec](../../../codedeploy/latest/userguide/application-specification-files.md "../../../codedeploy/latest/userguide/application-specification-files.md") files to define deployment and validation steps.
4. Where applicable, [integrate AWS CodeDeploy with other AWS services](../../../codedeploy/latest/userguide/integrations-aws.md "../../../codedeploy/latest/userguide/integrations-aws.md") or [integrate AWS CodeDeploy with partner product and services](../../../codedeploy/latest/userguide/integrations-partners.md "../../../codedeploy/latest/userguide/integrations-partners.md").
5. [Monitor deployments](../../../codedeploy/latest/userguide/monitoring.md "../../../codedeploy/latest/userguide/monitoring.md") using Amazon CloudWatch, AWS CloudTrail, and Amazon SNS event notifications.
6. Perform post-deployment automated testing, including functional, security, regression, integration, and load testing.
7. [Troubleshoot](../../../codedeploy/latest/userguide/troubleshooting.md "../../../codedeploy/latest/userguide/troubleshooting.md") deployment issues.
8. Successful validation of preceding steps should initiate a manual approval workflow to authorize deployment to production.

**Level of effort for the implementation plan:** High

## Resources

**Related best practices:**

- [OPS05-BP02 Test and validate changes](ops_dev_integ_test_val_chg.md "ops_dev_integ_test_val_chg.md")

**Related documents:**

- [AWS Builders' Library | Automating safe, hands-off deployments | Test Deployments](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/#Test_deployments_in_pre-production_environments "https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/#Test_deployments_in_pre-production_environments")
- [AWS Whitepaper | Practicing Continuous Integration and Continuous Delivery on AWS](../../../whitepapers/latest/practicing-continuous-integration-continuous-delivery/testing-stages-in-continuous-integration-and-continuous-delivery.md "../../../whitepapers/latest/practicing-continuous-integration-continuous-delivery/testing-stages-in-continuous-integration-and-continuous-delivery.md")
- [The Story of Apollo - Amazon's Deployment Engine](https://www.allthingsdistributed.com/2014/11/apollo-amazon-deployment-engine.html "https://www.allthingsdistributed.com/2014/11/apollo-amazon-deployment-engine.html")
- [How
  to test and debug AWS CodeDeploy locally before you ship your
  code](https://aws.amazon.com/blogs/devops/how-to-test-and-debug-aws-codedeploy-locally-before-you-ship-your-code/ "https://aws.amazon.com/blogs/devops/how-to-test-and-debug-aws-codedeploy-locally-before-you-ship-your-code/")
- [Integrating Network Connectivity Testing with Infrastructure Deployment](https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-network-connectivity-testing-with-infrastructure-deployment/ "https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-network-connectivity-testing-with-infrastructure-deployment/")

**Related videos:**

- [re:Invent 2020 | Testing software and systems at Amazon](https://www.youtube.com/watch?v=o1sc3cK9bMU "https://www.youtube.com/watch?v=o1sc3cK9bMU")

**Related examples:**

- [Tutorial | Deploy and Amazon ECS service with a validation test](../../../codedeploy/latest/userguide/tutorial-ecs-deployment-with-hooks.md "../../../codedeploy/latest/userguide/tutorial-ecs-deployment-with-hooks.md")
