

# Build a scoreboard headline from the game state without a model
<a name="functions-examples-passthrough-gamestate"></a>

A passthrough function that turns the tracked game state into a display string and a clutch-time flag, refreshed every 5 seconds. Requires an enabled event clipping output that is mapped to a sports data source, so that `media.clip.eventState` is populated. For more information, see [Aligning clips to plays with Sports Data](create-feed-outputs.md#event-clip-sports-data).

The request expression reads the game phase that the data source reports and does the arithmetic. The response expression formats the result. For the phase values, see [Fields in `media.clip`](functions-context.md#functions-context-clip). Set `$regulationPeriods` to the number of regulation periods in the game: 4 for quarters, 2 for halves.

**Target**

```
{ "passthrough": {} }
```

**Request expression**

```
(
  $state := media.clip.eventState;
  $regulationPeriods := 4;

  /* Seconds left in the period, from an "M:SS" count-down clock. Unset for any other clock. */
  $remaining := $state.clock != null and $contains($state.clock, /^[0-9]+:[0-9]{2}$/)
    ? (
        $parts := $split($state.clock, ":");
        $number($parts[0]) * 60 + $number($parts[1])
      );

  /* Unset unless both scores are reported. */
  $margin := $state.homeScore != null and $state.awayScore != null
    ? $abs($state.homeScore - $state.awayScore);

  {
    "phase": $state.phase != null ? $state.phase : "PRE_GAME",
    "period": $state.period,
    "clock": $state.clock,
    "homeScore": $state.homeScore,
    "awayScore": $state.awayScore,
    "margin": $margin,
    "isClutch": ($state.phase = "IN_PROGRESS" or $state.phase = "OVERTIME")
                and $state.period != null and $state.period >= $regulationPeriods
                and $margin != null and $margin <= 5
                and $remaining != null and $remaining <= 120
  }
)
```

**Important**  
Test a value with `!= null` before you compare it with `<`, `>`, `<=`, or `>=`. A relational comparison against `null` is an error that fails the run, so the window produces no metadata. `$exists()` is not enough on its own, because it returns `true` for a value that is present and `null`. `!= null` is `false` both for a missing value and for `null`, so it covers both. Equality operators are safe with `null`. Here the test guards the values that can be missing: the period, `$remaining`, which is unset when the clock is missing or isn't in `M:SS` form, and `$margin`, which is unset when a score is missing.

**Response expression**

```
(
  $score := $string(homeScore) & "-" & $string(awayScore);
  {
    "phase": phase,
    "isClutch": isClutch,
    "headline": phase = "PRE_GAME" ? "Coming up next."
      : phase = "FINAL" ? "Final: " & $score
      : phase = "INTERMISSION" or phase = "END_OF_REGULATION" ? "End of period " & $string(period) & ": " & $score
      : isClutch ? "Clutch time: " & $score & ", " & clock & " to go"
      : "P" & $string(period) & " " & clock & " - " & $score
  }
)
```

**Function output**. A fixed-interval trigger runs in every window, including a window with no clip, so the headline stays current between plays.

```
{
  "name": "scoreboard",
  "status": "ENABLED",
  "outputConfig": {
    "function": {
      "functionArn": "arn:aws:elemental-inference:us-west-2:111122223333:function/{{function-id}}",
      "trigger": { "fixedInterval": { "intervalSeconds": 5 } },
      "clippingSettings": { "outputName": "game-clips" }
    }
  }
}
```

**Results** for four different game states.


| `media.clip.eventState` | Stored value | 
| --- | --- | 
| phase "PRE\_GAME", or absent | {"phase":"PRE\_GAME","isClutch":false,"headline":"Coming up next."} | 
| homeScore 54, awayScore 48, period 3, clock "05:30", phase "IN\_PROGRESS" | {"phase":"IN\_PROGRESS","isClutch":false,"headline":"P3 05:30 - 54-48"} | 
| homeScore 98, awayScore 97, period 4, clock "00:45", phase "IN\_PROGRESS" | {"phase":"IN\_PROGRESS","isClutch":true,"headline":"Clutch time: 98-97, 00:45 to go"} | 
| homeScore 101, awayScore 101, period 4, clock "00:00", phase "END\_OF\_REGULATION" | {"phase":"END\_OF\_REGULATION","isClutch":false,"headline":"End of period 4: 101-101"} | 