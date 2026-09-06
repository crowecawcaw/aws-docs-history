# Pip queue environment for Deadline Cloud

The pip\_queue\_env.yaml queue environment provides Python packages to jobs
using pip and the standard library venv module, rather than a package
manager such as conda or Rez. For more information about the queue environment, see
[pip\_queue\_env.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/pip_queue_env.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/pip_queue_env.yaml")
on the GitHub website. For more information about pip, see
[pip](https://pip.pypa.io/ "https://pip.pypa.io/") on the pip website. For more information about venv, see
[venv](https://docs.python.org/3/library/venv.html "https://docs.python.org/3/library/venv.html") on
the Python website.

When a job provides a `PipPackages` parameter value, the
queue environment creates a Python virtual environment in the session
working directory, installs the requested packages into it with pip, and
activates it so that the job's steps run with those packages available.
If `PipPackages` is empty, the queue environment does nothing,
so you can add it to a queue that also runs jobs that don't use it.

The `PipIndexUrl` and `PipExtraIndexUrls`
parameters let jobs install from a private package index, such as an
[AWS
CodeArtifact](../../../codeartifact/latest/ug/welcome.md "../../../codeartifact/latest/ug/welcome.md") repository, instead of the default
[PyPI](https://pypi.org/ "https://pypi.org/") index on the PyPI website.

Unlike conda and Rez, pip and venv are included with Python itself, so
worker hosts only need a `python3` (or `python`)
interpreter on the `PATH`. Deadline Cloud service-managed fleets provide
one.

The
[pip\_package\_job](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/pip_package_job "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/pip_package_job")
job bundle on the GitHub website shows how to submit a job that uses this queue environment. For
a job bundle that defines the same pip environment inline without a queue
environment, see [pip\_self\_contained\_job](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/pip_self_contained_job "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/pip_self_contained_job") on the GitHub website.
