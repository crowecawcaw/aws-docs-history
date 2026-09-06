

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Use AMS SSP to provision AWS Well-Architected Tool in your AMS account
<a name="well-arch"></a>

Use AMS Self-Service Provisioning (SSP) mode to access AWS Well-Architected Tool capabilities directly in your AMS managed account. The AWS Well-Architected Tool helps you review the state of your workloads and compares them to the latest AWS architectural best practices. The tool is based on the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/), developed to help cloud architects build secure, high-performing, resilient, and efficient application infrastructure. This framework provides a consistent approach for you to evaluate architectures, has been used in tens of thousands of workload reviews conducted by the AWS solutions architecture team, and provides guidance to help implement designs that scale with application needs over time. To learn more, see [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/).

## AWS WA Tool in AWS Managed Services FAQ
<a name="set-well-arch-faqs"></a>

Common questions and answers:

**Q: How do I request access to AWS Well-Architected Tool in my AMS account?**

Request access to AWS Well-Architected Tool by submitting an RFC with the Management \| AWS service \| Self-provisioned service \| Add change type (ct-1w8z66n899dct). This RFC provisions the following IAM role to your account: `customer_well_architected_tool_console_admin_role`. After it's provisioned in your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using AWS Well-Architected Tool in my AMS account?**

Full functionality of the AWS Well-Architected Tool is available in your AMS account.

**Q: What are the prerequisites or dependencies to using AWS Well-Architected Tool in my AMS account?**

There are no prerequisites or dependencies to use AWS Well-Architected Tool in your AMS account.