# Managing WorkSpaces Applications Computer Objects in Active Directory

WorkSpaces Applications does not delete computer objects from Active Directory. These computer
objects can be easily identified in your directory. Each computer object in the
directory is created with the `Description` attribute, which specifies a
fleet or an image builder instance and the name.

| Computer Object Description Examples | Type                | Name                                                             | Description Attribute |
| ------------------------------------ | ------------------- | ---------------------------------------------------------------- | --------------------- |
| Fleet                                | ExampleFleet        | `WorkSpaces Applications<br>• fleet:ExampleFleet`                |
| Image builder                        | ExampleImageBuilder | `WorkSpaces Applications -<br>image-builder:ExampleImageBuilder` |

You can identify and delete inactive computer objects created by WorkSpaces Applications by using
the following `dsquery computer` and `dsrm` commands. For more
information, see [Dsquery
computer](https://technet.microsoft.com/en-us/library/cc730720.aspx "https://technet.microsoft.com/en-us/library/cc730720.aspx") and [Dsrm](https://technet.microsoft.com/en-us/library/cc731865.aspx "https://technet.microsoft.com/en-us/library/cc731865.aspx") in
the Microsoft documentation.

The `dsquery` command identifies inactive computer objects over a
certain period of time and uses the following format. The `dsquery`
command should also be run with the parameter `-desc "WorkSpaces Applications*"`
to display only WorkSpaces Applications objects.

```
`dsquery computer "`OU-distinguished-name`" -desc "WorkSpaces Applications*" -inactive `number-of-weeks-since-last-login``
```

- `OU-distinguished-name` is the
  distinguished name of the organizational unit. For more information, see
  [Finding the Organizational Unit Distinguished Name](active-directory-oudn.md "active-directory-oudn.md"). If you don't provide the
  `OU-distinguished-name` parameter, the command
  searches the entire directory.
- `number-of-weeks-since-last-log-in`
  is the desired value based on how you want to define inactivity.
  For example, the following command displays all computer objects in the
  `OU=ExampleOU,DC=EXAMPLECO,DC=COM` organizational unit that have not
  been logged into within the past two weeks.

```
`dsquery computer OU=ExampleOU,DC=EXAMPLECO,DC=COM -desc "WorkSpaces Applications*" -inactive 2`
```

If any matches are found, the result is one or more object names. The
`dsrm` command deletes the specified object and uses the following
format:

```
`dsrm `objectname``
```

Where `objectname` is the full object name
from the output of the `dsquery` command. For example, if the
`dsquery` command above results in a computer object named
"ExampleComputer", the `dsrm` command to delete it would be as
follows:

```
`dsrm "CN=ExampleComputer,OU=ExampleOU,DC=EXAMPLECO,DC=COM"`
```

You can chain these commands together by using the pipe (`|`) operator.
For example, to delete all WorkSpaces Applications computer objects, prompting for confirmation for
each, use the following format. Add the `-noprompt` parameter to
`dsrm` to disable confirmation.

```
`dsquery computer `OU-distinguished-name` -desc "WorkSpaces Applications*" –inactive `number-of-weeks-since-last-log-in` | dsrm`
```
