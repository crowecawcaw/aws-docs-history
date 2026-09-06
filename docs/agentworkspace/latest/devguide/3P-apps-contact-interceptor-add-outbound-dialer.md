

# Intercept the outbound dialer action in Connect Customer agent workspace
<a name="3P-apps-contact-interceptor-add-outbound-dialer"></a>

Registers an interceptor for the outbound dialer action, which runs when the user chooses the number pad or outbound dialer. To block the built-in outbound dialer and present your own dialer UI, return `{ continue: false }` (or `false`).

**Signature**

```
addOpenOutboundDialerInterceptor(
  interceptor: Interceptor<ContactInterceptorContext>,
  options?: RegisterInterceptorOptions
): Promise<void>

addOpenOutboundDialerInterceptor(
  interceptor: Interceptor<ContactInterceptorContext>,
  contactId: string,
  options?: RegisterInterceptorOptions
): Promise<void>
```

**Usage**

```
// Block the outbound dialer from opening
await service.addOpenOutboundDialerInterceptor(async (context) => {
  return { continue: false };
});

// Scoped to a specific contact
await service.addOpenOutboundDialerInterceptor(myInterceptor, contactId);
```

**Input**

The following table describes the input parameters.


| **Parameter** | **Type** | **Description** | 
| --- | --- | --- | 
| interceptor Required | Interceptor<ContactInterceptorContext> | An asynchronous callback that receives a { contactId?: string } context and returns an InterceptorResult. See [Interceptor callback type in Connect Customer agent workspace](3P-apps-extensibility-interceptor-type.md). | 
| contactId Optional | string | The contactId of the contact to scope the interceptor to. If you omit this value, the interceptor applies to all contacts. | 
| options Optional | RegisterInterceptorOptions | The registration options. If you omit this value, the service uses the default timeout of 5000 milliseconds and the default maximum consecutive block limit of 5. See [RegisterInterceptorOptions in Connect Customer agent workspace](3P-apps-extensibility-options.md). | 

**Output**

`Promise<void>`