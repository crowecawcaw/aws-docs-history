# Applying automated ABR rules

Use **Automated ABR rules** to specify restrictions for the rendition
sizes that MediaConvert creates in your automated ABR stack. We recommend using these
rules if your ABR workflow has specific rendition size requirements, but you still want
MediaConvert to optimize for video quality and overall file size.

You can define the following rules:

- **Min top rendition size**
- **Min bottom rendition size**
- **Force include renditions**
- **Allowed renditions**

## Min top rendition size

Specify a minimum size for the highest video resolution in your ABR stack. The
highest resolution is greater than or equal to the value that you enter.

For example: If you specify 1920x1080, the highest resolution in your ABR stack is
greater than or equal to 1920x1080.

## Min bottom rendition size

Specify a minimum size for the lowest video resolution in your ABR stack. The
lowest resolution in your ABR stack is greater than or equal to the value that you
enter.

For example: If you specify 512x288, the lowest resolution in your ABR stack is
greater than or equal to 512x288.

## Force include renditions

Specify one or more video resolutions to include in your ABR stack. To optimize
automated ABR, we recommend that you specify as few resolutions as possible.

The ABR stack might include other resolutions that you do not specify here,
depending on the **Max renditions** setting. For example: If you
specify 2 resolutions under **Force include renditions**, and
specify 7 **Max renditions**, then 5 resolutions are automatically
determined.

**Force include renditions** has the following restrictions with
other automated ABR rules or settings:

- At least one resolution must be greater than or equal to **Min top
  rendition size**.
- All resolutions must be greater than or equal to **Min bottom
  rendition size**.
- **Allowed renditions** cannot be not specified.
- The number of resolutions must be less than or equal to **Max
  renditions**.
- Duplicate resolutions are ignored.

## Allowed renditions

Specify a list of possible video resolutions in your ABR stack. MediaConvert
creates an ABR stack exclusively from the list of resolutions that you
specify.

Some resolutions in the **Allowed renditions** list might not be
included. However you can force a resolution to be included by setting
**Required** to **ENABLED**.

**Allowed renditions** has the following restrictions with other
automated ABR rules:

- At least one resolution must be greater than or equal to **Min top
  rendition size**.
- At least one resolution must be greater than or equal to **Min
  bottom rendition size**.
- **Force include renditions** cannot be not
  specified.
- The number of resolutions must be less than or equal to **Max
  renditions**.
- Duplicate resolutions are ignored.
