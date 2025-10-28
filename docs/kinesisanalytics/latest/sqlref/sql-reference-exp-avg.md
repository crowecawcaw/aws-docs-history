# EXP_AVG

```
EXP_AVG ( expression, <time-interval> )
```

EXP_AVG returns an exponentially-weighted average
([exponential moving average](https://en.wikipedia.org/wiki/Moving_average "https://en.wikipedia.org/wiki/Moving_average")) of a
stream of value expressions selected in a specified time window. EXP_AVG divides the specified
window into intervals based on the value of <time-interval>. The values of the specified
expression are weighted the most heavily for the most recent time-intervals and exponentially
less heavily for earlier intervals.

## Example

This example creates an exponentially-weighted average of the price of each stock ticker
over a 30-second window such that the prices (for that ticker symbol) in the most recent
10-second subwindow carry double the weight of the prices in the middle 10-second subwindow
and four times the weight of the prices in the oldest 10-second subwindow.

```
select stream t.rowtime, ticker, price,
exp_avg(price, INTERVAL '10' SECOND) over w as avgPrice
from t
window w as (partition by ticker range interval '30' second preceding);
```

In this example, 10 seconds is the half-life of the decay function, that is, the period over
which the weights applied to the prices being averaged decrease by a factor of two. In other
words, the older one will be given half as much weight as the newer one. It is specified as the
time_interval in the call to EXP_AVG as interval '10' second .
