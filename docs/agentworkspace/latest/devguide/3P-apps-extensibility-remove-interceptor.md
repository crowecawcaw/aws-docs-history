

# Unregister an interceptor in Connect Customer agent workspace
<a name="3P-apps-extensibility-remove-interceptor"></a>

Removes a previously registered interceptor. You must pass the same function reference and the same optional parameter that you used at registration.

 **Signature** 

```
removeInterceptor<T>(
  interceptorKey: InterceptorKey,
  interceptor: Interceptor<T>,
  parameter?: string
): Promise<void>
```

 **Usage** 

```
await service.removeInterceptor('clearContact', myInterceptor);

// If registered with a parameter, pass the same parameter
await service.removeInterceptor('openQuickConnect', myInterceptor, contactId);
```

 **Input** 

The following table describes the input parameters.


| **Parameter** | **Type** | **Description** | 
| --- | --- | --- | 
| interceptorKey Required | InterceptorKey (string) | The action key that you registered the interceptor for. | 
| interceptor Required | Interceptor<T> | The same function reference that you passed to addInterceptor. | 
| parameter Optional | string | The same scoping parameter that you passed to addInterceptor. For the currently supported interceptor keys, pass the same contactId you used when you registered the interceptor. If you omit this value, the interceptor applies to all contacts. | 

 **Output** 

`Promise<void>`