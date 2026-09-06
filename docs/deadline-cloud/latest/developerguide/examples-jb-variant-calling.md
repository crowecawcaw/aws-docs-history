

# Call genetic variants with bwa and bcftools on Deadline Cloud
<a name="examples-jb-variant-calling"></a>

The [variant\_calling\_bwa](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/variant_calling_bwa) job bundle on the GitHub website finds the genetic differences between an individual and a reference genome. It aligns sequencing reads with `bwa`, calls variants with `bcftools`, and merges the results into one VCF file. The pipeline reimplements the AWS HealthOmics WDL variant-calling tutorial pipeline in Open Job Description.

The bundle demonstrates patterns that carry over to other scientific workloads:
+ Software delivered as conda packages from the bioconda channel rather than built into container images.
+ Fan-out over two different task parameters: alignment scatters over samples, and variant calling scatters over genome regions, with a merge step as the gather.
+ A job environment that verifies every required tool is on `PATH` once per session, and reports the exact packages and channels to configure if any is missing.

The bundle requires a farm with a Linux fleet, a conda queue environment with channels set to `conda-forge bioconda` in that order, and the Deadline Cloud CLI. Download the sample data (about 950 KB), then submit:

```
python sample_inputs/fetch_test_data.py
deadline bundle submit .
```

The default parameters (2 samples, 4 regions) produce 10 tasks. The README covers bringing your own cohort, scaling the region list, and the steps a production analysis would add. For other bioscience examples, see [Predict protein structures with ESMFold on Deadline Cloud](examples-jb-esmfold.md), [Run GROMACS molecular dynamics simulations on Deadline Cloud](examples-jb-gromacs.md), and [Run virtual screening with AutoDock Vina on Deadline Cloud](examples-jb-virtual-screening.md).