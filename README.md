# TweetEval
This is the repository for the [_TweetEval_ benchmark (Findings of EMNLP 2020)](https://arxiv.org/pdf/2010.12421.pdf). _TweetEval_ consists of seven heterogenous tasks in Twitter, all framed as multi-class tweet classification. All tasks have been unified into the same benchmark, with each dataset presented in the same format and with fixed training, validation and test splits.

# TweetEval: The Benchmark

These are the seven datasets of TweetEval, with its corresponding labels (more details about the format in the [datasets](https://github.com/cardiffnlp/tweeteval/tree/main/datasets) directory):

- **Emotion Recognition**: [SemEval 2018 (Emotion Recognition)](https://www.aclweb.org/anthology/S18-1001/) - 4 labels: `anger`, `joy`,`sadness`, `optimism`

- **Emoji Prediction**, [SemEval 2018 (Emoji Prediction)](https://www.aclweb.org/anthology/S18-1003.pdf) - 20 labels: :heart:, :heart_eyes:, :joy:  `...` :evergreen_tree:, :camera:, :stuck_out_tongue_winking_eye:

- **Irony Detection**, [SemEval 2018 (Irony Detection)](https://www.aclweb.org/anthology/S18-1005.pdf) - 2 labels: `irony`, `not irony`

- **Hate Speech Detection**, [SemEval 2019 (Hateval)](https://www.aclweb.org/anthology/S19-2007.pdf) - 2 labels: `hateful`, `not hateful`
  
- **Offensive Language Identification**, [SemEval 2019 (OffensEval)](https://www.aclweb.org/anthology/S19-2010/) - 2 labels: `offensive`, `not offensive`

- **Sentiment Analysis**, [SemEval 2017 (Sentiment Analysis in Twitter)](https://www.aclweb.org/anthology/S17-2088/) - 3 labels: `positive`, `neutral`, `negative`

- **Stance Detection***, [SemEval 2016 (Detecting Stance in Tweets)](https://www.aclweb.org/anthology/S16-1003/) - 3 labels: `favour`, `neutral`, `against`

**Note***: For stance there are five different target topics (Abortion, Atheism, Climate change, Feminism and Hillary Clinton), each of which contains its own training, validation and test data.

# TweetEval: Leaderboard (Test set)

| Model | Emoji | Emotion | Hate | Irony | Offensive | Sentiment | Stance | ALL(TE) | Reference |
|----------|------:|--------:|-----:|------:|----------:|----------:|-------:|----:|---------|
| RoBERTa-Retrained   | 31.4     | 78.5       | 52.3    | 61.7     | 80.5         | 72.6         | 69.3     | **65.2**  | [TweetEval](https://arxiv.org/pdf/2010.12421.pdf) |
| RoBERTa-Base   | 30.9     | 76.1       | 46.6    | 59.7     | 79.5         | 71.3         | 68      | 61.3  | [TweetEval](https://arxiv.org/pdf/2010.12421.pdf) |
| RoBERTa-Twitter   | 29.3     | 72.0       | 49.9    | 65.4     | 77.1         | 69.1        | 66.7     | 61.0  | [TweetEval](https://arxiv.org/pdf/2010.12421.pdf) |
| FastText | 25.8     | 65.2       | 50.6    | 63.1     | 73.4         | 62.9         | 65.4      | 58.1 | [TweetEval](https://arxiv.org/pdf/2010.12421.pdf) |
| LSTM      | 24.7     | 66.0       | 52.6    | 62.8     | 71.7         | 58.3         | 59.4      | 56.5 | [TweetEval](https://arxiv.org/pdf/2010.12421.pdf) |
| SVM      | 29.3     | 64.7       | 36.7    | 61.7     | 52.3         | 62.9         | 67.3      | 53.5 | [TweetEval](https://arxiv.org/pdf/2010.12421.pdf) |

**Note***: Check the [reference paper](https://arxiv.org/pdf/2010.12421.pdf) for details on the official metrics for each task

If you would like to have your results added to the leaderboard you can either submit a pull request or send an email to any of the paper authors with results and the predictions of your model. Please also submit a reference to a paper describing your approach.

# Evaluating your system

For evaluating your system, you simply need an individual predictions file for each of the tasks. The format of the predictions file should be the same as the output examples in the predictions folder (one output label per line as per the original test file). The predictions included as an example in this repo correspond to the best model evaluated in the paper, i.e., RoBERTa re-trained on Twitter (RoB-Rt in the paper).  

### Example usage

```bash
python evaluation_script.py
```
The script takes the TweetEval gold test labels and the predictions from the "predictions" folder by default, but you can set this to suit your needs as optional arguments.

### Optional arguments

Three optional arguments can be modified: 

*--tweeteval_path*: Path to TweetEval datasets. Default: *"./datasets/"*

*--predictions_path*: Path to predictions directory. Default: *"./predictions/"*

*--task*: Use this to get single task detailed results *(emoji|emotion|hate|irony|offensive|sentiment|stance)*. Default: ""

Evaluation script sample usage from the terminal with parameters:

```bash
python evaluation_script.py --tweeteval_path ./datasets/ --predictions_path ./predictions/ --task emoji
```
(this script would output the breakdown of the results for the emoji prediction task only)

# Pre-trained models and code

You can download the best Twitter masked language model (RoBERTa-retrained in the paper) from 🤗HuggingFace [here](https://huggingface.co/cardiffnlp/twitter-roberta-base). We also provide task-specific models:

- [Twitter-RoBERTa-emoji](https://huggingface.co/cardiffnlp/twitter-roberta-base-emoji)
- [Twitter-RoBERTa-emotion](https://huggingface.co/cardiffnlp/twitter-roberta-base-emotion)
- [Twitter-RoBERTa-hate](https://huggingface.co/cardiffnlp/twitter-roberta-base-hate)
- [Twitter-RoBERTa-irony](https://huggingface.co/cardiffnlp/twitter-roberta-base-irony)
- [Twitter-RoBERTa-offensive](https://huggingface.co/cardiffnlp/twitter-roberta-base-offensive)
- [Twitter-RoBERTa-sentiment](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment)
- Twitter-RoBERTa-stance - Coming soon

To know how to use the pre-trained models, you can check our [Google Colab Notebook](https://colab.research.google.com/drive/18cNn4cJ-bAi-Luiqi8V6c09Tj-iiX0oG?authuser=2), with sample code for masked language modeling, extracting embeddings from tweets and tweet classification.

# Citing TweetEval

If you use TweetEval in your research, please use the following `bib` entry to cite the [reference paper](https://arxiv.org/pdf/2010.12421.pdf).

```
@inproceedings{barbieri2020tweeteval,
  title={{TweetEval:Unified Benchmark and Comparative Evaluation for Tweet Classification}},
  author={Barbieri, Francesco and Camacho-Collados, Jose and Espinosa-Anke, Luis and Neves, Leonardo},
  booktitle={Proceedings of Findings of EMNLP},
  year={2020}
}
```
# License

TweetEval is released without any restrictions but restrictions may apply to individual tasks (which are derived from existing datasets) or Twitter (main data source). We refer users to the original licenses accompanying each dataset and Twitter regulations.


# Citing TweetEval datasets

If you use any of the TweetEval datasets, please cite their original publications:

#### Emotion Recognition:
```
@inproceedings{mohammad2018semeval,
  title={Semeval-2018 task 1: Affect in tweets},
  author={Mohammad, Saif and Bravo-Marquez, Felipe and Salameh, Mohammad and Kiritchenko, Svetlana},
  booktitle={Proceedings of the 12th international workshop on semantic evaluation},
  pages={1--17},
  year={2018}
}

```
#### Emoji Prediction:
```
@inproceedings{barbieri2018semeval,
  title={Semeval 2018 task 2: Multilingual emoji prediction},
  author={Barbieri, Francesco and Camacho-Collados, Jose and Ronzano, Francesco and Espinosa-Anke, Luis and 
    Ballesteros, Miguel and Basile, Valerio and Patti, Viviana and Saggion, Horacio},
  booktitle={Proceedings of The 12th International Workshop on Semantic Evaluation},
  pages={24--33},
  year={2018}
}
```

#### Irony Detection:
```
@inproceedings{van2018semeval,
  title={Semeval-2018 task 3: Irony detection in english tweets},
  author={Van Hee, Cynthia and Lefever, Els and Hoste, V{\'e}ronique},
  booktitle={Proceedings of The 12th International Workshop on Semantic Evaluation},
  pages={39--50},
  year={2018}
}
```

#### Hate Speech Detection:
```
@inproceedings{basile-etal-2019-semeval,
    title = "{S}em{E}val-2019 Task 5: Multilingual Detection of Hate Speech Against Immigrants and Women in {T}witter",
    author = "Basile, Valerio  and Bosco, Cristina  and Fersini, Elisabetta  and Nozza, Debora and Patti, Viviana and
      Rangel Pardo, Francisco Manuel  and Rosso, Paolo  and Sanguinetti, Manuela",
    booktitle = "Proceedings of the 13th International Workshop on Semantic Evaluation",
    year = "2019",
    address = "Minneapolis, Minnesota, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/S19-2007",
    doi = "10.18653/v1/S19-2007",
    pages = "54--63"
}
```
#### Offensive Language Identification:
```
@inproceedings{zampieri2019semeval,
  title={SemEval-2019 Task 6: Identifying and Categorizing Offensive Language in Social Media (OffensEval)},
  author={Zampieri, Marcos and Malmasi, Shervin and Nakov, Preslav and Rosenthal, Sara and Farra, Noura and Kumar, Ritesh},
  booktitle={Proceedings of the 13th International Workshop on Semantic Evaluation},
  pages={75--86},
  year={2019}
}
```

#### Sentiment Analysis:
```
@inproceedings{rosenthal2017semeval,
  title={SemEval-2017 task 4: Sentiment analysis in Twitter},
  author={Rosenthal, Sara and Farra, Noura and Nakov, Preslav},
  booktitle={Proceedings of the 11th international workshop on semantic evaluation (SemEval-2017)},
  pages={502--518},
  year={2017}
}
```

#### Stance Detection:
```
@inproceedings{mohammad2016semeval,
  title={Semeval-2016 task 6: Detecting stance in tweets},
  author={Mohammad, Saif and Kiritchenko, Svetlana and Sobhani, Parinaz and Zhu, Xiaodan and Cherry, Colin},
  booktitle={Proceedings of the 10th International Workshop on Semantic Evaluation (SemEval-2016)},
  pages={31--41},
  year={2016}
}
```
