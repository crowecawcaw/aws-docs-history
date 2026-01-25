AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Blu Age Runtime Utilities

Mainframe JCL scripts use customer business programs and system utilities. AWS Blu Age Runtime includes support for commonly used system utilities to enable proper JCL modernization to Groovy, plus additional convenience utilities.

The purpose of this document is to:

- Explain how to configure and deploy utilities;
- List existing supported system utilities and give details about their usage and purpose.

## Configure and deploy Utility web application

Utilities are provided in `gapwalk-utility-pgm-<version>.war` (where `<version>` is the Blu Age runtime release). Deploy alongside `gapwalk-application` and modernized applications to enable utility access from modernized JCL scripts.

All supported utilities are registered as programs in the "Programs Registry" (see this [Running and calling programs](ba-shared-structure.md#ba-shared-structure-run-call "ba-shared-structure.md#ba-shared-structure-run-call") for details about registering programs and using them in scripts or in other programs). Therefore, they can be called either by other programs or by modernized job scripts.

The utilities web-application has its own configuration file, named `application-utility-pgm.yml`, whose contents are detailed in this [Configure access to utilities for managed
applications](applications-m2-ba-utilities.md "applications-m2-ba-utilities.md").

## Available Utility programs

Available utility programs, listed according to their domain of application:

- [Datasets Utilities](system-datasets-utilities.md "system-datasets-utilities.md")
  - [BLUESAMCOPY/BLUESAMCREATE/BLUESAMDELETE/BLUESAMCLEAR](system-datasets-utilities.md#bluesam-utilities "system-datasets-utilities.md#bluesam-utilities")
  - [BPXWDYN](system-datasets-utilities.md#bpxwdyn "system-datasets-utilities.md#bpxwdyn")
  - [GDGUTILS](system-datasets-utilities.md#gdgutils "system-datasets-utilities.md#gdgutils")
  - [ICEGENER/SYNCGENR](system-datasets-utilities.md#icegener "system-datasets-utilities.md#icegener")
  - [IDCAMS/KQCAMS](system-datasets-utilities.md#idcams "system-datasets-utilities.md#idcams")
  - [IEBGENER/JSDGENER](system-datasets-utilities.md#iebgener "system-datasets-utilities.md#iebgener")
  - [IEFBR14](system-datasets-utilities.md#iefbr14 "system-datasets-utilities.md#iefbr14")
  - [JCLBCICS](system-datasets-utilities.md#jclbcics-utility "system-datasets-utilities.md#jclbcics-utility")

- [Database Utilities](system-database-utilities.md "system-database-utilities.md")
  - [DSNTEP2/DSNTEP4](system-database-utilities.md#dsntep2-dsntep4 "system-database-utilities.md#dsntep2-dsntep4")
  - [DSNUTILB](system-database-utilities.md#dsnutilb "system-database-utilities.md#dsnutilb")
  - [INFUTILB / INZUTILB](system-database-utilities.md#infutilb-inzutilb "system-database-utilities.md#infutilb-inzutilb")
  - [JXHDBCLR](system-database-utilities.md#jxhdbclr "system-database-utilities.md#jxhdbclr")

- [Commands Utilities](system-commands-utilities.md "system-commands-utilities.md")
  - [IKJEFT1A/IKJEFT1B/KEQEFT01/IKJEFT01/DSNDBTCH](system-commands-utilities.md#ikjeft1a-ikjeft1b-keqeft01-ikjeft01-dsndbtch "system-commands-utilities.md#ikjeft1a-ikjeft1b-keqeft01-ikjeft01-dsndbtch")
  - [QCMDEXC](system-commands-utilities.md#qcmdexc "system-commands-utilities.md#qcmdexc")

- [Sort Utilities](system-sort-utilities.md "system-sort-utilities.md")
  - [ICETOOL](system-sort-utilities.md#icetool "system-sort-utilities.md#icetool")
  - [MFSORT](system-sort-utilities.md#mfsort "system-sort-utilities.md#mfsort")
  - [SORT/SYNCSORT/ICEMAN](system-sort-utilities.md#sort-syncsort-iceman "system-sort-utilities.md#sort-syncsort-iceman")

- [Other / Miscellaneous Utilities](system-misc-utilities.md "system-misc-utilities.md")
  - [CBL_AND/CBL_OR/CBL_XOR/CBL_EQ/CBL_IMP/CBL_NOT](system-misc-utilities.md#cbl-bitwise "system-misc-utilities.md#cbl-bitwise")
  - [CEE3ABD](system-misc-utilities.md#cee3abd "system-misc-utilities.md#cee3abd")
  - [CEEDATE](system-misc-utilities.md#ceedate "system-misc-utilities.md#ceedate")
  - [CEELOCT](system-misc-utilities.md#ceeloct "system-misc-utilities.md#ceeloct")
  - [CEERAN0](system-misc-utilities.md#ceeran0 "system-misc-utilities.md#ceeran0")
  - [CEESECS](system-misc-utilities.md#ceesecs "system-misc-utilities.md#ceesecs")
  - [ILBOABN0](system-misc-utilities.md#ilboabn0 "system-misc-utilities.md#ilboabn0")

###### Topics

- [Datasets Utilities](system-datasets-utilities.md "system-datasets-utilities.md")
- [Database Utilities](system-database-utilities.md "system-database-utilities.md")
- [Commands Utilities](system-commands-utilities.md "system-commands-utilities.md")
- [Sort Utilities](system-sort-utilities.md "system-sort-utilities.md")
- [Other / Miscellaneous Utilities](system-misc-utilities.md "system-misc-utilities.md")
