from hatchet.forest import Forest, Tree
import forest_tests_truths

import pandas as pd
import json
import pytest


def test_forest():
    forest = Forest.from_samples(forest_tests_truths.input_samples, 'path', {'time': 'sum', 'module': 'sum'})

    assert(json.dumps(forest.to_json(), sort_keys=True) ==
           json.dumps([forest_tests_truths.true_tree], sort_keys=True))

    roots = forest.roots()

    assert(len(roots) == 1)
    assert(json.dumps(roots[0].to_dict(), sort_keys=True) ==
           json.dumps(forest_tests_truths.true_root, sort_keys=True))

    tree = Tree(roots[0])

    assert(json.dumps(tree.to_json(), sort_keys=True) ==
           json.dumps(forest_tests_truths.true_tree, sort_keys=True))

    hot_path = [node.to_dict() for node in tree.hot_path('time')]

    assert(json.dumps(hot_path, sort_keys=True) ==
           json.dumps(forest_tests_truths.true_hot_path, sort_keys=True))

    # When modifying samples, the inclusive tree should update
    forest.df_samples['time'] = forest.df_samples['time'] * 10.0

    assert(json.dumps(forest.to_json(), sort_keys=True) ==
           json.dumps([forest_tests_truths.true_scaled_tree], sort_keys=True))

    # Modifying the nodes directly should not be allowed
    with pytest.raises(Exception) as e:
        forest.df_nodes = pd.DataFrame([1, 2, 3])
