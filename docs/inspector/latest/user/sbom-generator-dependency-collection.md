

# Programming language dependency collection
<a name="sbom-generator-dependency-collection"></a>

 The Amazon Inspector SBOM Generator supports different programming languages and frameworks, which make up a robust and detailed collection of dependencies. Generating an SBOM helps you understand the composition of your software, so you can identify vulnerabilities and maintain compliance with security standards. The Amazon Inspector SBOM Generator supports the following programming languages and file formats. 

## Go dependency scanning
<a name="w2aac39c25b5"></a>


| Programming language | Package manager | Supported artifacts | Toolchain support | Development dependencies | Transitive dependencies | Private flag | Recursively | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| Go | Go | `go.mod`<br />`go.sum`<br />`Go Binaries`<br />`GOMODCACHE` | N/A<br />N/A<br />Yes<br />N/A | N/A<br />N/A<br />N/A<br />N/A | N/A<br />N/A<br />N/A<br />N/A | N/A<br />N/A<br />N/A<br />N/A | Yes<br />Yes<br />Yes<br />No | 

### go.mod/go.sum
<a name="w2aac39c25b5b5"></a>

 Use `go.mod` and `go.sum` files to define and lock dependencies in Go projects. The Amazon Inspector SBOM Generator manages these files differently based on the Go toolchain version. 

**Key features**
+  Collects dependencies from `go.mod` (if the Go toolchain version is 1.17 or higher) 
+  Collects dependencies from `go.sum` (if the Go toolchain version is 1.17 or lower) 
+  Parses `go.mod` to identify all declared dependencies and dependency versions 

**Example `go.mod` file**  
 The following is an example of `go.mod` file. 

```
module example.com/project

go 1.17

require (
github.com/gin-gonic/gin v1.7.2
golang.org/x/crypto v0.0.0-20210616213533-5cf6c0f8e123
)
```

**Example `go.sum` file**  
 The following is an example of `go.sum` file. 

```
github.com/gin-gonic/gin v1.7.2 h1:VZ7DdRl0sghbA6lVGSkX+UXO2+J0aH7RbsNugG+FA8Q=
github.com/gin-gonic/gin v1.7.2/go.mod h1:ILZ1Ngh2f1pL1ASUj7gGk8lGFeNC8cRTaN2ZhsBNbXU=
golang.org/x/crypto v0.0.0-20210616213533-5cf6c0f8e123 h1:b6rCu+qHze+BUsmC3CZzH8aNu8LzPZTVsNTo64OypSc=
golang.org/x/crypto v0.0.0-20210616213533-5cf6c0f8e123/go.mod h1:K5Dkpb0Q4ewZW/EzWlQphgJcUMBCzoWrLfDOVzpTGVQ=
```

**Note**  
 Each of these files produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

### Go Binaries
<a name="w2aac39c25b5b7"></a>

 The Amazon Inspector SBOM Generator extracts dependencies from compiled Go binaries to provide assurance about the code in use. 

**Note**  
 The Amazon Inspector SBOM Generator supports capturing and evaluating toolchain versions from Go binaries built using the official Go compiler. For more information, see [Download and install](https://go.dev/doc/install) on the Go website. If you are using the Go toolchain from another vendor, such as Red Hat, evaluation might not be accurate due to potential differences in distribution and metadata availability. 

**Key features**
+  Extracts dependency information directly from Go binaries 
+  Collects dependencies embedded within the binary 
+  Detects and extracts the Go toolchain version used for compiling the binary. 

### GOMODCACHE
<a name="w2aac39c25b5b9"></a>

 The Amazon Inspector SBOM Generator scans the Go module cache to collect information about installed dependencies. This cache stores downloaded modules to make sure the same versions are used across different builds. 

**Key features**
+  Scans the `GOMODCACHE` directory to identify cached modules 
+  Extracts detailed metadata, including module names, versions, and source URLs 

**Example structure**  
 The following is an example of the `GOMODCACHE` structure. 

```
~/go/pkg/mod/
├── github.com/gin-gonic/gin@v1.7.2
├── golang.org/x/crypto@v0.0.0-20210616213533-5cf6c0f8e123
```

**Note**  
 This structure produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

## Java dependency scanning
<a name="w2aac39c25b7"></a>


| Programming language | Package manager | Supported artifacts | Toolchain support | Development dependencies | Transitive dependencies | Private flag | Recursively | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| Java | Maven | Compiled Java applications (.jar/.war/.ear)<br />`pom.xml` | N/A<br />N/A | N/A<br />N/A | Yes<br />Yes | N/A<br />N/A | Yes<br />Yes | 

**Note**  
 Our vulnerability evaluation feature only supports Maven Central repository. Third-party repositories, such as JBoss Enterprise Maven Repository, are not currently supported. 

 The Amazon Inspector SBOM Generator performs Java dependency scanning by analyzing compiled Java applications and `pom.xml` files. When scanning compiled applications, the scanner generates SHA–1 hashes for integrity verification, extracts embedded `pom.properties` files, and parses nested `pom.xml` files. 

### SHA–1 hash collection (for compiled .jar, .war, .ear files)
<a name="w2aac39c25b7b9"></a>

 The Amazon Inspector SBOM Generator tries to collect SHA–1 hashes for all `.ear`, `.jar`, and `.war` files in a project to guarantee the integrity and traceability of compiled Java artifacts. 

**Key features**
+  Generates SHA–1 hashes for all compiled Java artifacts 

**Example artifact**  
 The following is an example of an SHA–1 artifact. 

```
{
  "bom-ref": "comp-52",
  "type": "library",
  "name": "jul-to-slf4j",
  "version": "2.0.6",
  "hashes": [
    {
      "alg": "SHA-1",
      "content": ""
    }
  ],
  "purl": "pkg:maven/jul-to-slf4j@2.0.6",
  "properties": [
    {
      "name": "amazon:inspector:sbom_generator:source_path",
      "value": "test-0.0.1-SNAPSHOT.jar/BOOT-INF/lib/jul-to-slf4j-2.0.6.jar"
    }
  ]
}
```

**Note**  
 This artifact produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

### pom.properties
<a name="w2aac39c25b7c11"></a>

 The `pom.properties` file is used in Maven projects to store project metadata, including package names and package versions. The Amazon Inspector SBOM Generator parses this file to collect project information. 

**Key features**
+  Parses and extracts package artifacts, package groups, and package versions 

**Example `pom.properties` file**  
 The following is an example of a `pom.properties` file. 

```
#Generated by Maven
#Tue Mar 16 15:44:02 UTC 2021

version=1.6.0
groupId=net.datafaker
artifactId=datafaker
```

**Note**  
 This file produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

**Excluding nested `pom.xml` parsing**  
 If you want to exclude `pom.xml` parsing when scanning compiled Java applications, use the `--skip-nested-pomxml` argument. 

### pom.xml
<a name="w2aac39c25b7c13"></a>

 The `pom.xml` file is the core configuration file for Maven projects. It contains information about projects and project dependencies. The Amazon Inspector SBOM Generator parses pom.xml files to collect dependencies, scanning standalone files in repositories and files inside compiled .jar files. 

**Key features**
+  Parses and extracts package artifacts, package groups, and package versions from `pom.xml` files. 

**Supported Maven scopes and tags**  
 Dependencies are collected with the following Maven scopes: 
+  compile 
+  provided 
+  runtime 
+  test 
+  system 
+  import 

 Dependencies are collected with the following Maven tag: `<optional>true</optional>`. 

**Example `pom.xml` file with a scope**  
 The following is an example of a `pom.xml` file with a scope. 

```
<dependency>
<groupId>jakarta.servlet</groupId>
<artifactId>jakarta.servlet-api</artifactId>
</version>6.0.0</version>
<scope>provided</scope>
</dependency>
<dependency>
<groupId>mysql</groupId>
<artifactId>mysql-connector-java</artifactId>
<version>8.0.28</version>
<scope>runtime</scope>
</dependency>
```

**Example `pom.xml` file without a scope**  
 The following is an example of a `pom.xml` file without a scope. 

```
<dependency>
<groupId>com.fasterxml.jackson.core</groupId>
<artifactId>jackson-databind</artifactId>
<version>2.17.1</version>
</dependency>

<dependency>
<groupId>org.jenkins-ci.plugins</groupId>
<artifactId>plain-credentials</artifactId>
<version>183.va_de8f1dd5a_2b_</version>
</dependency>

<dependency>
<groupId>org.jenkins-ci.plugins</groupId>
<artifactId>jackson2-api</artifactId>
<version>2.15.2-350.v0c2f3f8fc595</version>
</dependency>
```

**Note**  
 Each of these files produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

## JavaScript dependency scanning
<a name="w2aac39c25b9"></a>


| Programming language | Package manager | Supported artifacts | Toolchain support | Development dependencies | Transitive dependencies | Private flag | Recursively | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| Javascript | `Node Modules`<br />`NPM`<br />`PNPM`<br />`YARN` | `node_modules/*/package.json`<br />`package-lock.json (v1, v2, and v3) / npm-shrinkwrap.json`<br />`pnpm-lock.yaml`<br />`yarn.lock` | N/A<br />N/A<br />N/A<br />N/A | N/A<br />Yes<br />Yes<br />Yes | Yes<br />N/A<br />N/A<br />N/A | Yes<br />N/A<br />N/A<br />N/A | Yes<br />No<br />No<br />No | 

### package.json
<a name="w2aac39c25b9b5"></a>

 The `package.json` file is a core component of Node.js projects. It contains metadata about installed packages. The Amazon Inspector SBOM Generator scans this file to identify package names and package versions. 

**Key features**
+  Parses the JSON file structure to extract package names and versions 
+  Identifies private packages with private values 

**Example `package.json` file**  
 The following is an example of a `package.json` file. 

```
{
"name": "arrify",
"private": true,
"version": "2.0.1",
"description": "Convert a value to an array",
"license": "MIT",
"repository": "sindresorhus/arrify"
}
```

**Note**  
 This file produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

### package-lock.json
<a name="w2aac39c25b9b7"></a>

 The `package-lock.json` file is automatically generated by npm to lock exact versions of dependencies installed for a project. It ensures consistency in environments by storing exact versions of all dependencies and their sub-dependencies. This file can distinguish between regular dependencies and development dependencies. 

**Key features**
+  Parses the JSON file structure to extract package names and package versions 
+  Supports dev dependency detection 

**Example `package-lock.json` file**  
 The following is an example of a `package-lock.json` file. 

```
"verror": {
"version": "1.10.0",
"resolved": "https://registry.npmjs.org/verror/-/verror-1.10.0.tgz",
"integrity": "sha1-OhBcoXBTr1XW4nDB+CiGguGNpAA=",
"requires": {
    "assert-plus": "^1.0.0",
    "core-util-is": "1.0.2",
    "extsprintf": "^1.2.0"
}
},
"wrappy": {
"version": "1.0.2",
"resolved": "https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz",
"integrity": "sha1-tSQ9jz7BqjXxNkYFvA0QNuMKtp8=",
"dev": true
},
"yallist": {
"version": "3.0.2",
"resolved": "https://registry.npmjs.org/yallist/-/yallist-3.0.2.tgz",
"integrity": "sha1-hFK0u36Dx8GI2AQcGoN8dz1ti7k="
}
```

**Note**  
 This file produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

### npm-shrinkwrap.json
<a name="w2aac39c25b9b9"></a>

 npm automatically generates`package-lock.json` and `npm-shrinkwrap.json` files to lock exact versions of dependencies installed for a project. This guarantees consistency in environments by storing exact versions of all dependencies and sub-dependencies. The files distinguish between regular dependencies and development dependencies. 

**Key features**
+  Parse `package-lock` versions 1 ,2, and 3 of the JSON file structure to extract the package name and version 
+  Developer dependency detection is supported (`package-lock.json` captures production and development dependencies, allowing tools to identify which packages are used in development environments) 
+  The `npm-shrinkwrap.json` file is prioritized over the `package-lock.json` file 

**Example**  
 The following is an example of a `package-lock.json` file. 

```
"verror": {
            "version": "1.10.0",
            "resolved": "https://registry.npmjs.org/verror/-/verror-1.10.0.tgz",
            "integrity": "sha1-OhBcoXBTr1XW4nDB+CiGguGNpAA=",
            "requires": {
                "assert-plus": "^1.0.0",
                "core-util-is": "1.0.2",
                "extsprintf": "^1.2.0"
            }
        },
        "wrappy": {
            "version": "1.0.2",
            "resolved": "https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz",
            "integrity": "sha1-tSQ9jz7BqjXxNkYFvA0QNuMKtp8=",
            "dev": true
        },
        "yallist": {
            "version": "3.0.2",
            "resolved": "https://registry.npmjs.org/yallist/-/yallist-3.0.2.tgz",
            "integrity": "sha1-hFK0u36Dx8GI2AQcGoN8dz1ti7k="
}
```

### pnpm-yaml.lock
<a name="w2aac39c25b9c11"></a>

 The `pnpm-lock.yaml` file is generated by pnpm to maintain a record of installed dependency versions. It also tracks development dependencies separately. 

**Key features**
+  Parses the YAML file structure to extract package names and versions 
+  Supports dev dependency detection 

**Example**  
 The following is an example of a `pnpm-lock.yaml` file. 

```
lockfileVersion: 5.3
importers:
my-project:
dependencies:
  lodash: 4.17.21
devDependencies:
  jest: 26.6.3
specifiers:
  lodash: ^4.17.21
  jest: ^26.6.3
packages:
/lodash/4.17.21:
resolution:
  integrity: sha512-xyz
engines:
  node: '>=6'
dev: false
/jest/26.6.3:
resolution:
  integrity: sha512-xyz
dev: true
```

**Note**  
 This file produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

### yarn.lock
<a name="w2aac39c25b9c13"></a>

 The Amazon Inspector SBOM Generator tries to collect SHA–1 hashes for `.ear`, `.jar`, and `.war` files in a project to guarantee the integrity and traceability of compiled Java artifacts. 

**Key features**
+  Generates SHA–1 hashes for all compiled Java artifacts 

**Example SHA–1 artifact**  
 The following is an example of an SHA–1 artifact. 

```
"@ampproject/remapping@npm:^2.2.0":
version: 2.2.0
resolution: "@ampproject/remapping@npm:2.2.0"
dependencies:
"@jridgewell/gen-mapping": ^0.1.0
"@jridgewell/trace-mapping": ^0.3.9
checksum: d74d170d06468913921d72430259424b7e4c826b5a7d39ff839a29d547efb97dc577caa8ba3fb5cf023624e9af9d09651afc3d4112a45e2050328abc9b3a2292
languageName: node
linkType: hard

"@babel/code-frame@npm:^7.0.0, @babel/code-frame@npm:^7.12.13, @babel/code-frame@npm:^7.18.6, @babel/code-frame@npm:^7.21.4":
version: 7.21.4
resolution: "@babel/code-frame@npm:7.21.4"
dependencies:
"@babel/highlight": ^7.18.6
checksum: e5390e6ec1ac58dcef01d4f18eaf1fd2f1325528661ff6d4a5de8979588b9f5a8e852a54a91b923846f7a5c681b217f0a45c2524eb9560553160cd963b7d592c
languageName: node
linkType: hard
```

**Note**  
 This artifact produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

## .NET dependency scanning
<a name="w2aac39c25c11"></a>


| Programming language | Package manager | Supported artifacts | Toolchain support | Development dependencies | Transitive dependencies | Private flag | Recursively | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| .NET | `.NET Core`<br />`Nuget`<br />`Nuget`<br />`.NET` | `*.deps.json`<br />`Packages.config`<br />`packages.lock.json`<br />`.csproj` | N/A<br />N/A<br />N/A<br />N/A | N/A<br />N/A<br />N/A<br />N/A | N/A<br />N/A<br />Yes<br />N/A | N/A<br />N/A<br />N/A<br />N/A | Yes<br />Yes<br />Yes<br />Yes | 

### Packages.config
<a name="w2aac39c25c11b5"></a>

 The `Packages.config` file is an XML file used by an older version of Nuget to manage project dependencies. It lists all the packages referenced by the project, including specific versions. 

**Key features**
+  Parses XML structure to extract package IDs and versions 

**Example**  
 The following is an example of a `Packages.config` file. 

```
<?xml version="1.0" encoding="utf-8"? >
<packages>
<package id="FluentAssertions" version="5.4.1" targetFramework="net461" />
<package id="Newtonsoft.Json" version="11.0.2" targetFramework="net461" />
<package id="SpecFlow" version="2.4.0" targetFramework="net461" />
<package id="SpecRun.Runner" version="1.8.0" targetFramework="net461" />
<package id="SpecRun.SpecFlow" version="1.8.0" targetFramework="net461" />
<package id="SpecRun.SpecFlow.2-4-0" version="1.8.0" targetFramework="net461" />
<package id="System.ValueTuple" version="4.5.0" targetFramework="net461" />
</packages>
```

**Note**  
 This file produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

### \*.deps.json
<a name="w2aac39c25c11b7"></a>

 The `*.deps.json` file is generated by .NET Core projects and contains detailed information about all dependencies, including paths, versions, and runtime dependencies. This file makes sure the runtime has necessary information to load correct versions of dependencies. 

**Key features**
+ Parses the JSON structure for comprehensive dependency details
+  Extracts package names and versions in a `libraries` list. 

**Example `.deps.json` file**  
 The following is an example of a `.deps.json` file. 

```
{
"runtimeTarget": {
    "name": ".NETCoreApp,Version=v7.0",
    "signature": ""
},
"libraries": {
    "sample-Nuget/1.0.0": {
        "type": "project",
        "serviceable": false,
        "sha512": ""
    },
    "Microsoft.EntityFrameworkCore/7.0.5": {
        "type": "package",
        "serviceable": true,
        "sha512": "sha512-RXbRLHHWP2Z3pq8qcL5nQ6LPeoOyp8hasM5bd0Te8PiQi3RjWQR4tcbdY5XMqQ+oTO9wA8/RLhZRn/hnxlTDnQ==",
        "path": "microsoft.entityframeworkcore/7.0.5",
        "hashPath": "microsoft.entityframeworkcore.7.0.5.nupkg.sha512"
    },
}
```

**Note**  
 This file produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

### packages.lock.json
<a name="w2aac39c25c11b9"></a>

 The `packages.lock.json` file is used by newer versions of Nuget to lock exact versions of dependencies for a .NET project to guarantee the same versions are used consistently across different environments. 

**Key features**
+ Parses the JSON structure to list locked dependencies
+ Supports both direct and transitive dependencies
+ Extracts package name and resolved versions

**Example `packages.lock.json` file**  
 The following is an example of a `packages.lock.json` file. 

```
{
"version": 1,
"dependencies": {
"net7.0": {
  "Microsoft.EntityFrameworkCore": {
    "type": "Direct",
    "requested": "[7.0.5, )",
    "resolved": "7.0.5",
    "contentHash": "RXbRLHHWP2Z3pq8qcL5nQ6LPeoOyp8hasM5bd0Te8PiQi3RjWQR4tcbdY5XMqQ+oTO9wA8/RLhZRn/hnxlTDnQ==",
    "dependencies": {
      "Microsoft.EntityFrameworkCore.Abstractions": "7.0.5",
      "Microsoft.EntityFrameworkCore.Analyzers": "7.0.5",
      "Microsoft.Extensions.Caching.Memory": "7.0.0",
      "Microsoft.Extensions.DependencyInjection": "7.0.0",
      "Microsoft.Extensions.Logging": "7.0.0"
    }
  },
  "Newtonsoft.Json": {
    "type": "Direct",
    "requested": "[13.0.3, )",
    "resolved": "13.0.3",
    "contentHash": "HrC5BXdl00IP9zeV+0Z848QWPAoCr9P3bDEZguI+gkLcBKAOxix/tLEAAHC+UvDNPv4a2d18lOReHMOagPa+zQ=="
  },
  "Microsoft.Extensions.Primitives": {
    "type": "Transitive",
    "resolved": "7.0.0",
    "contentHash": "um1KU5kxcRp3CNuI8o/GrZtD4AIOXDk+RLsytjZ9QPok3ttLUelLKpilVPuaFT3TFjOhSibUAso0odbOaCDj3Q=="
  }
}
}
}
```

**Note**  
 This file produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

### .csproj
<a name="w2aac39c25c11c11"></a>

 The `.csproj` file is written in XML and the project file for .NET projects. It includes references to Nuget packages, project properties, and build configurations. 

**Key features**
+  Parses XML the structure to extract package references 

**Example `.csproj` file**  
 The following is an example of a `.csproj` file. 

```
<Project Sdk="Microsoft.NET.Sdk">
<PropertyGroup>
<TargetFramework>net7.0</TargetFramework>
<RootNamespace>sample_Nuget</RootNamespace>
<ImplicitUsings>enable</ImplicitUsings>
<Nullable>enable</Nullable>
<RestorePackagesWithLockFile>true</RestorePackagesWithLockFile>
</PropertyGroup>
<ItemGroup>
</ItemGroup>
<ItemGroup>
<PackageReference Include="Newtonsoft.Json" Version="13.0.3" />
<PackageReference Include="Microsoft.EntityFrameworkCore" Version="7.0.5" />
</ItemGroup>
</Project>
```

**Example `.csproj` file**  
 The following is an example of a `.csproj` file. 

```
<PackageReference Include="ExamplePackage" Version="6.*" />
<PackageReferencePackageReference Include="ExamplePackage" Version="(4.1.3,)" />
<PackageReference Include="ExamplePackage" Version="(,5.0)" />
<PackageReference Include="ExamplePackage" Version="[1,3)" />
<PackageReference Include="ExamplePackage" Version="[1.3.2,1.5)" />
```

**Note**  
 Each of these files produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

## PHP dependency scanning
<a name="w2aac39c25c13"></a>


| Programming language | Package manager | Supported artifacts | Toolchain support | Development dependencies | Transitive dependencies | Private flag | Recursively | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| PHP | Composer | `composer.lock`<br />`/vendor/composer/installed.json` | N/A<br />N/A | N/A<br />N/A | Yes<br />Yes | N/A<br />N/A | Yes<br />Yes | 

### composer.lock
<a name="w2aac39c25c13b5"></a>

 The `composer.lock` file is automatically generated when running the composer install or composer update commands. This file guarantees the same versions of dependencies are installed in every environment. This provides a consistent and reliable build process. 

**Key features**
+  Parses the JSON format for structured data 
+  Extracts dependency names and versions 

**Example `composer.lock` file**  
 The following is an example of a `composer.lock` file. 

```
{
"packages": [
    {
        "name": "nesbot/carbon",
        "version": "2.53.1",
        // TRUNCATED
    },
    {
        "name": "symfony/deprecation-contracts",
        "version": "v3.2.1",
        // TRUNCATED
    },
    {
        "name": "symfony/polyfill-mbstring",
        "version": "v1.27.0",
        // TRUNCATED
    }
]
// TRUNCATED
}
```

**Note**  
 This produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

### /vendor/composer/installed.json
<a name="w2aac39c25c13b7"></a>

 The `/vendor/composer/installed.json` file is located in the `vendor/composer` directory and provides a comprehensive list of all installed packages and package versions. 

**Key features**
+  Parses the JSON format for structured data 
+  Extracts dependency names and version 

**Example `/vendor/composer/installed.json` file**  
 The following is an example of a `/vendor/composer/installed.json` file. 

```
 
{
"packages": [
    {
        "name": "nesbot/carbon",
        "version": "2.53.1",
        // TRUNCATED
    },
    {
        "name": "symfony/deprecation-contracts",
        "version": "v3.2.1",
        // TRUNCATED
    },
    {
        "name": "symfony/polyfill-mbstring",
        "version": "v1.27.0",
        // TRUNCATED
    }
]
// TRUNCATED
}
```

**Note**  
 This file produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

## Python dependency scanning
<a name="w2aac39c25c15"></a>


| Programming language | Package manager | Supported artifacts | Toolchain support | Development dependencies | Transitive dependencies | Private flag | Recursively | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| Python | `pip`<br />`Poetry`<br />`Pipenv`<br />`uv`<br />`Egg/Wheel` | `requirements.txt`<br />`Poetry.lock`<br />`Pipfile.lock`<br />`uv.lock`<br />`.egg-info/PKG-INFO`<br />`.dist-info/METADATA` | N/A<br />N/A<br />N/A<br />N/A<br />N/A<br />N/A | N/A<br />N/A<br />N/A<br />Yes<br />N/A<br />N/A | N/A<br />N/A<br />N/A<br />N/A<br />N/A<br />N/A | N/A<br />N/A<br />N/A<br />N/A<br />N/A<br />N/A | Yes<br />Yes<br />Yes<br />Yes<br />Yes<br />Yes | 

### requirements.txt
<a name="w2aac39c25c15b5"></a>

 The `requirements.txt` file is a widely used format in Python projects to specify project dependencies. Each line in this file includes a package with its version constraints. The Amazon Inspector SBOM Generator parses this file to identify and catalog dependencies accurately. 

**Key features**
+  Supports version specifiers (== and ˜=) 
+  Supports comments and complex dependency lines 

**Note**  
 The version specifiers <= and => aren't supported. 

**Example `requirements.txt` file**  
 The following is an example of a `requirements.txt` file. 

```
flask==1.1.2
requests==2.24.0
numpy==1.18.5
foo~=1.2.0
# Comment about a dependency
scipy. # invalid
```

**Note**  
 This file produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

### Pipfile.lock
<a name="w2aac39c25c15b9"></a>

 Pipenv is a tool bringing the best of all packaging worlds (bundled, pinned, and unpinned). The `Pipfile.lock` locks exact versions of dependencies to facilitate deterministic builds. The Amazon Inspector SBOM Generator reads this file to list dependencies and their resolved versions. 

**Key features**
+  Parses the JSON format for dependency resolution 
+  Supports default and development dependencies 

**Example `Pipfile.lock` file**  
 The following is an example of a `Pipfile.lock` file. 

```
{
"default": {
    "requests": {
        "version": "==2.24.0",
        "hashes": [
            "sha256:cc718bb187e53b8d"
        ]
    }
},
"develop": {
    "blinker": {
        "hashes": [
            "sha256:1779309f71bf239144b9399d06ae925637cf6634cf6bd131104184531bf67c01",
            "sha256:8f77b09d3bf7c795e969e9486f39c2c5e9c39d4ee07424be2bc594ece9642d83"
        ],
        "markers": "python_version >= '3.8'",
        "version": "==1.8.2"
    }
}
}
```

**Note**  
 This file produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

### Poetry.lock
<a name="w2aac39c25c15c11"></a>

 Poetry is a dependency management and packaging tool for Python. The `Poetry.lock` file locks exact versions of dependencies to facilitate consistent environments. The Amazon Inspector SBOM Generator extracts detailed dependency information from this file. 

**Key features**
+  Parses the TOML format for structured data 
+  Extracts dependency names, and versions 

**Example `Poetry.lock` file**  
 The following is an example of a `Poetry.lock` file. 

```
[[package]]
name = "flask"
version = "1.1.2"
description = "A simple framework for building complex web applications."
category = "main"
optional = false
python-versions = ">=3.5"
[[package]]
name = "requests"
version = "2.24.0"
description = "Python HTTP for Humans."
category = "main"
optional = false
python-versions = ">=3.5"
```

**Note**  
 This file produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

### uv.lock
<a name="w2aac39c25c15c13"></a>

 uv is a fast Python package manager written in Rust. The `uv.lock` file locks exact versions of dependencies to facilitate consistent environments. The Amazon Inspector SBOM Generator extracts detailed dependency information from this file. 

**Key features**
+  Parses the TOML formatted `uv.lock` for structured data 
+  Extracts dependency names, and versions 
+  Supports development dependencies 
+  Collects only packages where the source is a registry 

**Example `uv.lock` file**  
 The following is an example of a `uv.lock` file. 

```
version = 1
requires-python = ">=3.12"

[[package]]
name = "flask"
version = "3.1.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "blinker" },
    { name = "click" },
    { name = "itsdangerous" },
    { name = "jinja2" },
    { name = "markupsafe" },
    { name = "werkzeug" },
]

[[package]]
name = "pytest"
version = "8.3.4"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "iniconfig" },
    { name = "packaging" },
    { name = "pluggy" },
]

[package.dev-dependencies]
dev = [
    { name = "pytest" },
]
```

**Note**  
 This file produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

### Egg/Wheel
<a name="w2aac39c25c15c15"></a>

 For globally installed Python packages, the Amazon Inspector SBOM Generator supports parsing metadata files found in the `.egg-info/PKG-INFO` and `.dist-info/METADATA` directories. These files provide detailed metadata about installed packages. 

**Key features**
+  Extracts package name, and version 
+  Supports both egg and wheel formats 

**Expanded default scan paths (Sbomgen 1.13.0 and later)**  
 In Amazon Inspector SBOM Generator release 1.13.0 and later, the scanner's default localhost scan paths were expanded to include user-level `pip` installs (`pip install --user`) and installs produced by the `uv tool install` command. This enables detection of Python packages that are installed outside system-wide `site-packages`, including frameworks and tools such as CrewAI, Aider, GPT Engineer, and Open Interpreter, whose recommended install methods produce installs in these locations (for example, `uv tool install crewai`).   
 Added default scan paths:   
 Linux – `/home/*/.local/lib/python*/site-packages/`, `/home/*/.local/share/uv/tools/*/lib/python*/site-packages/` (with `/root/` equivalents for containers running as root). 
 Windows – `%APPDATA%\Python\Python*\Lib\site-packages\`, `%LOCALAPPDATA%\uv\tools\*\Lib\site-packages\`. 
 For non-default Python install prefixes on any platform, use the `--path` argument to point the scanner at the install location. 

**Example `PKG-INFO/METADATA` file**  
 The following is an example of a `PKG-INFO/METADATA` file. 

```
Metadata-Version: 1.2
Name: Flask
Version: 1.1.2
Summary: A simple framework for building complex web applications.
Home-page: https://palletsprojects.com/p/flask/
```

**Note**  
 This file produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

## Ruby dependency scanning
<a name="w2aac39c25c17"></a>


| Programming language | Package manager | Supported artifacts | Toolchaing support | Development dependencies | Transitive dependencies | Private flag | Recursively | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| Ruby | Bundler | `Gemfile.lock`<br />`.gemspec`<br />`globall installed Gems` | N/A<br />N/A<br />N/A | N/A<br />N/A<br />N/A | Yes<br />N/A<br />N/A | N/A<br />N/A<br />N/A | Yes<br />Yes<br />Yes | 

### Gemfile.lock
<a name="w2aac39c25c17b5"></a>

 The `Gemfile.lock` file locks exact versions of all dependencies to make sure the same versions are used in every environment. 

**Key features**
+  Parses the `Gemfile.lock` file to identity dependencies and dependency versions 
+  Extracts detailed package names and package versions 

**Example `Gemfile.lock` file**  
 The following is an example of a `Gemfile.lock` file. 

```
GEM
remote: https://rubygems.org/
specs:
ast (2.4.2)
awesome_print (1.9.2)
diff-lcs (1.5.0)
json (2.6.3)
parallel (1.22.1)
parser (3.2.2.0)
nokogiri (1.16.6-aarch64-linux)
```

**Note**  
 This file produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

### .gemspec
<a name="w2aac39c25c17b7"></a>

 The `.gemspec` file is a RubyGem file containing metadata about a gem. The Amazon Inspector SBOM Generator parses this file to collect detailed information about a gem. 

**Key features**
+  Parses and extracts the gem name and gem version 

**Note**  
 Reference specification is not supported. 

**Example `.gemspec` file**  
 The following is an example of a `.gemspec` file. 

```
Gem::Specification.new do |s|
s.name        = "generategem"
s.version     = "2.0.0"
s.date        = "2020-06-12"
s.summary     = "generategem"
s.description = "A Gemspec Builder"
s.email       = "edersondeveloper@gmail.com"
s.files       = ["lib/generategem.rb"]
s.homepage    = "https://github.com/edersonferreira/generategem"
s.license     = "MIT"
s.executables = ["generategem"]
s.add_dependency('colorize', '~> 0.8.1')
end
```

```
# Not supported 

Gem::Specification.new do |s|
s.name        = &class1
s.version     = &foo.bar.version
```

**Note**  
 This file produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

### Globally installed gems
<a name="w2aac39c25c17b9"></a>

 The Amazon Inspector SBOM Generator supports scanning globally installed gems, which are located in standard directories, such as `/usr/local/lib/ruby/gems/<ruby_version>/gems/` in Amazon EC2/Amazon ECR and `ruby/gems/<ruby_version>/gems/` in Lambda. This makes sure all globally installed dependencies are identified and cataloged. 

**Key features**
+  Identifies and scans all globally installed gems in standard directories 
+  Extracts metadata and version information for each globally installed gem 

**Example directory structure**  
 The following is an example of a directory structure. 

```
. 
└── /usr/local/lib/ruby/3.5.0/gems/ 
├── actrivesupport-6.1.4 
├── concurrent-ruby-1.1.9 
└── i18n-1.8.10
```

**Note**  
 This structure produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

## Rust dependency scanning
<a name="w2aac39c25c19"></a>


| Programming language | Package manager | Supported artifacts | Toolchain support | Development dependencies | Transitive dependencies | Private flag | Recursively | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| Rust | Cargo.toml | `Cargo.toml`<br />`Cargo.lock`<br /> `Rust binary (built with cargo-auditable)` | N/A<br />N/A<br />Yes | N/A<br />N/A<br />N/A | N/A<br />Yes<br />N/A | N/A<br />N/A<br />N/A | Yes<br />Yes<br />Yes | 

### Cargo.toml
<a name="w2aac39c25c19b5"></a>

 The `Cargo.toml` file is the manifest file for Rust projects. 

**Key features**
+  Parses and extracts the `Cargo.toml` file to identify the project package name and version. 

**Example `Cargo.toml` file**  
 The following is an example of a `Cargo.toml` file. 

```
[package]
name = "wait-timeout"
version = "0.2.0"
description = "A crate to wait on a child process with a timeout specified across Unix and\nWindows platforms.\n"
homepage = "https://github.com/alexcrichton/wait-timeout"
documentation = "https://docs.rs/wait-timeout"
readme = "README.md"
categories = ["os"]
license = "MIT/Apache-2.0"
repository = "https://github.com/alexcrichton/wait-timeout"
[target."cfg(unix)".dependencies.libc]
version = "0.2"
[badges.appveyor]
repository = "alexcrichton/wait-timeout"
```

**Note**  
 This file produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

### Cargo.lock
<a name="w2aac39c25c19b7"></a>

 The `Cargo.lock` file locks dependency versions to make sure the same versions are used whenever a project is built. 

**Key features**
+  Parses the `Cargo.lock` file to identify all dependencies and dependency versions. 

**Example `Cargo.lock` file**  
 The following is an example of a `Cargo.lock` file. 

```
# This file is automatically @generated by Cargo.
# It is not intended for manual editing.
[[package]]
name = "adler32"
version = "1.0.3"
source = "registry+https://github.com/rust-lang/crates.io-index"

[[package]]
name = "aho-corasick"
version = "0.7.4"
source = "registry+https://github.com/rust-lang/crates.io-index"
```

**Note**  
 This file produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

### Rust binaries with cargo-auditable
<a name="w2aac39c25c19b9"></a>

 The Amazon Inspector SBOM Generator collects dependencies from Rust binaries built with the `cargo-auditable` library. This provides additional dependency information by enabling dependency extraction from compiled binaries. 

**Key features**
+  Extracts dependency information directly from Rust binaries built with the `cargo-auditable` library 
+  Retrieves metadata and version information for dependencies included in the binaries 

**Note**  
 This file produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

## Swift dependency scanning
<a name="w2aac39c25c21"></a>


| Programming language | Package manager | Supported artifacts | Toolchain support | Development dependencies | Transitive dependencies | Private flag | Recursively | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| Swift | Swift Package Manager | `Package.resolved (v1, v2, and v3)` | N/A | N/A | N/A | N/A | Yes | 

### Package.resolved
<a name="w2aac39c25c21b5"></a>

 The `Package.resolved` file is generated by Swift Package Manager to lock exact versions of dependencies for a Swift project. The Amazon Inspector SBOM Generator parses this file to collect dependency names, versions, and source repository information. Schema versions 1, 2, and 3 of the `Package.resolved` format are supported. 

**Note**  
 The Amazon Inspector SBOM Generator does not generate the `Package.resolved` file. If your project does not already contain a `Package.resolved` file, you must generate it before scanning by running `swift package resolve` in your project directory. 

**Supported artifacts**
+  `Package.resolved` (schema version 1) 
+  `Package.resolved` (schema version 2) 
+  `Package.resolved` (schema version 3) 

**Key features**
+  Extracts dependency names and locked versions from pinned packages 
+  Derives the package namespace from the source repository URL (for example, `github.com/Alamofire`) 
+  Skips branch-only pins that don't have a resolved version 
+  Filters out local source control and file system dependencies 
+  Excludes `Package.resolved` files inside `.build/` directories to prevent collecting dependencies from the Swift Package Manager build cache 

**Note**  
 The `Package.resolved` file is platform-independent. The Amazon Inspector SBOM Generator discovers this file recursively on Linux, macOS, and Windows. 

**Example `Package.resolved` file (v2)**  
 The following is an example of a version 2 `Package.resolved` file. 

```
{
  "pins" : [
    {
      "identity" : "alamofire",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/Alamofire/Alamofire.git",
      "state" : {
        "revision" : "a1b2c3...",
        "version" : "5.8.1"
      }
    },
    {
      "identity" : "swift-argument-parser",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-argument-parser.git",
      "state" : {
        "revision" : "d4e5f6...",
        "version" : "1.3.0"
      }
    }
  ],
  "version" : 2
}
```

**Example `Package.resolved` file (v1)**  
 The following is an example of a version 1 `Package.resolved` file. 

```
{
  "object": {
    "pins": [
      {
        "package": "Alamofire",
        "repositoryURL": "https://github.com/Alamofire/Alamofire.git",
        "state": {
          "branch": null,
          "revision": "a1b2c3...",
          "version": "5.8.1"
        }
      }
    ]
  },
  "version": 1
}
```

**Example PURL**  
 The following is an example package URL for a Swift Package Manager dependency. 

```
pkg:swift/github.com/Alamofire/Alamofire@5.8.1
```

**Note**  
 Each of these files produces an output that contains a package URL. This URL can be used to specify information about software packages when generating a software bill of materials and can be included in the [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_inspector-scan_ScanSbom.html) API. For more information, see [package-url](https://github.com/package-url/purl-spec) on the GitHub Website. 

## Unsupported artifacts
<a name="w2aac39c25c23"></a>

 This section describes unsupported artifacts. 

### Java
<a name="w2aac39c25c23b5"></a>

 The Amazon Inspector SBOM Generator generator only supports vulnerability detection for dependencies sourced from [the mainstream Maven repository](https://repo1.maven.org/maven2). Private or custom Maven repositories, such as Red Hat Maven and Jenkins, aren't supported. For accurate vulnerability detection, make sure Java dependencies are pulled from the mainstream Maven repository. Dependencies from other repositories won't be covered in vulnerability scans. 

### JavaScript
<a name="w2aac39c25c23b7"></a>

**esbuild bundles**  
 For esbuild minified bundles, the Amazon Inspector SBOM Generator doesn't support dependency scanning for projects using esbuild. Source maps generated by esbuild don't include sufficient metadata(dependency names and versions) required for accurate Sbomgen generation. For reliable results, scan the original project files, such as the `node_modules/directory` and `package-lock.json`, prior to the bundling process. 

**package.json**  
 The Amazon Inspector SBOM Generator doesn't support scanning the root-level package.json file for dependency information. This file only specifies package names and version ranges, but doesn't include fully resolved package versions. For accurate scanning results, use `package.json` or other lock files, such as `yarn.lock` and `pnpm.lock`, that include resolved versions. 

### Dotnet
<a name="w2aac39c25c23b9"></a>

 When using floating versions or version ranges in `PackageReference`, it becomes more challenging to determine the exact package version used in a project without performing package resolution. Floating versions and version ranges allow developers to specify a range of acceptable package versions rather than a fixed version. 

### Go binaries
<a name="w2aac39c25c23c11"></a>

 The Amazon Inspector SBOM Generator doesn't scan Go binaries that are built with build flags configured to exclude the build ID. These build flags prevent Amazon Inspector SBOM Generator from accurately mapping the binary to its original source. Unclear Go binaries aren't supported due to the inability to extract package information. For accurate dependency scanning, make sure that Go binaries are built with default settings, including the build ID. 

### Rust binaries
<a name="w2aac39c25c23c13"></a>

 The Amazon Inspector SBOM Generator only scans Rust binaries if the binaries are built using [the cargo-auditable library](https://github.com/rust-secure-code/cargo-auditable). Rust binaries not utilizing this library lack necessary metadata for accurate dependency extraction. The Amazon Inspector SBOM Generator extract the compiled Rust toolchain version starting from Rust 1.7.3, but only for binaries in a Linux environment. For comprehensive scanning, build Rust binaries on Linux using cargo-auditable. 

**Note**  
 Vulnerability detection for the Rust toolchain itself isn't supported, even if the toolchain version is extracted. 