# AWS Glue Scala ChoiceOption APIs

###### Topics

- [ChoiceOption trait](#glue-etl-scala-apis-glue-choiceoption-trait "#glue-etl-scala-apis-glue-choiceoption-trait")
- [ChoiceOption object](#glue-etl-scala-apis-glue-choiceoption-object "#glue-etl-scala-apis-glue-choiceoption-object")
- [Case class ChoiceOptionWithResolver](#glue-etl-scala-apis-glue-choiceoptionwithresolver-case-class "#glue-etl-scala-apis-glue-choiceoptionwithresolver-case-class")
- [Case class MatchCatalogSchemaChoiceOption](#glue-etl-scala-apis-glue-matchcatalogschemachoiceoption-case-class "#glue-etl-scala-apis-glue-matchcatalogschemachoiceoption-case-class")
  **Package: com.amazonaws.services.glue**

## ChoiceOption trait

```
trait ChoiceOption extends Serializable
```

## ChoiceOption object

**ChoiceOption**

```
object ChoiceOption
```

A general strategy to resolve choice applicable to all `ChoiceType` nodes in a
`DynamicFrame`.

- `val CAST`
- `val MAKE_COLS`
- `val MAKE_STRUCT`
- `val MATCH_CATALOG`
- `val PROJECT`

### Def apply

```
def apply(choice: String): ChoiceOption
```

## Case class ChoiceOptionWithResolver

```
case class ChoiceOptionWithResolver(name: String, choiceResolver: ChoiceResolver) extends ChoiceOption {}
```

## Case class MatchCatalogSchemaChoiceOption

```
case class MatchCatalogSchemaChoiceOption() extends ChoiceOption {}
```
