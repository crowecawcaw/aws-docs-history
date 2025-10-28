# Use Case 5: Extend your on-premises Active Directory to the AWS Cloud

If you already have an Active Directory infrastructure and want to use it when migrating Active Directory-aware
workloads to the AWS Cloud, AWS Managed Microsoft AD can help. You can use [Active Directory trusts](ms_ad_tutorial_test_lab_trust.md "ms_ad_tutorial_test_lab_trust.md") to connect AWS Managed Microsoft AD to your existing Active Directory. This means your users can
access Active Directory-aware and AWS applications with their on-premises Active Directory credentials, without needing
you to synchronize users, groups, or passwords.

For example, your users can sign in to the AWS Management Console and Amazon WorkSpaces by using their existing
Active Directory user names and passwords. Also, when you use Active Directory-aware applications such as SharePoint with
AWS Managed Microsoft AD, your logged-in Windows users can access these applications without needing to
enter credentials again.

You can also migrate your on-premises Active Directory domain to AWS to be free of
the operational burden of your Active Directory infrastructure using the [Active Directory Migration Toolkit (ADMT)](https://aws.amazon.com/blogs/security/how-to-migrate-your-on-premises-domain-to-aws-managed-microsoft-ad-using-admt/ "https://aws.amazon.com/blogs/security/how-to-migrate-your-on-premises-domain-to-aws-managed-microsoft-ad-using-admt/") along with the Password Export Service
(PES) to perform the migration.
