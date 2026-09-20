# RareFocus

Reproducibility materials for **RareFocus: An Extensible Multi-Agent Framework for Rare Disease Diagnosis via Progressive Retrieval and Focused Differential Reasoning**.

## Diagnosis-name matching

This starter repository contains the frozen diagnosis-name matching materials used in the reported evaluation:

- `prompts/diagnosis_name_matching_prompt.json`: the exact system prompt, instruction and prompt-construction rule;
- `evaluation/diagnosis_name_matching.py`: prompt construction and response parsing;
- `docs/diagnostic_name_matching_rules.md`: the prespecified matching and rank-mapping rules.

The evaluator used `gpt-4o-2024-08-06` with a fixed seed of 42. Candidate diagnoses were fixed before the reference diagnosis was supplied to the evaluator.

## Release status

This is a repository starter for preparing the manuscript-associated release. The manuscript-aligned diagnostic workflow, analysis scripts, runtime environment, dependencies, licence and full reproduction instructions will be added and frozen before submission.
