# Allow web page access to local files in Infrastructure Composer

The Infrastructure Composer console supports [local sync mode](using-composer-project-local-sync.md "using-composer-project-local-sync.md") and [Importing functions from the Lambda console](other-services-lambda.md "other-services-lambda.md"). To use these features, a web browser that
supports the File System Access API is required. Any recent version of Google Chrome and Microsoft Edge support all capabilities of the File
System Access API and can be used with **local sync** mode in Infrastructure Composer.

The File System Access API lets web pages gain access to your local file system in order to
read, write, or save files. This feature is off by default and requires your permission through a
visual prompt to allow it. Once granted, this access remains for the duration of your web page’s
browser session.

To learn more about the File System Access API, see:

- [File
  System Access API](https://developer.mozilla.org/en-US/docs/Web/API/File_System_Access_API "https://developer.mozilla.org/en-US/docs/Web/API/File_System_Access_API") in the _mdn web docs_.
- [The File System Access API: simplifying
  access to local files](https://web.dev/file-system-access/ "https://web.dev/file-system-access/") in the _web.dev_ website.

## local sync mode

**Local sync** mode lets you automatically sync and save your template files and project
folders locally as you design in Infrastructure Composer. To use this feature, a web browser that supports the File
System Access API is required.

## Data Infrastructure Composer gains access to

Infrastructure Composer gains read and write access to the project folder you allow, along with any child
folders of that project folder. This access is used to create, update, and save any template
files, project folders, and backup directories that are generated as you design. Data accessed by
Infrastructure Composer is not used for any other purpose and is not stored anywhere beyond your local file
system.

### Access to sensitive data

The File System Access API excludes or limits access to specific directories that may
contain sensitive data. An error will occur if you select one of these directories to use with
Infrastructure Composer _local sync_ mode. You can choose another local directory to connect with or use
Infrastructure Composer in its default mode with _local sync_ deactivated.

For more information, including examples of sensitive directories, see [Users giving access to
more, or more sensitive files than they intended](https://wicg.github.io/file-system-access/#privacy-wide-access "https://wicg.github.io/file-system-access/#privacy-wide-access") in the _File System Access
W3C Draft Community Group Report_.

If you use Windows Subsystem for Linux (WSL), the File System Access API
excludes access to the entire Linux directory because of its location within your
Windows system. You can use Infrastructure Composer with _local sync_ deactivated or
configure a solution to sync project files from your WSL directory to a working directory in
Windows. Then, use Infrastructure Composer _local sync_ mode with your Windows
directory.
