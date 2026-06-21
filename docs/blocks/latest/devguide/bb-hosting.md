# Hosting

This section covers frontend hosting and deployment.

## Hosting

Frontend deployment with server-side rendering (SSR) support. Hosting auto-detects your frontend framework (Next.js, Nuxt, Astro, or SPA) and provisions the appropriate AWS resources. Import from `@aws-blocks/blocks/cdk` and use in your CDK layer file (`aws-blocks/index.cdk.ts`).

Locally, your frontend is served by the development server at `http://localhost:3000` with hot reload. On AWS, Hosting provisions a CloudFront distribution with S3 origin, Lambda compute for SSR, optional WAF, monitoring dashboards, and DNS records. Supports custom domains and skew protection for zero-downtime deployments.

Hosting is used in the CDK layer, not in the IFC layer. It is included automatically when you run `npm run deploy`. For sandbox deployments (`npm run sandbox`), hosting is not deployed because sandboxes focus on backend hot-swapping.

For more information, see [hosting on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/hosting "https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/hosting").
