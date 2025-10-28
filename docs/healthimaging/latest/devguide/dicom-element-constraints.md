# DICOM element constraints

When importing your medical imaging data into AWS HealthImaging, max length constraints are applied
to the following DICOM elements. To achieve a successful import, ensure that your data does not
exceed the max length constraints.

| DICOM element constraints during import | DICOM keyword | DICOM tag | Max length |
| --------------------------------------- | ------------- | --------- | ---------- |
| PatientName                             | (0010,0010)   | 256       |
| PatientID                               | (0010,0020)   | 256       |
| PatientBirthDate                        | (0010,0030)   | 18        |
| PatientSex                              | (0010,0040)   | 16        |
| StudyInstanceUID                        | (0020,000D)   | 256       |
| StudyID                                 | (0020,0010)   | 256       |
| StudyDescription                        | (0008,1030)   | 256       |
| NumberOfStudyRelatedSeries              | (0020,1206)   | 1,000,000 |
| NumberOfStudyRelatedInstances           | (0020,1208)   | 1,000,000 |
| AccessionNumber                         | (0008,0050)   | 256       |
| StudyDate                               | (0008,0020)   | 18        |
| StudyTime                               | (0008,0030)   | 28        |
| SOPInstanceUID                          | (0008,0018)   | 256       |
| SeriesInstanceUID                       | (0020,000E)   | 256       |
