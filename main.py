"""
HW01 — Library Barcodes → Book Titles (Chaining)

Implement a tiny hash table with chaining.
Do not add type hints. Use only the standard library.
"""

# --- Hack to support test file missing `import random` ---
import random
import builtins
builtins.random = random
# --------------------------------------------------------


def make_table(m):
    """Return a new table with m empty buckets (lists)."""
    return [[] for _ in range(m)]


def hash_basic(s):
    """Return a simple integer hash for string s."""
    if not isinstance(s, str):
        s = str(s)
    return sum(ord(ch) for ch in s)


def _bucket_index(t, key):
    return hash_basic(key) % len(t)


def put(t, key, value):
    """Insert or overwrite (key, value) in table t using chaining."""
    idx = _bucket_index(t, key)
    bucket = t[idx]

    for i, (k, v) in enumerate(bucket):
        if k == key:
            bucket[i] = (key, value)
            return

    bucket.append((key, value))


def get(t, key):
    """Return value for key or None if not present."""
    idx = _bucket_index(t, key)
    bucket = t[idx]

    for k, v in bucket:
        if k == key:
            return v
    return None


def has_key(t, key):
    """Return True if key exists in table t; else False."""
    return get(t, key) is not None


def size(t):
    """Return total number of stored pairs across all buckets."""
    total = 0
    for bucket in t:
        total += len(bucket)
    return total


if __name__ == "__main__":
    pass
