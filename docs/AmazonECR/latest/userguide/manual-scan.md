# Manually scanning an image for OS vulnerabilities in

Amazon ECR

If your repositories aren't configured to **scan on push**, you
can manually start image scans. An image can be scanned once per 24 hours. The 24
hours includes the initial scan on push, if configured, and any manual scans.

For troubleshooting details for some common issues when scanning images, see [Troubleshooting image scanning in
Amazon ECR](image-scanning-troubleshooting.md "image-scanning-troubleshooting.md").

AWS Management Console
Use the following steps to start a manual image scan using the
AWS Management Console.

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/private-registry/repositories](https://console.aws.amazon.com/ecr/private-registry/repositories "https://console.aws.amazon.com/ecr/private-registry/repositories")
2. From the navigation bar, choose the Region to create your
   repository in.
3. In the navigation pane, choose
   **Repositories**.
4. On the **Repositories** page, choose the
   repository that contains the image to scan.
5. On the **Images** page, select the image to
   scan and then choose **Scan**.

AWS CLI

- [start-image-scan](../../../cli/latest/reference/ecr/start-image-scan.md "../../../cli/latest/reference/ecr/start-image-scan.md") (AWS CLI)

The following example uses an image tag.

```
`aws ecr start-image-scan --repository-name `name` --image-id imageTag=`tag_name` --region `us-east-2``
```

The following example uses an image digest.

```
`aws ecr start-image-scan --repository-name `name` --image-id imageDigest=`sha256_hash` --region `us-east-2``
```

AWS Tools for Windows PowerShell

- [Get-ECRImageScanFinding](../../../powershell/latest/reference/items/Start-ECRImageScan.md "../../../powershell/latest/reference/items/Start-ECRImageScan.md") (AWS Tools for Windows PowerShell)

The following example uses an image tag.

```
`Start-ECRImageScan -RepositoryName `name` -ImageId_ImageTag `tag_name` -Region `us-east-2` -Force`
```

The following example uses an image digest.

```
`Start-ECRImageScan -RepositoryName `name` -ImageId_ImageDigest `sha256_hash` -Region `us-east-2` -Force`
```
