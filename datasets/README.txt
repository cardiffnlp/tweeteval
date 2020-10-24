=== TWEETEVAL ===

This README describes the format, file and directory structure associated with TweetEval, the benchmark associated with the Findings of EMNLP 2020 paper "TweetEval: Unified Benchmark and Comparative Evaluation for Tweet Classification".

=== DIRECTORY STRUCTURE ===

{dataset} = - train_text.txt
			- train_labels.txt
			- val_text.txt
			- val_labels.txt
			- test_text.txt

- emoji
	- {dataset}
	- mapping.txt
- emotion
	- {dataset}
	- mapping.txt
- hate
	- {dataset}
	- mapping.txt
- irony
	- {dataset}
	- mapping.txt
- offensive
	- {dataset}
	- mapping.txt
- sentiment
	- {dataset}
	- mapping.txt
- stance
	- abortion
		- {dataset}
	- atheism
		- {dataset}
	- climate
		- {dataset}
	- feminist
		- {dataset}
	- hilary
		- {dataset}
	mapping.txt

=== FILE FORMAT ===

Each {train/val/test}_text.txt file has one tweet per line in the original format, i.e., no preprocessing has been applied. Each {train/val/test}_labels.txt file has one label per line which maps to its corresponding tweet. The mapping.txt files contain tab-separated lines of the form 'label_id <tab> label_name', for example, for stance detection '0 <tab> 1', '1 <tab> against' and '2 <tab> favor'.

=== REFERENCES ===

Please check the main README for details about the main reference paper and the articles associated with each of the datasets
