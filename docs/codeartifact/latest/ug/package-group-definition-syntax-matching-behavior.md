# Package group definition syntax and matching behavior

This topic contains information about defining package groups, pattern matching behavior, package association strength, and
package group hierarchy.

###### Contents

- [Package group definition syntax and examples](package-group-definition-syntax-matching-behavior.md#package-group-definition-syntax-examples "package-group-definition-syntax-matching-behavior.md#package-group-definition-syntax-examples")
  - [Package group definition and normalization](package-group-definition-syntax-matching-behavior.md#package-group-definition-syntax-examples-normalization "package-group-definition-syntax-matching-behavior.md#package-group-definition-syntax-examples-normalization")
  - [Namespaces in package group definitions](package-group-definition-syntax-matching-behavior.md#package-group-definition-syntax-examples-namespaces "package-group-definition-syntax-matching-behavior.md#package-group-definition-syntax-examples-namespaces")

- [Package group hierarchy and pattern specificity](package-group-definition-syntax-matching-behavior.md#package-group-hierarchy-pattern-specificity "package-group-definition-syntax-matching-behavior.md#package-group-hierarchy-pattern-specificity")
- [Words, word boundaries, and prefix matching](package-group-definition-syntax-matching-behavior.md#package-group-word-boundary-prefix "package-group-definition-syntax-matching-behavior.md#package-group-word-boundary-prefix")
- [Case sensitivity](package-group-definition-syntax-matching-behavior.md#package-group-case-sensitivity "package-group-definition-syntax-matching-behavior.md#package-group-case-sensitivity")
- [Strong and weak match](package-group-definition-syntax-matching-behavior.md#package-group-strong-and-weak-match "package-group-definition-syntax-matching-behavior.md#package-group-strong-and-weak-match")
- [Additional variations](package-group-definition-syntax-matching-behavior.md#package-group-additional-variations "package-group-definition-syntax-matching-behavior.md#package-group-additional-variations")

## Package group definition syntax and examples

The pattern syntax for defining package groups closely follows the formatting of package paths. A package path is created
from a package's coordinate components (format, namespace, and name) by adding a forward slash to the start and separating each
of the components with a forward slash. For example, the package path for the npm package named _anycompany-ui-components_
in the namespace _space_ is _/npm/space/anycompany-ui-components_.

A package group pattern follows the same structure as a package path, except components that are not specified as part
of the group definition are omitted, and the pattern is terminated with a suffix. The suffix that is included determines the matching
behavior of the pattern, as follows:

- A `$` suffix will match the full package coordinate.
- A `~` suffix will match a prefix.
- A `*` suffix will match all values of the previously defined component.

Here are example patterns for each of the allowed combinations:

1. All package formats: `/*`
2. A specific package format: `/npm/*`
3. Package format and namespace prefix: `/maven/com.anycompany~`
4. Package format and namespace: `/npm/space/*`
5. Package format, namespace, and name prefix: `/npm/space/anycompany-ui~`
6. Package format, namespace, and name: `/maven/org.apache.logging.log4j/log4j-core$`

As shown in the examples above, the `~` suffix is added to the end of a namespace or name to represent a prefix match
and `*` comes after a forward slash when used to match all values for the next component in the path
(either all formats, all namespaces, or all names).

### Package group definition and normalization

CodeArtifact normalizes NuGet, Python, and Swift package names, and normalizes Swift package namespaces before storing them. CodeArtifact uses these
normalized names when matching packages with package group definitions. Therefore, package groups that contain a namespace or name in these
formats must use the normalized namespace and name. For more information about how
the package names and namespaces are normalized, see the [NuGet](nuget-name-normalization.md "nuget-name-normalization.md"),
[Python](python-name-normalization.md "python-name-normalization.md"), and [Swift](swift-name-normalization.md "swift-name-normalization.md") name normalization documentation.

### Namespaces in package group definitions

For packages or package formats without a
namespace (Python and NuGet), package groups must not contain a namespace. The package group definition for these
package groups contain a blank namespace section. For example, the path for the Python package named
_requests_ is _/python//requests_.

For packages or package formats with a namespace (Maven, generic, and Swift), the namespace must be included if the package name is included. For the Swift package
format, the normalized package namespace will be used. For more information about how Swift package namespaces are normalized, see
[Swift package name and namespace normalization](swift-name-normalization.md "swift-name-normalization.md").

## Package group hierarchy and pattern specificity

The packages that are “in” or “associated with” a package group are packages with a package path that matches the group’s pattern
but do not match a more specific group’s pattern. For example, given the package groups `/npm/*` and `/npm/space/*`,
the package path _/npm//react_ is associated with the first group (`/npm/*`) while _/npm/space/aui.components_
and _/npm/space/amplify-ui-core_ are associated with the
second group (`/npm/space/*`). Even though a package may match multiple groups, each package is only associated with a single group, the most specific
match, and only that one group’s configuration applies to the package.

When a package path matches multiple patterns, the “more specific” pattern can be thought of as the longest matching pattern.
Alternatively, the more specific pattern is the one that matches a proper subset of the packages that match
the less specific pattern. From our earlier example, every package that matches `/npm/space/*` also matches `/npm/*`, but the reverse is not true,
which makes `/npm/space/*` the more specific pattern because it is a proper subset of `/npm/*`. Because one group is a subset of another
group, it creates a hierarchy, in which `/npm/space/*` is a subgroup of the parent group, `/npm/*`.

Though only the most specific package group’s configuration applies to a package, that group may be configured to inherit
from its parent group’s configuration.

## Words, word boundaries, and prefix matching

Before discussing prefix matching, let's define some key terms:

- A _word_ a letter or number followed by zero or more letters, numbers, or
  mark characters (such as accents, umlauts, etc.).
- A _word boundary_ is at the end of a word, when a non-word character is reached. Non-word
  characters are punctuation characters such as `.`, `-`, and `_`.

Specifically, the regex pattern for a word is `[\p{L}\p{N}][\p{L}\p{N}\p{M}]*`, which can be broken down as follows:

- `\p{L}` represents any letter.
- `\p{N}` represents any number.
- `\p{M}` represents any mark character, such as accents, umlauts, etc.

Therefore, `[\p{L}\p{N}]` represents a number or letter, and `[\p{L}\p{N}\p{M}]*`
represents zero or more letters, numbers, or mark characters and a word boundary is at the end of each match of this regex pattern.

###### Note

Word boundary matching is based on this definition of a “word”. It is not based on words defined in a dictionary, or CameCase. For example,
there is no word boundary in `oneword` or `OneWord`.

Now that word and word boundary are defined, we can use them to describe prefix matching in CodeArtifact. To indicate a
prefix match on a word boundary, a match character (`~`) is used after a word character.
For example, the pattern `/npm/space/foo~` matches the package paths `/npm/space/foo` and
`/npm/space/foo-bar`, but not `/npm/space/food` or
`/npm/space/foot`.

A wildcard (`*`) is required to be used instead of `~`
when following a non-word character, such as in the pattern `/npm/*`.

## Case sensitivity

Package group definitions are case sensitive, which means that patterns that differ only by case
can exist as separate package groups. For example, a user can create separate package groups with
the patterns `/npm//AsyncStorage$`, `/npm//asyncStorage$`, and `/npm//asyncstorage$`
for the three separate packages that exist on the npm Public Registry:
_AsyncStorage_, _asyncStorage_, _asyncstorage_ that differ only by case.

While case matters, CodeArtifact still associates packages to a package group if the package has a variation of the
pattern that differs by case. If a user creates the `/npm//AsyncStorage$` package group without creating the
other two groups shown above, then all case variations of the name _AsyncStorage_, including _asyncStorage_ and
_asyncstorage_, will be associated with the package group.
But, as described in the next section, [Strong and weak match](#package-group-strong-and-weak-match "#package-group-strong-and-weak-match"), these
variations will be handled differently than _AsyncStorage_, which exactly matches the pattern.

## Strong and weak match

The information in the previous section, [Case sensitivity](#package-group-case-sensitivity "#package-group-case-sensitivity"), states that package groups
are case sensitive, and then goes on to explain they are case insensitive.
This is because package group definitions in CodeArtifact have a concept of strong match (or exact match) and a weak match (or variation match).
A strong match is when the package matches the pattern exactly, without any variation. A weak match is
when the package matches a variation of the pattern, such as different letter case. Weak match behavior
prevents packages that are variations of a package group’s pattern from rolling up to a more general package
group. When a package is a variation (weak match) of the most specific matching group’s pattern, then the
package is associated with the group but the package is blocked instead of applying the group’s origin control
configuration, preventing any new versions of the package from being pulled from upstreams or published.
This behavior reduces the risk of supply chain attacks resulting from dependency confusion of packages with nearly
identical names.

To illustrate weak match behavior, suppose package group `/npm/*` allows ingestion and blocks
publishing. A more specific package group, `/npm//anycompany-spicy-client$`,
is configured to block ingestion and allow publish. The package named _anycompany-spicy-client_ is a strong match
of the package group, which allows package versions to be published and blocks ingestion of package versions. The only
casing of the package name that is allowed to be published is _anycompany-spicy-client_, since it is a strong match for
the package definition pattern. A different case variation, such as _AnyCompany-spicy-client_ is blocked from
publishing because it is a weak match. More importantly, the package group blocks ingestion
of all case variations, not just the lowercase name used in the pattern, reducing the risk of a dependency confusion attack.

## Additional variations

In addition to case differences, weak matching also ignores differences in sequences of dash `-`, dot `.`,
underscore `_`, and confusable characters (such as similar looking characters from separate alphabets). During normalization used for weak matching, CodeArtifact performs
casefolding (similar to converting to lowercase), replaces sequences of dash, dot, and underscore characters with a single dot,
and normalizes confusable characters.

Weak matching treats dashes, dots, and underscores as equivalent but does not completely ignore them. This means that _foo-bar_,
_foo.bar_, _foo..bar_, and _foo_bar_ are all weak match equivalents, but
_foobar_ is not. Although several public repositories implement steps to prevent these types of varations, the
protection provided by public repositories does not make this feature of package groups unnecessary. For example,
public repositories such as the npm Public Registry registry will only prevent new variations of the package named
_my-package_ if _my-package_ is already published to it. If _my-package_ is an
internal package and package group `/npm//my-package$` is created that allows publish and blocks ingestion, you likely don't want to
publish _my-package_ to the npm Public Registry in order to prevent a variant such as _my.package_ from being allowed.

While some package formats such as Maven treat these characters differently (Maven treats `.` as a namespace hierarchy separator
but not `-` or `_`), something like _com.act-on_ could still be confused with _com.act.on_.

###### Note

Note that whenever multiple variations are associated with a package group, an administrator may create a new package group for a specific variation
to configure different behavior for that variation.
