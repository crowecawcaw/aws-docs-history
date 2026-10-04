

# Unified graphics images
<a name="unified-graphics-images"></a>

A unified graphics image is a single graphics image that can support multiple graphics instance families, including Graphics G4dn, G5, G6, Gr6, G6f, Gr6f, and G7. Previously, each graphics family used a separate base image. The AWS base image for a unified graphics image uses the name prefix `AppStream-Graphics-NV-` and is available for Windows Server 2025 and 2022, Red Hat Enterprise Linux 8, and Rocky Linux 8.

With a unified graphics image, you can do the following:
+ Launch an image builder on any supported graphics family from the same image.
+ Create a fleet on any supported graphics family from the same image.
+ Change a fleet's instance type across supported graphics families. For more information, see [Update a Fleet with a New Image in Amazon WorkSpaces Applications](update-fleets.md).

There are three ways to use a unified graphics image:

1. Use the `AppStream-Graphics-NV-{{OperatingSystem}}-{{MM-DD-YYYY}}` base images or create your own images from them.

1. Update an existing graphics image through managed image updates. Managed image updates convert your existing graphics image to a unified graphics image. For more information, see [Update an Image by Using Managed WorkSpaces Applications Image Updates](keep-image-updated-managed-image-updates.md).

1. Create an image from an existing graphics image by using the image builder. As long as a graphics driver is detected on the source image, WorkSpaces Applications converts the image to a unified graphics image. The unified image supports graphics instance families based on the installed driver version. For more information about creating an image, see [Launch an Image Builder to Install and Configure Streaming Applications](tutorial-image-builder-create.md). For details about driver version support, see [Install NVIDIA GRID drivers](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nvidia-GRID-driver.html).

**Note**  
Unified graphics images are not supported for custom or BYOL image types.