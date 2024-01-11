#!/usr/bin/python3
"""canUnlockAll module"""


def canUnlockAll(boxes):
    """canUnlockAll function
    Args:
        boxes (List[List[int]]): list of lists
    Returns:
        bool: True if all boxes can be opened, else False
    """

    if len(boxes) == 0:
        return False

    if len(boxes) == 1:
        return True

    result = []
    result.append(0)
    req_indexs = []
    for i in boxes[0]:
        result.append(i)
    for i in boxes:
        if len(i) != 0:
            req_indexs.append(boxes.index(i))
    for i in result:
        if i >= len(boxes):
            del result[result.index(i)]
            continue
        if len(boxes[i]) > 0:
            for j in boxes[i]:
                if j not in result:
                    result.append(j)
    for i in req_indexs:
        if i not in result:
            return False
    return True
