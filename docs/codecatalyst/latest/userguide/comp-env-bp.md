Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Adding environment components to a blueprint

The custom blueprint wizard is dynamically generated from the `Options` interface exposed through the wizard. Blueprints
support generating user-interface (UI) components from exposed types.

**To import Amazon CodeCatalyst blueprints environment components**

In your `blueprint.ts` file, add the following:

```
import {...} from '@amazon-codecatalyst/codecatalyst-environments'
```

###### Topics

- [Creating development environments](#create-dev-env-bp "#create-dev-env-bp")
- [List of environments](#list-env-bp "#list-env-bp")
- [Mock interface examples](#examples-comp-env-bp "#examples-comp-env-bp")

## Creating development environments

The following example shows how to deploy your application to the cloud:

```
export interface Options extends ParentOptions {
        ...
        myNewEnvironment:  EnvironmentDefinition{
            thisIsMyFirstAccountConnection: AccountConnection{
                thisIsARole: Role['lambda', 's3', 'dynamo'];
             };
        };
    }
```

The interface generates a UI component that asks for a new environment
(`myNewEnvironment`) with a single account connection
(`thisIsMyFirstAccountConnection`. A role on the account connection
(`thisIsARole`) is also generated with `['lambda', 's3', 'dynamo']` as
the minimum required role capabilities. Not all users have account connections, so you should
check for the case where a user doesn't connect an account or doesn't connect an account with
a role. Roles can also be annotated with `@inlinePolicies`. For more information,
see [@inlinePolicy ./path/to/policy/file.json](wizard-bp.md#inline-policy-tag "wizard-bp.md#inline-policy-tag").

The environment component requires a `name` and `environmentType`.
The following code is the minimum required default shape:

```
{
  ...
  "myNewEnvironment": {
    "name": "myProductionEnvironment",
    "environmentType": "PRODUCTION"
  },
}
```

The UI component then prompts you for various fields. As you fill in the fields, the
blueprint gets a fully expanded shape. It can be helpful for you to include the full mock in
the `defaults.json` file for testing and development purposes.

## List of environments

Specifying an array of type `EnvironmentDefinition` will generate a list of
environments in the wizard UI.

```
export interface Options extends ParentOptions {
    ...
   /**
     @showName readOnly
   */
    myEnvironments:  EnvironmentDefinition<{
        thisIsMyFirstAccountConnection: AccountConnection<{
            thisIsARole: Role<['lambda', 's3', 'dynamo']>;
        }>;
    }>[];

}
```

The following example shows the defaults for an environment list:

```
{
  ...
  "myEnvironments": [
  {
    "name": "myProductionEnvironment",
    "environmentType": "PRODUCTION"
  },
  {
    "name": "myDevelopmentEnvironment",
    "environmentType": "DEVELOPMENT"
  },
  ]
}
```

## Mock interface examples

### Simple mock interface

```
{
    ...
    "thisIsMyEnvironment": {
        "name": "myProductionEnvironment",
        "environmentType": "PRODUCTION",
        "thisIsMySecondAccountConnection": {
            "id": "12345678910",
            "name": "my-account-connection-name",
            "secondAdminRole": {
                "arn": "arn:aws:iam::12345678910:role/ConnectedQuokkaRole",
                "name": "ConnectedQuokkaRole",
                "capabilities": [
                    "lambda",
                    "s3",
                    "dynamo"
                ]
            }
        }
    }
}
```

### Complex mock interface

```
export interface Options extends ParentOptions {
  /**
   * The name of an environment
   * @displayName This is a Environment Name
   * @collapsed
   */
  thisIsMyEnvironment: EnvironmentDefinition{
    /**
     * comments about the account that is being deployed into
     * @displayName This account connection has an overriden name
     * @collapsed
     */
    thisIsMyFirstAccountConnection: AccountConnection{
      /**
       * Blah blah some information about the role that I expect
       * e.g. here's a copy-pastable policy: [to a link]
       * @displayName This role has an overriden name
       */
      adminRole: Role['admin', 'lambda', 's3', 'cloudfront'];
      /**
       * Blah blah some information about the second role that I expect
       * e.g. here's a copy-pastable policy: [to a link]
       */
      lambdaRole: Role['lambda', 's3'];
    };
    /**
     * comments about the account that is being deployed into
     */
    thisIsMySecondAccountConnection: AccountConnection{
      /**
         * Blah blah some information about the role that I expect
         * e.g. here's a copy-pastable policy: [to a link]
         */
      secondAdminRole: Role['admin', 'lambda', 's3', 'cloudfront'];
      /**
         * Blah blah some information about the second role that I expect
         * e.g. here's a copy-pastable policy: [to a link]
         */
      secondLambdaRole: Role['lambda', 's3'];
    };
  };
}
```

### Complete mock interface

```
{
  ...
  "thisIsMyEnvironment": {
    "name": "my-production-environment",
    "environmentType": "PRODUCTION",
    "thisIsMySecondAccountConnection": {
      "id": "12345678910",
      "name": "my-connected-account",
      "secondAdminRole": {
        "name": "LambdaQuokkaRole",
        "arn": "arn:aws:iam::12345678910:role/LambdaQuokkaRole",
        "capabilities": [
          "admin",
          "lambda",
          "s3",
          "cloudfront"
        ]
      },
      "secondLambdaRole": {
        "name": "LambdaQuokkaRole",
        "arn": "arn:aws:iam::12345678910:role/LambdaQuokkaRole",
        "capabilities": [
          "lambda",
          "s3"
        ]
      }
    },
    "thisIsMyFirstAccountConnection": {
      "id": "12345678910",
      "name": "my-connected-account",
      "adminRole": {
        "name": "LambdaQuokkaRole",
        "arn": "arn:aws:iam::12345678910:role/LambdaQuokkaRole",
        "capabilities": [
          "admin",
          "lambda",
          "s3",
          "cloudfront"
        ]
      },
      "lambdaRole": {
        "name": "LambdaQuokkaRole",
        "arn": "arn:aws:iam::12345678910:role/LambdaQuokkaRole",
        "capabilities": [
          "lambda",
          "s3"
        ]
      }
    }
  },
}
```
