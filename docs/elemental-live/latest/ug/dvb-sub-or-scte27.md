# Information for DVB-Sub or SCTE-27

This section provides information specific to DVB-Sub or SCTE-27 input captions. It
describes the fields that appear when you choose **DVB-Sub** or
**SCTE-27** in the **Source** field in the
**Caption Selector** section of the event. For more context, see the
steps earlier in this section.

DVB-Sub and SCTE-27 formats are supported only in TS inputs. You must specify the
location of the captions.

Complete the **PID** and **Language code** fields in
one of the ways described in the following table. Each row in the table describes a valid
way to complete these two fields.

| PID       | Language code | Result                                                                                                                                                                                       |
| --------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Specified | Blank         | Extracts the captions from the specified PID.                                                                                                                                                |
| Blank     | Specified     | Extracts the captions from the first PID that Elemental Live<br>encounters that matches the specified language. This might or<br>might not be the PID with the lowest number.                |
| Specified | Specified     | Extracts the captions from the specified PID. Elemental Live<br>ignores the language code, therefore we recommend you leave it<br>blank.                                                     |
| Blank     | Blank         | Valid only if the source is DVB-Sub and the output is DVB-Sub. With this<br>combination of PID and Language, all input DVB-Sub PIDs will be included in the<br>output.Not valid for SCTE-27. |
