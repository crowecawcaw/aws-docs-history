# Prerequisites for Embedding Amazon WorkSpaces Applications Streaming Sessions

To embed an WorkSpaces Applications streaming session in a website, you must have the following:

- A configured WorkSpaces Applications environment that includes an WorkSpaces Applications image, fleet, and
  stack. For information about how to create these resources, see the following
  topics in the _WorkSpaces Applications Administration Guide_:
  - [Tutorial: Create a Custom WorkSpaces Applications Image by Using the
    WorkSpaces Applications Console](tutorial-image-builder.md "tutorial-image-builder.md") or [Create Your Amazon WorkSpaces Applications Image Programmatically by Using the Image Assistant CLI Operations](programmatically-create-image.md "programmatically-create-image.md")
  - [Create a Fleet in Amazon WorkSpaces Applications](set-up-stacks-fleets-create.md "set-up-stacks-fleets-create.md")
  - [Create a Stack in Amazon WorkSpaces Applications](set-up-stacks-fleets-install.md "set-up-stacks-fleets-install.md")

- A streaming URL for user authentication. SAML 2.0 and WorkSpaces Applications user pools are
  currently not supported as authentication methods for embedded WorkSpaces Applications streaming
  sessions.
- Optionally, you can use custom domains for embedded WorkSpaces Applications streaming sessions. You can use custom domains so that your own company URL displays for users rather than an WorkSpaces Applications URL. Custom domains are required if your users have web browsers that block third-party cookies.

###### Note

You can configure custom domains by using Amazon CloudFront. For information, see [Using Custom Domains with WorkSpaces Applications](https://aws.amazon.com/blogs/desktop-and-application-streaming/using-custom-domains-with-amazon-appstream-2-0/ "https://aws.amazon.com/blogs/desktop-and-application-streaming/using-custom-domains-with-amazon-appstream-2-0/").

When you use a custom domain, you must:

    + Create a streaming URL that uses the same domain.
    + Add `appstream-custom-url-domain` to the header of the
     webpage that will host the embedded WorkSpaces Applications streaming sessions. For the header value, use the domain that your reverse proxy displays to users. For more information, see [Configuration Requirements for Using Custom Domains](create-streaming-url-user-authentication.md#configuration-requirements-custom-domains "create-streaming-url-user-authentication.md#configuration-requirements-custom-domains").
