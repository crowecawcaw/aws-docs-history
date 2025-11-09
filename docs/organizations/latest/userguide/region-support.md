# Region support for AWS Organizations

AWS Organizations is available in all AWS commercial Regions, AWS GovCloud (US) Regions, and China Regions.

For a list of functionality differences in AWS GovCloud (US) Regions, see [AWS Organizations in AWS GovCloud (US)](../../../govcloud-us/latest/UserGuide/govcloud-organizations.md "../../../govcloud-us/latest/UserGuide/govcloud-organizations.md").

For a list of functionality differences in China Regions, see [AWS Organizations in China](https://docs.amazonaws.cn/en_us/aws/latest/userguide/organizations.html "https://docs.amazonaws.cn/en_us/aws/latest/userguide/organizations.html").

**The service endpoints for Organizations are located**:

- In US East (N. Virginia) for commercial
  organizations
- In AWS GovCloud (US-West) for AWS GovCloud (US) organizations
- In China (Ningxia) for China organizations, operated by
  Ningxia Western Cloud Data Technology Co. Ltd (NWCD).
  All organization entities are globally accessible, except for organizations managed in China,
  similar to how AWS Identity and Access Management (IAM) works today.
  You do not need to specify an AWS Region when you create and manage your organization,
  but you will need to create a separate organization for accounts used in China.
  Users in your AWS accounts can use AWS services in any geographic Region where that service is available.

###### Note

**Tag policies are only supported in a subset of Regions**

Tag policies are a type of policy that can help you standardize tags across resources in your organization's accounts.
Tag policies are only supported in a subet of Regions where Organizations is supported. For a list of Regions where tag policies are supported,
see [Tag policies | Support Regions](orgs_manage_policies_tag-policies-supported-regions.md "orgs_manage_policies_tag-policies-supported-regions.md").

## List of available AWS Regions

The following table lists all the available AWS Regions.

| Region Name                | Region         | Endpoint                                                                            | Protocol       |
| -------------------------- | -------------- | ----------------------------------------------------------------------------------- | -------------- |
| US East (Ohio)             | us-east-2      | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Asia Pacific (Hong Kong)   | ap-east-1      | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Asia Pacific (Hyderabad)   | ap-south-2     | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Asia Pacific (Jakarta)     | ap-southeast-3 | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Asia Pacific (Malaysia)    | ap-southeast-5 | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Asia Pacific (Melbourne)   | ap-southeast-4 | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Asia Pacific (Mumbai)      | ap-south-1     | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Asia Pacific (New Zealand) | ap-southeast-6 | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Asia Pacific (Osaka)       | ap-northeast-3 | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Asia Pacific (Seoul)       | ap-northeast-2 | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Asia Pacific (Singapore)   | ap-southeast-1 | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Asia Pacific (Sydney)      | ap-southeast-2 | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Asia Pacific (Taipei)      | ap-east-2      | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Asia Pacific (Thailand)    | ap-southeast-7 | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Asia Pacific (Tokyo)       | ap-northeast-1 | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Canada (Central)           | ca-central-1   | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Canada West (Calgary)      | ca-west-1      | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Europe (Frankfurt)         | eu-central-1   | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Europe (Ireland)           | eu-west-1      | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Europe (London)            | eu-west-2      | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Europe (Milan)             | eu-south-1     | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Europe (Paris)             | eu-west-3      | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Europe (Spain)             | eu-south-2     | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Europe (Stockholm)         | eu-north-1     | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Europe (Zurich)            | eu-central-2   | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Israel (Tel Aviv)          | il-central-1   | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Mexico (Central)           | mx-central-1   | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Middle East (Bahrain)      | me-south-1     | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| Middle East (UAE)          | me-central-1   | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| South America (São Paulo)  | sa-east-1      | organizations.us-east-1.amazonaws.com<br>organizations-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| AWS GovCloud (US-East)     | us-gov-east-1  | organizations.us-gov-west-1.amazonaws.com                                           | HTTPS          |
| AWS GovCloud (US-West)     | us-gov-west-1  | organizations.us-gov-west-1.amazonaws.com                                           | HTTPS          |
