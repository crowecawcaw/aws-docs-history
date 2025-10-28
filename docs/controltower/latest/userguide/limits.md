# Limitations and quotas in AWS Control Tower

This chapter covers the AWS service limitations and quotas that you should keep in mind
as you use AWS Control Tower. If you're unable to set up your landing zone due to a service quota issue,
contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").

For more information about limitations that are specific to controls, see [Control limitations](control-limitations.md "control-limitations.md").

###### The Controls Reference Guide

Detailed information about AWS Control Tower controls has been moved to [the AWS Control Tower Controls Reference Guide](../controlreference/introduction.md "../controlreference/introduction.md").

## Known limitations in AWS Control Tower

This section describes known limitations and unsupported use cases in AWS Control Tower.

- AWS Control Tower has overall _concurrency limitations_. In general,
  one operation at a time is permitted. Two exceptions to this limitation are
  allowed:
  - Optional controls can be activated and deactivated concurrently,
    through an asynchronous process. Up to one hundred (100) control-related
    operations at a time can be in progress, in total, no matter if they are
    called from the console or from an API.
  - Accounts can be provisioned, updated, and enrolled concurrently in
    Account Factory, through an asynchronous process, with up to five (5)
    account-related operations in progress simultaneously. Unmanaging
    accounts must be performed one account at a time.

- Email addresses of shared accounts in the Security OU can be changed, but you
  must update your landing zone to see these changes in the AWS Control Tower
  console.
- A limit of five (5) SCPs per OU applies to OUs in your AWS Control Tower landing
  zone.
- AWS Control Tower supports up to 10,000 accounts in your landing zone's organization,
  divided among all of your OUs.
- Existing OUs with over 1000 directly nested accounts cannot be registered or
  re-registered in AWS Control Tower. For more information about limitations with
  registering OUs, see [Limitations based on underlying AWS
  services](region-stackset-limitations.md "region-stackset-limitations.md").
- **Customizations for AWS Control Tower (CfCT)** is unavailable in
  these AWS Regions, because some dependencies are not available:

      + Europe (Zurich), eu-central-2
      + Europe (Spain), eu-south-2
      + Canada West (Calgary) ca-west-1
      + Asia Pacific (Melbourne), ap-southeast-4
      + Asia Pacific (Malaysia), ap-southeast-5
      + Asia Pacific (Thailand), ap-southeast-7
      + Mexico (Central), mx-central-1

  You can deploy and manage resources in these Regions with CfCT, if you deploy
  CfCT to your AWS Control Tower home Region, but you cannot build CfCT in these
  Regions.

- **AWS Control Tower Account Factory for Terraform (AFT)** is not
  available in the following AWS Regions, because some dependencies are not
  available:
  - Europe (Zurich), eu-central-2
  - Europe (Spain), eu-south-2
  - Canada West (Calgary), ca-west-1
  - Asia Pacific (Melbourne), ap-southeast-4
  - Asia Pacific (Malaysia), ap-southeast-5
  - Asia Pacific (Thailand), ap-southeast-7
  - Mexico (Central), mx-central-1

- **AWS Control Tower Account Factory for Terraform (AFT)** cannot be
  deployed by new AFT customers in the following Regions, because AWS
  CodeConnections is not available to connect to a third-party version control
  system (VCS):
  - Asia Pacific (Hong Kong), Africa (Cape Town), Middle East (Bahrain),
    Europe (Zurich), Asia Pacific (Jakarta), Asia Pacific (Hyderabad), Asia
    Pacific (Osaka), Asia Pacific (Melbourne), Israel (Tel Aviv), Europe
    (Spain), Middle East (UAE), Asia Pacific (Thailand),
    Mexico (Central)

- The following Regions do not support **AWS Service Catalog**.
  - Canada West (Calgary), ca-west-1
  - Asia Pacific (Malaysia), ap-southeast-5
  - Asia Pacific (Thailand), ap-southeast-7
  - Mexico (Central), mx-central-1

###### Note

Regions that do not support Service Catalog do not support Account Factory Customizations for AWS Control Tower (AFC).

For more information about AWS Control Tower functionality in Regions that do not
support AWS Service Catalog, see [AWS Control Tower available in AWS
Canada West (Calgary)](2024-all.md#yyc-available "2024-all.md#yyc-available").

- When calling a control API to activate or deactivate a control, the limit for
  `EnableControl` and `DisableControl` updates in
  AWS Control Tower is one hundred (100) concurrent operations. Ten operations (10) can be
  in progress simultaneously, with the remaining operations queued. You may need
  to adjust your code to wait for completions.
- When you provision accounts through **Account Factory Customizations
  (AFC)**, with blueprints that are based in Terraform, you can
  deploy those blueprints to only one AWS Region. By default, AWS Control Tower deploys
  to the home Region.
