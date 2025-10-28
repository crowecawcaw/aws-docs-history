# Complete the PIDs for ARIB

This section applies when you set up the captions encode as described in [Step 1: Identify the
source captions that you want](identify-captions-in-the-input.md "identify-captions-in-the-input.md"), if the output group is UDP/TS and the
output captions format is ARIB. It describes how to complete the PIDs for the output
that contains these captions.

###### To complete the PIDs (ARIB)

1. In the Output section, open the PID Control section.
2. Complete the ARIB Captions field and the ARIB Captions PID field as
   follows:

| ARIB Captions PID Control | ARIB Captions PID                 | Result                                                                                |
| ------------------------- | --------------------------------- | ------------------------------------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------- |
| Unchecked                 | Ignore.                           | A PID will automatically be assigned during encoding; this value could be any number. |
| Checked                   | Type a decimal or hexadecimal.    | This PID will be used for the captions.                                               |
| Leave the default (507)   | The PID for captions will be 507. |                                                                                       | Delete the default | A PID will automatically be assigned during encoding; this value could be any number. |
