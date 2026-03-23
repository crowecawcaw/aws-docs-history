# FT.ALIASUPDATE

Update an existing alias to point to a different physical index. This command only affects future references to the alias. Currently in-progress operations (FT.SEARCH, FT.AGGREGATE) are unaffected by this command.

**Syntax**

```
FT.ALIASUPDATE <alias> <index>

```

**Return**

Returns a simple string OK message or an error reply.
