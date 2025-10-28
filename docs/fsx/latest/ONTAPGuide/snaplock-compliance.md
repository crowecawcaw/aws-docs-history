# Understanding SnapLock Compliance

This section describes use cases and considerations for the SnapLock Compliance retention mode.

You might choose the Compliance retention mode for the following use cases.

- You can use SnapLock Compliance to address government or industry-specific
  mandates such as SEC Rule 17a-4(f), FINRA Rule 4511, and CFTC Regulation
  1.31. SnapLock Compliance on Amazon FSx for NetApp ONTAP was assessed for these mandates
  and regulations by Cohasset Associates. For more information, see the
  [_Compliance Assessment Report
  for Amazon FSx for NetApp ONTAP_](https://d1.awsstatic.com/r2018/b/FSx/cohasset_assessment_for_fsx_for_ontap_report.pdf "https://d1.awsstatic.com/r2018/b/FSx/cohasset_assessment_for_fsx_for_ontap_report.pdf").
- You can use SnapLock Compliance to complement or enhance a comprehensive data protection
  strategy to combat ransomware attacks.
  Here are some important items to consider about the SnapLock Compliance retention mode.

- After a file is
  transitioned to the write once, read many (WORM) state on a SnapLock Compliance volume, it can't be deleted
  before its retention period expires by any user.
- A SnapLock Compliance volume can only be deleted when the retention
  periods of all WORM files on the volume have expired, and the WORM files
  have been deleted from the volume.
- You can't rename a SnapLock Compliance volume after creation.
- You can use SnapMirror to replicate WORM files, but the source volume and destination volume must have
  the same retention mode (for example, both must be Compliance).
- A SnapLock Compliance volume can't be converted to a SnapLock Enterprise
  volume, and the reverse.
