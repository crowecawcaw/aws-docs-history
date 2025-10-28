# Run a single node job in AWS PCS

To run a job using Slurm, you prepare a submission script specifying job requirements and
submit it to a queue with the `sbatch` command. Typically, this is done from a shared
directory so the login and compute nodes have a common space for accessing files.

Connect to the login node of your cluster and run the following commands at its shell
prompt.

- Become the default user. Change to the shared directory.

```
sudo su - ec2-user
cd /shared
```

- Use the following commands to create an example job script:

```
cat << EOF > job.sh
#!/bin/bash
#SBATCH -J single
#SBATCH -o single.%j.out
#SBATCH -e single.%j.err

echo "This is job \${SLURM_JOB_NAME} [\${SLURM_JOB_ID}] running on \${SLURMD_NODENAME}, submitted from \${SLURM_SUBMIT_HOST}" && sleep 60 && echo "Job complete"
EOF
```

- Submit the job script to the Slurm scheduler:

```
sbatch -p demo job.sh
```

- When the job is submitted, it will return a job ID as a number. Use that ID to check the
  job status. Replace `job-id` in the following command with the number
  returned from `sbatch`.

```
squeue --job `job-id`
```

```
squeue --job 1
```

The `squeue` command returns output similar to the following:

```
JOBID PARTITION NAME USER     ST TIME NODES NODELIST(REASON)
1     demo      test ec2-user CF 0:47 1     compute-1
```

- Continue to check the status of the job until it reaches the `R` (running) status. The job
  is done when `squeue` doesn't return anything.
- Inspect the contents of the `/shared` directory.

```
ls -alth /shared
```

The command output is similar to the following:

```
-rw-rw-r- 1 ec2-user ec2-user 107 Mar 19 18:33 single.1.out
-rw-rw-r- 1 ec2-user ec2-user 0 Mar 19 18:32 single.1.err
-rw-rw-r- 1 ec2-user ec2-user 381 Mar 19 18:29 job.sh
```

The files named `single.1.out` and `single.1.err` were written by one of
your cluster's compute nodes. Because the job was run in a shared directory
(`/shared`), they are also available on your login node. This is why you configured
an FSx for Lustre file system for this cluster.

- Inspect the contents of the `single.1.out` file.

```
cat /shared/single.1.out
```

The output is similar to the following:

```
This is job test [1] running on compute-1, submitted from ip-10-3-13-181
Job complete
```
