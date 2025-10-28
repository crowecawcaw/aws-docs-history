# Unified storage in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio provides flexible file storage options to support your analytics, AI and ML workflows.

Amazon SageMaker Unified Studio brings together the functionality and tools from existing AWS Analytics and AI/ML services into a single data and
AI development environment. As you work with different tools like JupyterLab, SQL Editor, Visual ETL Builder, or capabilities
from Amazon Bedrock inside Amazon SageMaker Unified Studio you'll create and manage files that represent your work.

## S3 storage

Amazon Simple Storage Service (S3) storage is the default option for storage of project files in Amazon SageMaker Unified Studio.

With S3 storage, you can easily share files by moving them between local and shared folders using simple
drag-and-drop operations. The file explorer provides a consistent interface across all tools, displaying both local and
shared directories in a single view with drag-and-drop functionality for easy file management. It allows users to create,
edit, delete, upload, and download files directly through the interface, with optional auto-save capabilities to prevent
data loss.

S3 storage provides basic file versioning capabilities when enabled by your administrator. This option is available
in all AWS regions where Amazon SageMaker Unified Studio is supported, making it ideal for teams working across different geographic locations.

For more information on configuring S3 storage see [Configuring project storage options](../adminguide/configuring-project-storage.md "../adminguide/configuring-project-storage.md").

### Key benefits of S3 storage:

- Simple file management
- Easy file sharing with drag-and-drop between folders
- Availability in all regions where Amazon S3 is supported

## Git-based storage

For projects requiring advanced version control, Amazon SageMaker Unified Studio allows you to connect your project to a Git repository where
all project members can access, store, and collaborate on files. This option provides full version control capabilities
including comprehensive commit history, branching, and merging.

When you choose Git-based storage, you'll need to specify a repository and branch during project creation. Once the project
is created, you'll be able to see the files that were created during repository bootstrapping directly from the project's home page.

With Git-based storage, you'll have access to full Git semantics regardless of whether you're using space-based tools
like JupyterLab or web-based tools like SQL Query Editor. This provides a consistent experience for team members accustomed
to working with Git.

### Key benefits of Git-based storage include:

- Full version control with commit history, branching, and merging
- Collaboration features like pull requests and code reviews
- Cross-project sharing by allowing multiple projects to use the same repository
- Integration with existing development workflows

## Storage working in different tools

Amazon SageMaker Unified Studio provides a consistent storage experience across different tools while optimizing for each tool's specific requirements.

### Web-based tools

When using web-based tools such as Query Editor and Visual ETL, you'll interact with files through a unified File
Explorer interface. This explorer displays your shared directory and allows you to navigate and manage shared files seamlessly.

You can perform various file operations directly from the File Explorer:

- Create, edit, and delete files and folders
- Upload and download files to/from shared storage
- Access version history (when available)
- Edit files directly within the source

All web-based tools offer optional auto-save functionality, which can be enabled to automatically save your changes as
you work. This feature helps prevent data loss if you navigate away from the page or experience connectivity issues.

### Space-based tools

Space-based tools like JupyterLab and Code Editor provide access to two types of storage spaces to support both individual work and
team collaboration.

#### Local storage (local folder)

The local storage features dedicated EBS storage that delivers superior performance for frequent file operations within your
workspace. Local storage serves as your personal workspace and the files in it are private to your Space.

Within your local storage, you can create and manage subfolders to organize your files effectively. This helps
you maintain a structured workspace for different aspects of your work.

When you save files to your local storage, they operate on a 'last write wins' principle—new changes overwrite
previous versions without versioning capabilities.

Your local folder

- Includes this root folder and any subfolders (except shared)
- Serves as your private workspace within each project
- Allows you to work on files privately
- Is ideal for frequent file access and modification
- Is visible only in this space
- Remains isolated from other project members, creating a secure environment for experimentation
  and development

#### Shared storage (shared folder)

Shared storage is implemented in Amazon S3 or Git repository and is accessible from all Amazon SageMaker Unified Studio tools. Project
members can create and manage subfolders within the shared storage to help organize artifacts effectively.

By default, all project members have read, write, update, and delete access to files within the shared storage.
This central repository allows team members to access common resources, share completed work, and maintain
project artifacts in a single location.

Shared storage operates on a "last write wins" principle, so you have to coordinate with team members when
working on the same files to avoid overwriting each other's changes.

The shared folder (Git and non-Git):

- Contains files visible to all project members
- Functions as a collaborative workspace accessible to all project members
- Is accessible across all your tools
- Updates immediately when any member adds or modifies files
- Operates on a "last write wins" mechanism, so team members should coordinate when working on the
  same files
- Is not well-suited for heavy file read/write workloads due to remote Amazon S3 origin of this folder
  and potential additional costs associated with frequent Amazon S3 access
- If two individuals are modifying the same file in this folder at the same time that might result
  in losing some changes

You can copy files between these locations as needed, allowing you to optimize your workflow based on
performance requirements and collaboration needs. For example, copy files from shared storage to local
storage for ML tasks requiring low latency.
