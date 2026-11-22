

# Agent release notes

## Latest Agent Version
<a name="gs-agent-releases-latest"></a>

### Version 1.0.8022.0
<a name="gs-agent-version-1-0-8022-0"></a>

Release Date: 2026-11-17

The Amazon Linux 2023 RPM has the following checksums:
+ SHA256: `1b63585d1d2032118598d8ffcd53e4fde495dd2304f23a405b446c6e43547362`
+ MD5: `18ab683256ed52498147e4bb733a02e8`

The Amazon Linux 2 RPM has the following checksums:
+ SHA256: `442c32f2bea5ce7697ffe729a237d8a74c2013aaea7e563ff9d7ebd0dea4dad9`
+ MD5: `eb3ceacfcc2932272c0bc5f272d4facf`

This version includes the following changes:
+ Support dataflow endpoints whose Elastic IP is on a secondary network interface

## Deprecated Agent Versions
<a name="gs-agent-releases-deprecated"></a>

### Version 1.0.5953.0
<a name="gs-agent-version-1-0-5953-0"></a>

Release Date: 2026-06-29

End of Support Date: 2027-04-17

The Amazon Linux 2023 RPM has the following checksums:
+ SHA256: `083eaf4da2095250ab901251446c67b764a574a3cee34c7d2c6d41aa5790ae16`
+ MD5: `76fedce9de360cbb0464986214bcfbc1`

The Amazon Linux 2 RPM has the following checksums:
+ SHA256: `f2905ff0da26473669ac2d3c096b04c8e423166be3e5b1dcf39912a2f6002915`
+ MD5: `c178f0d7f1ad86e0717c7fac2c6edaf2`

This version includes the following changes:
+ Add support for Amazon Linux 2023

### Version 1.0.4382.0
<a name="gs-agent-version-1-0-4382-0"></a>

Release Date: 2025-11-18

End of Support Date: 2026-06-30

The RPM has the following checksums:
+ SHA256: `620fd307124f1276194f2faa0104fe0549427ae18e4f5655444f8c30b919c640`
+ MD5: `73e06dcad44adaccbe2ab005218abfc7`

This version includes the following changes:
+ Update client retry behavior when server indicates overload.

### Version 1.0.3555.0
<a name="gs-agent-version-1-0-3555-0"></a>

Release Date: 2024-03-27

End of Support Date: 2026-06-30

The RPM has the following checksums:
+ SHA256: `108f3aceb00e5af549839cd766c56149397e448a6e1e1429c89a9eebb6bc0fc1`
+ MD5: `65b72fa507fb0af32651adbb18d2e30f`

This version includes the following changes:
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

Release Date: 2023-06-26

End of Support Date: 2024-05-31

The RPM has the following checksums:
+ SHA256: `7d94b642577504308a58bab28f938507f2591d4e1b2c7ea170b77bea97b5a9b6`
+ MD5: `661ff2b8f11aba5d657a6586b56e0d8f`

This version includes the following changes:
+ Added error logs for when Agent RPM is updated on disk and needs Agent restart for changes to take effect.
+ Added network tuning validation to ensure Agent user guide tuning steps are followed and applied correctly.
+ Fix bug that caused erroneous warnings in Agent logs about log archival.
+ Improved packet loss detection.
+ Updated Agent install to prevent install or upgrade of the RPM if the Agent is already running.

### Version 1.0.2716.0
<a name="gs-agent-version-1-0-2716-0"></a>

Release Date: 2023-03-15

End of Support Date: 2024-05-31

The RPM has the following checksums:
+ SHA256: `cb05b6a77dfcd5c66d81c0072ac550affbcefefc372cc5562ee52fb220844929`
+ MD5: `65266490c4013b433ec39ee50008116c`

This version includes the following changes:
+ Enable uploading logs when Agent experiences failures during tasking.
+ Fix linux compatability bug in provided network tuning scripts.

### Version 1.0.2677.0
<a name="gs-agent-version-1-0-2677-0"></a>

Release Date: 2023-02-15

End of Support Date: 2024-05-31

The RPM has the following checksums:
+ SHA256: `77cfe94acb00af7ca637264b17c9b21bd7afdc85b99dffdd627aec9e99397489`
+ MD5: `b8533be7644bb4d12ab84de21341adac`

This version includes the following changes:
+ First generally available Agent release.