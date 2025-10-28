# Requesting Python packages from upstreams and external connections

When importing a Python package version from [pypi.org](https://pypi.org/ "https://pypi.org/"), CodeArtifact will import all the assets in that
package version. While most Python packages contain a small number of assets, some contain over 100 assets, typically to support
multiple hardware architectures and Python interpreters.

It’s common for new assets to be published to pypi.org for an existing package version. For example, some projects publish new
assets when new versions of Python are released. When a Python package is installed from CodeArtifact with `pip install`,
package versions retained in the CodeArtifact repository are updated to reflect the latest set of assets from pypi.org.

Similarly, if new assets are available for a package version in an upstream CodeArtifact repository
that are not present in the current CodeArtifact repository, they will be retained in the current
repository when `pip install` is run.

## Yanked package versions

Some package versions in pypi.org are marked as _yanked_, which communicates to the package installer (such as pip)
that the version should not be installed unless it is the only one that matches a version specifier
(using either `==` or `===`). See [PEP_592](https://peps.python.org/pep-0592/ "https://peps.python.org/pep-0592/") for more information.

If a package version in CodeArtifact was originally fetched from an external connection to
[pypi.org](https://pypi.org/ "https://pypi.org/"), when you install the
package version from a CodeArtifact repository, CodeArtifact ensures that the updated yanked metadata of the package version
is fetched from pypi.org.

### How to know if a package version is yanked

To check if a package version is yanked in CodeArtifact, you can attempt to install it with
`pip install `packageName`===`packageVersion``.
If the package version is yanked, you will receive a warning message similar to the following:

```
WARNING: The candidate selected for download or install is a yanked version
```

To check if a package version is yanked in [pypi.org](https://pypi.org/ "https://pypi.org/"), you can visit the package version's pypi.org listing
at `https://pypi.org/project/`packageName`/`packageVersion`/`.

### Setting yanked status on private packages

CodeArtifact does not support setting yanked metadata for packages published directly to CodeArtifact repositories.

## Why is CodeArtifact not fetching the latest yanked metadata or assets for a package version?

Normally, CodeArtifact ensures that when a Python package version is fetched from a
CodeArtifact repository, the yanked metadata is up-to-date with the latest value on [pypi.org](https://pypi.org/ "https://pypi.org/").
Additionally, the list of assets in the package version are also kept updated with the latest set on pypi.org and any upstream CodeArtifact repositories.
This is true whether you’re installing the package version for the first time and CodeArtifact imports
it from pypi.org into your CodeArtifact repository, or if you've installed the package before.
However, there are cases when the package manager client, such as pip, won’t pull the latest yanked metadata
from pypi.org or upstream repositories. Instead, CodeArtifact will return the data that is already stored in your repository.
This section describes the three ways this can occur:

**Upstream configuration:** If the external connection to pypi.org is removed from the
repository or its upstreams using
[disassociate-external-connection](external-connection.md#removing-an-external-connection "external-connection.md#removing-an-external-connection"), yanked metadata will no
longer be refreshed from pypi.org. Similarly, if you remove an upstream repository, assets from the removed
repository and the removed repository’s upstreams will no longer be available to the current repository.
The same is true if you use CodeArtifact [package origin controls](package-origin-controls.md "package-origin-controls.md")
to prevent new versions of a specific package from being pulled—
setting `upstream=BLOCK` will block yanked metadata from being refreshed.

**Package version status:** If you set the status of a package version to anything except
`Published` or `Unlisted`, yanked metadata and assets of the package version will not be refreshed. Similarly, if you are fetching a
specific package version (say `torch 2.0.1`) and the same package version is present
in an upstream repository with a status that isn’t `Published` or `Unlisted`, this will also block
yanked metadata and asset propagation from the upstream repository to the current repository. This is
because other package version statuses are an indication that the versions are not meant to be consumed anymore in any repository.

**Direct publishing:** If you publish a specific
package version directly into a CodeArtifact repository, this will prevent yanked metadata and asset refresh for
the package version from its upstream repositories and pypi.org.
For example, say you download an asset from the package version `torch 2.0.1`,
such as `torch-2.0.1-cp311-none-macosx_11_0_arm64.whl`, using a web browser and
then publish this to your CodeArtifact repository using twine as `torch 2.0.1`. CodeArtifact tracks that the
package version entered the domain by direct publishing to your repository, not from an
external connection to pypi.org or an upstream repository. In this case, CodeArtifact does not keep the yanked metadata in sync with upstream
repositories or pypi.org. The same is true if you
publish `torch 2.0.1` into an upstream repository— the presence of the package version
will block propagation of yanked metadata and assets to repositories further down the upstream graph.
