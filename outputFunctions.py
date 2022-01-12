from conversionFunctions import MAX_COMBINATIONS, color_pair_to_string, get_color_from_pair_number

def get_printable_form():

  printable_form = "" # Create empty string to start writting on it
  for zero_based_pair_number in range(MAX_COMBINATIONS):
    pair_number = zero_based_pair_number + 1
    major_color, minor_color = get_color_from_pair_number(pair_number)
    colors_string = color_pair_to_string(major_color, minor_color)
    printable_form += "Pair no. "+str(pair_number) + " - " + colors_string + "\n"

  return printable_form[:-1] # Remove last \n before returning