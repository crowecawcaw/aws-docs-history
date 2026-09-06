

# Troubleshooting Amazon Braket
<a name="braket-troubleshooting"></a>

Use the troubleshooting information and solutions in this section to help resolve issues with Amazon Braket.

**Topics**
+ [AccessDeniedException](#braket-troubleshooting-access-denied)
+ [An error occurred (ValidationException) when calling the CreateQuantumTask operation](#braket-troubleshooting-create-fail)
+ [An SDK feature does not work](#braket-troubleshooting-sdk)
+ [Hybrid job fails due to ServiceQuotaExceededException](#braket-jobs-quota-troubleshoot)
+ [Components stopped working in notebook instance](#braket-troubleshooting-notebook-issue)
+ [Troubleshooting Python 3.12 Upgrade](braket-troubleshooting-python312.md)
+ [Troubleshooting OpenQASM](braket-troubleshooting-openqasm.md)

## AccessDeniedException
<a name="braket-troubleshooting-access-denied"></a>

If you receive an **AccessDeniedException** when enabling or using Braket, you are likely attempting to enable or use Braket in a region where your restricted role does not have access.

In such cases, contact your internal AWS administrator to understand which of the following conditions apply:
+ If there are role restrictions preventing access to a region.
+ If the role you are attempting to use is permitted to use Braket.

If your role does not have access to a given region when using Braket, then you will be unable to use devices in that particular region.

## An error occurred (ValidationException) when calling the CreateQuantumTask operation
<a name="braket-troubleshooting-create-fail"></a>

If you receive an error similar to: `An error occurred (ValidationException) when calling the CreateQuantumTask operation: Caller doesn't have access to amazon-braket-…​` Check that you are referring to an existing s3\_folder. Braket does not auto create new Amazon S3 buckets and prefixes for you.

If you are accessing the API directly and receiving an error similar to: `Failed to create quantum task: Caller doesn't have access to s3://MY_BUCKET` Check that you are not including `s3://` in the Amazon S3 bucket path.

## An SDK feature does not work
<a name="braket-troubleshooting-sdk"></a>

Your Python version must be 3.10 or above. For Amazon Braket Hybrid Jobs, we recommend Python 3.12.

Verify your SDK and schemas are up-to-date. To update the SDK from the notebook or your python editor, run the following command:

```
pip install amazon-braket-sdk --upgrade --upgrade-strategy eager
```

To update the schemas, run the following command:

```
pip install amazon-braket-schemas --upgrade
```

If you are accessing Amazon Braket from your own client, verify your [AWS Region](https://docs.aws.amazon.com/braket/latest/developerguide/braket-devices.html#braket-regions) is set to a region supported by Amazon Braket.

## Hybrid job fails due to ServiceQuotaExceededException
<a name="braket-jobs-quota-troubleshoot"></a>

A hybrid job running quantum tasks against the Amazon Braket simulators can fail to be created if you exceed the concurrent quantum task limit for the simulator device you are targeting. For more information on the service limits, see the [Quotas](braket-quotas.md) topic.

 If you are running concurrent tasks against a simulator device in multiple hybrid jobs from your account, you could encounter this error.

To see the number of concurrent quantum tasks against a specific simulator device, use the `search-quantum-tasks` API, as shown in the following code example.

```
DEVICE_ARN=arn:aws:braket:::device/quantum-simulator/amazon/sv1
task_list=""
for status_value in "CREATED" "QUEUED" "RUNNING" "CANCELLING"; do
    tasks=$(aws braket search-quantum-tasks --filters name=status,operator=EQUAL,values=${status_value} name=deviceArn,operator=EQUAL,values=$DEVICE_ARN --max-results 100 --query 'quantumTasks[*].quantumTaskArn' --output text)
    task_list="$task_list $tasks"
done;
echo "$task_list" | tr -s ' \t' '[\n*]' | sort | uniq
```

You can also view the created quantum tasks against a device using Amazon CloudWatch metrics: ** Braket ** > **By Device**.

**To avoid running into these errors:**

1. Request a service quota increase for the number of concurrent quantum tasks for the simulator device. This is only applicable to the SV1 device.

1. Handle `ServiceQuotaExceeded` exceptions in your code and retry.

## Components stopped working in notebook instance
<a name="braket-troubleshooting-notebook-issue"></a>

If some components of your notebook stop working, try the following:

1. Download any notebooks you created or modified to a local drive.

1. Stop your notebook instance.

1. Delete your notebook instance.

1. Create new notebook instance with a different name.

1. Upload the notebooks to the new instance.