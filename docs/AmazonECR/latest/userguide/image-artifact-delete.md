# Deleting signatures and other artifacts from an Amazon ECR private repository

You can use the ORAS client to list and delete signatures and other reference type
artifacts from an Amazon ECR private repository. Deleting signatures and other reference
artifacts is similar to how an image is deleted (see [Deleting an image in Amazon ECR](delete_image.md "delete_image.md")). Here is how to list artifacts and delete
signatures:

###### To manage image artifacts using the ORAS CLI

1. Install and configure the ORAS client.

For information about installing and configuring the ORAS client, see [Installation](https://oras.land/docs/installation "https://oras.land/docs/installation") in the ORAS
documentation. 2. To list available artifacts for an Amazon ECR image, use `oras
 discover`, followed by an image name:

```
oras discover 111222333444.dkr.ecr.us-east-1.amazonaws.com/oci:helloworld
```

The output should look similar to this:

```

111222333444.dkr.ecr.us-east-1.amazonaws.com/oci@sha256:88c0c54329bfdc1d94d6f58cd3fcb1226d46f58670f44a8c689cb3c9b37b6925
└── application/vnd.cncf.notary.signature
    ├── sha256:387c10c1598ee18aae81dcfc86d0d06d116e46461d1c3cda8927e69c48108c42
    └── sha256:6527bcec87adf1d55460666183b9d0968b3cd4e4bc34602d485206a219851171
```

3. To delete a signature using the ORAS CLI, given the previous example, run the
   following command:

```
oras manifest delete 111222333444.dkr.ecr.us-east-1.amazonaws.com/oci@sha256:387c10c1598ee18aae81dcfc86d0d06d116e46461d1c3cda8927e69c48108c42

```

The output should look similar to this:

```

Are you sure you want to delete the manifest "111222333444.dkr.ecr.us-east-1.amazonaws.com/oci@sha256:387c10c1598ee18aae81dcfc86d0d06d116e46461d1c3cda8927e69c48108c42" and all tags associated with it? [y/N] y
```

4. Press `y`. The artifact should be deleted.

###### To troubleshoot artifact deletion

If a signature deletion, such as the one just shown, should fail, output similar
to the following appears.

```

Error response from registry: failed to delete 111222333444.dkr.ecr.us-east-1.amazonaws.com/oci@sha256:387c10c1598ee18aae81dcfc86d0d06d116e46461d1c3cda8927e69c48108c42:
unsupported: Requested image referenced by manifest list: [sha256:005e2c97a6373e483799fa4ff29ac64a42dd10f08efcc166d6775f9b74943b5b]
```

This failure can happen when deleting an image pushed before the OCI 1.1 launch.
As noted in the error, you must delete the manifest referencing the image before you
can delete the image as follows:

1. To delete the manifest associated with the signature you want to delete,
   type:

```
 oras manifest delete 111222333444.dkr.ecr.us-east-1.amazonaws.com/oci@sha256:005e2c97a6373e483799fa4ff29ac64a42dd10f08efcc166d6775f9b74943b5b

```

The output should look similar to this:

```

Are you sure you want to delete the manifest "sha256:005e2c97a6373e483799fa4ff29ac64a42dd10f08efcc166d6775f9b74943b5b" and all tags associated with it? [y/N] y

```

2. Press `y`. The manifest should be deleted.
3. With the manifest gone, you can delete the signature:

```
 oras manifest delete 111222333444.dkr.ecr.us-east-1.amazonaws.com/oci@sha256:387c10c1598ee18aae81dcfc86d0d06d116e46461d1c3cda8927e69c48108c42

```

The output should look similar to this. Press `y`.

```

Are you sure you want to delete the manifest "sha256:387c10c1598ee18aae81dcfc86d0d06d116e46461d1c3cda8927e69c48108c42" and all tags associated with it? [y/N] y
Deleted [registry] 111222333444.dkr.ecr.us-east-1.amazonaws.com/oci@sha256:387c10c1598ee18aae81dcfc86d0d06d116e46461d1c3cda8927e69c48108c42
```

4. To see that the signature was deleted, type:

```
oras discover 111222333444.dkr.ecr.us-east-1.amazonaws.com/oci:helloworld

```

The output should look similar to this:

```

111222333444.dkr.ecr.us-east-1.amazonaws.com/oci@sha256:88c0c54329bfdc1d94d6f58cd3fcb1226d46f58670f44a8c689cb3c9b37b6925
└── application/vnd.cncf.notary.signature
    └── sha256:6527bcec87adf1d55460666183b9d0968b3cd4e4bc34602d485206a219851171
```
