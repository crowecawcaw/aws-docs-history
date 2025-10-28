# Use CodeArtifact with deps.edn

You use `deps.edn` with `clj` to manage dependencies for Clojure projects. This section shows how to configure `deps.edn` to use a CodeArtifact repository.

###### Topics

- [Fetch dependencies](#fetching-dependencies-deps "#fetching-dependencies-deps")
- [Publish artifacts](#publishing-artifacts-deps "#publishing-artifacts-deps")

## Fetch dependencies

To configure `Clojure` to fetch dependencies from a CodeArtifact repository, you must
edit the Maven configuration file, `settings.xml`.

1. In `settings.xml`, add a `<servers>` section with a reference to the `CODEARTIFACT_AUTH_TOKEN` environment variable so that Clojure passes the token in HTTP requests.

###### Note

Clojure expects the settings.xml file to be located at `~/.m2/settings.xml`. If elsewhere, create the file in this location.

```
<settings>
...
    <servers>
        <server>
            <id>codeartifact</id>
            <username>aws</username>
            <password>${env.CODEARTIFACT_AUTH_TOKEN}</password>
        </server>
    </servers>
...
</settings>
```

2. If you do not have one already, generate a POM xml for your project using `clj -Spom`.
3. In your `deps.edn` configuration file, add a repository matching the server id from Maven `settings.xml`.

```
:mvn/repos {
  "clojars" nil
  "central" nil
  "codeartifact" {:url "https://my_domain-111122223333.d.codeartifact.us-west-2.amazonaws.com/maven/my_repo/"}
}
```

###### Note

    * `tools.deps` guarantees that the `central` and `clojars` repositories will be checked first for Maven libraries. Afterward, the other repositories listed in `deps.edn` will be checked.
    * To prevent downloading from Clojars and Maven Central directly, `central` and `clojars` need to be set to `nil`.

Make sure you have the CodeArtifact Auth token in an environment variable (see [Pass an auth token using an environment variable](tokens-authentication.md#env-var "tokens-authentication.md#env-var")). When building the package after these changes, dependencies in `deps.edn` will be fetched from CodeArtifact.

###### Note

To use a dualstack endpoint, use the `codeartifact.`region`.on.aws` endpoint.

## Publish artifacts

1. Update your Maven settings and `deps.edn` to include CodeArtifact as a maven-recognized server (see [Fetch dependencies](#fetching-dependencies-deps "#fetching-dependencies-deps")). You can use a tool such as [deps-deploy](https://github.com/slipset/deps-deploy "https://github.com/slipset/deps-deploy") to upload artifacts to CodeArtifact.
2. In your `build.clj`, add a `deploy` task to upload required artifacts to the previously setup `codeartifact` repository.

```
(ns build
(:require [deps-deploy.deps-deploy :as dd]))

(defn deploy [_]
  (dd/deploy {:installer :remote
          :artifact "PATH_TO_JAR_FILE.jar"
          :pom-file "pom.xml" ;; pom containing artifact coordinates
          :repository "codeartifact"}))
```

3. Publish the artifact by running the command: `clj -T:build deploy`

For more information on modifying default repositories, see [Modifying the default repositories](https://clojure.org/reference/deps_and_cli#_modifying_the_default_repositories "https://clojure.org/reference/deps_and_cli#_modifying_the_default_repositories") in the _Clojure Deps and CLI Reference Rationale_.
