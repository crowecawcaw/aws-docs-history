# Exporting files using HSM commands

To export an individual file to your data repository and verify the success of the
export, run the following commands. A return value of `states: (0x00000009) exists
 archived` indicates that export was successful.

```
sudo lfs hsm_archive `path/to/export/file`
sudo lfs hsm_state `path/to/export/file`
```

###### Note

You must run the HSM commands (such as `hsm_archive`) as the root
user or using `sudo`.

To export changes on an entire cache or an entire directory in your cache,
run the following commands. If you export multiple files simultaneously,
Amazon File Cache exports your files to your data repository in parallel.

```
nohup find `local/directory` -type f -print0 | xargs -0 -n 1 sudo lfs hsm_archive &
```

To determine whether the export is complete, run the following command.

```
find `path/to/export/file` -type f -print0 | xargs -0 -n 1 -P 8 sudo lfs hsm_state | awk '!/\<archived\>/ || /\<dirty\>/' | wc -l
```

If the command returns with zero files remaining, the export is complete.
