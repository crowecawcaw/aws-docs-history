# Transfer files

###### Topics

- [Send and retrieve files by using
  an SFTP connector](#send-retrieve-connector-details "#send-retrieve-connector-details")

## Send and retrieve files by using

an SFTP connector

To send and retrieve files by using an SFTP connector, you use the [StartFileTransfer](../APIReference/API_StartFileTransfer.md "../APIReference/API_StartFileTransfer.md") API operation and specify the
following parameters, depending on whether you're _sending files_
(outbound transfers) or _receiving files_ (inbound transfers).
Note that each `StartFileTransfer` request can contain 10 distinct paths.

###### Note

By default, SFTP connectors process one file at a time, transferring files sequentially.
You have an option to accelerate transfer performance by having your connectors create
concurrent sessions with remote servers that support concurrent sessions from the same
user, and process up to 5 files in parallel.

To enable concurrent connections for any connector, you can edit the **Maximum conncurent connections** setting when creating or updating a connector.
For details, see [Create an SFTP connector with
service-managed egress](create-sftp-connector-procedure.md "create-sftp-connector-procedure.md").

- **Outbound transfers**
  - `send-file-paths` contains from one to ten source file
    paths, for files to transfer to the partner's SFTP server.
  - `remote-directory-path` is the remote path to send a
    file to on the customer's SFTP server.

- **Inbound transfers**
  - `retrieve-file-paths` contains from one to ten remote
    paths. Each path specifies a location for transferring files from
    the partner's SFTP server to your Transfer Family server.
  - `local-directory-path` is the Amazon S3 location (bucket and
    optional prefix) where your files are stored.

To send files, you specify the `send-file-paths` and
`remote-directory-path` parameters. You can specify up to 10 files
for the `send-file-paths` parameter. The following example command sends
the files named `/amzn-s3-demo-source-bucket/file1.txt` and
`/amzn-s3-demo-source-bucket/file2.txt`, located in Amazon S3
storage, to the `/tmp` directory on your partner's SFTP server.
To use this example command, replace the
`amzn-s3-demo-source-bucket` with your
own bucket.

```
aws transfer start-file-transfer --send-file-paths /amzn-s3-demo-source-bucket/file1.txt /amzn-s3-demo-source-bucket/file2.txt \
    --remote-directory-path /tmp --connector-id c-`1111AAAA2222BBBB3` --region `us-east-2`
```

To retrieve files, you specify the `retrieve-file-paths` and
`local-directory-path` parameters. The following example retrieves
the files `/my/remote/file1.txt` and
`/my/remote/file2.txt` on the partner's SFTP server, and
places it in the Amazon S3 location
/amzn-s3-demo-bucket/`prefix`. To use this example
command, replace the `user input placeholders`
with your own information.

```
aws transfer start-file-transfer --retrieve-file-paths /my/remote/file1.txt  /my/remote/file2.txt \
   --local-directory-path /`amzn-s3-demo-bucket/prefix` --connector-id c-`2222BBBB3333CCCC4` --region `us-east-2`
```

The previous examples specify absolute paths on the SFTP server. You can also use
relative paths: that is, paths that are relative to the SFTP user's home directory.
For example, if the SFTP user is `marymajor` and their home
directory on the SFTP server is `/users/marymajor/`, the
following command sends `/amzn-s3-demo-source-bucket/file1.txt`
to `/users/marymajor/test-connectors/file1.txt`

```
aws transfer start-file-transfer --send-file-paths /amzn-s3-demo-source-bucket/file1.txt \
   --remote-directory-path test-connectors --connector-id c-`2222BBBB3333CCCC4` --region `us-east-2`
```
