# Forecast lock

You can use the forecast lock feature to lock specific periods in your forecast to prevent any further edits or adjustments. To configure the forecast lock,
enter a number between zero and time horizon -1 in the Demand Plan settings page to lock the first _x_ forecast period. The default value is 0, indicating no periods are locked.

The forecast lock is not applied to the initial forecast but will take effect from the second demand planning cycle carrying over the finalized values from the previous demand plan. In the Demand Plan,
locked periods are indicated by a _lock_ icon. The change history icon will display the reason code _PLAN_LOCKED_ for audit purpose at the most granular level. Once the forecast period is locked,
the lock applies to all products within that timeframe.

When the forecast granularity is changed, forecast overrides from the prior planning cycles are not carried over to the current planning cycle.
The prior forecast and accuracy metrics will also not display any data in the Demand plan and any prior forecast locks are no longer valid. It takes
two consecutive forecast executions in the modified granularity to apply a new forecast lock. You can unlock forecast periods by setting the configuration to zero and starting a new forecast.

The example below displays how intra-cycle forecast refresh scheduler works (when it's disabled) with forecast lock in the following settings:

- Demand plan granularity – Weekly
- Forecast horizon selected – 5
- intra-cycle forecast refresh schedule – Disabled
- Final forecast publish – 7th day of the week
- Lock period – 2

![Displays intra-cycle forecast refresh scheduler works (when it's disabled) with forecast lock](images/intra-cycle_with_forecast_lock.png)
The example below displays how intra-cycle forecast refresh scheduler works (when it's enabled) with forecast lock in the following settings:

- Demand plan granularity – Weekly
- Forecast horizon selected – 5
- intra-cycle forecast refresh schedule – Enabled
- Final forecast publish – 7th day of the week
- Interim forecast publish – 3rd day of the week
- Lock period – 2

![Displays intra-cycle forecast refresh scheduler works (when it's enabled) with forecast lock](images/forecast_intracycle.png)
