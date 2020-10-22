# TweetEval
This is the repository for the _TweetEval_ benchmark[1]. _TweetEval_ consists of seven heterogenous tasks in Twitter, all framed as multi-class tweet classification. All tasks have been unified into the same benchmark, with each dataset presented in the same format and with fixed training, validation and test splits.

# TweetEval: Datasets

In the following we present the seven datasets of TweetEval, and its corresponding labels:

- **Emotion Recognition**: _Mohammad, S., Bravo-Marquez, F., Salameh, M., & Kiritchenko, S. (2018, June). Semeval-2018 task 1: Affect in tweets. In Proceedings of the 12th international workshop on semantic evaluation (pp. 1-17)._

  - [x] `anger`
  - [x] `joy`
  - [x] `sadness`
  - [x] `optimism`

- **Emoji Prediction**, [SemEval 2018 (Emoji Prediction)](https://www.aclweb.org/anthology/S18-1003.pdf): 

- **Irony Detection**, [SemEval 2018 (Irony Detection)](https://www.aclweb.org/anthology/S18-1005.pdf): True and False

- **Hate Speech Detection**, [SemEval 2019 (Hateval)](https://www.aclweb.org/anthology/S19-2007.pdf)

- **Offensive Language Identification**, SemEval 2019 (OffensEval)

- **Sentiment Analysis**, SemEval 2017 (Sentiment Analysis in Twitter)

- **Stance Detection***, SemEval 2016 (Detecting Stance in Tweets)

* Note: For stance there are five different target words (Abortion, Atheism, Climate change, Feminism and Hillary Clinton), each of which contains its own training, validation and test data.

# TweetEval: Leaderboard

TODO: Add table with leaderboard



# Evaluating your system

For evaluating your system, you simply need a prediction file with the same format as the output example XXX. This is, you would need a prediction file for each task......

# Citing TweetEval

If you use TweetEval in your research, please use the following `bib` entry.

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

TODO: Add bibfiles for each task

Hate Speech:
```
@inproceedings{basile-etal-2019-semeval,
    title = "{S}em{E}val-2019 Task 5: Multilingual Detection of Hate Speech Against Immigrants and Women in {T}witter",
    author = "Basile, Valerio  and
      Bosco, Cristina  and
      Fersini, Elisabetta  and
      Nozza, Debora  and
      Patti, Viviana  and
      Rangel Pardo, Francisco Manuel  and
      Rosso, Paolo  and
      Sanguinetti, Manuela",
    booktitle = "Proceedings of the 13th International Workshop on Semantic Evaluation",
    year = "2019",
    address = "Minneapolis, Minnesota, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/S19-2007",
    doi = "10.18653/v1/S19-2007",
    pages = "54--63"
}
```
