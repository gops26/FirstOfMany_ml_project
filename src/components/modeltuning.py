params = {
    "random forest":{
        "n_estimators":[50,100,200,500,1000],
        "criterion":["squared_error", "absolute_error", "friedman_mse", "poisson"],
        "max_depth":[1,2,5,8,10],
        "max_features":["sqrt", "log2"]
    },
    "Decision tree regressor":{
        "criterion":["squared_error", "absolute_error", "friedman_mse", "poisson"],
        "max_depth":[1,2,5,8,10],
        "max_features":["sqrt", "log2"],
        # "n_estimators":[50,100,200,500,1000],

        
    },
    "ada boost": {
        "n_estimators":[50,100,200,500,1000],
        "loss":['linear', 'square', 'exponential'],
        'learning_rate':[0.01,0.1]
    },
    "ridge": {

    },
    "linear_model":{},
    "xgb regressor": {
        "n_estimators":[50,100,200,500,1000],
        "max_depth":[1,2,5,8,10],
        "learning_rate":[0.1,0.01]

    },
    "k nearest neighbor regressor":{
        "n_neighbors":[2,3,4,5,6],
        "algorithm":["ball_tree", "kd_tree", "brute"],
        "weights":["uniform", "distance"],
        "leaf_size":[10,20,30,40,50]
    }
}