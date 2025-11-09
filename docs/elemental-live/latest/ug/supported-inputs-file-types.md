# Supported upstream systems

for file inputs

This table describes the different upstream systems that can provide
file content to Elemental Live.

The rows are sorted by type of input.

| Upstream system                             | Use case                                                                                  | Type of input  | Protocol                          | Push or pull? |
| ------------------------------------------- | ----------------------------------------------------------------------------------------- | -------------- | --------------------------------- | ------------- |
| Amazon S3 bucket                            | Pull a VOD asset from an Amazon S3 bucket, using a secure or<br>unsecure connection.      | File input     | custom protocol s3:// or s3ssl:// | Pull          |
| Aspera server                               | Pull a VOD asset from a server that supports the Aspera data<br>transfer protocol.        | File input     | Custom protocol aspera://         | Pull          |
| A directory on the Elemental Live appliance | Pull a VOD asset that is stored on a directory on the Live<br>appliance.                  | File input     | Not applicable                    | Pull          |
| FTP or SFTP server                          | Pull a VOD asset from a server that supports FTP or SFTP.                                 | File input     | ftp:// or sftp://                 | Pull          |
| SCP server                                  | Pull a VOD asset from a server that supports SCP.                                         | File input     | scp://                            | Pull          |
| Amazon S3 bucket                            | Pull an HLS VOD asset from an Amazon S3 bucket, using a<br>secure or unsecure connection. | HLS file input | custom protocol s3:// or s3ssl:// | Pull          |
| HTTP or HTTPS server                        | Pull an HLS VOD asset from a server that supports HTTP or<br>HTTPS.                       | HLS file input | http:// or https://               | Pull          |
