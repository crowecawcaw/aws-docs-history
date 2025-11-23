# Retagging an image in Amazon ECR

With Docker Image Manifest V2 Schema 2 images, you can use the `--image-tag`
option of the **put-image** command to retag an existing image. You can
retag without pulling or pushing the image with Docker. For larger images, this process
saves a considerable amount of network bandwidth and time required to retag an image.

###### To retag an image with the AWS CLI

1. Use the **batch-get-image** command to get the image
   manifest for the image to retag and write it to a file. In this example,
   the manifest for an image with the tag, `latest`,
   in the repository, `amazonlinux`, is written to
   an environment variable named `MANIFEST`.

```
`MANIFEST=$(aws ecr batch-get-image --repository-name `amazonlinux` --image-ids imageTag=`latest` --output text --query 'images[].imageManifest')`
```

2. Use the `--image-tag` option of the **put-image**
   command to put the image manifest to Amazon ECR with a new tag. In this
   example, the image is tagged as `2017.03`.

###### Note

If the `--image-tag` option isn't available in your
version of the AWS CLI, upgrade to the latest version. For more
information, see [Installing the
AWS Command Line Interface](../../../cli/latest/userguide/install-cliv2.md "../../../cli/latest/userguide/install-cliv2.md") in the _AWS Command Line Interface User Guide_.

```
`aws ecr put-image --repository-name `amazonlinux` --image-tag `2017.03` --image-manifest "$MANIFEST"`
```

3. Verify that your new image tag is attached to your image. In the
   following output, the image has the tags `latest` and `2017.03`.

```
`aws ecr describe-images --repository-name `amazonlinux``
```

The output is as follows:

```
{
    "imageDetails": [
        {
            "imageSizeInBytes": 98755613,
            "imageDigest": "sha256:8d00af8f076eb15a33019c2a3e7f1f655375681c4e5be157a26EXAMPLE",
            "imageTags": [
                "latest",
                "2017.03"
            ],
            "registryId": "aws_account_id",
            "repositoryName": "amazonlinux",
            "imagePushedAt": 1499287667.0
        }
    ]
}
```

###### To retag an image with the AWS Tools for Windows PowerShell

1. Use the **Get-ECRImageBatch**
   **cmdlet**
   to obtain the description of the image to retag and write it to an
   environment variable. In this example, an image with the tag, `latest`, in the repository, `amazonlinux`,
   is written to the environment variable, `$Image`
   .

###### Note

If you don't have the **Get-ECRImageBatch**
**cmdlet** available on your system, see [Setting up the
AWS Tools for Windows PowerShell](../../../powershell/latest/userguide/pstools-getting-set-up.md "../../../powershell/latest/userguide/pstools-getting-set-up.md") in the _AWS Tools for PowerShell User Guide_.

```
`$Image = Get-ECRImageBatch -ImageId @{ imageTag="`latest`" } -RepositoryName `amazonlinux``
```

2. Write the manifest of the image to the `$Manifest`
   environment variable.

```
`$Manifest = $Image.Images[0].ImageManifest`
```

3. Use the `-ImageTag` option of the **Write-ECRImage**
   **cmdlet** to put the image manifest to Amazon ECR with a new tag. In
   this example, the image is tagged as `2017.09`.

```
`Write-ECRImage -RepositoryName `amazonlinux` -ImageManifest $Manifest -ImageTag `2017.09``
```

4. Verify that your new image tag is attached to your image. In the
   following output, the image has the tags `latest` and `2017.09`.

```
`Get-ECRImage -RepositoryName `amazonlinux``
```

The output is as follows:

```
ImageDigest                                                             ImageTag
-----------                                                             --------
sha256:359b948ea8866817e94765822787cd482279eed0c17bc674a7707f4256d5d497 latest
sha256:359b948ea8866817e94765822787cd482279eed0c17bc674a7707f4256d5d497 2017.09
```
