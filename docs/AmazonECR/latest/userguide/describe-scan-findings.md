# Retrieving the findings for basic scans in

Amazon ECR

You can retrieve the scan findings for the last completed basic image scan. The
software vulnerabilities that were discovered are listed by severity based on the
Common Vulnerabilities and Exposures (CVEs) database.

For troubleshooting details for some common issues when scanning images, see [Troubleshooting image scanning in
Amazon ECR](image-scanning-troubleshooting.md "image-scanning-troubleshooting.md").

AWS Management Console
Use the following steps to retrieve image scan findings using the
AWS Management Console.

###### To retrieve image scan findings

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/private-registry/repositories](https://console.aws.amazon.com/ecr/private-registry/repositories "https://console.aws.amazon.com/ecr/private-registry/repositories")
2. From the navigation bar, choose the Region to create your
   repository in.
3. In the navigation pane, choose
   **Repositories**.
4. On the **Repositories** page, choose the
   repository that contains the image to retrieve the scan findings
   for.
5. On the **Images** page, under the
   **Image tag** column, select the image tag
   to retrieve the scan findings.

AWS CLI
Use the following AWS CLI command to retrieve image scan findings using
the AWS CLI. You can specify an image using the `imageTag` or
`imageDigest`, both of which can be obtained using the
[list-images](../../../cli/latest/reference/ecr/list-images.md "../../../cli/latest/reference/ecr/list-images.md")
CLI command.

- [describe-image-scan-findings](../../../cli/latest/reference/ecr/describe-image-scan-findings.md "../../../cli/latest/reference/ecr/describe-image-scan-findings.md") (AWS CLI)

The following example uses an image tag.

```
`aws ecr describe-image-scan-findings --repository-name `name` --image-id imageTag=`tag_name` --region `us-east-2``
```

The following example uses an image digest.

```
`aws ecr describe-image-scan-findings --repository-name `name` --image-id imageDigest=`sha256_hash` --region `us-east-2``
```

AWS Tools for Windows PowerShell

- [Get-ECRImageScanFinding](../../../powershell/latest/reference/items/Get-ECRImageScanFinding.md "../../../powershell/latest/reference/items/Get-ECRImageScanFinding.md") (AWS Tools for Windows PowerShell)

The following example uses an image tag.

```
`Get-ECRImageScanFinding -RepositoryName `name` -ImageId_ImageTag `tag_name` -Region `us-east-2``
```

The following example uses an image digest.

```
`Get-ECRImageScanFinding -RepositoryName `name` -ImageId_ImageDigest `sha256_hash` -Region `us-east-2``
```
