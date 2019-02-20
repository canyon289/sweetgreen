"""Various tests to debug json cleaning and serialization process"""


def test_json_equality():
    """Determine why Buffalo Chicken product is not passing equality assertion"""
    proposed = {
        "asset_class": "image",
        "assetable_id": 260,
        "assetable_type": "Gravy::MasterProduct",
        "child_asset_ids": [6631, 6610, 6604],
        "content_type": "image/jpeg",
        "created_at": "2019-01-03T03:41:16.764Z",
        "file_name": "img_buffalochickencaesar@3x.jpg",
        "file_size": 4866227,
        "height": 3600,
        "id": 6603,
        "metadata": {
            "height": 3600,
            "read_url": "https://gravy-herd.s3.amazonaws.com/production/images/master/img_buffalochickencaesar%403x.jpg",
            "width": 5400,
        },
        "position": None,
        "transform_name": None,
        "type": "Herd::Image",
        "updated_at": "2019-01-03T03:41:16.764Z",
        "url": "//cdn-7.sweetgreen.com/production/images/master/img_buffalochickencaesar%403x.jpg",
        "width": 5400,
    }

    existing = {
        "asset_class": "image",
        "assetable_id": 260,
        "assetable_type": "Gravy::MasterProduct",
        "child_asset_ids": [6604, 6610, 6631],
        "content_type": "image/jpeg",
        "created_at": "2019-01-03T03:41:16.764Z",
        "file_name": "img_buffalochickencaesar@3x.jpg",
        "file_size": 4866227,
        "height": 3600,
        "id": 6603,
        "metadata": {
            "height": 3600,
            "read_url": "https://gravy-herd.s3.amazonaws.com/production/images/master/img_buffalochickencaesar%403x.jpg",
            "width": 5400,
        },
        "position": None,
        "transform_name": None,
        "type": "Herd::Image",
        "updated_at": "2019-01-03T03:41:16.764Z",
        "url": "//cdn-7.sweetgreen.com/production/images/master/img_buffalochickencaesar%403x.jpg",
        "width": 5400,
    }
    assert proposed == existing
