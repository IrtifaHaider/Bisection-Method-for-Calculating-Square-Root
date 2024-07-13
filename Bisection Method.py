def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')
    else:
        # Initialize the bounds for the bisection method
        low = 0
        high = max(1, square_target)
        root = None
        # Perform the bisection method for a maximum of max_iterations times
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2
            # Check if the square of the midpoint is close enough to the target
            if abs(square_mid - square_target) < tolerance:
                root = mid # Set the root to the midpoint
                break # Exit the loop
            elif square_mid < square_target:
                low = mid # Move the lower bound up to the midpoint
            else:
                high = mid  # Move the upper bound down to the midpoint

         # Check if the root was found within the allowed iterations
        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root

def main():
    N=int(input("Enter the number to calculate Square root:"))
    print(square_root_bisection(N))# Call the bisection function and print the result
main()

