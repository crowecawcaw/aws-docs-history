# Predict protein structures with ESMFold on Deadline Cloud

The
[esmfold\_predict](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/esmfold_predict "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/esmfold_predict")
job bundle on the GitHub website runs protein structure prediction with ESMFold (Meta's
`facebook/esmfold_v1`, MIT license). The bundle takes a FASTA
file as input and produces a `.pdb` file per sequence as
output, along with confidence metrics and an optional validation report
against experimental reference structures.

The job runs four steps:

1. Parse the input FASTA, validate sequences (up to 1024 amino
   acids, standard residues plus X), and split records across worker
   tasks.
2. Run ESMFold inference on each batch of sequences on
   GPU.
3. Render a backbone trace image of each predicted structure,
   colored by per-residue pLDDT confidence.
4. Optional: when you supply a directory of experimental reference
   PDBs, compute TM-score, RMSD, and a per-residue pLDDT/error
   calibration plot.
   The bundle requires a farm with an NVIDIA GPU service-managed fleet
   (A10G, L4, or A100; at least 16 GB VRAM and 16 GB system RAM) and a
   queue with a conda queue environment that consumes the
   `CondaPackages` and `CondaChannels` job
   parameters. The fastest setup is the
   [cuda\_farm](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm")
   AWS CloudFormation (CloudFormation) template on the GitHub website. Amazon Elastic Compute Cloud (Amazon EC2) GPU instances are gated
   by per-region vCPU quotas; if your fleet doesn't scale up, request an
   increase for
   _Running On-Demand G and VT instances_ in the
   Service Quotas console.

Submit the demo, which folds three short benchmark proteins
(Trp-cage variants 1L2Y and 2JOF, and villin headpiece 1VII):

```
deadline bundle submit ./job_bundles/esmfold_predict/ \
  -p InputFasta=./job_bundles/esmfold_predict/sample_inputs/demo.fasta
```

The first fold on a fresh worker downloads the 5.2 GB
`facebook/esmfold_v1` weights into
`<OutputDir>/.hf_cache/` (about three minutes on a
`g5.2xlarge`). Subsequent fold tasks in the same job reuse
the cache.

To validate predictions against experimental references, place
`<seq_id>.pdb` files in a directory and pass it as
`ReferencePdbDir`. The `Validate` step writes
`validation.csv` and a per-sequence
`calibration.png`.
