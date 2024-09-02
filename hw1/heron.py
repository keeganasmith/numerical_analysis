import sys
sys.setrecursionlimit(20000)
MAX_DEPTH = 1000;
def heron_rec(num, approx, depth):
    if(depth >= MAX_DEPTH):
        return approx;

    next_approx = .5 * approx + .5 * (num / approx)
    return heron_rec(num, next_approx, depth  +1)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = heron_rec(num, num / 2, 1)
    print(f"sqrt of {num} is approx. {result}")