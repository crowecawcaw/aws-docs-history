# Delete a distribution

The following procedure deletes a distribution by using the CloudFront console.
For information about deleting with the CloudFront API, see [DeleteDistribution](../../../cloudfront/latest/APIReference/API_DeleteDistribution.md "../../../cloudfront/latest/APIReference/API_DeleteDistribution.md") in the
_Amazon CloudFront API Reference_.

If you need to delete a distribution with an OAC attached to an S3 bucket, see [Delete a distribution with an OAC
attached to an S3 bucket](private-content-restricting-access-to-s3.md#delete-oac-distribution-s3 "private-content-restricting-access-to-s3.md#delete-oac-distribution-s3") for important details.

###### Warning

- Before you can delete a distribution, you must disable it, which requires
  permission to update the distribution. Once deleted, a distribution cannot
  be recovered.
- If you disable a distribution that has an alternate domain name associated
  with it, CloudFront stops accepting traffic for that domain name (such as
  www.example.com), even if another distribution has an alternate domain name
  with a wildcard (\*) that matches the same domain (such as
  \*.example.com).

Multi-tenant
Before you can delete a multi-tenant distribution, you must first delete all associated distribution tenants from it.

###### To delete a multi-tenant distribution

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the right pane of the CloudFront console, choose the name of the multi-tenant distribution that you want to
   delete.
3. For **Tenants**, select and delete all associated distribution tenants.
4. Choose **Disable** to disable the distribution, and choose
   **Disable distribution** to confirm.
5. Wait until the new timestamp appears
   under the **Last modified** column.
   - It might take a few minutes for CloudFront to propagate your change to all edge locations.

6. Choose **Delete**, **Delete distribution**.

###### To delete a distribution tenant

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Under **SaaS**, choose **Distribution tenants**.
3. Search for the distribution tenant. Use the dropdown menu in the search bar to filter by domain, name, distribution ID, certificate ID, connection group ID, or web ACL ID.
4. Select the distribution tenant to delete.
5. Choose **Delete tenant**, **Delete distribution tenant**.

Standard

###### To delete a standard distribution

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the right pane of the CloudFront console, find the distribution that you want to
   delete.
   - If the **Status** column shows that the distribution is already
     **Disabled**, skip to Step 6.
   - If the **Status** shows **Enabled** but the distribution still shows **Deploying** in the **Last modified** column, wait for deployment to finish before continuing to step 3.

3. In the right pane of the CloudFront console, select the check box for the distribution that
   you want to delete.
4. Choose **Disable** to disable the distribution, and choose
   **Yes, Disable** to confirm. Then choose **Close**.
   - The value of the **Status** column immediately changes to
     **Disabled**.

5. Wait until the new timestamp appears
   under the **Last modified** column.
   - It might take a few minutes for CloudFront to propagate your change to all edge locations.

6. Select the check box for the distribution that you want to delete.
7. Choose **Delete**, **Delete**.
   - If the **Delete** option isn't available, it means that CloudFront is
     still propagating your change to the edge locations. Wait until the new timestamp appears
     under the **Last modified** column, then repeat steps 6-7.
