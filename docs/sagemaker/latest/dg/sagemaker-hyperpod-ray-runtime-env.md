# Managing dependencies with runtime\_env

Ray `runtime_env` installs pip packages and ships a working directory to the
cluster at run time. You add a dependency without rebuilding a container image, which keeps
interactive development fast.

## Inject dependencies interactively

Pass `runtime_env` to `ray.init()`. Ray installs the packages
and uploads the working directory to the cluster before your code runs.

```
import ray

ray.init(runtime_env={
    "pip": ["pandas==2.2.2", "scikit-learn"],
    "working_dir": "`./src`",
})
```

## Inject dependencies for a submitted job

For a job you submit from the command line, pass the same environment with
`--working-dir` and `--runtime-env-json`.

```
ray job submit \
    --address sagemaker_ray://`my-cluster`/`my-namespace` \
    --working-dir `./src` \
    --runtime-env-json '{"pip": ["pandas==2.2.2", "scikit-learn"]}' \
    -- python `my-script.py`
```

For the full set of `runtime_env` fields, including conda environments and
environment variables, see [Ray runtime
environments](https://docs.ray.io/en/latest/ray-core/handling-dependencies.html "https://docs.ray.io/en/latest/ray-core/handling-dependencies.html") in the Ray documentation.
