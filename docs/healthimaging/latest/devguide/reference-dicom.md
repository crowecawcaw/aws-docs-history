# DICOM support for AWS HealthImaging

AWS HealthImaging supports specific DICOM elements and transfer syntaxes. Familiarize yourself with
the supported Patient, Study, and Series level DICOM data elements, as HealthImaging metadata keys are
based on them. Before you start an import, verify that your medical imaging data is compliant with
HealthImaging's supported transfer syntaxes and DICOM element constraints.

###### Note

AWS HealthImaging does not currently support Binary Segmentation Images or Icon Image Sequence pixel
data.

###### Topics

- [Supported SOP classes](supported-sop-classes.md "supported-sop-classes.md")
- [Metadata normalization](metadata-normalization.md "metadata-normalization.md")
- [Supported transfer syntaxes](supported-transfer-syntaxes.md "supported-transfer-syntaxes.md")
- [DICOM element constraints](dicom-element-constraints.md "dicom-element-constraints.md")
- [DICOM metadata constraints](dicom-metadata-constraints.md "dicom-metadata-constraints.md")
