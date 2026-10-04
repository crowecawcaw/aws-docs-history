

# Typed routine result contracts
<a name="rd-routine-results"></a>

 `run_routine` differs from the read commands in one respect: two different ABS pump-cycle tests can complete with the same UDS success code and mean different things — cycles completed as expected, cycles short of expected, or a marginal deviation the operator should track. The transport layer cannot see this; the guidance encodes it at the payload layer as a **per-routine result schema** plus a **verdict**.

## Per-routine result schema
<a name="rd-result-schema"></a>

Each remotely invocable routine has an entry in a schema registry that declares:
+ A **version** number, for wire-compatible evolution.
+ A **fields** list — the flat set of primitives (scalars, or 1-level arrays of scalars) the routine’s `result` dict is required to contain, each with a name, type, unit, and short description.
+ A **verdict function** — a pure function that maps a valid `result` dict to one of `in_spec`, `marginal`, or `out_of_spec`. Missing fields default to `in_spec` (a defensive default, not a crash path).
+ A **renderer hint** — advisory metadata the operator UI uses to select a rendering surface (table, key-value grid, list). Not enforcement; the operator UI is free to render more richly.

The schemas are colocated with the routine catalog so a routine cannot ship a schema without a catalog entry; an import-time guard fails the build if the two disagree.

## Verdict on the wire
<a name="rd-verdict-wire"></a>

A successful `run_routine` response carries a typed `result` and the verdict computed from it:

```
{
  "correlation_id": "…",
  "status": "SUCCEEDED",
  "routine_id": "evap_leak_test",
  "result": {
    "system_pressure_kpa": 3.4,
    "leak_rate_ccm": 0.8
  },
  "verdict": "marginal",
  "latency_ms": 5200
}
```

The verdict is computed by the sidecar (or the sim producer, in the deterministic testing path) and written into the payload before publish. The operator UI reads `response.verdict` directly and does not recompute — recomputation on the client is explicitly disallowed, because the verdict is a safety-shaped output and the wire value is the audit record.

Verdict bands and renderer patterns are stable across routines: `in_spec` renders green, `marginal` renders amber, `out_of_spec` renders red, and the underlying result values render alongside the verdict so an operator can see *why* the classification was made rather than only *what* it was.

## Pilot routines
<a name="rd-result-pilot"></a>

The v1 pilot covers six routines chosen to exercise five distinct rendering patterns and both ICE and EV powertrain surfaces:


|  `routine_id`  | Renderer hint | What is measured | 
| --- | --- | --- | 
|  `lamp_self_check`  |  `list`  | Per-lamp verdict array (ok / dim / flicker / open\_circuit / short) plus ambient light reading. | 
|  `o2_heater_check`  |  `kv_grid`  | Bank-1 upstream O2 sensor heater response time vs manufacturer threshold. | 
|  `evap_leak_test`  |  `kv_grid`  | EVAP system pressure and measured fuel-vapour leak rate. | 
|  `abs_pump_cycle`  |  `kv_grid`  | Observed vs expected ABS pump cycle count. | 
|  `pack_isolation_test`  |  `kv_grid`  | HV traction-battery isolation resistance vs manufacturer minimum. | 
|  `cell_balance_check`  |  `table`  | Per-cell voltage array plus derived maximum inter-cell delta. | 

Additional routines register their own schema entries as they ship. A routine without a registered schema falls back to a raw-JSON renderer with no verdict banner, so unimplemented routines degrade legibly rather than crash the operator surface.