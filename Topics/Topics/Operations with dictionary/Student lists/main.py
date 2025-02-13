import operator

# write your code here
student_count = {key: len(value) for (key, value) in student_list.items()}
student_count_sorted = dict(sorted(student_count.items(), key=operator.itemgetter(1), reverse=True))
print(list(student_count_sorted.keys())[0])
