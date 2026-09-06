

# Step 7: Deploy test infrastructure
<a name="transform-containers-step-test-deploy"></a>

In this step, AWS Transform deploys test infrastructure so that you can validate your containerized application before production cutover.

## What happens during test deployment
<a name="transform-containers-test-deploy-process"></a>

AWS Transform deploys the infrastructure templates generated in the previous step to your AWS account. For Amazon EKS deployments, this uses Helm. For Amazon ECS deployments, this uses Terraform.

Before deploying, AWS Transform presents an infrastructure values form where you can configure deployment parameters such as resource names, replica counts, and environment-specific settings. AWS Transform also generates a deployment preview that shows what resources will be created, so you can review the changes before approving.

## What you need to do
<a name="transform-containers-test-deploy-user-actions"></a>

**To deploy and validate test infrastructure**

1. Complete the infrastructure values form with your deployment configuration. The form includes parameters such as cluster names, namespaces, replica counts, and other environment-specific settings.

1. Review the deployment preview that shows the resources that will be created or modified.

1. Approve the infrastructure deployment when AWS Transform requests it.

1. Wait for the deployment to complete. AWS Transform displays the deployment results.

1. Test your deployed application to verify that it runs correctly in a container and that the infrastructure meets your requirements.

1. Tell AWS Transform whether you are satisfied with the deployment, or whether you want to modify the infrastructure and redeploy.

## Iterating on the infrastructure
<a name="transform-containers-test-deploy-iterate"></a>

If you need to modify the infrastructure templates, you can upload updated templates and redeploy:

1. Tell AWS Transform you want to modify the IaC.

1. Upload a zip file containing your modified infrastructure templates.

1. AWS Transform replaces the templates and performs an incremental update (Terraform apply or Helm upgrade).

1. Review the updated deployment results.

You can repeat this cycle until you are satisfied with the deployment.

## Session recovery
<a name="transform-containers-test-deploy-recovery"></a>

Infrastructure deployments run asynchronously using . If your session is interrupted during a deployment, AWS Transform automatically recovers the operation when you reconnect and displays the deployment results.