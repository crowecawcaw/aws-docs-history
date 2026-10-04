

# Submitting files with a job
<a name="submitting-files-with-a-job"></a>

A job bundle defines its job attachments in two places:
+ **`PATH` job parameters** in the job template. A parameter's `dataFlow` property marks its value as an input (`IN`), an output (`OUT`), or both (`INOUT`). Its `objectType` property says whether the value is a `FILE` or a `DIRECTORY`. For more information, see [JobPathParameterDefinition](https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#22-jobpathparameterdefinition) in the [Open Job Description specification](https://github.com/OpenJobDescription/openjd-specifications) on the GitHub website.
+ **The asset references file** (`asset_references.yaml` or `asset_references.json`), which lists input files, input directories, and output directories. For more information, see [Asset references elements for job bundles](build-job-bundle-assets.md).

The Deadline Cloud [integrated submitter plugins](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/jobs-using-submitter.html) automatically find the files that your scene references. The plugins list these files on the submitter's **Job attachments** tab, where you can add any files or directories that the submitter didn't find. To open the same tab for a job bundle of your own, use the `deadline bundle gui-submit` command.

The following image shows the **Job attachments** tab. It lists the input files, input directories, and output directory that the submitter detected automatically.

![The Job attachments tab of a submitter, listing automatically detected input files, input directories, and an output directory.](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/images/bundle-gui-submit-job-attachments.png)


The following topics show how job attachments handles these files, using the [job\_attachments\_devguide job bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_attachments_devguide) on the GitHub website.

**Topics**
+ [How Deadline Cloud uploads files to Amazon S3](what-job-attachments-uploads-to-amazon-s3.md)
+ [How Deadline Cloud chooses the files to upload](how-job-attachments-decides-what-to-upload-to-amazon-s3.md)
+ [How jobs find job attachment input files](how-jobs-find-job-attachments-input-files.md)