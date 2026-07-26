# ContactInterceptorContext in Connect Customer agent workspace

Defines the invocation context that the contact interceptor methods receive.

**Signature**

```

type ContactInterceptorContext = {
  contactId?: string;
}
```

**Properties**

The following table describes the properties.

| **Property**         | **Type** | **Description**                                                                                                                      |
| -------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| contactId _Optional_ | string   | The identifier of the contact that triggered the action. The service omits this value when no specific contact initiated the action. |
