# Troubleshooting redirects and rewrites

If you encounter issues when setting up redirects and rewrites for an Amplify
application, consult the topics in this section for help.

###### Topics

- [Access is denied for certain routes even with the SPA redirect rule.](#spa-redirect-access-denied "#spa-redirect-access-denied")
- [I want to set up a reverse proxy to an API](#reverse-proxy-api "#reverse-proxy-api")

## Access is denied for certain routes even with the SPA redirect rule.

If you are getting an access denied error for certain routes with an SPA redirect
rule, the `baseDirectory` might not be set correctly in the app's build
settings. For example, if your app's frontend is built to the `build`
directory, your build settings must also point to the `build` directory.
The following build specification example demonstrates this setting.

```
frontend:
  artifacts:
    baseDirectory: build
    files:
        - "**/*"
```

For a full example of the build specification settings for an Amplify app, see
[Build specification YAML syntax reference](yml-specification-syntax.md#build-yaml-syntax "yml-specification-syntax.md#build-yaml-syntax")

## I want to set up a reverse proxy to an API

You can use the following JSON to set up a reverse proxy to a dynamic
endpoint.

```
[
  {
    "source": "/documents/<*>",
    "target": "https://otherdomain/resource/<*>",
    "status": "200",
    "condition": null
  }
]
```

For a basic example of creating a reverse proxy for your Amplify app to a
third-party API, see [Reverse proxy rewrite](redirect-rewrite-examples.md#reverse-proxy-rewrite "redirect-rewrite-examples.md#reverse-proxy-rewrite").
