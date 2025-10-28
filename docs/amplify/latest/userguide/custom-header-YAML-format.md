# Custom header YAML reference

Specify custom headers using the following YAML format:

```
customHeaders:
  - pattern: `'*.json'`
    headers:
    - key: `'custom-header-name-1'`
      value: `'custom-header-value-1'`
    - key: `'custom-header-name-2'`
      value: `'custom-header-value-2'`
  - pattern: `'/path/*'`
    headers:
    - key: `'custom-header-name-1'`
      value: `'custom-header-value-2'`
```

For a monorepo, use the following YAML format:

```
applications:
  - appRoot: `app1`
    customHeaders:
    - pattern: `'**/*'`
      headers:
      - key: `'custom-header-name-1'`
        value: `'custom-header-value-1'`
  - appRoot: `app2`
    customHeaders:
    - pattern: `'/path/*.json'`
      headers:
      - key: `'custom-header-name-2'`
        value: `'custom-header-value-2'`

```

When you add custom headers to your app, you will specify your own values for the
following:

**pattern**

Custom headers are applied to all URL file paths that match the pattern.

**headers**

Defines the headers that match the file pattern.

**key**

The name of the custom header.

**value**

The value of the custom header.

To learn more about HTTP headers, see Mozilla's list of [HTTP Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers").
