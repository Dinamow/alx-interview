from typing import List
"""canUnlockAll module"""


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """canUnlockAll function
    Args:
        boxes (List[List[int]]): list of lists
    Returns:
        bool: True if all boxes can be opened, else False
    """
    empty_boxes: int = 0
    if len(boxes) == 0:
        return False

    if len(boxes) == 1:
        return True

    result: List[int] = []

    for i in boxes[0]:
        result.append(i)

    for i in result:
        if len(boxes[i]) > 0:
            for j in boxes[i]:
                if j not in result:
                    result.append(j)
        else:
            empty_boxes += 1
    if len(result) == len(boxes) - empty_boxes:
        return True
    return False