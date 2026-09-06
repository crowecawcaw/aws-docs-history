

# Enabling trusted access for AWS Account Management
<a name="using-orgs-trusted-access"></a>

Enabling trusted access for AWS Security Incident Response allows the delegated administrator of the management account to modify the information and metadata (for example, primary or alternate contact details) specific to each member account in AWS Organizations.

Use the following procedure to enable trusted access for AWS Security Incident Response in your organization.

**Minimum permissions**  
To perform these tasks, you must meet the following requirements:  
You can perform this only from the organization's management account.
Your organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html).

------
#### [ Console ]

**To enable trusted access for AWS Security Incident Response**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations). You must sign in as an IAM user, assume an IAM role, or sign in as the root user (not recommended) in the organization’s management account.

1. Choose **Services** in the navigation pane.

1. Choose **AWS Security Incident Response** in the list of services.

1. Choose **Enable trusted access**.

1. In the **Enable trusted access for AWS Security Incident Response** dialog box, type **enable** to confirm it, and then choose **Enable trusted access**.

------
#### [ API/CLI ]

**To enable trusted access for AWS Account Management**  
After running the following command, you can use credentials from the organization's management account to call Account Management API operations that use the `--accountId` parameter to reference member accounts in an organization.
+ AWS CLI: [enable-aws-service-access](https://docs.aws.amazon.com/organizations/latest/userguide/enable-aws-service-access.html)

  The following example enables trusted access for AWS Security Incident Response in the calling account's organization.

  ```
  $ aws organizations enable-aws-service-access \
                                         --service-principal security-ir.amazonaws.com
  ```

  This command produces no output if it's successful.

------