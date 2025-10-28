# AWS Glue Scala DynamicNode

APIs

###### Topics

- [DynamicNode class](#glue-etl-scala-apis-glue-types-dynamicnode-class "#glue-etl-scala-apis-glue-types-dynamicnode-class")
- [DynamicNode object](#glue-etl-scala-apis-glue-types-dynamicnode-object "#glue-etl-scala-apis-glue-types-dynamicnode-object")
  **Package: com.amazonaws.services.glue.types**

## DynamicNode class

**DynamicNode**

```
class DynamicNode extends Serializable with Cloneable
```

### DynamicNode def methods

```
def getValue : Any
```

Get plain value and bind to the current record:

```
def nodeType : TypeCode
```

```
def toJson : String
```

Method for debug:

```
def toRow( schema : Schema,
           options : Map[String, ResolveOption]
         ) : Row
```

```
def typeName : String
```

## DynamicNode object

**DynamicNode**

```
object DynamicNode
```

### DynamicNode def methods

```
def quote( field : String,
           useQuotes : Boolean
         ) : String
```

```
def quote( node : DynamicNode,
           useQuotes : Boolean
         ) : String
```
