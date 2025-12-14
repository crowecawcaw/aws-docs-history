**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Configuring logging for an AWS Network Firewall policy

This section explains how you can enable centralized logging for your Network Firewall policies to get detailed information
about traffic within your organization. You can select flow logging to capture network
traffic flow, or alert logging to report traffic that matches a rule with the rule action
set to `DROP` or `ALERT`. For more information about AWS Network Firewall
logging, see [Logging network traffic from AWS Network Firewall](../../../network-firewall/latest/developerguide/firewall-logging.md "../../../network-firewall/latest/developerguide/firewall-logging.md") in the _AWS Network Firewall Developer Guide_.

You send logs from your policy's Network Firewall firewalls to an Amazon S3 bucket.
After you enable logging, AWS Network Firewall delivers logs for each configured Network Firewall
by updating the firewall settings to deliver logs to your selected Amazon S3 buckets
with the reserved AWS Firewall Manager prefix, `<policy-name>-<policy-id>`.

###### Note

This prefix is used by Firewall Manager to determine whether a logging configuration
was added by Firewall Manager, or whether it was added by the account owner. If the
account owner attempts to use the reserved prefix for their own custom logging, it
is overwritten by the logging configuration in the Firewall Manager policy.

For more information about how to create an Amazon S3 bucket and review the stored logs,
see [What is Amazon S3?](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") in the _Amazon Simple Storage Service User Guide_.

To enable logging you must meet the following requirements:

- The Amazon S3 that you specify in your Firewall Manager policy must exist.
- You must have the following permissions:
  - `logs:CreateLogDelivery`
  - `s3:GetBucketPolicy`
  - `s3:PutBucketPolicy`

- If the Amazon S3 bucket that's your logging destination uses server-side encryption with keys that are stored in AWS Key Management Service, you must add the following policy to your AWS KMS customer-managed key to allow Firewall Manager to log to your CloudWatch Logs log group:

```

{
    "Effect": "Allow",
    "Principal": {
        "Service": "delivery.logs.amazonaws.com"
    },
    "Action": [
        "kms:Encrypt*",
        "kms:Decrypt*",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:Describe*"
    ],
    "Resource": "*"
}

```

Note that only buckets in the Firewall Manager administrator account may be used for
AWS Network Firewall central logging.

When you enable centralized logging on a Network Firewall policy, Firewall Manager takes these
actions on your account:

- Firewall Manager updates the permissions on selected S3 buckets to allow
  for log delivery.
- Firewall Manager creates directories in the S3 bucket for each member
  account in the scope of the policy. The logs for each account can be
  found at `<bucket-name>/<policy-name>-<policy-id>/AWSLogs/<account-id>`.

###### To enable logging for a Network Firewall policy

1. Create an Amazon S3 bucket using your Firewall Manager administrator account.
   For more information, see
   [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon Simple Storage Service User Guide_.
2. Sign in to the AWS Management Console using your Firewall Manager administrator account, and then open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2 "https://console.aws.amazon.com/wafv2/fmsv2"). For information about setting up a Firewall Manager administrator account, see
   [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md").

###### Note

For information about setting up a Firewall Manager administrator account, see
[AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md"). 3. In the navigation pane, choose **Security Policies**. 4. Choose the Network Firewall policy that you want to enable logging for. For
more information about AWS Network Firewall logging, see
[Logging network traffic from AWS Network Firewall](../../../network-firewall/latest/developerguide/firewall-logging.md "../../../network-firewall/latest/developerguide/firewall-logging.md") in the _AWS Network Firewall Developer Guide_. 5. On the **Policy details** tab, in the **Policy rules**
section, choose **Edit**. 6. To enable and aggregate logs, choose one or more options under
**Logging configuration**:

    * **Enable and aggregate flow logs**
    * **Enable and aggregate alert logs**

7. Choose the Amazon S3 bucket where you want your logs to be delivered. You must choose a bucket for
   each log type that you enable. You can use the same bucket for both log
   types.
8. (Optional) If you want custom member account-created logging to be replaced with the policy’s
   logging configuration, choose **Override existing logging
   configuration**.
9. Choose **Next**.
10. Review your settings, then choose **Save** to save your
    changes to the policy.

###### To disable logging for a Network Firewall policy

1. Sign in to the AWS Management Console using your Firewall Manager administrator account, and then open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2 "https://console.aws.amazon.com/wafv2/fmsv2"). For information about setting up a Firewall Manager administrator account, see
   [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md").

###### Note

For information about setting up a Firewall Manager administrator account, see
[AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md"). 2. In the navigation pane, choose **Security Policies**. 3. Choose the Network Firewall policy that you want to disable logging for. 4. On the **Policy details** tab, in the
**Policy rules** section, choose **Edit**. 5. Under **Logging configuration status**, deselect
**Enable and aggregate flow logs** and
**Enable and aggregate alert logs** if they are selected. 6. Choose **Next**. 7. Review your settings, then choose **Save** to save
your changes to the policy.
