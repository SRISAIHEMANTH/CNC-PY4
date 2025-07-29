# list_dict_operations.py

from functools import reduce

# --- 1. Merge Lists ---
def merge_lists(list1, list2):
    return list1 + list2

# --- 2. Filter a List ---
def filter_list(input_list, condition):
    return list(filter(condition, input_list))

# --- 3. Transform a List ---
def transform_list(input_list, transformation):
    return list(map(transformation, input_list))

# --- 4. Merge Dictionaries ---
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

# --- 5. Filter a Dictionary ---
def filter_dict(input_dict, condition):
    return {key: value for key, value in input_dict.items() if condition(key, value)}

# --- 6. Transform a Dictionary ---
def transform_dict(input_dict, transformation):
    return {key: transformation(value) for key, value in input_dict.items()}

def main():
    # Lists to demonstrate merge, filter, and transform
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]

    # Merging lists
    merged_list = merge_lists(list1, list2)
    print(f"Merged List: {merged_list}")

    # Filtering even numbers from the merged list
    even_numbers = filter_list(merged_list, lambda x: x % 2 == 0)
    print(f"Filtered (Even Numbers): {even_numbers}")

    # Transforming (squared) the merged list
    squared_list = transform_list(merged_list, lambda x: x ** 2)
    print(f"Transformed (Squared Numbers): {squared_list}")

    # Dictionaries to demonstrate merge, filter, and transform
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"d": 4, "e": 5}

    # Merging dictionaries
    merged_dict = merge_dicts(dict1, dict2)
    print(f"Merged Dictionary: {merged_dict}")

    # Filtering dictionary to get items with values > 2
    filtered_dict = filter_dict(merged_dict, lambda k, v: v > 2)
    print(f"Filtered Dictionary (Values > 2): {filtered_dict}")

    # Transforming dictionary values to their squares
    transformed_dict = transform_dict(merged_dict, lambda v: v ** 2)
    print(f"Transformed Dictionary (Squared Values): {transformed_dict}")

if __name__ == "__main__":
    main()
