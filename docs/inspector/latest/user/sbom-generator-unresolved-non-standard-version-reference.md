# Handling unresolved or non-standard version references in the Amazon Inspector SBOM Generator

The Amazon Inspector SBOM Generator locates and parses supported artifacts within a system by identifying dependencies directly from source files.
It's not a package manager and does not resolve version ranges, infer versions based on dynamic references, or handle registry lookups.
It collects dependencies only as they're defined in project source artifacts.
In many cases, dependencies in package manifests, such as `package.json`, `pom.xml`, or `requirements.txt`, are specified using unresolved or range-based versions.
This topic includes examples of how these dependencies might look.

## Recommendations

The Amazon Inspector SBOM Generator extracts dependencies from source artifacts, but doesn't resolve or interpret version ranges or dynamic references.
For more accurate vulnerability scanning and SBOMs, we recommend using resolved, semantic version identifiers in project dependencies.

## Java

For Java, Maven projects can use version ranges to define dependencies in the `pom.xml` file.

```

<dependency>
    <groupId>org.inspector</groupId>
    <artifactId>inspector-api</artifactId>
    <version>(,1.0]</version>
</dependency>

```

The range specifies that any version up to and including 1.0 is acceptable.
However, if a version is not a resolved version, the Amazon Inspector SBOM Generator won't collect it because it cannot be mapped to a specific release.

## JavaScript

For JavaScript, the `package.json` file can include version ranges that resemble the following:

```

"dependencies": {
    "ky": "^1.2.0",
    "registry-auth-token": "^5.0.2",
    "registry-url": "^6.0.1",
    "semver": "^7.6.0"
}

```

The `^` operator specifies that any version greater than or equal to the specified version is acceptable.
However, if the specified version is not a resolved version, the Amazon Inspector SBOM Generator won't collect it becaue doing so can lead to false positives during vulnerability detection.

## Python

For Python, the `requirements.txt` file can include entries with a boolean expression.

```
requests>=1.0.0
```

The `>=` operator specifies that any version greater than or equal to `1.0.0` is acceptable.
Because this particular expression doesn't specify an exact version, the Amazon Inspector SBOM Generator cannot reliably collect a version for vulnerability analysis.

The Amazon Inspector SBOM Generator doesn't support non-standard or ambiguous version identifiers, such as beta, latest, or snapshot.

```
pkg:maven/org.example.com/testmaven@1.0.2%20Beta-RC-1_Release
```

###### Note

The use of a non-standard suffix, such as Beta-RC-1_Release, isn't compliant with standard semantic versioning and cannot be assessed for vulnerabilities within the Amazon Inspector detection engine.
