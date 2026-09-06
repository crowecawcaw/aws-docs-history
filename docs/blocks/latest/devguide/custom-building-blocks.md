

# Creating custom Blocks
<a name="custom-building-blocks"></a>

When the built-in Blocks don’t cover your use case, you can create your own. A custom Block packages infrastructure, runtime logic, and a local implementation into a single reusable module, usable across projects or shared with your team.

## Use cases for custom Blocks
<a name="custom-bb-when"></a>

Create a custom Block when:
+ You’re repeating the same AWS resource \+ SDK boilerplate across multiple API methods
+ You want local development support for a resource that doesn’t have a built-in Block
+ You want to share a reusable capability across projects or teams

Don’t create a custom Block when:
+ You only need the resource in one place. Use the [The CDK layer](concepts.md#concepts-cdk-layer) directly instead
+ A built-in Block already does what you need

## Block structure
<a name="custom-bb-structure"></a>

A Block is an npm package with up to four exports, each targeting a different execution context:

```
my-building-block/
├── src/
│   ├── index.ts          
│   ├── index.mock.ts     
│   ├── index.cdk.ts      
│   ├── client-hook.ts    
│   └── types.ts          
├── package.json
├── tsconfig.json
└── README.md
```

 **Runtime**: AWS SDK integration, runs in Lambda.

 **Local**: In-memory/filesystem implementation, runs during `npm run dev`.

 **Infrastructure**: CDK constructs, runs during `cdk synth`.

 **Client hook**: Browser-side protocol extensions (optional).

 **Shared types**: Type definitions shared across all exports.

## Configure package.json exports
<a name="custom-bb-package-json"></a>

The `package.json` uses conditional exports to route imports to the correct file:

```
{
  "name": "@my-org/bb-notifications",
  "version": "1.0.0",
  "type": "module",
  "exports": {
    ".": {
      "types": "./dist/types.d.ts",
      "cdk": "./dist/index.cdk.js",
      "aws-runtime": "./dist/index.js",
      "default": "./dist/index.mock.js"
    }
  },
  "files": ["dist"]
}
```


| Export condition | File | When it’s used | 
| --- | --- | --- | 
|  `types`  |  `types.d.ts`  | IDE IntelliSense and TypeScript compilation | 
|  `cdk`  |  `index.cdk.js`  | CDK synthesis (infrastructure provisioning) | 
|  `aws-runtime`  |  `index.js`  | Lambda execution (production) | 
|  `default`  |  `index.mock.js`  | Local development (`npm run dev`) | 

## Define shared types
<a name="custom-bb-types"></a>

Start by defining the interface your Block exposes. Both the runtime and local implementations must conform to this interface.

```
// src/types.ts
import { Scope } from '@aws-blocks/core';

export interface NotificationOptions {
  /** The sender email address (must be verified in SES) */
  fromAddress: string;
}

export interface SendEmailInput {
  to: string;
  subject: string;
  body: string;
}

export declare class Notifications {
  constructor(scope: Scope, id: string, options: NotificationOptions);
  sendEmail(input: SendEmailInput): Promise<{ messageId: string }>;
}
```

## Implement the runtime
<a name="custom-bb-runtime"></a>

The runtime implementation uses the AWS SDK to interact with real services. It runs inside Lambda in production.

```
// src/index.ts
import { SESv2Client, SendEmailCommand } from '@aws-sdk/client-sesv2';
import { Scope } from '@aws-blocks/core';
import type { NotificationOptions, SendEmailInput } from './types.js';

export class Notifications {
  private client: SESv2Client;
  private fromAddress: string;

  constructor(scope: Scope, id: string, options: NotificationOptions) {
    this.client = new SESv2Client({});
    this.fromAddress = options.fromAddress;
  }

  async sendEmail(input: SendEmailInput): Promise<{ messageId: string }> {
    const result = await this.client.send(new SendEmailCommand({
      FromEmailAddress: this.fromAddress,
      Destination: { ToAddresses: [input.to] },
      Content: {
        Simple: {
          Subject: { Data: input.subject },
          Body: { Text: { Data: input.body } },
        },
      },
    }));
    return { messageId: result.MessageId ?? 'unknown' };
  }
}
```

## Implement the local version
<a name="custom-bb-mock"></a>

The local implementation provides the same API but runs without AWS. Use in-memory data structures, the filesystem, or embedded databases.

```
// src/index.mock.ts
import { Scope } from '@aws-blocks/core';
import { getMockDataDir } from '@aws-blocks/core/bb-utils';
import { writeFileSync, mkdirSync } from 'fs';
import { join } from 'path';
import type { NotificationOptions, SendEmailInput } from './types.js';

export class Notifications {
  private logDir: string;

  constructor(scope: Scope, id: string, options: NotificationOptions) {
    this.logDir = getMockDataDir(scope);
    mkdirSync(this.logDir, { recursive: true });
  }

  async sendEmail(input: SendEmailInput): Promise<{ messageId: string }> {
    const messageId = crypto.randomUUID();
    const logFile = join(this.logDir, `${messageId}.json`);
    writeFileSync(logFile, JSON.stringify({ ...input, messageId, sentAt: new Date().toISOString() }));
    console.log(`[mock] Email sent to ${input.to}: "${input.subject}"`);
    return { messageId };
  }
}
```

During local development, emails are logged to the console and saved as JSON files in `.bb-data/` instead of being sent through SES.

## Implement the infrastructure
<a name="custom-bb-infra"></a>

The infrastructure export defines CDK constructs that are synthesized during deployment. Grant the Lambda handler the permissions it needs.

```
// src/index.cdk.ts
import { Scope } from '@aws-blocks/core/cdk';
import type { NotificationOptions } from './types.js';
import * as iam from 'aws-cdk-lib/aws-iam';

export class Notifications {
  constructor(scope: Scope, id: string, options: NotificationOptions) {
    // Grant the Lambda handler permission to send emails via SES
    scope.handler.addToRolePolicy(new iam.PolicyStatement({
      actions: ['ses:SendEmail'],
      resources: ['*'],
      conditions: {
        StringEquals: { 'ses:FromAddress': options.fromAddress },
      },
    }));
  }

  // No-op methods. Infrastructure doesn't execute runtime logic
  async sendEmail() { return { messageId: '' }; }
}
```

## Client hook (optional)
<a name="custom-bb-client-hook"></a>

Most Blocks don’t need a client hook. Add one only if your Block requires a custom client-server protocol (such as WebSockets or streaming).

```
// src/client-hook.ts

// No client-side protocol needed for email notifications
export {};
```

If your Block does need a client hook (for example, a real-time messaging block), export a class with lifecycle methods:

```
// src/client-hook.ts (for a real-time Block)
export class RealtimeClientHook {
  private ws?: WebSocket;

  async onInit(config: { websocketUrl: string }) {
    this.ws = new WebSocket(config.websocketUrl);
  }

  subscribe(channel: string, handler: (msg: any) => void) {
    this.ws?.addEventListener('message', (event) => {
      const data = JSON.parse(event.data);
      if (data.channel === channel) handler(data.message);
    });
  }
}
```

## Use your Block
<a name="custom-bb-usage"></a>

After building your package, install it in your project and use it like any built-in Block:

```
// aws-blocks/index.ts
import { ApiNamespace, Scope } from '@aws-blocks/blocks';
import { Notifications } from '@my-org/bb-notifications';

const scope = new Scope('my-app');
const email = new Notifications(scope, 'email', {
  fromAddress: 'noreply@example.com',
});

export const api = new ApiNamespace(scope, 'api', (context) => ({
  async sendWelcomeEmail(userEmail: string) {
    return email.sendEmail({
      to: userEmail,
      subject: 'Welcome!',
      body: 'Thanks for signing up.',
    });
  },
}));
```

## Testing your Block
<a name="custom-bb-testing"></a>

Test both the mock and runtime implementations:
+  **Mock tests**: Run directly with a test runner (Vitest, Jest). Verify that the mock behaves correctly and returns expected shapes.
+  **Runtime tests**: Deploy to a sandbox and verify against real AWS services.
+  **Interface parity**: Ensure both implementations accept the same inputs and return the same output shapes.

```
// tests/notifications.test.ts
import { describe, it, expect } from 'vitest';
import { Notifications } from '../src/index.mock.js';

describe('Notifications (mock)', () => {
  it('returns a messageId', async () => {
    const scope = new MockScope('test');
    const notif = new Notifications(scope, 'test-email', {
      fromAddress: 'test@example.com',
    });

    const result = await notif.sendEmail({
      to: 'user@example.com',
      subject: 'Test',
      body: 'Hello',
    });

    expect(result.messageId).toBeDefined();
  });
});
```

## Publishing
<a name="custom-bb-publishing"></a>

To share your Block:
+  **Within a monorepo**: Reference it as a workspace dependency. No publishing needed.
+  **Within your organization**: Publish to a private npm registry (such as AWS CodeArtifact).
+  **Publicly**: Publish to the npm public registry.

Include a `README.md` with usage examples, API documentation, and information about the AWS resources provisioned. AI coding agents use this documentation to help developers integrate your Block.

## Best practices for custom Blocks
<a name="custom-bb-best-practices"></a>
+  **Keep the interface identical** between runtime and mock. Consumers shouldn’t need to know which implementation is active.
+  **Document mock limitations**: If the mock doesn’t replicate all production behavior (such as DynamoDB query limits), document the differences.
+  **Use `getMockDataDir(scope)` ** for persistent mock data. This follows the `.bb-data/{id}/` convention.
+  **Minimize client hooks**: Only use them for non-HTTP protocols. Most Blocks don’t need one.
+  **Export `{}` for unused layers**: Don’t omit files. An explicit empty export signals intent.
+  **Share types in a separate file**: This ensures type consistency across all implementations.