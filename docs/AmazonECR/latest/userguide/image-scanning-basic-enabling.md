# Configuring basic scanning for

images in Amazon ECR

By default, Amazon ECR turns on basic scanning for all private registries. As a result,
unless you've changed the scanning settings on your private registry there is no
need to turn on basic scanning.

You can use the following steps to define one or more scan on push filters.

###### To turn on basic scanning for your private registry

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/private-registry/repositories](https://console.aws.amazon.com/ecr/private-registry/repositories "https://console.aws.amazon.com/ecr/private-registry/repositories")
2. From the navigation bar, choose the Region to set the scanning
   configuration for.
3. In the navigation pane, choose **Private registry**, **Scanning**.
4. On the **Scanning configuration** page, For **Scan
   type** choose **Basic
   scanning**.
5. By default all of your repositories are set for **Manual**
   scanning. You can optionally configure scan on push by specifying **Scan
   on push filters**. You can set scan on push for all repositories or
   individual repositories. For more information, see [Filters to choose which repositories are
   scanned in Amazon ECR](image-scanning-filters.md "image-scanning-filters.md").

###### Note

If scan on push is enabled for a repository, scans are also done on
images that are restored after being archived. No old scans will be
available from the restored image.
