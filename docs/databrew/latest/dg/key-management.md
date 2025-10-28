# Key management

You can use IAM with DataBrew to define users, AWS resources, groups, roles, and
fine-grained policies regarding access, denial, and more.

You can define the access to the metadata using both resource-based and identity-based
policies, depending on your organization's needs. Resource-based policies list the
principals that are allowed or denied access to your resources, allowing you to set up
policies such as cross-account access. Identity policies are specifically attached to
users, groups, and roles within IAM.

DataBrew supports creating your own AWS KMS key "bring your own key" encryption.
DataBrew also provides server-side encryption using KMS keys from AWS KMS for DataBrew jobs.
