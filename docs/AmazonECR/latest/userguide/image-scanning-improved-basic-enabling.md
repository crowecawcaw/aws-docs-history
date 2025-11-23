# Switching to the improved

basic
scanning for images in Amazon ECR

Amazon ECR provides enhanced container image scanning capabilities through improved
version of basic scanning that uses AWS native technology. This feature helps you
identify software vulnerabilities in your container images. The following procedure
helps you to switch to this improved version of basic scanning if you are using
previous version of basic scanning that uses `CLAIR` technology.

###### Important

For new users, your registries are automatically configured to use the `AWS_NATIVE` scanning technology upon creation. There is no action for you
to take. Amazon ECR doesn't recommend reverting to the previous scanning technology `CLAIR`,which has been deprecates. See [Clair Deprecation](image-scanning-basic.md#clair-deprecation "image-scanning-basic.md#clair-deprecation") for details

AWS Management Console

###### To turn on improved basic scanning for your private

registry

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/private-registry/repositories](https://console.aws.amazon.com/ecr/private-registry/repositories "https://console.aws.amazon.com/ecr/private-registry/repositories")
2. From the navigation bar, choose the Region to set the scanning
   configuration for.
3. In the navigation pane, choose **Private
   registry**, **Features &
   Settings**, **Scanning**.
4. On the **Scanning configuration** page,
   choose **Opt in (recommended)** to select
   improved version of basic scanning.
5. By default all of your repositories are set for **Manual** scanning. You can optionally configure scan on
   push by specifying **Scan on push
   filters**. You can set scan on push for all
   repositories or individual repositories. For more information,
   see [Filters to choose which repositories are
   scanned in Amazon ECR](image-scanning-filters.md "image-scanning-filters.md").

AWS CLI
Amazon ECR has basic scanning enabled for all private registries. Use the
following commands below to view your current basic scan type and to
change your basic scan type.

- To retrieve the basic scan type version you are currently
  using.

```
`aws ecr get-account-setting --name BASIC_SCAN_TYPE_VERSION`
```

The parameter name is a required field. If you don't provide
the name you will receive the following error:

```
 `aws: error: the following arguments are required: --name`
```

To change your basic scan type version from `CLAIR`
to `AWS_NATIVE`. Once you change your basic scan type
version from `CLAIR` to `AWS_NATIVE` it's
not recommended that you revert back to `CLAIR`.

```
`aws ecr put-account-setting --name BASIC_SCAN_TYPE_VERSION --value `value``
```
