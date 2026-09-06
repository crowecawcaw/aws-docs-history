

# Troubleshooting node lifecycle actions in AWS PCS
<a name="cng-node-lifecycle-actions-troubleshooting"></a>

Use this troubleshooting information to resolve common node lifecycle action issues.


| **Symptom** | **Likely cause** | **What to do** | 
| --- | --- | --- | 
| Node terminates during launch | A `nodeBootstrapped` or `nodeReady` script exited non-zero with `onError=TERMINATE` | Check `/var/log/amazon/pcs/lifecycle/actions/<stage>/<name>.log`. Set `onError=STOP_SEQUENCE` temporarily to keep the node for debugging. | 
| Script download fails | Missing `s3:GetObject`, no network egress, or wrong URL | Verify the instance IAM role and VPC routing or endpoints; confirm the URL and (for S3) `s3VersionId`. | 
| Checksum mismatch | Script content changed or is corrupt | Regenerate the SHA-256 and update the configuration, or remove the checksum while iterating. | 
| Node never becomes ready | Scripts exceed the approximately 30-minute registration window | Move long installs to the AMI or a shared file system; split work across stages. | 
| Updated script not applied | `CACHE_ONCE` keeps the original copy | Use `REFRESH_ON_REBOOT`, or replace the instance. | 
| Script didn't re-run after reboot | `executionPolicy` is `FIRST_BOOT_ONLY` (default) | Set `executionPolicy=EVERY_BOOT` for scripts that must run on every boot. | 
| `sinfo` or `scontrol` not found in a script | The script runs in the `nodeBootstrapped` stage, before `slurmd` | Move Slurm-dependent work to the `nodeReady` stage. | 
| Can't see logs after termination | Logs are local to the instance | Add a node bootstrapped script that forwards logs to Amazon CloudWatch. | 