

# Upload a job bundle
<a name="share-job-bundles-upload"></a>

To share a job bundle from the command line, upload the bundle directory:

```
deadline bundle upload {{/path/to/job/bundle}}
```

The command packages the directory as an `.ojd` archive and uploads it to the queue:

```
Archiving  [####################################]  100%
Uploading  [####################################]  100%
Uploaded bundle to s3://{{amzn-s3-demo-bucket}}/DeadlineCloud/job-bundles/{{my_render_job}}.ojd
```

By default, the shared bundle takes the name of the bundle directory. To use a different name, pass the `--name` option. You can also upload an `.ojd` archive that you exported earlier instead of a directory.

```
deadline bundle upload {{/path/to/job/bundle}} --name {{my_render_job_v2}}
```

You can also share a bundle while you're submitting a job. In the job submission dialog, choose **Save bundle as**, enter a name, then choose **Queue** as the save location. Choosing **Local** instead exports the bundle to a directory on your workstation.