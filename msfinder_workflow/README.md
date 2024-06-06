# Galaxy Workflow Documentation: MS Finder Pipeline

This document outlines a MSFinder Galaxy workflow designed for peak annotation. The workflow consists of several steps aimed at preprocessing MS data, filtering, enhancing, and running MSFinder.

## Step 1: Data Collection and Preprocessing
Collect if the inchi and smiles are missing from the dataset, and subsequently filter out the spectra which are missing inchi and smiles.

### 1.1 MSMetaEnhancer: Collect InChi, Isomeric_smiles, and Nominal_mass
- Utilizes MSMetaEnhancer to collect InChi and Isomeric_smiles using PubChem and IDSM databases.
- Utilizes MSMetaEnhancer to collect MW using RDkit (For GOLM).

### 1.2 replace key
- replace isomeric_smiles key to smiles using replace text tool
- replace MW key to parent_mass using replace text tool (For GOLM)

### 1.3 Matchms Filtering
- Filters out invalid SMILES and InChi from the dataset using Matchms filtering.

## Step 2: Complex Removal and Subsetting Dataset
Removes coordination complexes from the dataset.

### 2.1 Remove Complexes and Subset Data
- Removes complexes from the dataset.
- Exports metadata using Matchms metadata export, cuts the SMILES column, removes complexes using Rem_Complex tool, and updates the dataset using Matchms subsetting.

## Step 3: Data Key Manipulation
Add missing metadata required by the MSFinder for annotation.

### 3.1 Matchms Remove Key
- Removes existing keys such as adduct, and ionmode from the dataset.

### 3.2 Matchms Add Key
- Adds necessary keys like ionmode, and adduct to the dataset.

### 3.3 Matchms Filtering
- Derives precursor m/z using parent mass and adduct information using matchms filtering.

### 3.4 Matchms Convert
- Converts the dataset to Riken format for compatibility with MSFinder using matchms convert.

## Step 4: Peak Annotation
### 4.1 Recetox-MSFinder
- Executes MSFinder with a 0.5 Da tolerance for both MS1 and MS2, including all element checks and an extended range for peak annotation.

## Step 5: Error Handling and Refinement
Check the MSFinder output to see if the output is the results or the log file. If the output is log file remove the smile from the dataset using matchms subsetting tool and rerun MSFinder.

### 5.1 Error Handling
- Handles errors in peak annotation by removing SMILES that are not accepted by MSFinder.
- Reruns MSFinder after error correction or with different parameter (if applicable).

## Step 6: High-res Annotation
### 6.1 High-Res Peak Overwriting
- Utilizes the Use_Theoretical_mz_Annotations tool to Overwrite experimentally measured mz values for peaks with theoretical values from peak comments.
