if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list2= list(set(arr))
    list2.sort(reverse=True)
    print(list2[1])
