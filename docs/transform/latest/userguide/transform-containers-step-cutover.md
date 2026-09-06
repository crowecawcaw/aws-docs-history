

# Step 9: Deploy cutover infrastructure
<a name="transform-containers-step-cutover"></a>

In this final step, AWS Transform deploys the finalized infrastructure for production use. The cutover deployment uses the same infrastructure templates that you validated during the test deployment step.

## What you need to do
<a name="transform-containers-cutover-user-actions"></a>

**To deploy cutover infrastructure**

1. Complete the infrastructure values form with your production deployment configuration. You can adjust parameters from the test deployment or use the same values.

1. Review the deployment preview that shows the production resources that will be created.

1. Approve the production deployment when AWS Transform requests it.

1. Wait for the deployment to complete. AWS Transform displays the cutover deployment results.

1. Verify that your application is running correctly in the production environment.

**Important**  
Review the generated infrastructure configurations with your team to ensure that they meet your organization's security, compliance, and business requirements. While AWS Transform provides automated configuration recommendations, you are responsible for validating and adjusting the settings to match your needs before proceeding with the cutover deployment.

## Session recovery
<a name="transform-containers-cutover-recovery"></a>

Production deployments run asynchronously using . If your session is interrupted during deployment, AWS Transform automatically recovers the operation when you reconnect and displays the deployment results.