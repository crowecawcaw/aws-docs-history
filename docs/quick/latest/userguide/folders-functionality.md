

# Overview of Quick folders
<a name="folders-functionality"></a>

In Quick, you can create personal and shared folders. You can also favorite your personal or shared folders for quick access by choosing the favorite ( ![Star icon outline.](http://docs.aws.amazon.com/quick/latest/userguide/images/favorite-icon.png)) icon next to it. 

You can do the following with personal folders:
+ Create subfolders.
+ Add assets to your folder, including analyses, dashboards, datasets, and data sources. To add assets to a personal folder, you must already have access to the assets. Multiple assets can have the same name.

**Shared folders (unrestricted)**

Quick administrators can perform the following tasks with shared folders.
+ Create or delete a shared folder and subfolders inside of it. You can move either of these around within the top-level folder.
+ Add or remove owners, contributors, and viewers. When you make a person an *owner* of the folder, you give them ownership of every asset in the folder. For more information, see [Permissions for Quick shared folders](folders-security.md).

The following table summarizes the actions that a Quick user can take when working with unrestricted shared folders based on their role.



| Action | Owner | Contributor | Viewer | 
| --- | --- | --- | --- | 
| Share an asset in a folder with users that don't have access to the folder | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Modify folder permissions | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Create assets in the folder | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Modify assets in the folder | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Delete assets in the folder | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Add an existing asset to a folder | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Remove an asset from a shared folder | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| View assets in the folder | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| Create downstream assets outside of the shared folder that use assets that are located in the shared folder | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes\* | 
| Create downstream assets in the folder that use assets that are located outside of the folder | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Create subfolders | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Delete subfolders | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Manage subfolder permissons | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Add existing assets to subfolders | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Create new assets in subfolders | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Delete assets in subfolders | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 

\*The user must be assigned an admin or author role to create assets.

**Restricted shared folders**

Restricted shared folders provide an additional security boundary that restricts the sharing of data outside of the folder. Administrators with the appropriate IAM permissions can perform the following tasks with restricted shared folders.
+ Restricted folders can be created using the `CreateFolder` API operation. For more information about the `CreatFolder` API operation, see [CreateFolder](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateFolder.html).
+ The contributor role is assigned to users that can create and edit assets within the restricted folders. Contributors can't manage the permissions of the folder or of the assets that are in the restricted folder.
+ Administrators can assign folder contributor and viewer permissions to users with the `UpdateFolderPermissions` API operation. For more information about the `UpdateFolderPermissions` API operation, see [UpdateFolderPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateFolderPermissions.html).

The following table summarizes the actions that a Quick user can take when working with restricted shared folders based on their role.



| Action | Contributor | Viewer | 
| --- | --- | --- | 
| Share an asset in a folder with users that don't have access to the folder | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Modify folder permissions | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Create assets in the folder | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Modify assets in the folder | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Delete assets from the folder | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Add an existing asset to a folder | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Remove an asset from a shared folder | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| View assets in the folder | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| Create downstream assets outside of the shared folder that use assets that are located in the shared folder | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Create downstream assets in the folder that use assets that are located outside of the folder | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Create subfolders | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Delete subfolders | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Manage subfolder permissions | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Add existing assets to subfolders | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Create new assets in subfolders | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| Delete assets from subfolders | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 

The owner role is not supported for restricted shared folders.

After you choose which folder type best fits your use case, see [Permissions for Quick shared folders](folders-security.md) and [Create and manage membership permissions for Quick shared folders](sharing-folders.md) to create folders and set up folder permissions.