# Using PyFlink

Amazon EMR on EKS releases 6.15.0 and higher supports PyFlink. If you already have a PyFlink script, you can do one of the following:

- Create a custom image with your PyFlink script included.
- Upload your script to an Amazon S3 location
  If you don't already have a script, you can use the following example to launch a PyFlink job. This example retrieves the script from S3. If you're using
  a custom image with your script already included in the image, you must update the script path to the location of where you stored your script. If the script
  is in an S3 location, Amazon EMR on EKS will retrieve the script and place it under the `/opt/flink/usrlib/` directory in the Flink container.

```
apiVersion: flink.apache.org/v1beta1
kind: FlinkDeployment
metadata:
  name: python-example
spec:
  flinkVersion: v1_17
  flinkConfiguration:
    taskmanager.numberOfTaskSlots: "1"
  executionRoleArn: `job-execution-role`
  emrReleaseLabel: "emr-6.15.0-flink-latest"
  jobManager:
    highAvailabilityEnabled: false
    replicas: 1
    resource:
      memory: "2048m"
      cpu: 1
  taskManager:
    resource:
      memory: "2048m"
      cpu: 1
  job:
    jarURI: s3://`S3 bucket with your script`/`pyflink-script.py`
    entryClass: "org.apache.flink.client.python.PythonDriver"
    args: ["-py", "/opt/flink/usrlib/`pyflink-script.py`"]
    parallelism: 1
    upgradeMode: stateless
```
