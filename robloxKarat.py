'''
You're developing a system for scheduling advising meetings with students in a Computer Science program.
Each meeting should be scheduled when a student has completed 50% of their academic program.

Each course at our university has at most one prerequisite that must be taken first.
No two courses share a prerequisite. There is only one path through the program.

Write a function that takes a list of (prerequisite, course) pairs, and returns the name of the course that the student will be taking when they are halfway through their program. (If a track has an even number of courses, and therefore has two "middle" courses, you should return the first one.)

Sample input 1: (arbitrarily ordered)
prereqs_courses1 = [
	["Foundations of Computer Science", "Operating Systems"],
	["Data Structures", "Algorithms"],
	["Computer Networks", "Computer Architecture"],
	["Algorithms", "Foundations of Computer Science"],
	["Computer Architecture", "Data Structures"],
	["Software Design", "Computer Networks"]
]

In this case, the order of the courses in the program is:
	Software Design
	Computer Networks
	Computer Architecture
	Data Structures
	Algorithms
	Foundations of Computer Science
	Operating Systems

Sample output 1:
	"Data Structures"


Sample input 2:
prereqs_courses2 = [
	["Data Structures", "Algorithms"],
	["Algorithms", "Foundations of Computer Science"],
	["Foundations of Computer Science", "Logic"]
]



Sample output 2:
	"Algorithms"

Sample input 3:
prereqs_courses3 = [
	["Data Structures", "Algorithms"],
]


Sample output 3:
	"Data Structures"

Complexity analysis variables:

n: number of pairs in the input

'''

student_course_pairs_1 = [
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
  ["58", "Software Design"],
]

def find_pairs(student_course_pairs_1):
    store = {}
    for elem in student_course_pairs_1:
        idd, subject = elem
#         print(idd, subject)
        store[idd] = store.get(idd, []) + [subject]
    output = {}
#     print(store.keys())
    store_list = list(store.keys())
#     print(f[0])
    for i in range(len(store_list)):
        for j in range(i+1, len(store_list)):
            key1, key2 = store_list[i], store_list[j]
#             print(key1, key2)
    #         print(set(store[key1]))
            val1 = set(store[key1])
            val2 = set(store[key2])
            res = val1.intersection(val2)
            output[key1 + "," + key2] = list(res)
#             print(output)
    return output
        
#         val1, val2 = set(store[key1]), set(store(key2))
#         print(val1, val2)
        
        
student_course_pairs_2 = [
  ["42", "Software Design"],
  ["0", "Advanced Mechanics"],
  ["9", "Art History"],
]

# print(find_pairs(student_course_pairs_2))

prereqs_courses1 = [
    ["Foundations of Computer Science", "Operating Systems"],
    ["Data Structures", "Algorithms"],
    ["Computer Networks", "Computer Architecture"],
    ["Algorithms", "Foundations of Computer Science"],
    ["Computer Architecture", "Data Structures"],
    ["Software Design", "Computer Networks"]
]

prereqs_courses2 = [
    ["Data Structures", "Algorithms"],
    ["Algorithms", "Foundations of Computer Science"],
    ["Foundations of Computer Science", "Logic"]
 ]

prereqs_courses3 = [
    ["Data Structures", "Algorithms"]
]


def find_pairs_2(prereqs_courses1):
    graph = {}; indegree = {}
    for a,b in prereqs_courses1:
        graph[a] = [b]
        if a not in indegree:
            indegree[a] = 0
        indegree[b] = indegree.get(b, 0) + 1
    source = [i for i in indegree if indegree[i] == 0][0]
    path = []
    print(source, graph)
    while source in graph:
        path += [source]
        source = graph[source]

    print(path)
    return path[len(path)//2]


print(find_pairs_2(prereqs_courses1))


def find_pairs_2_2(prereqs_courses1):
#     graph = {}
#     n=0
#     for c1, c2 in prereqs_courses1:
#         graph[c2] = graph.get(c2, []) + [c1]
#         n += abs
    
    graph = {}
    for a,b in prereqs_courses1:
        graph[a] = [b]
        graph[b] = [a]
    
    course = prereqs_courses1[0][0]
    
    res = []
    vis = set()
    def dfs(graph, course, res, vis):
        res += [course]
        vis.add(course)
        for child in graph.get(course, []):
            if child not in vis:
                dfs(graph, child, res, vis)
    allc = []
    for i,j in prereqs_courses1:
        if j not in allc:
            allc.append(j)
        if i not in allc:
            allc.append(i)
        
    print(allc)
    for course in allc:
        dfs(graph, course, res, vis)
    return res[len(res)//2]


# print(find_pairs_2(prereqs_courses1))

prereqs_courses2 = [
	["Data Structures", "Algorithms"],
	["Algorithms", "Foundations of Computer Science"],
	["Foundations of Computer Science", "Logic"]
]
print(find_pairs_2(prereqs_courses2))

prereqs_courses3 = [
	["Data Structures", "Algorithms"],
]
print(find_pairs_2(prereqs_courses3))