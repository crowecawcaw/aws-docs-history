

# Disabling trusted access for S3 Storage Lens
<a name="storage_lens_with_organizations_disabling_trusted_access"></a>

Removing an account as a delegated administrator or disabling trusted access limits the account owner's S3 Storage Lens dashboard metrics to work only on an account level. Each account holder is then only be able to see the benefits of S3 Storage Lens through the limited scope of their account, and not their entire organization.

When you disable trusted access in S3 Storage Lens, any dashboards requiring trusted access are no longer updated. Any organizational dashboards that are created are also no longer updated. Instead, you're only able to query [historic data for the S3 Storage Lens dashboard](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_basics_metrics_recommendations.html#storage_lens_basics_data_queries), while the data is still available.

**Note**  
Disabling trusted access for S3 Storage Lens also automatically stops all organization-level dashboards from collecting and aggregating storage metrics. This is because S3 Storage Lens no longer has trusted access to the organization accounts.
Your management and delegate administrator accounts can still see the historic data for any disabled dashboards. They can also query this historic data while it is still available. 