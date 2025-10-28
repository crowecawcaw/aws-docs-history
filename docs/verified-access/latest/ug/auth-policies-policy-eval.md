# Verified Access policy evaluation

A policy document is a set of one or more policy statements (`permit` or
`forbid` statements). The policy applies if the conditional clause (the
`when` statement) is true. In order for a policy document to allow access, at
least one permit policy in the document must apply and no forbid policies can apply. If no
permit policies apply and/or one or more forbid policies apply, then the policy document
denies access. If you have defined policy documents for both the Verified Access group and the
Verified Access endpoint, both documents must allow access. If you have not defined a policy
document for the Verified Access endpoint, only the Verified Access group policy needs access.

AWS Verified Access validates the syntax when you create the policy, but it does not validate the
data you put in the conditional clause.
