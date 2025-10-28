# AI-based services and AWS Control Tower

You can create service control policies (SCPs) that allow you to opt out of
having your data stored by AI-based services on AWS. These SCP policies specify that AI-based services, such
as Amazon Rekognition or Amazon CodeWhisperer, cannot store and use your data to improve other AI-based AWS services.

These AI opt-out SCP policies can apply to your entire organization, to an OU, or to a specific
account. The policies are global in effect. You can find more information about these
policies at [AI services
opt-out policies](../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md "../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md"), in the AWS Organizations documentation.

For a list of AWS services that use AI, along with examples of policies, see [AI
services opt-out policy syntax and examples](../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out_syntax.md "../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out_syntax.md"), in the _AWS Organizations User Guide_.
