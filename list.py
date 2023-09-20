'''def len_function(list1):
  """Returns the length of the list."""
  return len(list1)

def indexing_example(list1):
  """Prints the element at the given index in the list."""
  index = int(input("Enter the index of the element you want to print: "))
  print(list1[index])

def slicing_example(list1):
  """Prints a slice of the list."""
  start_index = int(input("Enter the start index of the slice: "))
  end_index = int(input("Enter the end index of the slice: "))
  print(list1[start_index:end_index])

def max_function(list1):
  """Returns the largest element in the list."""
  return max(list1)

def min_function(list1):
  """Returns the smallest element in the list."""
  return min(list1)

def pop_function(list1):
  """Removes and returns the last element in the list."""
  return list1.pop()

def remove_function(list1, element):
  """Removes the first occurrence of the given element from the list."""
  list1.remove(element)
'''
# Define list of names:

list1 = ["Durgesh", "Pawan", "KD", "Yaseen", "Mahendra"]
print(list1)
list1.append("Likhil")
print(list1)
list1.sort()
print(list1)