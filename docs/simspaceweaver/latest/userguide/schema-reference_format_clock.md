End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Clock

The `clock` section (required) specifies the properties of the simulation clock.

```
clock:
  tick_rate: `tick-rate`

```

**Properties**

`tick_rate`

Specifies the number of ticks per second that the clock publishes to apps.

_Required:_ Yes

_Type:_

- _Version `1.14` and `1.15`:_ String
- _Version `1.13` and `1.12`:_ Integer

_Valid values:_

- _Version `1.14` and `1.15`:_ `"10"` | `"15"` | `"30"` | `"unlimited"`
  - `"unlimited"`: the clock sends the next tick as soon as all apps finish
    their commit operations for the current tick.

- _Version `1.13` and `1.12`:_ `10` | `15` | `30`
