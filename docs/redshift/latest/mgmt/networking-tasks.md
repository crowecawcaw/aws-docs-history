Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Networking tasks

You can perform networking tasks like customizing your connection to a Redshift database. You might want to do this to control traffic for security or other purposes. You can also perform DNS-related tasks,
like setting up a custom domain name for your Redshift resources. These configuration tasks are available to you if you have an Amazon Redshift provisioned cluster
or with an Amazon Redshift Serverless workgroup.

###### Topics

- [Custom domain names for client
  connections](connecting-connection-CNAME.md "connecting-connection-CNAME.md")
- [Redshift-managed VPC endpoints](managing-cluster-cross-vpc.md "managing-cluster-cross-vpc.md")
- [Redshift resources in a VPC](managing-clusters-vpc.md "managing-clusters-vpc.md")
- [Controlling network traffic with Redshift enhanced VPC routing](enhanced-vpc-routing.md "enhanced-vpc-routing.md")
