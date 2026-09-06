

# SEC 2. How do you manage authentication for people and machines?
<a name="sec-02"></a>

There are two types of identities you need to manage when approaching operating secure AWS workloads.
+  **Human identities:** The human identities that require access to your AWS environments and applications can be categorized into three groups: workforce, third parties, and users.

   The *workforce* group includes administrators, developers, and operators who are members of your organization. They need access to manage, build, and operate your AWS resources. 

   *Third parties* are external collaborators, such as contractors, vendors, or partners. They interact with your AWS resources as part of their engagement with your organization. 

   *Users* are the consumers of your applications. They access your AWS resources through web browsers, client applications, mobile apps, or interactive command-line tools. 
+  **Machine identities:** Your workload applications, operational tools, and components require an identity to make requests to AWS services, such as reading data. These identities also include machines running within your AWS environment, like Amazon EC2 instances or AWS Lambda functions. You may also manage machine identities for external parties, or machines outside of AWS, that require access to your AWS environment.

**Topics**
+ [SEC02-BP01 Use strong sign-in mechanisms](sec_identities_enforce_mechanisms.md)
+ [SEC02-BP02 Use temporary credentials](sec_identities_unique.md)
+ [SEC02-BP03 Store and use secrets securely](sec_identities_secrets.md)
+ [SEC02-BP04 Rely on a centralized identity provider](sec_identities_identity_provider.md)
+ [SEC02-BP05 Audit and rotate credentials periodically](sec_identities_audit.md)
+ [SEC02-BP06 Employ user groups and attributes](sec_identities_groups_attributes.md)