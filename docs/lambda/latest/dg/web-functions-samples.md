

# Web Function sample applications
<a name="web-functions-samples"></a>

Every sample uses `index.js` as the entry file and listens on the host and port from `AWS_LAMBDA_HTTP_ENDPOINT`. Package the application with its production dependencies and deploy it from a versioned Amazon S3 object.

The following table lists each sample and what you can learn from it.


| Sample | Use it to learn | 
| --- | --- | 
| [Minimal Express application](#web-functions-samples-express) | Start an HTTP server with Express. | 
| [Hono API and static files](#web-functions-samples-hono) | Serve API routes and static files with Hono. | 
| [Server-sent events](#web-functions-samples-streaming) | Stream server-sent events and stop work when the client disconnects. | 
| [Multi-Region verification route](#web-functions-samples-region) | Return the serving Region when validating multi-Region routing. | 

## Minimal Express application
<a name="web-functions-samples-express"></a>

This framework-based sample is an alternative to the zero-dependency starter created by `--hello-world`. For the starter deployment, see [Deploy and test your Web Function](web-functions-create.md#web-functions-create-cli-deploy).

Install Express:

```
npm init -y
npm install express
```

Create `index.js`:

```
const express = require('express');
const app = express();
const [host, port] = (process.env.AWS_LAMBDA_HTTP_ENDPOINT || 'localhost:3000').split(':');

app.get('/', (request, response) => {
  response.send('Hello from Lambda Web Functions!');
});

app.listen(port, host);
```

For packaging guidance, see [Package and deploy a sample](#web-functions-samples-deploy).

## Hono API and static files
<a name="web-functions-samples-hono"></a>

Install the dependencies:

```
npm init -y
npm pkg set type=module
npm install hono @hono/node-server
```

Create `index.js`:

```
import { serve } from '@hono/node-server';
import { serveStatic } from '@hono/node-server/serve-static';
import { Hono } from 'hono';
import { secureHeaders } from 'hono/secure-headers';

const app = new Hono();
app.use(secureHeaders());
app.use('/static/*', serveStatic({ root: './' }));
app.get('/api/health', (context) => context.json({ status: 'ok' }));
app.notFound((context) => context.json({ error: 'not found' }, 404));

const [host, port] = (process.env.AWS_LAMBDA_HTTP_ENDPOINT || 'localhost:3000').split(':');

serve({ fetch: app.fetch, port: Number(port), hostname: host });
```

Put static files under a `static` directory and include the directory in the deployment package.

## Server-sent events
<a name="web-functions-samples-streaming"></a>

Add the following route to an Express application:

```
app.get('/events', (request, response) => {
  response.setHeader('Content-Type', 'text/event-stream');
  response.setHeader('Cache-Control', 'no-cache');
  response.flushHeaders();

  const interval = setInterval(() => {
    response.write(`data: ${JSON.stringify({ time: Date.now() })}\n\n`);
  }, 1000);

  response.on('close', () => {
    clearInterval(interval);
  });
});
```

The request remains active until the application ends the response or the client disconnects. Set the revision timeout for the maximum stream duration. WebSocket upgrades are not supported.

## Multi-Region verification route
<a name="web-functions-samples-region"></a>

Add a route that returns the Region in which the request executed:

```
app.get('/region', (request, response) => {
  response.json({
    region: process.env.AWS_REGION,
    requestId: request.get('lambda-web-request-id')
  });
});
```

Call the route from the client locations that matter to your application. For a `MultiRegion` endpoint, the selected Region comes from latency-based routing and can change. Do not use the execution environment as a session store.

## Package and deploy a sample
<a name="web-functions-samples-deploy"></a>

```
npm ci --omit=dev
zip -r function.zip index.js package.json package-lock.json node_modules
aws s3 cp function.zip s3://{{amzn-s3-demo-bucket}}/samples/function.zip
```

Include other files that the selected sample uses, such as the `static` directory in the Hono sample. To create a revision that references the uploaded object, see [Deploying Web Function code from Amazon S3](web-functions-code-s3.md) and [Managing Web Function revisions](web-functions-revisions.md). For the higher-level `deploy` workflow, see [Creating a Web Function (AWS CLI)](web-functions-create.md#web-functions-create-cli). After the revision is `Active` and the endpoint serves it, send a request to the endpoint domain to confirm the sample responds. For test coverage beyond this smoke test, see [Testing Lambda Web Functions](web-functions-testing.md).