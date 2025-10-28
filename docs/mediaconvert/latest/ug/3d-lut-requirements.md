# 3D LUTs job settings requirements

When you include 3D LUTs as part of your MediaConvert job, you must also
include the following settings:

**Input color space**

Specify which inputs use this 3D LUT, according to the input's color space.

**Input mastering luminance**

(Optional) Include **Input mastering luminance** only
when your input has an **HDR10** or **P3D65 (HDR)** color space. Otherwise, keep blank. Use to select between
inputs with different mastering luminances.

**Output color space**

Specify which outputs use this 3D LUT, according to the output's color space.

**Output mastering luminance**

(Optional) Include **Output mastering luminance** only
when your output has an **HDR10** or **P3D65 (HDR)** color space. Otherwise, keep blank. Use to select between
outputs with different mastering luminances.

**.cube file**

Specify an Amazon S3, HTTP, or HTTPS URL for your .cube file. MediaConvert accepts .cube
files up to 8MB in size.

**Color corrector**

Specify an output color space in the **Color corrector** preprocessor for your video output.
