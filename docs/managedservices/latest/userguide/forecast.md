# Use AMS SSP to provision Amazon Forecast in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Forecast (Forecast) capabilities directly in your AMS managed account. Amazon Forecast is a fully managed service that
uses machine learning to deliver highly accurate forecasts.

###### Note

AWS has closed new customer access to Amazon Forecast, effective July 29, 2024. Amazon Forecast existing customers can continue to use the service as normal.
AWS continues to invest in security, availability, and performance improvements for Amazon Forecast, but AWS does not plan to introduce new features.

If you want to use Amazon Forecast, reach out to your CSDM so that they can guide you further regarding how to
[Transition your Amazon Forecast usage to Amazon SageMaker Canvas](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/").

Based on the same technology used at Amazon.com, Forecast uses machine learning to combine time
series data with additional variables to build forecasts. Forecast requires no machine learning experience
to get started. You only need to provide historical data, plus any additional data that you believe may impact
your forecasts. For example, the demand for a particular color of a shirt may change with the seasons and store
location. This complex relationship is hard to determine on its own, but machine learning is ideally suited to
recognize it. Once you provide your data, Forecast will automatically examine it, identify what is meaningful,
and produce a forecasting model capable of making predictions that are up to 50% more accurate than looking at time
series data alone.

To learn more, see [Amazon Forecast](https://aws.amazon.com/forecast/ "https://aws.amazon.com/forecast/").

## Amazon Forecast in AWS Managed Services FAQ

**Q: How do I request access to Forecast in my AMS account?**

Request access to AWS Firewall Manager by submitting an RFC with the Management | AWS service | Self-provisioned service | Add (ct-1w8z66n899dct) change type.
This RFC provisions the following IAM role to your account: `customer_forecast_admin_role`.
Once provisioned in your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Forecast in my AMS account?**

The default S3 bucket access only allows you to access buckets with the naming pattern
'customer-forecast-\*'. If you have your own naming convention for data buckets, discuss bucket naming and
related access setup with your Cloud Architect (CA). For example:

- You could define your specific Amazon Forecast service role with naming
  like 'AmazonForecast-ExecutionRole-\*' and associated proper S3 bucket access.
  See the Service role - AmazonForecast-ExecutionRole-Admin and IAM
  policy - customer_forecast_default_s3_access_policy, in the IAM console.
- You may need to associate related S3 buckets access to IAM federation role.
  See the IAM policy - customer_forecast_default_s3_access_policy, in the IAM console.

**Q: What are the prerequisites or dependencies to using Forecast in my AMS account?**

- Proper Amazon S3 bucket(s) must be created before using Forecast. Especially,
  the default S3 buckets access is with naming pattern ‘customer-forecast-\*’
- If you want to use naming patterns on S3 buckets other than 'customer-forecast-\*',
  you must create a new service role with S3 access permissions on the buckets:
  1.  A new service role to be created with naming 'AmazonForecast-ExecutionRole-{suffix}'.
  2.  A new IAM policy to be created which is similar to customer_forecast_default_s3_access_policy
      and to be associated with the new service role and related federation admin role
      (e.g. 'customer_forecast_admin_role')

**Q: How can I enhance data security while using Amazon Forecast?**

- For data encryption at rest, you can use AWS KMS to provision a customer-managed CMK to
  protect data storage on Amazon S3 service:
  - Enable default encryption on the bucket with the provision key and set up bucket
    policy to accept AWS KMS data encryption while putting data.
  - Enable the Amazon Forecast service role 'AmazonForecast-ExecutionRole-\*' and
    federation admin role (e.g. 'customer_forecast_admin_role') as the AWS KMS key user.

- For data encryption in transit, you can set up the HTTPS protocol, which is required while
  transferring objects on Amazon S3 bucket policy.
- Further restrictions on access control, enable a bucket policy for approved access
  for the Amazon Forecast service role 'AmazonForecast-ExecutionRole-\*' and admin role
  (e.g. 'customer_forecast_admin_role').

**Q: What are the best practices while using Amazon Forecast?**

- You should have a good understanding of your data classification practices and map out
  the related data security needs while using S3 buckets with Amazon Forecast.
- For Amazon S3 bucket configuration, we strongly advise you to enable HTTPS enforcement
  in your S3 bucket policy.
- You must be aware of the admin role 'customer_forecast_admin_role' support permissive
  access (Get/Delete/Put S3 objects) on Amazon S3 buckets with naming of 'customer-forecast-\*'.
  NOTE: If you require fine-grained access control for multiple teams, follow these practices:
  - Define your team-based access IAM identity (role/user) with least-privilege
    access to related Amazon S3 buckets.
  - Create team/project based AWS KMS CMKs grant proper access to corresponding IAM identities.
    (user access and 'AmazonForecast-ExecutionRole-{team/project}'.
  - Setup S3 bucket default encryption with the created AWS KMS CMKs.
  - Enforce S3 API traffics with HTTPS protocol on S3 bucket policy.
  - Enforce S3 bucket configuration for approved access for related IAM
    identities (user access and 'AmazonForecast-ExecutionRole-{team/project}' to the buckets.

- If you want to use the 'customer_forecast_admin_role' for general purpose, consider
  points listed previously to protect S3 buckets.

**Q: Where is compliance information about Amazon Forecast?**

See the [AWS services Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
