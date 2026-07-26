# Connect Customer agent workspace Extensibility API

With the Amazon Connect SDK, your app in the Connect Customer agent workspace can
register and manage interceptors for UI actions by using
`ExtensibilityService`. `ExtensibilityService` is the generic,
low-level interceptor API, and it accepts any interceptor key. Domain-specific
interceptor services define typed methods and callback contexts for a specific set of
actions. When a domain-specific service covers your use case, prefer it over
`ExtensibilityService`.

###### Note

To intercept contact-related UI actions, use the contact-specific methods in
[Connect Customer agent workspace Contact UI API](api-reference-3P-apps-contact-ui-client.md "api-reference-3P-apps-contact-ui-client.md"). Use
`ExtensibilityService` directly only when no domain-specific service
covers your interceptor key.

You can instantiate the extensibility service as follows:

```

import { ExtensibilityService } from '@amazon-connect/extensibility';

const service = new ExtensibilityService(provider);
```

###### Note

The `provider` is your `AmazonConnectProvider` instance
— the same provider you use to initialize other
`@amazon-connect/*` packages.

Interceptors are asynchronous callbacks. They run before a default UI action runs.
To allow the default action, return `{ continue: true }` (or
`true`). For example, you can require a disposition code in your app before a
contact is cleared. To block the default action, return `{ continue: false }`
(or `false`). When you block the default action, you can provide a custom experience. For example, you
can present your own Quick Connect experience instead of the built-in one.

The framework accepts any string as an interceptor key, but only keys that the UI
actively invokes have an effect. The following table lists the currently supported
keys.

| **Key**              | **Triggers when**                                     | **Context**              |
| -------------------- | ----------------------------------------------------- | ------------------------ |
| `openQuickConnect`   | The user chooses the Quick Connect or transfer button | `{ contactId?: string }` |
| `openOutboundDialer` | The user chooses the number pad or outbound dialer    | `{ contactId?: string }` |
| `clearContact`       | The user chooses to clear or end a contact            | `{ contactId?: string }` |

###### Contents

- [addInterceptor()](3P-apps-extensibility-add-interceptor.md "3P-apps-extensibility-add-interceptor.md")
- [removeInterceptor()](3P-apps-extensibility-remove-interceptor.md "3P-apps-extensibility-remove-interceptor.md")
- [Interceptor callback](3P-apps-extensibility-interceptor-type.md "3P-apps-extensibility-interceptor-type.md")
- [Options](3P-apps-extensibility-options.md "3P-apps-extensibility-options.md")
- [Interceptor behavior](3P-apps-extensibility-behavior.md "3P-apps-extensibility-behavior.md")
