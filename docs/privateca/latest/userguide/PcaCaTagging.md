# Add tags for your private CA

Tags are words or phrases that act as metadata for identifying and organizing AWS
resources. Each tag consists of a **key** and a **value**. You can use the AWS Private CA console, AWS Command Line Interface (AWS CLI),
or the PCA API to add, view, or remove tags for private CAs.

You can add or remove custom tags for your private CA at any time. For example, you
could tag private CAs with key-value pairs like `Environment=Prod` or
`Environment=Beta` to identify which environment the CA is intended for.
For more information, see [Create a Private CA](create-CA.md "create-CA.md").

###### Note

To attach tags to a private CA during the creation procedure, a CA administrator must
first associate an inline IAM policy with the `CreateCertificateAuthority` action and explicitly allow
tagging. For more information, see [Tag-on-create: Attaching tags to a CA at the
time of creation](auth-InlinePolicies.md#tag-on-create "auth-InlinePolicies.md#tag-on-create").

Other AWS resources also support tagging. You can assign the same tag to different
resources to indicate that those resources are related. For example, you can assign a
tag such as `Website=example.com` to your CA, the ELB load balancer, and
other related resources. For more information on tagging AWS resources, see [Tagging
your Amazon EC2 Resources](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md") in the [Amazon EC2 User Guide](../../../ec2/index.md#lang/en_us "../../../ec2/index.md#lang/en_us").

The following basic restrictions apply to AWS Private CA tags:

- The maximum number of tags per private CA is 50.
- The maximum length of a tag key is 128 characters.
- The maximum length of a tag value is 256 characters.
- The tag key and value can contain the following characters: A-Z, a-z, and
  .:+=@\_%-(hyphen).
- Tag keys and values are case-sensitive.
- The `aws:` and `rds:` prefixes are reserved for AWS
  use; you cannot add, edit, or delete tags whose key begins with
  `aws:` or `rds:`. Default tags that begin with
  `aws:` and `rds:` do not count against your
  tags-per-resource quota.
- If you plan to use your tagging schema across multiple services and resources,
  remember that other services might have different restrictions for allowed
  characters. Refer to the documentation for that service.
- AWS Private CA tags are not available for use in the [Resource Groups
  and Tag Editor](https://aws.amazon.com/blogs/aws/resource-groups-and-tagging/ "https://aws.amazon.com/blogs/aws/resource-groups-and-tagging/") in the AWS Management Console.
  You can tag a private CA from the [AWS Private CA
  Console](https://console.aws.amazon.com/acm-pca "https://console.aws.amazon.com/acm-pca"), the [AWS Command Line Interface (AWS CLI)](../../../cli/latest/reference.md "../../../cli/latest/reference.md"), or the
  [AWS Private CA API](../APIReference.md "../APIReference.md").

###### To tag a private CA (console)

1. Sign in to your AWS account and open the AWS Private CA console at [https://console.aws.amazon.com/acm-pca/home](https://console.aws.amazon.com/acm-pca/home "https://console.aws.amazon.com/acm-pca/home").
2. On the **Private certificate authorities page**, choose your
   private CA from the list.
3. In the details area below the list, choose the **Tags** tab.
   A list of existing tags is displayed.
4. Choose **Manage tags**.
5. Choose **Add new tag**.
6. Type a key and value pair.
7. Choose **Save**.

###### To tag a private CA (AWS CLI)

Use the [tag-certificate-authority](../../../cli/latest/reference/acm-pca/tag-certificate-authority.md "../../../cli/latest/reference/acm-pca/tag-certificate-authority.md") command to add tags to your private CA.

```
`$` `aws acm-pca tag-certificate-authority \
 --certificate-authority-arn arn:aws:acm-pca:`region`:`account`:certificate-authority/`CA_ID` \
 --tags Key=`Admin`,Value=`Alice``
```

Use the [list-tags](../../../cli/latest/reference/acm-pca/list-tags.md "../../../cli/latest/reference/acm-pca/list-tags.md") command to list the
tags for a private CA.

```
`$` `aws acm-pca list-tags \
 --certificate-authority-arn arn:aws:acm-pca:`region`:`account`:certificate-authority/`CA_ID` \
 --max-results 10`
```

Use the [untag-certificate-authority](../../../cli/latest/reference/acm-pca/untag-certificate-authority.md "../../../cli/latest/reference/acm-pca/untag-certificate-authority.md") command to remove tags from a private CA.

```
`$` `aws acm-pca untag-certificate-authority \
 --certificate-authority-arn arn:aws:acm-pca:`aregion`:`account`:certificate-authority/`CA_ID` \
 --tags Key=`Purpose`,Value=`Website``
```
