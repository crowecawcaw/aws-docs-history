# DICOM metadata constraints

When you use `UpdateImageSetMetadata` to update HealthImaging [metadata](getting-started-concepts.md#concept-metadata "getting-started-concepts.md#concept-metadata") attributes, the following DICOM constraints are
applied.

- Cannot update or remove private attributes on Patient/Study/Series/Instance level
  attributes unless the update constraint applies to both `updatableAttributes` and
  `removableAttributes`
- Cannot update the following AWS HealthImaging generated attributes: `SchemaVersion`,
  `DatastoreID`, `ImageSetID`, `PixelData`,
  `Checksum`, `Width`, `Height`, `MinPixelValue`,
  `MaxPixelValue`, `FrameSizeInBytes`
- Cannot update the following DICOM attributes unless the `force` flag is set:
  `Tag.PixelData`, `Tag.StudyInstanceUID`,
  `Tag.SeriesInstanceUID`, `Tag.SOPInstanceUID`, `Tag.StudyID`
- Cannot update attributes with VR type SQ (nested attributes) unless the
  `force` flag is set
- Cannot update multivalued attributes unless the `force` flag is set
- Cannot update attributes with values that are not compatible with the attribute VR type
  unless the `force` flag is set
- Cannot update attributes which are not considered valid attributes according to the DICOM
  standard unless the `force` flag is set
- Cannot update attributes across modules. For example, if a Patient level attribute is
  given at the Study level in customer payload request, the request can be invalidated.
- Cannot update attributes if the associated attribute module is not present in existing
  `ImageSetMetadata`. For example, you are not allowed to update attributes for a
  `seriesInstanceUID` if the Series with `seriesInstanceUID` is not
  present in existing image set metadata.
