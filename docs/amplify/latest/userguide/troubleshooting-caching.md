# Troubleshooting caching

If you encounter caching issues for an Amplify application, consult the topics in
this section for help.

###### Topics

- [I want to reduce the size of the cache for an
  app](#reduce-cache-size "#reduce-cache-size")
- [I want to disable reading from the cache for
  an app](#disable-reading-cache "#disable-reading-cache")

## I want to reduce the size of the cache for an

app

If you are using the cache, you might be caching intermediate files that aren't
cleaned up between builds. Caching these infrequently used files will increase the
size of your cache. To prevent this, you can exclude specific folders from being
cached by using the `!` directive in the `cache` section of
your app's build specification.

The following build settings example demonstrates how to use the `!`
directive to specify a folder that you don't want to cache.

```
cache:
  paths:
    - node_modules/**/*
    - "!node_modules/path/not/to/cache"
```

When you cache the `node_modules` folder,
`node_modules/.cache` is omitted by default.

For a full example of the build specification settings for an Amplify app, see
[Build specification YAML syntax reference](yml-specification-syntax.md#build-yaml-syntax "yml-specification-syntax.md#build-yaml-syntax")

## I want to disable reading from the cache for

an app

If you want to disable reading from the cache for an app, remove the cache section
from your app's build specification.
