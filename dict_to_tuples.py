def dict_to_tuples(in_dict):
    result = []
    for key in in_dict:
        result.append((key, in_dict[key]))
    return result

# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
#[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

print dict_to_tuples(my_dict)
