

# Register an interceptor in Connect Customer agent workspace
<a name="3P-apps-extensibility-add-interceptor"></a>

Registers an asynchronous interceptor callback for the specified action key. When the UI triggers the action, your interceptor runs before the default behavior.

 **Signature** 

```
addInterceptor<T>(
  interceptorKey: InterceptorKey,
  interceptor: Interceptor<T>,
  options?: RegisterInterceptorOptions
): Promise<void>

addInterceptor<T>(
  interceptorKey: InterceptorKey,
  interceptor: Interceptor<T>,
  parameter: string,
  options?: RegisterInterceptorOptions
): Promise<void>
```

 **Usage** 

```
// Without parameter
await service.addInterceptor('clearContact', myInterceptor, { timeout: 5000 });

// With parameter (scoped to a specific contact)
await service.addInterceptor('openQuickConnect', myInterceptor, contactId, { timeout: 5000 });
```

 **Input** 

The following table describes the input parameters.


| **Parameter** | **Type** | **Description** | 
| --- | --- | --- | 
| interceptorKey Required | InterceptorKey (string) | The action key to intercept. Valid values: + `openQuickConnect` – The Quick Connect or transfer action.<br />+ `openOutboundDialer` – The number pad or outbound dialer action.<br />+ `clearContact` – The clear or end contact action. | 
| interceptor Required | Interceptor<T> | An asynchronous callback that receives a context object and returns an InterceptorResult. See [Interceptor callback type in Connect Customer agent workspace](3P-apps-extensibility-interceptor-type.md). | 
| parameter Optional | string | A scoping parameter. For the currently supported interceptor keys, pass the contactId of the contact that the interceptor applies to. If you omit this value, the interceptor applies to all contacts. | 
| options Optional | RegisterInterceptorOptions | The configuration options for this interceptor. If you omit this value, the service uses the default timeout of 5000 milliseconds and the default maximum consecutive block limit of 5. See [RegisterInterceptorOptions in Connect Customer agent workspace](3P-apps-extensibility-options.md). | 

 **Output** 

`Promise<void>`