import time
import itertools

def eliminate_redundant(group):
    new_group = []
    for j in group:
        new=[]
        for i in j:
            if i not in new:
                new.append(i)
        new_group.append(new)
    return new_group

def eliminate_redundant_list(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

def verify_empty(group):

    if len(group) == 0:
        return True

    else:
        count = 0
        for i in group:
            if i:
                count+=1
        if count == 0:
            return True
    return False

def prime_search(Chart):
    prime = []
    for col in range(len(Chart[0])):
        count = 0
        pos = 0
        for row in range(len(Chart)):

            if Chart[row][col] == 1:
                count += 1
                pos = row

        if count == 1:
            prime.append(pos)

    return prime

def all_zero_check(Chart):
    for i in Chart:
        for j in i:
            if j != 0:
                return False
    return True

def find_max(l):
    max = -1
    index = 0
    for i in range(len(l)):
        if l[i] > max:
            max = l[i]
            index = i
    return index

def multiply(list1, list2):
    list_result = []

    if len(list1) == 0 and len(list2)== 0:
        return list_result

    elif len(list1)==0:
        return list2

    elif len(list2)==0:
        return list1

    else:
        for i in list1:
            for j in list2:

                if i == j:
                    list_result.append(i)
                
                else:
                    list_result.append(list(set(i+j)))

        
        list_result.sort()
        return list(list_result for list_result,_ in itertools.groupby(list_result))

def min_cost_calculation(Chart, unchecked):
    P_final = []
    
    essential_prime = prime_search(Chart)
    essential_prime = eliminate_redundant_list(essential_prime)

    if len(essential_prime) > 0:
        s = "\nEssential Prime Implicants :\n"
        for i in range(len(unchecked)):
            for j in essential_prime:
                if j == i:
                    s += change_to_letter(unchecked[i]) + ' , '
        print(s[:(len(s) - 3)])

        for i in essential_prime:
            for col in range(len(Chart[0])):
                if Chart[i][col] == 1:
                    for row in range(len(Chart)):
                        Chart[row][col] = 0

    if all_zero_check(Chart):
        P = [essential_prime]
        P_cost = []
        
        for prime in P:
            count = 0
            for i in range(len(unchecked)):
                for j in prime:
                    if j == i:
                        count += calculate_literal(unchecked[i])
            P_cost.append(count)

        for i in range(len(P_cost)):
            if P_cost[i] == min(P_cost):
                P_final.append(P[i])

    return P_final
                
def compare_binary(s1,s2):
    count = 0
    pos = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count+=1
            pos = i
    if count == 1:
        return True, pos
    else:
        return False, None

def compare_binary_same(term,number):
    for i in range(len(term)):
        if term[i] != '-':
            if term[i] != number[i]:
                return False
    return True

def pair_combination(group, unchecked):

    l = len(group) - 1

    check_list = []

    next_group = [[] for x in range(l)]

    for i in range(l):

        for elem1 in group[i]:
            for elem2 in group[i + 1]:
                b, pos = compare_binary(elem1, elem2)
                if b is True:
                    check_list.append(elem1)
                    check_list.append(elem2)
                    new_elem = list(elem1)
                    new_elem[pos] = '-' 
                    new_elem = "".join(new_elem) 
                    next_group[i].append(new_elem)
    for i in group:
        for j in i:
            if j not in check_list:
                unchecked.append(j)

    return next_group, unchecked

def calculate_literal(s):
    count = 0
    for i in range(len(s)):
        if s[i] != '-':
            count+=1

    return count

def change_to_letter(s):
    out = ''
    c = 'a'
    more = False
    n = 0
    for i in range(len(s)):

        if more == False:
            if s[i] == '1':
                out = out + c
            elif s[i] == '0':
                out = out + c+'\''

        if more == True:
            if s[i] == '1':
                out = out + c + str(n)
            elif s[i] == '0':
                out = out + c + str(n) + '\''
            n+=1

        if c=='z' and more == False:
            c = 'A'
        elif c=='Z':
            c = 'a'
            more = True

        elif more == False:
            c = chr(ord(c)+1)
    return out

def main(n_var, minterms):
    a = minterms.split()
    a = list(map(int, a))

    group = [[] for x in range(n_var + 1)]

    for i in range(len(a)):
        a[i] = bin(a[i])[2:]
        if len(a[i]) < n_var:
            for j in range(n_var - len(a[i])):
                a[i] = '0' + a[i]
        elif len(a[i]) > n_var:
            print('\nError : Choose the correct number of variables(bits)\n')
            return
        index = a[i].count('1')
        group[index].append(a[i])

    all_group = []
    unchecked = []
    while verify_empty(group) == False:
        all_group.append(group)
        next_group, unchecked = pair_combination(group, unchecked)
        group = eliminate_redundant(next_group)

    s = "\nPrime Implicants :\n"
    for i in unchecked:
        s = s + change_to_letter(i) + " , "
    print(s[:(len(s) - 3)])

    Chart = [[0 for x in range(len(a))] for x in range(len(unchecked))]
    for i in range(len(a)):
        for j in range(len(unchecked)):
            if compare_binary_same(unchecked[j], a[i]):
                Chart[j][i] = 1

    primes = min_cost_calculation(Chart, unchecked)
    primes = eliminate_redundant(primes)
    print("\n--  Answers --\n")
    for prime in primes:
        s = ''
        for i in range(len(unchecked)):
            for j in prime:
                if j == i:
                    s = s + change_to_letter(unchecked[i]) + ' + '
        print(s[:(len(s) - 3)])

if __name__ == "__main__":
    try:
        with open("testfile.txt", "r") as file:
            content = file.readline().strip().split()
            n_var = int(content[0]) 
            minterms = " ".join(content[1:]) 
    except FileNotFoundError:
        print("File testfile.txt tidak ditemukan. Pastikan file ada di direktori yang benar.")
        exit()

    start_time = time.time()
    main(n_var, minterms)
    print("Time elapsed: {:.2f}ms".format((time.time() - start_time) * 1000))
