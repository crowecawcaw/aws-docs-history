# Enable and Administer Home Folders for Your WorkSpaces Applications Users

WorkSpaces Applications supports the following persistent storage options for users in your
organization:

- Home folders
- Google Drive for Google Workspace
- OneDrive for Business
- Custom shared folders (Server Message Block (SMB) network drives)
  You can enable one or more options for your organization. When you enable home folders
  for an WorkSpaces Applications stack, users of the stack can access a persistent storage folder during
  their application streaming sessions. No further conﬁguration is required for your users
  to access their home folder. Data stored by users in their home folder is automatically
  backed up to an Amazon Simple Storage Service bucket in your Amazon Web Services account and is made available to those
  users in subsequent sessions.

Files and folders are encrypted in transit using Amazon S3's SSL endpoints. Files and
folders are encrypted at rest using Amazon S3-managed encryption keys.

Home folders are stored on fleet instances in the following default locations:

- For single-session, non-domain-joined Windows instances:
  C:\Users\PhotonUser\My Files\Home Folder
- For multi-session, non-domain-joined Windows instances:
  C:\Users\as2-xxxxxxxx\My Files\Home Folder , where as2-xxxxxxxxx is a random
  user name assigned to each user session. You can determine your local user name
  through env variable $USERNAME.
- Domain-joined Windows instances: C:\Users\%username%\My Files\Home
  Folder
- Linux instances: ~/MyFiles/HomeFolder
  As an administrator, use the applicable path if you configure your applications to
  save to the home folder. In some cases, your users may not be able to find their home
  folder because some applications do not recognize the redirect that displays the home
  folder as a top-level folder in File Explorer. If this is the case, your users can
  access their home folder by browsing to the same directory in File Explorer.

###### Contents

- [Files and Directories Associated with Compute-Intensive Applications](storage-solutions-files-directories-associated-with-compute-intensive-applications.md "storage-solutions-files-directories-associated-with-compute-intensive-applications.md")
- [Enable Home Folders for Your WorkSpaces Applications Users](enable-home-folders.md "enable-home-folders.md")
- [Administer Your Home Folders](home-folders-admin.md "home-folders-admin.md")
