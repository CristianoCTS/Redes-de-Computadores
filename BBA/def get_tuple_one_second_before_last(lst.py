def get_tuple_one_second_before_last(lst):
    if len(lst) < 2:
        return None  # Not enough data to find a match

    last_time = lst[-1][0]  # Get the timestamp of the last tuple

    # Reverse the list and use next() to find the tuple with timestamp last_time - 1
    result = next((tup for tup in lst[::-1] if tup[0] < last_time - 1), None)
    
    return result

# Example usage
my_list = [(5.443563, 'data1'), (5.52453, 'data2'), (6.3254, 'data3'), (6.524755, 'data4'), (6.53546, 'data5')]
result = get_tuple_one_second_before_last(my_list)

if result:
    print(f"Tuple recorded 1 second before the last: {result}")
else:
    print("No tuple found 1 second before the last item.")
