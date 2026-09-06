

# Supported platforms
<a name="supported-platforms"></a>

 AWS Blocks supports web, desktop, and mobile platforms. Your backend API is defined once in TypeScript, and type-safe clients are available for every supported platform.

## Web frameworks
<a name="platforms-web"></a>

 AWS Blocks auto-detects your web framework and configures the development server and deployment pipeline accordingly. The following frameworks are supported:


| Framework | Minimum version | Notes | 
| --- | --- | --- | 
| Next.js | 15.x | Full SSR support with automatic route detection and middleware handling | 
| Nuxt | 4.x | SSR via Nitro adapter with automatic server routes | 
| Astro | 4.x | Static and SSR modes supported | 
| SolidStart | 1.x | Via Nitro adapter | 
| TanStack Start | 1.x | Via Nitro adapter | 
| React (SPA) | 18.x | Static single-page application, any build tool (Vite, Create React App) | 
| Vue (SPA) | 3.x | Static single-page application via Vite | 
| Svelte (SPA) | 4.x | Static single-page application via Vite or SvelteKit (static adapter) | 
| Angular (SPA) | 17.x | Static single-page application | 

For SPA frameworks, AWS Blocks serves static assets from CloudFront with S3 origin. For SSR frameworks (Next.js, Nuxt, Astro SSR), AWS Blocks deploys server-side rendering via Lambda compute.

Framework detection is automatic based on your `package.json` dependencies. You can override it explicitly in your Hosting configuration.

## Native and mobile platforms
<a name="platforms-native"></a>

 AWS Blocks generates typed native clients from your backend API via OpenRPC codegen. You define your API once in TypeScript, and native platform SDKs are generated automatically.


| Platform | Language | Use case | 
| --- | --- | --- | 
| iOS | Swift | Native iOS applications via Swift Package Manager | 
| Android | Kotlin | Native Android applications via Maven/Gradle | 
| Cross-platform mobile | Dart (Flutter) | iOS, Android, web, and desktop from a single codebase | 
| Desktop | Kotlin, Dart | Desktop applications with type-safe backend access | 

### How native codegen works
<a name="how-native-codegen-works"></a>

The build pipeline generates an OpenRPC specification (`aws-blocks/blocks.spec.json`) from your `ApiNamespace` methods. Native codegen tools read this specification to produce typed SDKs for each platform.

The codegen pipeline has two layers:

 **Platform SDK** (hand-written, built once per platform)  
Handles transport (HTTP JSON-RPC), authentication (cookie management, token injection), Realtime hydration (WebSocket connections), and FileBucket hydration (presigned URL operations).

 **Generated typed facade** (app-specific, produced by codegen)  
One typed method per `ApiNamespace` method. Calls into the platform SDK’s transport layer. Contains no transport logic.

To generate the specification:

```
npx blocks-generate-spec
```

This reads `aws-blocks/index.ts` and writes `aws-blocks/blocks.spec.json`. Add it to your build script for continuous generation:

```
{
  "scripts": {
    "build:spec": "blocks-generate-spec",
    "build": "npm run build:spec && tsc && vite build"
  }
}
```

### Writing APIs for native compatibility
<a name="writing-apis-for-native-compatibility"></a>

TypeScript method signatures produce correct native types automatically. For richer types (format constraints, enums), use Zod schemas:
+ Plain TypeScript types (tier 2): correct base types inferred from method signatures
+ Zod schemas (tier 1): full JSON Schema with constraints (`format: uuid`, `maxLength`, `minLength`)
+ If neither is detected, parameters emit as `unknown` (generates `Any` in native clients)

For best results, use explicit return types and Zod validation on complex inputs.

## Hosting and deployment
<a name="platforms-hosting"></a>

 AWS Blocks provides `Hosting` (import from `@aws-blocks/blocks/cdk`) for deploying your frontend alongside your backend. Hosting provisions:
+  **Amazon CloudFront** distribution with global edge caching
+  **Amazon S3** origin for static assets
+  **Lambda compute** for server-side rendering (SSR frameworks only)
+  **Optional WAF** integration for security rules
+  **Custom domains** with automatic DNS and TLS
+  **Skew protection** for zero-downtime deployments

Locally, your frontend runs on `http://localhost:3000` with hot reload. Hosting is deployed when you run `npm run deploy` (full deployment). Sandbox deployments (`npm run sandbox`) do not include hosting because they focus on backend hot-swapping.

### Framework auto-detection
<a name="framework-auto-detection"></a>

Hosting detects your framework from `package.json` dependencies:
+  `next` in dependencies → Next.js adapter
+  `nuxt`, `nitropack`, `@solidjs/start`, `@tanstack/start` → Nitro adapter
+  `astro` → Astro adapter
+ None of the above → SPA/static adapter

Override detection by setting `framework` explicitly in your Hosting configuration.