# Allowed Domains

For WorkSpaces Pools users to access WorkSpaces, you must allow various domains on the
network from which users initiate access to the WorkSpaces. For more information, see
[IP address and port requirements for
WorkSpaces Personal](workspaces-port-requirements.md "workspaces-port-requirements.md"). Note that the page specifies
that it applies to WorkSpaces Personal but it also applies to WorkSpaces Pools.

###### Note

If your S3 bucket has a “.” character in the name, the domain used is
`https://s3.`<aws-region>`.amazonaws.com`.
If your S3 bucket does not have a “.” character in the name, the domain used is
`https://`<bucket-name>`.s3.`<aws-region>`.amazonaws.com`.
