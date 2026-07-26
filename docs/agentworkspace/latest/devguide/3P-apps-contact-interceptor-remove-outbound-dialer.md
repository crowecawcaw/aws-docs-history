# Unregister an outbound dialer interceptor in Connect Customer agent workspace

Unregisters an interceptor that you registered with `addOpenOutboundDialerInterceptor`. Pass the same interceptor reference and the same `contactId` that you used at registration.

**Signature**

```

removeOpenOutboundDialerInterceptor(
  interceptor: Interceptor<ContactInterceptorContext>,
  contactId?: string
): Promise<void>
```

**Usage**

```

await service.removeOpenOutboundDialerInterceptor(myInterceptor);
```

**Input**

The following table describes the input parameters.

| **Parameter**          | **Type**                                 | **Description**                                                                                                                                                                                   |
| ---------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| interceptor _Required_ | `Interceptor<ContactInterceptorContext>` | The same function reference that you passed to `addOpenOutboundDialerInterceptor`.                                                                                                                |
| contactId _Optional_   | string                                   | The contact ID that the interceptor was scoped to. Pass the same value that you used at registration. If you omit this value, the framework removes the interceptor that applies to all contacts. |

**Output**

`Promise<void>`
