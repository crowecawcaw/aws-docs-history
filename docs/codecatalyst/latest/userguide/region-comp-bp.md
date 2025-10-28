Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Adding region components to a blueprint

The region type can be added to your custom blueprint's `Options` interface to generate a
component in the blueprint wizard you can input one or more AWS gions. The gion type can be
imported from your base blueprint in your `blueprint.ts` file. For more
information, see [AWS regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/").

**To import Amazon CodeCatalyst blueprints region type**

In your `blueprint.ts` file, add the following:

```
import { Region } from '@amazon-codecatalyst/blueprints.blueprint'
```

The region type parameter is an array of AWS region codes to choose from, or you can use
`*` to include all supported AWS regions.

###### Topics

- [Annotations](#region-annotations-bp "#region-annotations-bp")
- [Region components examples](#region-components-examples "#region-components-examples")

## Annotations

JSDoc tags can be added to each field in the `Options` interface to customize how a field
appears and behaves in the wizard. For the region type, the following tags are
supported:

- The `@displayName` annotation can be used to change the field's label in the wizard.

Example: `@displayName AWS Region`

- The `@placeholder` annotation can be used to change the select/multiselect
  component's placeholder.

Example: `@placeholder Choose AWS Region`

## Region components examples

### Choosing a region from a specified list

```
export interface Options extends ParentOptions {
    ...
  /**
   * @displayName Region
   */
  region: Region<['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']>;
}
```

### Choosing one or more regions from a specified

list

```
export interface Options extends ParentOptions {
    ...
  /**
   * @displayName Regions
   */
  multiRegion: Region<['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']>[];
}
```

### Choosing one AWS egion

```
export interface Options extends ParentOptions {
    ...
  /**
   * @displayName Region
   */
  region: Region<['*']>;
}
```

### Choosing one or more regions from a specified

list

```
export interface Options extends ParentOptions {
    ...
  /**
   * @displayName Regions
   */
  multiRegion: Region<['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']>[];
}
```
