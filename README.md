# Bengli Female VS Male Names Dataset

An NLP dataset that contains 2030 data samples of bengli names and corresponding gender both for female and male. This is a very small and simple toy dataset that can be used by NLP starters to practice sequence classification problem and other NLP problems like gender recognition from names.

# Background

In Bengli language, name of a person is dependent largely on their gender. Normally, name of a female ends with certain type of suffix "A", "I", "EE" ["আ", "ই", "ঈ"]. And the names of male are significantly different from female in terms of phoneme patterna and ending suffix. So, In my observation their is a significant possibility that these difference in patterns can be used for gender classification based on names.

## Dataset Format

The dataset is in CSV format. There are two columns- namely 
1. Name
2. Gender

Each row has two attributes. First one is name, second one is the gender. The name attribute is in ```utf-8``` encoding. And the second attribute i.e. the gender attribute has been signified by 0 and 1 as 

|   |   |
|---|---|
|male| 0|
|female| 1|
|   |   |


## Dataset Statistics

The number of samples per class is as bellow-

|   |   |
|---|---|
|male| 1029|
|female| 1001|
|   |   |

## Possible Use Cases

1. Sequence Classificaion using RNN, LSTM etc
2. Sequence modeling using other type of machine learning algorithms
3. Gender recognition based on names


## Contribute

If you feel to contribute to this dataset, you are welcome to contribute in the following ways-
1. Can add more data samples in the dataset. If you want to add more samples in the dataset, then add your data to the ```female.txt``` and ```male.txt``` file using newlines and send a pull request. I will merge your update to the csv file.

2. You can also created notebooks for different use cases using this dataset and put your notebook in the notebook directory and send a pull request.