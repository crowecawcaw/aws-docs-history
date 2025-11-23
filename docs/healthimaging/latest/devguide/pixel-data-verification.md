# AWS HealthImaging pixel data verification

During import, HealthImaging provides built-in pixel data verification by checking the lossless
encoding and decoding state of every image. This feature ensures that images decoded using [HTJ2K decoding libraries](reference-libraries.md "reference-libraries.md") always match the original DICOM P10
images imported into HealthImaging.

- The image onboarding process begins when an import job captures the original pixel
  quality state of DICOM P10 images before they are imported. A unique immutable Image Frame
  Resolution Checksum (IFRC) is generated for each image using the CRC32 algorithm. The IFRC
  checksum value is presented in the `job-output-manifest.json` metadata document.
  For more information, see [Understanding import jobs](understanding-import-jobs.md "understanding-import-jobs.md").
- After the images are imported into a HealthImaging [data
  store](getting-started-concepts.md#concept-data-store "getting-started-concepts.md#concept-data-store") and transformed into [image sets](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set"), the
  HTJ2K-encoded [image frames](getting-started-concepts.md#concept-image-frame "getting-started-concepts.md#concept-image-frame") are immediately
  decoded and new IFRCs are calculated. HealthImaging then compares the full resolution IFRCs of the
  original images against the new IFRCs of the imported image frames to verify
  accuracy.
- A corresponding per-image descriptive error condition is captured in the import job
  output log (`job-output-manifest.json`) for you to review and
  verify.

###### To verify pixel data

1. After importing your medical imaging data, view the per-image set descriptive success
   (or error condition) captured in the import job output log,
   `job-output-manifest.json`. For more information, see [Understanding import jobs](understanding-import-jobs.md "understanding-import-jobs.md").
2. [Image sets](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set") are comprised of [metadata](getting-started-concepts.md#concept-metadata "getting-started-concepts.md#concept-metadata") and [image
   frames](getting-started-concepts.md#concept-image-frame "getting-started-concepts.md#concept-image-frame") (pixel data). Image set metadata contains information about associated image
   frames. Use the `GetImageSetMetadata` action to get metadata for an image set.
   For more information, see [Getting image set metadata](get-image-set-metadata.md "get-image-set-metadata.md").
3. The `PixelDataChecksumFromBaseToFullResolution` contains the IFRC (checksum)
   for the full resolution image. For images stored in their original transfer syntax
   1.2.840.10008.1.2.4.203, 1.2.840.10008.1.2.4.91, 1.2.840.10008.1.2.4.50, and
   1.2.840.10008.1.2.1 (Binary Segmentation only) the checksum is calculated on the original
   image. For images that are stored in HTJ2K Lossless with RPCL, the checksum is calculated on
   the decoded full resolution image. For more information, see [Supported transfer syntaxes](supported-transfer-syntaxes.md "supported-transfer-syntaxes.md").

Following is example metadata output for the IFRC that is generated as part of the
import job process and recorded to `job-output-manifest.json`.

```
"ImageFrames": [{
"ID": "67890678906789012345123451234512",
"PixelDataChecksumFromBaseToFullResolution": [
{
    "Width": 512,
    "Height": 512,
    "Checksum": 2510355201
}
]

```

For images stored in their original transfer syntax 1.2.840.10008.1.2.4.203,
1.2.840.10008.1.2.4.91, 1.2.840.10008.1.2.4.50, and 1.2.840.10008.1.2.1 (Binary Segmentation
only) the `MinPixelValue` and `MaxPixelValue` will not be available.
The `FrameSizeInBytes` indicates the size of the original frame.

```
"PixelDataChecksumFromBaseToFullResolution": [
   {"Width": 512, "Height": 512, "Checksum": 1379921327 }
],
"MinPixelValue": null,
"MaxPixelValue": null,
"FrameSizeInBytes": 429

```

For images stored in HTJ2K Lossless with RPCL, the `FrameSizeInBytes`
indicates the size of the decoded image frame.

```
"PixelDataChecksumFromBaseToFullResolution": [
   {"Width": 512, "Height": 512, "Checksum": 1379921327 }
],
"MinPixelValue": 11,
"MaxPixelValue": 11,
"FrameSizeInBytes": 1652

```

4. For instances containing video, HealthImaging performs a lightweight codec
   validation that verifies the transfer syntax specified in the DICOM metadata
   matches the video codec.

HealthImaging computes an IFRC checksum value on the original video object using the CRC32
algorithm. The IFRC checksum value is recorded to the `job-output-manifest.json`, and
persisted in the HealthImaging metadata. As with images stored in their original transfer
syntax (described above), the `MinPixelValue` and `MaxPixelValue` will not be available. The
FrameSizeInBytes indicates the size of the original frame. 5. HealthImaging verify pixel data, access the [Pixel data verification](https://github.com/aws-samples/aws-healthimaging-samples/tree/main/pixel-data-verification "https://github.com/aws-samples/aws-healthimaging-samples/tree/main/pixel-data-verification") procedure on GitHub and follow the instructions in
the`README.md` file to independently verify lossless image processing
by the various [Image frame decoding libraries](reference-libraries.md "reference-libraries.md") that
are utilized by HealthImaging. After the full image is loaded, you can compute the IFRC for raw
input data on your end and compare it with the IFRC value provided in the HealthImaging metadata to
verify the pixel data.
