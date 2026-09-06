

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Networking tasks
<a name="networking-tasks"></a>

You can perform networking tasks like customizing your connection to a Redshift database. You might want to do this to control traffic for security or other purposes. You can also perform DNS-related tasks, like setting up a custom domain name for your Redshift resources. These configuration tasks are available to you if you have an Amazon Redshift provisioned cluster or with an Amazon Redshift Serverless workgroup.

**Topics**
+ [Custom domain names for client connections](connecting-connection-CNAME.md)
+ [Redshift-managed VPC endpoints](managing-cluster-cross-vpc.md)
+ [Redshift resources in a VPC](managing-clusters-vpc.md)
+ [Controlling network traffic with Redshift enhanced VPC routing](enhanced-vpc-routing.md)