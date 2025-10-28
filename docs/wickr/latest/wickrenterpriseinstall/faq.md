This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# FAQ

Q: My deployment fails with the following error in helm stderr:

`Error: UPGRADE FAILED: cannot patch "enterprise-init" with kind Job: Job.batch
 "enterprise-init" is invalid: spec.template: Invalid value: core.`

A: This can happen when Debug Logging is enabled. Please disable debug logging, delete the
problematic jobs, and try again.
