

# Updating Running Applications
<a name="updating-running-applications"></a>

You can update key application configurations such as maximum capacity, and custom image settings — without stopping and restarting the application.

## Updating Maximum Capacity configuration
<a name="updating-max-capacity"></a>

You can use the existing `UpdateApplication` API to increase or decrease the maximum capacity (vCPU, memory, disk) for a `STARTED` application to modify the scaling boundary for an application. When reducing the Maximum Capacity Configuration, running workloads are not affected. The new settings only apply to workers on new workloads or new workers replenishing a pre-initialized capacity pool.

## Updating custom image configurations
<a name="updating-custom-image"></a>

You can update the custom image used by an EMR Serverless application without stopping it - either by retagging an image in Amazon ECR or by updating the `imageConfiguration` configuration in an application. New workloads submitted after the update automatically will use the new image, while existing workloads continue with the original image.

To identify which image version each job is running, the `GetJobRun` API response returns the `resolvedImageDigest` for that specific job.

### Image digest resolution behavior
<a name="image-digest-resolution"></a>


**Image digest resolution behavior by EMR release**  

| EMR Release | Default behavior | Details | 
| --- | --- | --- | 
| EMR 7.13 and earlier | applicationLevelDigestResolution = true | Custom images are resolved to a digest at application start; that digest is used for all jobs until the application restarts. To enable live image updates, set applicationLevelDigestResolution to false, then update the image. | 
| EMR 7.14 and later | applicationLevelDigestResolution = false | New custom images take effect for new workloads immediately. Older workloads continue with their original image. | 

### Considerations
<a name="updating-custom-image-considerations"></a>
+ Custom image updates on running applications are not supported on applications with pre-initialized capacity configured.
+ For long-running streaming jobs, you must restart the job for a new custom image to take effect. New job attempts will pick new images.