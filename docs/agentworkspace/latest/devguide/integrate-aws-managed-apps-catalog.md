# Retrieve available applications

The `getAppCatalog` method retrieves applications available to the
authenticated user. AppManager filters the list based on the user's Security Profile
permissions. Use this method to verify if user has permission for the AWS-managed
application prior to launching.

```

import { AppConfig } from "@amazon-connect/workspace-types";

// Retrieve applications filtered by Security Profile permissions
const applications: AppConfig[] = await appManager.getAppCatalog();
```

**Application configuration properties:**

Each `AppConfig` object contains the following properties:

- `arn` - Amazon Resource Name (ARN) that uniquely identifies the
  application
- `name` - Display name for the application

###### Note

This is not required if you know the name of the AWS-managed application that you
want to launch and the user is guaranteed to have access.
