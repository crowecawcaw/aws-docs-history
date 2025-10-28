# Multi-Account Landing Zone viewing the compliance status of your AWS Config Rules

AMS multi-account landing zone utilizes the AWS Config aggregator service to create a centralized view of compliance across all your accounts.
This means you can see the compliance status of all AWS Config Rules across your AMS multi-account landing zone environment under the AWS Config aggregator in your security account.

The following is a sample of the AWS Config aggregator showcasing central compliance
status of AWS Config Rules across accounts.

![AWS Config dashboard showing compliant rules across regions and accounts.](images/ams-malz-dd-agg-rules.png)
For more information, see the AWS documentation for
[Config Aggregator](../../../config/latest/developerguide/aggregate-data.md "../../../config/latest/developerguide/aggregate-data.md").

- How does AMS use AWS Config rules?

AMS creates AWS Config Rules to give visibility into the configuration of your AWS resources against conditions
specified in the rules. If a rule is non-compliant, you can request a change and the AMS Ops team
will work with you to take corrective action.

- In that case, you see the following changes appear in your AMS accounts:

      + AWS Config Rules under AWS Config > Rules
      + Custom Config rules with their Lambda functions exist in your account
      + Config Aggregator in Security account and Config Authorization in all accounts
       (Multi-Account Landing Zone only)

  The following is a sample of AWS Config Rules and their compliance evaluation results
  is shown below:

![AWS Config Rules dashboard showing compliant status for multiple security-related rules.](images/ams-malz-dd-rules-2.png)
To learn more about AWS Config, see:

- AWS Config: [What Is Config?](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md")
- AWS Config Rules: [Evaluating Resources with Rules](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md")
- AWS Config Rules: [Dynamic Compliance Checking: AWS Config Rules – Dynamic Compliance Checking for Cloud Resources](https://aws.amazon.com/blogs/aws/aws-config-rules-dynamic-compliance-checking-for-cloud-resources/ "https://aws.amazon.com/blogs/aws/aws-config-rules-dynamic-compliance-checking-for-cloud-resources/")
- AWS Config Aggregator: [Multi-Account Multi-Region Data Aggregation](../../../config/latest/developerguide/aggregate-data.md "../../../config/latest/developerguide/aggregate-data.md")
