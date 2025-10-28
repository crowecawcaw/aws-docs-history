# Job queue template

The following is an empty job queue template. You can use this template to create your job
queue. You can then save this job queue to a file and use it with the AWS CLI
`--cli-input-json` option. For more information about these parameters, see [CreateJobQueue](../APIReference/API_CreateJobQueue.md "../APIReference/API_CreateJobQueue.md") in the _AWS Batch API Reference_.

###### Note

You can generate a job queue template with the following AWS CLI command.

```
$ `aws batch create-job-queue --generate-cli-skeleton`
```

```
{
   "computeEnvironmentOrder": [
      {
         "computeEnvironment": "",
         "order": 0
      }
   ],
   "jobQueueName": "",
   "jobStateTimeLimitActions": [
      {
         "state": "RUNNABLE",
         "action": "CANCEL",
		 "maxTimeSeconds": 0,
         "reason": ""

      }
   ],
   "priority": 0,
   "schedulingPolicyArn": "",
   "state": "ENABLED",
   "tags": {
      "KeyName": ""
   }
}
```
