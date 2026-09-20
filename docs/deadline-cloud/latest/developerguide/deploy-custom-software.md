

# Deploy and configure custom software on workers
<a name="deploy-custom-software"></a>

AWS Deadline Cloud provides multiple methods to deploy and configure custom software, plugins, and tools on your workers. The method you choose depends on your requirements, such as whether you need administrator privileges, how often the software changes, and whether the software should be available to all jobs or only specific jobs.

## Choose a deployment method
<a name="deploy-custom-software-choose"></a>

Use the following table to choose the right deployment method for your use case.


| Criteria | Plugin sync | Queue environment | Host configuration | Custom conda package | 
| --- | --- | --- | --- | --- | 
| Fleet support | Service-managed fleets; customer-managed fleets with a supporting conda package | Service-managed and customer-managed fleets | Service-managed fleet: host configuration script; customer-managed fleet: manual worker configuration | Service-managed and customer-managed fleets with a conda queue environment | 
| Administrator privileges required | No | No | Yes | No | 
| When it runs | Conda activation at session start | Session start | Service-managed fleet: worker startup; customer-managed fleet: before the worker joins the fleet | Session start | 
| Scope | Per queue, application, and version | Per queue or job | All workers in fleet | Per queue or job | 
| Can be controlled by job submission | Application and version selection | Yes | No | Yes | 
| Setup complexity | Low | Low | Medium | High | 
| Best for | Simple file-based plugins for supported applications | Simple plugins, scripts, and environment variables | System drivers, containers, and storage mounts | Applications or plugins with dependencies | 

**Quick decision guide:**
+ *Simple application plugin that plugin sync supports?* Start with [Use custom plugins with Deadline Cloud](custom-plugins.md).
+ *Need administrator or root privileges?* For a service-managed fleet, use a [host configuration script](smf-admin.md). For a customer-managed fleet, [configure the worker hosts manually](install-software.md).
+ *Simple plugin or script without administrator privileges?* Use a [queue environment](configure-jobs.md).
+ *Application or plugin with dependencies and version constraints?* Create a [custom conda package](configure-jobs-s3-channel.md).