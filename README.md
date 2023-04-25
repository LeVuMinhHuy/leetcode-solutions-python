All credits belong to https://www.kaggle.com/datasets/erichartford/leetcode-solutions

I collected only python solutions:

```
id: <number>
code_with_data:
<
  # Slug
  # Title
  # Difficulty
  # Content
  Code Answer in Python
  # Explanation
>
code_only: < Code Answer in Python >
```

I'm using this for code generation so the data will have the format like above

You guys can use it from HuggingFace

```python
from datasets import load_dataset

dataset = load_dataset("mhhmm/leetcode-solutions-python")
```
