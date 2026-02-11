def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    # Write code here
    return [x[0]*x[1]/(x[1] + min_votes) + global_mean*min_votes/(x[1] + min_votes) for x in items]