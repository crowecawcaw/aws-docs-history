# Configuring enhanced scanning for

images in Amazon ECR

Configure enhanced scanning per Region for your private registry.

Verify that you have the proper IAM permissions to configure enhanced scanning.
For information, see [IAM permissions required for
enhanced scanning in Amazon ECR](image-scanning-enhanced-iam.md "image-scanning-enhanced-iam.md").

AWS Management Console

###### To turn on enhanced scanning for your private registry

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories "https://console.aws.amazon.com/ecr/repositories").
2. From the navigation bar, choose the Region to set the scanning
   configuration for.
3. In the navigation pane, choose **Private
   registry**, and then choose
   **Settings**.
4. On the **Scanning configuration** page, for
   **Scan type** choose **Enhanced
   scanning**.

By default, when **Enhanced scanning** is
selected, all of your repositories are continuously
scanned. 5. To choose specific repositories to continuously scan, clear
the **Continuously scan all repositories** box,
and then define your filters:

###### Important

Filters with no wildcard will match all repository names
that contain the filter. Filters with wildcards
(`*`) match on a repository name where the
wildcard replaces zero or more characters in the repository
name. To see examples of how filters behave, see [Filter wildcards](image-scanning-filters.md#image-scanning-filters-wildcards "image-scanning-filters.md#image-scanning-filters-wildcards").

    1. Enter a filter based on repository names, and then
     choose **Add filter**.
    2. Decide which repositories to scan when an image is
     pushed:




    	* To scan all repositories on push, select
    	 **Scan on push all
    	 repositories**.
    	* To choose specific repositories to scan on
    	 push, enter a filter based on repository names,
    	 and then choose **Add
    	 filter**.

6. Choose **Save**.
7. Repeat these steps in each Region in which you want to turn on
   enhanced scanning.

AWS CLI
Use the following AWS CLI command to turn on enhanced scanning for your
private registry using the AWS CLI. You can specify scan filters using the
`rules` object.

- [put-registry-scanning-configuration](../../../cli/latest/reference/ecr/put-registry-scanning-configuration.md "../../../cli/latest/reference/ecr/put-registry-scanning-configuration.md") (AWS CLI)

The following example turns on enhanced scanning for your
private registry. By default, when no `rules` are
specified, Amazon ECR sets the scanning configuration to continuous
scanning for all repositories.

```
`aws ecr put-registry-scanning-configuration \
 --scan-type `ENHANCED` \
 --region `us-east-2``
```

The following example turns on enhanced scanning for your
private registry and specifies a scan filter. The scan filter in
the example turns on continuous scanning for all repositories
with `prod` in its name.

```
`aws ecr put-registry-scanning-configuration \
 --scan-type `ENHANCED` \
 --rules '[{"repositoryFilters" : [{"filter":"`prod`","filterType" : "WILDCARD"}],"scanFrequency" : "`CONTINUOUS_SCAN`"}]' \
 --region `us-east-2``
```

The following example turns on enhanced scanning for your
private registry and specifies multiple scan filters. The scan
filters in the example turns on continuous scanning for all
repositories with `prod` in its name and turns on
scan on push only for all other repositories.

```
`aws ecr put-registry-scanning-configuration \
 --scan-type `ENHANCED` \
 --rules '[{"repositoryFilters" : [{"filter":"`prod`","filterType" : "WILDCARD"}],"scanFrequency" : "`CONTINUOUS_SCAN`"},{"repositoryFilters" : [{"filter":"`*`","filterType" : "WILDCARD"}],"scanFrequency" : "`SCAN_ON_PUSH`"}]' \
 --region `us-west-2``
```
