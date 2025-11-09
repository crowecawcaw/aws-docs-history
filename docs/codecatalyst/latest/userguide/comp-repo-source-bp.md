Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Adding repository and source code components to a blueprint

A repository is used by Amazon CodeCatalyst to store code. The repository takes a name as an input.
Most components are stored in a repository, such as source code files, workflows, and other
components like managed development environments (MDE). The source repository component also exports components used
for managing files and static assets. Repositories have name constraints. For more information,
see [Store and collaborate on code with source repositories in CodeCatalyst](source.md "source.md").

```
const repository = new SourceRepository(this, {
  title: 'my-new-repository-title',
});
```

**To import Amazon CodeCatalyst blueprints repository and source code
components**

In your `blueprint.ts` file, add the following:

```
import {...} from '@caws-blueprint-component/caws-source-repositories'
```

###### Topics

- [Adding a file](#repo-add-file-bp "#repo-add-file-bp")
- [Adding a generic file](#repo-add-generic-file-bp "#repo-add-generic-file-bp")
- [Copying files](#repo-copy-file-bp "#repo-copy-file-bp")
- [Targeting multiple files](#target-multiple-files-bp "#target-multiple-files-bp")
- [Creating a new repository and adding files](#repo-code-examples-bp "#repo-code-examples-bp")

## Adding a file

You can write a text file to a repository with the `SourceFile` construct. The
operation is one of the most common use cases and takes a repository, a filepath, and text
contents. If the file path doesn't exist within a repository, the component creates all the
required folders.

```
new SourceFile(repository, `path/to/my/file/in/repo/file.txt`, 'my file contents');
```

###### Note

If you write two files to the same location within the same repository, the most recent
implementation overwrites the previous one. You can use the feature to layer generated code,
and it's especially useful for extending over the code that the custom blueprints may have
generated.

## Adding a generic file

You can write arbitrary bits to your repository. You can read from a buffer and use the `File`
construct.

```
new File(repository, `path/to/my/file/in/repo/file.img`, new Buffer(...));

new File(repository, `path/to/my/file/in/repo/new-img.img`, new StaticAsset('path/to/image.png').content());
```

## Copying files

You can get started with generated code by copying and pasting starter code and then
generating more code on top of that base. Place the code inside the `static-assets`
directory, and then target that code with the `StaticAsset` construct. The path in
this case always begins at the root of the `static-assets` directory.

```
const starterCode = new StaticAsset('path/to/file/file.txt')
const starterCodeText = new StaticAsset('path/to/file/file.txt').toString()
const starterCodeRawContent = new StaticAsset('path/to/image/hello.png').content()

const starterCodePath = new StaticAsset('path/to/image/hello.png').path()
// starterCodePath is equal to 'path/to/image/hello.png'
```

A subclass of `StaticAsset` is `SubstitutionAsset`. The subclass
functions exactly the same, but instead you can run a mustache substitution over the file
instead. It can be useful for performing copy-and-replace style generation.

Static asset substitution uses a mustache templating engine to render the static files that
are seeded into the generated source repository. Mustache templating rules are applied during the
rendering, which means that all values are HTML-encoded by default. To render unescaped HTML, use
the triple mustache syntax `{{{name}}}`. For more information, see the
[mustache templating
rules](https://github.com/janl/mustache.js?tab=readme-ov-file#variables "https://github.com/janl/mustache.js?tab=readme-ov-file#variables").

###### Note

Running a substitute over files that aren't text-interpretable can produce errors.

```
const starterCodeText = new SubstitionAsset('path/to/file/file.txt').subsitite({
  'my_variable': 'subbed value1',
  'another_variable': 'subbed value2'
})
```

## Targeting multiple files

Static assets support glob targeting through a static function on `StaticAsset` and its subclasses called
`findAll(...)`, which returns a list of static assets preloaded with their paths, contents, and more. You can chain
the list with `File` constructions to copy and paste contents in the `static-assets` directory.

```
new File(repository, `path/to/my/file/in/repo/file.img`, new Buffer(...));

new File(repository, `path/to/my/file/in/repo/new-img.img`, new StaticAsset('path/to/image.png').content());
```

## Creating a new repository and adding files

You can use a repository component to create a new repository in a generated project. You can
then add files or workflows to the created repository.

```
import { SourceRepository } from '@amazon-codecatalyst/codecatalyst-source-repositories';
...
const repository = new SourceRepository(this, { title: 'myRepo' });
```

The following example shows how to add files and workflows to an existing repository:

```
import { SourceFile } from '@amazon-codecatalyst/codecatalyst-source-repositories';
import { Workflow } from '@amazon-codecatalyst/codecatalyst-workflows';
...
new SourceFile(repository, 'README.md', 'This is the content of my readme');
new Workflow(this, repository, {/**...workflowDefinition...**/});
```

Combining the two pieces of code generates a single repository named
`myRepo` with a source file `README.md` and a CodeCatalyst
workflow at the root.
