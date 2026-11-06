import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    if y is None:
        return 0.0

    labels_num = len(y)
    classes = {}
    for label in y:
        classes[label] = classes.get(label, 0) + 1
    print(classes)

    classes_p = np.asarray([class_num / labels_num for class_num in classes.values()])
    print(classes_p)
    entropy = -np.sum(classes_p @ np.log2(classes_p))
    return entropy