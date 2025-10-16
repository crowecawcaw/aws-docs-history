# Test the configuration of your worker host

After you have installed the worker agent, installed the software necessary to process your
 jobs, and configured the AWS credentials for the worker agent, you should test that the
 installation can process your jobs before creating an AMI for your fleet. You should test the
 following:


* The Deadline Cloud worker agent is properly configured to run as a system service.
* That the worker polls the associated queue for work.
* That the worker successfully processes jobs sent to the queue associated with the
 fleet.
After you test the configuration and can successfully process representative jobs, you can
 use the configured worker to create an AMI for Amazon EC2 workers, or as a model for your
 on-premises workers.

###### Note

If you are testing the worker host configuration of an auto scaling fleet, you may have
 difficulty testing your worker in the following situations: 


* If there is no work in the queue, Deadline Cloud stops the worker agent shortly after the
 worker starts.
* If the worker agent is configured to shut down the host when stopping, the agent shuts
 down the machine if there is no work in the queue.
To avoid these issues, use a staging fleet that doesn't auto scale to configure and test
 your workers. After testing the worker host, be sure to set the correct fleet ID before baking
 an AMI.

###### To test your worker host configuration

1. Run the worker agent by starting the operating system service.



Linux
From a root shell run the following command:



```
systemctl start deadline-worker
```


Windows
From an administrator command prompt or PowerShell terminal, enter
 the following command:



```
sc.exe start DeadlineWorker
```
2. Monitor the worker to make sure it starts and polls for work.



Linux
From a root shell run the following command:



```
systemctl status deadline-worker
```

The command should return a response like:



```
Active: active (running) since Wed 2023-06-14 14:44:27 UTC; 7min ago
```

If the response doesn't look like that, inspect the log file using the following
 command:



```
tail -n 25 /var/log/amazon/deadline/worker-agent.log
```


Windows
From an administrator command prompt or PowerShell terminal, enter
 the following command:



```
sc.exe query DeadlineWorker
```

The command should return a response like:



```
STATE   : 4 RUNNING
```

If the response doesn't contain `RUNNING`, inspect the worker log file.
 Open and administrator PowerShell prompt and run the following
 command:



```
Get-Content -Tail 25 -Path $env:PROGRAMDATA\Amazon\Deadline\Logs\worker-agent.log
```
3. Submit jobs to queue associated with your fleet. The jobs should be representative of
 the jobs that the fleet processes.
4. Monitor the progress of the job [using the Deadline Cloud monitor](../userguide/view-logs.md "../userguide/view-logs.md") or
 CLI. If a job fails, check the session and worker logs.
5. Update the configuration of the worker host as needed until jobs complete
 successfully.
6. When the test jobs succeed you can stop the worker:



Linux
From a root shell run the following command:



```
systemctl stop deadline-worker
```


Windows
From an administrator command prompt or PowerShell terminal, enter
 the following command:



```
sc.exe stop DeadlineWorker
```
