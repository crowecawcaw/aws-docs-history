# AWS Glue Scala ObjectNode APIs

###### Topics

- [ObjectNode object](#glue-etl-scala-apis-glue-types-objectnode-object "#glue-etl-scala-apis-glue-types-objectnode-object")
- [ObjectNode case
  class](#glue-etl-scala-apis-glue-types-objectnode-case-class "#glue-etl-scala-apis-glue-types-objectnode-case-class")
  **Package: com.amazonaws.services.glue.types**

## ObjectNode object

**ObjectNode**

```
object ObjectNode
```

### ObjectNode def methods

```
def apply( frameKeys : Set[String],
           v1 : mutable.Map[String, DynamicNode],
           v2 : mutable.Map[String, DynamicNode],
           resolveWith : String
         ) : ObjectNode
```

## ObjectNode case

class

**ObjectNode**

```
case class ObjectNode extends MapLikeNode(value)  (
           val value : mutable.Map[String, DynamicNode] )
```

### ObjectNode def methods

```
def clone
```

```
def equals( other : Any )
```

```
def hashCode : Int
```

```
def nodeType
```

```
def this
```
