End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Allowing Amazon CloudFront to

access your AWS Elemental MediaStore container

You can use Amazon CloudFront to serve the content that you store in a container in
AWS Elemental MediaStore. You can do so in one of the following ways:

- [Using
  Origin Access Control (OAC)](#cdns-allowing-cloudfront-to-access-mediastore-using-oac "#cdns-allowing-cloudfront-to-access-mediastore-using-oac") -
  (Recommended) Use this option if your AWS Region supports the OAC feature of
  CloudFront.
- [Using Shared Secrets](#cdns-allowing-cloudfront-to-access-mediastore-using-shared-secrets "#cdns-allowing-cloudfront-to-access-mediastore-using-shared-secrets") - Use this option if your AWS Region does not support the OAC feature of
  CloudFront.

## Using

Origin Access Control (OAC)

You can use the Origin Access Control (OAC) feature of Amazon CloudFront to secure
AWS Elemental MediaStore origins with improved security. You can enable [AWS Signature Version 4 (SigV4)](../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md "../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md") on CloudFront requests for MediaStore
origins and set when and if CloudFront should sign the requests. You can access the OAC
feature of CloudFront through the console, APIs, SDK, or CLI, and there are no additional
fees for its use.

For more information about using the OAC feature with MediaStore, see [Restricting access to a MediaStore origin](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-mediastore.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-mediastore.md") in the [Amazon CloudFront Developer Guide](../../../AmazonCloudFront/latest/DeveloperGuide.md "../../../AmazonCloudFront/latest/DeveloperGuide.md").

## Using Shared Secrets

If your AWS Region does not support the OAC feature of Amazon CloudFront, you can attach
a policy to your AWS Elemental MediaStore container that grants read access or greater to
CloudFront.

###### Note

We recommend using the OAC feature if your AWS Region supports it. The
following procedures require you to configure MediaStore and CloudFront with shared
secrets in order to restrict access to MediaStore containers. To follow best
security practices, this manual configuration requires periodic rotation of
secrets. With OAC on MediaStore origins, you can instruct CloudFront to sign
requests using SigV4 and forward them to MediaStore for signature matching,
eliminating the need to use and rotate secrets. This ensures that requests are
automatically verified before media content is served, making the delivery of
media content through MediaStore and CloudFront simpler and more secure.

###### To allow CloudFront to access your container (console)

1. Open the MediaStore console at [https://console.aws.amazon.com/mediastore/](https://console.aws.amazon.com/mediastore/ "https://console.aws.amazon.com/mediastore/").
2. On the **Containers** page, choose the container
   name.

The container details page appears. 3. In the **Container policy** section, attach a policy that
grants read access or greater to Amazon CloudFront.

The following example policy, which is similar to the example policy
for [Public Read Access
over HTTPS](policies-examples-public-https.md "policies-examples-public-https.md"), matches these requirements because it allows
`GetObject` and `DescribeObject` commands from
anyone who submits requests to your domain through HTTPS. Furthermore,
the following example policy better secures your workflow because it
allows CloudFront access to MediaStore objects only when the request occurs
over an HTTPS connection and contains the correct Referer header. 4. In the **Container CORS policy** section, assign a policy
that allows the appropriate access level.

###### Note

A [CORS policy](cors-policy.md "cors-policy.md") is necessary only if
you want to provide access to a browser-based player. 5. Make note of the following details:

    * The data endpoint that is assigned to your container. You can find
     this information in the **Info** section of the
     **Containers** page. In CloudFront, the data endpoint
     is referred to as the *origin domain
     name*.
    * The folder structure in the container where the objects are
     stored. In CloudFront, this is referred to as the *origin
     path*. Note that this setting is optional. For more
     information about origin paths, see the [Amazon CloudFront Developer Guide](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#DownloadDistValuesOriginPath "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#DownloadDistValuesOriginPath").

6. In CloudFront, create a distribution that is [configured to serve content from AWS Elemental MediaStore](../../../AmazonCloudFront/latest/DeveloperGuide/live-streaming.md#video-streaming-mediastore "../../../AmazonCloudFront/latest/DeveloperGuide/live-streaming.md#video-streaming-mediastore"). You will
   need the information that you collected in the preceding step.

After attaching the policy to your MediaStore containers, you must configure
CloudFront to use only HTTPS connections for origin requests, and also add a custom header
with the correct secret value.

###### To configure CloudFront to access your container via an HTTPS connection with a

secret value for the Referer header (console)

1. Open the CloudFront console.
2. On the **Origins** page, choose your MediaStore
   origin.
3. Choose **Edit**.
4. Choose **HTTPS only** for the protocol.
5. In the **Add custom header** section, choose
   **Add header**.
6. For the **Name**, choose **Referer**.
   For the **value**, use the same
   `<secretValue>` string that you used in your
   container policy.
7. Choose **Save** and let the changes deploy.
