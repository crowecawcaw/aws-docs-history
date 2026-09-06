# Run GROMACS molecular dynamics simulations on Deadline Cloud

The
[gromacs\_md
job bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/gromacs_md "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/gromacs_md") on the GitHub website runs a molecular dynamics simulation
pipeline from raw protein structure to analyzed trajectory with [GROMACS](https://www.gromacs.org/ "https://www.gromacs.org/") on the GROMACS website. The
pipeline runs system preparation, energy minimization, NVT/NPT
equilibration, production MD, and analysis (RMSD, RMSF, radius of
gyration, hydrogen bonds). Multiple independent replicas fan out in
parallel through the `MaxReplicaIndex` parameter.

The bundle requires a Deadline Cloud farm with a Linux x86\_64 service-managed
fleet (minimum 4 vCPU) and a conda queue environment with
`gromacs` from `conda-forge`. No host configuration
script or custom conda recipe is needed.

The bundle includes sample data for hen egg-white lysozyme
(PDB: 1AKI) and MDP parameter files under
`sample_inputs/mdp/`.

From the `job_bundles` directory, submit the job:

```
deadline bundle submit gromacs_md \
  -p "InputPdb=sample_inputs/protein.pdb" \
  -p "MdpMinimization=sample_inputs/mdp/minimization.mdp" \
  -p "MdpNvt=sample_inputs/mdp/nvt.mdp" \
  -p "MdpNpt=sample_inputs/mdp/npt.mdp" \
  -p "MdpProduction=sample_inputs/mdp/production.mdp" \
  -p "ProductionSteps=500000"
```

To run 10 independent replicas in parallel:

```
deadline bundle submit gromacs_md \
  -p "InputPdb=protein.pdb" \
  -p "MaxReplicaIndex=9" \
  -p "ProductionSteps=5000000"
```
