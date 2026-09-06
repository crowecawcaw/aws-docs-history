

# Deploy and configure custom software on workers
<a name="deploy-custom-software"></a>

AWS Deadline Cloud provides multiple methods to deploy and configure custom software, plugins, and tools on your workers. The method you choose depends on your requirements, such as whether you need administrator privileges, how often the software changes, and whether the software should be available to all jobs or only specific jobs.

## Choose a deployment method
<a name="deploy-custom-software-choose"></a>

Use the following table to choose the right deployment method for your use case.


| Criteria | Queue environment | Host configuration script | Custom conda package | 
| --- | --- | --- | --- | 
| Administrator privileges required | No | Yes | No | 
| When it runs | Session start | Worker startup | Session start | 
| Scope | Per queue or job | All workers in fleet | Per queue or job | 
| Can be controlled by job submission | Yes | No | Yes | 
| Setup complexity | Low | Medium | High | 
| Best for | Simple plugins, scripts, environment variables | System drivers, Docker, storage mounts | Complex applications with dependencies | 

**Quick decision guide:**
+ *Need administrator or root privileges?* Use a [host configuration script](smf-admin.md).
+ *Simple plugin or script without admin rights?* Use a [queue environment](configure-jobs.md).
+ *Complex application with version control needs?* Create a [custom conda package](configure-jobs-s3-channel.md).