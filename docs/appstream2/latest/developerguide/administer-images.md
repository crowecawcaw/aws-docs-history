# Administer Your Amazon AppStream 2.0 Images

Available images are listed in the **Image
Registry** in the AppStream 2.0 console, and categorized by visibility as follows:

- **Public** — Base images that are owned and made
  available by AWS. Base images include the latest Windows operating system and the AppStream 2.0 agent software. You can use these base images to create new images that include your own applications. For information about the base images released by AWS, see
  [AppStream 2.0 Base Image and Managed Image Update
  Release Notes](base-image-version-history.md "base-image-version-history.md").
- **Private** — Images that you create and own,
  and that you have not shared with other AWS accounts.
- **Shared with others** — Images that you create
  and own, and that you have shared with one or more AWS accounts in the same AWS Region. When
  you share an image with another AWS account, you can specify whether the image can
  be used for an image builder (to create a new image), for a fleet, or both.
- **Shared with me** — Images that are created and owned by
  another AWS account in the same AWS Region, and that are shared with your AWS account.
  Depending on the permissions that the owner provided when sharing the image with
  your account, you can use this image for image builders, for fleets, or both.

###### Contents

- [Delete a Private Image in Amazon AppStream 2.0](delete-private-image.md "delete-private-image.md")
- [Copy an Image That You Own to Another AWS Region in Amazon AppStream 2.0](copy-image-different-region.md "copy-image-different-region.md")
- [Share an Image That You Own With Another AWS
  Account in Amazon AppStream 2.0](share-image-with-another-account.md "share-image-with-another-account.md")
- [Stop Sharing an Image That You Own in Amazon AppStream 2.0](stop-sharing-image-with-all-accounts.md "stop-sharing-image-with-all-accounts.md")
- [Keep Your Amazon AppStream 2.0 Image Up-to-Date](keep-image-updated.md "keep-image-updated.md")
- [Windows Update and Antivirus Software on Amazon AppStream 2.0](windows-update-antivirus-software.md "windows-update-antivirus-software.md")
- [Programmatically Create a New Image in Amazon AppStream 2.0](create-image-programmatically.md "create-image-programmatically.md")
- [Manage License Included Applications on Your Image in Amazon AppStream 2.0](license-included-applications.md "license-included-applications.md")
