def main():
    height = int(input('What\'s Height ? '))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print('#' * (i + 1))

if __name__ == '__main__':
    main()