input_samples = [
    {
        'path': ('a', 'b', 'c1', 'd1'),
        'module': ['hypre'],
        'time': 10.0,
    },
    {
        'path': ('a', 'b', 'c2'),
        'module': ['mpi'],
        'time': 100.0,
    }
]

true_root = {
    "depth#path": 1,
    "time": 110.0,
    "module": [
        "mpi",
        "hypre"
    ],
    "parent_hash#path": 3527539,
    "path": [
        "a"
    ],
    "hash#path": 12418971936901571
}

true_tree = {
    "depth#path": 1,
    "time": 110.0,
    "module": [
        "mpi",
        "hypre"
    ],
    "parent_hash#path": 3527539,
    "path": [
        "a"
    ],
    "children": [
        {
            "depth#path": 2,
            "time": 110.0,
            "module": [
                "mpi",
                "hypre"
            ],
            "parent_hash#path": 12418971936901571,
            "path": [
                "a",
                "b"
            ],
            "children": [
                {
                    "depth#path": 3,
                    "time": 100.0,
                    "module": [
                        "mpi"
                    ],
                    "parent_hash#path": -3816799034373630758,
                    "path": [
                        "a",
                        "b",
                        "c2"
                    ],
                    "hash#path": 6381261120127002631
                },
                {
                    "depth#path": 3,
                    "time": 10.0,
                    "module": [
                        "hypre"
                    ],
                    "parent_hash#path": -3816799034373630758,
                    "path": [
                        "a",
                        "b",
                        "c1"
                    ],
                    "children": [
                        {
                            "depth#path": 4,
                            "time": 10.0,
                            "module": [
                                "hypre"
                            ],
                            "parent_hash#path": 6381261120130497778,
                            "path": [
                                "a",
                                "b",
                                "c1",
                                "d1"
                            ],
                            "hash#path": 5741758759063404953
                        }
                    ],
                    "hash#path": 6381261120130497778
                }
            ],
            "hash#path": -3816799034373630758
        }
    ],
    "hash#path": 12418971936901571
}

true_hot_path = [
    {
        "depth#path": 1,
        "time": 110.0,
        "module": [
            "mpi",
            "hypre"
        ],
        "parent_hash#path": 3527539,
        "path": [
            "a"
        ],
        "hash#path": 12418971936901571
    },
    {
        "depth#path": 2,
        "time": 110.0,
        "module": [
            "mpi",
            "hypre"
        ],
        "parent_hash#path": 12418971936901571,
        "path": [
            "a",
            "b"
        ],
        "hash#path": -3816799034373630758
    },
    {
        "depth#path": 3,
        "time": 100.0,
        "module": [
            "mpi"
        ],
        "parent_hash#path": -3816799034373630758,
        "path": [
            "a",
            "b",
            "c2"
        ],
        "hash#path": 6381261120127002631
    }
]

true_scaled_tree = {
    "depth#path": 1,
    "time": 1100.0,
    "module": [
        "mpi",
        "hypre"
    ],
    "parent_hash#path": 3527539,
    "path": [
        "a"
    ],
    "children": [
        {
            "depth#path": 2,
            "time": 1100.0,
            "module": [
                "mpi",
                "hypre"
            ],
            "parent_hash#path": 12418971936901571,
            "path": [
                "a",
                "b"
            ],
            "children": [
                {
                    "depth#path": 3,
                    "time": 1000.0,
                    "module": [
                        "mpi"
                    ],
                    "parent_hash#path": -3816799034373630758,
                    "path": [
                        "a",
                        "b",
                        "c2"
                    ],
                    "hash#path": 6381261120127002631
                },
                {
                    "depth#path": 3,
                    "time": 100.0,
                    "module": [
                        "hypre"
                    ],
                    "parent_hash#path": -3816799034373630758,
                    "path": [
                        "a",
                        "b",
                        "c1"
                    ],
                    "children": [
                        {
                            "depth#path": 4,
                            "time": 100.0,
                            "module": [
                                "hypre"
                            ],
                            "parent_hash#path": 6381261120130497778,
                            "path": [
                                "a",
                                "b",
                                "c1",
                                "d1"
                            ],
                            "hash#path": 5741758759063404953
                        }
                    ],
                    "hash#path": 6381261120130497778
                }
            ],
            "hash#path": -3816799034373630758
        }
    ],
    "hash#path": 12418971936901571
}
