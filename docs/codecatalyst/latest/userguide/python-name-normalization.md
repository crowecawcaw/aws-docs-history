Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Python package name normalization

CodeCatalyst normalizes package names before storing them, which means the package names in CodeCatalyst may be different than the name provided when the
package was published.

For Python packages, when performing normalization the package name is lowercased and all instances of the characters
`.`, `-`, and `_` are
replaced with a single `-` character. So the package names `pigeon_cli` and
`pigeon.cli` are normalized and stored as `pigeon-cli`.
The non-normalized name can be used by pip and twine. For more information about Python package name normalization, see
[PEP 503](https://www.python.org/dev/peps/pep-0503/#normalized-names "https://www.python.org/dev/peps/pep-0503/#normalized-names") in the Python documentation.
