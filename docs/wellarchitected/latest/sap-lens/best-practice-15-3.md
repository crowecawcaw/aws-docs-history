# Best Practice 15.3 – Modify SAP

parameters to align with hardware selection

Tuning SAP application parameters can help improve the performance of the application.
These parameters are often dependent on the underlying hardware configuration and
operating system type.

**Suggestion 15.3.1 – Allow SAP to self-tune according to
`PHYS_MEMSIZE`**

For recent versions of SAP software, using kernel release 7.40 or higher, self-tuning
of certain parameters is possible and recommended. For instance, many parameters are
derived via formulas related to the main memory available on an instance (PHYS_MEMSIZE).
This allows for automatic tuning of memory parameters when resizing an EC2 instance
underlying the SAP software to meet changing performance requirements.

- SAP Documentation: [SAP Memory Management: Parameter Reference](https://help.sap.com/viewer/f146e75588924fa4987b6c8f1a7a8c7e/LATEST/en-US/493431b15cce5717e10000000a42189b.html "https://help.sap.com/viewer/f146e75588924fa4987b6c8f1a7a8c7e/LATEST/en-US/493431b15cce5717e10000000a42189b.html")
- SAP Note: [2085980
  – New features in memory management as of Kernel Release 7.40](https://launchpad.support.sap.com/#/notes/2085980 "https://launchpad.support.sap.com/#/notes/2085980") [Requires SAP
  Portal Access]

**Suggestion 15.3.2 – Review SAP swap space and maximum memory
use**

When running SAP on AWS, overutilized swap space on disk can cause I/O credit
exhaustion on Amazon EBS and lead to performance degradation. Evaluate the different
[EBS storage options](../../../AWSEC2/latest/UserGuide/ebs-volume-types.md "../../../AWSEC2/latest/UserGuide/ebs-volume-types.md") available on AWS and configure swap space to meet your
performance needs.

- SAP Note: [1597355

* Swap-space recommendation for Linux](https://launchpad.support.sap.com/#/notes/1597355 "https://launchpad.support.sap.com/#/notes/1597355") [Requires SAP Portal Access]

- SAP Documentation: [Swap Space Requirements](https://help.sap.com/saphelp_nw73/helpdata/en/49/325e42e93934ffe10000000a421937/frameset.htm "https://help.sap.com/saphelp_nw73/helpdata/en/49/325e42e93934ffe10000000a421937/frameset.htm")
