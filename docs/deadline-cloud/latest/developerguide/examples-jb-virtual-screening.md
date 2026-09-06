# Run virtual screening with AutoDock Vina on Deadline Cloud

The
[virtual\_screening\_vina job bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/virtual_screening_vina "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/virtual_screening_vina")
on the GitHub website uses
[AutoDock
Vina](https://github.com/ccsb-scripps/AutoDock-Vina "https://github.com/ccsb-scripps/AutoDock-Vina") to screen large compound libraries against a protein target.
The bundle splits a compound library into chunks and docks them in parallel
across a fleet of workers, then aggregates and ranks the results by binding
affinity.

The pipeline runs four steps:

1. **PrepareReceptor** — Converts
   the protein PDB to PDBQT format with Open Babel.
2. **SplitLibrary** — Splits the
   SDF compound library into N chunks.
3. **DockCompounds** — Runs N
   parallel docking tasks (one per chunk). Each task is idempotent and
   safe for Spot preemption.
4. **ScoreAndRank** — Aggregates
   all chunk results into a ranked CSV of top hits.
   The bundle requires a Linux x86\_64 service-managed fleet (Spot
   recommended), a conda queue environment with `openbabel` from
   `conda-forge`, and AutoDock Vina. Install Vina by building the
   [Build an AutoDock Vina conda package for Deadline Cloud](examples-conda-autodock-vina.md "examples-conda-autodock-vina.md") conda recipe into your S3
   channel, or by installing the binary through a fleet host configuration
   script.

Set `CompoundLibrary=chembl` (default) to automatically
download and filter drug-like molecules from
[ChEMBL](https://www.ebi.ac.uk/chembl/ "https://www.ebi.ac.uk/chembl/") on the EMBL-EBI
website, or provide your own SDF file.

From the `job_bundles` directory, submit the job:

```
deadline bundle submit virtual_screening_vina \
  -p "ReceptorPdb=receptor.pdb" \
  -p "CompoundLibrary=chembl" \
  -p "MaxCompounds=100000" \
  -p "CompoundsPerChunk=100" \
  -p "CenterX=-10.7" \
  -p "CenterY=12.4" \
  -p "CenterZ=68.8"
```

For details on building the AutoDock Vina conda package, see
[Build an AutoDock Vina conda package for Deadline Cloud](examples-conda-autodock-vina.md "examples-conda-autodock-vina.md").
