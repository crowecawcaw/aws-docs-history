

# Complete the PIDs for ARIB
<a name="complete-the-pids-for-arib"></a>

This section applies when you set up the captions encode as described in [Step 1: Identify the source captions that you want](identify-captions-in-the-input.md), if the output group is UDP/TS and the output captions format is ARIB. It describes how to complete the PIDs for the output that contains these captions.

**To complete the PIDs (ARIB)**

1. In the Output section, open the PID Control section.

1. Complete the ARIB Captions field and the ARIB Captions PID field as follows:



- ** Unchecked **
  - **ARIB Captions PID:** Ignore.
  - **Result:** A PID will automatically be assigned during encoding; this value could be any number.

- ** Checked **
  - **ARIB Captions PID:** Type a decimal or hexadecimal. / **Result:** This PID will be used for the captions.
  - **ARIB Captions PID:** Leave the default (507) / **Result:** The PID for captions will be 507.
  - **ARIB Captions PID:** Delete the default / **Result:** A PID will automatically be assigned during encoding; this value could be any number.

