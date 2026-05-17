# Step 8: Clean up test infrastructure

After you complete validation, AWS Transform tears down the test infrastructure to avoid
unnecessary costs.

## What you need to do

###### To clean up test infrastructure

1. AWS Transform informs you that the test infrastructure will be torn down.
2. Approve the destroy operation when AWS Transform requests it.
3. Wait for the cleanup to complete. AWS Transform displays the results when
   all test resources have been removed.

For Amazon ECS deployments, this step removes all resources that were created during
the test deployment, including compute resources, load balancers, storage, and
networking components.

For Amazon EKS deployments, the cleanup is scoped by label to your specific project.
Only resources tagged for this containerization workflow are removed. Other
workloads running on the same Amazon EKS cluster are not affected.
