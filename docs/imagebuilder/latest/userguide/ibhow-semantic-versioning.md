# Semantic versioning in Image Builder

Image Builder uses semantic versioning to organize resources and ensure that
they have unique IDs. The semantic version has four nodes:

_`<major>`.`<minor>`.`<patch>`/<build>_

You can assign values for the first three, and can filter on all of them.

Semantic versioning is included in each object's Amazon Resource Name (ARN),
at the level that applies to that object as follows:

1. Versionless ARNs and Name ARNs do not include specific values in any of the nodes. The nodes are
   either left off entirely, or they are specified as wildcards, for example: x.x.x.
2. Version ARNs have only the first three nodes: <major>.<minor>.<patch>
3. Build version ARNs have all four nodes, and point to a specific build for a specific version of an object.
   **Assignment:** For the first three nodes you can assign any positive integer value, or
   zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the
   build number to the fourth node.

**Patterns:** You can use any numeric pattern that adheres to the assignment requirements for
the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or
a date, such as 2021.01.01.

**Selection:** With semantic versioning, you have the flexibility to use wildcards (x)
to specify the most recent versions or nodes when selecting the base image or components for your
recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be
wildcards.

For example, given the following recent versions: 2.2.4, 1.7.8, and 1.6.8, version
selection using wildcards produces the following results:

- `x.x.x` = 2.2.4
- `1.x.x` = 1.7.8
- `1.6.x` = 1.6.8
- `x.2.x` is not valid, and produces an error
- `1.x.8` is not valid, and produces an error

## Using version references

Version references are ready-to-use ARN strings that incorporate wildcard patterns based
on the semantic version of the resource you created or retrieved. Instead of writing custom code
to parse ARNs and insert wildcards, Image Builder does this work for you.

When you create or retrieve Image Builder resources, Image Builder automatically provides
pre-constructed ARNs with wildcard version patterns in the `latestVersionReferences` object. This
eliminates the need to manually parse and reconstruct ARNs when you want to reference resources
using wildcard versioning patterns.

For example, when you create a component with version `1.2.3`, Image Builder returns:

```

{
    "componentBuildVersionArn": "arn:aws:imagebuilder:us-west-2:123456789012:component/my-component/1.2.3/1",
    "latestVersionReferences": {
        "latestVersionArn": "arn:aws:imagebuilder:us-west-2:123456789012:component/my-component/x.x.x",
        "latestMajorVersionArn": "arn:aws:imagebuilder:us-west-2:123456789012:component/my-component/1.x.x",
        "latestMinorVersionArn": "arn:aws:imagebuilder:us-west-2:123456789012:component/my-component/1.2.x",
        "latestPatchVersionArn": "arn:aws:imagebuilder:us-west-2:123456789012:component/my-component/1.2.3"
    }
}

```

## Available version reference patterns

The `latestVersionReferences` object contains four ARN patterns:

- latestVersionArn (x.x.x) - Always resolves to the absolute latest version.
- atestMajorVersionArn (1.x.x) - Resolves to the latest minor and patch versions within a major version.
- latestMinorVersionArn (1.2.x) - Resolves to the latest patch version within a specific minor version.
- latestPatchVersionArn (1.2.3) - References a specific semantic version and resolves to the latest build version for resources that support multiple build versions.

## Resources that return version references

Version references are returned by `Create` and `Get` APIs for all versioned Image Builder resources:

- Components - `CreateComponent`, `GetComponent`
- Image recipes - `CreateImageRecipe`, `GetImageRecipe`
- Container recipes - `CreateContainerRecipe`, `GetContainerRecipe`
- Images - `CreateImage`, `GetImage`
- Workflows - `CreateWorkflow`, `GetWorkflow`

_Note:_ For Image Builder-managed workflows, only `latestVersionArn (x.x.x)` is returned, since Image Builder requires you to always use the latest version of Image Builder-managed workflows.
