

# `ALTER SYSTEM`
<a name="alter-system-syntax-support"></a>

 With `ALTER SYSTEM`, you can set or reset the subset of configuration parameters that Aurora DSQL supports at the system level. 

## Supported syntax
<a name="alter-system-supported-syntax"></a>

```
ALTER SYSTEM SET configuration_parameter { TO | = } value
ALTER SYSTEM RESET configuration_parameter
ALTER SYSTEM RESET ALL
```

## Description
<a name="alter-system-description"></a>

 `ALTER SYSTEM` persists a supported configuration parameter for the logical database that the cluster group represents. Aurora DSQL applies the change automatically across the logical database. 

 Because peered clusters present a single logical database, a system-level setting applies to connections through any cluster endpoint in the group. The setting applies only to the cluster group's logical database. 

 Transactions that are already in progress when you run `ALTER SYSTEM` continue using the system settings that were in effect when they started. Afterward, subsequent transactions use the new setting once Aurora DSQL propagates the change across the logical database. 

 You must run `ALTER SYSTEM` outside an explicit transaction block. 

 Aurora DSQL supports a managed subset of parameters at the system level, and this set can expand over time. Use `SET` for session-level parameter changes. 

 Aurora DSQL applies the change automatically, and it takes effect immediately. 

## Examples
<a name="alter-system-examples"></a>

Set a supported parameter at the system level:

```
ALTER SYSTEM SET dsql.enable_batched_nestloop = on;
```

Reset a parameter to its default value:

```
ALTER SYSTEM RESET dsql.enable_batched_nestloop;
```

Reset all system-level parameter changes:

```
ALTER SYSTEM RESET ALL;
```

## Compatibility
<a name="alter-system-compatibility"></a>

 In Aurora DSQL, `ALTER SYSTEM` sets or resets supported configuration parameters at the system level. 