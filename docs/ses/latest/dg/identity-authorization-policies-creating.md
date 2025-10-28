# Creating an identity

authorization policy in Amazon SES

An identity authorization policy is comprised of statements specifying what API actions
are allowed or denied for an identity and under what conditions.

To authorize an Amazon SES domain or email address identity that you own, you create an
authorization policy, and then attach that policy to the identity. An identity can have
zero, one, or many policies. However, a single policy can only be associated with a single
identity.

For a list of API actions that can be used in an identity authorization policy, see the
_Action_ row in the [Statements specific to
the policy](policy-anatomy.md#identity-authorization-policy-statements "policy-anatomy.md#identity-authorization-policy-statements") table.

You can create an identity authorization policy in the following ways:

- By using the policy generator – You can
  create a simple policy by using the policy generator in the SES console. In
  addition to allowing or denying permissions on SES API actions, you can
  constrain the actions with conditions. You can also use the policy generator to
  quickly create the basic structure of a policy and then customize it later by
  editing the policy.
- By creating a custom policy – If you want to
  include more advanced conditions or use an AWS service as the principal, you can
  create a custom policy and attach it to the identity by using the SES console
  or the SES API.

###### Topics

- [Using the policy generator](using-policy-generator.md "using-policy-generator.md")
- [Creating a custom policy](creating-custom-policy.md "creating-custom-policy.md")
