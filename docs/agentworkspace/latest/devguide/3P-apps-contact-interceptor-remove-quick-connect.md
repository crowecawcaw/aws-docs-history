

# Unregister a Quick Connect interceptor in Connect Customer agent workspace
<a name="3P-apps-contact-interceptor-remove-quick-connect"></a>

Unregisters an interceptor that you registered with `addOpenQuickConnectInterceptor`. Pass the same interceptor reference and the same `contactId` that you used at registration.

**Signature**

```
removeOpenQuickConnectInterceptor(
  interceptor: Interceptor<ContactInterceptorContext>,
  contactId?: string
): Promise<void>
```

**Usage**

```
await service.removeOpenQuickConnectInterceptor(myInterceptor);

// If scoped to a contact, pass the same contactId
await service.removeOpenQuickConnectInterceptor(myInterceptor, contactId);
```

**Input**

The following table describes the input parameters.


| **Parameter** | **Type** | **Description** | 
| --- | --- | --- | 
| interceptor Required | Interceptor<ContactInterceptorContext> | The same function reference that you passed to addOpenQuickConnectInterceptor. | 
| contactId Optional | string | The contact ID that the interceptor was scoped to. Pass the same value that you used at registration. If you omit this value, the framework removes the interceptor that applies to all contacts. | 

**Output**

`Promise<void>`