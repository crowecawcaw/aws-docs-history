

# Build an AYON Launcher conda package for Deadline Cloud
<a name="examples-conda-ayon"></a>

The [ayon-launcher](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/ayon-launcher) rattler-build recipe on the GitHub website packages the [AYON Launcher](https://github.com/ynput/ayon-launcher) as a conda package. The package provides the pipeline runtime needed for headless publishing on Deadline Cloud workers. It repackages the pre-built AYON Launcher release (cx\_Freeze binary) containing the Python 3.11 runtime, `ayon-python-api`, and core launcher logic.

The conda package provides only the runtime environment. The studio-specific bundle (addons and dependency package) is delivered separately through Deadline Cloud job attachments. This separation means the conda package rarely changes and no rebuild is needed when addons are updated.

The recipe builds for Linux (`linux-64`) directly from GitHub releases. For Windows (`win-64`), extract the installer on a Windows machine and place the resulting zip in `conda_recipes/archive_files`. Refer to the recipe's README for exact steps.

Submit the build from the `conda_recipes` directory:

```
./submit-package-job ayon-launcher
```

At runtime, the job must provide the following environment variables:
+ `AYON_SERVER_URL` — URL of the AYON server.
+ `AYON_API_KEY` — API key for server authentication.
+ `AYON_BUNDLE_NAME` — Bundle name to resolve addons from.