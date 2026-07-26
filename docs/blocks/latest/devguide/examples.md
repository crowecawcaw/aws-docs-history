# Examples and patterns

This topic shows common application patterns you can build with AWS Blocks. Each example demonstrates how Blocks compose together to solve real-world problems.

For more information about runnable sample applications, see [AWS Blocks example applications on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/examples "https://github.com/aws-devtools-labs/aws-blocks/tree/main/examples").

## CRUD API with authentication

A typical data-driven application with user authentication and scoped data access.

```
import { ApiNamespace, Scope, KVStore, AuthBasic } from '@aws-blocks/blocks';

const scope = new Scope('notes-app');
const auth = new AuthBasic(scope, 'auth');
const notes = new KVStore(scope, 'notes', {});

export const api = new ApiNamespace(scope, 'api', (context) => ({
  async create(title: string, body: string) {
    const user = await auth.requireAuth(context);
    const id = crypto.randomUUID();
    const note = { id, title, body, createdAt: Date.now() };
    await notes.put(`${user.username}:${id}`, note);
    return note;
  },

  async list() {
    const user = await auth.requireAuth(context);
    const results = [];
    for await (const entry of notes.scan()) {
      if (entry.key.startsWith(`${user.username}:`)) results.push(entry.value);
    }
    return results;
  },

  async delete(id: string) {
    const user = await auth.requireAuth(context);
    await notes.delete(`${user.username}:${id}`);
  },
}));

export { auth };
```

**Blocks used:**
`AuthBasic`, `KVStore`, `ApiNamespace`

## Real-time chat

A chat application with WebSocket pub/sub and message history.

```
import { ApiNamespace, Scope, KVStore, AuthBasic, Realtime } from '@aws-blocks/blocks';
import { z } from 'zod';

const scope = new Scope('chat-app');
const auth = new AuthBasic(scope, 'auth');
const messages = new KVStore(scope, 'messages', {});

const messageSchema = z.object({ id: z.string(), user: z.string(), text: z.string(), ts: z.number() });

const realtime = new Realtime(scope, 'realtime', {
  namespaces: { chat: Realtime.namespace(messageSchema) },
});

export const api = new ApiNamespace(scope, 'api', (context) => ({
  async sendMessage(text: string) {
    const user = await auth.requireAuth(context);
    const msg = { id: crypto.randomUUID(), user: user.username, text, ts: Date.now() };
    await messages.put(`msg:${msg.id}`, msg);
    await realtime.publish('chat', 'general', msg);
    return msg;
  },

  async getHistory() {
    const results = [];
    for await (const entry of messages.scan()) {
      if (entry.key.startsWith('msg:')) results.push(entry.value);
    }
    return results;
  },

  async subscribeChat() {
    await auth.requireAuth(context); // Ensure caller is authenticated
    return realtime.getChannel('chat', 'general');
  },
}));

export { auth };
```

### Frontend integration

The frontend subscribes to real-time updates:

```
import { api } from 'aws-blocks';

// Subscribe to messages via API method
const channel = await api.subscribeChat();
channel.subscribe((msg) => {
  console.log(`${msg.user}: ${msg.text}`);
});

// Send a message
await api.sendMessage('Hello, world!');

// Load history
const history = await api.getHistory();
```

**Blocks used:**
`AuthBasic`, `KVStore`, `Realtime`, `ApiNamespace`

## File uploads with metadata

An application that stores files with associated metadata.

```
import { ApiNamespace, Scope, KVStore, FileBucket, AuthBasic } from '@aws-blocks/blocks';

const scope = new Scope('files-app');
const auth = new AuthBasic(scope, 'auth');
const files = new FileBucket(scope, 'uploads');
const metadata = new KVStore(scope, 'file-metadata', {});

export const api = new ApiNamespace(scope, 'api', (context) => ({
  async upload(name: string, data: Buffer) {
    const user = await auth.requireAuth(context);
    const key = `${user.username}/${name}`;
    await files.put(key, data);
    await metadata.put(key, { name, size: data.length, uploadedAt: Date.now() });
    return { key };
  },

  async listFiles() {
    const user = await auth.requireAuth(context);
    const results = [];
    for await (const entry of metadata.scan()) {
      if (entry.key.startsWith(`${user.username}/`)) results.push(entry.value);
    }
    return results;
  },

  async download(key: string) {
    const user = await auth.requireAuth(context);
    if (!key.startsWith(`${user.username}/`)) throw new Error('Forbidden');
    return files.get(key);
  },
}));

export { auth };
```

**Blocks used:**
`AuthBasic`, `FileBucket`, `KVStore`, `ApiNamespace`

## SQL-backed application

An application using relational data with joins and transactions.

```
import { ApiNamespace, Scope, Database, AuthBasic, sql } from '@aws-blocks/blocks';

const scope = new Scope('store-app');
const auth = new AuthBasic(scope, 'auth');
const db = new Database(scope, 'db');

export const api = new ApiNamespace(scope, 'api', (context) => ({
  async createOrder(items: Array<{ productId: string; qty: number }>) {
    const user = await auth.requireAuth(context);

    return db.transaction(async (trx) => {
      const [order] = await trx.query(sql`
        INSERT INTO orders (user_id, status, created_at)
        VALUES (${user.username}, 'pending', NOW())
        RETURNING *
      `);

      for (const item of items) {
        await trx.execute(sql`
          INSERT INTO order_items (order_id, product_id, quantity)
          VALUES (${order.id}, ${item.productId}, ${item.qty})
        `);
      }

      return order;
    });
  },

  async getOrders() {
    const user = await auth.requireAuth(context);
    return db.query(sql`
      SELECT * FROM orders
      WHERE user_id = ${user.username}
      ORDER BY created_at DESC
    `);
  },
}));

export { auth };
```

**Blocks used:**
`AuthBasic`, `Database`, `ApiNamespace`

## Common patterns

| Pattern          | Approach                                                                                  |
| ---------------- | ----------------------------------------------------------------------------------------- |
| User-scoped data | Prefix keys with `${user.username}:` to isolate data per user                             |
| Optimistic UI    | Return the created/updated object from API methods so the frontend can update immediately |
| Background work  | Use the CDK layer to add SQS queues or EventBridge rules alongside Blocks                 |
| Multi-tenant     | Use Scope IDs or key prefixes to partition data by tenant                                 |
| Feature flags    | Store flags in a `KVStore` and read them in API methods before executing logic            |

## Related resources

For more information about runnable sample applications with frontend code, deployment instructions, and tests:

- [AWS Blocks example applications on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/examples "https://github.com/aws-devtools-labs/aws-blocks/tree/main/examples")
- [AWS Blocks project templates](https://github.com/aws-devtools-labs/aws-blocks/tree/main/templates "https://github.com/aws-devtools-labs/aws-blocks/tree/main/templates") used by `npm create @aws-blocks/blocks-app@latest`
