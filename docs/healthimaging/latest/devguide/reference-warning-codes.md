

# HealthImaging Warning Codes
<a name="reference-warning-codes"></a>

HealthImaging attempts to import all your medical imaging data. If data non-conformances or unrecognized data elements are encountered during imports, HealthImaging will add one of the following warnings to the `warning.ndjson` file. A warning associated with an imported instance will also be searchable via the `SearchDICOMInstances` action with the `WarningReason` element. Instances imported with a warning may have reduced support via HealthImaging APIs, as described below.


**HealthImaging Import Warning Codes**  
<a name="warning-codes"></a>
<table>
<thead>
  <tr><th>Warning Reason (Hexadecimal)</th><th>Warning Reason (Decimal)</th><th>Warning Type (Enum)</th><th>Warning Details</th><th>Resulting Behavior</th></tr>
</thead>
<tbody>
  <tr><td colspan="5"><b>DICOM Standard Warning Reasons</b></td></tr>
  <tr><td>0xB000</td><td>45056</td><td>COERCION_OF_DATA_ELEMENTS</td><td>The ingestion modified one or more data elements during storage of the instance. See Section <a href="https://dicom.nema.org/dicom/2013/output/chtml/part18/sect_6.6.html#sect_6.6.1.3">6.6.1.3</a>.</td><td>n/a</td></tr>
  <tr><td>0xB006</td><td>45062</td><td>ELEMENTS_DISCARDED</td><td>The ingestion discarded some data elements during storage of the instance. See Section <a href="https://dicom.nema.org/dicom/2013/output/chtml/part18/sect_6.6.html#sect_6.6.1.3">6.6.1.3</a>.</td><td>n/a</td></tr>
  <tr><td>0xB007</td><td>45063</td><td>SOP_CLASS_DATA_MISMATCH</td><td>The <code>StoreDICOM</code> action observed that the Data Set did not match the constraints of the SOP Class during storage of the instance.</td><td>n/a</td></tr>
  <tr><td colspan="5"><b>AWS HealthImaging Warning Reasons</b></td></tr>
  <tr><td>0xB100</td><td>45312</td><td>TRANSCODING_EXCEPTION</td><td>This warning occurs when HealthImaging cannot transcode the instance PixelData to HTJ2K (default storage format), or if the PixelData cannot be transcoded for another reason (i.e. failed validations, wrong pixel data attributes, etc). In this case, the pixel data will be stored as a blob.</td><td>Pixel data may still be retrievable as a single blob if required, passing wildcard "*" as the <code>transfer-syntax</code> in Accept header will return it in the stored format.</td></tr>
  <tr><td>0xB110</td><td>45328</td><td>FRAMES_EXTRACTION_FAILURE</td><td>This warning occurs when there is an issue parsing individual frames from the PixelData based on the given DICOM metadata.</td><td>Pixel data was malformed and cannot be retrieved, use <code>GetDICOMInstance</code> to retrieve the entire instance</td></tr>
  <tr><td>0xB111</td><td>45329</td><td>FRAME_NUMBER_MISMATCH</td><td>This warning occurs when the "NumberOfFrames" DICOM element does not match the actual number of image "fragments" in the input DICOM file.</td><td>Pixel data was malformed and cannot be retrieved, use <code>GetDICOMInstance</code> to retrieve the entire instance</td></tr>
  <tr><td>0xB112</td><td>45330</td><td>INVALID_OFFSET_TABLE</td><td>This warning occurs when the offset table in the fragments of the input DICOM file do not match up with the actual frame length and could result in malformed frames depending on the severity.</td><td>Pixel data was malformed and cannot be retrieved, use <code>GetDICOMInstance</code> to retrieve the entire instance</td></tr>
  <tr><td>0xB120</td><td>45344</td><td>UNSUPPORTED_TRANSFER_SYNTAX</td><td>This warning occurs when HealthImaging encounters an unrecognized or unsupported transfer syntax. When this happens, HealthImaging will store the pixel data as a blob.</td><td>Pixel data may still be retrievable as a single blob if required, passing wildcard "*" as the <code>transfer-syntax</code> in Accept header will return it in the stored format.</td></tr>
  <tr><td>0xB201</td><td>45570</td><td>INVALID_UID_FORMAT</td><td>This warning occurs when one or more UID elements violate the DICOM Value Represention (e.g. <code>1.2.3..4</code>)</td><td>n/a</td></tr>
  <tr><td>0xB202</td><td>45571</td><td>INVALID_DICOM_VALUE_LENGTH</td><td>This warning occurs when a DICOM element has a length longer than that supported by the DICOM Value Representation, potentially introducing invalid behaviors for search/retrieve actions.</td><td>Some fields may not be parseable and therefore cannot be searched on (i.e. <code>StudyDate</code> or <code>StudyTime</code>)</td></tr>
  <tr><td>0xBFFF</td><td>47513</td><td>OTHER</td><td>This warning occurs when there an uncaught warning that HealthImaging does not capture as a specific warning code.</td><td>Pixel data was malformed and cannot be retrieved, use <code>GetDICOMInstance</code> to retrieve the entire instance</td></tr>
</tbody>
</table>
