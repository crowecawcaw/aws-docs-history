# Directory assessments for hybrid directories

A directory assessment examines your self-managed Active Directory environment to make sure it meets the
requirements for creating a hybrid directory. This assessment verifies network connectivity,
domain controller configuration, and required services to help identify and resolve
potential issues before establishing a connection between your self-managed AD and
Directory Service.

There are two types of directory assessments:

- _`CUSTOMER` assessments_ – Initiated by you in the
  console when you begin setting up a hybrid directory. You can delete customer directory assessments,
  even while they're in progress. You can have up to 100 customer assessments.
- _`SYSTEM` assessments_ – Automatically created by
  AWS and run periodically after successful creation. You can't delete
  `SYSTEM` assessments.
  Directory assessments provide valuable information about your environment's readiness, including:

- Connectivity between your self-managed AD and AWS
- Availability of required services on your domain controllers
- Configuration compatibility with AWS Directory Service requirements
- Potential issues that might prevent successful hybrid directory creation
  A successful (passed) directory assessment is required before you can create a hybrid directory. If an
  assessment fails, you can view the detailed report to identify and address the issues before
  trying again. AWS deletes `SYSTEM` assessments after 30 days.

###### Topics

- [Creating directory assessments](create_directory_assessment.md "create_directory_assessment.md")
- [Viewing directory assessments](viewing_hybrid_dir_assessment.md "viewing_hybrid_dir_assessment.md")
- [Deleting directory assessments](deleting_hybrid_dir_assessment.md "deleting_hybrid_dir_assessment.md")
