# Run a Monte Carlo simulation on Deadline Cloud

The
[monte\_carlo\_simulation](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/monte_carlo_simulation "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/monte_carlo_simulation")
job bundle prices a portfolio of autocallable structured notes using Monte
Carlo simulation with QuantLib's Heston stochastic volatility model. The
job is a Deadline Cloud port of the
[Pricing
Financial Derivatives with AWS Batch](https://ec2spotworkshops.com/monte-carlo-with-batch.html "https://ec2spotworkshops.com/monte-carlo-with-batch.html") workshop.

The bundle defines a two-step pipeline:

1. `PricePositions`: One task per portfolio position.
   Tasks are grouped into chunks that calibrate the Heston model once and
   price all positions in the chunk, amortizing calibration cost.
2. `AggregateResults`: Collects per-position results into
   a portfolio summary.
   The bundle uses the Open Job Description
   [TASK\_CHUNKING](https://github.com/OpenJobDescription/openjd-specifications/blob/mainline/rfcs/0001-task-chunking.md "https://github.com/OpenJobDescription/openjd-specifications/blob/mainline/rfcs/0001-task-chunking.md")
   extension for load balancing. The scheduler starts by dispatching individual
   positions, observes how long they take, and then automatically grows the
   chunk size to match a target runtime. Fast positions are grouped into
   larger chunks; slow positions stay in small chunks to keep work spread
   across the fleet.

To run this bundle, you need a queue with a conda queue environment
that includes the `conda-forge` channel for
`quantlib-python`. When you deploy the
[starter
farm template](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/starter_farm "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/starter_farm"), set the `ProdCondaChannels` parameter to
`deadline-cloud conda-forge`.

Submit the bundle with the GUI submitter:

```
deadline bundle gui-submit monte_carlo_simulation/
```

Or submit a quick test with fewer positions:

```
deadline bundle submit monte_carlo_simulation/ \
  -p PositionRange="0-1" -p NumPaths=100
```
