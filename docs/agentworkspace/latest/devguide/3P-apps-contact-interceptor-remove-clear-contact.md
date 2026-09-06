

# Unregister a clear contact interceptor in Connect Customer agent workspace
<a name="3P-apps-contact-interceptor-remove-clear-contact"></a>

Unregisters an interceptor that you registered with `addClearContactInterceptor`. Pass the same interceptor reference and the same `contactId` that you used at registration.

**Signature**

```
removeClearContactInterceptor(
  interceptor: Interceptor<ContactInterceptorContext>,
  contactId?: string
): Promise<void>
```

**Usage**

```
await service.removeClearContactInterceptor(myInterceptor);
```

**Input**

The following table describes the input parameters.


| **Parameter** | **Type** | **Description** | 
| --- | --- | --- | 
| interceptor Required | Interceptor<ContactInterceptorContext> | The same function reference that you passed to addClearContactInterceptor. | 
| contactId Optional | string | The contact ID that the interceptor was scoped to. Pass the same value that you used at registration. If you omit this value, the framework removes the interceptor that applies to all contacts. | 

**Output**

`Promise<void>`