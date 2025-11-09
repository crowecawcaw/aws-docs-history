# Organizing assets into folders for Amazon Quick Sight

|                                            |
| ------------------------------------------ |
| \*_Applies<br>to:_<br>• Enterprise Edition |

In Quick Suite Enterprise edition, your team members can create personal and shared
folders to add hierarchical structure to Quick Sight asset management. Using folders,
people can more easily organize, navigate through, and discover dashboards, analyses,
datasets, data sources, and topics. Within a folder, you can still use your usual tools to
search for assets or to add assets to your favorites list.

You can use the following types of folders with Quick Sight:

- Personal folders to organize work for yourself.

Personal folders are visible only to the person who owns them. You can't transfer
ownership of personal folders to anyone else.

- Shared folders:

      + **Shared folders** organize work and simplify
       sharing among multiple people. To create and manage shared folders, you need
       to be a Quick Sight administrator.
      + **Shared restricted folders** are a type of
       shared folder in Quick Sight that ensure that assets remain in the shared
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


      Restricted folders can only be created with the Quick Sight [`CreateFolder`](https://aws.amazon.com/quicksight/latest/APIReference/API_CreateFolder.html "https://aws.amazon.com/quicksight/latest/APIReference/API_CreateFolder.html") API operation.
      + Users that are viewers on a folder and have the Author or Admin role in
       Quick Suite can view all asset types that are in the folder. Users
       that are viewers on a folder and have the Reader role in Quick Suite
       can only see dashboards and stories that are in the folder.

  All shared folders are visible to people who have access to them.
  Use the following topics to learn more about creating and configuring a folder or
  subfolder in Quick Sight.

###### Topics

- [Considerations for Quick Sight folders](folders-limitations.md "folders-limitations.md")
- [Overview of Quick Sight folders](folders-functionality.md "folders-functionality.md")
- [Permissions for Quick Sight shared folders](folders-security.md "folders-security.md")
- [Create and manage membership permissions for
  Quick Sight shared folders](sharing-folders.md "sharing-folders.md")
- [Creating Quick Sight scaled folders with the
  Quick Sight APIs](folders-scaled.md "folders-scaled.md")
