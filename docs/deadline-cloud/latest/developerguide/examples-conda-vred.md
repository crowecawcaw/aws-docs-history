

# Build an Autodesk VRED Core conda package for Deadline Cloud
<a name="examples-conda-vred"></a>

The samples repository on the GitHub website includes the following VRED conda recipes:
+ [vredcore-2025](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/vredcore-2025)
+ [vredcore-2026](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/vredcore-2026)

Submit the build:

```
./submit-package-job vredcore-2026
```

For a job bundle that uses this package, see [Render Autodesk VRED scenes on Deadline Cloud](examples-jb-vred-render.md).