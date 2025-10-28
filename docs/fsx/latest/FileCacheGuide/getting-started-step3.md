# Step 3: Run your analysis

Now that your cache is created and mounted to a compute instance, you can use it to run
your high-performance compute workload. The workload loads data from the Amazon S3 data repository
as files are accessed by your workload.

After you run the workload, you can export the data that you write to your cache back to
your Amazon S3 bucket at any time. From a terminal on one of your compute instances, run the
following command to export a file to your Amazon S3 bucket.

```
sudo lfs hsm_archive `file_name`
```

For more information about how to run this command on a folder or large collection of
files quickly, see [Exporting files using HSM commands](exporting-files-hsm.md "exporting-files-hsm.md").
