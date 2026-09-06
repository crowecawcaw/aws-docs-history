

# Pattern-based feature branch deployments
<a name="pattern-based-feature-branch-deployments"></a>

Pattern-based branch deployments allow you to automatically deploy branches that match a specific pattern to Amplify. Product teams using feature branch or GitFlow workflows for their releases, can now define patterns such as **release\*\*** to automatically deploy Git branches that begin with ‘release’ to a shareable URL.

1. Choose **App settings**, then **Branch settings**.

1. On the **Branch settings** page, choose **Edit**.

1. Select **Branch autodetection** to automatically connect branches to Amplify that match a pattern set.

1. In the **Branch autodetection - patterns** box, enter the patterns for automatically deploying branches.
   + **\*** – Deploys all branches in your repository.
   + **release\*** – Deploys all branches that begin with the word ‘release'.
   + **release\*/** – Deploys all branches that match a ‘release /’ pattern.
   + Specify multiple patterns in a comma-separated list. For example, **release\*, feature\***.

1. Set up automatic password protection for all branches that are automatically created by selecting **Branch autodetection access control** .

1. For Gen 1 applications built with an Amplify backend, you can choose to create a new environment for every connected branch, or point all branches to an existing backend.

1. Choose **Save**.

## Pattern-based feature branch deployments for an app connected to a custom domain
<a name="pattern-based-feature-branch-deployments-for-an-app-connected-to-a-custom-domain"></a>

You can use pattern-based feature branch deployments for an app connected to an Amazon Route 53 custom domain. 
+ For instructions on setting up pattern-based feature branch deployments, see [Setting up automatic subdomains for an Amazon Route 53 custom domain](to-set-up-automatic-subdomains-for-a-Route-53-custom-domain.md)
+ For instructions on connecting an Amplify app to a custom domain managed in Route 53, see [Adding a custom domain managed by Amazon Route 53](to-add-a-custom-domain-managed-by-amazon-route-53.md)
+ For more information about using Route 53, see [What is Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html).