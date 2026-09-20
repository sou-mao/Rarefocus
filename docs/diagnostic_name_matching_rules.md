# Prespecified diagnostic name-matching rules

1. Each method's candidate diagnoses and their order were fixed before the reference diagnosis was made available to the matching evaluator.
2. Up to five candidate disease names were presented in their frozen order. The evaluator could identify a matching position but could not add, remove or reorder candidates.
3. The standard-diagnosis field contained a candidate-blind expansion of the reference diagnosis using its canonical disease name and unambiguous exact synonyms.
4. The evaluator returned the position of the highest-ranked matching candidate. It returned `No` when no candidate matched the standard diagnosis.
5. A returned candidate position was mapped back to that candidate's explicit diagnostic rank. When explicitly tied candidates shared a rank, a match to any member of the tied group received that shared rank.
6. An unmatched result was treated as not recalled. Recall@k was counted as correct when the matched explicit rank was no greater than k.
7. The same model version, prompt and matching procedure were applied to all compared methods and evaluation datasets.
