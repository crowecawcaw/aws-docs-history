

# Method-Specific Requirements

In addition to the general prerequisites, ensure you meet the following requirements for Identity Tagging:
+ **Product listing on AWS Marketplace.** The product code in your tag must correspond to a product listing on AWS Marketplace for your partner account. Tags that reference a product code without a matching Marketplace listing are rejected for attribution.
+ **Supported IAM principal type.** Identity Tagging applies to taggable IAM principals, which are IAM roles (cross-account and same-account) and IAM users. Federated users accessed through AWS IAM Identity Center use permission sets and session attributes rather than taggable IAM roles, and are not supported at launch.
+ **In-scope IAM principals.** Tag the IAM roles and users your partner solution operates, including cross-account roles your organization assumes in the customer's account. Both the tagged principal's direct API actions and the secondary actions it drives through another assumed or created principal are attributed, based on activity on billable AWS resources. Operations that do not reference billable resources do not generate attribution.