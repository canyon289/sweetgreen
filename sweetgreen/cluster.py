"""
Clustering Analysis for Sweetgreen restaurant locations

Location count and name taken from https://www.sweetgreen.com/menu/
"""

from sklearn import cluster
from sklearn import preprocessing

# This was hand coded after manual observation of clustering results
CLUSTER_MAP = {
    0: "New York",
    1: "Los Angeles",
    2: "Chicago",
    3: "DC, MD, VA",
    4: "Bay Area",
    5: "Boston",
    6: "Philly",
}


def location_clustering(restaurant_df, clusters=7):
    """K means clustering of restaurants and outposts by geographical location

    Notes
    -----
    Through visual analysis its pretty clear k means clustering should
    work well. Verification can be done manually. Random state set for reproducibility

    Parameters
    ----------
    restaurant_df: pd.DataFrame
        Data frame of restaurants. Must include latitude and longitude columns

    clusters: int, opt
        Number of location clusters. Defaults to 7 because that's how many sweetgreen lists
        on their menu webpage


    Returns
    -------
    cluster_ids: nd.Array
        An array of predicted cluster_id for each restaurant row
    """
    lat_long = restaurant_df[["latitude", "longitude"]].values
    unit_scaler = preprocessing.MinMaxScaler()

    scaled_lat_long = unit_scaler.fit_transform(lat_long)
    cluster_id = cluster.KMeans(n_clusters=7, random_state=0).fit_predict(
        scaled_lat_long
    )

    return cluster_id
