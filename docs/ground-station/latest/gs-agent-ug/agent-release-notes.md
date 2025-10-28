# Agent release notes

## Latest Agent Version

### Version 1.0.3555.0

Release Date: 03/27/2024

RPM Checksums:

- SHA256: `108f3aceb00e5af549839cd766c56149397e448a6e1e1429c89a9eebb6bc0fc1`
- MD5: `65b72fa507fb0af32651adbb18d2e30f`

Changes:

- Add Agent metric for selected executable version during tasking startup.
- Add config file support for avoiding specific executable versions when other versions are available.
- Add network and routing diagnostics.
- Additional security features.
- Fix issue where some metric reporting errors were written to stdout/journal instead of log file.
- Gracefully handle network unreachable socket errors.
- Measure packet loss and latency between source and destination agents.
- Release aws-gs-datapipe version 2.0 to support new protocol features and the ability to transparently upgrade contacts to the new protocol.

## Deprecated Agent Versions

### Version 1.0.2942.0

Release Date: 06/26/2023

End of Support Date: 05/31/2024

RPM Checksums:

- SHA256: `7d94b642577504308a58bab28f938507f2591d4e1b2c7ea170b77bea97b5a9b6`
- MD5: `661ff2b8f11aba5d657a6586b56e0d8f`

Changes:

- Added error logs for when Agent RPM is updated on disk and needs Agent restart for changes to take effect.
- Added network tuning validation to ensure Agent user guide tuning steps are followed and applied correctly.
- Fix bug that caused erroneous warnings in Agent logs about log archival.
- Improved packet loss detection.
- Updated Agent install to prevent install or upgrade of the RPM if the Agent is already running.

### Version 1.0.2716.0

Release Date: 03/15/2023

End of Support Date: 05/31/2024

RPM Checksums:

- SHA256: `cb05b6a77dfcd5c66d81c0072ac550affbcefefc372cc5562ee52fb220844929`
- MD5: `65266490c4013b433ec39ee50008116c`

Changes:

- Enable uploading logs when Agent experiences failures during tasking.
- Fix linux compatability bug in provided network tuning scripts.

### Version 1.0.2677.0

Release Date: 02/15/2023

End of Support Date: 05/31/2024

RPM Checksums:

- SHA256: `77cfe94acb00af7ca637264b17c9b21bd7afdc85b99dffdd627aec9e99397489`
- MD5: `b8533be7644bb4d12ab84de21341adac`

Changes:

- First generally available Agent release.
