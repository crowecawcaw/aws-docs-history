

# Intercept the clear contact action in Connect Customer agent workspace
<a name="3P-apps-contact-interceptor-add-clear-contact"></a>

Registers an interceptor for the clear contact action, which runs when the user chooses to clear or end a contact. To block clearing the contact until a disposition code is submitted, return `{ continue: false }` (or `false`).

**Signature**

```
addClearContactInterceptor(
  interceptor: Interceptor<ContactInterceptorContext>,
  options?: RegisterInterceptorOptions
): Promise<void>

addClearContactInterceptor(
  interceptor: Interceptor<ContactInterceptorContext>,
  contactId: string,
  options?: RegisterInterceptorOptions
): Promise<void>
```

**Usage**

```
// Require a disposition code before clearing the contact
await service.addClearContactInterceptor(async (context) => {
  const done = await collectDisposition(context.contactId);
  return { continue: done };
});

// Scoped to a specific contact
await service.addClearContactInterceptor(myInterceptor, contactId);
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