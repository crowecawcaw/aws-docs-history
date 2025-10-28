# Importing a permissions file

The `imports` section is typically the first section of the permissions file. You can use this section to reference and include
existing permissions files. You can also use it to incorporate previously defined Amazon DCV permissions into your permissions file.

A permissions file can include multiple imports. An imported permissions file might import other permissions files.

###### To import a permissions file into your permissions file

- Use the `#import` statement and specify the location of the file with an absolute or a relative path
  - Windows Amazon DCV server:

  ```
  #import `..\file_path\file`
  ```

  - Linux Amazon DCV server:

  ```
  #import `../file_path/file`
  ```

###### Example

The following statement imports a permissions file named `dcv-permissions.file` using an absolute path. It's located in the
Amazon DCV installation folder on a Windows Amazon DCV server.

```
#import `c:\Program Files\NICE\DCV\dcv-permissions.file`
```
