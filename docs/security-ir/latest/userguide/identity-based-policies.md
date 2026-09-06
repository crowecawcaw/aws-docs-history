

# Identity-based policies for AWS Security Incident Response
<a name="identity-based-policies"></a>

 Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*. 

 With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. You can't specify the principal in an identity-based policy because it applies to the user or role to which it is attached. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*. 

**Topics**
+ [Identity-based policy examples](iam-examples.md)
+ [Policy best practices](policy-best-practices.md)
+ [Using the AWS Security Incident Response console](using-the-amazon-aws-security-incident-response-console.md)
+ [Allow users to view their own permissions](allow-users-to-view-their-own-permissions.md)
+ [Resource-Based Policies](resource-based-policies.md)
+ [Policy Actions](policy-actions.md)