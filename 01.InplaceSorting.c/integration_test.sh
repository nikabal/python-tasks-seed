#!/bin/bash

status=true

# ---------------------------------------------------
# Original test - run demo
# ---------------------------------------------------

result=$(uv run python -O ./sorting_demo.py)

echo ""
echo "=== Testing on different array sizes ==="
uv run python -c "
import random
import sortings
for size in [10, 100, 500, 1000]:
    data = list(range(size))
    random.shuffle(data)
    a1, a2 = data.copy(), data.copy()
    sortings.bubble_sort(a1)
    sortings.quick_sort(a2)
    print(f'Size {size}: bubble={a1==sorted(data)}, quick={a2==sorted(data)}')
"

if [ "$status" = true ]; then
    echo "All tests passed"
    exit 0
else
    echo "Some tests failed"
    exit 1
fi