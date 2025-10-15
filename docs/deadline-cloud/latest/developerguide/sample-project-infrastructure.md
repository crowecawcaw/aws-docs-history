# Sample project infrastructure

To demonstrate using job attachments and storage profiles, set up a test environment with
 two separate projects. You can use the Deadline Cloud console to create the test resources.

1. If you haven't already, create a test farm. To create a farm, follow the procedure in
 [Create a
 farm](../userguide/farms.md "../userguide/farms.md").
2. Create two queues for jobs in each of the two projects. To create queues, follow the
 procedure in [Create a queue](../userguide/create-queue.md "../userguide/create-queue.md").


	1. Create the first queue called `Q1`. Use the following
	 configuration, use the defaults for all other items.
	
	
	
	
		* For job attachments, choose **Create a new Amazon S3
		 bucket**.
		* Select **Enable association with customer-managed
		 fleets**.
		* For the run as user, enter `jobuser` for both the POSIX
		 user and group.
		* For the queue service role, create a new role named
		 `AssetDemoFarm-Q1-Role`
		* Clear the default Conda queue environment checkbox.
	2. Create the second queue called `Q2`. Use the following
	 configuration, use the defaults for all other items.
	
	
	
	
		* For job attachments, choose **Create a new Amazon S3
		 bucket**.
		* Select **Enable association with customer-managed
		 fleets**.
		* For the run as user, enter `jobuser` for both the POSIX
		 user and group.
		* For the queue service role, create a new role named
		 `AssetDemoFarm-Q2-Role`
		* Clear the default Conda queue environment checkbox.
3. Create a single customer-managed fleet that runs the jobs from both queues. To create
 the fleet, follow the procedure in [Create a customer-managed
 fleet](../userguide/create-a-cmf.md "../userguide/create-a-cmf.md"). Use the following configuration:




	* For **Name**, use `DemoFleet`.
	* For **Fleet type** choose **Customer
	 managed**
	* For **Fleet service role**, create a new role named
	 **AssetDemoFarm-Fleet-Role**.
	* Don't associate the fleet with any queues.
The test environment assumes that there are three file systems shared between hosts using
 network file shares. In this example, the locations have the following names:


* `FSCommon` - contains input job assets that are common to both
 projects.
* `FS1` - contains input and output job assets for project 1.
* `FS2` - contains input and output job assets for project 2.
The test environment also assumes that there are three workstations, as follows:


* `WSAll` - A Linux-based workstation used by developers for all projects.
 The shared file system locations are:




	+ `FSCommon`: `/shared/common`
	+ `FS1`: `/shared/projects/project1`
	+ `FS2`: `/shared/projects/project2`
* `WS1` - A Windows-based workstation used for project 1. The shared file
 system locations are:




	+ `FSCommon`: `S:\`
	+ `FS1`: `Z:\`
	+ `FS2`: Not available
* `WS1` - A macOS-based workstation used for project 2.The shared file
 system locations are:




	+ `FSCommon`: `/Volumes/common`
	+ `FS1`: Not available
	+ `FS2`: `/Volumes/projects/project2`
Finally, define the shared file system locations for the workers in your fleet. The
 examples that follow refer to this configuration as `WorkerConfig`. The shared
 locations are: 


* `FSCommon`: `/mnt/common`
* `FS1`: `/mnt/projects/project1`
* `FS2`: `/mnt/projects/project2`
 You don't need to set up any shared file systems, workstations, or workers that match
 this configuration. The shared locations don't need to exist for the demonstration.
