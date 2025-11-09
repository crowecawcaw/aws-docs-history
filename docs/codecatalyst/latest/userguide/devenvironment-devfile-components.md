Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Devfile components

Currently, CodeCatalyst only supports `container` components in your devfile. For more information, see [Adding components](https://devfile.io/docs/2.0.0/adding-components "https://devfile.io/docs/2.0.0/adding-components") in the
Devfile.io documentation.

The following example shows you how to add a startup command to your container in your
devfile.

```
components:
  - name: test
    container:
      image: public.ecr.aws/amazonlinux/amazonlinux:2
      command: ['sleep', 'infinity']

```

###### Note

When the container has short lived entry command, you must include
`command: ['sleep', 'infinity']` to keep the container running.

CodeCatalyst also supports the following properties in your container component:
`args`, `env`, `mountSources`, and
`volumeMounts`.
