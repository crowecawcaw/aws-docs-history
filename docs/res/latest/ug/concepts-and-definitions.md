

# Concepts and definitions
<a name="concepts-and-definitions"></a>

This section describes key concepts and defines terminology specific to Research and Engineering Studio on AWS:

**File browser**  
A file browser is a part of the RES user interface where users who are currently logged in can view their file system.

**File system**  
The file system acts as a container for project data (often referred to as datasets). It provides a storage solution within a project's boundaries and improves collaboration and data access control.

**Global administrator**  
An administrative delegate with access to RES resources that are shared across a RES environment. Scope and permissions span multiple projects. They can create or modify projects and assign project owners. They can delegate or assign permissions to project owners and project members. Sometimes the same person acts as the RES administrator depending on the size of the organization.

**Project**  
A project is a logical partition within the application that serves as a distinct boundary for data and compute resources. This ensures governance over data flow and prevents sharing data and VDI hosts across projects.

**Project-based permissions**  
Project-based permissions describes a logical partition of both data and VDI hosts in a system where multiple projects can exist. A user's access to data and VDI hosts within a project is determined by their associated roles. A user must be assigned access (or project membership) for each project to which they require access. Otherwise, a user is unable to access project data and VDIs when they have not been granted membership.

**Project member**  
An end user of RES resources (VDI, storage, etc). Scope and permissions are restricted to the projects they are assigned to. They cannot delegate or assign any permissions.

**Project owner**  
An administrative delegate with access to, and ownership over, a specific project. Scope and permissions are restricted to the projects they own. They can assign permissions to project members in the projects they own.

**Software stack**  
Software stacks are [ Amazon Machine Images (AMIs)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) with RES-specific metadata based on any operating system a user has selected to provision for their VDI host.

**VDI hosts**  
Virtual desktop instance (VDI) hosts allow project members to access project-specific data and compute environments, ensuring secure and isolated workspaces.

For a general reference of AWS terms, see the [AWS Glossary](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html).