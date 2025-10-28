# Set rules for player matching

Create a set of rule statements that evaluate players for acceptance in to a match.
Rules might set requirements that apply to individual players, teams, or an entire
match. When Amazon GameLift Servers processes a match request, it starts with the oldest player in the
pool of available players and builds a match around that player. For detailed help on
creating FlexMatch rules, see [FlexMatch rule types](match-rules-reference-ruletype.md "match-rules-reference-ruletype.md").

- _name_ (required) – A meaningful name
  that uniquely identifies the rule within a rule set. Rule names are also
  referenced in event logs and metrics that track activity related to this rule.
- _description_ (optional) – Use this
  element to attach a free-form text description.
- _type_ (required) – The type element
  identifies the operation to use when processing the rule. Each rule type
  requires a set of additional properties. See a list of valid rule types and
  properties in [FlexMatch rules language](match-rules-reference.md "match-rules-reference.md").
- Rule type property (may be required) – Depending on the type of rule
  defined, you may need to set certain rule properties. Learn more about
  properties and how to use the FlexMatch property expression language in [FlexMatch rules language](match-rules-reference.md "match-rules-reference.md").
