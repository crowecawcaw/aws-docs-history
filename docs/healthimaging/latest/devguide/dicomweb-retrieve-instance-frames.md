# Getting DICOM instance frames from

HealthImaging

Use the `GetDICOMInstanceFrames` action to retrieve single or batch image frames
(`multipart` request) from a DICOM instance in a HealthImaging [data store](getting-started-concepts.md#concept-data-store "getting-started-concepts.md#concept-data-store") by specifying the Series UID, Study UID, Instance
UIDs, and frame numbers associated with a resource. You can specify the [image set](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set") from which instance frames should be retrieved by
providing the image set ID as a query parameter. The API will only return instance frames from
primary image sets unless the optional [image set](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set") parameter
is provided. You can retrieve any instance frame (from primary or non-primary image sets) in the
data store by specifying the `imageSetId` as a query parameter.

DICOM data can be retrieved in either its stored
transfer syntax or as uncompressed (ELE) format.

###### To get DICOM instance frames (`multipart`)

1. Collect HealthImaging `datastoreId` and `imageSetId` parameter values.
2. Use the [`GetImageSetMetadata`](../APIReference/API_GetImageSetMetadata.md "../APIReference/API_GetImageSetMetadata.md") action with the `datastoreId` and
   `imageSetId` parameter values to retrieve associated metadata values for
   `studyInstanceUID`, `seriesInstanceUID`, and `sopInstanceUID`.
   For more information, see [Getting image set metadata](get-image-set-metadata.md "get-image-set-metadata.md").
3. Determine the image frames to retrieve from the associated metadata to form the
   `frameList` parameter. The `frameList` parameter is a comma-separated
   list of one or more non-duplicate frame numbers, in any order. For example, the first image
   frame in the metadata will be frame 1.
   - Single-frame request: `/frames/1`
   - Multi-frame request: `/frames/1,2,3,4`

4. Construct a URL for the request using the values for `datastoreId`,
   `studyInstanceUID`, `seriesInstanceUID`, `sopInstanceUID`,
   `imageSetId`, and `frameList`. To view the entire URL path in the
   following example, scroll over the **Copy** button. The URL is of the
   form:

```
GET https://dicom-medical-imaging.`region`.amazonaws.com/datastore/`datastore-id`/studies/`study-instance-uid`/series/`series-instance-uid`/instances/`sop-instance-uid`/frames/1?imageSetId=`image-set-id`

```

5. Prepare and send your request. `GetDICOMInstanceFrames` uses a HTTP GET request
   with [AWS Signature
   Version 4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") signing protocol. The following code example uses the `curl`
   command line tool to get image frames in a `multipart` response from HealthImaging.

Shell

```
curl --request GET \
  'https://dicom-medical-imaging.us-east-1.amazonaws.com/datastore/d9a2a515ab294163a2d2f4069eed584c/studies/1.3.6.1.4.1.5962.1.2.4.20040826285059.5457/series/1.3.6.1.4.1.5962.1.3.4.1.20040825185059.5457/instances/1.3.6.1.4.1.5962.1.1.4.1.1.20040826186059.5457/frames/1?imageSetId=459e50687f121185f747b67bb60d1bc8' \
  --aws-sigv4 'aws:amz:us-east-1:medical-imaging' \
  --user "`$AWS_ACCESS_KEY_ID`:`$AWS_SECRET_ACCESS_KEY`" \
  --header "x-amz-security-token:`$AWS_SESSION_TOKEN`" \
  --header 'Accept: multipart/related; type=application/octet-stream; transfer-syntax=1.2.840.10008.1.2.1'

```

###### Note

The `transfer-syntax` UID is optional and defaults to Explicit VR Little Endian
if not included. If transcoding to ELE is not feasible (due to import with warning) then pixels
will be returned without transcoding. Supported transfer syntaxes include:

    * Explicit VR Little Endian (ELE) - `1.2.840.10008.1.2.1` (default for lossless image frames)
    * If `transfer-syntax=*` then the image frame(s) will be returned in the stored transfer syntax.
    * High-Throughput JPEG 2000 with RPCL Options Image Compression (Lossless Only) -
     `1.2.840.10008.1.2.4.202` - if the instance is stored in HealthImaging as
     `1.2.840.10008.1.2.4.202`
    * JPEG 2000 Lossless - `1.2.840.10008.1.2.4.90` - if the instance is stored in HealthImaging as lossless.
    * JPEG Baseline (Process 1): Default Transfer Syntax for Lossy JPEG 8-bit Image
     Compression - `1.2.840.10008.1.2.4.50` - if the instance is stored in HealthImaging as
     `1.2.840.10008.1.2.4.50`
    * JPEG 2000 Image Compression - `1.2.840.10008.1.2.4.91` - if the instance is stored in
     HealthImaging as `1.2.840.10008.1.2.4.91`
    * High-Throughput JPEG 2000 Image Compression - `1.2.840.10008.1.2.4.203` - if the instance
     is stored in HealthImaging as `1.2.840.10008.1.2.4.203`
    * JPEG XL Image Compression - `1.2.840.10008.1.2.4.112` - if the instance is stored in HealthImaging
     as `1.2.840.10008.1.2.4.112`
    * Instances stored in HealthImaging with one or more image frames encoded in the MPEG family of
     [Transfer Syntaxes](supported-transfer-syntaxes.md "supported-transfer-syntaxes.md") (which includes MPEG2, MPEG-4
     AVC/H.264 and HEVC/H.265) may be retrieved with the corresponding transfer-syntax UID. For example,
     `1.2.840.10008.1.2.4.100` if the instance is stored as MPEG2 Main Profile Main Level.
    * You may receive a 406 `NotAcceptableException` if the requested transfer syntax cannot
     be returned based on the stored transfer syntax, or if there are specific processing warnings for the
     instance. If this occurs, retry the call with `transfer-syntax=*`.

For more information, see [Supported transfer syntaxes](supported-transfer-syntaxes.md "supported-transfer-syntaxes.md") and [Image frame decoding libraries for AWS HealthImaging](reference-libraries.md "reference-libraries.md").
