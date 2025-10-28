# List contents of a remote directory

Before you retrieve files from a remote SFTP server, you can retrieve the contents of a
directory on the remote SFTP server. To do this, you use the [StartDirectoryListing](../APIReference/API_StartDirectoryListing.md "../APIReference/API_StartDirectoryListing.md") API operation.

The following example lists the contents of the `home` folder on the
remote SFTP server, which is specified in the connector's configuration. The results are
placed into the Amazon S3 location `/amzn-s3-demo-bucket/connector-files`, and
into a file named
`c-AAAA1111BBBB2222C-6666abcd-11aa-22bb-cc33-0000aaaa3333.json`.

```
aws transfer start-directory-listing  \
   --connector-id c-AAAA1111BBBB2222C  \
   --output-directory-path /amzn-s3-demo-bucket/example/connector-files  \
   --remote-directory-path /home
```

This AWS CLI command returns a listing ID and the name of the file that contains the
results.

```
{
    "ListingId": "6666abcd-11aa-22bb-cc33-0000aaaa3333",
    "OutputFileName": "c-AAAA1111BBBB2222C-6666abcd-11aa-22bb-cc33-0000aaaa3333.json"
}
```

###### Note

The naming convention for the output file is
``connector-ID`-`listing-ID`.json`.

The JSON file contains the following information:

- `filePath`: the complete path of a remote file, relative to the
  directory of the listing request for your SFTP connector on the remote
  server.
- `modifiedTimestamp`: the last time the file was modified, in seconds,
  Coordinated Universal Time (UTC) format. This field is optional. If the remote file
  attributes don't contain a timestamp, it is omitted from the file listing.
- `size`: the size of the file, in bytes. This field is optional. If the
  remote file attributes don't contain a file size, it is omitted from the file
  listing.
- `path`: the complete path of a remote directory, relative to the
  directory of the listing request for your SFTP connector on the remote
  server.
- `truncated`: a flag indicating whether the list output contains all of
  the items contained in the remote directory or not. If your `truncated`
  output value is true, you can increase the value provided in the optional
  `max-items` input attribute to be able to list more items (up to the
  maximum allowed list size of 10,000 items).
  The following is an example of the contents of the output file
  (`c-AAAA1111BBBB2222C-6666abcd-11aa-22bb-cc33-0000aaaa3333.json`),
  where the remote directory contains two files and two sub-directories (paths).

```
{
    "files": [
        {
            "filePath": "/home/what.txt",
            "modifiedTimestamp": "2024-01-30T20:34:54Z",
            "size" : 2323
        },
        {
            "filePath": "/home/how.pgp",
            "modifiedTimestamp": "2024-01-30T20:34:54Z",
            "size" : 4691
        }
    ],
    "paths": [
        {
            "path": "/home/magic"
        },
        {
            "path": "/home/aws"
        },
    ],
    "truncated": "false"
}
```
