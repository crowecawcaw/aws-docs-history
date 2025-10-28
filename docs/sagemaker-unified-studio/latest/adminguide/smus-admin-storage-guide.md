# Unified storage in Amazon SageMaker Unified Studio

As an Amazon SageMaker Unified Studio administrator, you are responsible for configuring and managing storage options that support your
organization's data science and machine learning workflows. This guide provides essential information for setting up,
configuring, and managing storage resources within Amazon SageMaker Unified Studio projects.

Amazon SageMaker Unified Studio provides two primary storage implementations for files used in Amazon SageMaker Unified Studio projects:

- **Amazon S3 storage**: This is the default option using Amazon Simple Storage Service for shared storage
  areas. All project members have read, write, update, and delete access by default to the shared storage area. This
  storage operates on a "last write wins" principle, meaning that files are immediately visible to all project members
  when modified. Due to this immediate visibility and the potential for concurrent access, team members must coordinate
  when working on the same files to avoid overwriting each other's changes.
- **Git-based storage**: This allows advanced version control using Git repositories
  connected via the Code Connections service to GitHub, GitHub Enterprise Server, GitLab, GitLab Self-Managed, and Bitbucket.

###### Topics

- [Configuring project storage options](configuring-project-storage.md "configuring-project-storage.md")
- [Performance and cost optimization](performance-cost-optimization.md "performance-cost-optimization.md")
- [Feature comparison matrix](feature-comparison.md "feature-comparison.md")
