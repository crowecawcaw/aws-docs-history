# Clean up a conda

environment

Cleaning up conda environments that you’re not using can help free up disk space
and improve performance. Use the following template to clean up a conda
environment:

```

# list your environments to select an environment to clean
conda info --envs # or conda info -e

# once you've selected your environment to purge
conda remove --name test-env --all

# run conda environment list to ensure the target environment is purged
conda info --envs # or conda info -e

```
