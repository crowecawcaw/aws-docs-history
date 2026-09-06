# Classify satellite imagery in parallel on Deadline Cloud

The
[satellite\_classification](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/satellite_classification "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/satellite_classification")
job bundle on the GitHub website classifies satellite image tiles into land-cover categories
(water, vegetation, bare soil, rock, cloud) and merges the results into
a single map. The classifier reads color ratios between the four
spectral bands of each tile to decide what's on the ground.

The job runs in two steps. `ClassifyTiles` fans out one
parallel task per tile that downloads the tile, classifies its pixels,
and writes a result file plus a color PNG. `MosaicResults`
runs after the parallel step finishes and merges every tile into one
map plus an overview image with class percentages. This fan-out and
merge pattern applies to any workload where input files are
independent.

The bundle ships with five sample tiles simulating the Grand
Canyon area. They're downloaded automatically from the Deadline Cloud samples
CDN when the job runs — no external data or accounts
needed.

The bundle requires a farm with a conda queue environment that has
`conda-forge` in the channel list (the classifier uses the
`rasterio` package). The quickest setup is the
[starter
farm AWS CloudFormation (CloudFormation) template](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/starter_farm "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/starter_farm") on the GitHub website. Set its
`ProdCondaChannels` parameter to
`deadline-cloud conda-forge`.

Submit with the sample tiles:

```
deadline bundle submit job_bundles/satellite_classification/
```

To classify your own tiles, point `TilesDir` at a local
directory of 4-band `.tif` files:

```
deadline bundle submit job_bundles/satellite_classification/ \
  -p TilesDir=`path-to-tiles`
```
