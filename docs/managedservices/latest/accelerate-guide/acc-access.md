# Access management in AMS Accelerate

Access management is how your resources are protected by allowing only authorized and authenticated access. With AMS Accelerate, you're
responsible for managing access to your AWS accounts and their underlying resources, such as access management solutions, access policies, and
related processes. In order to help you manage your access solution, AMS Accelerate deploys AWS Config rules that detect common IAM misconfigurations,
and then deliver remediation notifications. A common IAM misconfiguration is that the root user has access keys. The `iam-root-access-key-check` config rule
checks if the root user access key is available and is compliant or if the access key does not exist. For a list of config rules deployed by AMS, see the
[AMS AWS Config Rule library](acc-sec-compliance.md#acc-sec-compliance-rules "acc-sec-compliance.md#acc-sec-compliance-rules").

###### Topics

- [Get access to the Accelerate console](acc-access-permissions.md "acc-access-permissions.md")
- [Permissions to use AMS features](acc-access-customer.md "acc-access-customer.md")
- [Why and when AMS accesses your account](access-justification.md "access-justification.md")
- [How AMS accesses your account](acc-access-operator.md "acc-access-operator.md")
- [How and when to use the root user account in AMS](how-when-to-use-root.md "how-when-to-use-root.md")
