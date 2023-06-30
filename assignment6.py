def ds(roll_no, name):
  """
  This function adds the parameters roll_no and name to the following data structures:
  list, tuple, sets and dictionaries
  """

  # Create a list
  list = [roll_no, name]
  print("List : ",list)

  # Create a tuple
  tuple = (roll_no, name)
  print("Tupple : ", tuple)

  # Create a set
  set = {roll_no, name}
  print("Set : ",set)

  # Create a dictionary
  dict = {"roll_no": roll_no, "name": name}
  print("dictionary : ", dict)

  # Change the values during runtime
  list[0] = 1000
  tuple = (200, name)
  set.add(300)
  dict["roll_no"] = 400

  # Delete the data structures
  del list
  del tuple
  del set
  del dict

if __name__ == "__main__":
  # Call the function
  ds(17, "Gaurav Puri")
