# Theme in Amazon Connect

Agent Workspace

The theme package defines and applies the Amazon Connect theme when developing with
Cloudscape for Amazon Connect Agent Workspace.

**Install from NPM**

Install the theme package from NPM by installing **@amazon-connect/theme**.

```

% npm install -P @amazon-connect/theme

```

**Usage**

The theme package must be imported once at the entry point of the
application.

```

// src/index.ts

import { applyConnectTheme } from "@amazon-connect/theme";

applyConnectTheme();

```

From then on cloudscape components and design tokens can be used directly from
Cloudscape.

```

// src/app.ts

import * as React from "react";
import Button from "@cloudscape-design/components/button";

export default () => {
  return <Button variant="primary">Button</Button>;
}

```
