# Retrieving the

findings for enhanced scans in Amazon ECR

You can retrieve the scan findings for the last completed enhanced image scan, and
then open the findings in Amazon Inspector to see more detail. The software vulnerabilities
that were discovered are listed by severity based on the Common Vulnerabilities and
Exposures (CVEs) database.

For troubleshooting details for some common issues when scanning images, see [Troubleshooting image scanning in
Amazon ECR](image-scanning-troubleshooting.md "image-scanning-troubleshooting.md").

AWS Management Console
Use the following steps to retrieve image scan findings using the
AWS Management Console.

###### To retrieve image scan findings

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/ "https://console.aws.amazon.com/ecr/").
2. From the navigation bar, choose the Region where your
   repository exists.
3. In the navigation pane, choose **Repositories**
   .
4. On the **Repositories** page, choose the
   repository that contains the image to retrieve the scan findings
   for.
5. On the **Images** page, under the **Image
   tag** column, select the image tag to retrieve the scan
   findings.
6. To view more details in the Amazon Inspector console, choose the
   vulnerability name in the **Name** column.

AWS CLI
Use the following AWS CLI command to retrieve image scan findings using
the AWS CLI. You can specify an image using the `imageTag` or `imageDigest`, both of which can be obtained using the [list-images](../../../cli/latest/reference/ecr/list-images.md "../../../cli/latest/reference/ecr/list-images.md") CLI
command.

- [describe-image-scan-findings](../../../cli/latest/reference/ecr/describe-image-scan-findings.md "../../../cli/latest/reference/ecr/describe-image-scan-findings.md") (AWS CLI)

The following example uses an image tag.

```
`aws ecr describe-image-scan-findings \
 --repository-name `name` \
 --image-id imageTag=`tag_name` \
 --region `us-east-2``
```

The following example uses an image digest.

```
`aws ecr describe-image-scan-findings \
 --repository-name `name` \
 --image-id imageDigest=`sha256_hash` \
 --region `us-east-2``
```
