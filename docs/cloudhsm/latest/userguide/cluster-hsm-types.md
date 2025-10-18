# AWS CloudHSM cluster modes

AWS CloudHSM offers clusters in two modes: *FIPS* and *non-FIPS*. In FIPS mode, only Federal Information Processing Standard (FIPS) validated keys and algorithms can be used. 
Non-FIPS mode offers all the keys and algorithms that are supported by AWS CloudHSM, regardless of FIPS approval.

Review the details on this page before deciding which cluster mode and HSM type is right for
 your needs. 

###### Note

All clusters created before June 10, 2024 are in FIPS mode and have HSM type hsm1.medium.

To see your cluster's mode and HSM type, use the [describe-clusters](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/describe-clusters.html "https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/describe-clusters.html") command.

The following table lists the major differences between each cluster mode:



| Differentiating feature | FIPS mode | Non-FIPS mode |
| --- | --- | --- |
| **HSM type compatibility** | Available with hsm1.medium and hsm2m.medium. | Available with hsm2m.medium. |
| **Backup compatibility** | Can only be used to backup restore clusters in FIPS mode. | Can only be used to backup restore clusters in non-FIPS mode. |
| **Key selection** | Supports generating and using keys with mechanisms that are FIPS approved[1](#cluster-mode-note-1 "#cluster-mode-note-1"). | Supports generating and using keys with all FIPS-validated mechanisms, in addition to other non-validated mechanisms. |
| **Algorithms** | Supports AWS CloudHSM algorithms that are FIPS approved[1](#cluster-mode-note-1 "#cluster-mode-note-1"). | Supports AWS CloudHSM algorithms that are both FIPS approved and not FIPS approved. | [1] See [Deprecation notifications](compliance-dep-notif.md#compliance-dep-notif-1 "compliance-dep-notif.md#compliance-dep-notif-1") for details. Before choosing a cluster mode, note that a cluster’s mode (FIPS or non-FIPS) cannot be changed after it is created, so ensure you select the right mode for your needs.
