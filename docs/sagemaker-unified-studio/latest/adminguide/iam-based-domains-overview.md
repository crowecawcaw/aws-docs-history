# Overview of IAM-based domains

IAM-based domains provide the following capabilities:

- Setup using existing IAM roles and resources
- Authentication through federated IAM roles used for login
- Project creation and management interface within Amazon SageMaker Unified Studio
  IAM-based domains require two IAM roles to function properly:

Login IAM role

This role authenticates users and provides access to Amazon SageMaker Unified Studio. The login role
must have specific managed policies attached and inline policies configured to enable
domain and project operations. Users use this role to access the project assigned to
that IAM role when accessing the Amazon SageMaker Unified Studio interface.

Execution IAM role

This role defines the AWS services and data that can be accessed through
Amazon SageMaker Unified Studio projects. The execution role determines which tools, compute resources, data
sources, and AI/ML assets project members can access. Amazon SageMaker Unified Studio assumes this role to
make service calls on behalf of users within projects.

###### Note

The Execution IAM role can be the same IAM role as the Login IAM role.

Both roles require specific policy attachments and trust relationships to function
correctly within the IAM-based domain architecture. The system validates these permissions
during setup and provides guidance for any missing configurations.

Considerations:

- For the role used as the admin Login IAM role, consider a role with a smaller
  population of users who will be responsible for administering the domain.
- For the role used as the admin Execution IAM role, again consider a role with a
  smaller population of users because the role will grant access to a broader set of data
  within the account. A default project will be created for this Execution IAM role.
  Consider a role that has access to the appropriate data resources (Glue, Athena, etc.).
  This role will automatically be assigned AWS Lake Formation administrator permission
  enabling further data access.
