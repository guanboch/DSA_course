# Types of Binary Trees

## By Structure

### Full Binary Tree
Every node has either **0 or 2 children** — never 1.

```
      1
     / \
    2   3
   / \
  4   5
```

---

### Complete Binary Tree
All levels are fully filled except possibly the last, which is filled **left to right**.

```
      1
     / \
    2   3
   / \  /
  4   5 6
```

> Used in heaps.

---

### Perfect Binary Tree
All internal nodes have exactly 2 children and all leaves are at the **same level**.

```
      1
     / \
    2   3
   / \ / \
  4  5 6  7
```

> Has exactly `2^h - 1` nodes where `h` is height.

---

### Balanced Binary Tree
The height difference between left and right subtrees of **every node** is at most 1.

```
      1
     / \
    2   3
   /
  4
```

> Guarantees O(log N) operations. AVL trees and Red-Black trees enforce this.

---

### Degenerate (Skewed) Tree
Every node has only **one child** — essentially a linked list.

```
1
 \
  2
   \
    3
     \
      4
```

> Worst case for most tree algorithms: O(N) height.

---

## By Ordering / Purpose

### Binary Search Tree (BST)
`left child < parent < right child` at every node.

```
      4
     / \
    2   6
   / \ / \
  1  3 5  7
```

> O(log N) search/insert on a balanced BST.

---

### AVL Tree
A **self-balancing BST** — automatically rotates to maintain balance after every insert/delete.

- Balance factor (height difference) at every node is kept at -1, 0, or 1.
- Guarantees O(log N) for all operations.

---

### Red-Black Tree
A **self-balancing BST** with color properties (red/black nodes) that guarantee O(log N) height.

- Used in most language standard libraries: Java `TreeMap`, C++ `std::map`.
- Less strictly balanced than AVL, so faster inserts/deletes.

---

### Heap (Min / Max)
A **complete binary tree** where every parent is smaller (min-heap) or larger (max-heap) than its children.

```
      1        ← min-heap
     / \
    3   2
   / \
  5   4
```

> O(1) access to min/max, O(log N) insert/delete. Used in priority queues.

---

## Quick Reference

| Type        | Key Property                     | Common Use              |
|-------------|----------------------------------|-------------------------|
| Full        | 0 or 2 children                  | Expression trees        |
| Complete    | Filled left-to-right             | Heaps                   |
| Perfect     | All levels full                  | Theoretical analysis    |
| Balanced    | Height diff ≤ 1                  | Efficient operations    |
| Degenerate  | One child only                   | Worst-case scenario     |
| BST         | Left < root < right              | Search / sort           |
| AVL         | BST + auto-balance (strict)      | Frequent lookups        |
| Red-Black   | BST + color rules (relaxed)      | Language std libs       |
| Heap        | Parent ≤ / ≥ children            | Priority queues         |
