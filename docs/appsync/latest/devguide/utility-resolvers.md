# Configuring utilities for the `APPSYNC_JS` runtime

AWS AppSync provides two libraries that aid in the development of resolvers with the `APPSYNC_JS`
runtime:

- `@aws-appsync/eslint-plugin` - Catches and fixes problems quickly during
  development.
- `@aws-appsync/utils` - Provides type validation and autocompletion in code editors.

## Configuring the eslint plugin

[ESLint](https://eslint.org/ "https://eslint.org/") is a tool that statically analyzes your code to quickly
find problems. You can run ESLint as part of your continuous integration pipeline.
`@aws-appsync/eslint-plugin` is an ESLint plugin that catches invalid syntax in your code when
leveraging the `APPSYNC_JS` runtime. The plugin allows you to quickly get feedback about your
code during development without having to push your changes to the cloud.

`@aws-appsync/eslint-plugin` provides two rule sets that you can use during development.

**"plugin:@aws-appsync/base"** configures a base set of rules that you can
leverage in your project:

| Rule                           | Description                                                                       |
| ------------------------------ | --------------------------------------------------------------------------------- |
| no-async                       | Async processes and promises are not supported.                                   |
| no-await                       | Async processes and promises are not supported.                                   |
| no-classes                     | Classes are not supported.                                                        |
| no-for                         | `for` is not supported (except for `for-in` and `for-of`,<br>which are supported) |
| no-continue                    | `continue` is not supported.                                                      |
| no-generators                  | Generators are not supported.                                                     |
| no-yield                       | `yield` is not supported.                                                         |
| no-labels                      | Labels are not supported.                                                         |
| no-this                        | `this` keyword is not supported.                                                  |
| no-try                         | Try/catch structure is not supported.                                             |
| no-while                       | While loops are not supported.                                                    |
| no-disallowed-unary-operators  | `++`, `--`, and `~` unary operators are not<br>allowed.                           |
| no-disallowed-binary-operators | The `instanceof` operator is not allowed.                                         |
| no-promise                     | Async processes and promises are not supported.                                   |

**"plugin:@aws-appsync/recommended"** provides some additional rules but
also requires you to add TypeScript configurations to your project.

| Rule                  | Description                                                                                                                                                         |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| no-recursion          | Recursive function calls are not allowed.                                                                                                                           |
| no-disallowed-methods | Some methods are not allowed. See the [reference](resolver-util-reference-js.md "resolver-util-reference-js.md") for a full<br>set of supported built-in functions. |
| no-function-passing   | Passing functions as function arguments to functions is not allowed.                                                                                                |
| no-function-reassign  | Functions cannot be reassigned.                                                                                                                                     |
| no-function-return    | Functions cannot be the return value of functions.                                                                                                                  |

To add the plugin to your project, follow the installation and usage steps at [Getting Started
with ESLint](https://eslint.org/docs/latest/user-guide/getting-started#installation-and-usage "https://eslint.org/docs/latest/user-guide/getting-started#installation-and-usage"). Then, install the [plugin](https://www.npmjs.com/package/@aws-appsync/eslint-plugin "https://www.npmjs.com/package/@aws-appsync/eslint-plugin") in your project using your
project package manager (e.g., npm, yarn, or pnpm):

```
$ npm install @aws-appsync/eslint-plugin
```

In your `.eslintrc.{js,yml,json}` file, add **"plugin:@aws-appsync/base"** or **"plugin:@aws-appsync/recommended"** to the `extends` property. The snippet below is
a basic sample `.eslintrc` configuration for JavaScript:

```
{
  "extends": ["plugin:@aws-appsync/base"]
}
```

To use the **"plugin:@aws-appsync/recommended"** rule set, install the
required dependency:

```
$ npm install -D @typescript-eslint/parser
```

Then, create an `.eslintrc.js` file:

```
{
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaVersion": 2018,
    "project": "./tsconfig.json"
  },
  "extends": ["plugin:@aws-appsync/recommended"]
}
```
