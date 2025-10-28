End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Workers

The `workers` section (required) specifies configurations for _worker groups_ (groups of workers). SimSpace Weaver
uses this information together with `placement_constraints` to configure the
underlying infrastructure of your simulation. Only 1 worker group is currently supported.

To specify the properties for a worker group, replace
`worker-group-name` with a name of your choice. The
name must be 3-64 characters long and can contain the characters **A** -**Z** , **a** -**z** , **0** -**9** , and **\_ -** (hyphen). Specify the properties of the worker group
after the name.

```
workers:
  `worker-group-name`:
    type: "sim.c5.24xlarge"
    desired: `number-of-workers`

```

**Properties**

`type`

Specifies worker type.

_Required:_ Yes

_Type:_ String

_Valid values:_ `sim.c5.24xlarge`

`desired`

Specifies the desired number of workers for this worker group.

_Required:_ Yes

_Type:_ Integer

_Valid values:_ `1`-`3`. Your service quota (limit)
for the number of workers for your simulations determines the maximum value of this property.
For example, if your service quota is `2` then the maximum value for this
property is `2`. You can request an increase to your service quota. For more
information, see [SimSpace Weaver endpoints and quotas](service-quotas.md "service-quotas.md").
