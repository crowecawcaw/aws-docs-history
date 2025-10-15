# Run the Deadline Cloud worker agent

Before you can run the jobs you submit to the queue on your developer farm, you must run
 the AWS Deadline Cloud worker agent in developer mode on a worker host.

Throughout the remainder of this tutorial, you will perform AWS CLI operations on your
 developer farm using two AWS CloudShell tabs. In the first tab, you can submit jobs. In the second
 tab, you can run the worker agent.

###### Note

If you leave your CloudShell session idle for more than 20 minutes, it will timeout
 and stop the worker agent. To restart the worker agent, follow the instructions in the
 following procedure.

Before you can start a worker agent, you must set up a Deadline Cloud farm, queue, and fleet. See
 [Create a Deadline Cloud farm](create-a-farm.md "create-a-farm.md").

**To run the worker agent in developer mode**

1. With your farm still open in the first CloudShell tab, open a second
 CloudShell tab, then create the `demoenv-logs` and
 `demoenv-persist` directories.



```
`mkdir ~/demoenv-logs 
mkdir ~/demoenv-persist`
```
2. Download and install the Deadline Cloud worker agent packages from PyPI:


###### Note

On Windows, it is required that the agent files are installed
 into Pythonâs global site-packages directory. Python virtual environments are
 not currently supported.



```
`python -m pip install deadline-cloud-worker-agent`
```
3. To allow the worker agent to create the temporary directories for running jobs,
 create a directory:



```
`sudo mkdir /sessions
sudo chmod 750 /sessions
sudo chown cloudshell-user /sessions`
```
4. Run the Deadline Cloud worker agent in developer mode with the variables
 `DEV_FARM_ID` and `DEV_CMF_ID` that you added to the
 `~/.bashrc`.



```
`deadline-worker-agent \
 --farm-id $DEV_FARM_ID \
 --fleet-id $DEV_CMF_ID \
 --run-jobs-as-agent-user \
 --logs-dir ~/demoenv-logs \
 --persistence-dir ~/demoenv-persist`
```

As the worker agent initializes and then polls the
 `UpdateWorkerSchedule` API operation the following output is
 displayed:



```
INFO    Worker Agent starting
[2024-03-27 15:51:01,292][INFO    ] ð Worker Agent starting
[2024-03-27 15:51:01,292][INFO    ] AgentInfo 
Python Interpreter: /usr/bin/python3
Python Version: 3.9.16 (main, Sep  8 2023, 00:00:00)  - [GCC 11.4.1 20230605 (Red Hat 11.4.1-2)]
Platform: linux
...
[2024-03-27 15:51:02,528][INFO    ] ð¥ API.Resp ð¥ [deadline:UpdateWorkerSchedule](200) params={'assignedSessions': {}, 'cancelSessionActions': {}, 'updateIntervalSeconds': 15} ...
[2024-03-27 15:51:17,635][INFO    ] ð¥ API.Resp ð¥ [deadline:UpdateWorkerSchedule](200) params=(Duplicate removed, see previous response) ...
[2024-03-27 15:51:32,756][INFO    ] ð¥ API.Resp ð¥ [deadline:UpdateWorkerSchedule](200) params=(Duplicate removed, see previous response) ...
...

```
5. Select your first CloudShell tab, then list the workers in the fleet.



```
`deadline worker list --fleet-id $DEV_CMF_ID`

```

Output such as the following is displayed:



```
Displaying 1 of 1 workers starting at 0

- workerId: worker-8c9af877c8734e89914047111f
  status: STARTED
  createdAt: 2023-12-13 20:43:06+00:00

```
In a production configuration, the Deadline Cloud worker agent requires setting up multiple users
 and configuration directories as an administrative user on the host machine. You can
 override these settings because you're running jobs in your own development farm, which only
 you can access.


## Next steps


Now that a worker agent is running on your worker hosts, you can send jobs to your
 workers. You can:



* [Submit with Deadline Cloud](submit-a-job.md "submit-a-job.md") using a simple
 OpenJD job bundle.
* [Submit jobs with job attachments in Deadline Cloud](run-jobs-job-attachments.md "run-jobs-job-attachments.md") that share files between
 workstations using different operating systems.
