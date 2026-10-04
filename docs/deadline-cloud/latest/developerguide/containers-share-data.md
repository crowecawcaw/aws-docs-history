

# Share data between the worker session and container
<a name="containers-share-data"></a>

A container has its own filesystem. Mount a worker directory into the container when an action needs files that Deadline Cloud prepared on the worker or when later host actions need files that the container created.


| Storage | Use for | Lifetime and scope | 
| --- | --- | --- | 
| Session working directory | Embedded files, job attachments, temporary files, and job output. | One job session on one worker. | 
| Persistent storage | Container layers, downloaded models, application installations, and reusable caches. | Reusable by later workers in the same service-managed fleet and Availability Zone. It isn't shared concurrently between workers. | 

For session inputs and outputs, see [Share the session working directory](containers-share-session-directory.md). For reusable worker data, see [Mount persistent storage in a container](containers-mount-persistent-storage.md).