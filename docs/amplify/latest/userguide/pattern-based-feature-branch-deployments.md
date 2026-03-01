# Pattern-based feature branch deployments

Pattern-based branch deployments allow you to automatically deploy branches that match a
specific pattern to Amplify. Product teams using feature branch or GitFlow workflows for
their releases, can now define patterns such as `release**` to automatically deploy Git
branches that begin with ‘release’ to a shareable URL.

1. Choose **App settings**, then **Branch settings**.
2. On the **Branch settings** page, choose **Edit**.
3. Select **Branch autodetection** to automatically connect branches to Amplify that match a pattern set.
4. In the **Branch autodetection - patterns** box, enter the patterns for automatically deploying branches.
   - `*` – Deploys all branches
     in your repository.
   - `release*` – Deploys all
     branches that begin with the word ‘release'.
   - `release*/` – Deploys all
     branches that match a ‘release /’ pattern.
   - Specify multiple patterns in a comma-separated list. For example,
     `release*, feature*`.

5. Set up automatic password protection for all branches that are automatically
   created by selecting **Branch autodetection access
   control** .
6. For Gen 1 applications built with an Amplify backend, you can choose to create a
   new environment for every connected branch, or point all branches to an existing
   backend.
7. Choose **Save**.

## Pattern-based feature branch deployments for an app connected to a custom domain

You can use pattern-based feature branch deployments for an app connected to an
Amazon Route 53 custom domain.

- For instructions on setting up pattern-based feature branch deployments, see
  [Setting up automatic subdomains for an Amazon Route 53 custom domain](to-set-up-automatic-subdomains-for-a-Route-53-custom-domain.md "to-set-up-automatic-subdomains-for-a-Route-53-custom-domain.md")
- For instructions on connecting an Amplify app to a custom domain managed in
  Route 53, see [Adding a custom domain managed by Amazon Route 53](to-add-a-custom-domain-managed-by-amazon-route-53.md "to-add-a-custom-domain-managed-by-amazon-route-53.md")
- For more information about using Route 53, see [What is Amazon Route
  53](../../../Route53/latest/DeveloperGuide/Welcome.md "../../../Route53/latest/DeveloperGuide/Welcome.md").
