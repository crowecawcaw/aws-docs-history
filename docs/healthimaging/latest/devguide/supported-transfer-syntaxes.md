# Supported transfer syntaxes

AWS HealthImaging supports importing DICOM P10 files with different transfer syntaxes. Some files
retain their original transfer syntax encoding during import, while others are transcoded to
HTJ2K lossless by default. The following example shows how HealthImaging records a
`StoredTransferSyntaxUID` for each instance within the
[metadata](getting-started-concepts.md#concept-metadata "getting-started-concepts.md#concept-metadata") returned by [GetImageSetMetadata](get-image-set-metadata.md "get-image-set-metadata.md").

```
"Instances": {
   "999.999.2.19941105.134500.2.101": {
       "StoredTransferSyntaxUID": "1.2.840.10008.1.2.4.50",
       "ImageFrames": [{ ...

```

###### Note

Keep these points in mind when viewing the following table:

- A transfer syntax UID entry marked with an asterisk (\*) indicates a file is stored in its
  original encoded format during import. For these files, the
  `StoredTransferSyntaxUID` located in the instance metadata matches the original
  transfer syntax.
- A transfer syntax UID entry marked _without_ an asterisk indicates a
  file is transcoded to HTJ2K lossless during import and stored in HealthImaging. For these files, the
  `StoredTransferSyntaxUID` located in the instance metadata is High-Throughput JPEG
  2000 with RPCL Options Image Compression—Lossless Only
  (1.2.840.10008.1.2.4.202).
- If the `StoredTransferSyntaxUID` key does not exist or is set to
  `null`, you can assume it is encoded as HTJ2K Lossless RPCL
  (1.2.840.10008.1.2.4.202).

| HealthImaging supported transfer syntaxes                                                                                                    | Transfer syntax UID                                                                                                                                     | Transfer syntax name                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| 1.2.840.10008.1.2                                                                                                                            | Implicit VR Endian: Default Transfer Syntax for DICOM                                                                                                   |
| 1.2.840.10008.1.2.1\* (binary segmentation retains original encoding, whereas, non-binary segmentation is transcoded to HTJ2K Lossless RPCL) | Explicit VR Little Endian                                                                                                                               |
| 1.2.840.10008.1.2.1.99                                                                                                                       | Deflated Explicit VR Little Endian                                                                                                                      |
| 1.2.840.10008.1.2.2                                                                                                                          | Explicit VR Big Endian                                                                                                                                  |
| 1.2.840.10008.1.2.4.50\*                                                                                                                     | JPEG Baseline (Process 1): Default Transfer Syntax for Lossy JPEG 8-bit Image Compression                                                               |
| 1.2.840.10008.1.2.4.51                                                                                                                       | JPEG Baseline (Processes 2 & 4): Default Transfer Syntax for Lossy JPEG 12-bit Image Compression (Process 4 only)                                       |
| 1.2.840.10008.1.2.4.57                                                                                                                       | JPEG Lossless Non-Hierarchical (Process 14)                                                                                                             |
| 1.2.840.10008.1.2.4.70                                                                                                                       | JPEG Lossless, Nonhierarchical, First- Order Prediction (Processes 14 [Selection Value 1]): Default Transfer Syntax for Lossless JPEG Image Compression |
| 1.2.840.10008.1.2.4.80                                                                                                                       | JPEG-LS Lossless Image Compression                                                                                                                      |
| 1.2.840.10008.1.2.4.81                                                                                                                       | JPEG-LS Lossy (Near-Lossless) Image Compression                                                                                                         |
| 1.2.840.10008.1.2.4.90                                                                                                                       | JPEG 2000 Image Compression (Lossless Only)                                                                                                             |
| 1.2.840.10008.1.2.4.91\*                                                                                                                     | JPEG 2000 Image Compression                                                                                                                             |
| 1.2.840.10008.1.2.4.92                                                                                                                       | JPEG 2000 Part 2 Multicomponent Image Compression (Lossless Only)                                                                                       |
| 1.2.840.10008.1.2.4.93                                                                                                                       | JPEG 2000 Part 2 Multicomponent Image Compression                                                                                                       |
| 1.2.840.10008.1.2.4.201                                                                                                                      | High-Throughput JPEG 2000 Image Compression (Lossless Only)                                                                                             |
| 1.2.840.10008.1.2.4.202                                                                                                                      | High-Throughput JPEG 2000 with RPCL Options Image Compression (Lossless Only)                                                                           |
| 1.2.840.10008.1.2.4.203\*                                                                                                                    | High-Throughput JPEG 2000 Image Compression                                                                                                             |
| 1.2.840.10008.1.2.5                                                                                                                          | RLE Lossless                                                                                                                                            |
| 1.2.840.10008.1.2.4.100\*, 1.2.840.10008.1.2.4.100.1\*                                                                                       | MPEG2 Main Profile Main Level                                                                                                                           |
| 1.2.840.10008.1.2.4.101\*, 1.2.840.10008.1.2.4.101.1\*                                                                                       | MPEG2 Main Profile at High Level                                                                                                                        |
| 1.2.840.10008.1.2.4.102\*, 1.2.840.10008.1.2.4.102.1\*                                                                                       | MPEG-4 AVC/H.264 High Profile / Level 4.1                                                                                                               |
| 1.2.840.10008.1.2.4.103\*, 1.2.840.10008.1.2.4.103.1\*                                                                                       | MPEG-4 AVC/H.264 BD-compatible High Profile / Level 4.1                                                                                                 |
| 1.2.840.10008.1.2.4.104\*, 1.2.840.10008.1.2.4.104.1\*                                                                                       | MPEG-4 AVC/H.264 High Profile / Level 4.2 for 2D Video                                                                                                  |
| 1.2.840.10008.1.2.4.105\*, 1.2.840.10008.1.2.4.105.1\*                                                                                       | MPEG-4 AVC/H.264 High Profile / Level 4.2 of the ITU-T H.264 Video                                                                                      |
| 1.2.840.10008.1.2.4.106\*, 1.2.840.10008.1.2.4.106.1\*                                                                                       | MPEG-4 AVC/H.264 Stereo High Profile / Level 4.2 of the ITU-T H.264 Video                                                                               |
| 1.2.840.10008.1.2.4.107\*                                                                                                                    | HEVC/H.265 Main Profile / Level 5.1 Video                                                                                                               |
| 1.2.840.10008.1.2.4.108\*                                                                                                                    | HEVC/H.265 Main 10 Profile / Level 5.1                                                                                                                  | \*Retains original transfer syntax encoding during import |
