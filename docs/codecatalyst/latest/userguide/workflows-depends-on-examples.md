Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Examples of how to configure

dependencies between actions

The following examples show how to configure dependencies between actions and
groups in the workflow definition file.

###### Topics

- [Example: Configuring a
  simple dependency](#workflows-depends-on-example-simple "#workflows-depends-on-example-simple")
- [Example:
  Configuring an action group to depend on an action](#workflows-depends-on-example-action-groups-actions "#workflows-depends-on-example-action-groups-actions")
- [Example:
  Configuring an action group to depend on another action group](#workflows-depends-on-example-two-action-groups "#workflows-depends-on-example-two-action-groups")
- [Example: Configuring an
  action group to depend on multiple actions](#workflows-depends-on-example-advanced "#workflows-depends-on-example-advanced")

## Example: Configuring a

simple dependency

The following example shows how to configure a `Test` action to
depend on the `Build` action using the `DependsOn`
property.

```
Actions:
  Build:
    Identifier: aws/build@v1
    Configuration:
      ...
  Test:
    **DependsOn:
 - Build**
    Identifier: aws/managed-test@v1
     Configuration:
       ...
```

## Example:

Configuring an action group to depend on an action

The following example shows how to configure a `DeployGroup` action
group to depend on the `FirstAction` action. Notice that action and
action group are at the same level.

```
Actions:
  FirstAction: #An action outside an action group
    Identifier: aws/github-actions-runner@v1
    Configuration:
      ...
  DeployGroup: #An action group containing two actions
    **DependsOn:
 - FirstAction**
    Actions:
      DeployAction1:
      ...
      DeployAction2:
      ...
```

## Example:

Configuring an action group to depend on another action group

The following example shows how to configure a `DeployGroup` action
group to depend on the `BuildAndTestGroup` action group. Notice that
the action groups are at the same level.

```
Actions:
  BuildAndTestGroup: # Action group 1
    Actions:
      BuildAction:
      ...
      TestAction:
      ...
  DeployGroup: #Action group 2
    **DependsOn:
 - BuildAndTestGroup**
    Actions:
      DeployAction1:
      ...
      DeployAction2:
      ...
```

## Example: Configuring an

action group to depend on multiple actions

The following example shows how to configure a `DeployGroup` action
group to depend on the `FirstAction` action, the
`SecondAction` action, as well as the
`BuildAndTestGroup` action group. Notice that
`DeployGroup` is at the same level as `FirstAction`,
`SecondAction`, and `BuildAndTestGroup`.

```
Actions:
  FirstAction: #An action outside an action group
    ...
  SecondAction: #Another action
    ...
  BuildAndTestGroup: #Action group 1
    Actions:
      Build:
      ...
      Test:
      ...
  DeployGroup: #Action group 2
    **DependsOn:
 - FirstAction
 - SecondAction
 - BuildAndTestGroup**
    Actions:
      DeployAction1:
      ...
      DeployAction2:
      ...
```
