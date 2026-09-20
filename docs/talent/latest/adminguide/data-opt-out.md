

# Opting out of data use for service improvement
<a name="data-opt-out"></a>

AWS might use certain content that you process with Amazon Connect Talent to improve the service. This includes fixing operational issues, evaluating service performance, and debugging. Your content is not used for model training. You can choose to opt out of this use.

Only Amazon employees have access to this data. Your trust, privacy, and the security of Your Content are our highest priority, and our use complies with our commitments to you.

For Amazon Connect Talent, the content in scope for this use includes the following:
+ AI-led interview transcripts
+ Amazon Connect Talent Teammate chat transcripts

You control this choice with an AI services opt-out policy in AWS Organizations. An AI services opt-out policy applies to the accounts in your organization that you specify. When you opt out, AWS does not use the in-scope content to develop or improve the covered services, and AWS deletes content that is stored for that purpose.

## To opt out using an AI services opt-out policy
<a name="data-opt-out-configure"></a>

1. Sign in as a user in your organization's management account.

1. In AWS Organizations, enable the AI services opt-out policy type.

1. Create an AI services opt-out policy that opts out of data use for Amazon Connect Talent.

1. Attach the policy to the root, organizational units (OUs), or accounts that you want it to apply to.

For more information about AI services opt-out policies, see [AI services opt-out policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html) in the *AWS Organizations User Guide*.

## To check your opt-out status
<a name="data-opt-out-check"></a>

To check your opt-out status, review the opt-out policy configured by your organization. For more information, see [AI services opt-out policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out_syntax.html) in the *AWS Organizations User Guide*.

**Note**  
To use the opt-out policy, your AWS accounts must be centrally managed by AWS Organizations. If you have not already created an organization for your AWS accounts, see [Creating and managing an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org.html) in the *AWS Organizations User Guide*.