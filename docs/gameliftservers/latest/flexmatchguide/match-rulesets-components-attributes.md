

# Declare player attributes
<a name="match-rulesets-components-attributes"></a>

In this section, list individual player attributes to include in matchmaking requests. There are two reasons you might declare player attributes in a rule set: 
+ When the rule set contains rules that rely on player attributes.
+ When you want to pass a player attribute to the game session through the match request. For example, you might want to pass player character choices to the game session before each player connects. 

When declaring a player attribute, include the following information: 
+ *name* (required) – This value must be unique to the rule set.
+ *type* (required) – The data type of the attribute value. Valid data types are number, string, string list, or string map.
+ *default* (optional) – Enter a default value to use if a matchmaking request doesn't provide an attribute value. If no default is declared and a request doesn't include a value, FlexMatch can't fulfill the request. An empty string is treated as not providing a default.