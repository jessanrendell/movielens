# movielens

Evaluating k-nearest neighbors and singular value decomposition techniques for collaborative filtering recommender systems

## Variables

*int* `userId`: the integer ID of the anonymized user  
*int* `movieId`: the integer ID of the movie  
*int* `rating`: integer rating ranging from 1 to 5 given by the user to the movie  
*int* `timestamp`: the number of seconds had elapsed since the Unix epoch until the user rated the movie  

## Files

Aside from `README.md`, the repository contains 1 subdirectory and 3 other files:

1. `ml-100k`, the folder which contains the MovieLens 100K dataset
1. `preprocessing.R`, the R script for validating the data
1. `movielens.ipynb`, the notebook in which the k-NN and SVD++ algorithms are implemented and compared
1. `movielens.html`, the exported HTML version of `movielens.ipynb` for browser-viewing

## Generating recommendations

To generate movie recommendations for a specific user:

1. Run `recommend.py`.
1. Enter the ID of the user for which you want to produce recommendations.
1. Enter the number of recommendations.

<br>

- - -

#### Code authorship

2022 © Jessan Rendell G. Belenzo

<br>

#### Terms of use

Licensed under the GNU General Public License v3.0. See [LICENSE](https://github.com/jessanrendell/movielens/blob/main/LICENSE).

<br>

## Acknowledgments

Hug, Nicolas. "[Surprise: A Python library for recommender systems.](https://surpriselib.com/)" Journal of Open Source Software 5.52 (2020): 2174.

Harper, F. Maxwell, and Joseph A. Konstan. "[The movielens datasets: History and context.](https://grouplens.org/datasets/movielens/100k/)" Acm transactions on interactive intelligent systems (tiis) 5.4 (2015): 1-19.

Ricci, Francesco, Lior Rokach, and Bracha Shapira. "[Recommender systems handbook.](https://link.springer.com/chapter/10.1007/978-0-387-85820-3_1)" Springer, Boston, MA, 2011. 1-35.

Koren, Yehuda. "[Factorization meets the neighborhood: a multifaceted collaborative filtering model.](https://dl.acm.org/doi/abs/10.1145/1401890.1401944)" Proceedings of the 14th ACM SIGKDD international conference on Knowledge discovery and data mining. 2008.
