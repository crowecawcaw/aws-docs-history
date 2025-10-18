# Updating an AWS Cloud Map service instance

You can update service instances in two ways, depending on which values you want to
 update:


* **Update any values**: If you want to update any of the values
 that you specified for a service instance when you registered it, including custom attributes,
 you need to reregister the service instance and respecify all values. Follow the steps in [Registering a resource as an AWS Cloud Map service
 instance](registering-instances.md "registering-instances.md"), specifying the
 instance ID of the existing service instance for **Service instance
 ID**.


Alternatively, you can use the [`RegisterInstance`](https://docs.aws.amazon.com/cloud-map/latest/api/API_RegisterInstance.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_RegisterInstance.html") API.
 You can specify the ID of the existing instance and service using the `InstanceId`
 and `ServiceId` parameters and respecify other values.
* **Update only custom attributes**: If you want to update only
 the custom attributes for a service instance, you don't need to reregister the instance. You can
 update only those values. See [Updating the custom attributes for a
 service instance](#updating-instance-attributes-procedure "#updating-instance-attributes-procedure").

## Updating the custom attributes for a
 service instance


###### To update only custom attributes for a service instance

1. Sign in to the AWS Management Console and open the AWS Cloud Map console at [https://console.aws.amazon.com/cloudmap/](https://console.aws.amazon.com/cloudmap/ "https://console.aws.amazon.com/cloudmap/").
2. In the navigation pane, choose **Namespaces**.
3. On the **Namespaces** page, choose the namespace that contains the
 service that you originally used to register the service instance.
4. On the **Namespace: `namespace-name`** page,
 choose the service that you used to register the service instance.
5. On the **Service: `service-name`** page, choose
 the name of the service instance that you want to update.
6. In the **Custom attributes** section, choose
 **Edit**.
7. On the **Edit service instance:
 `instance-name`** page, add, remove, or update custom
 attributes. You can update both keys and values for existing attributes.
8. Choose **Update service instance**.
