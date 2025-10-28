# Working with task completion reports

A _task completion report_ provides details about the
results of an export, import, or release data repository task. The report includes results for the
files processed by the task that match the scope of the report. You can specify whether
to generate a report for a task by using the `Enabled` parameter.

Amazon FSx delivers the report to the file system's linked data repository in Amazon S3, using
the path that you specify when you enable the report for a task. The report's file name is
`report.csv` for import tasks and
`failures.csv` for export or release tasks.

The report format is a comma-separated value (CSV) file that has three fields:
`FilePath`, `FileStatus`, and `ErrorCode`.

Reports are encoded using RFC-4180-format encoding as follows:

- Paths starting with any of the following characters are contained in single quotation marks:
  `@ + - =`
- Strings that contain at least one of the following characters are contained in double
  quotation marks: `" ,`
- All double quotation marks are escaped with an additional double quotation mark.
  Following are a few examples of the report encoding:

- `@filename.txt` becomes `"""@filename.txt"""`
- `+filename.txt` becomes `"""+filename.txt"""`
- `file,name.txt` becomes `"file,name.txt"`
- `file"name.txt` becomes `"file""name.txt"`
  For more information about RFC-4180 encoding, see [RFC-4180 - Common Format and MIME Type for
  Comma-Separated Values (CSV) Files](https://tools.ietf.org/html/rfc4180 "https://tools.ietf.org/html/rfc4180") on the IETF website.

The following is an example of the information provided in a task completion report that includes only failed files.

```
myRestrictedFile,failed,S3AccessDenied
dir1/myLargeFile,failed,FileSizeTooLarge
dir2/anotherLargeFile,failed,FileSizeTooLarge
```

For more information about task failures and how to resolve them, see [Troubleshooting data repository task failures](failed-tasks.md "failed-tasks.md").
