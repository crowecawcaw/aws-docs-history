

# Build an AutoDock Vina conda package for Deadline Cloud
<a name="examples-conda-autodock-vina"></a>

The [autodock-vina-1.2.5](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/autodock-vina-1.2.5) rattler-build recipe on the GitHub website packages [AutoDock Vina](https://github.com/ccsb-scripps/AutoDock-Vina), an open-source molecular docking program that predicts how small molecules (drug candidates) bind to a protein target. The package downloads the pre-built Linux x86\_64 binary from the GitHub release and installs it as the `vina` command.

Submit the build from the `conda_recipes` directory:

```
./submit-package-job autodock-vina-1.2.5
```

For a job bundle that uses this package to run parallel virtual screening campaigns, see [Run virtual screening with AutoDock Vina on Deadline Cloud](examples-jb-virtual-screening.md).