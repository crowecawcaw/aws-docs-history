

# Develop a job bundle through four stages on Deadline Cloud
<a name="examples-jb-job-progression"></a>

The [job\_dev\_progression](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_dev_progression) directory on the GitHub website contains a sequence of four job bundle development stages. As you add more options and split a workload into smaller parallel pieces, the complexity of the job grows. The four stages start with a single self-contained template and end at a Python package bundled with script entry points and unit tests. The sample is built around Python, but the ideas are not Python-specific.

Submit the first stage to your farm:

```
deadline bundle submit stage_1_self_contained_template
```

You can also run jobs locally for development with the [Open Job Description CLI](https://github.com/OpenJobDescription/openjd-cli) on the GitHub website.

```
openjd run stage_1_self_contained_template/template.yaml
```

To use a queue environment locally to provide conda packages, pass the `--environment` option:

```
openjd run --environment ../../queue_environments/conda_queue_env_from_console.yaml \
    stage_1_self_contained_template/template.yaml
```