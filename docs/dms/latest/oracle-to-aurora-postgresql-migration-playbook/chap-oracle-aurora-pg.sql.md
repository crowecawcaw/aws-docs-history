# Oracle UTL_FILE package

With AWS DMS, you can access data and read/write files on the server’s file system using the Oracle `UTL_FILE` package. The `UTL_FILE` package provides APIs to operate on server files, allowing applications to read and write operating system files.

| Feature compatibility | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                    |
| --------------------- | ---------------------------------- | ------------------------- | -------------------------------------------------- |
| No compatibility      | No automation                      | N/A                       | PostgreSQL doesn’t have the `UTL_FILE` equivalent. |

## Oracle usage

Oracle `UTL_FILE` PL/SQL package enables you to access files stored outside of the database such as files stored on the operating system, the database server, or a connected storage volume. `UTL_FILE.FOPEN`, `UTL_FILE.GET_LINE`, and `UTL_FILE.PUT_LINE` are procedures within the `UTL_FILE` package used to open, read, and write files.

**Examples**

Run an anonymous PL/SQL block that reads a single line from file1 and writes it to file2.

- Use `UTL_FILE.FILE_TYPE` to create a handle for the file.
- Use `UTL_FILE.FOPEN` to open streamable access to the file and specify:
  - The logical Oracle directory object pointing to the O/S folder where the file resides.
  - The file name.
  - The file access mode: 'A'=append mode, 'W'=write mode

- Use `UTL_FILE.GET_LINE` to read a line from the input file into a variable.
- Use `UTL_FILE.PUT_LINE` to write a single line to the output file.

```
DECLARE
strString1 VARCHAR2(32767);
fileFile1 UTL_FILE.FILE_TYPE;
BEGIN
fileFile1 := UTL_FILE.FOPEN('FILES_DIR','File1.tmp','R');
UTL_FILE.GET_LINE(fileFile1,strString1);
UTL_FILE.FCLOSE(fileFile1);
fileFile1 := UTL_FILE.FOPEN('FILES_DIR','File2.tmp','A');
utl_file.PUT_LINE(fileFile1,strString1);
utl_file.fclose(fileFile1);
END;
/
```

For more information, see [UTL_FILE](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/UTL_FILE.html#GUID-EBC42A36-EB72-4AA1-B75F-8CF4BC6E29B4 "https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/UTL_FILE.html#GUID-EBC42A36-EB72-4AA1-B75F-8CF4BC6E29B4") in the _Oracle documentation_.

## PostgreSQL usage

Amazon Aurora PostgreSQL doesn’t currently provides a directly comparable alternative for Oracle `UTL_FILE` package.
