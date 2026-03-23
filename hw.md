# Homework - Pytest Practice

Write the following functions in a separate Python file
and then write a **pytest** file that tests them

## Question 1

Below is the function code:

```python
def is_positive(num):
    return num > 0
```

Write **pytest** tests for this function

Your tests should check different cases such as:

* a positive number
* a negative number
* zero

## Question 2

Below is the function code:

```python
def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count
```

Write **pytest** tests for this function

Your tests should check different cases such as:

* a word with vowels
* a word with no vowels
* an empty string
* a word with uppercase letters

## Bonus ⭐

Ask **Copilot** to add **2–3 more test functions** for the two functions above

Then:

* review Copilot’s suggestions
* keep only correct tests
* run them with **pytest**

📧 **Submission email:**
**[pythonai200425+pytest@gmail.com](mailto:pythonai200425+pytest@gmail.com)**
