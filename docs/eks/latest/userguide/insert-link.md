**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Insert a link

AsciiDoc supports multiple types of links. Using the right link type is important so the link works properly in different environments.

## Link to a page or section in the EKS User Guide

Use cross references (xref) to link between pages or sections within the same documentation site, such as the EKS User Guide. They automatically update if the target section moves or is renamed.

### Use page title as link text

For most cases when linking to another ID in this user guide, use the following approach to have the link text automatically update to the latest title as needed.

```
For more information, see <<page-or-section-id>>.
```

### Define custom link text

For cases where you must have custom link text, use the following format.

```
Here's an example of a <<page-or-section-id,link with custom text>>.
```

## Link to another guide in the AWS Docs

1. Find the link to the AWS documentation page.
2. Remove the `https://docs.aws.amazon.com/` prefix, keeping only the path. The path should start with a letter.
3. Create a link as shown below:

```
link:AmazonS3/latest/userguide/create-bucket-overview.html[Create a bucket, type="documentation"]
```

## Link to an external webpage

This format creates a standard link out to a page not hosted by Amazon. For example, use this for GitHub links.

```
https://example.com[Link text]
```

###### Note

We have an allowlist for external domains. The allowlist is at `vale/styles/EksDocs/ExternalDomains.yml`
