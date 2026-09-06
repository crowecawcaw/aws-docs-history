

# Using DICOMweb with AWS HealthImaging
<a name="using-dicomweb"></a>

You can retrieve DICOM objects from AWS HealthImaging using a representation of [DICOMweb](https://www.dicomstandard.org/using/dicomweb) APIs, which are web-based APIs that follow the DICOM standard for medical imaging. This functionality enables you to interoperate with systems that utilize DICOM Part 10 binaries while simultaneously taking advantage of HealthImaging’s [cloud native actions](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_Operations.html). The focus of this chapter is how to use HealthImaging's implementation of DICOMweb APIs to return DICOMweb responses.

**Important**  
HealthImaging stores DICOM data as [image sets](getting-started-concepts.md#concept-image-set). Use HealthImaging cloud-native actions to manage and retrieve image sets. HealthImaging's DICOMweb APIs can be used to return image set information with DICOMweb-conformant responses.  
The APIs listed in this chapter are built in conformance to the [DICOMweb](https://www.dicomstandard.org/using/dicomweb) standard for web-based medical imaging. Because they are representations of DICOMweb APIs, they are not offered through AWS CLI and AWS SDKs.

**Topics**
+ [Storing instances with STOW-RS](dicomweb-storing.md)
+ [Retrieving DICOM data from HealthImaging](dicomweb-retrieve.md)
+ [Searching DICOM data in HealthImaging](dicomweb-search.md)
+ [OIDC authentication for DICOMweb APIs](dicomweb-oidc.md)