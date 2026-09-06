# Organizing assets into folders for Amazon Quick

|                                           |
| ----------------------------------------- |
| **Applies<br>to:*<br>• Enterprise Edition |

In Quick Enterprise edition, your team members can create personal and shared
folders to add hierarchical structure to Quick asset management. Using folders,
people can more easily organize, navigate through, and discover dashboards, analyses,
datasets, data sources, and topics. Within a folder, you can still use your usual tools to
search for assets or to add assets to your favorites list.

You can use the following types of folders with Quick:

- Personal folders to organize work for yourself.

Personal folders are visible only to the person who owns them. You can't transfer
ownership of personal folders to anyone else.

- Shared folders:

  - **Shared folders** organize work and simplify
    sharing among multiple people. To create and manage shared folders, you need
    to be a Quick administrator.
  - **Shared restricted folders** are a type of
    shared folder in Quick that ensure that assets remain in the shared
    folder. Assets that are created from assets that exist within a shared
    restricted folder must also stay in the restricted folder. Assets that are
    located in restricted folders can't be moved or shared outside of the
    restricted folder. For example, if you create a dataset that uses a data
    source that's located in a shared restricted folder, the new dataset
    can't be moved outside of that shared restricted folder.

  Assets that are located in a restricted folder can be moved within the
  restricted folder tree into one or more subfolders. Subfolders of restricted
  folders behave like restricted folders, but dependent assets can exist in
  different subfolders under the same root restricted folder. The root
  restricted folder acts as a boundary that all assets in all subfolders can
  exist in as long as they remain within the root folder tree. For example, a
  dataset that is located in one subfolder can use a data source that is
  located either another subfolder in the same folder tree or in the root
  folder. Any supported asset type can be created in a root folder or in any
  of its subfolders. Users can have different roles in different subfolders.
  Subfolder permissions are inherited from the parent folders of that
  subfolder.

  ###### Restricted folder boundary enforcement scope

  Restricted folders enforce the security boundary only between these assets:
  analyses, dashboards, datasets, data sources, and topics. Other asset types
  and features in Quick can access data in a restricted folder.

  For example, an analysis in a restricted folder can be built only on a
  dataset within the same restricted folder tree, so it respects the boundary.
  However, a chat agent not in a restricted folder can still retrieve details
  from a dataset in a restricted folder.

  Restricted folders can only be created with the Quick [`CreateFolder`](../../../quicksight/latest/APIReference/API_CreateFolder.md "../../../quicksight/latest/APIReference/API_CreateFolder.md") API operation.
  - Users that are viewers on a folder and have the Author or Admin role in
    Quick can view all asset types that are in the folder. Users
    that are viewers on a folder and have the Reader role in Quick
    can only see dashboards and stories that are in the folder.
    All shared folders are visible to people who have access to them.
    Use the following topics to learn more about creating and configuring a folder or
    subfolder in Quick.

###### Topics

- [Considerations for Quick folders](folders-limitations.md "folders-limitations.md")
- [Overview of Quick folders](folders-functionality.md "folders-functionality.md")
- [Permissions for Quick shared folders](folders-security.md "folders-security.md")
- [Create and manage membership permissions for Quick shared folders](sharing-folders.md "sharing-folders.md")
- [Creating Quick scaled folders with the Quick APIs](folders-scaled.md "folders-scaled.md")
