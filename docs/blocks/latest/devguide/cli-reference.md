# CLI reference

AWS Blocks uses standard npm scripts for all development and deployment workflows. After scaffolding a project, all commands run from your project root.

For more information about CLI commands and options, see [AWS Blocks CLI documentation on GitHub](https://github.com/aws-devtools-labs/aws-blocks "https://github.com/aws-devtools-labs/aws-blocks").

## Create a project

```
npm create @aws-blocks/blocks-app@latest <project-name> [-- --template <template>]
```

Scaffolds a new AWS Blocks project.

| Option               | Description                                                                   |
| -------------------- | ----------------------------------------------------------------------------- |
| `--template default` | Todo app with auth, DistributedTable, Realtime, and CRUD operations (default) |
| `--template demo`    | Full-stack app with auth, KVStore, DistributedTable, and CRUD operations      |

## Local development

```
npm run dev
```

Starts the full-stack development server with hot reload. Blocks use local in-memory and filesystem storage. No AWS account required.

- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:3001`

## Sandbox deployment

```
npm run sandbox
```

Deploys a fast, ephemeral backend to AWS using Lambda hot-swapping. Uses real AWS services for testing. Each developer gets an isolated sandbox.

```
npm run sandbox:destroy
```

Tears down all sandbox resources.

## Production deployment

```
npm run deploy
```

Deploys the full application to AWS via CDK (CloudFormation). Use for staging and production environments.

```
npm run destroy
```

Tears down all deployed resources.

## Related resources

For more information about advanced CLI options, environment variables, and CI/CD configuration, see [AWS Blocks CLI reference on GitHub](https://github.com/aws-devtools-labs/aws-blocks "https://github.com/aws-devtools-labs/aws-blocks").
