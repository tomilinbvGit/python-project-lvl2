def sort(old_k, new_k):
    shared_k = sorted(list(set(old_k + new_k)))
    return shared_k
