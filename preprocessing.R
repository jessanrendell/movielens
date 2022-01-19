# Load the MovieLens ratings dataset
MovieLens <- read.table('ml-100k/u.data')
names(MovieLens) <- c('userId', 'movieId', 'rating', 'timestamp')

# Check for NAs and NaNs
any(is.na(MovieLens))

# Check for floating-point numbers in userId and movieId
any(!is.integer(MovieLens$userId))
any(!is.integer(MovieLens$movieId))

# Check for ratings that fall outside the bounds
table(MovieLens$rating)

# Compute for sparsity
n_ratings <- dim(MovieLens)[1]
n_users <- dim(as.data.frame(unique(MovieLens$userId)))[1]
n_movies <- dim(as.data.frame(unique(MovieLens$movieId)))[1]
# About 6.3% of the ratings matrix are filled
sparsity <- n_ratings / (n_users * n_movies)
