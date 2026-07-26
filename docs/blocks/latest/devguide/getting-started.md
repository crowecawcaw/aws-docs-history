# Getting started with AWS Blocks

In this tutorial, you set up your development environment, create a todo application with user authentication, data persistence, and a type-safe API. The application runs locally and can optionally deploy to AWS.

## Prerequisites

To develop with AWS Blocks, you need the following on your local machine:

- **Node.js** version 22 or later. Download from https://nodejs.org/.
- **npm** version 10 or later (included with Node.js).
- A code editor with TypeScript support, such as Visual Studio Code or Kiro.

To verify your Node.js and npm versions:

```
node --version
npm --version
```

For the optional deployment step, you also need:

- AWS CLI configured with credentials
- AWS CDK bootstrapped in your account

For deployment details, see [Deploy your application to AWS](deploy-to-aws.md "deploy-to-aws.md").

## Create your AWS Blocks project

Create a new AWS Blocks application:

```
npm create @aws-blocks/blocks-app@latest my-todo-app
cd my-todo-app
npm install
```

This creates a project with the following structure:

```
my-todo-app/
├── aws-blocks/
│   └── index.ts
├── src/
│   └── index.ts
├── index.html
└── package.json
```

## Run the application locally

Start the development server:

```
npm run dev
```

In your web browser, navigate to `http://localhost:3000`. You see a todo application with authentication, CRUD operations, and sorting.

All Blocks are running with local implementations:

- `DistributedTable` uses in-memory storage for structured data
- `AuthBasic` uses local JWT tokens for authentication
- `ApiNamespace` routes calls through a local HTTP server

No AWS account is needed. Changes to your code are reflected immediately through hot reload.

## Explore the backend code

The `aws-blocks/index.ts` file defines your backend and API in a single place:

```
import { ApiNamespace, Scope, DistributedTable, AuthBasic } from '@aws-blocks/blocks';
import { z } from 'zod';

const scope = new Scope('todo-app');

const auth = new AuthBasic(scope, 'auth');
export const authApi = auth.createApi();

const todoSchema = z.object({
  userId: z.string(),
  todoId: z.string(),
  title: z.string(),
  completed: z.boolean(),
});

const todos = new DistributedTable(scope, 'todos', {
  schema: todoSchema,
  key: { partitionKey: 'userId', sortKey: 'todoId' },
});
```

This code creates two Blocks:

- `new AuthBasic(scope, 'auth')` creates an authentication system. Locally, this uses JWT tokens. On AWS, this provisions a DynamoDB table for user records. The `auth.createApi()` call exports the auth API for the frontend to use.
- `new DistributedTable(scope, 'todos', {…​})` creates structured data storage with a Zod schema for validation. Locally, this is in-memory. On AWS, this provisions a DynamoDB table with indexes.

The API methods use these Blocks:

```
export const api = new ApiNamespace(scope, 'api', (context) => ({
  async createTodo(title: string) {
    const user = await auth.requireAuth(context);
    const todoId = crypto.randomUUID();
    await todos.put({ userId: user.username, todoId, title, completed: false });
    return { todoId, title, completed: false };
  },

  async listTodos() {
    const user = await auth.requireAuth(context);
    return await Array.fromAsync(
      todos.query({ where: { userId: { equals: user.username } } })
    );
  },

  async toggleTodo(todoId: string) {
    const user = await auth.requireAuth(context);
    const todo = await todos.get({ userId: user.username, todoId });
    if (!todo) throw new Error('Todo not found');
    await todos.put({ ...todo, completed: !todo.completed });
    return { ...todo, completed: !todo.completed };
  },
}));

export { auth };
```

## Explore the frontend code

The frontend in `src/index.ts` imports the backend API directly:

```
import { api, authApi } from 'aws-blocks';
```

There is no client generation step, no API URL configuration, and no SDK initialization. TypeScript provides full type safety. If you change a method signature in the backend, the frontend shows a compile error immediately.

## Make a change

Add a new API method to `aws-blocks/index.ts` inside the `ApiNamespace` definition:

```
  async deleteTodo(todoId: string) {
    const user = await auth.requireAuth(context);
    await todos.delete({ userId: user.username, todoId });
  },
```

The development server hot-reloads. You can immediately call `api.deleteTodo(todoId)` from the frontend with full type safety.

## Available Blocks

The following table lists the Blocks used in this tutorial and other commonly used blocks:

| Block              | Purpose                                            |
| ------------------ | -------------------------------------------------- |
| `DistributedTable` | Structured data with indexes and queries           |
| `AuthBasic`        | Username/password authentication with JWT sessions |
| `ApiNamespace`     | Type-safe RPC from browser to backend              |
| `Database`         | Full PostgreSQL with Kysely query builder          |
| `FileBucket`       | File uploads and downloads                         |
| `Realtime`         | WebSocket pub/sub channels                         |
| `AsyncJob`         | Background job processing                          |
| `Agent`            | AI agent with tool calling                         |

For the complete list of all available Blocks, see [Blocks reference](building-blocks-reference.md "building-blocks-reference.md").

## Optional: Deploy your application to AWS

When you’re ready to deploy to a real AWS environment, see [Deploy your application to AWS](deploy-to-aws.md "deploy-to-aws.md") for the full setup and deployment steps.

## Clean up

To stop the local development server, press `Ctrl+C` in your terminal.

If you deployed to AWS and want to remove all resources:

```
# Remove production deployment
npm run destroy

# Remove sandbox environment
npm run sandbox:destroy
```

## Next steps

- [AWS Blocks concepts](concepts.md "concepts.md"): Learn about Blocks, scopes, the IFC layer, and how code maps to resources.
- [Blocks reference](building-blocks-reference.md "building-blocks-reference.md"): Explore all available Blocks and their APIs.
- [Examples and patterns](examples.md "examples.md"): See common application patterns and sample code.
