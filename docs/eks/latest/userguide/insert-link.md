

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Insert a link
<a name="insert-link"></a>

AsciiDoc supports multiple types of links. Using the right link type is important so the link works properly in different environments.

## Link to a page or section in the EKS User Guide
<a name="_link_to_a_page_or_section_in_the_eks_user_guide"></a>

Use cross references (xref) to link between pages or sections within the same documentation site, such as the EKS User Guide. They automatically update if the target section moves or is renamed.

### Use page title as link text
<a name="_use_page_title_as_link_text"></a>

For most cases when linking to another ID in this user guide, use the following approach to have the link text automatically update to the latest title as needed.

```
For more information, see <<page-or-section-id>>.
```

### Define custom link text
<a name="_define_custom_link_text"></a>

For cases where you must have custom link text, use the following format.

```
Here's an example of a <<page-or-section-id,link with custom text>>.
```

## Link to another guide in the AWS Docs
<a name="link_to_another_guide_in_the_shared_aws_docs"></a>

1. Find the link to the AWS documentation page.

1. Remove the `https://docs.aws.amazon.com/` prefix, keeping only the path. The path should start with a letter.

1. Create a link as shown below:

```
link:AmazonS3/latest/userguide/create-bucket-overview.html[Create a bucket, type="documentation"]
```

## Link to an external webpage
<a name="_link_to_an_external_webpage"></a>

This format creates a standard link out to a page not hosted by Amazon. For example, use this for GitHub links.

```
https://example.com[Link text]
```

**Note**  
We have an allowlist for external domains. The allowlist is at `vale/styles/EksDocs/ExternalDomains.yml` 