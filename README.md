# maes
Automated Essay Scoring with Shallow Linguistic Features

### Branch descriptions
**`master` branch:**
- with feature extractions using EASE
- with score predictions using three methodologies (SVM, Human, BLRR)
- last update: 17/Dec/2020

**`v1` branch:**
- with feature extractions using EASE
- with score predictions using three methodologies (SVM, Human, BLRR)
- **maintainer: [@ikttan](https://github.com/ikttan)**

**`v2` branch:**
- to be added with domain adaptation
- to be added consensus reaching for two or more of the above mentioned methodologies within an acceptable margin
- **maintainer: [@itsjunqing](https://github.com/itsjunqing)**

### Update as of 27 Dec 2020
- added `features_csv_generator.ipynb`: notebook that generates csv files for all sets' features
- added `features` directory: contains the csv files of all sets' features
- added `qwk_scores_without_da.ipynb`: notebook that compiles all QWK scores without domain adaptation (da), obtained from `maes.ipynb`
- added `qwk_scores_with_da.ipynb`: notebook that compiles all QWK scores with domain adaptation (da), added the voting ensemble within a margin but domain adaptation not implemented yet

*Domain Adaptation requires further discussion as it has many possible implementations*
