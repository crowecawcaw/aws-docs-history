# Enhance your AWS Marketplace product with promotional media

As an AWS Marketplace seller, you can help customers better discover and evaluate your product
by enhancing your product listing with promotional media. Promotional media are videos and
images that are shown prominently on your product page and provides customers an easy way of
learning about your product. The following sections provide best practices for promotional
media and tips for adding and managing promotional media in the AWS Marketplace Management
Portal (AMMP).

###### Topics

- [Best practices for promotional media](#best-practices-promotional-media "#best-practices-promotional-media")
- [Tips to add and manage promotional media](#promotional-media-tips "#promotional-media-tips")

## Best practices for promotional media

Up to five videos and 10 images are supported. Each promotional media item should
include a required title and an optional description. Descriptions are used as alt text
for media and are highly recommended to improve visual accessibility and search engine
optimization.

###### Note

You must have the appropriate rights and permissions to upload or add any
promotional media. Media that are added to your product will be made publicly available
to all users browsing AWS Marketplace.

**Videos**

This asset type provides you the opportunity to introduce your product and company
through a concise overview. You can also include content such as customer interviews,
quotes, relevant benefits, and data points. Additionally, videos are a great way to showcase
your product through a recorded demo or walk-through, especially for key features or use cases.
We recommend videos to be 2-5 minutes in duration, as shorter videos are more impactful.

Specifications:

- We support direct upload of videos through AMMP or through publicly accessible S3
  links.
- Recommended video resolution is 1080p (1920x1080 pixels) with a preferred 16:9 aspect ratio.
- Video format must be .mp4 with max file size of 50MB.
- (Optional) A cover image can be added in place of the auto-generated cover.
  - Cover image should have a resolution of 500x281 pixels (16:9 aspect ratio).
  - Image format must be .png (preferred), .jpg, or .svg without transparency.

###### Note

Externally hosted videos are not directly supported. Public S3 links will be cached by AWS Marketplace
during addition and any post-addition changes will not reflect until the media is added again.

YouTube videos are supported with limited capability:

- If the product video URL field (separate field from promotional media) includes a direct link to a YouTube video,
  the video will be directly embedded as the last promotional media item if embedding is enabled for the video.
- Only one product video URL is supported (i.e. only one YouTube video) and re-ordering of the YouTube
  embedded media is not supported.

**Images**

This asset type provides you an opportunity to promote your product through screenshots and key concept call-outs. Images are ideal
to explain complex product features through concise diagrams or flow-charts. Additionally, images can be used to explain pricing tiers
and groupings that are not addressable with pricing dimension descriptions.

Specifications:

- We support direct upload of images through AMMP or through publicly accessible
  S3 links.
- Recommended image resolution is 780x439 pixels with a preferred 16:9 aspect ratio. Maximum of
  3480x3480 pixels.
- Image format must be .png (preferred), .jpg, or .svg without transparency.
- Thumbnails are auto-generated from original source images.

## Tips to add and manage promotional media

**Add media**

- Promotional media can be added by logging into the [AWS Marketplace Management
  Portal](https://aws.amazon.com/marketplace/management/ "https://aws.amazon.com/marketplace/management/") and either creating a new product or updating an
  existing product. The **Images and videos** section is used for
  adding promotional media and is located within the **Product
  information** area.
- While API can also be used to add promotional media, direct upload is only supported through AMMP. Public S3 links are
  supported in both API and AMMP.
- Add promotional media in the order you wish the media to display. The first item will be the featured media on the
  product page.
- When image asset type is used, the optional cover image is not available. Images will have thumbnails auto-generated
  once added.

**Update or remove media**

- Once promotional media is added to a product, the title, description, and cover (if available) can be adjusted as needed by
  editing the product.
- Promotional media can be removed once added by clicking on **Delete** for that asset in AMMP prior to submission.

**Order media**

- By default, new promotional media assets are added to the end of the asset order.
- To re-order media, delete assets that are out of order and add them again in the right order for submission.
