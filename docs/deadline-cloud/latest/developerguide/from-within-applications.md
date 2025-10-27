# Submit a job within an application

To make it easy for users to submit jobs, you can use the scripting runtimes or plugin
systems provided by an application. Users have a familiar interface and you can create powerful
tools that assist the users when submitting a workload.

## Embed job bundles in an application

This example demonstrates submitting job bundles that you make available in the
application.

To give a user access to these job bundles, create a script embedded in a menu item that
launches the Deadline Cloud CLI.

The following script enables a user to select the job bundle:

```
deadline bundle gui-submit --install-gui
```

To use a specific job bundle in a menu item instead, use the following:

```
deadline bundle gui-submit `</path/to/job/bundle>` --install-gui
```

This opens a dialog where the user can modify the job parameters, inputs, and outputs,
and then submit the job. You can have different menu items for different job bundles for a user
to submit in an application.

If the job that you submit with a job bundle contains similar parameters and asset
references across submissions, you can fill in the default values in the underlying job bundle.

## Get information from an application

To pull information from an application so that users don't have to manually add it to the
submission, you can integrate Deadline Cloud with the application so that your users can submit jobs
using a familiar interface without needing exit the application or use command line
tools.

If your application has a scripting runtime that supports Python and pyside/pyqt, you can
use the GUI components from the [Deadline Cloud client library](https://github.com/aws-deadline/deadline-cloud "https://github.com/aws-deadline/deadline-cloud") to create a UI. For an example, see [Deadline Cloud for Maya
integration](https://github.com/aws-deadline/deadline-cloud-for-maya "https://github.com/aws-deadline/deadline-cloud-for-maya") on GitHub.

The Deadline Cloud client library provides operations that do the following to help you provide a
strong integrated user experience:

- Pull queue environment parameters, job parameters, and asset references form environment
  variables and by calling the application SDK.
- Set the parameters in the job bundle. To avoid modifying the original bundle, you should
  make a copy of the bundle and submit the copy.

If you use the `deadline bundle gui-submit` command to submit the job bundle,
you must programmatically the `parameter_values.yaml` and
`asset_references.yaml` files to pass the information from the application. For
more information about these files see [Open Job Description (OpenJD) templates for Deadline Cloud](build-job-bundle.md "build-job-bundle.md").

If you need more complex controls than the ones offered by OpenJD, need to abstract the
job from the user, or want to make the integration match the application's visual style, you
can write your own dialog that calls the Deadline Cloud client library to submit the job.
