# Intercept the Quick Connect action in Connect Customer agent workspace

Registers an interceptor for the Quick Connect action, which runs when the user chooses the Quick Connect or transfer button. To block the built-in Quick Connect experience and present your own transfer UI, return `{ continue: false }` (or `false`).

**Signature**

```

addOpenQuickConnectInterceptor(
  interceptor: Interceptor<ContactInterceptorContext>,
  options?: RegisterInterceptorOptions
): Promise<void>

addOpenQuickConnectInterceptor(
  interceptor: Interceptor<ContactInterceptorContext>,
  contactId: string,
  options?: RegisterInterceptorOptions
): Promise<void>
```

**Usage**

```

// Block the Quick Connect menu from opening
await service.addOpenQuickConnectInterceptor(async (context) => {
  return { continue: false };
});

// Scoped to a specific contact
await service.addOpenQuickConnectInterceptor(myInterceptor, contactId);
```

**Input**

The following table describes the input parameters.

| **Parameter**          | **Type**                                 | **Description**                                                                                                                                                                                                                                                                                              |
| ---------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| interceptor _Required_ | `Interceptor<ContactInterceptorContext>` | An asynchronous callback that receives a `{ contactId?: string }` context and returns an `InterceptorResult`. See [Interceptor callback type in Connect Customer agent workspace](3P-apps-extensibility-interceptor-type.md "3P-apps-extensibility-interceptor-type.md").                                    |
| contactId _Optional_   | string                                   | The `contactId` of the contact to scope the interceptor to. If you omit this value, the interceptor applies to all contacts.                                                                                                                                                                                 |
| options _Optional_     | `RegisterInterceptorOptions`             | The registration options. If you omit this value, the service uses the default timeout of 5000 milliseconds and the default maximum consecutive block limit of 5. See [RegisterInterceptorOptions in Connect Customer agent workspace](3P-apps-extensibility-options.md "3P-apps-extensibility-options.md"). |

**Output**

`Promise<void>`
