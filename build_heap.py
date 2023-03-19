# python3
 
 
def build_heap(data):
    swaps = []
    n = len(data)
    
    for i in range(n // 2 - 1, -1, -1):
        j = i
        while True:
            o =2*j + 1
            if o >= n:
                break
            if o +1 < n and data[o + 1] < data[o]:
                o += 1
            if data[j] > data[o]:
                swaps.append((j, o))
                data[j], data[o] = data[o], data[j]
                j = o
            else:
                break  
  
    return swaps
 
 
def main():
    
    read_input = input()
    
    if read_input.startswith('I'):
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
            
    elif read_input.startswith('F'):
        file = input().strip()
        with open(f'tests/{file}', 'r') as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        
    else:
        print('Invalid character')
     
 
 
if __name__ == "__main__":
    main()
  
  #Igors Vlaskins 16.grupa
