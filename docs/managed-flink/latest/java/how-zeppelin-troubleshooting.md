Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Troubleshoot Studio notebooks for Managed Service for Apache Flink

This section contains troubleshooting information for Studio notebooks.

## Stop a stuck application

To stop an application that is stuck in a transient state, call the [StopApplication](../apiv2/API_StopApplication.md "../apiv2/API_StopApplication.md")
action with the `Force` parameter set to `true`. For more information, see
[Running Applications](how-running-apps.md "how-running-apps.md")
in the [Managed Service for Apache Flink Developer Guide](../java.md "../java.md").

## Deploy as an application with

durable state in a VPC with no internet access

The Managed Service for Apache Flink Studio deploy-as-application function does not support VPC applications without internet access. We recommend that you build your application in Studio,
and then use Managed Service for Apache Flink to manually create a Flink application and select the zip file you built in your Notebook.

The following steps outline this approach:

1. Build and export your Studio application to Amazon S3. This should be a zip file.
2. Create a Managed Service for Apache Flink application manually with code path referencing the zip file location in Amazon S3. In addition, you will need to configure the application with the following `env` variables (2 `groupID`, 3 `var` in total):
3. kinesis.analytics.flink.run.options
   1. python: source/note.py
   2. jarfile: lib/PythonApplicationDependencies.jar

4. managed.deploy_as_app.options
   1. DatabaseARN: `<glue database ARN (Amazon Resource Name)>`

5. You may need to give permissions to the Managed Service for Apache Flink Studio and Managed Service for Apache Flink IAM roles for the services your application uses. You can use the same IAM role for both apps.

## Deploy-as-app size and build time reduction

Studio deploy-as-app for Python applications packages everything available in the Python environment because we cannot determine which libraries you need. This may result in a larger-than necessary deploy-as-app size. The following procedure demonstrates how to reduce the size of the deploy-as-app Python application size by
uninstalling dependencies.

If you’re building a Python application with deploy-as-app feature from Studio, you might consider removing pre-installed Python packages from the system if your applications are not depending on. This will not only help to reduce the final artifact size to avoid breaching the service limit for application size, but also improve the build time of applications with the deploy-as-app feature.

You can execute following command to list out all installed Python packages with their respective installed size and selectively remove packages with significant size.

```
%flink.pyflink

!pip list --format freeze | awk -F = {'print $1'} | xargs pip show | grep -E 'Location:|Name:' | cut -d ' ' -f 2 | paste -d ' ' - - | awk '{gsub("-","_",$1); print $2 "/" tolower($1)}' | xargs du -sh 2> /dev/null | sort -hr
```

###### Note

`apache-beam` is required by Flink Python to operate. You should never remove this package and its dependencies.

Following is the list of pre-install Python packages in Studio V2 which can be considered for removal:

```
scipy
statsmodels
plotnine
seaborn
llvmlite
bokeh
pandas
matplotlib
botocore
boto3
numba
```

###### To remove a Python package from Zeppelin notebook:

1. Check if your application depends on the package, or any of its consuming packages, before removing it. You can identify dependants of a package using [pipdeptree](https://pypi.org/project/pipdeptree/ "https://pypi.org/project/pipdeptree/").
2. Executing following command to remove a package:

```
%flink.pyflink
!pip uninstall -y <package-to-remove>
```

3. If you need to retrieve a package which you removed by mistake, executing the following command:

```
%flink.pyflink
!pip install <package-to-install>
```

###### Example: Remove scipy package before deploying your Python application with deploy-as-app feature.

1. Use `pipdeptree` to discover all `scipy` consumers and verify if you can safely remove `scipy`.
   - Install the tool through notebook:

   ```
   %flink.pyflink
   !pip install pipdeptree
   ```

   - Get reversed dependency tree of `scipy` by running:

   ```
   %flink.pyflink
   !pip -r -p scipy
   ```

   You should see output similar to the following (condensed for brevity):

   ```
   ...
   ------------------------------------------------------------------------
   scipy==1.8.0
   ├── plotnine==0.5.1 [requires: scipy>=1.0.0]
   ├── seaborn==0.9.0 [requires: scipy>=0.14.0]
   └── statsmodels==0.12.2 [requires: scipy>=1.1]
       └── plotnine==0.5.1 [requires: statsmodels>=0.8.0]
   ```

2. Carefully inspect the usage of `seaborn`, `statsmodels` and `plotnine` in your applications.
   If your applications do not depend on any of `scipy`, `seaborn`, `statemodels`, or `plotnine`, you can remove all of these packages, or only ones which your applications don’t need.
3. Remove the package by running:

```
!pip uninstall -y scipy plotnine seaborn statemodels
```

## Cancel jobs

This section shows you how to cancel Apache Flink jobs that you can't get to from
Apache Zeppelin. If you want to cancel such a job, go to the Apache Flink dashboard,
copy the job ID, then use it in one of the following examples.

To cancel a single job:

```
%flink.pyflink
import requests

requests.patch("https://zeppelin-flink:8082/jobs/[job_id]", verify=False)
```

To cancel all running jobs:

```
%flink.pyflink
import requests

r = requests.get("https://zeppelin-flink:8082/jobs", verify=False)
jobs = r.json()['jobs']

for job in jobs:
    if (job["status"] == "RUNNING"):
        print(requests.patch("https://zeppelin-flink:8082/jobs/{}".format(job["id"]), verify=False))
```

To cancel all jobs:

```
%flink.pyflink
import requests

r = requests.get("https://zeppelin-flink:8082/jobs", verify=False)
jobs = r.json()['jobs']

for job in jobs:
    requests.patch("https://zeppelin-flink:8082/jobs/{}".format(job["id"]), verify=False)
```

## Restart the Apache Flink interpreter

To restart the Apache Flink interpreter within your Studio notebook

1. Choose **Configuration** near the top right corner of the screen.
2. Choose **Interpreter**.
3. Choose **restart** and then
   **OK**.
