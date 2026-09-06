

# Release Notes and Document History for Amazon DCV Access Console
<a name="doc-history-release-notes"></a>

This page provides the release notes and document history for Amazon DCV Access Console.

**Topics**
+ [Release Notes](#release-notes)
+ [Document History](#doc-history)

## Amazon DCV Access Console Release Notes
<a name="release-notes"></a>

This section provides release notes for the Amazon DCV Access Console by release date.

**Topics**
+ [2025.0-175 — February 2, 2026](#2025.0-175)
+ [2025.0-168 — December 23, 2025](#2025.0-168)
+ [2025.0-159 — November 12, 2025](#2025.0-159)
+ [2025.0-155 — October 23, 2025](#2025.0-155)
+ [2024.0-150 — June 17, 2025](#2024.0-150)
+ [2024.0-135 — January 15, 2025](#2024.0-135)
+ [2024.0-73 — October 1, 2024](#2024.0-73)
+ [2023.1-57 — August 1, 2024](#2023.1-57)
+ [2023.1-20 — June 26, 2024](#2023.1-20)
+ [2023.1 — June 13, 2024](#2023.1)

### 2025.0-175 — February 2, 2026
<a name="2025.0-175"></a>



| Build numbers | Release notes | 
| --- | --- | 
| Version: 2025.0-175+ Web Client: 175<br />+ Handler: 175<br />+ Authentication Server: 175<br />+ Setup Wizard: 175 |  +  Added `jwt-default-groups-claim-key` and `jwt-role-claim-key` parameters in the Handler configuration to support role and group assignment from external OAuth claims. <br />+  Added `loginUsername` support to CSV user import. <br />+  Replaced `userId` values with `loginUsername` values for display throughout the user interface and added support for filtering and sorting on these values.   | 

### 2025.0-168 — December 23, 2025
<a name="2025.0-168"></a>



| Build numbers | Release notes | 
| --- | --- | 
| Version: 2025.0-168+ Web Client: 168<br />+ Handler: 168<br />+ Authentication Server: 168<br />+ Setup Wizard: 168 |  +  Dropped support for Amazon Linux 2 due to security vulnerabilities in required packages.   | 

### 2025.0-159 — November 12, 2025
<a name="2025.0-159"></a>



| Build numbers | Release notes | 
| --- | --- | 
| Version: 2025.0-159+ Web Client: 159<br />+ Handler: 159<br />+ Authentication Server: 159<br />+ Setup Wizard: 159 |  +  Added support for macOS hosts. <br />+  Fixed token expiration handling to support both seconds and milliseconds timestamp formats, preventing token expiration issues.   | 

### 2025.0-155 — October 23, 2025
<a name="2025.0-155"></a>



| Build numbers | Release notes | 
| --- | --- | 
| Version: 2025.0-155+ Web Client: 155<br />+ Handler: 155<br />+ Authentication Server: 155<br />+ Setup Wizard: 155 |  +  Updated version to 2025.   | 

### 2024.0-150 — June 17, 2025
<a name="2024.0-150"></a>



| Build numbers | Release notes | 
| --- | --- | 
| Version: 2024.0-150+ Web Client: 150<br />+ Handler: 150<br />+ Authentication Server: 150<br />+ Setup Wizard: 150 |  +  Added parameters in the Handler and Web Client configuration files to support external OAuth providers. <br />+  Other fixes and performance improvements.   | 

### 2024.0-135 — January 15, 2025
<a name="2024.0-135"></a>



| Build numbers | Release notes | 
| --- | --- | 
| Version: 2024.0-135+ Web Client: 135<br />+ Handler: 94<br />+ Authentication Server: 90<br />+ Setup Wizard: 75 |  + Added configurable parameters in the Web Client configuration file to specify the maximum height and width of screenshots taken using the `GetSessionScreenshots` API.<br />+ Fixed an issue where session template requirements were not persisting when editing existing templates.<br />+ Fixed Web Client failing on EL9 based distributions.<br />+ Removed internet access requirement for Web Client installation.<br />+ Bug fixes and performance improvements.  | 

### 2024.0-73 — October 1, 2024
<a name="2024.0-73"></a>



| Build numbers | Release notes | 
| --- | --- | 
| Version: 2024.0-73+ Web Client: 73<br />+ Handler: 55<br />+ Authentication Server: 54<br />+ Setup Wizard: 50 |  + Rebranded NICE DCV to Amazon DCV.<br />+ Added support for Ubuntu 24.04.<br />+ Added functionality to make the Privacy link on the Sign In page configurable.<br />+ Bug fixes and performance improvements.  | 

### 2023.1-57 — August 1, 2024
<a name="2023.1-57"></a>



| Build numbers | Release notes | 
| --- | --- | 
| Version: 2023.1-57+ Web Client: 57<br />+ Handler: 39<br />+ Authentication Server: 34<br />+ Setup Wizard: 31 |  + Added the ability to upgrade the Access Console components in place.<br />+ Added the ability to select multiple session templates at once.<br />+ Modified the Setup Wizard to also be compatible with Python 3.6 and 3.7.<br />+ Bug fixes and performance improvements.  | 

### 2023.1-20 — June 26, 2024
<a name="2023.1-20"></a>



| Build numbers | Release notes | 
| --- | --- | 
| Version: 2023.1-20+ Web Client: 20<br />+ Handler: 20<br />+ Authentication Server: 26<br />+ Setup Wizard: 20 |  + Added an error if **Creating a session** fails.<br />+ Bug fixes and performance improvements.  | 

### 2023.1 — June 13, 2024
<a name="2023.1"></a>



| Build numbers | Release notes | 
| --- | --- | 
| Version: 2023.1+ Web Client: 16<br />+ Handler: 17<br />+ Authentication Server: 25<br />+ Setup Wizard: 15 | Initial release of the Amazon DCV Access Console. | 

## Document History
<a name="doc-history"></a>

The following table describes the documentation for this release of Amazon DCV Access Console.



| Change | Description | Date | 
| --- | --- | --- | 
| Amazon DCV Version 2025.0-175 | Amazon DCV Access Console has been updated for Amazon DCV 2025.0-175. For more information, see [2025.0-175--February 2, 2026](#2025.0-175). | February 2, 2026 | 
| Amazon DCV Version 2025.0-168 | Amazon DCV Access Console has been updated for Amazon DCV 2025.0-168. For more information, see [2025.0-168--December 23, 2025](#2025.0-168). | December 23, 2025 | 
| Amazon DCV Version 2025.0-159 | Amazon DCV Access Console has been updated for Amazon DCV 2025.0-159. For more information, see [2025.0-159--November 12, 2025](#2025.0-159). | November 12, 2025 | 
| Amazon DCV Version 2025.0-155 | Amazon DCV Access Console has been updated for Amazon DCV 2025.0-155. For more information, see [2025.0-155--October 23, 2025](#2025.0-155). | October 23, 2025 | 
| Amazon DCV Version 2024.0-150 | Amazon DCV Access Console has been updated for Amazon DCV 2024.0-150. For more information, see [2024.0-150--June 17, 2025](#2024.0-150). | June 17, 2025 | 
| Amazon DCV Version 2024.0-135 | Amazon DCV Access Console has been updated for Amazon DCV 2024.0-135. For more information, see [2024.0-135--January 15, 2025](#2024.0-135). | January 15, 2025 | 
| Amazon DCV Version 2024.0-73 | Amazon DCV Access Console has been updated for Amazon DCV 2024.0-73. For more information, see [2024.0-73--October 1, 2024](#2024.0-73). | October 1, 2024 | 
| Amazon DCV Version 2023.1-57 | Amazon DCV Access Console has been updated for Amazon DCV 2023.1-57. For more information, see [2023.1-57--July 29, 2024](#2023.1-57). | August 1, 2024 | 
| Amazon DCV Version 2023.1-20 | NICE DCV Access Console has been updated for NICE DCV 2023.1-20. For more information, see [2023.1-20--June 26, 2024](#2023.1-20). | June 26, 2024 | 
| Initial release | First publication of this content. | June 13, 2024 | 