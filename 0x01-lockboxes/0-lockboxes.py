def canUnlockAll(boxes):
    # Initialization
    keychain = []
    opened_boxes = [False for _ in range(len(boxes))]
    opened_count = 0
    
    # Start
    keychain += boxes[0]
    opened_boxes[0] = True
    opened_count += 1

    # Iterate
    for k in keychain:
        if k < len(boxes) and not opened_boxes[k]:
            keychain += boxes[k]
            opened_boxes[k] = True
            opened_count += 1

    # Success or Failure
    if opened_count == len(boxes):
        return True
    return False

