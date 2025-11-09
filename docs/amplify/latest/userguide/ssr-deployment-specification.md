# Using the Amplify Hosting deployment

specification to configure build output

The Amplify Hosting deployment specification is a file system based specification that
defines the directory structure that facilitates deployments to Amplify Hosting. A
framework can generate this expected directory structure as the output of its build command,
enabling the framework to take advantage of Amplify Hosting’s service primitives.
Amplify Hosting understands the structure of the deployment bundle and deploys it
accordingly.

For a video demonstration that explains how to use the deployment specification, see
_How to host any website using AWS Amplify_ on the Amazon Web
Services YouTube channel.

The following is an example of the folder structure that Amplify expects for the
deployment bundle. At a high level, it has a folder named `static`, a folder
named `compute` and a deployment manifest file named
`deploy-manifest.json`.

```
.amplify-hosting/
├── compute/
│   └── default/
│       ├── chunks/
│       │   └── app/
│       │       ├── _nuxt/
│       │       │   ├── index-xxx.mjs
│       │       │   └── index-styles.xxx.js
│       │       └── server.mjs
│       ├── node_modules/
│       └── server.js
├── static/
│   ├── css/
│   │   └── nuxt-google-fonts.css
│   ├── fonts/
│   │   ├── font.woff2
│   ├── _nuxt/
│   │   ├── builds/
│   │   │   └── latest.json
│   │   └── entry.xxx.js
│   ├── favicon.ico
│   └── robots.txt
└── deploy-manifest.json

```

## Amplify SSR primitive support

The Amplify Hosting deployment specification defines a contract that closely maps
to the following primitives.

**Static assets**

Provides frameworks with the ability to host static files.

**Compute**

Provides frameworks with the ability to run a Node.js HTTP server on port 3000.

**Image optimization**

Provides frameworks with a service to optimize images at runtime.

**Routing rules**

Provides frameworks with a mechanism to map incoming request paths to specific
targets.

## The .amplify-hosting/static

directory

You must place all publicly accessible static files that are meant to be served from
the application URL in the `.amplify-hosting/static` directory. The
files inside this directory are served via the static assets primitive.

Static files are accessible at the root (/) of the application URL without any changes
to their content, file name, or extension. Additionally, subdirectories are preserved in
the URL structure and appear before the file name. As an example,
`.amplify-hosting/static/favicon.ico` will be served from
`https://myAppId.amplify-hostingapp.com/favicon.ico` and
`.amplify-hosting/static/_nuxt/main.js` will be served from `https://myAppId.amplify-hostingapp.com/_nuxt/main.js`

If a framework supports the ability to modify the base path of the application, it
must prepend the base path to the static assets inside the
`.amplify-hosting/static` directory. For example, if the base path is
`/folder1/folder2`, then the build output for a static asset called
`main.css` will be
`.amplify-hosting/static/folder1/folder2/main.css`.

## The .amplify-hosting/compute

directory

A single compute resource is represented by a single subdirectory named
`default` contained within the
`.amplify-hosting/compute` directory. The path is
`.amplify-hosting/compute/default`. This compute resource maps to
Amplify Hosting's compute primitive.

The contents of the `default` subdirectory must conform to the
following rules.

- A file must exist in the root of the `default` subdirectory, to
  serve as the entry point to the compute resource.
- The entry point file must be a Node.js module and it must start an HTTP server
  that listens on port 3000.
- You can place other files in the `default` subdirectory and
  reference them from code in the entry point file.
- The contents of the subdirectory must be self-contained. Code in the entry point
  module can't reference any modules outside of the subdirectory. Note that frameworks
  can bundle their HTTP server in any way that they want. If the compute process can be
  initiated with the `node server.js` command, where `server.js
is` is the name of the entry file, from within the subdirectory, Amplify
  considers the directory structure to conform to the deployment specification.

Amplify Hosting bundles and deploys all files inside the
`default` subdirectory to a provisioned compute resource. Each
compute resource is allocated 512 MB of ephemeral storage. This storage isn't shared
between execution instances, but is shared among subsequent invocations within the same
execution instance. Execution instances are limited to a maximum execution time of 15
minutes, and the only writable path within the execution instance is the
`/tmp` directory. The uncompressed size of each compute resource bundle
can't exceed 220 MB. For example, the `.amplify/compute/default`
subdirectory can't exceed 220 MB when uncompressed.

## The

.amplify-hosting/deploy-manifest.json file

Use the `deploy-manifest.json` file to store the configuration
details and metadata for a deployment. At a minimum, a
`deploy-manifest.json` file must include a `version`
attribute, the `routes` attribute with a catch-all route specified, and the
`framework` attribute with framework metadata specified.

The following object definition demonstrates the configuration for a deployment
manifest.

```
type DeployManifest = {
  version: 1;
  routes: Route[];
  computeResources?: ComputeResource[];
  imageSettings?: ImageSettings;
  framework: FrameworkMetadata;
};
```

The following topics describe the details and usage for each attribute in the
deployment manifest.

### Using the version attribute

The `version` attribute defines the version of the deployment
specification that you are implementing. Currently, the only version for the Amplify
Hosting deployment specification is version 1. The following JSON example demonstrates
the usage for the `version` attribute.

```
"version": 1
```

### Using the routes attribute

The `routes` attribute enables frameworks to leverage the Amplify
Hosting routing rules primitive. Routing rules provide a mechanism for routing incoming
request paths to a specific target in the deployment bundle. Routing rules only dictate
the destination of an incoming request and are applied after the request has been
transformed by rewrite and redirect rules. For more information about how Amplify
Hosting handles rewrites and redirects, see [Setting up redirects and rewrites for an Amplify
application](redirects.md "redirects.md").

Routing rules don't rewrite or transform the request. If an incoming request matches
the path pattern for a route, the request is routed as-is to the route's target.

The routing rules specified in the `routes` array must conform to the
following rules.

- A catch-all route must be specified. A catch-all route has the `/*`
  pattern that matches all incoming requests.
- The `routes` array can contain a maximum of 25 items.
- You must specify either a `Static` route or a `Compute`
  route.
- If you specify a `Static` route, the
  `.amplify-hosting/static` directory must exist.
- If you specify a `Compute` route, the
  `.amplify-hosting/compute` directory must exist.
- If you specify an `ImageOptimization` route, you must also specify a
  `Compute` route. This is required because image optimization is not yet
  supported for purely static applications.

The following object definition demonstrates the configuration for the
`Route` object.

```
type Route = {
  path: string;
  target: Target;
  fallback?: Target;
}
```

The following table describes the `Route` object's properties.

| Key      | Type   | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------- | ------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path     | String | Yes      | Defines a pattern that matches incoming request paths (excluding<br>querystring).<br>The maximum path length is 255 characters.<br>A path must start with the forward slash `/`.<br>A path can contain any of the following characters: [A-Z], [a-z], [0-9],[<br>\_-.\*$/~"'@:+].<br>For pattern matching, only the following wildcard characters are<br>supported:<br>• `*` (matches 0 or more characters)<br>• The `/*` pattern is called a catch-all pattern and will<br>match all incoming requests. |
| target   | Target | Yes      | An object that defines the target to route the matched request to.<br>If a `Compute` route is specified, a corresponding<br>`ComputeResource` must exist.<br>If an `ImageOptimization` route is specified,<br>`imageSettings` must also be specified.                                                                                                                                                                                                                                                    |
| fallback | Target | No       | An object that defines the target to fallback to if the original target<br>returns a 404 error.<br>The `target` kind and the `fallback` kind can't be<br>the same for a specified route. For example, fallback from `Static`<br>to `Static` is not allowed. Fallbacks are only supported for GET<br>requests that don't have a body. If a body is present in the request, it will<br>be dropped during the fallback.                                                                                     |

The following object definition demonstrates the configuration for the
`Target` object.

```
type Target = {
  kind: TargetKind;
  src?: string;
  cacheControl?: string;
}
```

The following table describes the `Target` object's properties.

| Key          | Type       | Required                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------ | ---------- | -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| kind         | Targetkind | Yes                                          | An `enum` that defines the target type. Valid values are<br>`Static`, `Compute`, and<br>`ImageOptimization`.                                                                                                                                                                                                                                                                                                                                                                                 |
| src          | String     | Yes for `Compute`<br>No for other primitives | A string that specifies the name of the subdirectory in the deployment<br>bundle that contains the primitive's executable code. Valid and required only<br>for the Compute primitive.<br>The value must point to one of the compute resources present in the<br>deployment bundle. Currently, the only supported value for this field is<br>`default`.                                                                                                                                       |
| cacheControl | String     | No                                           | A string that specifies the value of the Cache-Control header to apply to<br>the response. Valid only for the Static and the ImageOptimization<br>primitives.<br>The specified value is overriden by custom headers. For more information<br>about Amplify Hosting customer headers, see [Setting custom headers for an Amplify app](custom-headers.md "custom-headers.md").<br>NoteThis Cache-Control header is only applied to successful responses with a<br>status code set to 200 (OK). |

The following object definition demonstrates the usage for the
`TargetKind` enumeration.

```
enum TargetKind {
  Static = "Static",
  Compute = "Compute",
  ImageOptimization = "ImageOptimization"
}
```

The following list specifies the valid values for the `TargetKind`
enum.

**Static**

Routes requests to the static assets primitive.

**Compute**

Routes requests to the compute primitive.

**ImageOptimization**

Routes requests to the image optimization primitive.

The following JSON example demonstrates the usage for the `routes`
attribute with multiple routing rules specified.

```
"routes": [
    {
      "path": "/_nuxt/image",
      "target": {
        "kind": "ImageOptimization",
        "cacheControl": "public, max-age=3600, immutable"
      }
    },
    {
      "path": "/_nuxt/builds/meta/*",
      "target": {
        "cacheControl": "public, max-age=31536000, immutable",
        "kind": "Static"
      }
    },
    {
      "path": "/_nuxt/builds/*",
      "target": {
        "cacheControl": "public, max-age=1, immutable",
        "kind": "Static"
      }
    },
    {
      "path": "/_nuxt/*",
      "target": {
        "cacheControl": "public, max-age=31536000, immutable",
        "kind": "Static"
      }
    },
    {
      "path": "/*.*",
      "target": {
        "kind": "Static"
      },
      "fallback": {
        "kind": "Compute",
        "src": "default"
      }
    },
    {
      "path": "/*",
      "target": {
        "kind": "Compute",
        "src": "default"
      }
    }
  ]
```

For more information about specifying routing rules in your deployment manifest, see
[Best practices for configuring routing
rules](#routing-best-practices "#routing-best-practices")

### Using the computeResources

attribute

The `computeResources` attribute enables frameworks to provide metadata
about the provisioned compute resources. Every compute resource must have a
corresponding route associated with it.

The following object definition demonstrates the usage for the
`ComputeResource` object.

```
type ComputeResource = {
  name: string;
  runtime: ComputeRuntime;
  entrypoint: string;
};

type ComputeRuntime = 'nodejs20.x' | 'nodejs22.x';
```

The following table describes the `ComputeResource` object's
properties.

| Key        | Type           | Required | Description                                                                                                                                                                                                                                 |
| ---------- | -------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name       | String         | Yes      | Specifies the name of the compute resource. The name must match the name<br>of the subdirectory inside the `.amplify-hosting/compute<br>directory`.<br>For version 1 of the deployment specification, the only valid value is<br>`default`. |
| runtime    | ComputeRuntime | Yes      | Defines the runtime for the provisioned compute resource.<br>Valid values are `nodejs20.x` and<br>`nodejs22.x`.                                                                                                                             |
| entrypoint | String         | Yes      | Specifies the name of the starting file that code will run from for the<br>specified compute resource. The file must exist inside the subdirectory that<br>represents a compute resource.                                                   |

If you have a directory structure that looks like the following.

```
.amplify-hosting
|---compute
|   |---default
|       |---index.js

```

The JSON for the `computeResource` attribute will look like the
following.

```
"computeResources": [
    {
      "name": "default",
      "runtime": "nodejs20.x",
      "entrypoint": "index.js",
    }
  ]
```

### Using the imageSettings attribute

The `imageSettings` attribute enables frameworks to customize the
behavior of the image optimization primitive, that provides on-demand optimization of
images at runtime.

The following object definition demonstrates the usage for the
`ImageSettings` object.

```
type ImageSettings = {
  sizes: number[];
  domains: string[];
  remotePatterns: RemotePattern[];
  formats: ImageFormat[];
  minumumCacheTTL: number;
  dangerouslyAllowSVG: boolean;
};

type ImageFormat = 'image/avif' | 'image/webp' | 'image/png' | 'image/jpeg';
```

The following table describes the `ImageSettings` object's
properties.

| Key                 | Type            | Required | Description                                                                                                                                                      |
| ------------------- | --------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sizes               | Number[]        | Yes      | An array of supported image widths.                                                                                                                              |
| domains             | String[]        | Yes      | An array of allowed external domains that can use image optimization.<br>Leave the array empty to allow only the deployment domain to use image<br>optimization. |
| remotePatterns      | RemotePattern[] | Yes      | An array of allowed external patterns that can use image optimization.<br>Similar to domains, but provides more control with regular expressions<br>(regex).     |
| formats             | ImageFormat[]   | Yes      | An array of allowed output image formats.                                                                                                                        |
| minimumCacheTTL     | Number          | Yes      | The cache duration in seconds for the optimized images.                                                                                                          |
| dangerouslyAllowSVG | Boolean         | Yes      | Allows SVG input image URLs. This is disabled by default for security<br>purposes.                                                                               |

The following object definition demonstrates the usage for the
`RemotePattern` object.

```
type RemotePattern = {
  protocol?: 'https';
  hostname: string;
  port?: string;
  pathname?: string;
}
```

The following table describes the `RemotePattern` object's
properties.

| Key      | Type   | Required | Description                                                                                                                                                                                                                                                     |
| -------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| protocol | String | No       | The protocol of the allowed remote pattern. The only valid value is<br>`https`.                                                                                                                                                                                 |
| hostname | String | Yes      | The hostname of the allowed remote pattern.<br>You can specify a literal or wildcard. A single `\*` matches a single<br>subdomain. A double `\*\*` matches any number of subdomains. Amplify doesn't<br>allow blanket wildcards where only `\*\*` is specified. |
| port     | String | No       | The port of the allowed remote pattern.                                                                                                                                                                                                                         |
| pathname | String | No       | The path name of the allowed remote pattern.                                                                                                                                                                                                                    |

The following example demonstrates the `imageSettings` attribute.

```
"imageSettings": {
    "sizes": [
      100,
      200
    ],
    "domains": [
      "example.com"
    ],
    "remotePatterns": [
      {
        "protocol": "https",
        "hostname": "example.com",
        "port": "",
        "pathname": "/**",
      }
    ],
    "formats": [
      "image/webp"
    ],
    "minumumCacheTTL": 60,
    "dangerouslyAllowSVG": false
  }
```

### Using the framework attribute

Use the `framework` attribute to specify framework metadata.

The following object definition demonstrates the configuration for the
`FrameworkMetadata` object.

```
type FrameworkMetadata = {
  name: string;
  version: string;
}
```

The following table describes the `FrameworkMetadata` object's
properties.

| Key     | Type   | Required | Description                                                                              |
| ------- | ------ | -------- | ---------------------------------------------------------------------------------------- |
| name    | String | Yes      | The name of the framework.                                                               |
| version | String | Yes      | The version of the framework.<br>It must be a valid semantic versioning (semver) string. |

## Best practices for configuring routing

rules

Routing rules provide a mechanism for routing incoming request paths to specific
targets in the deployment bundle. In a deployment bundle, framework authors can emit files
to the build output that are deployed to either of the following targets:

- Static assets primitive – Files are
  contained in the `.amplify-hosting/static` directory.
- Compute primitive – Files are contained in
  the `.amplify-hosting/compute/default` directory.

Framework authors also provide an array of routing rules in the deploy manifest file.
Each rule in the array is matched against the incoming request in sequential traversal
order, until there’s a match. When there’s a matching rule, the request is routed to the
target specified in the matching rule. Optionally, a fallback target can be specified for
each rule. If the original target returns a 404 error, the request is routed to the
fallback target.

The deployment specification _requires_ the last rule in the
traversal order to be a catch-all rule. A catch-all rule is specified with the
`/*` path. If the incoming request doesn't match with any of the previous
routes in the routing rules array, the request is routed to the catch-all rule
target.

For SSR frameworks like Nuxt.js, the catch-all rule target has to be
the compute primitive. This is because SSR applications have server-side rendered pages
with routes that aren't predictable at build time. For example, if a
Nuxt.js application has a page at `/blog/[slug]` where
`[slug]` is a dynamic route parameter. The catch-all rule target is the only
way to route requests to these pages.

In contrast, specific path patterns can be used to target routes that are known at
build time. For example, Nuxt.js serves static assets from the
`/_nuxt` path. This means that the `/_nuxt/*` path
can be targeted by a specific routing rule that routes requests to the static assets
primitive.

### Public folder routing

Most SSR frameworks provide the ability to serve mutable static assets from a
`public` folder. Files like `favicon.ico` and
`robots.txt` are typically kept inside the
`public` folder and are served from the application's root URL. For
example, the `favicon.ico` file is served from
`https://example.com/favicon.ico`. Note that there is no predictable path
pattern for these files. They are almost entirely dictated by the file name. The only
way to target files inside the `public` folder is to use the
catch-all route. However, the catch-all route target has to be the compute
primitive.

We recommend one of the following approaches for managing your
`public` folder.

1. Use a path pattern to target request paths that contain file extensions. For
   example, you can use `/*.*` to target all request paths that contain a
   file extension.

Note that this approach can be unreliable. For example, if there are files
without file extensions inside the `public` folder, they are not
targeted by this rule. Another issue to be aware of with this approach is that the
application could have pages with periods in their names. For example, a page at
`/blog/2021/01/01/hello.world` will be targeted by the
`/*.*` rule. This is not ideal since the page is not a static asset.
However, you can add a fallback target to this rule to ensure that when there is a
404 error from the static primitive, the request falls back to the compute
primitive.

```
{
    "path": "/*.*",
    "target": {
        "kind": "Static"
    },
    "fallback": {
        "kind": "Compute",
        "src": "default"
    }
}
```

2. Identify the files in the `public` folder at build time and
   emit a routing rule for each file. This approach is not scalable since there is a
   limit of 25 rules imposed by the deployment specification.

```
{
    "path": "/favicon.ico",
    "target": {
        "kind": "Static"
    }
},
{
    "path": "/robots.txt",
    "target": {
        "kind": "Static"
    }
}
```

3. Recommend that your framework users store all mutable static assets inside a
   sub-folder inside the `public` folder.

In the following example, the user can store all mutable static assets inside
the `public/assets` folder. Then, a routing rule with the path
pattern `/assets/*` can be used to target all mutable static assets
inside the `public/assets` folder.

```
{
    "path": "/assets/*",
    "target": {
        "kind": "Static"
    }
}
```

4. Specify a static fallback for the catch-all route. This approach has drawbacks
   that are described in more detail in the next [Catch-all fallback routing](#catchall-fallback-routing "#catchall-fallback-routing")
   section.

### Catch-all fallback routing

For SSR frameworks such as Nuxt.js, where a catch-all route is
specified for the compute primitive target, framework authors might consider specifying
a static fallback for the catch-all route to solve the `public` folder
routing problem. However, this type of routing rule breaks server-side rendered 404
pages. For example, if the end user visits a page that doesn't exist, the application
renders a 404 page with a status code of 404. However, if the catch-all route has a
static fallback, the 404 page isn't be rendered. Instead, the request falls back to the
static primitive and still ends up with a 404 status code, but the 404 page isn't be
rendered.

```
{
    "path": "/*",
    "target": {
        "kind": "Compute",
        "src": "default"
    },
    "fallback": {
        "kind": "Static"
    }
}
```

#### Base path routing

Frameworks that offer the ability to modify the base path of the application are
expected to prepend the base path to the static assets inside the
`.amplify-hosting/static` directory. For example, if the base
path is `/folder1/folder2`, then the build output for a static
asset called main.css will be
`.amplify-hosting/static/folder1/folder2/main.css`.

This means that the routing rules also need to be updated to reflect the base
path. For example, if the base path is `/folder1/folder2`, then the
routing rule for the static assets in the `public` folder will look
like the following.

```
{
    "path": "/folder1/folder2/*.*",
    "target": {
        "kind": "Static"
    }
}
```

Similarly, server-side routes also need to have the base path prepended to them.
For example, if the base path is `/folder1/folder2`, then the
routing rule for the `/api` route will look like the following.

```
{
    "path": "/folder1/folder2/api/*",
    "target": {
        "kind": "Compute",
        "src": "default"
    }
}
```

However, the base path should not be prepended to the catch-all route. For
example, if the base path is `/folder1/folder2`, then the catch-all
route will remain like the following.

```
{
    "path": "/*",
    "target": {
        "kind": "Compute",
        "src": "default"
    }
}
```

#### Nuxt.js routes examples

The following is an example `deploy-manifest.json` file for a
Nuxt application that demonstrates how to specify routing rules.

```
{
  "version": 1,
  "routes": [
    {
      "path": "/_nuxt/image",
      "target": {
        "kind": "ImageOptimization",
        "cacheControl": "public, max-age=3600, immutable"
      }
    },
    {
      "path": "/_nuxt/builds/meta/*",
      "target": {
        "cacheControl": "public, max-age=31536000, immutable",
        "kind": "Static"
      }
    },
    {
      "path": "/_nuxt/builds/*",
      "target": {
        "cacheControl": "public, max-age=1, immutable",
        "kind": "Static"
      }
    },
    {
      "path": "/_nuxt/*",
      "target": {
        "cacheControl": "public, max-age=31536000, immutable",
        "kind": "Static"
      }
    },
    {
      "path": "/*.*",
      "target": {
        "kind": "Static"
      },
      "fallback": {
        "kind": "Compute",
        "src": "default"
      }
    },
    {
      "path": "/*",
      "target": {
        "kind": "Compute",
        "src": "default"
      }
    }
  ],
  "computeResources": [
    {
      "name": "default",
      "entrypoint": "server.js",
      "runtime": "nodejs22.x"
    }
  ],
  "framework": {
    "name": "nuxt",
    "version": "3.8.1"
  }
}
```

The following is an example `deploy-manifest.json` file for
Nuxt that demonstrates how to specify routing rules including base paths.

```
{
  "version": 1,
  "routes": [
    {
      "path": "/base-path/_nuxt/image",
      "target": {
        "kind": "ImageOptimization",
        "cacheControl": "public, max-age=3600, immutable"
      }
    },
    {
      "path": "/base-path/_nuxt/builds/meta/*",
      "target": {
        "cacheControl": "public, max-age=31536000, immutable",
        "kind": "Static"
      }
    },
    {
      "path": "/base-path/_nuxt/builds/*",
      "target": {
        "cacheControl": "public, max-age=1, immutable",
        "kind": "Static"
      }
    },
    {
      "path": "/base-path/_nuxt/*",
      "target": {
        "cacheControl": "public, max-age=31536000, immutable",
        "kind": "Static"
      }
    },
    {
      "path": "/base-path/*.*",
      "target": {
        "kind": "Static"
      },
      "fallback": {
        "kind": "Compute",
        "src": "default"
      }
    },
    {
      "path": "/*",
      "target": {
        "kind": "Compute",
        "src": "default"
      }
    }
  ],
  "computeResources": [
    {
      "name": "default",
      "entrypoint": "server.js",
      "runtime": "nodejs22.x"
    }
  ],
  "framework": {
    "name": "nuxt",
    "version": "3.8.1"
  }
}
```

For more information about using the `routes` attribute, see [Using the routes attribute](#deployment-manifest-routes "#deployment-manifest-routes").
