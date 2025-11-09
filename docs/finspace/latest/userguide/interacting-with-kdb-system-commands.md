After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Supported system commands

System commands control the q environment. The following table shows a list of
system commands that FinSpace supports.

| System commands | Description                                                                                                     | Constraints                                                                                                                                                             |
| --------------- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `\a`            | Lists all the tables in the current namespace.                                                                  | None                                                                                                                                                                    |
| `\awk`          | A pattern scanning and text processing language.                                                                | Only available on General purpose and HDB clusters.                                                                                                                     |
| `\b`            | Lists all the views (derived tables).                                                                           | None                                                                                                                                                                    |
| `\B`            | Lists all the pending views.                                                                                    |
| `\base64`       | Encodes or decodes data in base64 format.                                                                       | Only available on General purpose and HDB clusters.                                                                                                                     |
| `\c`            | Shows or sets the console size.                                                                                 | None                                                                                                                                                                    |
| `\C`            | Shows or sets the HTTP response size.                                                                           |
| `\cat`          | Concatenates and display files.                                                                                 | Only available on General purpose and HDB<br>clusters.                                                                                                                  |
| `\cd`           | Shows or sets the current directory.                                                                            |
| `\cp`           | Copies files or directories.                                                                                    |
| `\curl`         | Transfers data to or from a web server using HTTP, HTTPS, SCP,<br>SFTP, TFTP, and more.                         |
| `\d`            | Changes the current namespace.                                                                                  | None                                                                                                                                                                    |
| `\dirname`      | Removes the last component of a file name, leaving the directory<br>path.                                       | Only available on General purpose and HDB clusters.                                                                                                                     |
| `\e`            | Governs error trapping for client requests.                                                                     | None                                                                                                                                                                    |
| `\echo`         | Displays text or variables to the standard output.                                                              | Only available on General purpose and HDB clusters.                                                                                                                     |
| `\egrep`        | Searches for a pattern in one or more input files (extended<br>grep).                                           |
| `\f`            | Lists all functions in the current namespace.                                                                   | None                                                                                                                                                                    |
| `\find`         | Searches for files based on various criteria such as name, size,<br>and modification time.                      | Only available on General purpose and HDB clusters.                                                                                                                     |
| `\g`            | Shows or sets garbage-collection mode.                                                                          | None                                                                                                                                                                    |
| `\grep`         | Looks for a pattern in one or more input files.                                                                 | Only available on General purpose and HDB<br>clusters.                                                                                                                  |
| `\gunzip`       | Uncompresses a file or list of files.                                                                           |
| `\gzip`         | Compresses a file or list of files.                                                                             |
| `\jq`           | A lightweight and flexible command-line JSON processor.                                                         |
| `\l`            | Loads a script or data from a file or directory.                                                                | None                                                                                                                                                                    |
| `\ln`           | Creates a hard link or symbolic link to a file.                                                                 | Only available on General purpose and HDB clusters.                                                                                                                     |
| `\ls`           | Lists information about files and directories.                                                                  |
| `\mkdir`        | Creates a new directory.                                                                                        |
| `\mv`           | Moves or renames files or directories.                                                                          |
| `\nohup`        | Runs a command immune to hangups, allowing it to continue running<br>in the background.                         |
| `\o`            | Shows or sets the offset from Coordinated Universal Time<br>(UTC).                                              | None                                                                                                                                                                    |
| `\p`            | Shows or sets the TCP port on which the q session listens.                                                      | FinSpace supports this command with no arguments, which gets the<br>current port. It is only permitted with argument 443 (noop), not<br>permitted with other arguments. |
| `\P`            | Sets the display precision for floating-point numbers.                                                          | None                                                                                                                                                                    |
| `\pgrep`        | Looks up or signal processes based on name and other<br>attributes.                                             | Only available on General purpose and HDB clusters.                                                                                                                     |
| `\ps`           | Displays information about running processes.                                                                   |
| `\pwd`          | Prints the current working directory.                                                                           |
| `\r`            | Renames a file.                                                                                                 | None                                                                                                                                                                    |
| `\readlink`     | Displays the value of a symbolic link.                                                                          | Only available on General purpose and HDB clusters.                                                                                                                     |
| `\rm`           | Removes files or directories.                                                                                   |
| `\rmdir`        | Removes empty directories.                                                                                      |
| `\s`            | Shows or sets the number of secondary threads available.                                                        | None                                                                                                                                                                    |
| `\S`            | Shows or sets the value of the random seed.                                                                     |
| `\sed`          | A stream editor that filters and transforms text.                                                               | Only available on General purpose and HDB clusters.                                                                                                                     |
| `\sleep`        | Suspends execution for a specified period of time.                                                              |
| `\t`            | Shows or sets the timer interrupt in milliseconds.                                                              | FinSpace supports this command but it is not fully functional as the<br>function called by the timer can only be set by the init script.                                |
| `\T`            | Shows or sets the client execution timeout.                                                                     | None                                                                                                                                                                    |
| `\touch`        | Creates a new file or updates the timestamp of an existing<br>file.                                             | Only available on General purpose and HDB clusters.                                                                                                                     |
| `\tr`           | Translates or deletes characters from standard input.                                                           |
| `\ts`           | Runs an expression and shows the runtime and memory used.                                                       | None                                                                                                                                                                    |
| `\unzip`        | Extracts files from a ZIP archive.                                                                              | Only available on General purpose and HDB clusters.                                                                                                                     |
| `\v`            | Lists variables in the current or specified namespace.                                                          | None                                                                                                                                                                    |
| `\w`            | Shows memory usage or sets workspace memory limit.                                                              |
| `\W`            | Shows or sets the start-of-week offset.                                                                         |
| `\wc`           | Counts the number of lines, words, and characters in one or more<br>files.                                      | Only available on General purpose and HDB clusters.                                                                                                                     |
| `\xargs`        | Builds and executes command lines from standard input.                                                          |
| `\z`            | Shows or sets the format for date parsing.                                                                      | None                                                                                                                                                                    |
| `\zip`          | Packages and compresses files into a ZIP archive.                                                               | Only available on General purpose and HDB clusters.                                                                                                                     |
| `\_`            | In debugger’s prompt, clears one level from the execution stack or<br>toggles between the q and k interpreters. | None                                                                                                                                                                    |
| `\1`            | Redirects stdout to files from within the q session.                                                            |
| `\2`            | Redirects stderr to files from within the q session.                                                            |

## Helper environment

variables

You can quickly access user directories through the following environment
variables that return a string of the folder path.

| Helper environment variables | Use for                                                                                 | Directory                  |
| ---------------------------- | --------------------------------------------------------------------------------------- | -------------------------- |
| `.aws.akcp`                  | Primary user code path.                                                                 | `/opt/kx/app/code`         |
| `.aws.akcsp`                 | Secondary user code path that's available only for<br>\*_General purpose_<br>• cluster. | `/opt/kx/app/code_scratch` |
| `.aws.akscp`                 | Primarily used for handling savedown functionality with an<br>RDB cluster.              | `/opt/kx/app/scratch`      |

## Loading databases relative to code

directory

We have added a symlink to the code directory to allow loading of database
relative to the code path. For example, if the database is labeled as _kxDatabase_ and the current working directory is
/`opt/kx/app/code` then the database can be loaded as `\l
 /kxDatabase`.
