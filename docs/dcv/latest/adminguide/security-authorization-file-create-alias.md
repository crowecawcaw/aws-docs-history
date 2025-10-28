# Creating aliases

You can use the `[aliases]` section of the permissions file to create sets of Amazon DCV features. After an alias was defined, you can
grant or deny groups or individual users permissions to use it. Granting or denying permissions to an alias grants or denies permissions to all
of the features that are included in it.

To create aliases in your permissions file, you must first add the aliases section heading to the file.

```
[aliases]
```

You can then create your aliases under the section heading. To create an alias, provide the alias name, and then specify the alias members
in a comma-separated list. Alias members can be individual Amazon DCV features or other aliases.

```
`alias_name`=`member_1`, `member_2`, `member_3`
```

###### Example

The following example adds the aliases section heading and creates an alias that's named `file-management`. It includes the
`file-upload` and `file-download` features and an existing alias that's named `clipboard-management`.

```
[aliases]
file-management=file-upload, file-download, clipboard-management
```
