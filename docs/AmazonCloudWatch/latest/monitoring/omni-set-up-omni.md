

# Set up Omni
<a name="omni-set-up-omni"></a>

Setting up CloudWatch Omni involves two steps: creating a **domain** (the identity and access boundary for your organization) and creating a **space** (where you work with your telemetry). Depending on your scenario, these steps might happen together in one session or separately across teams.

**Note**  
Enabling Omni does not change or disable anything in CloudWatch. Your existing metrics, logs, alarms, dashboards, and Logs Insights queries keep working.

**Choose your setup path**

How you set up Omni depends on whether you work in a single AWS account or across an AWS Organization.

**Compare setup paths**

![With an account-level domain, the domain serves one account, and Region 1 and Region 2 in that account each hold one space reading its own CloudWatch Dataset. With an organization-level domain, one domain serves several accounts: Account A holds a space in Region 1 and in Region 2, and Account B holds a space in Region 1, each reading its own CloudWatch Dataset. There is one space per account and Region.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/omni-setup-domain-modes-compare-reskin.png)



| Capability | Single account | Multiple accounts (AWS Organizations) | 
| --- | --- | --- | 
| Single sign-in URL for your organization | Per account | Yes | 
| Member accounts create spaces without additional domain setup | No — each account creates its own domain | Yes | 
| Centralized identity provider configuration (IAM Identity Center) | Yes — configured per domain | Yes — configured once for the organization | 
| Multiple spaces across accounts share one domain | No | Yes | 
| Accounts that can create this domain | Any individual AWS account | AWS Organizations management account | 

Choose **single account** setup if you operate in one AWS account. Choose **organization** setup if you use multiple AWS accounts and want a single entry point.

**Single account**

You create an Account domain and a space together in your AWS account.

For instructions, see [Set up Omni for a single account](omni-set-up-omni-for-a-single-account.md).

**Multiple accounts (AWS Organizations)**

An administrator creates the domain once from the management account. Any member account can then create its own space, which is automatically linked to the domain.

For instructions, see [Set up Omni for your organization](omni-set-up-omni-for-your-organization.md).

**Your organization already has a domain**

If an Organization domain already exists for your AWS Organization, you do not need to create a domain. Your account is already linked. Skip to space setup in [Set up Omni for your organization](omni-set-up-omni-for-your-organization.md).

**After setup**

After you complete either setup path:
+ Send telemetry from your applications or agents. See [Send telemetry to CloudWatch Omni](omni-send-telemetry.md).
+ Add your team and choose what each person can do. See [Control access to your space](omni-control-access-to-your-space.md).
+ Bring telemetry from more than one account into your space. See the centralization section of [Set up Omni for your organization](omni-set-up-omni-for-your-organization.md).