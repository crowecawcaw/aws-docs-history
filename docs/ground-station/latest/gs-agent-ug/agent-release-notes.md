

# Agent release notes
<a name="agent-release-notes"></a>

## Latest Agent Version
<a name="gs-agent-releases-latest"></a>

### Version 1.0.5953.0
<a name="gs-agent-version-1-0-5953-0"></a>

Release Date: 06/29/2026

AL2023 RPM Checksums:
+ SHA256: `083eaf4da2095250ab901251446c67b764a574a3cee34c7d2c6d41aa5790ae16`
+ MD5: `76fedce9de360cbb0464986214bcfbc1`

AL2 RPM Checksums:
+ SHA256: `f2905ff0da26473669ac2d3c096b04c8e423166be3e5b1dcf39912a2f6002915`
+ MD5: `c178f0d7f1ad86e0717c7fac2c6edaf2`

Changes:
+ Add support for Amazon Linux 2023

## Deprecated Agent Versions
<a name="gs-agent-releases-deprecated"></a>

### Version 1.0.4382.0
<a name="gs-agent-version-1-0-4382-0"></a>

Release Date: 11/18/2025

End of Support Date: 06/30/2026

RPM Checksums:
+ SHA256: `620fd307124f1276194f2faa0104fe0549427ae18e4f5655444f8c30b919c640`
+ MD5: `73e06dcad44adaccbe2ab005218abfc7`

Changes:
+ Update client retry behavior when server indicates overload.

### Version 1.0.3555.0
<a name="gs-agent-version-1-0-3555-0"></a>

Release Date: 03/27/2024

End of Support Date: 06/30/2026

RPM Checksums:
+ SHA256: `108f3aceb00e5af549839cd766c56149397e448a6e1e1429c89a9eebb6bc0fc1`
+ MD5: `65b72fa507fb0af32651adbb18d2e30f`

Changes:
+ Add Agent metric for selected executable version during tasking startup.
+ Add config file support for avoiding specific executable versions when other versions are available.
+ Add network and routing diagnostics.
+ Additional security features.
+ Fix issue where some metric reporting errors were written to stdout/journal instead of log file.
+ Gracefully handle network unreachable socket errors.
+ Measure packet loss and latency between source and destination agents.
+ Release aws-gs-datapipe version 2.0 to support new protocol features and the ability to transparently upgrade contacts to the new protocol.

### Version 1.0.2942.0
<a name="gs-agent-version-1-0-2942-0"></a>

Release Date: 06/26/2023

End of Support Date: 05/31/2024

RPM Checksums:
+ SHA256: `7d94b642577504308a58bab28f938507f2591d4e1b2c7ea170b77bea97b5a9b6`
+ MD5: `661ff2b8f11aba5d657a6586b56e0d8f`

Changes:
+ Added error logs for when Agent RPM is updated on disk and needs Agent restart for changes to take effect.
+ Added network tuning validation to ensure Agent user guide tuning steps are followed and applied correctly.
+ Fix bug that caused erroneous warnings in Agent logs about log archival.
+ Improved packet loss detection.
+ Updated Agent install to prevent install or upgrade of the RPM if the Agent is already running.

### Version 1.0.2716.0
<a name="gs-agent-version-1-0-2716-0"></a>

Release Date: 03/15/2023

End of Support Date: 05/31/2024

RPM Checksums:
+ SHA256: `cb05b6a77dfcd5c66d81c0072ac550affbcefefc372cc5562ee52fb220844929`
+ MD5: `65266490c4013b433ec39ee50008116c`

Changes:
+ Enable uploading logs when Agent experiences failures during tasking.
+ Fix linux compatability bug in provided network tuning scripts.

### Version 1.0.2677.0
<a name="gs-agent-version-1-0-2677-0"></a>

Release Date: 02/15/2023

End of Support Date: 05/31/2024

RPM Checksums:
+ SHA256: `77cfe94acb00af7ca637264b17c9b21bd7afdc85b99dffdd627aec9e99397489`
+ MD5: `b8533be7644bb4d12ab84de21341adac`

Changes:
+ First generally available Agent release.