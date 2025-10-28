# Configure logical directories examples

In this example, we create a user and assign two logical directories. The following
command creates a new user (for an existing Transfer Family server) with logical directories
`pics` and `doc`.

```
aws transfer create-user \
    --user-name marymajor \
    --server-id s-11112222333344445 \
    --role arn:aws:iam::1234abcd5678:role/marymajor-role \
    --home-directory-type LOGICAL \
    --home-directory-mappings "[{\"Entry\":\"/pics\", \"Target\":\"/amzn-s3-demo-bucket1/pics\"}, {\"Entry\":\"/doc\", \"Target\":\"/amzn-s3-demo-bucket2/test/mydocs\"}]" \
    --ssh-public-key-body file://~/.ssh/id_rsa.pub
```

If `marymajor` is an existing user and her home directory type is
`PATH`, you can change it to `LOGICAL` with a similar command
as the previous one.

```
aws transfer update-user \
    --user-name marymajor \
    --server-id s-11112222333344445 \
    --role arn:aws:iam::1234abcd5678:role/marymajor-role \
    --home-directory-type LOGICAL \
    --home-directory-mappings "[{\"Entry\":\"/pics\", \"Target\":\"/amzn-s3-demo-bucket1/pics\"}, {\"Entry\":\"/doc\", \"Target\":\"/amzn-s3-demo-bucket2/test/mydocs\"}]"
```

Note the following:

- If the directories `/amzn-s3-demo-bucket1/pics` and
  `/amzn-s3-demo-bucket2/test/mydocs` don't already exist,
  the user (or an administrator) needs to create them.

###### Note

These directories are created automatically by the Transfer Family server if you have
configured optimized directories.

- When `marymajor` connects to the server, and runs the
  `ls -l` command, Mary sees the following:

```
drwxr--r--   1        -        -        0 Mar 17 15:42 doc
drwxr--r--   1        -        -        0 Mar 17 16:04 pics
```

- `marymajor` cannot create any files or directories at
  this level. However, within `pics` and `doc`, she can add
  sub-directories.
- Files that Mary adds to `pics` and `doc`
  are added to Amazon S3 paths `/amzn-s3-demo-bucket1/pics` and
  `/amzn-s3-demo-bucket2/test/mydocs` respectively.
- In this example, we specify two different buckets to illustrate that
  possibility. However, you can use the same bucket for several or all of the
  logical directories that you specify for the user.
  This example provides an alternate configuration for a logical home path.

```
aws transfer create-user \
    --user-name marymajor \
    --server-id s-11112222333344445 \
    --role arn:aws:iam::1234abcd5678:role/marymajor-role \
    --home-directory-type LOGICAL \
    --home-directory /home/marymajor \
    --home-directory-mappings "[{\"Entry\":\"/home/marymajor/pics\", \"Target\":\"/amzn-s3-demo-bucket1/pics\"}, {\"Entry\":\"/home/marymajor/doc\", \"Target\":\"/amzn-s3-demo-bucket2/test/mydocs\"}]" \
    --ssh-public-key-body file://~/.ssh/id_rsa.pub
```

Note the following:

- The mappings provide for a common path, `/home/marymajor`, which is
  the first part of the two logical paths. Files then can be added to the
  `pics` and `doc` folders.
- As in the previous example, the home directory, `/home/marymajor`,
  is read-only.
