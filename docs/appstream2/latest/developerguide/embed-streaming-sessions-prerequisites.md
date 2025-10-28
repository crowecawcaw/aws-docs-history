# Prerequisites for Embedding Amazon AppStream 2.0 Streaming Sessions

To embed an AppStream 2.0 streaming session in a website, you must have the following:

- A configured AppStream 2.0 environment that includes an AppStream 2.0 image, fleet, and
  stack. For information about how to create these resources, see the following
  topics in the _AppStream 2.0 Administration Guide_:
  - [Tutorial: Create a Custom AppStream 2.0 Image by Using the
    AppStream 2.0 Console](tutorial-image-builder.md "tutorial-image-builder.md") or [Create Your Amazon AppStream 2.0 Image Programmatically by Using the Image Assistant CLI Operations](programmatically-create-image.md "programmatically-create-image.md")
  - [Create a Fleet in Amazon AppStream 2.0](set-up-stacks-fleets-create.md "set-up-stacks-fleets-create.md")
  - [Create a Stack in Amazon AppStream 2.0](set-up-stacks-fleets-install.md "set-up-stacks-fleets-install.md")

- A streaming URL for user authentication. SAML 2.0 and AppStream 2.0 user pools are
  currently not supported as authentication methods for embedded AppStream 2.0 streaming
  sessions.
- Optionally, you can use custom domains for embedded AppStream 2.0 streaming sessions. You can use custom domains so that your own company URL displays for users rather than an AppStream 2.0 URL. Custom domains are required if your users have web browsers that block third-party cookies.

###### Note

You can configure custom domains by using Amazon CloudFront. For information, see [Using Custom Domains with AppStream 2.0](https://aws.amazon.com/blogs/desktop-and-application-streaming/using-custom-domains-with-amazon-appstream-2-0/ "https://aws.amazon.com/blogs/desktop-and-application-streaming/using-custom-domains-with-amazon-appstream-2-0/").

When you use a custom domain, you must:

    + Create a streaming URL that uses the same domain.
    + Add `appstream-custom-url-domain` to the header of the
     webpage that will host the embedded AppStream 2.0 streaming sessions. For the header value, use the domain that your reverse proxy displays to users. For more information, see [Configuration Requirements for Using Custom Domains](create-streaming-url-user-authentication.md#configuration-requirements-custom-domains "create-streaming-url-user-authentication.md#configuration-requirements-custom-domains").
