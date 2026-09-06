

# Amazon Application Recovery Controller (ARC) readiness check availability change
<a name="arc-readiness-availability-change"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal.

After careful consideration, we decided to close the readiness check feature in Amazon Application Recovery Controller (ARC) to new customers. Existing customers can continue to use the service as normal.

ARC readiness check is a feature that enables you to monitor the readiness of your resources for disaster recovery. ARC continues to be available, but the readiness check feature is no longer open to new customers.

**Note**  
ARC and ARC Region switch continue to be fully supported. Only the readiness check feature is affected by this change. There are no changes to Region switch, routing controls, zonal shift, and zonal autoshift.

## Migration options
<a name="arc-readiness-availability-change.migration"></a>

For capabilities similar to readiness check, we recommend onboarding your multi-Region application to ARC Region switch.

ARC Region switch is a fully managed service that provides complete multi-Region recovery orchestration. It includes a capability called plan evaluation, which regularly monitors the state of your Region switch plan to ensure readiness for execution.

To get started with ARC Region switch, see [Region switch in ARC](region-switch.md).