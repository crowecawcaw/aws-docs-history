

# Apply a theme to your application in Connect Customer agent workspace
<a name="integrating-with-agent-workspace-theme"></a>

The theme package defines and applies the Connect Customer theme when developing with [Cloudscape](https://cloudscape.design) for the Connect Customer agent workspace.

 **Install from NPM** 

Install the theme package and Cloudscape global-styles from NPM by installing ** @amazon-connect/theme** and ** @cloudscape-design/global-styles**.

```
% npm install -P @amazon-connect/theme  
% npm install -P @cloudscape-design/global-styles
```

 **Usage** 

The theme package must be imported once at the entry point of the application. 

```
import { applyConnectTheme } from "@amazon-connect/theme"; 

await applyConnectTheme(provider);
```

**Note**  
You must first instantiate the [ AmazonConnectApp](getting-started-initialize-sdk.md) which initializes the default AmazonConnectProvider and returns ` { provider } `. 

From then on Cloudscape components and design tokens can be used directly from Cloudscape.

```
// src/app.ts

import * as React from "react";
import Button from "@cloudscape-design/components/button";

export default () => {
  return <Button variant="primary">Button</Button>;
}
```