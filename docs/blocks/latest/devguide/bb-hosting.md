# Hosting

The Hosting construct provides frontend deployment with server-side rendering (SSR) support. Hosting auto-detects your frontend framework (Next.js, Nuxt, Astro, or SPA) and provisions the required AWS resources. Import from `@aws-blocks/blocks/cdk` and use in your CDK layer file (`aws-blocks/index.cdk.ts`).

Locally, the development server serves your frontend at `http://localhost:3000` with hot reload. On AWS, Hosting provisions an Amazon CloudFront distribution with an Amazon S3 origin, AWS Lambda compute for SSR, an optional AWS WAF, monitoring dashboards, and DNS records. Hosting also supports custom domains and skew protection for zero-downtime deployments.

Use Hosting in the CDK layer, not in the IFC layer. The `npm run deploy` command includes Hosting automatically. For sandbox deployments (`npm run sandbox`), the deploy skips hosting because sandboxes focus on backend hot-swapping.

## What Hosting provisions

On AWS, a single `Hosting` construct provisions a complete, production-ready frontend stack:

- **Amazon CloudFront** – a global content delivery network (CDN) distribution that serves your site from edge locations close to your users
- **Amazon S3** – an origin bucket that stores your static assets (HTML, CSS, JavaScript, images)
- **AWS Lambda** – server-side rendering (SSR) compute for framework routes that render on the server. Applies to SSR frameworks only. Hosting skips this resource for single-page applications (SPAs) and static sites.
- **Custom domains with TLS** – optional Amazon Route 53 records and an AWS Certificate Manager (ACM) certificate for your own domain over HTTPS
- **AWS WAF** – optional web application firewall rules, including rate limiting
- **Amazon CloudWatch monitoring** – alarms for Amazon CloudFront 5xx rates, AWS Lambda errors and throttles, and revalidation failures (enabled by default)
- **Skew protection** – cookie-based pinning that keeps a user’s session on a single build during rolling deployments (enabled by default)

When you provide the `api` prop, Hosting also adds Amazon CloudFront behaviors that proxy backend API requests through the same domain as your frontend. Your frontend calls the API with relative URLs (for example, `/aws-blocks/…​`). Because the frontend and API share a single origin, you avoid cross-origin resource sharing (CORS) concerns.

## Supported frameworks

Hosting detects your framework from your `package.json` dependencies and selects the matching adapter. SSR frameworks deploy with AWS Lambda compute. SPA frameworks deploy as static assets that Amazon CloudFront serves from an Amazon S3 origin.

| Framework                                | Rendering                      | Detected from                                                       |
| ---------------------------------------- | ------------------------------ | ------------------------------------------------------------------- |
| Next.js                                  | SSR                            | `next` in dependencies                                              |
| Nuxt                                     | SSR                            | `nuxt` or `nitropack` in dependencies                               |
| Astro                                    | Static or SSR                  | `astro` in dependencies                                             |
| Nitro-based (SolidStart, TanStack Start) | SSR                            | `@solidjs/start`, `@tanstack/start`, or `nitropack` in dependencies |
| React, Vue, Svelte, Angular (SPA)        | Static single-page application | None of the above (falls back to the SPA/static adapter)            |

Framework detection is automatic. To override it, set the `framework` prop explicitly:

```
new Hosting(stack, 'Web', {
  root: join(__dirname, '..'),
  framework: 'nextjs',
});
```

For the full list of supported framework versions and native platform clients, see [Supported platforms](supported-platforms.md "supported-platforms.md").

## Basic usage

Before you begin, make sure you have a CDK layer file (`aws-blocks/index.cdk.ts`) and a frontend app with a `package.json` in your project.

Add Hosting to your CDK layer file. At minimum, provide the `root` path to your frontend app and a `buildCommand`. Pass your backend stack as `api` to serve the frontend and API from the same domain.

```
// aws-blocks/index.cdk.ts
import * as cdk from 'aws-cdk-lib';
import { BlocksStack, Hosting } from '@aws-blocks/blocks/cdk';
import { join } from 'node:path';

const app = new cdk.App();
const blocksStack = await BlocksStack.create(app, 'my-stack', {
  backendHandlerPath: './index.handler.ts',
  backendCDKPath: './index.ts',
});

new Hosting(blocksStack, 'Web', {
  root: join(__dirname, '..'),
  buildCommand: 'npm run build',
  api: blocksStack,
});
```

Omit the `api` prop to deploy a static-only site with no backend. If you already built your app, omit `buildCommand` and Hosting deploys the existing output.

The `Hosting` construct exposes the resources it creates as public readonly members, so you can reference them elsewhere in your CDK layer:

| Member             | Description                                                                    |
| ------------------ | ------------------------------------------------------------------------------ |
| `bucket`           | The Amazon S3 bucket storing static assets.                                    |
| `distribution`     | The Amazon CloudFront distribution serving the site.                           |
| `url`              | The public HTTPS URL of the deployed site.                                     |
| `ssrFunction`      | The primary SSR AWS Lambda function, when the framework uses SSR.              |
| `buildCacheBucket` | The build-cache Amazon S3 bucket, when `buildCache.enabled` is `true`.         |
| `monitoringTopic`  | The Amazon SNS topic for Amazon CloudWatch alarms, when monitoring is enabled. |

## Custom domains

Configure a custom domain with the `domain` prop. Amazon CloudFront requires the ACM certificate to be in the `us-east-1` AWS Region. This requirement applies regardless of where you deploy the rest of your stack.

You can set up a domain in two ways.

**Amazon Route 53 (automatic)** – provide a `hostedZone` you control. Hosting requests a DNS-validated ACM certificate and creates the A and AAAA alias records automatically:

```
new Hosting(blocksStack, 'Web', {
  root: join(__dirname, '..'),
  buildCommand: 'npm run build',
  api: blocksStack,
  domain: {
    domainName: 'app.example.com',
    hostedZone: 'example.com',
  },
});
```

To serve both an apex domain and its `www` subdomain, pass an array of domain names and set `wwwRedirect`:

```
domain: {
  domainName: ['example.com', 'www.example.com'],
  hostedZone: 'example.com',
  wwwRedirect: 'toApex',
}
```

**Bring your own DNS (manual)** – if you manage DNS outside Amazon Route 53, omit `hostedZone` and supply a pre-validated `certificate` in `us-east-1`. Hosting does not create DNS records. Instead, it outputs the Amazon CloudFront distribution domain name. Point a CNAME (or an ALIAS/ANAME record for an apex domain) at that domain name:

```
domain: {
  domainName: ['app.example.com'],
  certificate: myPreValidatedCert, // ACM certificate in us-east-1
}
```

###### Note

If you provide neither a hosted zone nor a certificate, synthesis fails fast with a `MissingCertificateError` rather than waiting on an unvalidated certificate at deploy time. A certificate outside `us-east-1` fails with an `InvalidCertificateRegionError`.

## SSR compute

For SSR frameworks, tune the AWS Lambda function that renders your server-side routes with the `compute` prop. Hosting ignores this prop for SPA and static deployments.

```
new Hosting(blocksStack, 'Web', {
  root: join(__dirname, '..'),
  buildCommand: 'npm run build',
  framework: 'nextjs',
  api: blocksStack,
  compute: {
    memorySize: 1024,
    timeout: cdk.Duration.seconds(30),
  },
});
```

| Option                                  | Default    | Description                                                                                                                                   |
| --------------------------------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `memorySize`                            | 512        | AWS Lambda memory size, in MB.                                                                                                                |
| `timeout`                               | 30 seconds | AWS Lambda timeout. Accepts a `cdk.Duration` or a plain number of seconds.                                                                    |
| `reservedConcurrency`                   | None       | Reserved concurrent executions for the SSR AWS Lambda function.                                                                               |
| `imageOptimization.reservedConcurrency` | None       | Reserved concurrency for the image-optimization AWS Lambda function. Left unreserved by default so deployments succeed on fresh AWS accounts. |
| `logRetention`                          | Two weeks  | Amazon CloudWatch log retention for the SSR AWS Lambda function.                                                                              |

## Security

Hosting provides several controls for protecting your distribution.

**WAF** – enable AWS WAF with the `waf` prop to add managed protections and rate limiting. You can also associate an existing WebACL by ARN (the WebACL must be in `us-east-1`):

```
waf: {
  enabled: true,
  rateLimit: 1000, // requests per 5-minute window per IP
}
```

**Content Security Policy** – set `contentSecurityPolicy` to override the restrictive default `Content-Security-Policy` header:

```
contentSecurityPolicy: "default-src 'self'; img-src 'self' data:;",
```

**Geo-restriction** – use `geoRestriction` to restrict access by country. Configure the prop with a `countries` array of ISO country codes and a `type` that either allows only those countries or blocks them. For the exact type values, see the `geoRestriction` property in the [Hosting package source code on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/hosting "https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/hosting").

###### Warning

Hosting writes values from `backendConfig` to `/.blocks-sandbox/config.json` and injects them into the `BLOCKS_CONFIG`
AWS Lambda environment variable. Both locations are publicly accessible. Do not include secrets, API keys, or other sensitive configuration. For sensitive values, use AWS Systems Manager Parameter Store or AWS Secrets Manager and read them at runtime.

## Operations

Hosting includes operational features to keep deployments observable and reliable.

**Monitoring** – Amazon CloudWatch alarms are enabled by default and cover Amazon CloudFront 5xx rates, SSR AWS Lambda errors and throttles, and revalidation failures. If you omit `snsTopicArn`, Hosting creates an Amazon SNS topic and exposes it as the construct’s `monitoringTopic` member. You can subscribe to this topic for notifications. Set `monitoring: { enabled: false }` to opt out.

**Skew protection** – enabled by default. During a rolling deployment, viewers who started a session continue to receive assets from the same build. This prevents asset mismatches. Set `skewProtection: { enabled: false }` to disable it.

**Access logging** – enable Amazon CloudFront access logs to a dedicated Amazon S3 bucket with the `logging` prop:

```
logging: { enabled: true, retentionDays: 90 },
```

**Build cache** – enable `buildCache` to preserve framework build caches (such as `.next/cache`) between deployments in an Amazon S3 bucket, reducing cold-build times in CI:

```
buildCache: { enabled: true },
```

## Configuration reference

The following table summarizes the top-level `Hosting` properties. All properties except `root` are optional.

| Property         | Default                                                      | Description                                                                              |
| ---------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| `root`           | —                                                            | Path to the frontend app root directory. Required.                                       |
| `buildCommand`   | None                                                         | Shell command to build the frontend during CDK synthesis. Omit if you pre-built the app. |
| `framework`      | Auto-detected                                                | Framework type. Overrides detection from `package.json`.                                 |
| `buildOutputDir` | Auto-detected                                                | Path to the build output directory.                                                      |
| `basePath`       | None                                                         | URL prefix for the entire site (for example, `/app`).                                    |
| `api`            | None                                                         | Backend stack to proxy through the same domain (single-origin, no CORS).                 |
| `backendConfig`  | None                                                         | Extra config merged into `config.json`. Publicly accessible, so do not include secrets.  |
| `compute`        | See [SSR compute](#bb-hosting-compute "#bb-hosting-compute") | AWS Lambda compute configuration for SSR frameworks.                                     |
| `domain`         | None                                                         | Custom domain configuration.                                                             |
| `waf`            | Disabled                                                     | AWS WAF configuration.                                                                   |
| `priceClass`     | `PRICE_CLASS_100`                                            | Amazon CloudFront price class.                                                           |
| `geoRestriction` | None                                                         | Country allow/block list for the distribution.                                           |
| `buildCache`     | Disabled                                                     | Amazon S3-backed framework build cache.                                                  |
| `errorPages`     | None                                                         | Custom 404/500 HTML pages. Incompatible with SPA client-side routing.                    |
| `logging`        | Disabled                                                     | Amazon CloudFront access logging.                                                        |
| `monitoring`     | Enabled                                                      | Amazon CloudWatch alarms wired to an Amazon SNS topic.                                   |
| `skewProtection` | Enabled                                                      | Cookie-based build pinning during rolling deployments.                                   |
| `retainOnDelete` | `false`                                                      | Retain the Amazon S3 bucket when you delete the stack.                                   |

For the full construct API, adapter internals, and advanced configuration, see the [Hosting package source code on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/hosting "https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/hosting").
