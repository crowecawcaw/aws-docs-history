# AWS HealthImaging sample projects

AWS HealthImaging provides the following sample projects on GitHub.

**[OHIF Viewer integrated to AWS HealthImaging via OIDC](https://github.com/aws-samples/aws-healthimaging-samples/tree/main/AHI-OIDC-OHIF-installer "https://github.com/aws-samples/aws-healthimaging-samples/tree/main/AHI-OIDC-OHIF-installer")**

This [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/") project deploys [OHIF viewer](https://github.com/OHIF/Viewers "https://github.com/OHIF/Viewers") on [Amazon CloudFront](https://aws.amazon.com/cloudfront/ "https://aws.amazon.com/cloudfront/").
The viewer is integrated to an Amazon Web Services datastore as DICOMWeb data source, and with [Amazon Cognito](https://aws.amazon.com/cognito/ "https://aws.amazon.com/cognito/") as the
identity provider for authentication via OIDC.

**[DICOM Ingestion From On-Premises to AWS HealthImaging](https://github.com/aws-samples/aws-healthimaging-samples/tree/main/dicom-ingestion-to-s3-healthimaging "https://github.com/aws-samples/aws-healthimaging-samples/tree/main/dicom-ingestion-to-s3-healthimaging")**

An AWS serverless project for deploying an IoT edge solution that receives DICOM
files from a DICOM DIMSE source (PACS, VNA, CT scanner) and stores them in a secure Amazon S3
bucket. The solution indexes the DICOM files in a database and queues each DICOM series to
be imported in AWS HealthImaging. It is comprised of a component running at the edge that is
managed by [AWS IoT Greengrass](https://aws.amazon.com/greengrass/ "https://aws.amazon.com/greengrass/"), and a DICOM ingestion
pipeline running in AWS Cloud.

**[Tile Level Marker (TLM) Proxy](https://github.com/aws-samples/aws-healthimaging-samples/tree/main/tile-level-marker-proxy "https://github.com/aws-samples/aws-healthimaging-samples/tree/main/tile-level-marker-proxy")**

An [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/") project for retrieving image
frames from AWS HealthImaging by using tile level markers (TLM), a feature of High-Throughput JPEG
2000 (HTJ2K). This results in faster retrieval times with lower-resolution images.
Potential workflows include generating thumbnails and progressive loading of
images.

**[Amazon CloudFront Delivery](https://github.com/aws-samples/aws-healthimaging-samples/tree/main/amazon-cloudfront-delivery "https://github.com/aws-samples/aws-healthimaging-samples/tree/main/amazon-cloudfront-delivery")**

An AWS serverless project for creating an [Amazon CloudFront](https://aws.amazon.com/cloudfront/ "https://aws.amazon.com/cloudfront/") distribution with an HTTPS endpoint that caches (by using GET) and
delivers image frames from the edge. By default, the endpoint authenticates requests with
an Amazon Cognito JSON web token (JWT). Both authentication and request signing is done at the edge
using [Lambda@Edge](https://aws.amazon.com/lambda/edge/ "https://aws.amazon.com/lambda/edge/"). This service is a
feature of Amazon CloudFront that lets you run code closer to users of your application, which
improves performance and reduces latency. There is no infrastucture to manage.

**[AWS HealthImaging Viewer UI](https://github.com/aws-samples/aws-healthimaging-samples/tree/main/imaging-viewer-ui "https://github.com/aws-samples/aws-healthimaging-samples/tree/main/imaging-viewer-ui")**

An [AWS Amplify](https://aws.amazon.com/amplify/ "https://aws.amazon.com/amplify/") project for deploying
a frontend UI with backend authentication with which you can view image set metadata
attributes and image frames (pixel data) stored in AWS HealthImaging using progressive decoding.
You can optionally integrate the Tile Level Marker (TLM) Proxy and/or Amazon CloudFront Delivery
projects above to load image frames using an alternative method.

**[AWS HealthImaging DICOMweb Proxy](https://github.com/aws-samples/aws-healthimaging-samples/tree/main/dicomweb-proxy "https://github.com/aws-samples/aws-healthimaging-samples/tree/main/dicomweb-proxy")**

A Python-based project for enabling DICOMweb WADO-RS and QIDO-RS endpoints on a HealthImaging
data store to support web-based medical imaging viewers and other DICOMweb-compatible
apps.

###### Note

This project does not use HealthImaging's representation of DICOMweb APIs described in [Using DICOMweb with AWS HealthImaging](using-dicomweb.md "using-dicomweb.md").

To view additional sample projects, see [AWS HealthImaging Samples](https://github.com/aws-samples/aws-healthimaging-samples "https://github.com/aws-samples/aws-healthimaging-samples") on
GitHub.
