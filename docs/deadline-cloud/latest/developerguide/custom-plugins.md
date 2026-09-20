

# Use custom plugins with Deadline Cloud
<a name="custom-plugins"></a>

Choose among plugin sync, conda packages, queue environments, and worker host configuration based on the plugin's dependencies, required access, and fleet type. The following table compares these delivery methods.


| Plugin requirement | Delivery method | Fleet support | When to choose it | 
| --- | --- | --- | --- | 
| Simple file-based plugins | [Deliver custom plugins with plugin sync](plugin-sync.md) (simplest option) | Service-managed fleets; customer-managed fleets that use a supporting application conda package | Choose this method when the plugin can run after its files are copied to the application's plugin search path. | 
| Dependencies, installation steps, or per-job version selection | [Package a plugin](conda-package.md#conda-package-plugins) | Service-managed and customer-managed fleets with a conda queue environment | Choose this method when conda must install dependencies, register the plugin, or resolve compatible versions. | 
| Setup commands that do not require administrator access | [Configure jobs using queue environments](configure-jobs.md) | Service-managed and customer-managed fleets | Choose this method for scripts or environment variables that run at the start of each session. | 
| Drivers, system libraries, or administrator-level installation on a service-managed fleet | [Run host configuration scripts with administrator privileges](smf-admin.md) | Service-managed fleets | Choose this method to install system software when a worker starts. | 
| Drivers, system libraries, or administrator-level installation on a customer-managed fleet | [Install and configure software required for jobs](install-software.md) | Customer-managed fleets | Install the software in the worker image or on each worker host before the worker joins the fleet. | 

Plugin delivery does not provide a plugin license. If the plugin requires a license, configure the worker network and license client so that jobs can reach your license server. For more information, see [Using software licenses with Deadline Cloud](license.md).