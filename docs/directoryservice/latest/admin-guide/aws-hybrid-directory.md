# Understanding AWS Managed Microsoft AD (Hybrid Edition)

_AWS Managed Microsoft AD (Hybrid Edition)_ allows you to extend your existing Active Directory
to the AWS Cloud with AWS Managed Microsoft AD. This feature makes it easier to move your
AD–dependent workloads to AWS, adopt AWS services, and increase your Active Directory redundancy.
AWS will periodically run directory assessments on your hybrid directory which you can view in the Directory Service
console.

A hybrid directory in Directory Service connects your existing _Microsoft Active Directory_ with
_AWS Directory Service for Microsoft Active Directory_ (AWS Managed Microsoft AD). This creates an integrated identity
environment that spans on-premises, AWS, and multi-cloud infrastructure, allowing you to
maintain a single source of identity while extending your directory services to AWS.

A hybrid directory configuration provides several important capabilities:

- Extension of self-managed AD to the AWS Cloud without needing to establish a trust
  relationship
- Seamless authentication and authorization across environments using existing Active Directory
  credentials
- Consistent user credentials and group memberships across both your AD
  environments
- Centralized management of AD access policies and permissions

###### Topics

- [Hybrid directory prerequisites](create_hybrid_directory_prereqs.md "create_hybrid_directory_prereqs.md")
- [Creating a hybrid directory](hybrid_directory_create.md "hybrid_directory_create.md")
- [Viewing and editing a hybrid directory](hybrid_directory_view_and_edit.md "hybrid_directory_view_and_edit.md")
- [Deleting a hybrid directory](hybrid_directory_delete.md "hybrid_directory_delete.md")
- [Directory assessments for hybrid directories](hybrid_directory_assessment.md "hybrid_directory_assessment.md")
- [Troubleshooting hybrid directory and
  directory assessment](hybrid_directory_troubleshooting.md "hybrid_directory_troubleshooting.md")
