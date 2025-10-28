End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Clock

The `clock` section specifies properties of the simulation clock. Currently, you can
only configure the **tick rate** (the number of ticks per second
that the clock sends to apps). The tick rate is a maximum rate. The effective tick rate could
be lower because all operations (such as entity updates) for a tick must finish before the next tick
can start. The tick rate is also called the **clock rate**.

The valid values for `tick_rate` depend on the `sdk_version` specified
in your schema.

###### Valid values for the tick rate

- Versions earlier than `"1.14"`:
  - `10`

  - `15`

  - `30`

- Version `"1.14"` or later:
  - `"10"`

  - `"15"`

  - `"30"`

  - `"unlimited"`

  For more information, see [Unlimited tick rate](#working-with_configuring-simulation_clock_unlimited "#working-with_configuring-simulation_clock_unlimited").

###### Important

- For schemas with a `sdk_version` earlier than `"1.14"`
  the value of `tick_rate` is an **integer**,
  such as `30`.
- For schemas with a `sdk_version` of `"1.14"` or later,
  the value of `tick_rate` is a **string**,
  such as `"30"`. The value **must include the double quotes**.

If you convert a version `"1.12"` or `"1.13"` schema
to version `"1.14"` or later,
you must enclose the value of `tick_rate` in double quotes.

## Unlimited tick rate

You can set the `tick_rate` to `"unlimited"` to
enable your simulation to run as fast as your code can execute. With an
unlimited tick rate, SimSpace Weaver sends the next tick immediately after all
apps finish the commits for the current tick.

###### Important

Unlimited tick rate isn't supported in SimSpace Weaver versions before
1.14.0. The minimum value of `sdk_version` in the schema
is `"1.14"`.

###### Unlimited tick rate in SimSpace Weaver Local

SimSpace Weaver Local implements `"unlimited"` as if
the schema specified a tick rate of 10 kHz (10000). The effect
is the same as an unlimited tick rate in the AWS Cloud.
You still specify `tick_rate: "unlimited"` in your schema.
For more information about SimSpace Weaver Local, see
[Local development in SimSpace Weaver](working-with_local-development.md "working-with_local-development.md").

## Frequently asked

questions about the clock

### Q1. Can I change

a STARTED simulation to use a different tick rate?

You can't change the tick rate of a simulation that already exists in the AWS Cloud
at any stage of its life cycle. You also can't change the tick rate of a simulation running in
SimSpace Weaver Local. You can set the `tick_rate` in the schema and start a new
simulation from that schema.

### Q2. Can I run

my simulation with an unlimited tick rate in a version earlier than 1.14?

No, unlimited tick rate isn't supported in versions before 1.14.0.

## Troubleshooting clock errors

If your simulation fails to start, you can check the value of `"StartError"`
in the output of the **DescribeSimulation** API. An invalid
`tick_rate` value in your schema will produce the following errors.

###### Note

The error output shown here is displayed on multiple lines to improve readability.
The actual error output is a single line.

- The `sdk_version` is earlier than `"1.14"` and
  the value of `tick_rate` is an invalid integer. Valid values: `10`,
  `15`, `30`

```
"[{\"errorType\":\"SchemaFormatInvalid\",\"errorMessage\":
    \"$.clock.tick_rate: does not have a value in the enumeration [10, 15, 30]\"}]"
```

- The `sdk_version` is earlier than `"1.14"` and
  the value of `tick_rate` is a string. Valid values: `10`,
  `15`, `30`

```
"[{\"errorType\":\"SchemaFormatInvalid\",\"errorMessage\":
    \"$.clock.tick_rate: does not have a value in the enumeration [10, 15, 30]\"},
    {\"errorType\":\"SchemaFormatInvalid\",
    \"errorMessage\":\"$.clock.tick_rate: string found, integer expected\"}]"
```

- The `sdk_version` is `"1.14"` or later and
  the value of `tick_rate` is an invalid string. Valid values: `"10"`,
  `"15"`, `"30"`, `"unlimited"`

```
"[{\"errorType\":\"SchemaFormatInvalid\",\"errorMessage\":
    \"$.clock.tick_rate: does not have a value in the enumeration [10, 15, 30, unlimited]\"}]"
```

- The `sdk_version` is `"1.14"` or later and
  the value of `tick_rate` is an integer. Valid values: `"10"`,
  `"15"`, `"30"`, `"unlimited"`

```
"[{\"errorType\":\"SchemaFormatInvalid\",\"errorMessage\":
    \"$.clock.tick_rate: does not have a value in the enumeration [10, 15, 30, unlimited]\"},
    {\"errorType\":\"SchemaFormatInvalid\",
    \"errorMessage\":\"$.clock.tick_rate: integer found, string expected\"}]"
```
