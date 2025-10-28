# AWS Glue Scala ResolveSpec APIs

###### Topics

- [ResolveSpec object](#glue-etl-scala-apis-glue-resolvespec-object "#glue-etl-scala-apis-glue-resolvespec-object")
- [ResolveSpec case
  class](#glue-etl-scala-apis-glue-resolvespec-case-class "#glue-etl-scala-apis-glue-resolvespec-case-class")
  **Package: com.amazonaws.services.glue**

## ResolveSpec object

**ResolveSpec**

```
object ResolveSpec
```

### Def

```
def apply( path : String,
           action : String
         ) : ResolveSpec
```

Creates a `ResolveSpec`.

- `path` — A string representation of the choice field that needs to
  be resolved.
- `action` — A resolution action. The action can be one of the
  following: `Project`, `KeepAsStruct`, or `Cast`.

Returns the `ResolveSpec`.

### Def

```
def apply( product : Product2[String, String] ) : ResolveSpec
```

Creates a `ResolveSpec`.

- `product` — `Product2` of: source path, resolution
  action.

Returns the `ResolveSpec`.

## ResolveSpec case

class

```
case class ResolveSpec extends Product2[String, String]  (
           path : SchemaPath,
           action : String )
```

Creates a `ResolveSpec`.

- `path` — The `SchemaPath` of the choice field that needs
  to be resolved.
- `action` — A resolution action. The action can be one of the
  following: `Project`, `KeepAsStruct`, or `Cast`.

### ResolveSpec def methods

```
def _1 : String
```

```
def _2 : String
```
